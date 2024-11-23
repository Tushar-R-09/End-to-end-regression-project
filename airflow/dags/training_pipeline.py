from __future__ import annotations
from textwrap import dedent
from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import training_pipeline


training_object = training_pipeline("insurance.csv")

with DAG(
    "insurance_training_pipeline",
    default_args={"retries":2},
    description = "A simple training pipeline",
    schedule = "@hourly",
    start_date = pendulum.datetime(2022, 1, 1, tz = "UTC"),
    catchup = False,
    tags = ["training"]
) as dag:
    
    dag.doc_md = __doc__

    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        train_path, test_path = training_object.start_data_ingestion()
        # Combine both paths into a dictionary
        paths = {"train_path": train_path, "test_path": test_path}

        # Push the dictionary to XCom
        ti.xcom_push("data_ingestion_artifacts", paths)  #cross communication between components


    def data_transformation(**kwargs):
        ti = kwargs["ti"]
        data_ingestion_artifacts = ti.xcom_pull(key="data_ingestion_artifacts", task_ids="data_ingestion_task")
        train_path = data_ingestion_artifacts["train_path"]
        test_path = data_ingestion_artifacts["test_path"]
        transformed_train_data_path, transformed_test_data_path = training_object.start_data_transformation(train_path, test_path)
        # Combine both paths into a dictionary
        paths = {"train_path": transformed_train_data_path, "test_path": transformed_test_data_path}

        # Push the dictionary to XCom
        ti.xcom_push("data_transformation_artifacts", paths)



    def model_trainer(**kwargs):
        ti = kwargs["ti"]
        data_transformation_artifacts = ti.xcom_pull(key="data_transformation_artifacts", task_ids="data_transformation_task")
        train_path = data_transformation_artifacts["train_path"]
        test_path = data_transformation_artifacts["test_path"]
        training_object.start_model_training(train_path, test_path)

    
    data_ingestion_task = PythonOperator(
        task_id = "data_ingestion_task",
        python_callable = data_ingestion
    )

    data_transformation_task = PythonOperator(
        task_id = "data_transformation_task",
        python_callable = data_transformation
    )

    model_trainer_task = PythonOperator(
        task_id = "model_trainer_task",
        python_callable = model_trainer
    )

    data_ingestion_task >> data_transformation_task >> model_trainer_task

         


