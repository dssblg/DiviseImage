# PEUT ETRE MODIFIER LA PARTIE POUR RECUPERER LES SOUS BLOCS SI UTILE 
from Couleur import Couleur
from Coordone import *
import dill
import csv

class Bloc:
    """Paramètres :
    La class Bloc a etait créer pour faciliter la mise en place de blocs, elle prend en parametre les Coordonées du point le plus haut à gauche du bloc et les coordonnées du point le plus bas à droite du bloc ,et ( la couleur ) ou (les 4 sous_blocs)  

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    
    def __init__(self, haut_gauche: Coordone, bas_droite: Coordone, couleur: Couleur | None , sous_blocs: list['Bloc']):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ bloc1 = Bloc(Coordone(0, 0), Coordone(255, 255), Couleur(123,98,23), [])
        $$$ bloc1.haut_gauche
        Coordone(0, 0)
        $$$ bloc1.bas_droite
        Coordone(255, 255)
        $$$ bloc1.couleur
        Couleur(123,98,23)
        $$$ bloc1.sous_blocs
        '[]'
        $$$ bloc2 = Bloc( Coordone(0, 0), Coordone(255, 255), None, [Bloc( Coordone(0, 0), Coordone(128, 128), Couleur(123,98,23), []), Bloc( Coordone(128, 0), Coordone(255, 128), Couleur(123,98,23), []), Bloc( Coordone(0, 128), Coordone(128, 255), Couleur(123,98,23), []),Bloc( Coordone(128, 128), Coordone(255, 255), Couleur(123,98,23), [])])
        $$$ bloc2.haut_gauche
        Coordone(0, 0)
        $$$ bloc2.bas_droite
        Coordone(255, 255)
        $$$ bloc2.couleur
        None
        $$$ bloc2.sous_blocs
        '[Bloc( Coordone(0, 0), Coordone(128, 128), Couleur(123, 98, 23), []), Bloc( Coordone(128, 0), Coordone(255, 128), Couleur(123, 98, 23), []), Bloc( Coordone(0, 128), Coordone(128, 255), Couleur(123, 98, 23), []), Bloc( Coordone(128, 128), Coordone(255, 255), Couleur(123, 98, 23), [])]'
        """
    
        assert (couleur == None) != (sous_blocs == []) # si il y a la couleur alors sous_blocs doit etre vide et inversement si il y a sous_blocs alors couleur doit valoir None
        self.haut_gauche = haut_gauche
        self.bas_droite = bas_droite
        self.couleur = couleur
        self.sous_blocs = repr(sous_blocs)
        
        
    def __repr__(self):
        """Elle renvoie une représentation de l'objet sous forme de chaine de caractère que l'utilisateur peut lire 

        Précondition : 
        Exemple(s) :
        $$$ bloc1 = Bloc(Coordone(0, 0), Coordone(255, 255), Couleur(123,98,23), [])
        $$$ bloc1.haut_gauche
        Coordone(0, 0)
        $$$ repr(bloc1)
        'Bloc( Coordone(0, 0), Coordone(255, 255), Couleur(123, 98, 23), [])'
    
        """
        return f'Bloc( Coordone{self.haut_gauche}, Coordone{self.bas_droite}, Couleur{self.couleur}, {self.sous_blocs})'
        
        
    def __eq__(self, autre)->bool:
        """renvoie True si les deux Blocs sont les meme 

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        return (self.haut_gauche == autre.haut_gauche) and (self.bas_droite == autre.bas_droite) and (self.couleur == autre.couleur) and (self.sous_blocs == autre.sous_blocs)

    def sauvegarder(self, nom_du_fichier : str )->None:
        """La fonction sauvegarde le bloc dans un fichier csv qu'il crée

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        infos = [self.haut_gauche.largeur, self.haut_gauche.hauteur, self.bas_droite.largeur, self.bas_droite.hauteur, self.couleur.rouge , self.couleur.vert , self.couleur.bleu]
        with open(nom_du_fichier, mode='w', newline='') as doc_infos_blocs:
            writer = csv.writer(doc_infos_blocs)
            for info in infos:
                writer.writerow(info)
            writer.writerow([]) 
        