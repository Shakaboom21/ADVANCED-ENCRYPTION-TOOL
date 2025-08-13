# Advanced Encryption Tool

A compact Python-based AES‑256 encryption and decryption tool built using the PyCryptodome library.

## ⚙️ Requirements

To use this tool, you need to install the required dependency:

```bash
pip install pycryptodome
```

## 🚀 Usage

To encrypt a file:

```bash
python main.py encrypt -i <input_file> -o <output_file>
```

To decrypt a file:

```bash
python main.py decrypt -i <input_file> -o <output_file>
```

## 📌 Features

- AES‑256 CBC mode with PKCS#7 padding.
- PBKDF2‑HMAC‑SHA256 key derivation.
- HMAC‑SHA256 integrity verification.
- Simple CLI for quick encryption/decryption.

## 🔐 Notes

- Keep your password safe; without it, decryption is impossible.
- Increase PBKDF2 iterations for stronger security.

