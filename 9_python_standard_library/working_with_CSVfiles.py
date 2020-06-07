# CSV stands for comma seperated value
import csv
#writing a csv files
# with open("data.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id","product_id","product_value"])
#     writer.writerow([100,3,4])
#     writer.writerow([1200,4,55])


#reading from csv files

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)