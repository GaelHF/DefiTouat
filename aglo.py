import math

## CRÉATION DE LA FORMULE
class FormuleTouat():
    def __init__(self, a, b, c, n):
        self.a = a
        self.b = b
        self.c = c
        self.n = n
    def input_n(self): self.n = int(input("Entrez la valeur de (n) > "))
    def calcul(self):
        #Formule M. Touat
        ft_result = math.sqrt(self.n*(self.n+1)*(self.n+2)*(self.n+3)+1)

        #Formule GaëlHF
        my_result = self.a*self.n**2 +self.b*self.n+self.c
        return [ft_result, my_result]


## TESTS
nombre_de_formule_de_gael_qui_on_fonctionner = 0
nombre_de_formule_de_gael_a_verifier = 1000

for n_value in range(nombre_de_formule_de_gael_a_verifier):
    formule_touat = FormuleTouat(1, 3, 1, n_value+1).calcul()[0]
    formule_gael = FormuleTouat(1, 3, 1, n_value+1).calcul()[1]

    print(f"n: {n_value+1}\nFormule de M. Touat : " + str(float(formule_touat)) + "\nFormule de Gaël HF : " + str(float(formule_gael)) + "\n")

    if formule_touat == formule_gael:
        nombre_de_formule_de_gael_qui_on_fonctionner += 1
        print("La formule de Gaël fonctionne")
    else: print("La formule de Gaël ne fonctionne pas")

if nombre_de_formule_de_gael_qui_on_fonctionner == nombre_de_formule_de_gael_a_verifier:
    print(f"\n\nLa formule de Gaël a fonctionner pour tout les nombres naturels de 1 à {str(nombre_de_formule_de_gael_a_verifier)}")

else: print(f"\n\nLa formule de Gaël n'a pas fonctionner pour tout les nombres naturels de 0 à {str(nombre_de_formule_de_gael_a_verifier)}\n{str(nombre_de_formule_de_gael_a_verifier-nombre_de_formule_de_gael_qui_on_fonctionner)} nombres naturels on fonctionnés avec la formule de Gaël")