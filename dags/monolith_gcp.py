from airflow import DAG

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator




default_args={
    "owner":"app_migrtaion",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
with DAG(
    dag_id="Monolith_gcp",
    default_args=default_args,
    description="monolith",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,20)

)as dag:
    task1=PostgresOperator(
        task_id="monolith_gcp",
        postgres_conn_id="postgres_localhost",
        sql="sql/monolith_gcp.sql",
        database="monolith_gcp"
    )
    # task2=PostgresOperator(
    #     task_id="monolith_gcp_data",
    #     postgres_conn_id="postgres_localhost",
    #     sql="sql/monolith_data.sql",
    #     database="monolith_gcp"

    # )
    
    
    task1 
