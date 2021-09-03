from datetime import datetime
from datetime import timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from hello_operator import HelloOperator
from hello_mssql_operator import HelloMsSqlOperator
import pendulum

local_tz = pendulum.timezone("Asia/Bangkok")

dag_params = {
    'owner': 'airflow',
    "depends_on_past": False,
    'start_date': datetime(2021, 8, 15, 0, 0, tzinfo=local_tz),
    'email_on_failure': False,
    'email_on_retry': False,
    'do_xcom_push': False
    # 'retries': 3,
    # 'retry_delay': timedelta(minutes=10),
}

dag = DAG('hello_world',
          catchup=False,
          default_args=dag_params,
          schedule_interval="@once"
)

dummy_op = DummyOperator(task_id="dummy_start", dag=dag)

hello_task = HelloOperator(task_id='sample-task', name='THIS IS FROM CUSTOM OPERATOR', dag=dag)

hello_task2 = HelloOperator(task_id='sample-task-2', name='I LOVE AIRFLOW', dag=dag)

hello_task3 = HelloMsSqlOperator(task_id='sample-task-3',mssql_conn_id="1_dms_conn_id", sql="SELECT @@version;", database="PhaNam_eSales_PRO", dag=dag)


dummy_op >> hello_task >> hello_task2 >> hello_task3
