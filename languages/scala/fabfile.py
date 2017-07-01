# -*- coding:utf8 -*-
"""

"""

from __future__ import with_statement
from fabric.api import run, env, task, parallel
from fabric.contrib import files


env.hosts = [
    'vagrant@192.168.18.164',
    'vagrant@192.168.18.190'
]

env.password = 'vagrant'


@task
# @parallel
def install():
    run('wget https://downloads.lightbend.com/scala/2.12.2/scala-2.12.2.tgz -O scala.tar.gz')
    # run('scp vagrant@192.168.18.164:~/scala-2.12.2.tgz scala.tar.gz')
    run('tar -zxvf scala.tar.gz')
    dir = run("tar -tf scala.tar.gz | awk -F/ '{print $1}' | tail -n 1")
    run('mv %s /opt/scala' % dir)
    run('rm scala.tar.gz')
    config()


@task
def config():
    files.append('.bashrc', 'export SCALA_HOME=/opt/scala')
    files.append('.bashrc', 'export PATH=$SCALA_HOME/bin:$PATH')
