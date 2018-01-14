# -*- coding:utf8 -*-
# 安装
"""

"""

from __future__ import with_statement
from fabric.api import env, task

env.hosts = [
    'vagrant@192.168.18.164',
    # 'vagrant@192.168.18.190'
    # 'root@www.livedrof.com'
]


@task
def install():
    # go.install()
    tidb.install()