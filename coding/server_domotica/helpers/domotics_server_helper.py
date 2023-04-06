import helpers.config_helper as config_helper
from helpers.logging_helper import logger

from telnetlib import Telnet
from enum import Enum


class Room(Enum):
    it = 1
    robotics = 2
    quinta_ssa = 3


class DomoticsServer:
    ip: str
    port: int

    def __init__(self, config: config_helper.Config):
        self.ip = config.domotics_ip
        self.port = config.domotics_port

    def get_status(self, command):
        with Telnet(self.ip, self.port) as tn:
            tn.write((f'GETLOAD {command}\n').encode())
            response = tn.read_some().decode()
            response = response[response.rfind(' ')+1:response.rfind('\n')]
            logger.info(f'Telnet response: {response}')
            return response

    def send_light_command(self, command):
        with Telnet(self.ip, self.port) as tn:
            tn.write((f'LOAD {command}\n').encode())
            response = tn.read_some().decode()
            logger.info(f'Telnet response: {response}')
            return response

    def send_blind_command(self, command):
        with Telnet(self.ip, self.port) as tn:
            tn.write((f'BTN {command}\n').encode())
            response = tn.read_some().decode()
            logger.info(f'Telnet response: {response}')
            return response

    def switch_lights(self, room: Room):
        if (room == Room.robotics):
            lights = ['15990', '15991']
        elif (room == Room.it):
            lights = ['15992', '15993']
        elif (room == Room.quinta_ssa):
            lights = ['15986', '15987']

        command = '100'

        if (float(self.get_status(lights[0])) != 0):
            command = '0'

        for light in lights:
            self.send_light_command(f'{light} {command}')

    def get_lights_status(self, room: Room):
        if (room == Room.robotics):
            lights = ['15990', '15991']
        elif (room == Room.it):
            lights = ['15992', '15993']
        elif (room == Room.quinta_ssa):
            lights = ['15986', '15987']

        return 'ON' if float(self.get_status(lights[0])) != 0 else 'OFF'

    def switch_lim(self, room: Room):
        if (room == Room.robotics):
            lim = '19604'
        elif (room == Room.it):
            lim = '19605'
        elif (room == Room.quinta_ssa):
            lim = '19602'

        command = '100'

        if (float(self.get_status(lim)) != 0):
            command = '0'

        self.send_light_command(f'{lim} {command}')

    def get_lights_status(self, room: Room):
        if (room == Room.robotics):
            lim = '19604'
        elif (room == Room.it):
            lim = '19605'
        elif (room == Room.quinta_ssa):
            lim = '19602'

        return 'ON' if float(self.get_status(lim)) != 0 else 'OFF'

    def open_blinds(self, room: Room):
        if (room == Room.robotics):
            blind = '16072'
        elif (room == Room.it):
            blind = '16082'
        elif (room == Room.quinta_ssa):
            blind = '16052'

        self.send_blind_command(blind)

    def close_blinds(self, room: Room):
        if (room == Room.robotics):
            blind = '16076'
        elif (room == Room.it):
            blind = '16086'
        elif (room == Room.quinta_ssa):
            blind = '16056'

        self.send_blind_command(blind)
