from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash import BashOperator  

default_args = {
    'owner': 'nk',
    'retries':5,
    'retry_delay':  timedelta(minutes=2)
}

with DAG(
    dag_id = 'our_first_dag_v3',
    default_args=default_args,
    description='this is our first dag that we write',
    start_date=datetime(2021,7,30),
    schedule_interval='@daily'
    
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )
    task2 =  BashOperator(
        task_id = 'second_task',
        bash_command = 'echo hello 2nd task running now'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hello 3rd task running parallel with 2nd task'
    )
    
    #Task Dependency method 1:
    task1 >> task2
    task1 >> task3

    #Task Dependency method 2:
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)

    #Task Dependency method 3:
    task1 >> [task2,task3]
