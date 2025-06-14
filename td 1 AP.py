PROMO = [{'nom': 'Calbuth', 'info': 12.5, 'maths': 15.8, 'physique': 8, 'chimie': 10},
{'nom': 'Talon', 'info': 9.5, 'maths': 11.7, 'chimie': 16, 'meca': 8},
{'nom': 'Cru', 'info': 17, 'maths': 7, 'meca': 14, 'physique': 11}]
def mo1(pr,ue):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    res = 0
    i = 0
    for et in pr:
        res = res + et[ue]
        i = i + 1
    return res / i

def mo2(pr,ue):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    res = 0
    i = 0
    for et in pr:
        if ue in et :
            res = res + et[ue]
            i = i + 1
    return res / i

def doub1(lis):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    rep = False
    for e in lis:
        if lis.count(e)> 2 :
            rep = True
    return rep
def doub2(lis):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    ens_liste = set(lis)
    return len(ens_liste) == len(lis)
    
def doub3(lis):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ liste = [ 3,1,4,1,5,9,2,6,5,3,5]
    $$$ doub3(liste)
    [3,1,5]

    """
    doub = []
    for e in lis :
        if lis.count(e) >= 2 and e not in doub:
            doub.append(e)
    return doub

def doub3_with_dict(lis):
    """Retourne les éléments qui apparaissent plus de deux fois dans la liste en utilisant un dictionnaire.

    Args:
        lis (list): La liste d'entrée.

    Returns:
        list: Liste des éléments qui apparaissent plus de deux fois.
    """
    counts = {}
    for e in lis:
        counts[e] = counts.get(e, 0) + 1

    doub = []
    for e, count in counts.items():
        if count >= 2:
            doub.append(e)

    return doub



def est_pair(n: int) -> bool:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    
    return n == 0 or not est_impair(n-1)

def est_impair(n: int) -> bool:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    return not (n == 0 or est_pair(n-1))
    
def est_pair1(n: int) -> bool:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ est_pair1(8)
    True
    $$$ est_pair1(9)
    False

    """
    
    if n == 0:
        res = True
    elif n == 1 :
        res = False
    else:
        res = est_pair1(n - 2)
    return res

def add(a,b):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ add(2,5)
    7
    $$$ add(4,9)
    13
    $$$ add(-4,9)
    5
    $$$ add(-4,-9)
    -13
    """
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return add(a-1, b+1)
        
def mult(a , b):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ mult(3,3)
    9
    $$$ mult(2,5)
    10
    $$$ mult(0,5)
    0

    """
    if a == 0:
        return 0
    else:
        return b + mult(a-1, b)
        
def pui(a ,n):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ pui(2,3)
    8
    $$$ pui(0,3)
    0

    """
    if n == 0:
        return 1
    else:
        return a * pui(a,n-1)
    
def nbch(n):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ nbch(6)
    1
    $$$ nbch(45)
    2
    $$$ nbch(4567)
    4
    $$$ nbch(45678799765)
    11
    """
    i = 0
    while n > 0 and n != 0:
        n = n // 10
        i = i +1
    return i

def est_divisible_par_trois(n):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ est_divisible_par_trois(590)
    False
    $$$ est_divisible_par_trois(56)
    False
    $$$ est_divisible_par_trois(198)
    True
    """
    res = False
    while n > 10 :
        n = sommes(n)
        est_divisible_par_trois(n) 
    if n == 3 or n == 6 or n == 9:
        res = True
    return res 
    
def sommes(n):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ sommes(35)
    8
    $$$ sommes(87)
    15
    $$$ sommes(369)
    18
    """
    i = 0
    somme = 0
    for i in str(n):
        somme = somme + int(i)
    return somme

def euclide( a:int, b:int )->int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ euclide(119, 544)
    17
    $$$ euclide(56, 118)
    2

    """
    if b == 0 :
        return a
    else:
        if a < b :
            a,b=b,a
        return euclide(b, a%b) 

def coefficient_binomial(n: int, k: int) -> int:
    """Calcul du coefficient binomial de n parmi k de manière récursive.

    Précondition : n et k sont des entiers positifs tels que k <= n.
    Exemple(s) :
    $$$ coefficient_binomial(5, 2)
    10
    $$$ coefficient_binomial(6, 3)
    20
    """
    if k == 0 or k == n:
        return 1
    else:
        return coefficient_binomial(n - 1, k - 1) + coefficient_binomial(n - 1, k)

def palin(mot):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ palin('sois')
    False
    $$$ palin('radar')
    True
    $$$ palin('elle')
    True
    """
    if len(mot) == 0:
        return True
    elif mot[0] == mot[-1]:
        return palin(mot[1:-1])
    else:
        return False
    
