# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings,show
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']



@task
@parallel
def install_target():
    """
    # sudo  yum -y install scsi-target-utils
    :return:
    """
    sudo('yum -y install scsi-target-utils')

@task
@parallel
def install_initiator():
    sudo('yum install -y iscsi-initiator-utils')
