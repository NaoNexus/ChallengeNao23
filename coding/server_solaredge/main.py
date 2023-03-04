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
                uploaded_file.save(
                    f'recordings/{datetime.now().isoformat()}.wav')

                match Input[input]:
                    case Input.ZIP:
                        pass
                    
                return jsonify({'code': 201, 'message': 'OK', 'data': 'OK'}), 201
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


class Input(Enum):
    NEW_PROJECT = 'new_project'

    INFO_SECTION = 'info_section'
    MODELLING_SECTION = 'modelling_section'
    POSITIONING_SECTION = 'positioning_section'
    STORAGE_SECTION = 'storage_section'
    ELECTRICAL_SECTION = 'electrical_section'
    FINANCIAL_SECTION = 'financial_section'
    SUMMARY_SECTION = 'summary_section'

    PROJECT_TYPE = 'project_type'
    PROJECT_NAME = 'project_name'
    COUNTRY = 'country'
    STREET = 'street'
    CITY = 'city'
    ZIP = 'zip'
    CONSUMPTION = 'consumption'
    CONSUMPTION_PERIOD = 'consumption_period'
    ELECTRICAL_GRID = 'electrical_grid'
    POWER_FACTOR = 'power_factor'
    NAME = 'name'
    SURNAME = 'surname'
    COMPANY = 'company'
    NOTES = 'notes'
