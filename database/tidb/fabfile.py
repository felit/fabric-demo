# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show, run
from fabric.contrib import files

# env.hosts = ['dev@192.168.181.21',
#              'dev@192.168.181.22',
#              'dev@192.168.181.23',
#              'dev@192.168.181.24']
from common.linux import fabfile as linux


@task
@parallel
def install():
    linux.install_packages(['git'])
    install_tidb()


def install_tidb():
    # run('git clone https://github.com/pingcap/tidb.git $GOPATH/src/github.com/pingcap/tidb')
    with cd('$GOPATH/src/github.com/pingcap/tidb'):
        run('make')
