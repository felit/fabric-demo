# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = ['root@139.198.6.107']
env.hosts = ['root@139.198.6.107']


@task
def load():
    sudo('yum install -y ipvsadm')
    sudo('yum install -y ipvsadm')