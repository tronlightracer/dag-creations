from airflow.models import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator, TriggerDagRunLink
from airflow.operators.python import PythonOperator
from airflow.utils.state import DagRunState
from airflow.utils.dates import days_ago

#from datetime import time
from time import sleep

with DAG(
    dag_id="trigger_middle_child",
    start_date=days_ago(2),
    schedule_interval=None,
    is_paused_upon_creation=False,
) as dag:

    t0 = PythonOperator(
        task_id="start_middle_child_dag",
        python_callable=lambda: sleep(45),
    )

    t1 = TriggerDagRunOperator(
        task_id="trigger_youngest_child_dag",
        trigger_dag_id="trigger_youngest_child",
        reset_dag_run=True,
        wait_for_completion=True,
        allowed_states=[DagRunState.SUCCESS],
        failed_states=[DagRunState.FAILED],
    )

t0 >> t1
