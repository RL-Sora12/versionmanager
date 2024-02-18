import subprocess
import requests
import re
from bs4 import BeautifulSoup
import zipfile
import os

def get_version(name):
    verNameList = ["version","-version","--version","-V","-VV"]
    for verName in verNameList:
        try:
            version_output = subprocess.check_output([name, verName], stderr=subprocess.STDOUT)
            version_output = version_output.decode('utf-8')
            version_line = version_output.splitlines()[0]
            version = version_line
            return version
        except subprocess.CalledProcessError:
            version = None
        except FileNotFoundError:
            version = None
    return None
