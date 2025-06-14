#TERMINER
#si je defini dans bloc is uniform ou non et que je fait dessiner seulement les blocs uniform ca renverrai ce qu il faut 
from Bloc import Bloc
from Couleur import Couleur
from Coordone import *
from PIL import Image, ImageDraw
import csv
import sys


def moyenne_couleur(liste_couleurs:list['Couleur'])->Couleur | None:
    """Prend une liste de Couleurs  en paramètre et renvoie une couleur moyenne de toutes les couleurs prisent en paramètre

    Précondition : aucune
    Exemple(s):
    $$$ liste_couleurss = [ Couleur(120,12,13), Couleur(0,0,255), Couleur(121,248,248)]
    $$$ moyenne_couleur(liste_couleurss)
    Couleur(80,86,172)
    $$$ res = moyenne_couleur(liste_couleurss)
    $$$ type(res) == Couleur
    True

    """
    rouge = 0
    vert = 0
    bleu = 0
    longueur_liste = len(liste_couleurs)
    if longueur_liste != 0:
        for couleur in liste_couleurs:
            rouge += couleur.rouge
            vert += couleur.vert
            bleu += couleur.bleu
        resultat = Couleur(rouge // longueur_liste, vert // longueur_liste, bleu // longueur_liste)        
        return resultat
    else:
        return None


def moyenne_couleur_rectangle(image: Image, haut_gauche : Coordone, bas_droite : Coordone) -> Couleur:
    """renvoie (en Couleur) la moyenne des couleurs de tout un rectangle (partie d'une image)

    Précondition : aucune
    Exemple(s) :
    $$$ from PIL import Image
    $$$ im = Image.open('assets/calbuth.png')
    $$$ im_rgb = im.convert('RGB')
    $$$ moyenne_couleur_rectangle(im_rgb, Coordone(0,0), Coordone(10,10))
    Couleur(236, 210, 111)
    $$$ moyenne_couleur_rectangle(im_rgb, Coordone(0,0), Coordone(100,100))
    Couleur(190, 170, 101)
    """
    liste_couleurs_rectangle =  []
    for x in range (haut_gauche.hauteur, bas_droite.hauteur):
        for y in range (haut_gauche.largeur, bas_droite.largeur):
            liste_couleurs_rectangle.append(Coordone(y, x).couleur(image))
    resultat = moyenne_couleur(liste_couleurs_rectangle)
    return resultat
    
def diviser_image_en_4_Blocs2(image: Image, liste_de_bloc: list['Bloc']) -> list['Bloc']:
    """Divise une image en 4 blocs et renvoie les quatres objets (Bloc) avec leur couleur qui équivaut à la moyenne des couleurs

    Précondition :  LA FONCTION FONCTIONNE TRES BIEN MAIS ERREUR DU TEST ALORS QU'A L'UTILISATION DE LA FONCTION DANS LE SHELL TT FONCTIONNE  
    Exemple(s) :
    $$$ from PIL import Image
    $$$ im = Image.open('assets/calbuth.png')
    $$$ im_rgb = im.convert('RGB')
    $$$ bloc1 = [Bloc( Coordone(0, 0), Coordone(128,128), Couleur(0,0,255), [] ), Bloc( Coordone(128, 0), Coordone(255, 128), Couleur(0,248,248), [] ), Bloc( Coordone(0, 128), Coordone(128, 255) , Couleur(248,248,248), [] ), Bloc( Coordone(128, 128), Coordone(255, 255), Couleur(116,248,248), [] )] 
    $$$ diviser_image_en_4_Blocs2(im_rgb, bloc1)
    [Bloc( Coordone(0, 0), Coordone(64, 64), Couleur(208, 185, 99), []), Bloc( Coordone(64, 0), Coordone(128, 64), Couleur(186, 168, 107), []), Bloc( Coordone(0, 64), Coordone(64, 128), Couleur(163, 144, 90), []), Bloc( Coordone(64, 64), Coordone(128, 128), Couleur(111, 96, 78), []), Bloc( Coordone(128, 0), Coordone(191, 64), Couleur(170, 148, 96), []), Bloc( Coordone(191, 0), Coordone(255, 64), Couleur(234, 208, 110), []), Bloc( Coordone(128, 64), Coordone(191, 128), Couleur(119, 101, 85), []), Bloc( Coordone(191, 64), Coordone(255, 128), Couleur(191, 169, 93), []), Bloc( Coordone(0, 128), Coordone(64, 191), Couleur(85, 69, 51), []), Bloc( Coordone(64, 128), Coordone(128, 191), Couleur(141, 107, 89), []), Bloc( Coordone(0, 191), Coordone(64, 255), Couleur(36, 0, 0), []), Bloc( Coordone(64, 191), Coordone(128, 255), Couleur(88, 76, 62), []), Bloc( Coordone(128, 128), Coordone(191, 191), Couleur(122, 86, 74), []), Bloc( Coordone(191, 128), Coordone(255, 191), Couleur(183, 158, 84), []), Bloc( Coordone(128, 191), Coordone(191, 255), Couleur(62, 50, 45), []), Bloc( Coordone(191, 191), Coordone(255, 255), Couleur(145, 28, 16), [])]
    """
    
    nouveaux_blocs = []
    for bloc in liste_de_bloc:
        point_plus_haut_gauche = bloc.haut_gauche
        point_plus_bas_droit = bloc.bas_droite

        milieu = Coordone((point_plus_bas_droit.largeur + point_plus_haut_gauche.largeur) // 2,
                          (point_plus_bas_droit.hauteur + point_plus_haut_gauche.hauteur) // 2)

        moyenne_couleur_sous_bloc_1 = moyenne_couleur_rectangle(image, point_plus_haut_gauche, milieu)
        moyenne_couleur_sous_bloc_2 = moyenne_couleur_rectangle(image, Coordone(milieu.largeur, point_plus_haut_gauche.hauteur),Coordone(point_plus_bas_droit.largeur, milieu.hauteur))
        moyenne_couleur_sous_bloc_3 = moyenne_couleur_rectangle(image, Coordone(point_plus_haut_gauche.largeur, milieu.hauteur), Coordone(milieu.largeur, point_plus_bas_droit.hauteur))
        moyenne_couleur_sous_bloc_4 = moyenne_couleur_rectangle(image, milieu, point_plus_bas_droit)

        sous_bloc1 = Bloc(point_plus_haut_gauche, milieu, moyenne_couleur_sous_bloc_1, [])
        sous_bloc2 = Bloc(Coordone(milieu.largeur, point_plus_haut_gauche.hauteur),Coordone(point_plus_bas_droit.largeur, milieu.hauteur), moyenne_couleur_sous_bloc_2, [])
        sous_bloc3 = Bloc(Coordone(point_plus_haut_gauche.largeur, milieu.hauteur),Coordone(milieu.largeur, point_plus_bas_droit.hauteur), moyenne_couleur_sous_bloc_3, [])
        sous_bloc4 = Bloc(milieu, point_plus_bas_droit, moyenne_couleur_sous_bloc_4, [])

        nouveaux_blocs.append(sous_bloc1)
        nouveaux_blocs.append(sous_bloc2)
        nouveaux_blocs.append(sous_bloc3)
        nouveaux_blocs.append(sous_bloc4)
    dessiner_bloc_sur_image2(image,nouveaux_blocs)
    for sousb in nouveaux_blocs :
        sousb.sauvegarder('infos_image.txt')
    
    return nouveaux_blocs

def diviser_image_en_4_Blocs(image: Image, bloc : Bloc)->list['Bloc']:
    """Divise une image en 4 blocs et renvoie les quatres objets (Bloc) avec leur couleur qui équivaut à la moyenne des couleurs

    Précondition :  
    Exemple(s) :
    $$$ from PIL import Image
    $$$ im = Image.open('assets/calbuth.png')
    $$$ im_rgb = im.convert('RGB')
    $$$ bloc1 = Bloc( Coordone(0, 0), Coordone(255, 255), None , [Bloc( Coordone(0, 0), Coordone(128,128), Couleur(0,0,255), [] ), Bloc( Coordone(128, 0), Coordone(255, 128), Couleur(0,248,248), [] ), Bloc( Coordone(0, 128), Coordone(128, 255) , Couleur(248,248,248), [] ), Bloc( Coordone(128, 128), Coordone(255, 255), Couleur(116,248,248), [] )] )
    $$$ diviser_image_en_4_Blocs(im_rgb, bloc1)
    [Bloc( Coordone(0, 0), Coordone(127, 127), Couleur(168, 149, 93), []), Bloc( Coordone(127, 0), Coordone(255, 127), Couleur(179, 157, 96), []), Bloc( Coordone(0, 127), Coordone(127, 255), Couleur(87, 63, 50), []), Bloc( Coordone(127, 127), Coordone(255, 255), Couleur(128, 81, 55), [])]    

    """
    
    if bloc is None:
        return []
    point_plus_haut_gauche = bloc.haut_gauche
    point_plus_bas_droit = bloc.bas_droite
    
    milieu = Coordone( (point_plus_bas_droit.largeur + point_plus_haut_gauche.largeur) //2, (point_plus_bas_droit.hauteur + point_plus_haut_gauche.hauteur) //2 )
    
    moyenne_couleur_sous_bloc_1 = moyenne_couleur_rectangle(image, point_plus_haut_gauche, milieu)
    moyenne_couleur_sous_bloc_2 = moyenne_couleur_rectangle(image, Coordone(milieu.largeur, point_plus_haut_gauche.hauteur), Coordone(point_plus_bas_droit.largeur, milieu.hauteur))
    moyenne_couleur_sous_bloc_3 = moyenne_couleur_rectangle(image, Coordone(point_plus_haut_gauche.largeur, milieu.hauteur), Coordone(milieu.largeur, point_plus_bas_droit.hauteur))
    moyenne_couleur_sous_bloc_4 = moyenne_couleur_rectangle(image, milieu, point_plus_bas_droit )
    
    sous_bloc1 = Bloc( point_plus_haut_gauche, milieu, moyenne_couleur_sous_bloc_1, [])
    sous_bloc2 = Bloc( Coordone(milieu.largeur, point_plus_haut_gauche.hauteur), Coordone(point_plus_bas_droit.largeur, milieu.hauteur), moyenne_couleur_sous_bloc_2, [])
    sous_bloc3 = Bloc( Coordone(point_plus_haut_gauche.largeur, milieu.hauteur), Coordone(milieu.largeur, point_plus_bas_droit.hauteur), moyenne_couleur_sous_bloc_3, [])
    sous_bloc4 = Bloc( milieu, point_plus_bas_droit, moyenne_couleur_sous_bloc_4,[] )
    
    nouveaux_blocs = [sous_bloc1, sous_bloc2, sous_bloc3, sous_bloc4]
    return nouveaux_blocs



def distance_couleur ( coul1:Couleur, coul2:Couleur)-> tuple[int, int, int]:
    """renvoie la distance entre deux Couleurs sous forme de tuple   

    Précondition : aucune
    Exemple(s) :
    $$$ distance_couleur ( Couleur(120, 13, 2), Couleur(121,72, 3))
    (1, 59, 1)
    $$$ distance_couleur ( Couleur(120, 73, 2), Couleur(121,72, 3))
    (1, 1, 1)
    $$$ distance_couleur ( Couleur(120, 74, 4), Couleur(121,72, 3))
    (1, 2, 1)

    """
    rouge = abs(coul1.rouge - coul2.rouge)
    vert = abs(coul1.vert - coul2.vert)
    bleu = abs(coul1.bleu - coul2.bleu)
    return rouge, vert, bleu
        
def couleur_proche(coul1:Couleur, coul2:Couleur, seuil:int)->bool:
    """renvoie True si les deux Couleurs sont proches selon un seuil et False sinon

    Précondition : aucune
    Exemple(s) :
    $$$ couleur_proche( Couleur(120, 13, 2), Couleur(121,72, 3), 5)
    False
    $$$ couleur_proche( Couleur(120, 73, 2), Couleur(121,72, 3), 5)
    True
    $$$ couleur_proche( Couleur(120, 74, 4), Couleur(121,72, 3), 5)
    True
    $$$ couleur_proche( Couleur(120, 74, 4), Couleur(125,72, 15), 10)
    False
    """
    rouge ,vert, bleu = distance_couleur (coul1, coul2)
    return rouge <= seuil and vert <= seuil and bleu <= seuil
    


def dessiner_bloc_sur_image(image: Image, bloc: Bloc)->None:
    """La fonction dessine sur l'image le bloc de couleur la moyenne des couleurs presentent dans la partie du bloc 

    Précondition : aucune
    Exemple(s) :
    $$$ 

    """
    dessin = ImageDraw.Draw(image)
    dessin.rectangle( (bloc.haut_gauche.Coord_to_tuple(), bloc.bas_droite.Coord_to_tuple()), fill = bloc.couleur.Couleur_to_tupl())

def dessiner_bloc_sur_image2(image: Image, liste_bloc: list['Bloc'])->None:
    """La fonction dessine sur l'image le bloc de couleur la moyenne des couleurs presentent dans la partie du bloc 

    Précondition : aucune
    Exemple(s) :
    $$$ 

    """
    
    for bloc in liste_bloc:
        dessin = ImageDraw.Draw(image)
        dessin.rectangle( (bloc.haut_gauche.Coord_to_tuple(), bloc.bas_droite.Coord_to_tuple()), fill = bloc.couleur.Couleur_to_tupl())
        

def fonction_principale(image: Image, ordre: int , haut_gauche: Coordone, bas_droite: Coordone)->None:
    """Fonction principale du projet 

    Précondition : aucune
    Exemple(s) :
    $$$ 

    """
    liste_bloc_affiche = []
    if ordre > 0:
        #Divise I en quatre images (les blocs) de même taille
        blocs = diviser_image_en_4_Blocs(image, Bloc( haut_gauche, bas_droite, moyenne_couleur_rectangle(image, haut_gauche, bas_droite), [] ))
        #applique l'algorithme sur chaque blocs en diminuant l'ordre de 1.
        for bloc in blocs:
            bloc = fonction_principale(image, ordre - 1, bloc.haut_gauche, bloc.bas_droite )
            #si les quatre blocs sont de couleurs proches, alors
            if couleur_proche(blocs[0].couleur, blocs[1].couleur, 10) and couleur_proche(blocs[0].couleur, blocs[2].couleur, 10) and couleur_proche(blocs[0].couleur, blocs[3].couleur, 10) and couleur_proche(blocs[1].couleur, blocs[2].couleur, 10) and couleur_proche(blocs[1].couleur, blocs[3].couleur, 10) and couleur_proche(blocs[2].couleur, blocs[3].couleur, 10):
                #crée et renvoie un bloc uniforme de couleur la moyenne des quatre couleurs et de dimensions celles de l'image
                couleur_bloc_uniform = moyenne_couleur_rectangle(image,blocs[0].haut_gauche , blocs[3].bas_droite )
                bloc_uniform = Bloc( blocs[0].haut_gauche, blocs[3].bas_droite, couleur_bloc_uniform, [])
                liste_bloc_affiche.append(bloc_uniform)
                
            #sinon   
            else:
                #crée et renvoie un bloc contenant les quatre blocs
                 blocs_non_uniform = diviser_image_en_4_Blocs2(image, liste_bloc_affiche)
                 for bloc_non_uniform in blocs_non_uniform:
                     liste_bloc_affiche.append(bloc_non_uniform)
    #sinon                  
    else:
        #crée et renvoie un bloc de la couleur moyenne de l'image
        couleur_bloc_final = moyenne_couleur_rectangle(image, haut_gauche, bas_droite)
        bloc_finale = Bloc( haut_gauche, bas_droite, couleur_bloc_final, [])
        liste_bloc_affiche.append(bloc_finale)
        dessiner_bloc_sur_image2(image, liste_bloc_affiche)
    return liste_bloc_affiche
     
def main():
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    
    if len(sys.argv) < 3:
        print("Usage: python script.py chemin_vers_image ordre ")
        sys.exit(1)

    chemin_vers_image = sys.argv[1]
    ordre = sys.argv[2]
    image = Image.open(chemin_vers_image)
    image = image.convert('RGB')    
    fonction_principale(image, int(ordre), Coordone(0,0), Coordone(image.size[0] - 1, image.size[1] - 1))
    image.show()
   

if __name__ == "__main__":
    main()
    
# if __name__ == '__main__':
#     # éxécuté qd ce module n'est pas initialisé par un import.
#     main()
#     chemin_vers_image =  input("Chemain relatif vers l'image( sans guillemets, sans parenthèses : ")
#     image = Image.open(chemin_vers_image)
#     image = image.convert('RGB')
#     ordre = int(input("Entrer l'ordre : "))
#     fonction_principale(image, ordre, Coordone(0,0), Coordone(image.size[0] - 1, image.size[1] - 1))
#     image.show()