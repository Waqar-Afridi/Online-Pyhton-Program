with open("data.txt",'r') as rf:
    with open("datacome.txt",'w') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"name is {name}  and salary  is {salary}")
