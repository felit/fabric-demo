# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, local, task
from fabric.contrib import files

env.hosts = ['root@www.livedrof.com', 'hadoop@192.168.19.11', 'root@192.168.49.66']
aliyun = ('root@www.livedrof.com', 'hadoop@192.168.19.11')
env.roledefs = {
    # 'mysql': 'root@139.198.6.107'
    'mysql': 'hadoop@192.168.19.11'
}
global_var = 900


@task()
@hosts(aliyun)
def host_test():
    run('uname -a', shell=False)


@task
@runs_once
def get_hosts():
    """
    可以更新roles属性
    可以更新hosts属性
    :return:
    """
    print env.user, env.host
    env.hosts = ['root@192.168.49.66']
    env.roledefs.update({
        'role1': ['root@192.168.49.66']
    })
    # print execute(get_all_ips)
    execute(role_execute)
    execute(multis, hosts=['root@192.168.49.66'])
    env.roledefs.update({
        'role1': ['hadoop@192.168.19.11']
    })
    execute(role_execute)


@task
@runs_once
def run_once_test():
    execute(multis)
    print execute(get_all_ips)
    print execute(get_hosts).values()


@task
def test_env():
    print env.user, env.host, env.roles


@task
@roles(['role1'])
def role_execute():
    run('whoami')


@task
def multis():
    run('whoami', shell=False)


@task
@runs_once
def get_all_ips():
    ip_list = execute(get_ips)
    ips_list = []
    for host, ips in ip_list.items():
        ips_list += ips
    return ips_list


@task
@parallel
def get_ips():
    """
    返回ip列表，返回主机的
    :return:
    """
    result = run("/sbin/ifconfig | grep inet | grep -v :10\. |grep -v :127\. |awk -F: '{print $2}'|awk '{print $1}'",
                 shell=False)
    ips = [ip.strip() for ip in result.split("\n")]

    return ips


@task
@runs_once
def nested_task():
    execute(nested_task1)


@task
# @runs_once
def nested_task1():
    execute(nested_task2)


@task
# @runs_once
def nested_task2():
    print execute(nested_task3)


@task
# TODO已出错
# @runs_once
def nested_task3():
    return run('hostname', shell=False)


@task
def get_hosts():
    return env.host