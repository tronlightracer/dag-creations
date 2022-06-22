from airflow.models import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator, TriggerDagRunLink
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


with DAG(
    dag_id="trigger_youngest_child",
    start_date=days_ago(2),
    schedule_interval=None,
    is_paused_upon_creation=False,
) as dag:

    t0 = PythonOperator(
        task_id="start_middle_child_dag",
        python_callable=lambda: "start_middle_child_dag",
    )



