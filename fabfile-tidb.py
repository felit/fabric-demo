# -*- coding:utf8 -*-
# 安装
"""

"""

from __future__ import with_statement
from fabric.api import run, env, task
from fabric.contrib import files

env.hosts = [
    'vagrant@192.168.18.164',
    # 'vagrant@192.168.18.190'
    # 'root@www.livedrof.com'
]
from languages.go import fabfile as go
from database.tidb import fabfile as tidb


@task
def install():
    # go.install()
    tidb.install()