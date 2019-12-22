from colorama import *
from module.module import *
import os
look='''
 m       mmmm   mmmm  m   m
 #      m"  "m m"  "m #  m"
 #      #    # #    # #m#
 #      #    # #    # #  #m
 #mmmmm  #mm#   #mm#  #   "m
'''
menu='''
1)start kali-lunux 
2)hacked vk(brutforce)
3)hacked instagramm (brut)
4)hacked telegramm (brut)
5)hacked gitlab (brut)
'''
script='root@look> '
def bunner():
    print(Fore.RED + look)
    print(Fore.BLUE + menu)
    you=input(script)
    if you == '1':
        kali()
    elif you == '2':
        vk()
    elif you == '3':
        insta()
    elif you == '4':
        teleg()
    elif you == '5':
        git()
    else:
       print(Fore.RED + 'command not found')
bunner()
