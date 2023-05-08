#!/usr/bin/python3
""" A fabric script that distributes an archive to your
web servers"""
from fabric.operations import local, run, put
from fabric.api import env
import time
import os
env.hosts = ["34.203.29.12", "34.227.90.80"]
env.user = "ubuntu"
def do_deploy(archive_path):
    """Deploying to server"""
    if not os.path.exists(archive_path):
        return False
    else:
        file = archive_path[9:]
        new_version = "/data/web_static/releases/" + file[:-4]
        file = "/tmp" + file
        put(archive_path, "/tmp")
        run('sudo mkdir -p {}'.format(new_version))
        run('sudo tar -xzf {} -C {}/'.format(file, new_version))
        run('sudo rm {}'.format(file))
        run('sudo mv {}/web_static/* {}'.format(new_version, new_version))
        run('sudo rm -rf {}/web_static'.format(new_version))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(new_version))
        print("New version deployed")

        return True
