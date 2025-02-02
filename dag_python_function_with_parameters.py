from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args={
    "owner": "nk3",
    "retries":3,
    "retry_delay":timedelta(minutes=1)
}

# def greet(name,age):
#     print(f"Hello world! my name is {name}",
#           f"age is {age}")

# def greet(age,ti):
#     name=ti.xcom_pull(task_ids='get_name')
#     print(f"Hello world! my name is {name}",
#           f"age is {age}")

# def greet(age,ti):
#     first_name=ti.xcom_pull(task_ids='get_name',key="first_name")
#     last_name=ti.xcom_pull(task_ids='last_name',key='last_name')
#     print(f"Hello world! my name is {first_name}{last_name}",
#           f"age is {age}")

def greet(ti):
    first_name=ti.xcom_pull(task_ids='get_name',key="first_name")
    last_name=ti.xcom_pull(task_ids='get_name',key='last_name')
    age=ti.xcom_pull(task_ids='get_age',key='age')
    print(f"Hello world! my name is {first_name}{last_name}",
          f"age is {age}")
    
# def get_name():
#     return 'jerry'

def get_name(ti):
    ti.xcom_push(key="first_name",value="jerry")
    ti.xcom_push(key="last_name",value="tom")
    
def get_age(ti):
    ti.xcom_push(key="age",value=20)
    
with DAG(
    default_args=default_args,
    dag_id='dag_python_function_with_parameters_v04',
    description="dag for python function with parameters",
    start_date=datetime(2024,12,31),
    schedule_interval="@daily"
) as dag:
    # task1=PythonOperator(
    #     task_id="greet",
    #     python_callable=greet,
    #     op_kwargs={"name":"neeraj",
    #                "age":24}
    # )
    task1=PythonOperator(
        task_id="greet",
        python_callable=greet #,
        #op_kwargs={"age":24}
    )
    task2=PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )
    task3=PythonOperator(
        task_id="get_age",
        python_callable=get_age
    )
    
    [task2,task3] >> task1
    
    #task2 >> task1
    
    #task1
    #task2
    
    #note: 
    #op_kwargs - dictionary of keywords arguments that get unpacked in python function
    #data sharing via airflow xcoms -> to share information between different tasks
    #MAX size of xcom is 48kb
    #ti -> task instance -- since xcom can be only called by ti