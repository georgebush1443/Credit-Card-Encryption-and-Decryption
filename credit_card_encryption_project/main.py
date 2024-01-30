# main.py
from authentication import authenticate_user, check_access
from encryption import encrypt_credit_card
from cloud_storage import store_in_cloud
from decryption import decrypt_credit_card
from logging_monitoring import log_activity, monitor_activity
from compliance import check_compliance

def main():
    # Example usage of modules
    username = input("Enter username: ")
    password = input("Enter password: ")

    if authenticate_user(username, password):
        print("Authentication successful.")
        user_role = "admin"  # Replace with actual user role retrieval logic

        if check_access(user_role, "admin"):
            credit_card_number = input("Enter credit card number: ")

            # Encryption
            encryption_key = b'mysecretkey12345'  # Replace with a secure key management system
            encrypted_data = encrypt_credit_card(credit_card_number, encryption_key)

            # Cloud Storage
            store_in_cloud(encrypted_data)

            # Decryption
            decrypted_data = decrypt_credit_card(encrypted_data, encryption_key)
            print("Decrypted Credit Card Number:", decrypted_data)

            # Logging and Monitoring
            log_activity(username, "Performed encryption and decryption")
            monitor_activity()

            # Compliance Checks
            check_compliance()
        else:
            print("Access denied.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
