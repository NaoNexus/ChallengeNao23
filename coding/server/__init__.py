import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return ''

@app.route('/api/report', methods=['GET', 'POST'])
def report():
    return jsonify({})
if __name__ == '__main__':
    app.run(debug=True)