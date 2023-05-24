from view.SplashScren import SplashScren
from view.Text import Text
from engine.Runner import Runner
import threading
import os

SplashScren.show()

print("Insira o endereço IP alvo")
ip = str(input(Text.cyan("Digite o IP => ")))
os.system('clear')

print(f"Insira a porta Ex: 8080 \n(Se não passar nada a padrão é {Text.yellow('80')})")
port = str(input(Text.cyan("Porta => ")))
os.system('clear')

print(f"Quantidade de pacotes na injeção Ex: 120 \n(Se não passar nada por padrão vai ser {Text.yellow('100')})")
pack = str(input(Text.cyan("Quantidade Pacotes => ")))
os.system('clear')

print(f"Threads Ex: 120 \n(Se não passar nada por padrão vai ser {Text.yellow('20')})")
thread = str(input(Text.cyan("Threads => ")))
os.system('clear')

#---- Passando valores padrao se vier vazio
if port == '':
    port = 80
if pack == '':
    pack = 100
if thread == '':
    thread = 20

run = Runner()
for x in range(thread):
    thred = threading.Thread(target=run.start(ip, port, pack, thread))
    thred.start()