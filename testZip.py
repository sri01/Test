
# #list1=('ap','ts','mh')
# #list2=('ama','hyd','mum')
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# #A1 = dict(zip(list1,list2))
# print (A0)
#
# print(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# #help(zip)
# #print (A1)
#
# A1=range(10)
# #for i in A1:
# #    print(i)
#
# A2=sorted([i for i in A1 if i in A0])
# # for i in A1:
# #     if i in A0:
# #         print
# for i in A0:
#     print(i)
#     print(A0[i])
#print(A2)
### Example 2
def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(4, [3,2,1])
f(3)

f(5)


