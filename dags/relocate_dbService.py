# from airflow import DAG

# from datetime import datetime,timedelta

# from airflow.providers.postgres.operators.postgres import PostgresOperator

# from airflow.providers.ssh.operators.ssh import SSHOperator


# default_args={
#     "owner":"app_migration",
#     "retries":5,
#     "retry_delay":timedelta(minutes=3)

# }
# with DAG(
#     dag_id="db_service_relocation",
#     default_args=default_args,
#     description=" relocating db from gcp to aws",
#     schedule="0 0 * * *",
#     start_date=datetime(2023,6,26)

# )as dag:
#     task1=