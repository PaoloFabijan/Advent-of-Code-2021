import numpy as np

data = np.genfromtxt("data_1.txt")

## Prvi dio zadatka
# list = []
# for i in range(0, len(data)-1):
#     if data[i+1] > data[i]:
#         list.append(data[i+1])
# print(f"Answer is: {len(list)}")


## Drugi dio zadatka
# all_sums = [] # Lista sa svim sumama triju brojeva
# for i in range(0, len(data)-2):
#     all_sums.append(data[i] + data[i+1] + data[i+2])

# sums = [] # Lista sa svim sumama triju brojeva koje su veće od prethodnih
# for i in range(0, len(all_sums)-1):
#     if all_sums[i+1] > all_sums[i]:
#         sums.append(all_sums[i+1])
# print(f"Answer is: {len(sums)}")