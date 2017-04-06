# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

# 通过roles与横块化来实现可重用
# known_hosts处理，不然会提示信息
# task 任务可重用
def gen_public_key():
    """
    生成id_rsa
    :return:
    """
    if not files.exists('.ssh/id_rsa.pub'):
        run("ssh-keygen -t rsa -f ~/.ssh/id_rsa -P ''")


def get_id_ras_public_key():
    return run('cat ~/.ssh/id_rsa.pub')


def append_authrozied_key(key):
    files.append('~/.ssh/authorized_keys', key)


# @roles('master')
@runs_once
@task
def add_public_key_authorizied_keys(add_keys=[]):
    # TODO 添加参数，实现额处添加key
    execute(gen_public_key)
    keys = execute(get_id_ras_public_key)
    local_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJXAZx0EzfFtyoFJvimiP1J4/XZZU7WOtx/cH2/dHAi5eBjqk5WjSRVgYGmJWCrivE2KEub25fGqR1wVnZXSfP3x9PsQnE5eO5I/K2OAfUGakHVZeYKm3J5ADryxcRxcKj8d0Y+/PHSyrL0smN+ZyyYqFJ2nfW2tGYKAK9bwdwjcf/QgnR558SbWAjKmBp81JUxQUpkNO+Hv4yIaPPbsYXsVk752DjIrgsE2riGrjCLju1yBu6T7mYw0wEpn4XrE0WQfyZkBRV/BS4Iz1iFYQExrsWaJbe82Gt00TJksbJJN81FGtllmo1AdGTVonwpv3dAS6AMfT2RcFrPZw018v congsl@congsl"""
    keys['local'] = local_key
    for host, key in keys.items():
        execute(append_authrozied_key, key)
        # execute(append_authrozied_key,local_key)
        # append_authrozied_key(local_key)


@task
def clear_id_rsa():
    run('rm ~/.ssh/id_rsa*')
    run('rm ~/.ssh/authorized_keys')
    run('rm ~/.ssh/known_hosts')


def test_hosts():
    pass