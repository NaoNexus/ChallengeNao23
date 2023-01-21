import config_helper
import db_helper
import time
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return ''


@app.route('/info', methods=['GET'])
def info():
    return jsonify({'Status': 'online', 'Elapsed time': time.time() - startTime})


@app.route('/api/report/<int:id>', methods=['GET', 'POST'])
def report(id):
    if (request.method == 'POST'):
        return jsonify(db_helper.save_report(request.json))
    elif (request.method == 'GET' and id != None):
        return jsonify(db_helper.get_report(id))


@app.route('/api/reports', methods=['GET'])
def reports():
    return jsonify(db_helper.get_reports())


if __name__ == '__main__':
    config_helper = config_helper.Config()
    db_helper = db_helper.DB(config_helper)
    startTime = time.time()
    app.run(host=config_helper.srv_host, port=config_helper.srv_port,
            debug=config_helper.srv_debug)
