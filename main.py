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

    f_name=input("File name (with extension): ")
    f_create(f_name,path)
        


def f_create(f_name,path):
    ext=Path(f_name).suffix
    t.echo(colored("\n\t\t-[","green") + colored("-d","magenta") + colored("]- for default content"))
    t.echo(colored("\t\t-[","green") + colored("-c","magenta") + colored("]- for custom content\n"))
    if ext == ".txt":
        default="""# Sensitive Information

Username: admin
Password: P@ssw0rd1234

API Key: 12345-abcde-67890-fghij
Secret Token: 98765-zyxwv-43210-lmnop
"""
        try:
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
            t.echo(f"An error occurred: {e}")
                


        
def custom():
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