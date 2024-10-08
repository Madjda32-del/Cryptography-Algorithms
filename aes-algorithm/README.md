# MiniAES

## Introduction
This report details the steps and results obtained during the lab on the implementation and use of MiniAES, a simplified version of the Advanced Encryption Standard (AES) encryption algorithm. The goal was to understand the internal workings of symmetric encryption algorithms by implementing key generation, encryption, and decryption.

## Methodology
### Key Generation:
The initial key (K0) was given in hexadecimal ('B2EA') and converted to binary for processing. Round keys K1 and K2 were generated following the lab instructions, involving substitution operations (SubBytes), shifting (ShiftRows), and XOR with constants and between the key elements.

### Encryption:
A 16-bit plaintext was used as an example for the encryption process, which follows the steps of SubBytes, ShiftRows, and AddRoundKey, repeated over two rounds as specified. The MixColumns step was simplified or omitted depending on the MiniAES context.

## Challenges and Solutions:
A common error involved mishandling binary strings and incorrectly using the zip function for XOR operations. Clarifying the use of zip and its distinction from XOR helped resolve the issues.

## Results:
- K0 (binary): 1011001011101010
- K1 (binary): 1100111000001010
- K2 (binary): 1000011001101100
The ciphertext was produced by applying the MiniAES steps on the given plaintext, demonstrating the encryption process's effectiveness.

## Conclusion:
This lab provided practical understanding of how a simplified symmetric encryption algorithm works, with successful key generation and encryption processes. It also helped develop problem-solving and Python programming skills essential for analyzing and implementing security algorithms.

