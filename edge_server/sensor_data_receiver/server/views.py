import struct
import sys

import mmap
from pprint import pprint

import numpy as np
from flask import request

from server import app, socketio, history


@app.route('/')
def root():
    return 'hello, world!'


@app.route('/sensor', methods=['POST', 'GET'])
def sensor():
    if request.method == 'POST':
        history[1:] = history[0:29]

        ori = eval(request.form['orientationAngles'])
        history[0] = ori + [eval(request.form['time']), ]


        with open('../../shared_memory/predicted.txt', 'rb+') as f:
            with mmap.mmap(f.fileno(), 48, access=mmap.ACCESS_WRITE) as mm:
                mm[:] = struct.pack('fffqfffq',
                                    -np.rad2deg(history[0][1]),
                                    np.rad2deg(history[0][0]),
                                    np.rad2deg(history[0][2]),
                                    history[0][3],
                                    -np.rad2deg(history[29][1]),
                                    np.rad2deg(history[29][0]),
                                    np.rad2deg(history[29][2]),
                                    history[29][3]
                                    )
                # mm[12:] = struct.pack('>q', eval(request.form['time']))
                mm.flush()
        pprint(history[0])

        return ''
    elif request.method == 'GET':
        return '0 45 0'
    else:
        return ''


@socketio.on('img')
def handle_img(img):
    pass


@socketio.on('message')
def handle_message(message):
    print(message + ' ' + request.sid, file=sys.stderr)
    socketio.send('test')


@socketio.on('json')
def handle_json(json):
    pass
