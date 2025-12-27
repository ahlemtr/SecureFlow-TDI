import re
from cryptography.fernet import Fernet

# 1. THE PRIVACY FILTER (Analysis)
# This function finds emails and hides them so we stay compliant with privacy rules.
def scrub_sensitive_data(text):
    # This pattern looks for any standard email format
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.sub(email_pattern, "[REDACTED]", text)

# 2. THE SECURITY VAULT (Security/Development)
# This part handles the encryption logic I'm learning in my SCC semester.
def run_pipeline():
    # Generate a key (In a real bank, this is kept in a hardware vault)
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    # Example of raw bank data that needs protection
    raw_data = "Urgent: Please contact client.support@example.com regarding ID 9942."
    print(f"Original Data: {raw_data}")
    
    # Step A: Remove PII (Emails)
    clean_data = scrub_sensitive_data(raw_data)
    print(f"Redacted Data: {clean_data}")
    
    # Step B: Encrypt the cleaned data
    encrypted_data = cipher.encrypt(clean_data.encode())
    
    # Save the 'locked' version to a file
    with open("secure_output.dat", "wb") as f:
        f.write(encrypted_data)
    
    # Save the key so we can unlock it later (For testing purposes)
    with open("file_key.key", "wb") as k:
        k.write(key)

    print("\nProcess Complete: Data is now redacted and encrypted in 'secure_output.dat'.")

if __name__ == "__main__":
    run_pipeline()
