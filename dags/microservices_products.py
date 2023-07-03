from airflow import DAG

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator




default_args={
    "owner":"santhosh",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
with DAG(
    dag_id="microservices_products",
    default_args=default_args,
    description="microservices",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,20)

)as dag:
    task1=PostgresOperator(
        task_id="microservices_products",
        postgres_conn_id="postgres_localhost",
        sql="sql/microservices_products.sql",
        database="microservices_products"
    )
    task2=PostgresOperator(
        task_id="microservices_products_data",
        postgres_conn_id="postgres_localhost",
        sql="sql/microservice_prodcut.sql",
        database="microservices_products"

    )
    
    
    task1 >> task2
