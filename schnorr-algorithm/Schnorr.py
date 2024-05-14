g = 70322
a = 755
p = 88667

def public_key(g, a, p):
    x = pow(g, -1, p)
    return pow(x, a, p) % p

y = public_key(g, a, p)

k = 543

def calc_b(g, k, p):
    return pow(g, k, p)

b = calc_b(g, k, p)

r = 1000 * 2
q = 1031

def calc_ms(k, a, r, q):
    return (k + a * r) % q

c = calc_ms(k, a, r, q)

def verification(g, c, y, r, p):
    return (pow(g, c, p) * pow(y, r, p) % p)

verification_result = verification(g, c, y, r, p)
is_correct = verification_result == b

# Définitions des fonctions
def calc_ms(k, a, r, q):
    return (k + a * r) % q

def verification(g, c, y, r, p):
    return (pow(g, c, p) * pow(y, r, p) % p)

def calc_b(g, k, p):
    return pow(g, k, p)

def public_key(g, a, p):
    x = pow(g, -1, p)
    return pow(x, a, p) % p

# Constantes
g = 70322
a = 755
p = 88667
k = 543
r = 1000 * 2
q = 1031

# Calculs
y = public_key(g, a, p)
b = calc_b(g, k, p)
c = calc_ms(k, a, r, q)
verification_result = verification(g, c, y, r, p)
is_correct = verification_result == b

# Affichage des résultats
print("Clé publique (y):", y)
print("b calculé (b):", b)
print("Réponse calculée (c):", c)
print("Résultat de la vérification:", verification_result, "Est correcte:", is_correct)
