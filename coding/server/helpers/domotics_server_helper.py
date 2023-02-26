import helpers.config_helper as config_helper
from logging_helper import logger

import socket

class DomoticsServer:
    ip: str
    port: int

    def __init__(self, config: config_helper.Config):
        self.ip = config.domotics_ip
        self.port = config.domotics_port

    def send_command(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port))
            s.sendall(bytes(command, 'utf-8'))
            data = s.recv(1024)
            logger.info(data)
            return data
