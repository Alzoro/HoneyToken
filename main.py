import typer as t
from art import text2art
from termcolor import colored
import os
from pathlib import Path


app=t.Typer()

def intractive_mode():
    pre_info()
    htok=colored("hTok > ",color="light_red")
    while True:
        command=input(htok)
        if command == "-help":
            help()
        elif command == "-deploy":
            honeytoken_deploy()
        elif command.lower() == "exit":
            break
        else:
            con=colored("\n\t\tUnknown command!\n\tTry -help for help or 'exit' to quit.\n",color="yellow")
            t.echo(con)


def pre_info():   #Info displayed at the beging of the tool
    art=text2art("h.Tok",font="varsity")
    t.echo(colored(art,"green"))
    text1=colored("\t\t  Dynamic Honeytoken Monitoring",color="light_red")
    t.echo(text1)
    te="""
    -[Elevate your cybersecurity game with our h.Tok tool]-
    -[Strategically deploy deceptive honeytokens throughout your file system]-
    -[Provide real-time monitoring and alerting with detailed logs]-
    -[Help you stay ahead of threats and fortify your defenses]-
    """
    t.echo(colored(te,color="green"))
    t.echo(colored("\t\t< ","green") + colored("-help ","yellow") + colored("for help or '","green" ) + colored("exit","yellow") + colored("' to quit >\n","green"))

def honeytoken_deploy():

    while True:
        p_input=input("Specify the path (absolute path): ")
        path=Path(p_input)

        if p_input == "exit":
            break

        if not path.is_absolute():
            t.echo(colored("\n\t\tPlease provide the absolute path\n","yellow"))
        else:
            break
    
    if not path.parent.exists():
        try:
            path.mkdir(parents=True,exist_ok=True)
            t.echo("\nCreated directories for the path: " + colored(path,"magenta") + "\n")
        except Exception as e:
            t.echo(colored(f"An error occured while creating directories: {e}","yellow"))
    elif path.exists():
        t.echo("\nCurrent path: " + colored(path,"magenta") + "\n")
    else:
        path.mkdir(exist_ok=True)
        t.echo(f"Created directories for the path: {path}")

    t.echo(colored("\t\tSupported file types","green"))
    t.echo(colored("\t\t-[","green") + colored(".txt ","magenta")+ colored("]-  Text File","green"))
    t.echo(colored("\t\t-[","green") + colored(".conf","magenta")+ colored("]-  Configuration File","green"))
    t.echo(colored("\t\t-[","green") + colored(".ini ","magenta")+ colored("]-  Initialization File","green"))
    t.echo(colored("\t\t-[","green") + colored(".docx","magenta")+ colored("]-  Microsoft Word Document (Open XML Document)","green"))
    t.echo(colored("\t\t-[","green") + colored(".sql ","magenta")+ colored("]-  Structured Query Language File","green"))
    t.echo(colored("\t\t-[","green") + colored(".db  ","magenta")+ colored("]-  Database File","green"))
    t.echo(colored("\t\t-[","green") + colored(".env ","magenta")+ colored("]-  Environment File","green"))
    t.echo(colored("\t\t-[","green") + colored(".json","magenta")+ colored("]-  JavaScript Object Notation File","green"))
    t.echo(colored("\t\t-[","green") + colored(".log ","magenta")+ colored("]-  Log File","green"))

    while True:
        f_name=input("File name (with extension): ")
        ext=Path(f_name).suffix
        if ext in [".txt",".conf",".ini",".sql",".log"]:
            f_create(f_name,path)
            break
        else:
            t.echo(colored("\n\t\tUnsupported file format\n","yellow"))
        


def f_create(f_name,path):
    ext=Path(f_name).suffix
    default=""" """
    t.echo(colored("\n\t\t-[","green") + colored("-d","magenta") + colored("]- for default content"))
    t.echo(colored("\t\t-[","green") + colored("-c","magenta") + colored("]- for custom content\n"))
    if ext == ".txt":                   #For text file
        default="""# Sensitive Information

Username: admin
Password: P@ssw0rd1234

API Key: 12345-abcde-67890-fghij
Secret Token: 98765-zyxwv-43210-lmnop
"""
    elif ext == ".conf":                #For Configuration File
        default="""# Application Configuration

database {
    host = "db.example.com"
    port = 5432
    user = "dbuser"
    password = "dbpass"
}

server {
    host = "0.0.0.0"
    port = 8080
}

logging {
    level = "INFO"
    file = "/var/log/application.log"
}
"""
    elif ext == ".ini":                  #For Initialization File
        default="""[Database]
host = db.example.com
port = 5432
username = dbuser
password = dbpass

[Server]
host = 0.0.0.0
port = 8080

[Logging]
logfile = /var/log/app.log
loglevel = INFO
"""
    elif ext == ".sql":                     #For Structured Query Language File
        default="""-- Database Schema

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    level VARCHAR(20),
    message TEXT
);

INSERT INTO users (username, password, email) VALUES
('admin', 'P@ssw0rd1234', 'admin@example.com'),
('user', 'User1234', 'user@example.com');
"""
    elif ext == ".log":                         #For log file
        default="""[2024-08-07 10:00:00] ERROR - Failed to connect to database: db.example.com:5432
[2024-08-07 10:05:00] INFO - Server started on 0.0.0.0:8080
[2024-08-07 10:10:00] WARN - Deprecated API used in request: GET /api/v1/old-endpoint
[2024-08-07 10:15:00] ERROR - Unexpected token in JSON response from API
"""

    try:                                       #To create the file
        with open(path/f_name,"w+") as file:
            while True:
                ct=input("Select one: ")
                if ct == "-d":
                    file.write(default)
                    t.echo("\nFile created\nFile content:\n")
                    file.seek(0)
                    c=file.read()
                    t.echo(c)
                    break
                elif ct == "-c":
                    file.write(custom())
                    t.echo("\nFile created\nFile content:\n")
                    file.seek(0)
                    c=file.read()
                    t.echo(c)
                    break
                else:
                    t.echo(colored("\n\t\tInvalid input\n","yellow"))
    except Exception as e:
        t.echo(colored("An error occurred: ","yellow") + colored(e,"red"))
        



        
def custom():                                #To get the customized input from the user to add in the file
    t.echo("Enter your custom content (type '-END' on a new line to finish)\n")
    lines=[]
    while True:
        l=input()
        if l == "-END" or l=="-end":
            break
        lines.append(l)
    
    return '\n'.join(lines)


@app.command()
def line():
    intractive_mode()

def help():
    t.echo("\n\nhelping\n\n")


if __name__ == "__main__":
    app()