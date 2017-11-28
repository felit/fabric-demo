# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files

env.hosts = [
    # 'root@139.198.6.107'
    # 'root@192.168.0.3'
    'vagrant@192.168.33.10',
    'vagrant@192.168.33.11',
    'vagrant@192.168.33.12'
]
env.password="vagrant"


@task
@parallel
def install_erlang():
    # run('yum -y install ncurses-devel openssl-devel gcc-c++  ')
    # run('yum -y install make gcc gcc-c++ kernel-devel m4 ncurses-devel openssl-devel wget')

    content="""
        deb http://mirrors.163.com/ubuntu/ precise-updates main restricted
        deb-src http://mirrors.163.com/ubuntu/ precise-updates main restricted
        deb http://mirrors.163.com/ubuntu/ precise universe
        deb-src http://mirrors.163.com/ubuntu/ precise universe
        deb http://mirrors.163.com/ubuntu/ precise-updates universe
        deb-src http://mirrors.163.com/ubuntu/ precise-updates universe
        deb http://mirrors.163.com/ubuntu/ precise multiverse
        deb-src http://mirrors.163.com/ubuntu/ precise multiverse
        deb http://mirrors.163.com/ubuntu/ precise-updates multiverse
        deb-src http://mirrors.163.com/ubuntu/ precise-updates multiverse
        deb http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
        deb-src http://mirrors.163.com/ubuntu/ precise-backports main restricted universe multiverse
    """
    files.append('/etc/apt/sources.list',content,use_sudo=True)
    sudo('apt update')
    sudo('apt install -y libnss3 erlang')

    # sudo('apt -y install make gcc g++ m4 libncurses5-dev openssl wget')
    # run('wget http://erlang.org/download/otp_src_20.0.tar.gz -o otp_src.tar.gz')
    # run('tar -zxvf otp_src.tar.gz')
    # run('mv otp_src_20.0 otp')
    # with cd('otp'):
    #     run('./configure --prefix=/opt/erlang --without-javac')
    #     run('make && make install')
#         TODO 设置路径


@task
@parallel
def install_rabbitmq():
    sudo('apt install -y xz-utils')
    # run('wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-generic-unix-3.6.1.tar.xz -o rabbitmq-server-generic-unix-3.6.1.tar.xz')
    # run('yum install -y xz')

    # run('rm rabbitmq-server-generic-unix-3.6.1.tar')
    run('wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-generic-unix-3.6.1.tar.xz -O rabbitmq-server-generic-unix-3.6.1.tar.xz')
    run('xz -d rabbitmq-server-generic-unix-3.6.1.tar.xz')
    run('tar -xvf rabbitmq-server-generic-unix-3.6.1.tar')
    sudo('cp -rf ./rabbitmq_server-3.6.1 /usr/local/')

    with cd('/usr/local/'):
        sudo('mv rabbitmq_server-3.6.1 rabbitmq-3.6.1')
@task
def start():
    # files.append('/etc/environment','PATH=/usr/local/rabbitmq-3.6.1/sbin:$PATH',use_sudo=True)
    run('/usr/local/rabbitmq-3.6.1/sbin/rabbitmq-server -detached')
@task
@parallel
def status():
    run('ls -l /usr/local/rabbitmq-3.6.1')
    sudo('apt install -y vim git')
    # run('pwd')
    # sudo('chown -R vagrant:vagrant /usr/local/rabbitmq-3.6.1')
    # '/usr/local/rabbitmq-3.6.1/sbin'
    # run('ps -ef | grep rabbit| grep -v grep',pty=False,shell=False)
    # run('rabbitmqctl status')
@task
def add_user():
    # run('/usr/local/rabbitmq-3.6.1/sbin/rabbitmqctl add_user admin admin')
    run('/usr/local/rabbitmq-3.6.1/sbin/rabbitmqctl set_user_tags admin administrator')
def master():
    pass
def slave():
    run('')