# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

"""

"""

env.hosts = [
    'vagrant@192.168.18.164',
    'vagrant@192.168.18.190'
]

@task
def install():
    run('yum install -y php')
    run('apt install -y php5')