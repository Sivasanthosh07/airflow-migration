
from aws import rds_demo

def get_name(ti):
    url,Port=rds_demo.RdsInstanceScenario.get_connection("demo")

    ti.xcom_push(key="url",value=url)
    ti.xcom_push(key="Port",value=Port)
    
    