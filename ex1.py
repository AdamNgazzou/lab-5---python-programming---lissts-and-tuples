# Exercice 1 : Manipulation de Listes

# 1. Demander le nombre d'étudiants à inscrire
# n = ...
n = int(input("Combien d'étudiants voulez-vous inscrire ? "))
# 2. Créer une liste vide pour stocker les noms
# etudiants = []
etudiants = []

# 3. Boucle pour saisir les noms des étudiants
# for i in range(...):
    # nom = input(...)
    # ...
for i in range(n):
    nom = input(f"Entrez le nom de l'étudiant {i + 1} : ")
    etudiants.append(nom)

# 4. Afficher la liste des étudiants
for i in range(n):
    print(f"Étudiant {i + 1} : {etudiants[i]}")
# 5. Afficher la liste triée
etudiants.sort()
for i in range(n):
    print(f"Étudiant {i + 1} (trié) : {etudiants[i]}")
# 6. Afficher le nombre total d'étudiants
print(f"Nombre total d'étudiants either len() or n: {len(etudiants)}")
# 7. Demander un nom à supprimer et supprimer s’il est dans la liste

nom_a_supprimer = input("Entrez le nom de l'étudiant à supprimer : ")
if nom_a_supprimer in etudiants:
    etudiants.remove(nom_a_supprimer)
    print(f"{nom_a_supprimer} a été supprimé de la liste.")
else:
    print(f"{nom_a_supprimer} n'est pas dans la liste.")
# 8. Afficher la nouvelle liste
for i in range(n):
    print(f"Étudiant {i + 1} : {etudiants[i]}")