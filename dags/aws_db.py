from airflow import DAG

from aws import rds_demo

from aws.helpers import connection,create_db

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.operators.python import PythonOperator



default_args={
    "owner":"app_migrtaion",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}

def call_func():
    rds_demo.RdsInstanceScenario.run_crete_db("demo")
with DAG(
    dag_id="RDS_DB",
    default_args=default_args,
    description="RDS POSTGRES",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,20)

)as dag:
    # task1=PythonOperator(
    #     task_id="rds_db_Instance_creation",
    #     python_callable=call_func,
    # )
    
    task2=PythonOperator(
        task_id="get_connection",
        python_callable=connection.get_name
    )
    task3=PythonOperator(
        task_id="db_creation",
        python_callable=create_db.create_databses
    )
    
    # task1>>task2
    task2>>task3