# import DagFactory
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def say_hi():
    print("Hi")

def say_hello():
    print("Say Hello")

default_args={
    "email":"rajesh.pyne@gmail.com"
}
dag_name = DAG('test_name', default_args=default_args)

t1 = PythonOperator(python_callable="print('Hi')",task_id="task_id1")