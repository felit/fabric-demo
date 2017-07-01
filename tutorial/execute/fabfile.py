from __future__ import with_statement
from fabric.api import run
from fabric.api import local
import logging
from fabric.api import local, settings, abort, lcd, cd, get, env, roles, task,hide
from fabric.contrib.console import confirm
env.hosts = ['root@www.livedrof.com','root@139.198.6.107']


@task
def task1():
    os = args()
    print os.lower().find('ubuntu') >= 0
    print os.lower().find('centos') >= 0
    print("ddd %s" % os)


def args():
    # with hide('stdout','stderr','running'):
    with hide('everything'):
        a = run('cat /etc/issue',warn_only=True)
    return a