def nb_occ(chaine, car):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ nb_occ('abcdef','z')
    0
    $$$ nb_occ('abccdecfgc','c')
    4
    $$$ nb_occ('abaccadaecaafgca','a')
    7
    $$$ nb_occ('cc','c')
    2

    """
    if len(chaine)== 0 :
        return 0
    elif chaine[0] == car:
        return 1 + nb_occ(chaine[1:],car)
    else:
        return nb_occ(chaine[1:],car)
        
def indice (chaine , car):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ indice( 'abcdeg','b')
    1
    $$$ indice( 'abcdeg','d')
    3
    $$$ indice( 'abcdeddg','d')
    3
    $$$ indice( 'abcdeg','z')
    ValueError

    """
    if len(chaine) == 0:
        raise ValueError
    elif chaine[0] == car :
        return 0
    else :
        return 1 + indice(chaine[1:],car)
    
def indice2(s,c):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ indice2( 'abcdeg','b')
    1
    $$$ indice2( 'abcdeg','d')
    3
    $$$ indice2( 'abcdeddg','d')
    3
    """
    return s.index(c)
UNITS = {'mm': 0.001,'cm': 0.01,'dm': 0.1,'m': 1.0,'dam': 10,'hm': 100,'km': 1000}
class Distance:
    """
1 le module distance
    $$$ d1 = Distance(3, 'km')
    $$$ d1.value
    3
    $$$ d1.unit
    'km'
    $$$ d1.en_metre()
    3000
    $$$ d2 = Distance(1, 'm')
    $$$ d1 == d2
    False
    $$$ d1 == Distance(30, 'hm')
    True
    $$$ d1 <= d2
    False
    $$$ d2 <= d1
    True
    $$$ d1 + d2
    Distance(3001, 'm')
    $$$ d1 - d2
    Distance(2999, 'm')
    $$$ str(Distance(2, 'cm'))
    '2 (cm)'
    """
    def __init__(self,valeur, unite):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km')
        $$$ d1.value
        3
        $$$ d1.unit
        'km'
        """
        self.value = valeur
        self.unit = unite
        
    def en_metre(self):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km')
        $$$ d1.en_metre()
        3000
        """
        return self.value*UNITS[self.unit]
    
    def __eq__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km') 
        $$$ d2 = Distance(1, 'm')
        $$$ d1 == d2
        False
        $$$ d1 == Distance(30, 'hm')
        True
        """
        return self.en_metre() == autre.en_metre()

    def __le__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km')
        $$$ d2 = Distance(1, 'm')
        $$$ d1 <= d2
        False
        $$$ d2 <= d1
        True
        """
        return self.en_metre() <= autre.en_metre()

    def __add__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km')
        $$$ d2 = Distance(1, 'm')
        $$$ d1 + d2
        Distance(3001, 'm')
        """
        somme_metre = self.en_metre() + autre.en_metre()
        return Distance(somme_metre,'m')
    
    def __sub__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km')
        $$$ d2 = Distance(1, 'm')
        $$$ d1 - d2
        Distance(2999, 'm')
        """
        sub_metre = self.en_metre() - autre.en_metre()
        return Distance(sub_metre,'m')
    
    def __str__(self):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ d1 = Distance(3, 'km')
        $$$ str(Distance(2, 'cm'))
        '2 (cm)'
        """
        return f'{self.value} ({self.unit})'
