#airflow taskflow api

from airflow import DAG
from airflow.decorators import dag,task
from datetime import datetime, timedelta


default_args={
    'owner':'nk4',
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

@dag(dag_id='dag_with_taskflow_api',
     default_args=default_args,
     start_date=datetime(2024,10,10),
     schedule_interval='@daily')
def hello_world_etl():
    #@task()
    # def get_name():
    #     return 'mickey'
    
    @task()
    def get_name(multiple_outputs=True):
        return {
            'first_name':'Jerry',
            'last_name':'Friedman'
        }
    
    @task()
    def get_age():
        return 19
    
    @task()
    def greet(first_name,last_name,age):
        print(f"Hello world! my name is {first_name}{last_name}, and i am {age} years old")
        
    name_dict = get_name()
    age = get_age()
    
    greet(first_name=name_dict['first_name'],last_name=name_dict['last_name'],age=age)
    
greet_dag=hello_world_etl()

#note:
#The @dag decorator turns the hello_world_etl function into a DAG, 
# Each function decorated with @task is converted into an Airflow task.

    