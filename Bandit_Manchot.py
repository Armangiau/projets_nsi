# -*- coding: utf-8 -*-


#### PROJET MACHINE A SOUS
### 1ère NSI Pavie 2022-2023

import random

symboles = '♠♥♦♣7Ω' ## Symboles utilisés dans le bandit-manchot


def choisir_symbole(symboles : str) -> str:
    """
fonction renvoyant un symbole aléatoire parmi une suite de symbole passée en argument
"""
    assert type(symboles) == str, "Bad symbole argument"
    return random.choice(symboles)

def fabriquer_chaine(symboles : str, taille : int = 3) -> str:
    """ fonction renvoyant une chaine aléatoire de dimension taille,
à partir de la liste de symbole symboles.
"""
    assert type(symboles) == str, "Bad symbole argument"
    assert type(taille) == int, 'Bad taille argument'
    return ''.join(choisir_symbole(symboles) for _ in range(taille))
    # ici on joint les {taille}(3) symboles généré aléatoirement par fonction choisir_>>> presence_symboles_identiques_multiples('', '')symbole

def compte_symboles_identiques(s : str, chaine: str) -> int :
    """
Fonction renvoyant le nombre d'occurences du symbole s au sein de la chaine chaine
Si le symbole n'est pas présent, renvoie 0

>>> compte_symboles_identiques("a", "abracadabra")
5
>>> compte_symboles_identiques("c", "abracadabra")
1
>>> compte_symboles_identiques("o", "abracadabra")
0
>>> compte_symboles_identiques("a", "")
0
>>> compte_symboles_identiques("", "abracadabra")
0
>>> compte_symboles_identiques("", "")
0
"""
    nb_symboles_identiques = 0
    for char in chaine:
        if char == s:
            nb_symboles_identiques += 1
    return nb_symboles_identiques
    # compte le nombre de s dans chaine  - si chaine ou s est vide retourner 0

def presence_symboles_identiques_multiples(symboles : str, chaine : str) -> bool:
    """ Fonction renvoyant un booléen True si l'un des symboles présent dans
la chaine symboles est présent plusieurs fois dans la chaine chaine, et False sinon

>>> presence_symboles_identiques_multiples('abc', 'abracadabra')
True
>>> presence_symboles_identiques_multiples('abc', 'abcdef')
False
>>> presence_symboles_identiques_multiples('a', 'aaaa')
True
>>> presence_symboles_identiques_multiples('abc', 'efgh')
False
>>> presence_symboles_identiques_multiples('', 'treytlei')
False
>>> presence_symboles_identiques_multiples('a', '')
False
>>> presence_symboles_identiques_multiples('', '')
False
"""
    for symbole in symboles:
        is_nb_symbole_identique_supérieur_a_1 =  compte_symboles_identiques(symbole, chaine) > 1 # on doit avoir plusieurs symboles identiques
        if is_nb_symbole_identique_supérieur_a_1 :
            return is_nb_symbole_identique_supérieur_a_1
    return False

def table_gain(chaine : str, mise: int) -> int:
    """
    Fonction renvoyant le gain selon la chaine passée en argument
    A titre d'information, l'espérance de gain avec la table donnée est de 37.5
>>> table_gain('777', 20)
2000
>>> table_gain('ΩΩΩ', 20)
1000
>>> table_gain('♥♥♥', 10)
200
>>> table_gain('Ω7Ω', 15)
150
>>> table_gain('♠♠7', 10)
50
>>> table_gain('7♠♠', 10)
50
>>> table_gain('♠7♣', 25)
50
>>> table_gain('♠77', 50)
0
    """
    
    # les cas spéciaux de la table codés en dur
    if chaine == '777':
        return mise * 100
    elif chaine == 'ΩΩΩ':
        return mise * 50
    elif chaine == '♥♥♥' or chaine =='♠♠♠' or chaine == '♣♣♣' or chaine == '♦♦♦':
        return mise * 20
    elif chaine == 'Ω7Ω' or chaine =='ΩΩ7' or chaine == '7ΩΩ' :
        return mise * 10 
    elif '7' in chaine and not '77' in chaine and presence_symboles_identiques_multiples(chaine, chaine) : # si la chaine contien un 7 et deux autres carractères identiques
        return mise * 5
    elif not presence_symboles_identiques_multiples(chaine, chaine): # si chaque symbole est différent
        return mise * 2
    else:
        return 0
    
    
