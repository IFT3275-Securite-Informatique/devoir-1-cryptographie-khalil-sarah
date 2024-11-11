from collections import Counter
from crypt import load_text_from_web

def analyse_frequence_texte(texte):
    # Analyse de fréquence des caractères simples
    frequence_caracteres = Counter(texte)

    # Total de caractères pour le calcul des pourcentages
    total_caracteres = len(texte)

    # Analyse de fréquence des bicaractères
    bicaracteres = [texte[i:i + 2] for i in range(len(texte) - 1)]
    frequence_bicaracteres = Counter(bicaracteres)

    # Total de bicaractères pour le calcul des pourcentages
    total_bicaracteres = len(bicaracteres)

    # Conversion des fréquences en pourcentages
    frequence_caracteres_percentage = {char: (freq / total_caracteres) * 100 for char, freq in frequence_caracteres.items()}
    frequence_bicaracteres_percentage = {pair: (freq / total_bicaracteres) * 100 for pair, freq in frequence_bicaracteres.items()}

    # Fusion des dictionnaires de fréquences
    frequence_combined = frequence_caracteres_percentage.copy()
    for pair, perc in frequence_bicaracteres_percentage.items():
        if pair in frequence_combined:
            frequence_combined[pair] += perc
        else:
            frequence_combined[pair] = perc

    # Tri des fréquences combinées par ordre décroissant
    frequence_combined_sorted = dict(sorted(frequence_combined.items(), key=lambda item: item[1], reverse=True))

    return frequence_combined_sorted

def analyse_frequence_octets(C):
    # Diviser la séquence en octets de 8 bits
    octets = [C[i:i + 8] for i in range(0, len(C), 8)]

    # Compter la fréquence de chaque octet
    frequences = Counter(octets)

    # Calculer le pourcentage pour chaque octet
    total_octets = len(octets)
    frequences_pourcentage = {octet: (count / total_octets) * 100 for octet, count in frequences.items()}

    # Classer les octets par fréquence décroissante
    frequences_pourcentage_triees = dict(sorted(frequences_pourcentage.items(), key=lambda item: item[1], reverse=True))

    return frequences_pourcentage_triees

def decrypt(C):
    # Charger les textes des URLs
    url1 = "https://www.gutenberg.org/ebooks/13846.txt.utf-8"
    url2 = "https://www.gutenberg.org/ebooks/4650.txt.utf-8"
    corpus1 = load_text_from_web(url1)
    corpus2 = load_text_from_web(url2)
    
    if corpus1 is None or corpus2 is None:
        raise ValueError("Error loading the corpus.")
    
    # Combiner les textes pour créer un corpus
    combined_corpus = corpus1 + corpus2
    
    # Effectuer une analyse de fréquence sur le corpus
    frequence_dico = analyse_frequence_texte(combined_corpus)
    
    # Effectuer une analyse de fréquence sur le cryptogramme
    frequence_resultat = analyse_frequence_octets(C)
    
    # Créer une correspondance des octets du cryptogramme aux caractères du corpus
    char_mapping = {}
    for crypt_octet, corpus_char in zip(frequence_resultat.keys(), frequence_dico.keys()):
        char_mapping[crypt_octet] = corpus_char
    
    # Déchiffrer le cryptogramme en utilisant la correspondance de fréquence
    octets = [C[i:i + 8] for i in range(0, len(C), 8)]
    decrypted_message = ''.join(char_mapping.get(octet, '?') for octet in octets)
    
    return decrypted_message
