from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def my_hello_world():
    print("Hello World!")

with DAG(
    dag_id="my_hello_world_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    hello_task = PythonOperator(
        task_id="hello_world_task",
        python_callable=my_hello_world,
    )