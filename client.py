import socketio
from crypto_utils import encrypt_message, decrypt_message

sio = socketio.Client()

print("=== CHAT CHIFFRE - CLIENT CONSOLE ===")
url = input("URL du serveur (ex: https://chat-chiffre.onrender.com) : ")
pseudo = input("Entre ton pseudo : ")

@sio.event
def connect():
    print(f"[Connecté en tant que {pseudo}]")
    sio.emit('join', {'pseudo': pseudo})

@sio.on('message')
def on_message(data):
    try:
        msg_clair = decrypt_message(data['msg'])
    except:
        msg_clair = data['msg']
    print(f"{data['pseudo']} : {msg_clair}")

@sio.event
def disconnect():
    print("[Déconnecté]")

sio.connect(url)
print("Tape /quit pour quitter")

while True:
    texte = input()
    if texte == "/quit":
        print("Au revoir !")
        sio.disconnect()
        break
    msg_chiffre = encrypt_message(texte)
    sio.emit('send_message', {'msg': msg_chiffre})
