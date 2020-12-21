durchlauf = 1

while durchlauf <= 5:
    print(durchlauf)
    durchlauf += 1

#
namen = ["Peter","Bruce Wayne", "Tony Stark"]

k = 0
while k< len(namen):
    print(namen[k])
    k += 1

# ci
# ontinue
j = 0
while j<= 20:
    j += 1
    if j % 2:
        continue
    print(j)

# break
while True:
    userinput = input("Euro (q beendet): ")
    if (userinput == "q"):
        break
    euro = float(userinput)
    print("Donnar : %.2f" %(euro*1.07))





