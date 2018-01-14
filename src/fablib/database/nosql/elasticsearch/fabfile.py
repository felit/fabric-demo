# -*- coding:utf8 -*-
"""
1、安装
2、输入
3、优化、并发
"""
from __future__ import with_statement
from fabric.api import parallel, task, run

# env.hosts = ['dev@192.168.181.21',
# 'dev@192.168.181.22',
# 'dev@192.168.181.23',
#              'dev@192.168.181.24']
url = "https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.6.3.tar.gz"


@task
@parallel
def install():
    run("wget %s" % url)


def install_jieba():
    # https://github.com/sing1ee/elasticsearch-jieba-plugin/archive/v5.2.0.tar.gz
    #build/distributions/elasticsearch-jieba-plugin-5.2.0.zip
    pass


def install_plugin_head():
    pass


def install_elasticsearch_sql():
    pass