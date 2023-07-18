import psycopg2


# def return_gcp_db(ti):

 
#     return db,db_instance,url,Port

def create_databses(ti):
    db=ti.xcom_pull(task_ids='get_gcp_db',key="datbases")
    db_instance=ti.xcom_pull(task_ids='get_gcp_db',key="db_instance")
    url=ti.xcom_pull(task_ids='get_connection',key="url")
    Port=ti.xcom_pull(task_ids='get_connection',key="Port")  
    engine = psycopg2.connect(
        user="postgres",
        password="postgres",
        host=url,
        port=Port,
    )
    engine.autocommit=True
    cur = engine.cursor()
    cur.execute("create database newdb")
    engine.commit()

