from cryptography.fernet import Fernet

# Clé AES-256 partagée (Fernet = AES-CBC + HMAC SHA256)
# En vrai projet, cette clé serait échangée de façon sécurisée
KEY = b'vX9zQ2mK8pL4nR7tY1wE5uI0oP3aS6dF9gH2jK5mN8bV1cX4zA7qW0eR3tY6uI=='
fernet = Fernet(KEY)

def encrypt_message(message: str) -> str:
    """Chiffre un message en clair avec AES-256"""
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(token: str) -> str:
    """Déchiffre un message avec AES-256"""
    return fernet.decrypt(token.encode()).decode()
