from rich.console import Console
import inspect
from rich.progress import track
import time

class EditorTxt:
    def __init__(self):
        self.console = Console()

    def negrito_black(self, param):
        self.console.print(f"[bold black]{param}")
        pass

    def negrito_bright_black(self, param):
        self.console.print(f"[bold bright_black]{param}")
        pass

    def negrito_red(self, param):
        self.console.print(f"[bold red]{param}")
        pass

    def negrito_bright_red(self, param):
        self.console.print(f"[bold bright_red]{param}")
        pass

    def negrito_green(self, param):
        self.console.print(f"[bold green]{param}")
        pass

    def negrito_bright_green(self, param):
        self.console.print(f"[bold bright_green]{param}")
        pass

    def negrito_yellow(self, param):
        self.console.print(f"[bold yellow]{param}")
        pass

    def negrito_bright_yellow(self, param):
        self.console.print(f"[bold bright_yellow]{param}")
        pass

    def negrito_blue(self, param):
        self.console.print(f"[bold blue]{param}")
        pass

    def negrito_bright_blue(self, param):
        self.console.print(f"[bold bright_blue]{param}")
        pass

    def negrito_magenta(self, param):
        self.console.print(f"[bold magenta]{param}")
        pass

    def negrito_bright_magenta(self, param):
        self.console.print(f"[bold bright_magenta]{param}")
        pass

    def negrito_cyan(self, param):
        self.console.print(f"[bold cyan]{param}")
        pass

    def negrito_bright_cyan(self, param):
        self.console.print(f"[bold bright_cyan]{param}")
        pass

    def negrito_white(self, param):
        self.console.print(f"[bold white]{param}")
        pass

    def negrito_bright_white(self, param):
        self.console.print(f"[bold bright_white]{param}")
        pass

    def charging_bar(self, ):
        for step in track(range(100), description="Processing..."):
            time.sleep(0.1)

class EditorBanner:
    def __init__(self):
        self.banner = str("""""")

    def banner_adm(self):
        admbanner ="""
                                    #*****+-+*+-+*+-+*+-+*****#
                                    #                         #
                                    #         |ADM|           #
                                    #                         #        
                                    #*****+-+*+-+*+-+*+-+*****#"""
        EditorTxt().negrito_bright_cyan(admbanner)
        pass

    def banner_user(self):
        userbanner = (" " * 44 + "===USER===")
        EditorTxt().negrito_bright_green(userbanner)
        pass








'''
l = ["maçã", "banana", "laranja", "uva", "abacaxi", "manga", "morango"]
out = EditorTxt()

# Obter e chamar todos os métodos que não começam com "__"
def run_all_metods():

    for nome, metodo in inspect.getmembers(out, predicate=inspect.ismethod):
        if not nome.startswith("__"):
            print(f"Executando: {nome}")
            metodo(l)
    pass

'''