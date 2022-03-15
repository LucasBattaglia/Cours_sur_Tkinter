def Verif_mdp(char1, char2):
    if char1 == char2:
        return True
    return False


def Verif_adresse(adresse):
    adresse = adresse.split('@')
    adresse = adresse[1].split(".")
    if adresse[0] in ['etu', 'free', 'gmail', 'hotmail']:
        if adresse[1] in ['fr', 'com']:
            return True
    elif adresse[0] == 'etu':
        if adresse[1] == 'uca' and adresse[2] == 'fr':
            return True
    return False
