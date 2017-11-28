# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts=['vagrant@192.168.18.164']
env.password='vagrant'

def install():
    pass


def load_files():
    pass

@task
def pre_requirements():
    sudo('yum install -y ed sed unzip ntp')
    sudo('chkconfig iptables off')

    pass


def dd():
    pass