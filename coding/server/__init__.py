import db
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
        return jsonify(db.save_report(request.json))
    elif (request.method == 'GET' and id != None):
        return jsonify(db.get_report(id))


@app.route('/api/reports', methods=['GET'])
def reports():
    return jsonify(db.get_reports())


if __name__ == '__main__':
    db = db.DB()
    startTime = time.time()
    app.run(host="192.168.0.106", debug=True)
