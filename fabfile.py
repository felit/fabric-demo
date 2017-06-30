from bigdata.kudu import fabfile as kudu

# @task(default=True)
def install():
    kudu.install_offline()