# pcost.py
#
# Exercise 1.27

f = open("Data/portfolio.csv", "rt")

headers = next(f).split(",")

name = []
shares = []
price = []


for line in f:
    row = line.split(',')
    name.append(row[0])
    shares.append(int(row[1]))
    price.append(float(row[2]))

sum = 0
for s, p in zip(shares,price):
    sum += s*p

print("Total Price: ", sum)

f.close()