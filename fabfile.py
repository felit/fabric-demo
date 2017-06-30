# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
from bigdata.kudu import fabfile as kudu
from common.ssh import fabfile as ssh

env.hosts = ['root@192.168.0.2', 'root@192.168.0.3', 'root@192.168.0.4']
env.roledefs = {
    'ssh-hosts': ['root@192.168.0.2', 'root@192.168.0.3', 'root@192.168.0.4'],
    'kudu': ['root@192.168.0.3',
             'root@192.168.0.4',
             'root@192.168.0.5',
             'root@192.168.0.6',
             'root@192.168.0.7',
             'root@192.168.0.8', ],
}



@task(default=True)
@runs_once
def install():
    # sudo('yum install -y wget')
    # ssh.add_public_key_authorizied_keys()
    # execute(kudu.install, mode='scp')
    execute(kudu.status)

