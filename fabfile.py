# -*- coding:utf8 -*-
from __future__ import with_statement

from fabric.api import env, execute, runs_once, task

from src.fablib.bigdata.kudu import fabfile as kudu


env.hosts = ['root@192.168.0.2', 'root@192.168.0.3', 'root@192.168.0.4']
env.roledefs = {
    'ssh-hosts': ['root@192.168.0.2', 'root@192.168.0.3', 'root@192.168.0.4'],
    'kudu': ['root@192.168.0.3',
             'root@192.168.0.4',
             'root@192.168.0.5',
             'root@192.168.0.6',
             'root@192.168.0.7',
             'root@192.168.0.8', ],
    'kudu-master': ['root@192.168.0.3',
                    'root@192.168.0.4'],
    'kudu-tserver': ['root@192.168.0.3',
                     'root@192.168.0.4',
                     'root@192.168.0.5',
                     'root@192.168.0.6',
                     'root@192.168.0.7',
                     'root@192.168.0.8', ]
}


@task(default=True)
@runs_once
def install():
    # sudo('yum install -y wget')
    # ssh.add_public_key_authorizied_keys()
    # execute(kudu.install, mode='scp')
    execute(kudu.status)