def saisir_mise(pot : int) -> int:
    """ Fonction récupérant la mise du joueur / de la joueuse,
     qui doit être un nombre entier compris entre 10 et pot.
     Cette fonction ne peut pas être testée par doctest."""
    user_input = demander_str(f'Entrez une mise entière entre 10 et {pot} :\n')
    if user_input.isnumeric() and 10 <= int(user_input) <= pot: # vérifit que la chaîne du nombre est entière et > à 0
        return int(user_input)
    print(f"Vous n'avez pas saisie un entier define entre 10 et {pot}")
    return saisir_mise(pot)

def demander(message = 'Voulez vous rejouer ?') ->  bool :
    """Fonction demandant au joueur / à la joueuse si il/elle souhaite faire l'action demandé.
    Le joueur/La joueuse doit pouvoir répondre par oui (ou o) ou par non (ou n),
    et la fonction doit être dumbproof.
    Ne peut pas être testée par doctest.
    """
    user_input = demander_str(f'{message} (o/n)').lower()
    if user_input not in ['o', 'oui', 'n', 'non'] :
        print('Je ne comprend pas voulez vous continuer ou arrêter')
        return demander(message)
    return user_input in ['o', 'oui']

def demander_str(message) -> str:
    """
Demande d'entrer une chaine de caractère
    """
    while True :
        entree_utilisteur = input(message).strip()
        if entree_utilisteur :
            return entree_utilisteur
        print("Vous n'avez rien entré")

                
def afficher_bandit(chaine : str, gain : int) -> None:
    """
    Fonction affichant dans la console le bandit-manchot, avec le tirage obtenu.
    Affiche aussi le gain réalisé.
    Renvoie None.
    Ne peut pas être testée par doctest.
    """
    print(f"""
    -------------
    |   |   |   |   o
    | {chaine[0]} | {chaine[1]} | {chaine[2]} |  //
    |   |   |   | //
    -------------//

    Vous gagnez {gain} €
    """)

def same_gamer(name, score, same_name_gamer) :
    """
    Fonction appelé lorsque deux noms sont identiques,
    elle revoie le nom de la partie avec le meilleur score si l'utillisateur nous confirme avoir déjà joué,
    sinon elle demande un nouveau nom à l'utilisateur
"""
    if same_name_gamer['want_to_replay'] == 'True' :
        return name, score
    if demander('Avez vous déjà joué avec ce nom ?') :
        if same_name_gamer['score'] < score :
            return name, score
        else :
            return name, same_name_gamer['score']
    return demander_str('Votre nom à déjà été enregistré:\nVotre noveau nom est: '), score

def demande_inscription(capital: int, gamer: str) -> None :
    if demander('Voulez vous sauvegarder votre partie ?') :
        want_to_replay = demander('Voudrez vous continuer votre partie plus tard ?')
        sauve_score(gamer, capital, want_to_replay, same_gamer)

def ask_view_score() :
    if demander('Voulez vous regarder le classement ?') :
        print(read_save().affiche_score())

def reprendre_partie_and_set_score(nom: str) -> int:
    """
Regarde dans le fichier de sauvegarde si le joueur voulait reprendre sa partie et renvoie son score s'il veut toujours reprendre cette partie,
sinon il renvoie la somme de 500 par défault
    """
    donees_txt = read_save().get_score()
    for gamer in donees_txt :
        assert type(gamer['want_to_replay']) == bool, '{want_to_replay} must be a boolean'
        if gamer['nom'] == nom and gamer['want_to_replay'] and gamer['score'] > 0:
            if demander('Voulez vous reprendre une partie déjà jouée'):
                return gamer['score']
    return privilegies(["fabien", "paolo", "armand"], nom) # quelque joueurs ayant participé au projet on droit à quelque privilèges


def privilegies(names, name) -> int:
    """
Fonction calculant le capitale de départ des privilègiés en conertissant leur nom de base 36 en base 10,
sinon pour les non privilégiés renvoitla somme par défaut : 50
>>> privilegies(["fabien", "paolo", "armand"], 'fabien')
Vous bénéficiez d'un petit privilège, faites en bone usage !
924325871
>>> privilegies(["fabien", "paolo", "armand"], 'Armand')
Vous bénéficiez d'un petit privilège, faites en bone usage !
651051625
>>> privilegies(["fabien", "paolo", "armand"], 'PaolO')
Vous bénéficiez d'un petit privilège, faites en bone usage !
42488844
    """
    if name.lower() in names :
        print("Vous bénéficiez d'un petit privilège, faites en bone usage !")
        return int(name, 36)
    return 500

def presentation() -> None :
    """ fonction affichant la présentation, et donnant les règles du jeu"""
    print("\n"*50)
    print("""
##############################################
#                                            #
#              Bandit Manchot                #
#                                            #
# 1ère NSI 2022-2023                         #
##############################################
""")
    print("\n"*5)
    print("Vous disposez d'un capital de départ de 500 € pour jouer au bandit manchot !")
    print("\n"*2)


