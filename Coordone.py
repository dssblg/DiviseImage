#TERMINER
from Couleur import Couleur
from PIL import Image

class Coordone:
    """Paramètres :
    La class Coordone est crée pour manipuler plus facilement les coordonées des blocs une coordonée correspondra à un point de l'image
        elle permet de donner les coordonées de chaque pixel d'une image et peut nous donner  sa couleur de ce pixel

    Précondition : 
    Exemple(s) :
    $$$

    """
    def __init__(self,largeur_x:int, hauteur_y:int):
        """init de la class Coordone

        Précondition : 
        Exemple(s) :
        $$$ cor1 = Coordone(23, 34)
        $$$ cor1.hauteur
        34
        $$$ cor1.largeur
        23
        $$$ type(cor1) == Coordone
        True

        """
        self.largeur = largeur_x
        self.hauteur = hauteur_y
        
    def __repr__(self)->str:
        """renvoie une représentation de l'objet sous forme de chaine de caractère que l'utilisateur peut lire 

        Précondition : 
        Exemple(s) :
        $$$ cor1 = Coordone(23, 34)
        $$$ repr(cor1)
        'Coordone(23, 34)'
        
        """
        return f'Coordone({self.largeur}, {self.hauteur})'
    
    def __str__(self)->str:
        """renvoie une représentation de l'objet sous forme de chaine de caractère que la machine peut lire 
            aucunement besoin
        Précondition : 
        Exemple(s) :
        $$$ cor1 = Coordone(23, 34)
        $$$ str(cor1)
        "(23, 34)"
        
        """
        return f"({self.largeur}, {self.hauteur})"

    def Coord_to_tuple(self)->tuple:
        """la fonction transforme l'élément de Coordone en tuple

        Précondition : 
        Exemple(s) :
        $$$ cor1 = Coordone(23, 34)
        $$$ cor1.Coord_to_tuple()
        (23, 34)

        """
        return (self.largeur, self.hauteur)
    

    
    def __eq__(self, autre)->bool:
        """retourne True si les deux objets de la class Coordone sont égaux (de meme Coordonées) 

        Précondition : 
        Exemple(s) :
        $$$ cor1 = Coordone(23, 34)
        $$$ cor2 = Coordone(52, 34)
        $$$ cor1 == cor2
        False
        $$$ cor3 = Coordone(23, 34)
        $$$ cor1 == cor3
        True

        """
        if not isinstance(autre, Coordone):
            return False
        return self.largeur == autre.largeur and self.hauteur == autre.hauteur
    
    def couleur(self, image: Image)-> Couleur:
        """La fonction donne la couleur du pixel avec ses coordonées passée en paramètre

        Précondition : 
        Exemple(s) :
        $$$ from PIL import Image
        $$$ im = Image.open('assets/calbuth.png')
        $$$ im_rgb = im.convert('RGB')
        $$$ Coordone(0,0).couleur()
        Couleur(236, 210, 111)
        $$$ Coordone(100,100).couleur()
        Couleur(0, 0, 0)
        """
        tuple_image = self.Coord_to_tuple()
        rouge, vert, bleu  = image.getpixel(tuple_image)
        return Couleur(rouge, vert, bleu)
        
def tuple_to_coord(tupl: tuple)-> Coordone:
    """la fonction transforme l'élément de Coordone en tuple

    Précondition : 
    Exemple(s) :
    $$$ tu1 = (12, 23)
    $$$ tuple_to_coord(tu1)
    Coordone(12 ,23)
    $$$ reponse = tuple_to_coord(tu1)
    $$$ type(reponse) == Coordone
    True
    $$$ reponse.largeur
    12

    """
    
    cor1 = Coordone(tupl[0], tupl[1])
    return cor1


        