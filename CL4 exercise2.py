# def sr(l):
#     em_list=[]
#     for i in l:
#         if type(i)==int or type(i)==float:
#          em_list.append(str(i))
#     return em_list
# print(sr([1,3,1.0]))
#

# CL

def num(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float) ]
print(num([1,3,1.0]))