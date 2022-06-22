with open('file0.txt','r+') as f:
   f.seek(len(f.read()))
   f.write('thanks for subsrcibling \n')