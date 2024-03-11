from collections import deque

# Définition des tables de permutation et des S-boxes
p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
p8 = [5, 2, 6, 3, 7, 4, 9, 8]
pi = [1, 5, 2, 0, 3, 7, 4, 6]
ep = [3, 0, 1, 2, 1, 2, 3, 0]
pi_1 = [3, 1, 5, 2, 6, 0, 7, 4]
p4 = [1, 3, 2, 0]

# Conversion des S-boxes en une structure plus simple pour un accès direct
S_0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S_1 = [
    [0, 2, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Fonctions de permutation et de substitution
def permute(key, perm):
    return [key[p] for p in perm]

def sbox_lookup(input_bits, sbox):
    row = (input_bits[0] << 1) + input_bits[3]
    col = (input_bits[1] << 1) + input_bits[2]
    return [int(bit) for bit in format(sbox[row][col], '02b')]

# Fonction de chiffrement avec S-boxes et permutations
def encrypt(plaintext, key):
    # Génération des clés
    key_permuted = permute(key, p10)
    key_left, key_right = key_permuted[:5], key_permuted[5:]
    key_left = deque(key_left)
    key_right = deque(key_right)

    print("key :", key)
    
    # Rotation et génération des sous-clés
    key_left.rotate(-1)
    key_right.rotate(-1)
    k1 = permute(list(key_left) + list(key_right), p8)
    print("k1 = ", k1)
    
    key_left.rotate(-2)
    key_right.rotate(-2)
    k2 = permute(list(key_left) + list(key_right), p8)
    print("k2 = ", k2)
    
    # Permutation initiale du texte
    data = permute(plaintext, pi)
    left, right = data[:4], data[4:]
    
    # Première ronde
    right_expanded = permute(right, ep)
    xor_with_k1 = [a ^ b for a, b in zip(right_expanded, k1)]
    sbox_output = sbox_lookup(xor_with_k1[:4], S_0) + sbox_lookup(xor_with_k1[4:], S_1)
    p4_output = permute(sbox_output, p4)
    left = [a ^ b for a, b in zip(left, p4_output)]
    
    # SW (échange des moitiés)
    left, right = right, left
    
    # Deuxième ronde
    right_expanded = permute(right, ep)
    xor_with_k2 = [a ^ b for a, b in zip(right_expanded, k2)]
    sbox_output = sbox_lookup(xor_with_k2[:4], S_0) + sbox_lookup(xor_with_k2[4:], S_1)
    p4_output = permute(sbox_output, p4)
    left = [a ^ b for a, b in zip(left, p4_output)]
    
    # Permutation inverse finale
    final_data = permute(left + right, pi_1)
    return final_data

# Exemple d'utilisation
plaintext = [0, 1, 1, 1, 0, 0, 1, 0]  # Représentation binaire de 0xAA
key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]  # Clé de 10 bits

encrypted = encrypt(plaintext, key)
print("plaintext :",plaintext)

print(f"Encrypted: {''.join(map(str, encrypted))}")
