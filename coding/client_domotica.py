from telnetlib import Telnet

def telnet_client(cmd):
   print(cmd)
   
   host = '192.168.5.6'
   port = 3001

   with Telnet(host, port) as tn:
      tn.write(cmd.encode() + '\n'.encode())


if __name__ == '__main__':
   cmd = 'BTN 16072'   
   telnet_client(cmd)
    
#AULA ELETTRONICA
#luce accensione  1 : LOAD 15990 100
#luce spegnimento 1 : LOAD 15990 0
#luce accensione 2  : LOAD 15991 100
#luce spegnimento 2 : LOAD 15991 0
#apertura tapparelle: BTN 16072
#chiusura tapparelle: BTN 16076
#luce LIM           : LOAD 19604 100
#luce LIM           : LOAD 19604 0

#AULA INFORMATICA
#luce accensione  1 : LOAD 15992 100
#luce spegnimento 1 : LOAD 15992 0
#luce accensione 2  : LOAD 15993 100
#luce spegnimento 2 : LOAD 15993 0
#apertura tapparelle: BTN 16082
#chiusura tapparelle: BTN 16086
#luce LIM           : LOAD 19605 100
#luce LIM           : LOAD 19605 0

#AULA 108
#luce accensione  1 : LOAD 15986 100
#luce spegnimento 1 : LOAD 15986 0
#luce accensione 2  : LOAD 15987 100
#luce spegnimento 2 : LOAD 15987 0
#apertura tapparelle: BTN 16052
#chiusura tapparelle: BTN 16056
#luce LIM           : LOAD 19602 100
#luce LIM           : LOAD 19602 0