# Réponse de la question 1.2
# Sarah Bedn – 20214949
# Khalil Rerhrhaye – 20179868

import math

# Clé publique Question 1.2
N = 172219604291138178634924980176652297603347655313304280071646410523864939208855547078498922947475940487766894695848119416017067844129458299713889703424997977808694983717968420001033168722360067307143390485095229367172423195469582545920975539060699530956357494837243598213416944408434967474317474605697904676813343577310719430442085422937057220239881971046349315235043163226355302567726074269720408051461805113819456513196492192727498270702594217800502904761235711809203123842506621973488494670663483187137290546241477681096402483981619592515049062514180404818608764516997842633077157249806627735448350463
e = 173

# Cryptogramme 1.2
C = 25782248377669919648522417068734999301629843637773352461224686415010617355125387994732992745416621651531340476546870510355165303752005023118034265203513423674356501046415839977013701924329378846764632894673783199644549307465659236628983151796254371046814548224159604302737470578495440769408253954186605567492864292071545926487199114612586510433943420051864924177673243381681206265372333749354089535394870714730204499162577825526329944896454450322256563485123081116679246715959621569603725379746870623049834475932535184196208270713675357873579469122917915887954980541308199688932248258654715380981800909

#p et q trouvés a partir de la fonction find_p_q(N), environ 45min de calcul
p = 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069673
q = 16072629107794009814226375735900027158421072175583004111656255825555265766874041837397975682235437871913920093763297202377807179285384710653976866362047862205901851662236346478131611907593556712816931273229569712475372911901098151338748315919115594371856794716529813251490644747478936580257043048672231

#pure brute force attack car pourquoi pas, tant que ca marche ca marche:
def find_p_q(N):
    facteurs = []
    #limite la recherche a max(sqrt(N))
    limite = int(math.sqrt(N)) + 1

    for p in range(1, limite):
        if N % p == 0:
            q = N // p
            facteurs.append((p, q))

    return facteurs

def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Pas d'inverse multiplicatif")
    else:
      return x % m

def integer_nth_root(x, n):
    low = 1
    high = x
    while low < high:
        mid = (low + high) // 2
        if mid ** n < x:
            low = mid + 1
        else:
            high = mid
    return low

def calculate_d(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception("e et phi(n) pas preimiers entre eux")
    else:
        return x % phi

def decrypt_rsa(C, d, N):
    return modular_pow(C, d, N)

def int_to_string(n):
    message_bytes = []
    while n > 0:
        message_bytes.append(n % 256)
        n //= 256
    message_bytes.reverse()
    return bytes(message_bytes).decode('utf-8', errors='ignore')

def decrypt_message(C, e, N, p, q):
    phi = (p - 1) * (q - 1) #calcul phi
    d = calculate_d(e, phi) #calcul d
    m = decrypt_rsa(C, d, N)
    return int_to_string(m)

message_str = decrypt_message(C, e, N, p, q)
print("message Q1.2:", message_str)