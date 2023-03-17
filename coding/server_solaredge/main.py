from threading import Thread
from helpers.config_helper import Config
from helpers.logging_helper import logger
from helpers.solaredge_helper import SolarEdge
from helpers.speech_recognition_helper import SpeechRecognition

from datetime import datetime

import utilities
import time

from flask import Flask, request, jsonify

from enum import Enum

app = Flask(__name__)
solar_edge = None

# Api calls


@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({'code': 200, 'status': 'online', 'elapsed time': utilities.getElapsedTime(startTime)}), 200


@app.route('/api/input/<string:Input>', methods=['POST'])
def recording_input(Input):
    if Input != '' and Input != None and Input in utilities.inputs:
        try:
            uploaded_file = None
            if (Input not in utilities.inputs_without_file):
                uploaded_file = request.files['file']

            if (Input in utilities.inputs_without_file or (uploaded_file and uploaded_file.filename != '')):
                if ((uploaded_file and uploaded_file.filename != '')):
                    path = f'recordings/recording.wav'
                    uploaded_file.save(path)
                    speech_recognition = SpeechRecognition(path)

                    solar_edge.input(Input, speech_recognition.result)

                    return jsonify({'code': 200, 'message': 'OK', 'result': speech_recognition.result}), 200

                solar_edge.input(Input, '')

                return jsonify({'code': 200, 'message': 'OK'}), 200
            else:
                logger.error('No file passed')
                return jsonify({'code': 500, 'message': 'No file was passed'}), 500
        except Exception as e:
            logger.error(str(e))
            return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No input was specified')
        return jsonify({'code': 500, 'message': 'Input is invalid'}), 500


@app.route('/api/recognise', methods=['POST'])
def recording():
    try:
        uploaded_file = request.files['file']

        if (uploaded_file and uploaded_file.filename != ''):
            path = f'recordings/recording.wav'
            uploaded_file.save(path)
            speech_recognition = SpeechRecognition(path)

            return jsonify({'code': 200, 'message': 'OK', 'result': speech_recognition.result}), 200
        else:
            logger.error('No file passed')
            return jsonify({'code': 500, 'message': 'No file was passed'}), 500
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500


def init_solar_edge():
    solar_edge = SolarEdge(config_helper)
    return solar_edge


def init_server():
    app.run(host=config_helper.srv_host, port=config_helper.srv_port,
            debug=config_helper.srv_debug)


if __name__ == '__main__':
    config_helper = Config()
    startTime = time.time()

    solar_edge = init_solar_edge()
    init_server()
