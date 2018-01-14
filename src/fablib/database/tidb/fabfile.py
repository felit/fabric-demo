# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import parallel, cd, task, run

# env.hosts = ['dev@192.168.181.21',
#              'dev@192.168.181.22',
#              'dev@192.168.181.23',
#              'dev@192.168.181.24']


@task
@parallel
def install():
    linux.install_packages(['git'])
    install_tidb()


def install_tidb():
    # run('git clone https://github.com/pingcap/tidb.git $GOPATH/src/github.com/pingcap/tidb')
    with cd('$GOPATH/src/github.com/pingcap/tidb'):
        run('make')
