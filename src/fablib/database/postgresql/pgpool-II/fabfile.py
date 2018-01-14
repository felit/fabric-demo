# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
# TODO

"""
make: pg_config: Command not found
解决:yum install postgresql-devel
"""


def install():
    run('wget http://www.pgpool.net/download.php?f=pgpool-II-3.6.4.tar.gz')
    run('tar -zxvf pgpool-II-3.6.4.tar.gz')
    run('mkdir /opt/pgpool')
    run('cd pgpool-II-3.6.4; ./configure --prefix=/opt/pgpool;make&& make install')
    run('rm pgpool-II-3.6.4.tar.gz')