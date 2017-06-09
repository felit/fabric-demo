from fabric.api import *
from fabric.colors import *
env.roledefs = {
  "druid":['dev@192.168.181.21'],
  "mysql":['dev@192.168.181.23']
}
@roles('druid')
def start():
	with cd('/opt/hadoop-2.4.1'):
		run('nohup sbin/start-dfs.sh &')
	with cd('/opt/hbase-0.98.16.1-hadoop2'):
		run('nohup bin/start-hbase.sh &')
	with cd('/opt/software/druid-0.8.2'):
		run('nohup ./run_druid_server.sh overlord ; sleep 3')


@roles('druid')
def stop():
    run("ps -ef | grep druid | grep overlord | grep -v grep | awk '{print $2}'|xargs kill")