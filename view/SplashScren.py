from colorama import init, Fore, Style
import time
import os

class SplashScren:
    def __init__(self) -> None:
        pass

    def show():
        os.system('clear')
        print('\n')
        time.sleep(1)
        print("2023 IPSTRESS | By: @elielson_and | contato@elielson.net")
        print("Carregando", end="")
        for i in range(30):
            print(".", end="", flush=True)
            time.sleep(0.08)
        os.system('clear')
        
        letras = {
            'I': ['▉▉▉▉▉', '  ▉  ', '  ▉  ', '  ▉  ', '▉▉▉▉▉'],
            'P': ['▉▉▉▉ ', '▉   ▉', '▉▉▉▉ ', '▉    ', '▉    '],
            'S': [' ▉▉▉▉', '▉    ', ' ▉▉▉▉', '    ▉', '▉▉▉▉ '],
            'T': ['▉▉▉▉▉', '  ▉  ', '  ▉  ', '  ▉  ', '  ▉  '],
            'R': ['▉▉▉▉ ', '▉   ▉', '▉▉▉▉ ', '▉  ▉ ', '▉   ▉'],
            'E': ['▉▉▉▉▉', '▉    ', '▉▉▉▉▉', '▉    ', '▉▉▉▉▉'],
        }

        init()  # Inicializar colorama
        
        for linha in range(5):
            for letra in 'IPSTRESS':
                print(Fore.GREEN + letras[letra][linha] + '  ', end='')
            print(Style.RESET_ALL) 

        print(Fore.RESET + Style.RESET_ALL)
        time.sleep(1.5)
        os.system('clear')