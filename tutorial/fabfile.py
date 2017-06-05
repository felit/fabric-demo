from __future__ import with_statement
from fabric.api import run
from fabric.api import local
import logging
from fabric.api import local, settings, abort, lcd, cd, get, env,roles
from fabric.contrib.console import confirm

# logging.basicConfig(level=logging.DEBUG)
env.roledefs = {
    'test': {
        'host': 'localhost',
        'env': 'content'
    }

}

@roles('test')
def host_type():
    run('uname -s')
    # run('ps -ef')


# fab hello:name=fabric,action="go go go"
def hello(name='world', action='get away'):
    print 'Hello %s,%s' % (name, action)


def local_test():
    local('git status')

def get_ip():
    result = run("ifconfig| grep 192| awk -F: '{print$2}'| awk '{print $1}'")
    print result
# Failure Handling
def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


# lcd local
def test_lcd():
    with lcd('/home/congsl'):
        result = local('ls')
        print result
        print result.__class__
    with settings(warn_only=True):
        if local('ls', capture=True).failed:
            local('pwd')


# cd run
def test_cd():
    code_dir = '/home/congsl'
    with cd(code_dir):
        run("pwd")
        run("ls")


def get_public_key():
    result = run('more ~/.ssh/id_rsa.pub')
    print result


def get_file():
    get('~/.ssh/id_rsa.pub')