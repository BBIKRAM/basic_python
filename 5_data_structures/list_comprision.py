items = [
("product1",8),
("product2",5),
("product3",12),
]

# prices =list( map(lambda item:item[0],items))
# prices =[expression for item in items]
prices = [item[1] for item in items]
print(prices)




# filtered=list( filter(lambda item:item[1]>7,items))
filtered =[item for item in items if item[1] > 6]
print(filtered)
