from helpers.config_helper import Config
from helpers.logging_helper import logger

from helpers.speech_recognition_helper import SpeechRecognition

from datetime import datetime
import utilities
import time

from flask import Flask, request, jsonify

app = Flask(__name__)

# Api calls


@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({'code': 200, 'status': 'online', 'elapsed time': utilities.getElapsedTime(startTime)}), 200


@app.route('/api/input', methods=['GET'])
def recording_input():
    try:
        uploaded_file = request.files['file']
        if (uploaded_file.filename != ''):
            uploaded_file.save(f'recordings/{datetime.now().isoformat()}.wav')

            return jsonify({'code': 201, 'message': 'OK', 'data': 'OK'}), 201
        else:
            logger.error('No file passed')
            return jsonify({'code': 500, 'message': 'No file was passed'}), 500
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500


if __name__ == '__main__':
    config_helper = Config()
    startTime = time.time()

    speech_recognition = SpeechRecognition('recordings/recording.wav')
    logger.info(speech_recognition.result)

    # app.run(host=config_helper.srv_host, port=config_helper.srv_port,
    #        debug=config_helper.srv_debug)
