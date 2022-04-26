#Autor: Vini
#O que o código faz: Calcula o ganho de informação de um atributo informado
#Motivo de ter feito: Infelicidade com a própria existência

import math

def entropia(pos_,neg_):
    if pos_ == 0 or neg_ == 0:
        return 0
    else:
        p1 = pos_/(pos_+neg_)
        p0 = neg_/(pos_+neg_)

        return -p1 * math.log(p1,2) - p0 * math.log(p0,2)
    
pos_total = 0
neg_total = 0
valor = dict()
entropia_dic = dict()
while True:
    temp = input("Digite o valor do atributo (s para sair): ")
    if temp == 's':
        break
    else:
        pos = int(input("Digite o número de positivos: "))
        neg = int(input("Digite o número de negativos: "))
        temp2 = {"pos":pos,"neg":neg}
        valor[temp] = temp2
        pos_total += pos
        neg_total += neg
        
for key, value in valor.items():
    entropia_res = entropia(value['pos'],value['neg'])
    entropia_dic[key] = round(entropia_res,5)
    
    
total = pos_total + neg_total
erestante = 0

print("\n")
for key,value in entropia_dic.items():
    numero_participacao = valor[key]['pos'] + valor[key]['neg']
    erestante += (numero_participacao/total) * value
    print(f"{key}: {value}\n")
    

print(f"H(S): {entropia(pos_total,neg_total)}\n")
ganho_informacao = entropia(pos_total,neg_total) - erestante
print("Ganho informação: ",round(ganho_informacao,5))

