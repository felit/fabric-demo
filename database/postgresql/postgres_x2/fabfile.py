# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
from fabric.contrib import files
# TODO
env.hosts = [
    # 'root@139.198.6.107',
    'vagrant@192.168.18.160',
    'vagrant@192.168.18.164',
    'vagrant@192.168.18.165',
    'vagrant@192.168.18.166',
    'vagrant@192.168.18.167',
    'vagrant@192.168.18.168',
]
env.password = 'vagrant'
env.roledefs = {
    'gtm': ['pgxc@192.168.18.164'],
    'gtm_standby': ['pgxc@192.168.18.165'],
    'datanode': [''],
    'coord': ['pgxc@192.168.18.166'],
}
"""
TODO
配置: coord/postgresql.conf
CREATE NODE dn3 WITH (TYPE='datanode', PORT=5432, HOST='192.168.18.167', primary);
CREATE NODE dn4 WITH (TYPE='datanode', PORT=5432, HOST='192.168.18.168');
"""


@parallel
def yum():
    sudo('yum install -y wget unzip')


@parallel
def pre_requirement():
    sudo(
        'yum -y install gcc* libtool* libxml2-devel readline-devel flex bison crypto* perl-ExtUtils-Embed zlib-devel pam-devel libxslt-devel openldap-devel python-devel openssl-devel cmake')


@parallel
def get_tar_files():
    run('wget https://github.com/postgres-x2/postgres-x2/archive/REL1_2_STABLE.zip')
    run('unzip REL1_2_STABLE.zip')
    sudo('mkdir -p /opt/pgx2')
    sudo('chown -R vagrant:vagrant /opt/pgx2')
    run('cd postgres-x2-REL1_2_STABLE; ./configure --prefix=/opt/pgx2 && make && make install')


@roles('gtm')
def init_gtm():
    """
       初始化gtm节点
    :return:
    """
    run('initgtm -Z /home/pgxc/gtm -D gtm')


@roles('coord')
def init_coord():
    """
        初始化协调节点
        :return:
    """
    run('rm -fr /home/pgxc/coord')
    run('initdb -D /home/pgxc/coord --nodename co')


@roles('datanode')
def init_datanode():
    """
       初始化数据节点
       TODO　dn名称
        :return:
    """
    run('mkdir /home/pgxc/datanode')
    run('initdb -D /home/pgxc/coord --nodename dn1')


def config_datanode_and_coord():
    """
        更新 pg_hba.conf
        更新 postgres.conf
        TODO gtm IP
    :return:
    """
    files.append('pg_hba.conf', 'host    all              pgxc        192.168.0.0/16            trust')
    files.append('postgres.conf', "listen_addresses = '*'")
    files.append('postgres.conf', "gtm_host = '192.168.18.164'")


def start_gtm():
    run('gtm -D gtm')


def start_coord():
    run('')


def add_to_bashrc():
    files.append('.bashrc', 'export PGHOME=/opt/pgx2')
    files.append('.bashrc', 'export PGUSER=pgxc')
    files.append('.bashrc', 'export LD_LIBRARY_PATH=$PGHOME/lib:$LD_LIBRARY_PATH')
    files.append('.bashrc', 'export PATH=$PGHOME/bin:$PATH')


def shutdown_iptables():
    sudo('chkconfig iptables off')
    sudo('service iptables stop')


def add_user_and_groups():
    """
      添加判断
    :return:
    """
    sudo('groupadd pgxc')
    sudo('useradd -g pgxc pgxc')
    sudo('passwd pgxc')