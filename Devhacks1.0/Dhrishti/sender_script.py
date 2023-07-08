from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class Enc:
    def encrypt_message(message, public_key):
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_message = cipher.encrypt(message.encode())
        encoded_message = base64.b64encode(encrypted_message)
        return encoded_message.decode()

    def de(self, mes):
    # Load recipient's public key from a file
        with open('message/receiver_public_key.pem', 'r') as file:
            recipient_public_key = file.read()

        # Message to be encrypted and sent
        message_to_send = mes

        # Encrypt the message using RSA
        encrypted_message = self.encrypt_message(message_to_send, recipient_public_key)
        print("Encrypted Message:", encrypted_message)

        with open("message/cont.txt", 'w') as f:
            f.write(encrypted_message)
        
        return

