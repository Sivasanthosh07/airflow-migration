from airflow import DAG

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.bash import BashOperator


default_args={
    "owner":"app_migration",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
with DAG(
    dag_id="Install-MonolithApp-onPrem",
    default_args=default_args,
    description="Install monolith app with DB on Prem",
    schedule="0 0 * * *",
    start_date=datetime(2023,9,11)

)as dag:
    task1=SSHOperator(
     task_id="install_mono",
     ssh_conn_id='on_prem_vm_ssh',
     command='/scripts/deploy_mono_app.sh',
     cmd_timeout=96000
     )
    
    task1
