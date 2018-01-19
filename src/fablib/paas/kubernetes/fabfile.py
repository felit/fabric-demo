# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import sudo, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task, settings, local
from fabric.contrib import files
import logging

env.hosts = [
    'vagrant@192.168.18.190'
]
env.password = "vagrant"
"""
centos7
http://blog.csdn.net/lic95/article/details/55015284
"""


@task
def install():
    # sudo('yum update -y')
    sudo('yum makecache')
    sudo('yum install -y etcd kubernetes ntp flannel')
    sudo('systemctl disable firewalld')
    sudo('systemctl stop firewalld')
    sudo('hostname k8s-master')
    sudo('echo k8s-master > /etc/hostname')
    files.append('/etc/etcd/etcd.conf', """
ETCD_NAME=default
ETCD_DATA_DIR="/var/lib/etcd/default.etcd"
ETCD_LISTEN_CLIENT_URLS="http://localhost:2379,http://192.168.18.190:2379"
ETCD_ADVERTISE_CLIENT_URLS="http://192.168.18.190:2379"
    """)
    files.append('/etc/kubernetes/config', """
KUBE_LOGTOSTDERR="--logtostderr=true"
KUBE_LOG_LEVEL="--v=0"
KUBE_ALLOW_PRIV="--allow-privileged=false"
KUBE_MASTER="--master=http://192.168.18.190:8080"
    """)
    files.append('/etc/kubernetes/apiserver', """
KUBE_API_ADDRESS="--insecure-bind-address=0.0.0.0"
KUBE_ETCD_SERVERS="--etcd-servers=http://192.168.18.190:2379"
KUBE_SERVICE_ADDRESSES="--service-cluster-ip-range=192.168.18.190/16"
KUBE_ADMISSION_CONTROL="--admission-control=AlwaysAdmit"
KUBE_API_ARGS=""
    """)
    files.append("/etc/kubernetes/controller-manager", """
KUBE_CONTROLLER_MANAGER_ARGS=""
    """)
    files.append("/etc/kubernetes/scheduler", """
KUBE_SCHEDULER_ARGS="--address=0.0.0.0"
    """)


@task
def start():
    sudo("""
    for SERVICES in etcd kube-apiserver kube-controller-manager kube-scheduler
    do
        systemctl restart $SERVICES
        systemctl enable $SERVICES
        systemctl status $SERVICES
    done
    """)


@task
def config_etcd():
    sudo("""
    etcdctl set /k8s/network/config '{"Network": "10.255.0.0/16"}'
    """)
    sudo('etcdctl get /k8s/network/config')


@task
def status():
    sudo('kubectl version')
    sudo('kubectl get nodes')


@task
def config_ssh():
    sudo('mkdir .ssh')
    sudo('chmod 700 .ssh')
    sudo('touch .ssh/authorized_keys')
    sudo('chmod 600 .ssh/authorized_keys')
    files.append('.ssh/authorized_keys', """
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJXAZx0EzfFtyoFJvimiP1J4/XZZU7WOtx/cH2/dHAi5eBjqk5WjSRVgYGmJWCrivE2KEub25fGqR1wVnZXSfP3x9PsQnE5eO5I/K2OAfUGakHVZeYKm3J5ADryxcRxcKj8d0Y+/PHSyrL0smN+ZyyYqFJ2nfW2tGYKAK9bwdwjcf/QgnR558SbWAjKmBp81JUxQUpkNO+Hv4yIaPPbsYXsVk752DjIrgsE2riGrjCLju1yBu6T7mYw0wEpn4XrE0WQfyZkBRV/BS4Iz1iFYQExrsWaJbe82Gt00TJksbJJN81FGtllmo1AdGTVonwpv3dAS6AMfT2RcFrPZw018v congsl@congsl
    """)

def test_file():
    pass