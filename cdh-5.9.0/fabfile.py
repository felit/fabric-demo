# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel

env.hosts = ['dev@192.168.181.21', 'dev@192.168.181.22',
             'dev@192.168.181.23', 'dev@192.168.181.24']
env.roledefs = {'cdh': env.hosts,
                'dd': env.hosts[:2]}
res = None
"""
env
{'': True, 'disable_known_hosts': False, 'effective_roles': [], 'tasks': ['get_authorized_keys'], 'linewise': True, 'show': None, 'password': None, 'key_filename': None, 'abort_on_prompts': False, 'skip_unknown_tasks': False, 'reject_unknown_hosts': False, 'skip_bad_hosts': False, 'use_ssh_config': False, 'roledefs': {'dd': ['dev@192.168.181.21', 'dev@192.168.181.22'], 'cdh': ['dev@192.168.181.21', 'dev@192.168.181.22', 'dev@192.168.181.23', 'dev@192.168.181.24']}, 'gateway': None, 'gss_auth': None, 'keepalive': 0, 'eagerly_disconnect': False, 'clean_revert': True, 'rcfile': '/home/congsl/.fabricrc', 'path_behavior': 'append', 'hide': None, 'sudo_prefix': "sudo -S -p '%(sudo_prompt)s' ", 'lcwd': '', 'no_agent': False, 'forward_agent': False, 'remote_interrupt': None, 'port': '22', 'shell': '/bin/bash -l -c', 'version': '1.13.1', 'use_exceptions_for': {'network': False}, 'connection_attempts': 1, 'hosts': ['dev@192.168.181.21', 'dev@192.168.181.22', 'dev@192.168.181.23', 'dev@192.168.181.24'], 'gss_deleg': None, 'new_style_tasks': False, 'cwd': '', 'abort_exception': None, 'real_fabfile': '/data/source/self/fabric-demo/cdh-5.9.0/fabfile.py', 'passwords': {}, 'sudo_password': None, 'host_string': 'dev@192.168.181.22', 'shell_env': {}, 'always_use_pty': True, 'colorize_errors': False, 'exclude_hosts': [], 'all_hosts': ['dev@192.168.181.21', 'dev@192.168.181.22', 'dev@192.168.181.23', 'dev@192.168.181.24'], 'sudo_prompt': 'sudo password:', 'again_prompt': 'Sorry, try again.', 'echo_stdin': True, 'user': 'dev', 'gss_kex': None, 'command_timeout': None, 'path': '', 'local_user': 'congsl', 'combine_stderr': True, 'command_prefixes': [], 'dedupe_hosts': True, 'warn_only': False, 'no_keys': False, 'sudo_passwords': {}, 'roles': [], 'fabfile': 'fabfile', 'use_shell': True, 'host': '192.168.181.22', 'pool_size': 0, 'system_known_hosts': None, 'prompts': {}, 'output_prefix': True, 'command': 'get_authorized_keys', 'timeout': 10, 'default_port': '22', 'ssh_config_path': '/home/congsl/.ssh/config', 'parallel': True, 'sudo_user': None, 'ok_ret_codes': [0]}
<class 'fabric.utils._AttributeDict'>
"""


@parallel(pool_size=5)
def get_authorized_keys():
    # 加一层检查，
    result = run('cat ~/.ssh/authorized_keys')
    print result


@roles('cdh')
def get_id_rsa_public_key():
    result = run('more ~/.ssh/id_rsa.pub')
    return result


@roles('dd')
def second():
    print res
    run('pwd')


@runs_once
def deploy():
    res = execute(get_id_rsa_public_key)
    print res
    for host, key in res.items():
        print host, key
    execute(second)

