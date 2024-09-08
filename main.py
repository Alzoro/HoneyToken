import typer as t #pip install typer
from art import text2art #pip install art
from termcolor import colored #pip install termcolor
import deploy
import monitor

app=t.Typer()

def intractive_mode():
    pre_info()
    htok=colored("hTok > ",color="light_red")
    while True:
        command=input(htok)
        if command == "-help":
            help()
        elif command == "-deploy":
            deploy.honeytoken_deploy()
        elif command == "-start":
            monitor.start_monitoring()
        elif command == "-stop":
            monitor.stop_monitoring()
        elif command == "-status":
            monitor.check_monitoring_status()
        elif command == "-pid":
            monitor.pid()
        elif command.lower() == "exit":
            break
        else:
            con=colored("\n\t\tUnknown command!\n\tTry","yellow" ) + colored("-help","magenta") + colored("for help or 'exit' to quit.\n",color="yellow")
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
    t.echo(colored("\n   - Once monitoring begins, the program will automatically exit. -\n","yellow"))
    t.echo(colored("\t\t< ","green") + colored("-help ","magenta") + colored("for help or '","green" ) + colored("exit","magenta") + colored("' to quit >\n","green"))




def help():
    t.echo(colored("\n\n\t-deploy","magenta") + colored("\t\t-\tTo deploy the honeytoken in any desired directory location."))
    t.echo(colored("\t-start","magenta") + colored(" \t\t-\tTo start the honeytoken monitoring process."))
    t.echo(colored("\t-status","magenta") + colored("\t\t-\tTo Check the status of the honeytoken monitoring."))
    t.echo(colored("\t-pid","magenta") + colored("   \t\t-\tTo retrieve the process ID for the honeytoken monitoring."))
    t.echo(colored("\t-stop","magenta") + colored("  \t\t-\tTo stop the honeytoken monitoring process."))
    t.echo(colored("\texit","magenta") + colored("  \t\t-\tTo exit the tool.\n\n"))


@app.command()
def line():
    intractive_mode()




if __name__ == "__main__":
    app()