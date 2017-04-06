from fabric.api import *
from fabric.colors import *
env.roledefs = {
  "kylin":['dev@192.168.181.21'],
  "mysql":['dev@192.168.181.23']
}
@roles('kylin')
def start():
	with cd('/opt/hadoop-2.4.1'):
		run('nohup sbin/start-dfs.sh &')
	with cd('/opt/hbase-0.98.16.1-hadoop2'):
		run('nohup bin/start-hbase.sh &')
	with cd('/opt/apache-kylin-1.1.1-incubating-bin'):
		run('bin/kylin.sh start')