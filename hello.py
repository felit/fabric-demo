from fabric.api import *
from fabric.colors import *
env.roledefs = {
  "dev":['dev@192.168.181.21','dev@192.168.181.22','dev@192.168.181.23','dev@192.168.181.24']
}

@roles('dev')
def ping():
  print green(run('df -lh'))
  print green('success')

@roles('dev')
def upload():
  put('/home/congsl/software/hadoop-2.4.1.tar.gz','/opt/')

@roles('dev')
def install():
  with cd('/opt'):
     run('tar -zxvf hadoop-2.4.1.tar.gz')
     run('ls -l')

@roles('dev')
def move():
   run('mkdir /opt/software')
   with cd('/opt'):
      run('mv hadoop-2.4.1.tar.gz /opt/software')

@roles('dev')
def config():
  with cd('/opt/hadoop-2.4.1'):
    put('templates/hadoop/core-site.xml','/opt/hadoop-2.4.1/etc/hadoop/')
    put('templates/hadoop/hadoop-env.sh','/opt/hadoop-2.4.1/etc/hadoop/')
    put('templates/hadoop/slaves','/opt/hadoop-2.4.1/etc/hadoop/')
    put('templates/hadoop/hdfs-site.xml','/opt/hadoop-2.4.1/etc/hadoop/')

@roles('dev')
def remove():
  run('rm -fr /data/hdfs')
  # with cd('/data/.ssh'):
    # put('templates/authorized_keys','authorized_keys',mode=0600)
# declare -x HADOOP_COMMON_LIB_NATIVE_DIR="/opt/hadoop-2.4.1/lib/native"
# declare -x HADOOP_OPTS="-Djava.library.path=/opt/hadoop-2.4.1/lib"
# declare -x HADOOP_PREFIX="/opt/hadoop-2.4.1"
# declare -x HADOOP_ROOT_LOGGER="DEBUG,console"

@roles('dev')
def ll():
  run('ls -l /data')

@roles('dev')
def hbase():
  # put('/home/congsl/software/hbase-1.0.1.1-bin.tar.gz',"/opt/software")
  put('files/hbase-0.98.16.1-hadoop2-bin.tar.gz',"/opt/software")
  with cd('/opt'):
    run('tar -zxvf /opt/software/hbase-0.98.16.1-hadoop2-bin.tar.gz')

@roles('dev')
def config_hbase():
   put('/home/congsl/apps/storm/fabric/templates/hbase-site.xml','/opt/hbase-0.98.16.1-hadoop2/conf/')

@roles('dev')
def remove_hbase1():
   run('rm -fr /opt/hbase-1.0.1.1')
   run('rm -fr /opt/software/hbase-1.0.1.1-bin.tar.gz')

def sd():
  #192.168.181.23:/opt/software
