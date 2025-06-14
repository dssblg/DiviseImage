#TERMINER
class Couleur:
    """Paramètres :
    La class Couleur est crée pour représenter les couleurs plus facilement, elle prend trois parametres rouge vert bleu  

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    def __init__(self, rouge:int, vert:int, bleu:int):
        """init de la class Couleur

        Précondition : aucune
        Exemple(s) :
        $$$ c1 = Couleur(129,45,89)
        $$$ c1.rouge
        129
        $$$ c1.vert
        45
        $$$ c1.bleu
        89
        $$$ type(c1) == Couleur
        True

        """
        self.rouge = rouge
        self.vert = vert
        self.bleu = bleu
        
    def __repr__(self)->str:
        """renvoie une représentation de l'objet sous forme de chaine de caractère que l'utilisateur peut lire 

        Précondition : aucune
        Exemple(s) :
        $$$ c1 = Couleur(129,45,89)
        $$$ repr(c1)
        'Couleur(129, 45, 89)'
        """
        return f'Couleur({self.rouge}, {self.vert}, {self.bleu})'
    
    def __str__(self)->str:
        """renvoie une représentation de l'objet sous forme de chaine de caractère que la machine peut lire 

        Précondition : aucune
        Exemple(s) :
        $$$ c1 = Couleur(129,45,89)
        $$$ str(c1)
        "(129, 45, 89)"
        
        """
        return f"({self.rouge}, {self.vert}, {self.bleu})"
    
    def Couleur_to_tupl(self)->tuple:
        """la fonction transforme l'élément de Couleur en tuple

        Précondition : aucune
        Exemple(s) :
        $$$ c1 = Couleur(129,45,89)
        $$$ c1.Couleur_to_tupl()
        (129,45,89)

        """
        return (self.rouge, self.vert, self.bleu)
          
    def __eq__(self, autre)->bool:
        """retourne True si les deux objets de la class Couleur sont égaux (de la meme couleur) 

        Précondition : aucune
        Exemple(s) :
        $$$ c1 = Couleur(129,45,89)
        $$$ c2 = Couleur(0,45,89)
        $$$ c1 == c2
        False
        $$$ c3 = Couleur(129,45,89)
        $$$ c1 == c3
        True

        """
        if not isinstance(autre, Couleur):
            return False
        return self.rouge == autre.rouge and self.vert == autre.vert and self.bleu == autre.bleu
    