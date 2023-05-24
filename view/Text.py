from colorama import Fore, Style
import time
class Text:

    # Text colors ---------------------

    def red(text):
        return Fore.RED + str(text) + Style.RESET_ALL
    
    def yellow(text):
        return Fore.YELLOW + str(text) + Style.RESET_ALL
    
    def green(text):
        return Fore.GREEN + str(text) + Style.RESET_ALL
    
    def cyan(text):
        return Fore.CYAN + str(text) + Style.RESET_ALL