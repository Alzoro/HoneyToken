import os
import typer as t   #pip install typer
from termcolor import colored #pip install termcolor
import subprocess
import daemon
import pickle
from watchdog.observers import Observer    #pip install watchdog
from watchdog.events import FileSystemEventHandler

state_log='/home/jones/Minor/h.monitor_state.pkl'
admin='jones'

def get_usr(fpath):
    try:
        res=subprocess.run(['lsof',fpath], capture_output=True, text=True)
        for line in res.stdout.splitlines():
            if fpath in line:
                p=line.split()
                user=p[2]
                return user
    except Exception as e:
        t.echo(colored("Error getting file user:","yellow") + colored(e,"red"))
    return None

