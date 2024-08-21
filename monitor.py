import os
import typer as t   #pip install typer
from termcolor import colored #pip install termcolor
import subprocess
import time
from pathlib import Path
import pickle
import signal
from watchdog.observers import Observer    #pip install watchdog
from watchdog.events import FileSystemEvent, FileSystemEventHandler

state_log='/home/jones/Minor/h.monitor_state.pkl'
admin='jones'
final_path='/home/jones/Minor'
f_pid=0

def change_admin():
    t.echo(colored("\n\tAdmin name will reset to default after exiting the program.\n","yellow"))
    t.echo(colored("\nCurrent admin: ",'yellow') + colored(f"{admin}\n","green"))
    new=input("New admin: ")
    admin=new



def get_usr(path):
    try:
        res=subprocess.run(['lsof',path], capture_output=True, text=True)
        for line in res.stdout.splitlines():
            if path in line:
                p=line.split()
                user=p[2]
                return user
    except Exception as e:
        t.echo(colored("Error getting file user:","yellow") + colored(e,"red"))
    return None


class Honeytoken(FileSystemEventHandler):
    def process_event(self, event):
        user=get_usr(final_path)
        if user and user != admin:
            t.echo(f"\n{event.src_path}\n")
            t.echo("\n\t\tAlert\n")
        else:
            t.echo("\n\t\tSuccess\n")

    def on_modified(self, event):
        self.process_event(event)

    def on_deleted(self, event):
        self.process_event(event)
    
    def on_accessed(self, event):
        self.process_event(event)

    def on_opened(self, event):
        self.process_event(event)

def monitor_honeytoken(f_path):
    e_handle=Honeytoken()
    obs=Observer()
    obs.schedule(e_handle,path=f_path,recursive=False)
    obs.start()

    try:
        while True:
            time.sleep(2)    
    except KeyboardInterrupt:
        obs.stop()
    obs.join()


def start_monitoring():
    while True:
        while True:
            p_input=input("Path of the directory (without file name): ")
            path=Path(p_input)

            if p_input == "exit":
                break

            if path.is_dir():
                if path.is_absolute():
                    final_path = p_input
                    break
                else:
                    t.echo(colored("\n\t\tPlease provide the absolute directory\n","yellow"))
            else:
                t.echo(colored("\n\t\tPlease provide a valid directory\n","yellow"))

        while True:
            fn=input("File name: ")

            if Path(fn).suffix() in ['txt','conf','ini','docx','sql','pem','env','json','log']:
                f_path=os.path.join(p_input,fn)
                break
            else:
                t.echo(colored("\n\t\tPlease provide a valid file name\n","yellow"))

        if os.path.exists(f_path):
            pid=os.fork()                             #start of daemon process
            time.sleep(4)
            if pid == 0:
                with open(state_log,"wb") as f:
                    pickle.dump({'Monitoring':True, 'path':f_path, 'pid':os.getpid()},f)
                
                f_pid=os.getpid()
                monitor_honeytoken(f_path)

            else:
                t.echo(colored(f"\nMonitoring started in background\n","blue"))
                os._exit(0)
        else:
            t.echo(colored("\n\tNo such file found at the path\n\tPlease provide an existing file path, or use ","yellow") + colored("-deploy ","magenta") + colored("to create one\n","yellow"))


def stop_monitoring():
    if os.path.exists(state_log):
        try:
            with open(state_log,"rb") as f:
                state=pickle.load(f)
                if state.get('Monitoring'):
                    pid=state.get('pid')
                    if pid:
                        try:
                            os.kill(pid,signal.SIGTERM)
                            t.echo(colored(f"\nMonitoring stopped. Process ID: {pid}\n","blue"))
                            os.remove(state_log)
                        except ProcessLookupError:
                            t.echo(colored("\nNo such process. Monitoring may not be running.\n","yellow"))
                        except Exception as e:
                            t.echo(colored("\nError in stopping monitoring: " + colored(e,"red")))
                    else:
                        t.echo(colored("\nNo PID found in the state file.\n","yellow"))
                else:
                    t.echo(colored("\nMonitoring is not active\n","blue"))
        except (EOFError , pickle.UnpicklingError):
            t.echo(colored("\nState file is empty or corrupted.\n","yellow"))
            os.remove(state_log)
    else:
        t.echo(colored("\nNo monitoring state file found.\n","yellow"))



def check_monitoring_status():
    if os.path.exists(state_log):
        try:
            if os.path.getsize(state_log) != 0:
                with open(state_log,"rb") as f:
                    state = pickle.load(f)
                    if state.get('Monitoring'):
                        t.echo(colored(f"\nMonitoring is active in {state.get('path')} \n","blue"))
                    else:
                        t.echo(colored("\nMonitoring is not active\n","blue"))
            else:
                t.echo(colored("\nMonitoring is not active\n","blue"))
        except (EOFError , pickle.UnpicklingError):
            t.echo(colored("\nState file is empty or corrupted.\n","yellow"))
            os.remove(state_log)
    else:
        t.echo(colored("\nNo monitoring state file found\n","yellow"))


def pid():
    if os.path.exists(state_log):
        try:
            if os.path.getsize(state_log) != 0:
                with open(state_log,"rb") as f:
                    state = pickle.load(f)
                    p=state.get('pid')
                    t.echo(colored("\nMonitoring Process ID: ","blue") + colored(f"{p}\n","yellow") )
            else:
                t.echo(colored("\nMonitoring is not active\n","blue"))
        except (EOFError , pickle.UnpicklingError):
            t.echo(colored("\nState file is empty or corrupted.\n","yellow"))
            os.remove(state_log)
    else:
        t.echo(colored("\nNo monitoring details found\n","yellow"))