# MiniAES encryption with two rounds

# Define SubByte transformation and initial key
sub_byte_transformation = {
    '0000': '1110', '0001': '0100', '0010': '1101', '0011': '0001',
    '0100': '0010', '0101': '1111', '0110': '1011', '0111': '1000',
    '1000': '0011', '1001': '1010', '1010': '0110', '1011': '1100',
    '1100': '0101', '1101': '1001', '1110': '0000', '1111': '0111'
}

# Convert initial key to binary
k0 = bin(int('B2EA', 16))[2:].zfill(16)
print(f"K0 (binary): {k0}")

# Generate K1
w0, w1, w2, w3 = k0[:4], k0[4:8], k0[8:12], k0[12:]
w4 = "".join([str(int(a)^int(b)) for a, b in zip(w0, sub_byte_transformation[w3])])  # w0 XOR SubByte(w3)
w4 = "".join([str(int(a)^int(b)) for a, b in zip(w4, '0001')])  # XOR with constant
w5 = "".join([str(int(a)^int(b)) for a, b in zip(w1, w4)])
w6 = "".join([str(int(a)^int(b)) for a, b in zip(w2, w5)])
w7 = "".join([str(int(a)^int(b)) for a, b in zip(w3, w6)])
k1 = w4 + w5 + w6 + w7
print(f"K1 (binary): {k1}")

# Generate K2
w8 = "".join([str(int(a)^int(b)) for a, b in zip(w4, sub_byte_transformation[w7])])  # w4 XOR SubByte(w7)
w8 = "".join([str(int(a)^int(b)) for a, b in zip(w8, '0010')])  # XOR with constant
w9 = "".join([str(int(a)^int(b)) for a, b in zip(w5, w8)])
w10 = "".join([str(int(a)^int(b)) for a, b in zip(w6, w9)])
w11 = "".join([str(int(a)^int(b)) for a, b in zip(w7, w10)])
k2 = w8 + w9 + w10 + w11
print(f"K2 (binary): {k2}")

# Assume a 16-bit plaintext for encryption example
plaintext = '1101011100101000'  # Example plaintext
print(f"\nEncrypting plaintext: {plaintext}")

# First Round of encryption
# 1. SubBytes
b0, b1, b2, b3 = sub_byte_transformation[plaintext[:4]], sub_byte_transformation[plaintext[4:8]], sub_byte_transformation[plaintext[8:12]], sub_byte_transformation[plaintext[12:]]
print("1. SubBytes step")
print(f"After SubBytes: {b0+b1+b2+b3}")

# 2. ShiftRows
c0, c3, c2, c1 = b0, b3, b2, b1  # ShiftRows operation
print("2. ShiftRows step")
print(f"After ShiftRows: {c0+c3+c2+c1}")

# 3. MixColumns (Note: Simplified as placeholder)
d0, d1, d2, d3 = c0, c1, c2, c3  # MixColumns placeholder for example
print("3. MixColumns step")
print(f"After MixColumns: {d0+d1+d2+d3}")

# 4. AddRoundKey with K1
# Perform XOR between the MixColumns result and K1, then split into four 4-bit parts
e = "".join([str(int(a)^int(b)) for a, b in zip(d0+d1+d2+d3, k1)])  # Apply XOR operation
e0, e1, e2, e3 = e[:4], e[4:8], e[8:12], e[12:]  # Split the result into four parts

print("4. AddRoundKey step with K1")
print(f"After AddRoundKey: {e0+e1+e2+e3}")

# Second Round (similar steps without MixColumns)
print("\nStarting Second Round...")
# 1. SubBytes
f0, f1, f2, f3 = sub_byte_transformation[e0], sub_byte_transformation[e1], sub_byte_transformation[e2], sub_byte_transformation[e3]
print("1. SubBytes step")
print(f"After SubBytes: {f0+f1+f2+f3}")

# 2. ShiftRows
g0, g3, g2, g1 = f0, f3, f2, f1  # ShiftRows operation
print("2. ShiftRows step")
print(f"After ShiftRows: {g0+g3+g2+g1}")

# 3. AddRoundKey with K2 (no MixColumns in the second round)
final_cipher = "".join([str(int(a)^int(b)) for a, b in zip(g0+g3+g2+g1, k2)])
print("3. AddRoundKey step with K2")
print(f"Final encrypted text: {final_cipher}")
