# -*- coding: utf-8 -*-


from random import choice


def choix_mot(adresse_fichier):
    """ fonction ouvrant un fichier texte dont l'adresse absolue ou relative
    est passée en argument sous la forme d'une chaine de caractère
    et renvoyant une chaine de caractère issue d'une ligne aléatoire du fichier
"""
    with open(adresse_fichier,'r', encoding='utf8') as file:
        mot = choice(list(file.readlines())).replace('\n', '').strip()
    return mot

def formate_mot(mot : str) -> str :
    """ fonction transformant une chaine de caractères accentués
en une chaine de caractère latin strict (sans accents ni signes diacritiques).
La chaine renvoyée est en majuscule.

>>> formate_mot('tRuC')
'TRUC'
>>> formate_mot('Abécédaire')
'ABECEDAIRE'
>>> formate_mot('')
''
>>> formate_mot('où')
'OU'
>>> formate_mot('garçONs')
'GARCONS'
>>> formate_mot('àâäéèêëîïôöûùüç')
'AAAEEEEIIOOUUUC'
>>> formate_mot('œil')
'OEIL'
>>> formate_mot('Lætitia')
'LAETITIA'
""" 
    from unidecode import unidecode
    return unidecode(mot).upper()
    
def genere_tirets(mot_a_trouver : str, lettres_utilisees: str ) -> str :
    """ fonction renvoyant une chaine de caractère correspondant
au mot à trouver pour lequel :
* les caractères non présents dans la chaine lettreUtilisees
sont remplacés par des _ (underscores) ;
* les tirest hauts "-" sont conservés ;
* tous les caractères sont suivis d'un espace, y compris le dernier.

>>> genere_tirets("Bidules", "Ble")
'B _ _ _ l e _ '
>>> genere_tirets("toto", "")
'_ _ _ _ '
>>> genere_tirets("bananes", "bn")
'b _ n _ n _ _ '
>>> genere_tirets("toto", "ot")
't o t o '
>>> genere_tirets("pull-over", "plr")
'p _ l l - _ _ _ r '
>>> genere_tirets("pull-over", "pulover")
'p u l l - o v e r '
"""
    finalString = ""
    for letterToFind in mot_a_trouver :
      if letterToFind in lettres_utilisees :
        for letter in lettres_utilisees :
          if letter == letterToFind :
            finalString += letter
            break
      elif letterToFind == "-" :
        finalString += "-"
      else :
        finalString += "_"
      finalString += " "
    return finalString
    
    
def compte_restantes(mot_a_trouver : str, lettres_utilisees : str ) -> int :
    """ fonction renvoyant le nombre de lettres non encore trouvées
dans le mot, en connaissant les lettres déjà utilisées.
Un tiret haut "-" ne compte pas dans les lettres à trouver.
La valeur renvoyée est un entier

>>> compte_restantes("bananes","bn")
4
>>> compte_restantes("toto","to")
0
>>> compte_restantes("toto","")
4
>>> compte_restantes("","")
0
>>> compte_restantes("","z")
0
>>> compte_restantes("bidules","bidule")
1
>>> compte_restantes("pull-over", "plr")
4
>>> compte_restantes("pull-over", "pulover")
0
>>> compte_restantes("lætitia", "ltia")
1

"""
    nb_letterfinded = sum(mot_a_trouver.count(letter) for letter in lettres_utilisees)
    return len(mot_a_trouver.replace('-', '')) - nb_letterfinded
        
def affiche_pendu(mot_a_trouver : str, lettres_utilisees : str, nb_echecs : int) -> None :
    """ fonction affichant à la fois la potence mais aussi le mot
à trouver sous sa forme de tirets
    """
    backslash = '\\'
    def afficheMembre(maxFail: int, membre: str) -> str:
        return membre if nb_echecs >= maxFail else ' '
        
    return f"""
                                                   _ _ _
                                                  {afficheMembre(1, 'o')}     |
                                                {afficheMembre(2, '/')} {afficheMembre(3, '|')} {afficheMembre(4, backslash)}   |
                                                 {afficheMembre(5, '/')} {afficheMembre(6, backslash)}    |
                                                        |
                                                 _______|__ 
{genere_tirets(mot_a_trouver, lettres_utilisees)}
    """
    
def demande_joueur_lettre() -> str:
    """ fonction demandant une lettre latine non accentuée au joueur,
et renvoyant cette lettre en majuscule. La fonction redemande au joueur
tant que celui-ci n'a pas fourni une lettre correcte.
La lettre est renvoyée en par la fonction.
"""
    import re
    chosenLetter = input("Quelle lettre choisissez-vous ? ") 
    if len(chosenLetter) == 1 and re.match("[a-zA-Z]", chosenLetter) :
        chosenLetter = str(chosenLetter.upper())
        return chosenLetter
    else :
        print("Je ne comprend pas ! Veuillez recomencer !")
        return demande_joueur_lettre()
    
    
def une_manche() -> None :
    """ fonction déclenchant une manche de jeu. On entend par manche de jeu :
* le choix d'un mot dans le fichier 'liste_francais_modifiee.txt' ;
* le formatage de ce mot ;
* puis la répétitions de :
    * la demande d'une lettre au joueur ;
    * la mise à jour des lettres utilisée le cas échéant ;
    * la mise à jour de l'affichage
    
    jusqu'à ce que soit le mot complet ait été trouvé,
    soit que le dessin du pendu soit terminé (6 étapes).
    """
    chosenWord = choix_mot("liste_francais_modifiee.txt")
    formatChWo = formate_mot(chosenWord)
    proposedLetters = ""
    goodProposedLetters = ""
    nbFailure = 0
    while True :
        chosenLetter = demande_joueur_lettre()
        if chosenLetter in proposedLetters :
            print("Lettre déjà proposé !")
            continue
        else :
            proposedLetters += chosenLetter
            if chosenLetter in formatChWo :
                goodProposedLetters += chosenLetter
            else :
                nbFailure += 1
        print(affiche_pendu(formatChWo, goodProposedLetters, nbFailure))
        if nbFailure >= 6 or compte_restantes(formatChWo, goodProposedLetters) == 0 :
            break
    if nbFailure >= 6 :
        print(f"Vous avez échoué ! Le mot à trouver était : {formatChWo}")
    elif compte_restantes(formatChWo, goodProposedLetters) == 0 :
        print(f"Vous avez réussi ! Vous avez trouvé le mot : {formatChWo}")
        
def presentation() -> None :
    """ fonction affichant uniquement la présentation"""
    print("""
##############################################
#                                            #
#                Jeu du Pendu                #
#                                            #
# 1ère NSI 2022-2023                         #
##############################################
""")
    
            
def main() -> None:
    """ fonction principale du jeu, permettant d'effectuer plusieurs manches"""
    while True :
        presentation()
        une_manche()
        rep = input("Voulez-vous rejouer ? (o/n)")
        if rep.lower() not in ['o', 'oui', 'y', 'yes'] :
            break
    print("Au revoir !")

## La partie ci-dessous n'est effectuée que si vous déclenchez le programme
## en tant que programme principal (notion de modules, vue en terminale)
            
if __name__ == "__main__" :
    
    import doctest
    doctest.testmod()
    main()