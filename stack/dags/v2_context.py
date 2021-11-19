import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
from airflow.operators.bash_operator import BashOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(1),
}

def push_xcom_with_return():
    return 'my_returned_xcom_with_clear'

def get_pushed_xcom_with_return(**context):
    print(context['ti'].xcom_pull(task_ids='t0'))

def print_ds(ds):
    print(ds)

def print_context(**context):
    print(context)

def clear_x_com(**context):
    context['ti'].clear_xcom_data()

with DAG(dag_id='v2_context', default_args=args, schedule_interval="@once") as dag:

    t0 = PythonOperator(
        task_id='t0',
        python_callable=push_xcom_with_return
    )

    t1 = PythonOperator(
        task_id='t1',
        provide_context=True,
        python_callable=get_pushed_xcom_with_return
    )
    
    t2 = PythonOperator(
        task_id='t2',
        python_callable=print_ds
    )

    t3 = PythonOperator(
        task_id='t3',
        provide_context=True,
        python_callable=print_context
    )

    t4 = PythonOperator(
        task_id='t4',
        provide_context=True,
        python_callable=clear_x_com
    )

    t0 >> t1 >> t2 >> t3 >> t4