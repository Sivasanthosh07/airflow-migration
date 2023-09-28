from airflow import DAG

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator




default_args={
    "owner":"app_migrtaion",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
with DAG(
    dag_id="GKE_microservices_DB_Setup",
    default_args=default_args,
    description="microservices",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,20)

)as dag:
    task1=PostgresOperator(
        task_id="Create_microservices_pg_DB",
        postgres_conn_id="postgres_gke",
        sql="sql/microservices_pg_db_create.sql",
        database="postgres"
    )
    task2=PostgresOperator(
        task_id="microservices_orders_table",
        postgres_conn_id="postgres_gke",
        sql=["sql/microservices_pg_users_table.sql", "sql/microservices_pg_orders_table.sql"],
        database="microservices_orders"

    )
    task3=PostgresOperator(
        task_id="microservices_products_table",
        postgres_conn_id="postgres_gke",
        sql="sql/microservices_pg_products_table.sql",
        database="microservices_products"

    )
    
    
    task1>>task2>>task3
