from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    pseudo = data['pseudo']
    users[request.sid] = pseudo
    emit('message', {'pseudo': 'SYSTEME', 'msg': f'--- {pseudo} a rejoint le salon ---'}, broadcast=True)

@socketio.on('send_message')
def on_message(data):
    pseudo = users.get(request.sid, 'Anonyme')
    emit('message', {'pseudo': pseudo, 'msg': data['msg']}, broadcast=True, include_self=True)

@socketio.on('disconnect')
def on_disconnect():
    pseudo = users.pop(request.sid, None)
    if pseudo:
        emit('message', {'pseudo': 'SYSTEME', 'msg': f'--- {pseudo} a quitté le salon ---'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=10000)
