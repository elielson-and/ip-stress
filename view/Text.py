from colorama import Fore, Style
import time
class Text:

    def input(message):
        return Fore.CYAN + message + " => " + Style.RESET_ALL
    
    
     # Text colors ---------------------
    def txt_blue(text):
        return Fore.BLUE + str(text) + Style.RESET_ALL
    
    def txt_red(text):
        return Fore.RED + str(text) + Style.RESET_ALL
    
    def txt_yellow(text):
        return Fore.YELLOW + str(text) + Style.RESET_ALL
    
    def txt_green(text):
        return Fore.GREEN + str(text) + Style.RESET_ALL
    
    def txt_cyan(text):
        return Fore.CYAN + str(text) + Style.RESET_ALL