# Exercice 2 : Coordonnées des Villes avec Tuples

# 1. Créer une liste de tuples contenant les coordonnées des villes
# villes = [("Paris", (lat1, lon1)), ("New York", (lat2, lon2)), ...]
villes = []
for i in range(2):
    nom_ville = input(f"Entrez le nom de la ville {i + 1} : ")
    latitude = float(input(f"Entrez la latitude de {nom_ville} : "))
    longitude = float(input(f"Entrez la longitude de {nom_ville} : "))
    villes.append((nom_ville, (latitude, longitude)))
# 2. Afficher chaque ville avec ses coordonnées
# for ville in villes:
    # ..................
for ville in villes:
    nom, coord = ville 
    latitude, longitude = coord
    print(f"Ville : {nom}, Latitude : {latitude}, Longitude : {longitude}")
# 3. Afficher uniquement les latitudes
# for ville in villes:
    # ..................
for ville in villes:
    nom, coord = ville 
    latitude, longitude = coord
    print(f"Latitude de {nom} : {latitude}")
# 4. Calculer et afficher la latitude moyenne
# latitudes = [...]
latitudes = [coord[1][0] for coord in villes]
print(f"latitudes pour tous les villes : {latitudes}")

# moyenne = ...
moyenne = sum(latitudes) / len(latitudes)
# print(...)
print(f"Latitude moyenne : {moyenne}")
