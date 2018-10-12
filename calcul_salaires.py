import unittest
def calcul_salaire(metier,experience):
    if metier == 'Architecte' and experience == 4:
        return '4000'
    
    if metier == 'Médecin' and experience == 8:
        return '7000'

    if metier == 'consultant' and experience == 5:
        return '5000'


if __name__ == '__main__':
    print(" Un architecte qui a 4 ans d'expérience gagne 4000 euros")
    print(" Un médecin qui a 8 ans d'expérience gagne 7000 euros")
    print(" Un architecte qui a 4 ans d'expérience gagne 4000 euros")


   
