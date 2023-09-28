from airflow import DAG

from datetime import datetime,timedelta

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.bash import BashOperator





default_args={
<<<<<<< HEAD
    "owner":"app_migraton",
=======
    "owner":"app_migrtaion",
>>>>>>> 98f4d4f2339caac4b26cf80cd879b70146c35de9
    "retries":5,
    "retry_delay":timedelta(minutes=3)

}
command="sudo apt -y update "
with DAG(
    dag_id="microshop-setup",
    default_args=default_args,
    description="microservices setup",
    schedule="0 0 * * *",
    start_date=datetime(2023,6,26)

)as dag:
    task1=SSHOperator(
     task_id="connect_to_vm",
     ssh_conn_id='ssh',
     command=command,
     )
    
    task2=SSHOperator(
        task_id="install_k3d",
        ssh_conn_id='ssh',
        command="/scripts/install_k3d.sh",
        cmd_timeout=9600
    )
    
    task3=SSHOperator(
        task_id="install_microservices",
        ssh_conn_id='ssh',
        command="/scripts/install_microservices.sh",
        cmd_timeout=96000
    )


    task4=SSHOperator(
        task_id="final",
        ssh_conn_id='ssh',
        command="echo INSTALLED SUCCESSFULLY"
    )

    task1>>task2>>task3>>task4
