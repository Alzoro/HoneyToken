import os
import typer as t   #pip install typer
from termcolor import colored #pip install termcolor
import subprocess
import daemon    #pip install daemon
import time
import pickle
from watchdog.observers import Observer    #pip install watchdog
from watchdog.events import FileSystemEvent, FileSystemEventHandler

state_log='/home/jones/Minor/h.monitor_state.pkl'
admin='jones'
fpath='/home/jones/Minor'

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


class Honeytoken(FileSystemEventHandler):
    def process_event(self, event):
        user=get_usr(fpath)
        if user and user != admin:
            t.echo(f"\n{event.src_path}\n")
            t.echo("\n\t\tAlert\n")
        else:
            t.echo(f"\n{event.src_path}\n")
            t.echo("\n\n\tsuccess\n\n")

    def on_modified(self, event):
        t.echo("\n\tmodified\n")
        self.process_event(event)

    def on_deleted(self, event):
        t.echo("\n\tdeleted\n")
        self.process_event(event)
    
    def on_accessed(self, event):
        t.echo("\n\taccessed\n")
        self.process_event(event)

    def on_opened(self, event):
        t.echo("\n\topened\n")
        self.process_event(event)

def monitor_honeytoken(path):
    e_handle=Honeytoken()
    obs=Observer()
    obs.schedule(e_handle,path=path,recursive=False)
    obs.start()

    try:
        while True:
            time.sleep(2)    
    except KeyboardInterrupt:
        obs.stop()
    obs.join()

monitor_honeytoken('/home/jones/Minor/test.txt')
