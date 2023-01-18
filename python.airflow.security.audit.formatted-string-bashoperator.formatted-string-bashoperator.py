import requests
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}
dag = DAG(
    "tutorialex2",
    default_args=default_args,
    description="Tutorial DAG",
    schedule_interval=timedelta(days=1)
)
message = requests.get("https://fakeurl.asdf/message").text
# ruleid: formatted-string-bashoperator
t1 = BashOperator(
    task_id="print_date",
    bash_command="echo " + message,
    dag=dag
howlong = requests.get("https://fakeurl.asdf/howlong").text
command = "sleep {}".format(howlong)
t2 = BashOperator(
    task_id="sleep",
    depends_on_past=False,
    bash_command=command,
    retries=3,
unsafe_templated_command = """
{% for i in range(5) %}
    echo "{{ ds }}"
    echo "{{ macros.ds_add(ds, 7)}}"
    echo "{{ params.my_param }}"
    echo "{{ %s }}"
{% endfor %}
""" % (message,)
t3 = BashOperator(
    task_id="templated",
    bash_command=unsafe_templated_command,
    params={
        "my_param": "Parameter I passed in"
    },
# ok: formatted-string-bashoperator
templated_command = """
"""
t4 = BashOperator(
    task_id="safe_templated",
    bash_command=templated_command,
t5 = BashOperator(
    task_id="safe",
    bash_command="echo hello world!",
echo_message = f"echo {message}"
    bash_command=echo_message,
t1 >> [t2, t3, t4, t5, t6]
