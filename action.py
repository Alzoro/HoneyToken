import os
import shutil
import requests
import subprocess
from pathlib import Path


destination = "/home/jones/Minor/.dump"
def stop(pid):
    pid=int(pid)
    os.kill(pid,9)


def move(path):
    try:
        p=Path(path)
        if p.parent.name in ['home','jones']:
            shutil.move(path,destination)
        elif p.parent.name in ['temp','Downloads','Desktop','Music','Templates','Videos','Pictures','Public','Documents']:
            base=Path(destination)/str(p.parent.name)
            base.mkdir(parents=True, exist_ok=True)
            for file in p.parent.iterdir():
                if file.is_file():
                    shutil.move(str(file),str(base))
        else:
            shutil.move(str(p.parent),destination)
    except FileNotFoundError :
        token="7260439440:AAE-jXdEPf385_nuxBgQpMUJ04YBtEkrX3k"
        id="5106130605"
        msg=f"The file got deleted"
        url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={msg}"
        requests.get(url)        


def hnyTok_bot():
    token="7260439440:AAE-jXdEPf385_nuxBgQpMUJ04YBtEkrX3k"
    id="5106130605"
    msg=f"Alert!!\n{get_msg()}"
    url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={msg}"
    requests.get(url)

def get_msg():
    with open("/home/jones/Minor/HoneyToken/log_status.log","r") as f:
        f.seek(0)
        l=f.readlines()
        return l[-1]

def clear():
    subprocess.run("clear",shell=True)