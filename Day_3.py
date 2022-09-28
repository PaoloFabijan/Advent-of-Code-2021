import numpy as np

# Prvi dio zadatka
list = [] # Lista sa binarnim zapisom
with open("data_3.txt") as data:
    for line in data:
        row = line.split()
        list.append(str(row[0]))
list2 = [] # Lista sa razdvojenim znamenkama binarnog zapisa
for i in range(0, len(list)):
    list2.append([int(x) for x in str(list[i])])
arr = np.array(list2) # Matrica sa razdvojenim znamenkama binarnog zapisa

gamma_rate = []
gamma = np.count_nonzero(arr > 0, 0) # Brojevi koji su veći od 0
for i in range(0, 12):
    if gamma[i] > 500: # Brojevi koji su veći od 500 tj. brojevi koji se češće pojavljuju
        gamma_rate.append(1)
    else:
        gamma_rate.append(0)
gamma_rate = str(int("".join([str(i) for i in gamma_rate]))) # Spajanje pojedinačnih brojeva iz liste u jedan
gamma_rate = int(gamma_rate, 2) # Pretvorba binarnog zapisa u dekadski zapis

epsilon_rate = []
epsilon = np.count_nonzero(arr > 0, 0) # Brojevi koji su veći od nule
for i in range(0, 12):
    if epsilon[i] < 500: # Brojevi manji od 500 tj. brojevi koji se manje pojavljuju
        epsilon_rate.append(1)
    else:
        epsilon_rate.append(0)
epsilon_rate = str(int("".join([str(i) for i in epsilon_rate]))) # Spajanje pojedinačnih brojeva iz liste u jedan
epsilon_rate = int(epsilon_rate, 2) # Pretvorba binarnog zapisa u dekadski zapis

print(f"Gamma rate is: {gamma_rate}\nEpsilon rate is: {epsilon_rate}\nThe power consumption of the submarine is: {gamma_rate*epsilon_rate}")


# Drugi dio zadatka
