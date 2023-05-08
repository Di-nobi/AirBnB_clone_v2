#!/usr/bin/python3
""" A fabric script for deploying"""
from fabric.api import *

env.hosts = ['34.203.29.12', '34.227.90.80']
env.user = "ubuntu"

def do_clean(number=0):


