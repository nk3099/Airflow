source py_env/bin/activate    
export AIRFLOW_HOME=`pwd`
airflow db init   
airflow webserver -p 8080 & airflow scheduler

airflow users create --help   
airflow users create --username admin --firstname neeraj --lastname kumar --role Admin --email admin@domain.com

![image](https://github.com/user-attachments/assets/1624e73e-c366-457b-b069-e8efa3aa5aa8)

![image](https://github.com/user-attachments/assets/2774f2fb-595d-4a91-a25f-70825220d7eb)

![image](https://github.com/user-attachments/assets/411ebbcc-c1e2-48fa-a18f-d0ce6859bf82)