import math 
class Fraction:
    """
    a class for rational numbers.
    $$$ f1 = Fraction(2, 3)
    $$$ f1.denominator
    3
    $$$ f1.numerator
    2
    $$$ f2 = Fraction(5, 7)
    $$$ f1 * f2 == Fraction(10, 21)
    True
    $$$ f1 + f2 == Fraction(29, 21)
    True
    $$$ f1 - f2 == Fraction(2, 21)
    False
    $$$ str(f1)
    '2/3'
    """
    def __init__(self,num,den):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ f1 = Fraction(2, 3)
        $$$ f1.denominator
        3
        $$$ f1.numerator
        2 

        """
        self.denominator = den
        self.numerator = num
        
    def __mul__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ f1 = Fraction(2, 3)
        $$$ f2 = Fraction(5, 7)
        $$$ f1 * f2 == Fraction(10, 21)
        True

        """
        return Fraction(self.numerator * autre.numerator , self.denominator * autre.denominator)
        

    def __eq__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ f1 = Fraction(2, 3)
        $$$ f2 = Fraction(5, 7)
        $$$ f1 * f2 == Fraction(10, 21)
        True
        $$$ f1 + f2 == Fraction(29, 21)
        True
        $$$ f1 - f2 == Fraction(2, 21)
        False
        """
        return self.numerator == autre.numerator and self.denominator == autre.denominator
    
    def __add__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ f1 = Fraction(2, 3)
        $$$ f2 = Fraction(5, 7)
        $$$ f1 + f2 == Fraction(29, 21)
        True
        """
        if self.denominator == autre.denominator :
            return Fraction(self.numerator + autre.numerateur , self.denominator)
        else:
            num = self.numerator * autre.denominator + self.denominator * autre.numerator
            den = self.denominator * autre.denominator  
            return Fraction(num,den)
    
    def __sub__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ f1 = Fraction(2, 3)
        $$$ f2 = Fraction(5, 7)
        $$$ f1 - f2 == Fraction(2, 21)
        False
        """
        if self.denominator == autre.denominator :
            return Fraction(self.numerator - autre.numerateur , self.denominator)
        else:
            num = self.numerator * autre.denominator - self.denominator * autre.numerator
            den = self.denominator * autre.denominator  
            return Fraction(num,den)
    def __str__(self):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ f1 = Fraction(2, 3)
        $$$ str(f1)
        '2/3'
        """
        return f'{self.numerator}/{self.denominator}'
import random
VALUES = ("Ace", "2", "3", "4", "5",  "6", "7", "8", "9", "10", "Jack", "Knight", "Queen", "King")
COLORS = ("spade", "heart", "diamond", "club")
class Card:
    """Paramètres :
    à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ c1 = Card('Ace', 'heart')
    $$$ c1.color
    'heart'
    $$$ c1.value
    'Ace'
    $$$ c2 = Card.random()
    $$$ c2.value, c2.color
    ('Jack', 'diamond')
    $$$ c2.compare(c1) > 0
    True
    $$$ c1.compare(c2) > 0
    False
    $$$ c1.compare(c1) == 0
    True
    $$$ c1 == c2
    False
    $$$ c1 != c2
    True
    $$$ c1 < c2
    True
    $$$ c1 > c2
    False

    """
    def __init__(self,valeur,couleur):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c1.color
        'heart'
        $$$ c1.value
        'Ace' 

        """
        self.color = couleur
        self.value = valeur
        
    def __repr__(self):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card("Ace", "heart")
        $$$ print(c1)
        Card("Ace", "heart")

        """
        return f'Card("{self.value}","{self.color}")'
        
        
    
    @classmethod
    def random(cls):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        
    

        """
        val = random.choice(VALUES)
        col = random.choice(COLORS)
        cls(val,col)
        
    def compare(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('Jack', 'diamond')
        $$$ c2.compare(c1) > 0
        True
        $$$ c1.compare(c2) > 0
        False
        $$$ c1.compare(c1) == 0
        True

        """
        if self.value == autre.value and self.color == autre.color:
            return 0
        elif VALUES.index(self.value) < VALUES.index(autre.value):
            return -1
        else:
            return 1
        
    def __eq__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('Jack', 'diamond')
        $$$ c1 == c2
        False
   

        """
        return self.compare(autre) == 0

    def __ne__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('Jack', 'diamond')
        $$$ c1 != c2
        True 

        """
        return self.compare(autre) != 0
    
    def __lt__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('Jack', 'diamond')
        $$$ c1 < c2
        True

        """
        return self.compare(autre) == -1
    
    def __gt__(self,autre):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('Jack', 'diamond')
        $$$ c1 > c2
        False

        """
        return self.compare(autre) == 1
        
    def deck():
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ 

        """
        deck = []
        for valeur in VALUES :
            for color in COLORS:
                c = Card(valeur,color)
                deck.append(c)
        return deck

def compare(a,b):
        """à_remplacer_par_ce_que_fait_la_fonction

        Précondition : 
        Exemple(s) :
        $$$ c1 = Card('Ace', 'heart')
        $$$ c2 = Card('Jack', 'diamond')
        $$$ c2.compare(c1) > 0
        True
        $$$ c1.compare(c2) > 0
        False
        $$$ c1.compare(c1) == 0
        True

        """
        if a == b :
            return 0
        elif a < b:
            return -1
        else:
            return 1
        
from typing import List, Any, Callable
  
def recherche_indice(liste: List[Any], element: Any, compare: Callable[[Any, Any], int]) -> int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    
    i = 0
    for elem in liste:
        if compare(elem, element) == 0:
            return i
        i = i + 1
    return -1

def recherche_indice2(liste: List[Any], element: Any, compare: Callable[[Any, Any], int]) -> int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ gh = [6,9,8,7,4,3,8,2]
    $$$ recherche_indice2(gh, 3, compare)
    5
    $$$ recherche_indice2(gh, 1, compare)
    8
    

    """
    
    i = 0
    while i<len(liste) and element != liste[i]:
        i = i+1
    return i

        
