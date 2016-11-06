from bottle import route, run, template
import time, math

TIMEOUT=5

@route('/')
def index():
    time.sleep(int(TIMEOUT))
    return template('<b>Hello world after {{timeout}}</b>!', timeout=TIMEOUT)

@route('/hello')
def hello():
    time.sleep(int(TIMEOUT))
    return template('<b>Hello world after {{timeout}}</b>!', timeout=TIMEOUT)

@route('/timeout/<to>')
def setTimeout(to):
    global TIMEOUT
    TIMEOUT=int(to)
    return template('<b>Timeout set to: {{timeout}}</b>!', timeout=to)

run(host='0.0.0.0', port=8080)

