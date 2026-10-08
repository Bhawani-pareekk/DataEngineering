# c3 answer - 

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import dag, task


@dag(
    dag_id="etl_operators_demo",
    schedule=None,
)
def etl_operators_demo():
    @task.python(task_id="start-a")
    def start():
        print("Pipeline started")

    @task.bash(task_id="download-a")
    def download():
        return 'echo "downloading file"'

    process = BashOperator(
        task_id="process",
        bash_command='echo "Processing File.."',
    )

    @task.python(task_id="finish-a")
    def finish():
        print("pipeline finished")

    @task.python(task_id="finish-b")
    def finish_b():
        print("pipeline finished add 5th task")

    start() >> download() >> process >> finish()>>finish_b()    


etl_operators_demo()
# the version is changing 