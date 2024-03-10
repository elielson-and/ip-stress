<p align="center"><a href="https://github.com/elielson-andre/ip-stress" target="_blank"><img src="https://elielson.net/assets/img/ipstress/ipstress_logo.png" width="400" alt="IP STRESS"></a></p>

<p align="center"> Versão: 1.0 - @elielson_and</p>

## Sobre
Uma pequena e poderosa ferramenta para testar e estressar TCP/IP de um servidor, muito útil para realizar testes.Note que a aplicação é apenas um node DoS que você pode usar em uma ou mais máquinas como um "cluster" para rodar os processos e testar seu ambiente em um cenário de ataque DDoS.

- [Contexto](https://tecnoblog.net/responde/o-que-e-um-ataque-ddos/).

## Diagrama
<p align="center"><a href="#" target="_blank"><img src="https://docs.aws.amazon.com/images/whitepapers/latest/aws-best-practices-ddos-resiliency/images/ddos-attack.png" width="600" alt="IP STRESS"></a></p>


## ⚡ Instalação/Execução no Linux com Docker

Clonar o projeto
```
git clone https://github.com/elielson-andre/ip-stress
```
Entre na pasta
```
cd ip-stress
```
Suba o contaner
```
docker-compose up -d
```
---------  
Pegar o nome com "docker ps" e acessar o bash da maquina
```
docker exec -it [nome_do_container] bash
```
Ao acessar o bash, rodar a ferramenta  
```
python setup.py
```  

