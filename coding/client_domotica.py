from telnetlib import Telnet
import string


def telnet_client(cmd):
    print(cmd)

    host = '192.168.5.6'
    port = 3001

    with Telnet(host, port) as tn:
        tn.write((f'LOAD {cmd}').encode() + '\n'.encode())


def telnet_client_status(cmd):
    print(cmd)

    host = '192.168.5.6'
    port = 3001

    with Telnet(host, port) as tn:
        tn.write((f'GETLOAD {cmd}').encode() + '\n'.encode())
        r = tn.read_some().decode()
        r = r[r.rfind(' ')+1:r.rfind('\n')]
        print(r)
        return r


def switch_lights(room):
    if (room == 1):
        lights = ['15990', '15991', '15992', '15993']

        command = '100'

        if (float(telnet_client_status(lights[0])) != 0):
            command = '0'

        for light in lights:
            telnet_client(f'{light} {command}')
    elif (room == 2):
        lights = ['15986', '15987']

        command = '100'

        if (float(telnet_client_status(lights[0])) != 0):
            command = '0'

        for light in lights:
            telnet_client(f'{light} {command}')


if __name__ == '__main__':
    #cmd = 'GETLOAD 15990'
    # telnet_client_status(cmd)

    #cmd = 'LOAD 15990 0'
    # telnet_client(cmd)

    switch_lights(1)


# AULA ELETTRONICA
# luce accensione  1 : LOAD 15990 100
# luce spegnimento 1 : LOAD 15990 0
# luce accensione 2  : LOAD 15991 100
# luce spegnimento 2 : LOAD 15991 0
# apertura tapparelle: BTN 16072
# chiusura tapparelle: BTN 16076
# luce LIM           : LOAD 19604 100
# luce LIM           : LOAD 19604 0
# lettura temperatura ambiente                             : GETTHERMTEMP 16237 INDOOR
# accensione temporizzata del riscaldamento/condizionamento: BTNPRESS 16074

# AULA INFORMATICA
# luce accensione  1 : LOAD 15992 100
# luce spegnimento 1 : LOAD 15992 0
# luce accensione 2  : LOAD 15993 100
# luce spegnimento 2 : LOAD 15993 0
# apertura tapparelle: BTN 16082
# chiusura tapparelle: BTN 16086
# luce LIM           : LOAD 19605 100
# luce LIM           : LOAD 19605 0

# AULA 108
# luce accensione  1 : LOAD 15986 100
# luce spegnimento 1 : LOAD 15986 0
# luce accensione 2  : LOAD 15987 100
# luce spegnimento 2 : LOAD 15987 0
# apertura tapparelle: BTN 16052
# chiusura tapparelle: BTN 16056
# luce LIM           : LOAD 19602 100
# luce LIM           : LOAD 19602 0
