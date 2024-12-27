from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('hello')

@socketio.on('message')
def handle_message(message):
    print("Received message:", message)
    socketio.emit("message", "Message received: " + message)

if __name__ == '__main__':
    socketio.run(app)
