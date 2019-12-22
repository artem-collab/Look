from os import *
from colorama import *
def kali():
    while True:
        kalil='root@kali|> '
        lose=input(Fore.RED + kalil)
        if lose == 'ifconfig':
            system('ifconfig')
        elif lose == 'ping vk.com':
            system('ping vk.com')
def vk():
    username=input(Fore.RED + 'username:')
    id=input(Fore.BLUE + 'id user: ')
    while True:
        print(Fore.RED + 'attack on' + username + id)
def insta():
    inusername=input(Fore.RED + 'username: ')
    while True:
        print(Fore.BLUE + 'attack on ' + inusername)
def teleg():
    id=input('id|> ')
    while True:
        print('attack on' + id)
def git():
    user=input('user|> ')
    while True:
        print('attack on' + user)
