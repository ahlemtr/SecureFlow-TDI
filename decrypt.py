from cryptography.fernet import Fernet

def unlock_data():
    # 1. Load the Secret Key we made earlier
    try:
        with open("file_key.key", "rb") as k:
            key = k.read()
    except FileNotFoundError:
        print("Error: Missing 'file_key.key'. I can't unlock the data without it!")
        return

    # 2. Load the Encrypted "Gibberish" Data
    try:
        with open("secure_output.dat", "rb") as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        print("Error: Missing 'secure_output.dat'. Nothing to decrypt!")
        return

    # 3. Decrypt (Unlock) the data
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data).decode()

    print("--- DECRYPTION SUCCESSFUL ---")
    print(f"Decrypted Content: {decrypted_data}")

if __name__ == "__main__":
    unlock_data()
