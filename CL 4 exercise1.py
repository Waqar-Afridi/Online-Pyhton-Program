def list_r(l):
    reverse_srt=[]

    for name in l:
        reverse_srt.append(name[: : -1])

    return reverse_srt

print(list_r(['abc','xyz']))

# LC
# def reverse_str(l):
#     return [name[: : -1] for  name in l]
#
# print(reverse_str(['abc','xyz']))

