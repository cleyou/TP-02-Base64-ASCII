# énoncé : Dans le language de programmation de votre choix, réaliser un script qui encode et décode en base64.
# Aucune bibliothèque qui ferait tout automatiquement n'est autorisé.


# table ASCII en liste, jusqu'à l'index 127
tableASCII = list(map(chr, range(128)))
# table base 64 en liste
# A - Z, a - z, 0 - 9, +, /
tableB64 = list(map(chr, range(65, 91))) + list(map(chr, range(97, 123))) + list(map(chr, range(48, 58))) + list(map(chr, [43, 47]))

def encode(input): # encode = ASCII to base64. input doit être une string ou un char
    # on transforme la chaîne en tableau de codes ASCII (étape 1-2)
    liste = [ord(char) for char in input]
    # convertir en bits sur 8 puis découper en 6 bits (étapes 3-5)
    liste_bits = decTo24bits(liste)
    # transformer chaque groupe de 6 bits en nombre décimal (étape 6)
    listeNb = [int(''.join(liste_bits[i:i+6]), 2) for i in range(0, len(liste_bits), 6)]
    # récupérer le caractère base64 correspondant à chaque nombre (étape 7)
    x64 = [tableB64[n] for n in listeNb]
    # ajouter du padding pour avoir une longueur multiple de 4 (étape 9)
    while len(x64) % 4 != 0:
        x64.append('=')
    return ''.join(x64)

def decode(input):
    # enlever le padding '=' qui ne sert plus
    input = input.rstrip('=')
    # retrouver les indices dans la table base64
    indices = [tableB64.index(char) for char in input]
    # reconvertir en bits de 6 puis regrouper
    liste_bits = ''.join(bin(n)[2:].zfill(6) for n in indices)
    # découper en octets de 8 bits pour retrouver les codes ASCII
    listeNb = [int(liste_bits[i:i+8], 2) for i in range(0, len(liste_bits), 8)]
    # transformer les codes ASCII en caractères
    output = ''.join(chr(n) for n in listeNb)
    return output

def decTo24bits(lst):
    # prendre chaque nombre et le convertir en 8 bits (étape 3)
    liste_bits = ''.join(bin(n)[2:].zfill(8) for n in lst)
    # compléter avec des 0 pour avoir un multiple de 6 bits (étape 5)
    while len(liste_bits) % 6 != 0:
        liste_bits += '0'
    return list(liste_bits)

# test du script
crypte = encode("ABCD!")
print(crypte)
print(decode(crypte))
