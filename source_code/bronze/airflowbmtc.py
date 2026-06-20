from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "raghu",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["raghu@email.com"]
}

with DAG(
    dag_id="bmtc_data_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval="0 6 * * *",  # Daily at 6 AM
    catchup=False,
    tags=["bmtc", "data-engineering"]
) as dag:

    def run_bronze(**kwargs):
        # In production: trigger Databricks notebook
        print("Bronze ingestion: loading raw BMTC CSV to Delta")

    def run_silver(**kwargs):
        print("Silver transform: cleaning and validating data")

    def run_gold(**kwargs):
        print("Gold aggregation: building route and city metrics")

    def run_quality_checks(**kwargs):
        print("Quality checks: validating row counts and nulls")

    bronze = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=run_bronze
    )

    silver = PythonOperator(
        task_id="silver_transform",
        python_callable=run_silver
    )

    gold = PythonOperator(
        task_id="gold_aggregation",
        python_callable=run_gold
    )

    quality = PythonOperator(
        task_id="quality_checks",
        python_callable=run_quality_checks
    )

    # Pipeline dependency chain
    bronze >> silver >> gold >> quality