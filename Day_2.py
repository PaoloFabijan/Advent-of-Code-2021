# Prvi dio zadatka
Dir = [] # Lista s pozicijama
Val = [] # Lista s vrijednostima pozicija
with open("data_2.txt") as data:
    for line in data:
        row = line.split()
        Dir.append(str(row[0]))
        Val.append(int(row[1]))
# f = [] # Lista sa svim odgovarajućim vrijednostima pozicija "forward"
# u = [] # Lista sa svim odgovarajućim vrijednostima pozicija "up"
# d = [] # Lista sa svim odgovarajućim vrijednostima pozicija "down"
# for i in range(0, len(Dir)):
#     if Dir[i] == "forward":
#         f.append(Val[i])
#         f_sum = sum(f) # Suma svih vrijednosti pozicija "forward"
#     if Dir[i] == "up":
#         u.append(Val[i])
#         u_sum = sum(u) # Suma svih vrijednosti pozicija "up"
#     if Dir[i] == "down":
#         d.append(Val[i])
#         d_sum = sum(d) # Suma svih vrijednosti pozicija "down"
# print(f"Final horizontal position is: {f_sum}\nFinal depth is: {d_sum - u_sum}\nProduct of the 2 positions: {f_sum*(d_sum-u_sum)}")


# Drugi dio zadatka
hor = 0
aim = 0
depth = 0
for i in range(0, len(Dir)):
    if Dir[i] == "forward":
        hor += Val[i]
        depth += (aim * Val[i])
    if Dir[i] == "up":
        aim -= Val[i]
    if Dir[i] == "down":
        aim += Val[i]
print(f"Final horizontal position is: {hor}\nFinal depth is: {depth}\nProduct of the 2 positions: {hor*depth}")