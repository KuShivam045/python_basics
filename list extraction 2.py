l = [[1,2,3,4,5], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,4,5]), 
{"k1": "sudh", "k2" : "ineuron", "k3": "kumar", 3:6, 7:8},["ineuron", "Data Science"]]

l1 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set :
        for j in i:
            if type(j) == int:
                l1.append(j)

    if type(i) == dict:
        for k in i.items():
            for g in k:
                if type(g) == int:
                    l1.append(g)
# print(l1)                    

# for i in set(l1):
#     print(i , " : ", l1.count(i))

# for i in l1:
#     if type(i) == str:
#         print(i)
# for i in l1:
#     if type(i) == str:
#         if i.isalnum():
#             print(i)

j = 1
for i in l1:
    if type(i) == int:

        j = i*j
print(j)
           