def recherche_indice_trie(liste: List[Any], element: Any, compare: Callable[[Any, Any], int]) -> int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ gh = [1,3,5,6,8]
    $$$ recherche_indice_trie(gh, 5, compare)
    2
    $$$ recherche_indice_trie(gh, 1, compare)
    0
    $$$ recherche_indice_trie(gh, 2, compare)
    False
    
    

    """
    i = 0
    while element != liste[i] and element > liste[i]:
        i = i+1
    if element != liste[i]:
        return False
    else:
        return i

    
def recherche_indice_plus_grand(liste: List[Any], element: Any, compare: Callable[[Any, Any], int]) -> int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ gh = [6,9,8,7,4,3,8,2,3,1,1,9]
    $$$ recherche_indice_plus_grand(gh, 3, compare)
    8
    $$$ recherche_indice_plus_grand(gh, 1, compare)
    10
    $$$ recherche_indice_plus_grand(gh, 5, compare)
    -1
    

    """
    
    i = len(liste)-1
    while i > -1 and element != liste[i]:
        i = i-1
    return i

def recherche_indice2_plus_grand(liste: List[Any], element: Any, compare: Callable[[Any, Any], int]) -> int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ gh = [6,9,8,7,4,3,8,2,3,1,1,9]
    $$$ recherche_indice2_plus_grand(gh, 3, compare)
    8
    $$$ recherche_indice2_plus_grand(gh, 1, compare)
    10
    $$$ recherche_indice2_plus_grand(gh, 5, compare)
    -1
    
    

    """
    liste = liste[::-1]
    i = 0
    while i<len(liste) and element != liste[i]:
        i = i+1
    return  (len(liste)-1) - i

        
def recherche_indice_trie_plus_grand(liste: List[Any], element: Any, compare: Callable[[Any, Any], int]) -> int:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ gh = [1,1,3,5,5,5,6,8,9]
    $$$ recherche_indice_trie_plus_grand(gh, 5, compare)
    5
    $$$ recherche_indice_trie_plus_grand(gh, 1, compare)
    1
    $$$ recherche_indice_trie_plus_grand(gh, 2, compare)
    False
    
    

    """
    liste = liste[::-1]
    i = 0
    while compare(element, liste[i]) !=0 and element < liste[i]:
        i = i+1
    if compare(element, liste[i]) !=0:
        return False
    else:
        return len(liste)-1-i


def recherche_laborieuse(li: list[int], a: int,b: int ,x: int) -> bool:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ recherche_laborieuse([3, 1, 2, 4, 5], 0, 5, 1)
    True
    $$$ recherche_laborieuse([3, 1, 2, 4, 1], 0, 5, 1)
    True
    $$$ recherche_laborieuse([3, 1, 2, 4, 5], 0, 5, 6)
    False
    """
    trouve = False
    for i in range(a,b):
        if li[i]==x:
            trouve=True
    return trouve


def recherche_laborieuse_erronee_plus_rapide(li: list[int], a: int,b: int ,x: int) -> bool:
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ recherche_laborieuse_erronee_plus_rapide([3, 1, 2, 4, 5], 0, 5, 1)
    False
    $$$ recherche_laborieuse_erronee_plus_rapide([3, 1, 2, 4, 1], 0, 5, 1)
    True
    $$$ recherche_laborieuse_erronee_plus_rapide([3, 1, 2, 4, 5], 0, 5, 6)
    False
    """
    trouve = False
    i = len(li)-1
    if li[i] ==x:
        return not trouve
    return trouve

