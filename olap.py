# -*- coding: utf8 -*-
# environtment variables
from fabric.api import *
from fabric.colors import *

#  kylin:1.2
#  hadoop 2.6.0
#  hive: 0.14.0
# hbase: 0.98.8
env.roledefs  =  {
      "hadoop":["dev@192.168.181.21","dev@192.168.181.22","dev@192.168.181.23","dev@192.168.181.24"],
      "master":["dev@192.168.181.21"],
      'kylin':['dev@192.168.181.21']
}
env.passwords = {
	"dev@192.168.181.21:21":"dev123",
	"dev@192.168.181.21:22":"dev123",
	"dev@192.168.181.21:23":"dev123",
	"dev@192.168.181.21:24":"dev123",
}
@roles('hadoop')
def test():
 	run('whoami')
@roles('hadoop')
def deploy():
	run('scp dev@192.168.181.23:/opt/software/hadoop-2.6.0.tar.gz /opt/')
	with cd('/opt'):
		run('tar -zxvf hadoop-2.6.0.tar.gz')
		run('rm hadoop-2.6.0.tar.gz')
	for f in ('core-site.xml','hadoop-env.sh','slaves','hdfs-site.xml'):
		put('/home/congsl/storm/fabric/files/hadoop/etc/hadoop/%s'%f,'/opt/hadoop-2.6.0/etc/hadoop/')

	run('scp dev@192.168.181.23:/opt/software/hbase-0.98.16.1-hadoop2-bin.tar.gz /opt/')
	with cd('/opt'):
		run('tar -zxvf hbase-0.98.16.1-hadoop2-bin.tar.gz')
		run('rm hbase-0.98.16.1-hadoop2-bin.tar.gz')
	for f in ('hbase-env.sh','hbase-site.xml','regionservers'):
		put('/home/congsl/storm/fabric/files/hbase/%s'%f,'/opt/hbase-0.98.16.1-hadoop2/conf/')
def format_hadoop():
	pass
@roles('master')
def start_hadoop():
	pass
	# with cd('/opt/hadoop-2.6.0'):

def stop_hadoop():
	pass
@roles('hadoop')
def clean():
	with cd('/data'):
		run('rm -fr hdfs')
	with cd('/opt'):
		run('rm -fr hadoop-2.6.0')
		run('rm -fr hbase-0.98.16.1-hadoop2')
@roles('master')
def deploy_master():
	run('scp dev@192.168.181.23:/opt/software/apache-hive-0.14.0-bin.tar.gz /opt/')
	with cd('/opt'):
		run('tar -zxvf apache-hive-0.14.0-bin.tar.gz ')
		run('rm apache-hive-0.14.0-bin.tar.gz')
		put('/home/congsl/storm/fabric/files/hive/hive-env.sh','apache-hive-0.14.0-bin/conf/')
		put('/home/congsl/storm/fabric/files/hive/hive-site.xml','apache-hive-0.14.0-bin/conf/')
		put('scp dev@192.168.181.23:/opt/software/postgresql-9.4-1206-jdbc4.jar','apache-hive-0.14.0-bin/lib/')
	run('scp dev@192.168.181.23:/opt/software/apache-kylin-1.2-bin.tar.gz /opt/')
	with cd('/opt'):
		run('tar -zxvf apache-kylin-1.2-bin.tar.gz')
		run('rm apache-kylin-1.2-bin.tar.gz')

def sqoop():
	pass
def pre_compile():
	pass
def compile_hadoop():
	with cd('/opt/software/hadoop-2.6.0-src'):
		run(' mvn package -Pdist,native -DskipTests -Dtar -Drequire.snappy')
@roles('kylin')
def stop():
	with cd('/opt/hadoop-2.4.1'):
		run('sbin/stop-dfs.sh')
	with cd('/opt/hbase-0.98.16.1-hadoop2'):
		run('bin/stop-hbase.sh')
@roles('hadoop')
def clean():
	with cd('/opt'):
		run('ls -ls')
		run('rm -fr hadoop-2.6.0')
		run('rm -fr hbase-0.98.16.1-hadoop2')
	with cd('/data'):
		run('ls -l')
		# run('rm -fr hdfs')

@roles('hadoop')
def ls():
    with cd('/opt'):
       # run('rm -fr hadoop-2.6.0')
       run('ls -lh')
       run('df -lh')

@roles('master')
def clean_master():
	with cd('/opt'):
		run('rm -fr apache-hive-0.13.1-bin')
		run('rm -fr apache-kylin-1.2-bin')
		run('rm -fr apache-kylin-1.2-bin')




