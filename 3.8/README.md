# READ ME

## [POSTGRES - SOLVED] Fail to connect Postgresql container
```
listen_adress = ‘*’
uncomment the port and change it for 5433
AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:mysecretpassword@postgres:5433/airflow
```