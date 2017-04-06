import ssh.fabfile2
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd,task
# env.hosts = ['vagrant@192.168.36.10']
env.hosts = ['vagrant@192.168.58.10', 'vagrant@192.168.58.12', 'vagrant@192.168.58.13']
# env.passwords={
#     'vagrant@192.168.58.10':'vagrant',
#     'vagrant@192.168.58.12':'vagrant',
#     'vagrant@192.168.58.13':'vagrant'
# }
# TODO password
env.roledefs = {'master': env.hosts[0:1]}
