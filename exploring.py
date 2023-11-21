import re


my_string = """FETO: Único ( X )	Gemelar (	)
SITUAÇÃO: Longitudinal ( X )   	Transverso (   )
APRESENTAÇÃO: Cefálico ( X )   	Pélvico (   )         (  ) Variável
BATIMENTOS CARDÍACOS FETAIS:
Presente ( X )   FC: [[Fetal Heart Rate]]	Ausente ( 	)
MOVIMENTOS FETAIS: Presentes ( X ) Ausentes (  )
PLACENTA:
Anterior ( X )  Posterior (   )  Fúndica (   )  Prévia (	)
Grau __ Colo uterino ________
_______________
CORDÃO UMBILICAL: _________
BIOMETRIA FETAL:
DBP: [[Biparietal Diameter]]		CF: [[Femur Length]]
CA: [[Abdominal Circumference]]	CC: [[Head Circumference]]
CNN: ___ cm         		PESO: [[Estimated Weight]]
OFD: [[Occipital-Frontal Diameter]]	BASED GA:_
BASED US:_
LÍQUIDO:
Oligodrâmnio (	)   Polidrâmnio (	)   Normal (   )
ILA: [[Amniotic Fluid Index]]

CONCLUSÃO: 

- BIOMETRIA FETAL COMPATIVEL COM SEMANAS E DIAS 
- ADEQUADO PARA IDADE GESTACIONAL [[Length]]"""

# print(re.findall(r'\[\[.+?\]\]', my_string))

# my_list = [
#     {
#         0: {'name': 'matheus'},
#         1: {'name': 'carol'},
#     }
# ]

my_list = [1, 2]
my_list2 = [1, 2]

print(my_list == my_list2)
