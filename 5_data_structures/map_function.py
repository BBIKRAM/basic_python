items = [
("product1",8),
("product2",5),
("product3",12),
]
# prices =[]
# for item in items:
#     prices.append(item[1])
# print(prices)

x = map(lambda item:item[0],items)
for item in x:
    print(item)