def recherche_dicho(elt: Any, liste: list[Any],a:int = 0, b: int = None,comp: Callable[[Any, Any], int]=compare) -> bool:
    """
    precondition: liste est triée selon `comp`
    """
    m = -1
    if b is None:
        b = len(liste)
    d = a
    f = b - 1
    while  d < f and m != elt:
        m = (d + f) // 2
        if comp(elt, liste[m]) == 1:
            d = m + 1
        else:
            f = m
    return (a < b) and comp(elt, liste[d]) == 0

def recherche_dicho_indice(elt: Any, liste: list[Any],a:int = 0, b: int = None,comp: Callable[[Any, Any], int]=compare) -> bool:
    """
    precondition: liste est triée selon `comp`
    """
    m = -1
    if b is None:
        b = len(liste)
    d = a
    f = b - 1
    while  d < f and m != elt:
        m = (d + f) // 2
        if comp(elt, liste[m]) == 1:
            d = m + 1
        else:
            f = m
    if (a < b) and comp(elt, liste[d]) == 0:
        return d
    else:
        return -1
    
def recherche_indice(l:list,a:int,b:int,x:int):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : a < b
    Exemple(s) :
    $$$ recherche_indice([4,6,7,7,7,8,9,7],0,8,7)
    {2, 3, 4, 7}
    $$$ recherche_indice([4,6,7,8],0,3,7)
    {2}
    $$$ recherche_indice([4,6,7,8,7],0,2,7)
    set()
    
    """
    ens = set()
    for i in range(a,b):
        if l[i] == x:
            ens.add(i)
    return ens
    
def reche_indice_sequ_trie(l:list,a:int,b:int,x:int):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : a < b
    Exemple(s) :
    $$$ reche_indice_sequ_trie([4,6,7,7,7,8,9],0,8,7)
    {2, 3, 4}
    $$$ reche_indice_sequ_trie([4,6,7,8],0,3,7)
    {2}
    $$$ reche_indice_sequ_trie([4,6,7,8],0,2,7)
    set()

    """
    ens = set()
    i = a
    while l[i] != x and i < b:
        i = i + 1
    if i < b :
        while i < b and l[i] == x:
            ens.add(i)
            i = i + 1
    return ens 
     
     
def reche_indice_dicho_trie(l:list,a:int,b:int,x:int):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : a < b
    Exemple(s) :
    $$$ reche_indice_dicho_trie([4,6,7,7,7,8,9],0,8,7)
    {2, 3, 4}
    $$$ reche_indice_dicho_trie([4,6,7,8],0,3,7)
    {2}
    $$$ reche_indice_dicho_trie([4,6,7,8],0,2,7)
    set()

    """
    milieu = -1
    ens = set()
    i = a
    while  i < b :
        milieu = (i + b) // 2
        if l[milieu] > x :
            b = milieu
        elif l[milieu] < x :
            i = milieu + 1
        else:
            ens.add(milieu)
            i = i+1
            while i < len(l) and l[i] == x:
                ens.add(i)
                i = i+1
    return ens
    
        
def est_trie(l,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ est_trie([3,1,4,1,5,9,2], compare)
    False
    $$$ est_trie([1,1,2,3,4,5,9], compare)
    True
    $$$ est_trie([1,2,3,4,5,9], compare)
    True

    """
    i=0
    trouve = True
    while trouve and i < len(l)-2:
        if compare(l[i],l[i+1]) == 1:
            trouve = False
        else:
            i = i+1
    return trouve

