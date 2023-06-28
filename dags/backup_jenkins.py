from airflow import DAG

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.providers.ssh.operators.ssh import SSHOperator






default_args={
    "owner":"santhosh",
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
command="sudo apt -y update "
with DAG(
    dag_id="jenkins_backup",
    default_args=default_args,
    description="jenkins backup",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,26)

)as dag:

    task1=SSHOperator(
        task_id="backup_jenknis",
        ssh_conn_id='ssh',
        command="/scripts/backup_jenkins.sh",
        cmd_timeout=9600
    )
    
    task1
