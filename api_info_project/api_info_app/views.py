from django.shortcuts import render
from rest_framework.decorators import api_view # Specifie la méthode HTTP (get/delete/put)
from rest_framework.response import Response #Retourne une réponse sous format JSON
from .serializers import EmployeSerializer, DepartSerializer
from .models import Employe, Depart

# LES SERIALIZERS :::  peuvent être perçus comme des filtres d'entrées/sorties. 
# Ils vous permettent donc de valider (entrées) ou formater (sorties) vos données. 
# Autant leur usage est quasiment automatique avec des modèles, 
# autant ils sont parfois oubliés pour des points d'entrée personnalisés quand on débute. 
# Sauf cas exceptionnel (ce qui ne devrait pratiquement jamais arriver), 
# les serializers répondront à tous vos besoins, vous feront gagner du temps, 
# de la robustesse et de la lisibilité.

# Car si vous n'utilisez pas les serializers :

# vous n'exploitez pas le potentiel de l'outil, les serializers existent précisément pour ça !
# vous devez vous-même refaire le parsing, la validation, la conversion, les erreurs HTTP, etc
# vous dupliquez le code pour chacune de vos vues : pas de mutualisation possible
# vous risquez probablement de déporter la logique métier dans vos vues


# le SERIALIZER ::: est une class qui transforme les requetes complèxes en donnée de type JSON, XML ou autre, 
# sous forme de dictionnaires acceptables par les applications web


# LA CLASS META :::
#  Permets de configurer les options de métadonnées qu’il est possible d’attribuer aux modèles.

# GESTION DES ERREURS :::
# La mehode .is_valid() prends en option ( raise_exception ) qui nous renvois les erreurs d'exeptions.


#-------------# ON RECUPERE TOUTES LES ENTITES #-------------#

# On récupère tous les employés 
@api_view(['GET'])

def allEmploye(request):
    employes = Employe.objects.all() # C'est notre requête SQL 
    serialization = EmployeSerializer(employes,many=True)
    return Response(serialization.data)

# On récupère tous les départements 
@api_view(['GET'])

def allDepart(request):
    depart = Depart.objects.all()
    serialization = DepartSerializer(depart,many=True)
    return Response(serialization.data)

#-------------# ON RECUPERE LES ENTITES UNE PAR UNE #-------------#

#On récupère un employé 

@api_view(['GET'])

def getEmploye(request,id):
    employe = Employe.objects.get(id=id)
    serializer = EmployeSerializer(employe)
    return Response(serializer.data)

# On récupère un département
@api_view(['GET'])

def getDepart(request,id):
    depart = Depart.objects.get(id=id)
    serializer = DepartSerializer(depart)
    return Response(serializer.data)

#-------------# ON AJOUTE LES ENTITES #-------------#

# On ajoute un employé

@api_view(['POST'])

def addEmploye(request):
    serializer = EmployeSerializer(data = request.data, many = True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

# On ajoute un département 

@api_view(['POST'])

def addDepart(request):
    serializer = DepartSerializer(data = request.data, many = True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


#-------------# ON MODIFIE LES ENTITES #-------------#

# Mis à jour de département

@api_view(['PUT'])

def updateDepart(request,id):
    depart = Depart.objects.get(id=id)
    serializer = DepartSerializer(instance = depart, data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

# Mis à jour de l'employé

@api_view(['PUT'])

def updateEmploye(request,id):
    employe = Employe.objects.get(id=id)
    serializer = EmployeSerializer(instance = employe, data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)



#-------------# ON SUPPRIME LES ENTITES #-------------#

# On supprime l'entité employé 

@api_view(['DELETE'])

def delEmploye(request,id):
    employe = Employe.objects.get(id=id)
    employe.delete()
    return Response("Employe supprimé ^_^")

# On supprime le département

@api_view(['DELETE'])

def delDepart(request,id):
    depart = Depart.objects.get(id=id)
    depart.delete()
    return Response("Département supprimé ^_^")