def est_trie2(l,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ est_trie2([3,1,4,1,5,9,2], compare)
    False
    $$$ est_trie2([1,1,2,3,4,5,9], compare)
    True
    $$$ est_trie2([1,2,3,4,5,9], compare)
    True

    """
    i = 0
    l1 = sorted(l)
    while  i < len(l) and l[i] == l1[i]:
        i = i+1
    return i == len(l)

def compare_car(c1,c2):
    """PAS FINI 

    Précondition : 
    Exemple(s) :
    $$$ 
    $$$ compare_car('a', 'A')
    -1
    $$$ compare_car('A','b')
    -1
    $$$ compare_car('@', 'Z')
    1
    $$$ compare_car('9', '@')
    -1
    $$$ compare_car('@', '@')
    0
    """
    l1 = [c1, c2]
    ls = sorted(l1)
    if c1 == c2:
        return 0
    else:
        if isinstance(c1,int)and isinstance(c2,str):
            return -1
        elif isinstance(c1,int) and isinstance(c2,int):
            if l1 == ls:
                return 1
            else:
                return -1   
        elif isinstance(c1,str) and isinstance(c2,int):
            return 1
        else:
            return 0
                    
def lis_doub(l):
    """PAS FINI 

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    l1= sorted(l)
    for i in l1 :
        return i

def tri_sel_max(l):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ tri_sel_max([5,2,3,1,4,6])
    [1,2,3,4,5,6]
    """
    res = 0
    for a in range (0,len(l)):
        res = a
        for i in range(a+1,len(l)):
            if l[a] > l[i]:
                res = i
                l[a],l[res] = l[res],l[a]
    return l
            
def selec_max(l,a,b,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    res = a
    for i in range(a+1,b):
        if compare(l[i], l[res]) ==1:
            res = i
    return res

def tri_selec(l,a,b,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ tri_selec([5,2,3,1,4,6],0,6,compare)
    [1,2,3,4,5,6]

    """
    for f in range(b-1,a,-1):
        i = selec_max(l,a,f+1,compare)
        l[i], l[f] = l[f], l[i]
    return l
            
def tri_par_insertion(l,a,b,compare):
    """trie le tableau T dans l'ordre croissant

    Précondition : 
    Exemple(s) :
    $$$ tri_par_insertion([5,2,3,1,4,6],0,6,compare)
    [1,2,3,4,5,6]
    $$$ tri_par_insertion([5,2,3,1,4,8,10,6],0,8,compare)
    [1,2,3,4,5,6,8,10]
    $$$ tri_par_insertion([5,8,2,9,3,1,4,7,6],0,9,compare)
    [1,2,3,4,5,6,7,8,9]

    """
    for i in range(a+1,b):
        x = l[i]
        j=i
        while compare(j,a) == 1 and compare(x,l[j-1])==-1:
            l[j],l[j-1] = l[j-1],l[j]
            j=j-1
        l[j] = x
    return l

def renverser_sommet(l,n):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ l = [3, 1, 4, 5, 6, 2]
    $$$ renverser_sommet (l,5)
    $$$ l
    [6, 5, 4, 1, 3, 2]
    $$$ renverser_sommet (l,6)
    $$$ l
    [2, 3, 1, 4, 5, 6]
    $$$ renverser_sommet (l,3)
    $$$ l
    [1, 2, 3, 4, 5, 6]

    """
    l[:n] = l[n-1::-1]

    
def selec_max(l,f,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ selec_max([3, 1, 4, 5, 6, 2],5, compare)
    4
    $$$ selec_max([2, 3, 1, 4, 5, 6],4, compare)
    4
    $$$ selec_max([2, 3, 1, 4, 5, 6],2, compare)
    1

    """
    imax = 0
    for i in range(1,f+1):
        if compare(l[i],l[imax])==1:
            imax = i
    return imax

def tri_crepes(l,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ tri_crepes([3, 1, 4, 5, 6, 2],compare)
    [1, 2, 3, 4, 5, 6]
    $$$ tri_crepes([2, 1, 4, 5, 6, 7, 3],compare)
    [1, 2, 3, 4, 5, 6, 7]
    $$$ tri_crepes([2, 3, 1, 6, 9, 4, 5, 8, 7],compare)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
    n = len(l)
    crepe = 0
    for crepe in range(n):
        k = selec_max(l, n,compare)
        l = renverser_sommet(l,k+1)
    return l
        
       
       
def rev(l,k):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    for i in range((n+1)//2):
        l[i],l[n-1] = l[n-1],l[i]
        
def max(l,f,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 

    """
    imax = 0
    for i in range(1,f+1):
        if compare(l[i],l[imax])==1:
            imax = i
    return imax

def tri(l,compare):
    """à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ tri_crepes([3, 1, 4, 5, 6, 2],compare)
    [1, 2, 3, 4, 5, 6]
    $$$ tri_crepes([2, 1, 4, 5, 6, 7, 3],compare)
    [1, 2, 3, 4, 5, 6, 7]
    $$$ tri_crepes([2, 3, 1, 6, 9, 4, 5, 8, 7],compare)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    """
    n=len(l)
    k=0
    for crepe in range(ln(l)-1,O,-1):
        imax = max(l,f,compare)
        rev(l,imax)
    return l
    
# st = ApStack()
# st.push(1)
# st.push(7)
# st.push(5)
# print("f{st.pop()}")
# print("f{st.pop()}")
# print("f{st.pop()}")
# st.is_empty()