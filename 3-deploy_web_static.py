#!/usr/bin/python3
""" Deployment with Fabric """
import os
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['