def main_game() -> int:
    """
    Fonction principale du jeu, qui lance une partie, et se poursuiit tant que le joueur /la joueuse
    souhaite ou peut continuer.
    Ne peut pas être testée par doctest.
    """
    presentation()
    nom = demander_str('Quel est votre prénom ? ')
    capital = reprendre_partie_and_set_score(nom)
    
    while True:
        mise = saisir_mise(capital)
        capital -= mise
        resultat_du_tirage = fabriquer_chaine(symboles)
        guain = table_gain(resultat_du_tirage, mise)
        capital += guain

        afficher_bandit(resultat_du_tirage, guain)
        print(f"Vous avez à présent {capital}€")

        if capital == 0 :
            print("Désolé c'est la fin de la partie vous n'avez plus d'argent")
            break
        elif not demander():
            print(f"Vous repartez avec la côquette some de {capital}€")
            break

    x = demande_inscription(capital, nom)
    if x is None :
        ask_view_score()
    return capital


class sauve_score :

    def __init__(self, nom_j : str, score_j: int, want_to_replay: bool, same_name_gamer) -> None :
        self.nom_j, self.score_j, self.want_to_replay = nom_j, score_j, want_to_replay
        self.same_name_gamer = same_name_gamer
        self._read_previous_save()
        self._write_score()

    def _read_previous_save(self) -> None :
        """
Lit les score déjà enregistré en modifiant {self.hight_score}
"""
        try :
            with open('HighScore.txt',"r", encoding="utf-8") as file :
                lines = file.readlines()
                self.hight_score = [{"nom":"", "score" : 0, "want_to_replay": False}]*len(lines)
                for i, line in enumerate(lines) :
                    nom, score, replay = line.split(" / ")
                    replay = replay.replace('\n', '')
                    try :
                        self.hight_score[i] = {"nom" : nom, "score" : int(score), "want_to_replay": replay}
                    except ValueError :
                        self.hight_score[i] = {"nom" : nom, "score" :0, "want_to_replay": replay}
            self._same_gamer()
            self._sort_hight_score()
        except FileNotFoundError :
            self.hight_score =[{"nom" : self.nom_j, "score" : self.score_j, "want_to_replay": self.want_to_replay}]

    def _same_gamer(self) -> None:
        """
Vérifit si le nom du joueur à déjà été enregitré, dans ce cas il enclanche la callback {self.same_name_gamer},
qui définit le comprtement associé
"""
        for gamer in self.hight_score:
                if gamer['nom'] == self.nom_j :
                    self.hight_score.remove(gamer)
                    self.nom_j, self.score_j = self.same_name_gamer(self.nom_j, self.score_j, gamer)
    
    def _sort_hight_score(self) -> None:
        for i, gamer in enumerate(self.hight_score) :
            saved_gamer_score = int(gamer['score'])
            if self.score_j >= saved_gamer_score :
                self.hight_score.insert(i, {"nom" : self.nom_j, "score" : self.score_j, 'want_to_replay': self.want_to_replay})
                return
        self.hight_score.append({"nom" : self.nom_j, "score" : self.score_j, 'want_to_replay': self.want_to_replay})
        
    def _write_score(self) -> None:
        """"
écrit le score du joueur dans le fichier HighScore.txt
"""
        with open("HighScore.txt", "w", encoding="utf8") as file :
            for s in self.hight_score :
                if s is not None :
                    file.write(f"{s['nom']} / {s['score']} / {s['want_to_replay']}\n")
                else :
                    file.write(f"Inconnu / 0\n")


class read_save :
    def get_score(self):
        """ Fonction récupérant les HighScore sauvegardés depuis un fichier HishScore.txt,
            et qui renvoie une chaine de caractères correctement formatée pour la console"""
        lines =""
        try:
            with open('HighScore.txt',"r", encoding="utf-8") as f  :
                lines = f.readlines()
        except FileNotFoundError :
                return []
        return [{'nom': line.split(" / ")[0], 'score': int(line.split(" / ")[1]), 'want_to_replay': line.split(" / ")[2].replace("\n", "") == 'True'} for line in lines]

    def affiche_score(self) -> str:
        return "".join(f"{index + 1} {d['nom']:>15} : {d['score']:>11} €\n" for index, d in enumerate(self.get_score()[:10]))

## La partie ci-dessous n'est effectuée que si vous déclenchez le programme
## en tant que programme principal (notion de modules, vue en terminale)

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
    main_game()