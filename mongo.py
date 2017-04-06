from fabric.api import *
from fabric.colors import *
env.roledefs = {
  "dev": [
       'dev@192.168.181.21'
      ,'dev@192.168.181.22'
      ,'dev@192.168.181.23'
#      ,'dev@192.168.181.24'
  ]
}


@roles('dev')
def stop():
   run("ps -ef | grep mongo| grep -v grep  | awk '{print $2}' | xargs kill") 
   run("ps -ef | grep mongo|grep -v grep") 
   
@roles('dev')
def disk():
   pass
   #run('rm -fr /data/mongo-data')
#   run('du -sh /data/mongo-data')
