from airflow import DAG

from aws import rds_demo

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.operators.python import PythonOperator



default_args={
    "owner":"app_migrtaion",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
def get_name(ti):
    url,Port=rds_demo.RdsInstanceScenario.get_connection("demo")

    ti.xcom_push(key="url",value=url)
    ti.xcom_push(key="Port",value=Port)
    
    
with DAG(
    dag_id="push_connection",
    default_args=default_args,
    description="RDS push",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,20)

)as dag:
    task1=PythonOperator(
        task_id="push_connection",
        python_callable=get_name,
    )
    
    task1