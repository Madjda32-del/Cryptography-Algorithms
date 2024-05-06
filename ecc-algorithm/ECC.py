import matplotlib.pyplot as plt
import numpy as np

# Définition de la courbe elliptique
p = 31
a = -5
b = 3

#discriminant
discriminant = (-16 * (4 * a**3 + 27 * b**2)) % p
print("le discriminant est :" , discriminant)

# Point de départ convenu
A = (5, 14)

# Vérification de l'appartenance des points B et M à la courbe
def appartient_courbe(point):
    x, y = point
    return (y**2) % p == (x**3 + a*x + b) % p

B = (9, 6)
M = (12, 11)

print("Appartenance du point B à la courbe :", appartient_courbe(B))
print("Appartenance du point M à la courbe :", appartient_courbe(M))

# Fonction d'addition de points sur la courbe elliptique
def addition_point(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if point1 == point2:
        # Point doubling
        m = (3*x1**2 + a) * pow(2*y1, -1, p) % p
    else:
        # Point addition
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p
    x3 = (m**2 - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p
    return (x3, y3)

# Fonction de multiplication scalaire sur la courbe elliptique
def multiplication_scalaire(k, point):
    result = (None, None)
    addend = point

    while k > 0:
        if k & 1:
            result = addition_point(result, addend) if result[0] is not None else addend
        addend = addition_point(addend, addend)
        k >>= 1

    return result

# Calcul de M+B
M_plus_B = addition_point(M, B)
print("Le point M+B est :", M_plus_B)

# Génération d'un dictionnaire contenant les points de la courbe elliptique
def generer_dictionnaire_points():
    points = {}
    for x in range(p):
        for y in range(p):
            if appartient_courbe((x, y)):
                points[(x, y)] = True
    return points

# Clés privées d'Alice et de Bob
ka = 6
kb = 7

# Calcul de la clé publique de Bob
Q_Bob = multiplication_scalaire(kb, A)
print("La clé publique de Bob est :", Q_Bob)

# Alice chiffre le message M avec la clé ka et l'envoie à Bob
C = addition_point(M, multiplication_scalaire(ka, Q_Bob))
print("Message chiffré envoyé par Alice à Bob :", C)

# Bob reçoit le message chiffré et le déchiffre
QK = multiplication_scalaire(ka, Q_Bob)
message_decrypte = addition_point(C, (-QK[0] % p, -QK[1] % p))
print("Message déchiffré par Bob :", message_decrypte)

# Génération du dictionnaire des points de la courbe elliptique
points_courbe = generer_dictionnaire_points()
print("Nombre de points sur la courbe :", len(points_courbe))
print(points_courbe)

# Define the curve equation
def curve_equation(x):
    return (x**3 + a*x + b) % p

# Generate a list of x values
x_values = np.linspace(0, p-1, 300)
# Calculate corresponding y values for the curve equation
y_values = [np.sqrt(curve_equation(x)) % p for x in x_values]

def generer_cles_signature(point_base, n):
    clé_privée = np.random.randint(1, n)  # n est l'ordre du groupe de points
    clé_publique = multiplication_scalaire(clé_privée, point_base)
    return clé_privée, clé_publique

def signer_message(message, clé_privée, point_base, n):
    e = hash(message) % n
    while True:
        k = np.random.randint(1, n)
        R = multiplication_scalaire(k, point_base)
        r = R[0] % n
        s = (pow(k, -1, n) * (e + r * clé_privée)) % n
        if s != 0 and np.gcd(s, n) == 1:
            return (r, s)

def verifier_signature(message, signature, clé_publique, point_base, n):
    r, s = signature
    if s == 0 or np.gcd(s, n) != 1:
        return False
    e = hash(message) % n
    w = pow(s, -1, n)
    u1 = (e * w) % n
    u2 = (r * w) % n
    point1 = multiplication_scalaire(u1, point_base)
    point2 = multiplication_scalaire(u2, clé_publique)
    point_vérification = addition_point(point1, point2)
    return point_vérification[0] % n == r


# Génération des clés pour Alice
clé_privée_alice, clé_publique_alice = generer_cles_signature(A, len(points_courbe))

# Alice signe un message
message = "Bonjour, ceci est un test de signature."
signature_alice = signer_message(message, clé_privée_alice, A, len(points_courbe))

# Bob vérifie la signature d'Alice
verification = verifier_signature(message, signature_alice, clé_publique_alice, A, len(points_courbe))
print("Vérification de la signature :", verification)


# Plot the curve
plt.figure(figsize=(10, 8))
plt.plot(x_values, y_values, label='Elliptic Curve')

# Scatter plot the points on the curve
for point in points_courbe:
    plt.scatter(*point, color='red')

# Adjust the plot
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Elliptic Curve over Finite Field F_{}'.format(p))
plt.legend()
plt.show()