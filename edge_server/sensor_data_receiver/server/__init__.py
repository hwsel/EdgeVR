import logging
import struct

import mmap
from flask import Flask
from flask_socketio import SocketIO

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config.from_object('server.setting')

# with open('t.txt', 'rb+') as tf:
#     with mmap.mmap(tf.fileno(), 3 * 10 * 4 + 4, access=mmap.ACCESS_WRITE) as tmm:
#         d = [0 for i in range(3 * 10 + 1)]
#         tmm[:] = struct.pack('31f', *d)
#         tmm.flush()

history = [[0, 0, 0, 0] for _ in range(30)]

# with app.app_context():
#     f = open('/home/zichenzhu/PycharmProjects/try_mmap/1234.txt', 'rb+')
#     g.mm = mmap.mmap(f.fileno(), 12, access=mmap.ACCESS_WRITE)

socketio = SocketIO(app, cors_allowed_origins="*")
# socketio = SocketIO(app, engineio_logger=True, cors_allowed_origins="*")

