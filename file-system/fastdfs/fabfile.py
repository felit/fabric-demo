# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, show
from fabric.contrib import files

env.hosts = ['dev@192.168.181.21',
             'dev@192.168.181.22',
             'dev@192.168.181.23',
             'dev@192.168.181.24']

fastdfs_url = "https://downloads.sourceforge.net/project/fastdfs/FastDFS%20Server%20Source%20Code/FastDFS%20Server%20with%20PHP%20Extension%20Source%20Code%20V1.27/FastDFS_v1.27.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Ffastdfs%2Ffiles%2FFastDFS%2520Server%2520Source%2520Code%2F&ts=1495071845&use_mirror=jaist fastdfs.tar.gz"


@task
def install_dfs():
    # 下载fastdfs
    run("wget -O fastdfs.tar.gz %s" % fastdfs_url)
    # 解压fastdfs tar -zxvf
    # ./make.sh
    # ./make.sh install
    # copy配置文件
    pass


@task
def start_dfs():
    # 启动dfs服务
    pass


def install_nginx_modules():
    # run('fastdfs-nginx-module')
    pass


def install_apache_modules():
    # fastdfs-apache-module
    pass


def install_dht():
    pass
