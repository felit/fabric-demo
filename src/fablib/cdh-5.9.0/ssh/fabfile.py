# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, execute, roles, runs_once, parallel, task
from fabric.contrib import files

"""
通过execute重复调用一个方法
直接调用方法　区别
"""

# 通过roles与横块化来实现可重用
# known_hosts处理，不然会提示信息
# task 任务可重用
# @parallel(pool_size=5)
@roles('interflow_hosts')
def gen_public_key():
    """
    生成id_rsa
    :return:
    """
    if not files.exists('.ssh'):
        run('mkdir .ssh')
    run('chmod 700 .ssh')

    if not files.exists('.ssh/authorized_keys'):
        run('touch .ssh/authorized_keys')
    run('chmod 600 .ssh/authorized_keys')

    if not files.exists('.ssh/id_rsa.pub'):
        run("ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''")


@roles('interflow_hosts')
def get_id_ras_public_key():
    return run('cat ~/.ssh/id_rsa.pub')


@parallel(pool_size=5)
@roles('interflow_hosts')
def append_authrozied_key(key):
    files.append('~/.ssh/authorized_keys', key)


# @roles('master')
@runs_once
@task
def add_public_key_authorizied_keys(add_keys=[]):
    """
    添加参数，实现额处添加key
    :param add_keys: 额处添加的key值
    :return:
    """
    execute(gen_public_key)
    keys = execute(get_id_ras_public_key)
    vals = keys.values() + add_keys
    for key in vals:
        execute(append_authrozied_key, key)


@task
@roles('interflow_hosts')
def clear_id_rsa():
    if files.exists('.ssh/id_rsa'):
        run('rm ~/.ssh/id_rsa*')
    if files.exists('.ssh/authorized_keys'):
        run('rm ~/.ssh/authorized_keys')
        # run('rm ~/.ssh/known_hosts')


def test_hosts():
    pass