#!/usr/bin/python3
""" A fabric script for deploying"""
from fabric.api import *

env.hosts = ['34.203.29.12', '34.227.90.80']
env.user = "ubuntu"

def do_clean(number=0):
    """ A fabric script that deletes out of date archives """
    number = int(number)
    if number == 0:
        number = 1
    else:
        number

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    way = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(way, number))
