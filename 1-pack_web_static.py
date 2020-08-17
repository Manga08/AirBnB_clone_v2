#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """Function to generate version compressed files"""
    local("mkdir -p versions")
    Name_Fl = "web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    archive = local("tar -zcvf versions/{} web_static".format(Name_Fl))

    if archive.failed:
        return None
    return Name_Fl
