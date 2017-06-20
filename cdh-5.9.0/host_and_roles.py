
# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
env.hosts = [
    # 'root@139.198.6.107',
    'pgxc@192.168.18.160',
    'pgxc@192.168.18.164',
    'pgxc@192.168.18.165',
    'pgxc@192.168.18.166',
    'pgxc@192.168.18.167',
    'pgxc@192.168.18.168',
]
env.password = 'pgxc'
env.roledefs = {'cdh': env.hosts,
                'master': env.hosts[:1],
                'slaves': env.hosts[1:],
                'mysql': env.hosts[:1],
                'interflow_hosts': env.hosts
}
from ssh import fabfile
@runs_once
@task
def add_keys():
    execute(fabfile.add_public_key_authorizied_keys, add_keys=[
        'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJXAZx0EzfFtyoFJvimiP1J4/XZZU7WOtx/cH2/dHAi5eBjqk5WjSRVgYGmJWCrivE2KEub25fGqR1wVnZXSfP3x9PsQnE5eO5I/K2OAfUGakHVZeYKm3J5ADryxcRxcKj8d0Y+/PHSyrL0smN+ZyyYqFJ2nfW2tGYKAK9bwdwjcf/QgnR558SbWAjKmBp81JUxQUpkNO+Hv4yIaPPbsYXsVk752DjIrgsE2riGrjCLju1yBu6T7mYw0wEpn4XrE0WQfyZkBRV/BS4Iz1iFYQExrsWaJbe82Gt00TJksbJJN81FGtllmo1AdGTVonwpv3dAS6AMfT2RcFrPZw018v congsl@congsl'])
@task
def add_to_bashrc():
    files.append('.bashrc', 'export PGHOME=/opt/pgx2')
    files.append('.bashrc', 'export PGUSER=pgxc')
    files.append('.bashrc', 'export LD_LIBRARY_PATH=$PGHOME/lib:$LD_LIBRARY_PATH')
    files.append('.bashrc', 'export PATH=$PGHOME/bin:$PATH')