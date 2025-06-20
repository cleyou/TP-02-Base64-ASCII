# table base 64 en liste
# A - Z, a - z, 0 - 9, +, /
tableB64 = list(map(chr, range(65, 91))) + list(map(chr, range(97, 123))) + list(map(chr, range(48, 58))) + list(map(chr, [43, 47]))

def encode(input): # encode = UTF-8 to base64. input doit être une string
    # transformer le texte en bytes UTF-8
    bytes_utf8 = input.encode('utf-8')
    # convertir chaque byte en nombre
    liste_nombres = list(bytes_utf8)
    # transformer chaque nombre en 8 bits
    liste_bits = decTo24bits(liste_nombres)
    # découper en groupes de 6 bits et convertir en nombres
    listeNb = [int(''.join(liste_bits[i:i+6]), 2) for i in range(0, len(liste_bits), 6)]
    # on récupère le caractère base64 pour chaque nombre
    x64 = [tableB64[n] for n in listeNb]
    # ajouter du padding '=' pour avoir une longueur multiple de 4
    while len(x64) % 4 != 0:
        x64.append('=')
    return ''.join(x64)

def decode(input):
    # enlever le padding '=' à la fin
    input = input.rstrip('=')
    # trouver l'index de chaque caractère dans la table base64
    indices = [tableB64.index(char) for char in input]
    # convertir chaque index en 6 bits
    liste_bits = ''.join(bin(n)[2:].zfill(6) for n in indices)
    # découper en octets de 8 bits
    listeNb = [int(liste_bits[i:i+8], 2) for i in range(0, len(liste_bits), 8)]
    # on retire les bytes incomplets à la fin
    while listeNb and listeNb[-1] == 0:
        listeNb.pop()
    # transformer les nombres en bytes
    bytes_resultat = bytes(listeNb)
    # décoder les bytes UTF-8 en texte
    try:
        output = bytes_resultat.decode('utf-8')
    except:
        output = "erreur de décodage UTF-8"
    return output

def decTo24bits(lst):
    # convertir chaque nombre en représentation binaire sur 8 bits
    liste_bits = []
    for nombre in lst:
        # transformer en binaire et compléter à 8 bits
        bits_8 = bin(nombre)[2:].zfill(8)
        # ajouter chaque bit individuellement
        for bit in bits_8:
            liste_bits.append(bit)
    # compléter avec des 0 pour avoir un multiple de 6 bits
    while len(liste_bits) % 6 != 0:
        liste_bits.append('0')
    return liste_bits

# test avec des caractères UTF-8
crypte = encode("lettre mim م ; emoji monde 🌍.")
print("Encode:", crypte)
print("Décode:", decode(crypte))

# test simple ()
crypte2 = encode("ABCD!")
print("Simple:", crypte2)
print("Retour:", decode(crypte2))
