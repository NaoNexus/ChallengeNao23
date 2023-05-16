from helpers.config_helper import Config
from helpers.db_helper import DB
from helpers.logging_helper import logger
from helpers.pdf_analyzer import PDFAnalyzer
from helpers.weather_api_helper import WeatherApi
from helpers.domotics_server_helper import Room, DomoticsServer

import utilities
import time

from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

# Web App calls


@app.route('/', methods=['GET'])
def index():
    if (request.args.get('room', '') == ''):
        room = Room.it
    else:
        room = Room[request.args['room']]

    light_status = 'ON'
    lim_status = 'OFF'

    # light_status = domotics_server_helper.get_lights_status(room)
    # lim_status = domotics_server_helper.get_lim_status(room)

    reports = db_helper.get_reports()

    return render_template('index.html', reports=reports, room=room.name, light_status=light_status, lim_status=lim_status)


@app.route('/reports', methods=['GET'])
def reports_screen():
    reports = db_helper.get_reports()

    return render_template('reports.html', reports=reports)


@app.route('/new_report', methods=['GET'])
def new_report_screen():
    report = {'id': '', 'date': '', 'co2': 0, 'temperature': 0,
              'humidity': 0, 'nPeople': 0, 'internalLight': 0, 'externalLight': 0}
    return render_template('report.html', report=report)


@app.route('/report/<id>', methods=['GET'])
def report_screen(id):
    if (id != None and id != ''):
        try:
            report = db_helper.get_report(id)
            return render_template('report.html', report=report)
        except Exception as e:
            logger.error(str(e))
            return redirect("/reports", code=500)

    return redirect("/reports", code=404)

# Api calls
# Reports calls


@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({'code': 200, 'status': 'online', 'elapsed time': utilities.getElapsedTime(startTime)}), 200


@app.route('/api/report', methods=['POST'])
def save_report():
    try:
        if request.content_type == 'application/json':
            json = request.json
            if int(json.get('externalLight', 0)) == 0:
                json['externalLight'] = weather_api_helper.get_currrent_light(
                    json['date'])
            return jsonify({'code': 201, 'message': 'OK', 'data': db_helper.save_report(json)}), 201
        else:
            json = request.form.to_dict()
            if int(json.get('externalLight', 0)) == 0:
                json['externalLight'] = weather_api_helper.get_currrent_light(
                    json['date'])
            db_helper.save_report(json)
            return redirect("/reports", code=302)
    except Exception as e:
        logger.error(str(e))
        if request.content_type == 'application/json':
            return jsonify({'code': 500, 'message': str(e)}), 500
        return redirect("/reports", code=500)


@app.route('/api/pdf_report', methods=['POST'])
def save_pdf_report():
    try:
        uploaded_file = request.files['file']
        if (uploaded_file.filename != ''):
            uploaded_file.save(f'report_pdfs/{uploaded_file.filename}')

            analyzed_pdf = PDFAnalyzer(weather_api_helper,
                                       f'report_pdfs/{uploaded_file.filename}', request.form['nPeople'], request.form['internalLight'])

            return jsonify({'code': 201, 'message': 'OK', 'data': db_helper.save_report(analyzed_pdf.report)}), 201
        else:
            logger.error('No file passed')
            return jsonify({'code': 500, 'message': 'No file was passed'}), 500
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500


@app.route('/api/report/<id>', methods=['GET', 'POST', 'DELETE'])
def report(id):
    if (id != None and id != ''):
        if request.method == 'GET':
            try:
                return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.get_report(id)}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
        elif request.method == 'POST':
            try:
                if request.content_type == 'application/json':
                    json = request.json
                else:
                    json = request.form.to_dict()
                json['id'] = id
                if int(json.get('externalLight', 0)) == 0:
                    json['externalLight'] = str(weather_api_helper.get_currrent_light(
                        json['date']))
                if request.content_type == 'application/json':
                    return jsonify({'code': 201, 'message': 'OK', 'data': db_helper.save_report(json)}), 201
                else:
                    db_helper.save_report(json)
                    return redirect("/reports", code=302)
            except Exception as e:
                logger.error(str(e))
                if request.content_type == 'application/json':
                    return jsonify({'code': 500, 'message': str(e)}), 500
                return redirect("/reports", code=500)
        elif request.method == 'DELETE':
            try:
                return jsonify({'code': 201, 'message': 'OK', 'data': db_helper.delete_report(id)}), 201
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('No id argument passed')
        return jsonify({'code': 500, 'message': 'No id was passed'}), 500


@app.route('/api/reports', methods=['GET'])
def reports():
    try:
        return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.get_reports()}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({'code': 500, 'message': str(e)}), 500

# Domotics calls


@app.route('/api/domotics/lights/<room>', methods=['POST', 'GET'])
def domotics_lights(room):
    if (room in [room.name for room in Room]):
        if (request.method == 'GET'):
            try:
                status = domotics_server_helper.get_lights_status(Room[room])
                return jsonify({'code': 200, 'message': 'OK', 'status': status}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
        else:
            try:
                domotics_server_helper.switch_lights(Room[room])
                return jsonify({'code': 200, 'message': 'OK'}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('Room value not valid')
        return jsonify({'code': 500, 'message': 'Room value not valid'}), 500


@app.route('/api/domotics/lim/<room>', methods=['GET', 'POST'])
def domotics_lim(room):
    if (room in [room.name for room in Room]):
        if (request.method == 'GET'):
            try:
                status = domotics_server_helper.get_lim_status(Room[room])
                return jsonify({'code': 200, 'message': 'OK', 'status': status}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
        else:
            try:
                domotics_server_helper.switch_lim(Room[room])
                return jsonify({'code': 200, 'message': 'OK'}), 200
            except Exception as e:
                logger.error(str(e))
                return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('Room value not valid')
        return jsonify({'code': 500, 'message': 'Room value not valid'}), 500


@app.route('/api/domotics/blinds/<room>', methods=['POST'])
def domotics_blinds(room):
    if (room in [room.name for room in Room]):
        try:
            if (request.args['action'] == 'open'):
                domotics_server_helper.open_blinds(Room[room])
            elif (request.args['action'] == 'close'):
                domotics_server_helper.close_blinds(Room[room])
            return jsonify({'code': 200, 'message': 'OK'}), 200
        except Exception as e:
            logger.error(str(e))
            return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('Room value not valid')
        return jsonify({'code': 500, 'message': 'Room value not valid'}), 500


@app.route('/api/domotics/thermo/<room>', methods=['POST'])
def domotics_thermostat(room):
    if (room in [room.name for room in Room]):
        try:
            domotics_server_helper.switch_temp(Room[room])
            return jsonify({'code': 200, 'message': 'OK'}), 200
        except Exception as e:
            logger.error(str(e))
            return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        logger.error('Room value not valid')
        return jsonify({'code': 500, 'message': 'Room value not valid'}), 500


if __name__ == '__main__':
    config_helper = Config()
    db_helper = DB(config_helper)
    weather_api_helper = WeatherApi(config_helper)
    domotics_server_helper = DomoticsServer(config_helper)

    startTime = time.time()

    pdf = PDFAnalyzer(weather_api_helper, './report_pdfs/20230324-175444.pdf', 5, 2000)

    # app.run(host=config_helper.srv_host, port=config_helper.srv_port,
    #        debug=config_helper.srv_debug)
