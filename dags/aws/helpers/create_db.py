import psycopg2

import pandas as pd


# def return_gcp_db(ti):

 
#     return db,db_instance,url,Port

def create_databses(ti):
    # db=ti.xcom_pull(task_ids='get_gcp_db',key="datbases")
    # db_instance=ti.xcom_pull(task_ids='get_gcp_db',key="db_instance")
    url=ti.xcom_pull(task_ids='get_connection',key="url")
    Port=ti.xcom_pull(task_ids='get_connection',key="Port")  
    testdb="microservices"
    engine = psycopg2.connect(
        user="postgres",
        password="postgres",
        host=url,
        port=Port,
    )
    engine.autocommit=True
    cur = engine.cursor()
    cur.execute("SELECT datname FROM pg_database;")
    df =(list(cur.fetchall()))
    databases=[list(i)[0] for i in df]
    print(databases)
    if testdb not in databases:
        cur.execute(f"CREATE DATABASE {testdb}")
        engine.commit()

