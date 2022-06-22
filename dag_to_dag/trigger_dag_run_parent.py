from airflow.models import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator, TriggerDagRunLink
from airflow.operators.python import PythonOperator
from airflow.utils.state import DagRunState
from airflow.utils.dates import days_ago

with DAG(
    dag_id="trigger_parent",
    start_date=days_ago(2),
    schedule_interval=None,
) as dag:

    t0 = PythonOperator(
        task_id="start",
        python_callable=lambda: "start_task",
    )

    t1 = TriggerDagRunOperator(
        task_id="trigger_dagrun_parent_task",
        trigger_dag_id="trigger_middle_child",
        reset_dag_run=True,
        wait_for_completion=True,
        allowed_states=[DagRunState.RUNNING],
        failed_states=[DagRunState.FAILED],
    )


