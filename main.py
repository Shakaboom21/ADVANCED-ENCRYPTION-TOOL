import sys
from encryption import encrypt_file, decrypt_file

def main():
    print("Advanced Encryption Tool (AES-256)")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Select an option (1/2): ").strip()
    if choice == '1':
        infile = input("Enter path to file to encrypt: ").strip()
        outfile = input("Enter output encrypted file name: ").strip()
        password = input("Enter password: ").strip()
        encrypt_file(infile, outfile, password)
        print(f"File encrypted and saved as {outfile}")
    elif choice == '2':
        infile = input("Enter path to file to decrypt: ").strip()
        outfile = input("Enter output decrypted file name: ").strip()
        password = input("Enter password: ").strip()
        try:
            decrypt_file(infile, outfile, password)
            print(f"File decrypted and saved as {outfile}")
        except Exception as e:
            print("Decryption failed:", str(e))
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()