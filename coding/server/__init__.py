from config_helper import Config
from db_helper import DB
from pdf_analyzer import PDFAnalyzer
import utilities

import time

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/reports')
def reports_screen():
    reports = db_helper.get_reports()

    return render_template('reports.html', reports=reports)


@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({'code': 200, 'status': 'online', 'elapsed time': utilities.getElapsedTime(startTime)}), 200


@app.route('/api/report', methods=['POST'])
def save_report():
    try:
        return jsonify({'code': 201, 'message': 'OK', 'data': db_helper.save_report(request.json)}), 201
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500


@app.route('/api/pdf_report', methods=['POST'])
def save_pdf_report():
    try:
        uploaded_file = request.files['file']
        if (uploaded_file.filename != ''):
            uploaded_file.save(f'report_pdfs/{uploaded_file.filename}')

            analyzed_pdf = PDFAnalyzer(f'report_pdfs/{uploaded_file.filename}')

            return jsonify({'code': 201, 'message': 'OK', 'data': db_helper.save_report(analyzed_pdf.report)}), 201
        else:
            return jsonify({'code': 500, 'message': 'No file was passed'}), 500
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500


@app.route('/api/report/<id>', methods=['GET'])
def report(id):
    if (id != None and id != ''):
        try:
            return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.get_report(id)}), 200
        except Exception as e:
            return jsonify({'code': 500, 'message': str(e)}), 500
    else:
        return jsonify({'code': 500, 'message': 'No id was passed'}), 500


@app.route('/api/reports', methods=['GET'])
def reports():
    try:
        return jsonify({'code': 200, 'message': 'OK', 'data': db_helper.get_reports()}), 200
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500


if __name__ == '__main__':
    config_helper = Config()
    db_helper = DB(config_helper)
    startTime = time.time()
    app.run(host=config_helper.srv_host, port=config_helper.srv_port,
            debug=config_helper.srv_debug)
