items = [
("product1",8),
("product4",5),
("product3",12),
]
# def sort_item(item):
#     return item[1]
# item.sort(key=sort_item,reverse=True)
# print(item)
items.sort(key=lambda a: a[0])
print(items)