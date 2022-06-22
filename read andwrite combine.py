with open("file11.txt",'r') as rf:
    with open("file12.txt", "w") as wf:
        wf.write(rf.read())