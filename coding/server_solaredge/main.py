from helpers.config_helper import Config
from helpers.logging_helper import logger

from helpers.speech_recognition_helper import SpeechRecognition

from datetime import datetime

import utilities
import time

from flask import Flask, request, jsonify

from enum import Enum

app = Flask(__name__)

# Api calls


@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({'code': 200, 'status': 'online', 'elapsed time': utilities.getElapsedTime(startTime)}), 200


@app.route('/api/input/<input>', methods=['GET'])
def recording_input(input):
    if input != '' and input != None and input in [i.value for i in Input]:
        try:
            uploaded_file = request.files['file']
            if (uploaded_file.filename != ''):
                path = f'recordings/{datetime.now().isoformat()}.wav'
                uploaded_file.save(path)
                speech_recognition = SpeechRecognition(path)

                if (input in utilities.inputs):
                    speech_recognition.result
                else:
                    return jsonify({'code': 500, 'message': 'Invalid input selected'}), 500
            else:
                logger.error('No file passed')
                return jsonify({'code': 500, 'message': 'No file was passed'}), 500
        except Exception as e:
            logger.error(str(e))
            return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No input was specified')
        return jsonify({'code': 500, 'message': 'No input was specified'}), 500


if __name__ == '__main__':
    config_helper = Config()
    startTime = time.time()

    speech_recognition = SpeechRecognition('recordings/recording.wav')
    logger.info(speech_recognition.result)

    # app.run(host=config_helper.srv_host, port=config_helper.srv_port,
    #        debug=config_helper.srv_debug)
