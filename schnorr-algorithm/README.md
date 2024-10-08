# Schnorr Identification Scheme

## Objective:
The main objective of this lab was to implement the Schnorr identification scheme in Python, focusing on key generation, transmission of responses, and verification in a cryptographic context.

## Algorithm Steps:
- **Public Key Calculation:** Alice calculates her public key using the given generator and prime.
- **Hidden Secret Transmission:** Alice generates a random number \( k \), calculates \( b \), and sends it to Bob for verification.
- **Response to Bob's Challenge:** Alice calculates a response \( c \) using \( k \) and Bob’s challenge \( r \).
- **Verification:** Bob verifies that Alice’s response matches the initial value of \( b \).

## Conclusion:
This lab provided a practical implementation of the Schnorr identification scheme, demonstrating key generation, challenge response, and verification in public-key cryptography.

