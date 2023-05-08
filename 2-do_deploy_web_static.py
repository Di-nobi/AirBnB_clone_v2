#!/usr/bin/python3
""" A fabric script that distributes an archive to your
web servers"""
from fabric.operations import local, run, put
from fabric.api import env
import time
import os
env.hosts = ["34.203.29.12", "34.227.90.80"]
env.user = "ubuntu"
def do_pack():
    """Function that compress files in an archive"""
    local("mkdir -p versions")
    final = local("tar -cvzf versions/web_static_{}.tgz web_static/".format(time.strftime("%Y%m%d%H%M%S")))
    if final.failed:
        return None
    return final

def do_deploy(archive_path):
    """Deploying an archive to server"""
    if not os.path.exists(archive_path):
        return False
    filed = archive_path[9:]
    new_version = "/data/web_static/releases/" + filed[:-4]
    filed = "/tmp/" + filed
    #uploading of files
    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(new_version))
    run("sudo tar -xzf {} -C {}/".format(filed, new_version))
    run("sudo rm /tmp/{}.tgz".format(filed))
    run("sudo mv {}/web_static/* {}".format(filed, filed))
    run("sudo rm -rf {}/web_static".format(new_version))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(new_version))

    print("New version deployed!")
    return True
