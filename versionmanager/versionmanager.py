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
    
def download_version(name):
    if name == "java":
        url = "https://www.java.com/en/download/"
    elif name == "python":
        url = "https://www.python.org/downloads/"
    response = requests.get(url)
    if response.status_code != 200:
        print("ページを取得できませんでした。")
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    version_element = soup.find("div", {"class": "product_version"})
    if version_element is None:
        print("バージョン情報が見つかりませんでした。")
        return None
    version_text = version_element.text.strip()
    version_text

    return version_text
