# game_of_life

# introduction
Le jeu de la Vie est un « jeu à zéro joueur », puisqu'il ne nécessite aucune intervention du joueur lors de son déroulement. Il s’agit d’un automate cellulaire, un modèle où chaque état conduit mécaniquement à l’état suivant à partir de règles préétablies.

Le jeu se déroule sur une grille à deux dimensions, théoriquement infinie, dont les cases — appelées « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ».

Une cellule possède huit voisines, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque itération, l'état d’une cellule est entièrement déterminé par l’état de ses huit cellules voisines, selon les règles suivantes : 
    - Une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît) ;
    - Si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à l’étape suivante ;
    - Si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante ;
    - Une cellule vivante ne possédant pas exactement deux ou trois cellules voisines vivantes meurt.
    
# prototype
class Cell
class Grid
 