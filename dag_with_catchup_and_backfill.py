from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta

default_args={
    'owner':'neeraj5',
    'retries':'2',
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v01',
    start_date=datetime(2025,1,30),
    description='dag with catchup & backfill',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True #by default, catchup is True -- but again setting it manually also.
    #catchup helps run dag since start_date till present date.
) as dag:
    t1=BashOperator(
        task_id='task1',
        bash_command='echo this is a simple bash command'
    )