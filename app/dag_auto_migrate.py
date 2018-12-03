# airflow DAG
import airflow
from migrate import upgrade
from datetime import datetime


flow = airflow.Flow()
start = datetime.now()

auto_migrate_dag = flow.define_dag(
    dag_id='auto_migrations',
    schedule_interval='0 */1 * * *',
    max_active_runs=1
)

auto_migrate_task = flow.python_operator(
    python_callable=upgrade,
    provide_context=False,
    depends_on_past=False,
    retries=0
)
