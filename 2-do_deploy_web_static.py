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
    try:
        """Deploying an archive to server"""
        if not os.path.exists(archive_path):
            return False
        #uploading of files
        put(archive_path, "/tmp/")
        file = archive_path[-18:-4]
        run("sudo mkdir -p /data/web_static/\releases/web_static_{}".format(file))
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C \ /data/web_Static/releases/web_static_{}/".format(file, file))
        run("sudo rm /tmp/web_static_{}.tgz".format(file))
        run("sudo mv /data/web_static/releases/web_static_{}/web_static/*\ /data/web_static/releases/web_static_{}/".format(file, file))
        run("sudo rm -rf /data/web_Static/releases/\web_static_{}/web_static".format(file))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/\ web_static_{}/ /data/web_static/current".format(file))
    except:
        return False
    return True
