These dags showcase the ability of the TriggerDagRunOperator in airflow that allows the user to trigger running dags from another dag.

To utilize this dag run the parent dag and the parent dag will trigger the middle_child dag which will in turn trigger the youngest_child dag.
