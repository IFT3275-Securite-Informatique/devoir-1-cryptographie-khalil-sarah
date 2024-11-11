# Réponse de la question 1.1
# Sarah Bedn – 20214949
# Khalil Rerhrhaye – 20179868

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

def small_e_attack(C, e, N):
    m = integer_nth_root(C, e)
    if pow(m, e) == C:
        return m
    else:
        return None

def int_to_string(n):
    message_bytes = []
    while n > 0:
        message_bytes.append(n % 256)
        n //= 256
    message_bytes.reverse()
    return bytes(message_bytes).decode('utf-8', errors='ignore')

# Clé publique Question 1.1
N = 143516336909281815529104150147210248002789712761086900059705342103220782674046289232082435789563283739805745579873432846680889870107881916428241419520831648173912486431640350000860973935300056089286158737579357805977019329557985454934146282550582942463631245697702998511180787007029139561933433550242693047924440388550983498690080764882934101834908025314861468726253425554334760146923530403924523372477686668752567287060201407464630943218236132423772636675182977585707596016011556917504759131444160240252733282969534092869685338931241204785750519748505439039801119762049796085719106591562217115679236583
e = 3

# Cryptogramme 1.1
C = 1101510739796100601351050380607502904616643795400781908795311659278941419415375

message_dechiffre = small_e_attack(C, e, N)
message_str = int_to_string(message_dechiffre)
print("Message original:", message_str)