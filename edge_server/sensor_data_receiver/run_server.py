from server import app, socketio, views

if __name__ == '__main__':
    # socketio.run(app, host='192.168.1.186')
    socketio.run(app, host='0.0.0.0')
