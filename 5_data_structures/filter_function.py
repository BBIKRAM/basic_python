items = [
("product1",8),
("product2",5),
("product3",12),
]

filtered =[]
x= filter(lambda item:item[1]>7,items)
for item in x:
    print(item)