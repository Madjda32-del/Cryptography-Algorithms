# Elliptic Curve Cryptography (ECC)

## Objective:
This lab focused on implementing the basics of elliptic curve cryptography (ECC) in Python, including operations on elliptic curve points, encryption and decryption, and digital signatures.

## Algorithm Description:
### Elliptic Curve Definition:
The elliptic curve is defined by the equation \( y^2 \equiv x^3 + ax + b \mod p \), where \( a = -5 \), \( b = 3 \), and \( p = 31 \).

### Operations on Points:
- **Point Addition:** Adds two points on the curve.
- **Scalar Multiplication:** Multiplies a point by a scalar, crucial for generating public and private keys in ECC.

### Encryption and Decryption:
Alice encrypts a message using Bob’s public key, and Bob decrypts it using his private key.

### Digital Signature:
- **Key Generation:** Each user generates a pair of keys (public and private).
- **Message Signing:** A message is signed using the private key.
- **Signature Verification:** The signature is verified using the public key.

## Conclusion:
The ECC lab demonstrates the efficiency and security of elliptic curve cryptography for encryption, decryption, and digital signatures.

