from airflow.sdk import dag, task

@dag(
    dag_id="my_first_dag"
)

def my_first_dag():
    @task
    def task1():
        print("hello Bhawani")
    @task
    def task2():
        dict={1,2,3,4}
        return dict
    
    @task
    def task3():
        print("learning dag and enjoy learningss")


    @task
    def task5():
        print("hello just writing a task to check the airflowssss")

    @task.bash   
    def task4():
        return "echo hello using shell"

    t1=task1()
    t2=task2()
    t3=task3()
    t4=task4()
    t5=task5()
    t1>>t2>>t3>>t4>>t5

my_first_dag()