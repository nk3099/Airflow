from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args={
    'owner':'nk2',
    'retries':2,
    'retry_delay':timedelta(minutes=2)
}

def greet():
    print("hello world")
    
with DAG (
    default_args=default_args,
    dag_id='create_dag_with_python_operator',
    description='creating dag with python operator',
    start_date=datetime(2024,2,1),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    
    #task1
    

