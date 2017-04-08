# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd
from fabric.contrib import files
# root w@^s1kta!FQq7z3H
env.hosts = ['root@10.91.11.43', 'root@10.91.12.13', 'root@10.91.12.16', 'root@10.91.34.2']
env.roledefs = {'cdh': env.hosts,
                'master': env.hosts[:1],
                'slaves': env.hosts[1:],
                'mysql': env.hosts[:1],
}
from mysql.install import install_mysql

res = None
"""
env
{'': True, 'disable_known_hosts': False, 'effective_roles': [], 'tasks': ['get_authorized_keys'], 'linewise': True, 'show': None, 'password': None, 'key_filename': None, 'abort_on_prompts': False, 'skip_unknown_tasks': False, 'reject_unknown_hosts': False, 'skip_bad_hosts': False, 'use_ssh_config': False, 'roledefs': {'master': ['dev@192.168.181.21'], 'cdh': ['dev@192.168.181.21', 'dev@192.168.181.22', 'dev@192.168.181.23', 'dev@192.168.181.24']}, 'gateway': None, 'gss_auth': None, 'keepalive': 0, 'eagerly_disconnect': False, 'clean_revert': True, 'rcfile': '/home/congsl/.fabricrc', 'path_behavior': 'append', 'hide': None, 'sudo_prefix': "sudo -S -p '%(sudo_prompt)s' ", 'lcwd': '', 'no_agent': False, 'forward_agent': False, 'remote_interrupt': None, 'port': '22', 'shell': '/bin/bash -l -c', 'version': '1.13.1', 'use_exceptions_for': {'network': False}, 'connection_attempts': 1, 'hosts': ['dev@192.168.181.21', 'dev@192.168.181.22', 'dev@192.168.181.23', 'dev@192.168.181.24'], 'gss_deleg': None, 'new_style_tasks': False, 'cwd': '', 'abort_exception': None, 'real_fabfile': '/data/source/self/fabric-demo/cdh-5.9.0/fabfile.py', 'passwords': {}, 'sudo_password': None, 'host_string': 'dev@192.168.181.22', 'shell_env': {}, 'always_use_pty': True, 'colorize_errors': False, 'exclude_hosts': [], 'all_hosts': ['dev@192.168.181.21', 'dev@192.168.181.22', 'dev@192.168.181.23', 'dev@192.168.181.24'], 'sudo_prompt': 'sudo password:', 'again_prompt': 'Sorry, try again.', 'echo_stdin': True, 'user': 'dev', 'gss_kex': None, 'command_timeout': None, 'path': '', 'local_user': 'congsl', 'combine_stderr': True, 'command_prefixes': [], 'dedupe_hosts': True, 'warn_only': False, 'no_keys': False, 'sudo_passwords': {}, 'roles': [], 'fabfile': 'fabfile', 'use_shell': True, 'host': '192.168.181.22', 'pool_size': 0, 'system_known_hosts': None, 'prompts': {}, 'output_prefix': True, 'command': 'get_authorized_keys', 'timeout': 10, 'default_port': '22', 'ssh_config_path': '/home/congsl/.ssh/config', 'parallel': True, 'sudo_user': None, 'ok_ret_codes': [0]}
<class 'fabric.utils._AttributeDict'>
"""
MASTER_HOST = env.roledefs['master'][0].split('@')[1]


@runs_once
def deploy():
    execute(useradd)
    execute(update_kernel)
    execute(config_hosts)
    execute(install_jdk)
    execute(install_mysql)
    execute(install_cm)
    execute(config_cm)
    execute(sync_cm)


@runs_once
def start():
    execute(start_server)
    execute(start_agent)


@roles('cdh')
def useradd():
    # 是否存在cloudera-scm
    sudo(
        'useradd --system --home=/opt/cm-5.9.0/run/cloudra-scm-server --no-create-home --shell=/bin/false --comment "Cloudera SCM User" cloudera-scm')


@roles('cdh')
def config_hosts():
    """
    TODO 配置hosts信息
    :return:
    """
    i = 0
    for host in env.hosts:
        i += 1
        files.append('/etc/hosts', '%s   kylin%s' % (host.split('@')[1], i))


@roles('cdh')
def update_kernel():
    run('echo 10 > /proc/sys/vm/swappiness')
    run('echo never > /sys/kernel/mm/transparent_hugepage/defrag')


@roles('master')
def install_jdk():
    """
    安装JDK
    """
    with cd('/opt'):
        run('tar -zxvf /data/jdk-8u66-linux-x64.tar.gz')
    files.append('~/.bashrc', 'export JAVA_HOME=/opt/jdk1.8.0_66')
    files.append('~/.bashrc', 'export PATH=/opt/jdk1.8.0_66/bin:$PATH')


def passwd_root():
    run('sudo passwd root')


@roles('master')
def init_mysql_driver():
    run('cp /data/python2.7/mysql-connector-java-5.1.41-bin.jar /opt/cm-5.9.0/share/cmf/lib')
    with cd('/opt/cm-5.9.0'):
        """
          更新IP
        """
        run(
            './share/cmf/schema/scm_prepare_database.sh mysql cm -h10.91.7.5 -uroot -padmin --scm-host 192.168.58.1 root admin scm -f')


@roles('master')
def update_master_host():
    config_filename = '/opt/cm-5.9.0/etc/cloudera-scm-agent/config.ini'
    # TODO 改成动态
    files.sed(config_filename, '^server_host=localhost', 'server_host=kylin1', limit='', use_sudo=False, backup='.bak',
              flags='', shell=False)


@roles('master')
def install_cm():
    """
      安装Cloudera manager
    """
    with cd('/opt'):
        run('tar -zxvf /data/cloudera-manager-el6-cm5.9.0_x86_64.tar.gz')
    run('mkdir -p /opt/cloudera/parcels')
    run('cp /data/CDH-5.9.0-1.cdh5.9.0.p0.23-el6.parcel /opt/cloudera/parcels')


@roles('master')
def config_cm():
    """
      配置Cloudera Manager
    """
    execute(init_mysql_driver)
    execute(update_master_host)


@roles('slaves')
def sync_cm():
    """
      同步cm
    :return:
    """
    with cd('/opt'):
        run('scp -r root@%s:/opt/cm-5.9.0 ./' % (MASTER_HOST))


@roles('cdh')
def start_agent():
    run('/opt/cm-5.9.0/etc/init.d/cloudera-scm-agent start')


@roles('master')
def start_server():
    run('/opt/cm-5.9.0/etc/init.d/cloudera-scm-server start')


@roles('master')
def stop_server():
    run('/opt/cm-5.9.0/etc/init.d/cloudera-scm-server stop')


@roles('cdh')
def stop_agent():
    run('/opt/cm-5.9.0/etc/init.d/cloudera-scm-agent stop')


@roles('cdh')
def clear_cm():
    run('rm -fr /opt/cm-5.9.0')


@runs_once
def stop():
    execute(stop_agent)
    execute(stop_server)