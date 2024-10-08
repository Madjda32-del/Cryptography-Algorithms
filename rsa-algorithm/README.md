# RSA Algorithm

## Objective:
The goal of this lab was to understand and implement the RSA encryption algorithm, which uses asymmetric cryptography to secure communication between two parties.

## Key Steps:
### Key Generation:
- Two prime numbers \( p \) and \( q \) are selected, and their product \( n = p * q \) is calculated.
- Euler’s totient function \( \phi = (p-1)(q-1) \) is calculated.
- A number \( e \) is chosen such that \( 1 < e < \phi \) and is co-prime with \( \phi \).
- Using the extended Euclidean algorithm, a number \( d \) is computed such that \( d*e \mod \phi = 1 \).

### Encryption:
The plaintext message is converted into numbers (e.g., using ASCII values), and each number is encrypted with the public key.

### Decryption:
Each encrypted number is decrypted using the private key.

## Conclusion:
Implementing RSA helped understand asymmetric cryptography principles, including key generation, encryption, and decryption, which are vital for securing digital communications.

