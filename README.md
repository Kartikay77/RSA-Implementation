# 🔐 RSA-Implementation
A minimal **RSA Encryption & Decryption** system in Python.  
Implements RSA **key generation**, **encryption**, and **decryption**, with a simple test harness and file-based input.

![Screenshot](https://github.com/Kartikay77/RSA-Implementation/blob/main/RSA.png)

---

## 📦 Project Structure
- `rsa.py` — Core RSA functions (keygen, encrypt, decrypt)
- `test.py` — Runner that loads inputs, generates keys, encrypts & decrypts messages
- `input.txt` — Sample input (primes + messages)

---

## ✅ Features
- Generates **public (e, n)** and **private (d, n)** keys
- Encrypts / decrypts integer messages
- Simple file-driven testing for quick verification

---

## 📝 Input Format (`input.txt`)
Line 1: two primes `p q`  
Next 5 lines: one integer **message** per line to encrypt/decrypt.

**Example**
67 83
24
29
31
16
13


> ⚠️ **Mac users (TextEdit)**: Use **Format → Make Plain Text** so `input.txt` is not saved as RTF.

---

## 🚀 How to Run


# 1) Clone (or open the folder if you already have it)
```
git clone https://github.com/Kartikay77/RSA-Implementation.git
cd RSA-Implementation
```
# 2) Ensure input.txt exists (see format above)

# 3) Run the test harness
```
python3 test.py -i input.txt
```

# 🧪 Example Output
p: 67, q: 83, phi: 5412, pu: (5561, 13), pr: (5561, 1249), message: 24, encrypted: 3658, decrypted: 24
p: 67, q: 83, phi: 5412, pu: (5561, 13), pr: (5561, 1249), message: 29, encrypted: 1838, decrypted: 29
p: 67, q: 83, phi: 5412, pu: (5561, 13), pr: (5561, 1249), message: 31, encrypted: 87,   decrypted: 31
p: 67, q: 83, phi: 5412, pu: (5561, 13), pr: (5561, 1249), message: 16, encrypted: 2600, decrypted: 16
p: 67, q: 83, phi: 5412, pu: (5561, 13), pr: (5561, 1249), message: 13, encrypted: 928,  decrypted: 13

#  Background
RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem.
Public key (e, n) encrypts
Private key (d, n) decrypts
Security relies on the difficulty of factoring n = p⋅q for large primes.

# Possible Improvements
Larger key sizes & probabilistic prime generation
Padding (e.g., PKCS#1 v1.5, OAEP) for real-world security
String/byte message support & chunking
Simple CLI: --gen, --encrypt, --decrypt
