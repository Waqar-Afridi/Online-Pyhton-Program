# form csv import reader
with open('file.csv','r')as f:
    csv_reader=reader(f)
    for row in csv_reader:
        print(row)

