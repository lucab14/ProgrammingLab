# #enumerate serve a indicizzare un elemento in una lista (parte da 0 e arriva fino a "n" escluso)
# names = [[1,7,2], ["Jack", 9], ["ciao",6]]
# lista=[]
# for index,name in enumerate(names):
#   if index==0:
#     for i in name:
#       print(i)
#     lista.append(name)
#   else:
#     print(name)
# print(lista)

# lista=[[12, 34.5], [31, 29.8], ["ciao", "io", 6], [34, 67]]
# ciao=[]
# for x in lista:
#   row=[]
#   for i, element in enumerate(x):
#     if i==0:
#       row.append(element)

#     else:
#       try:
#         ciao.append(float(element))
#       except:
#         print("Errore di conversione")
#         break
#   print(row)
# print(ciao)

# lista_liste=[[4,2],[4,5],[7,8]]
# list=[]
# #i=0
# for i, date in enumerate(lista_liste):
#   print(date)
#   #y=date[0]-(date[0]%2)
#   for x in lista_liste:
#     if x[0]%2==0:
#       i+=1
#     else: break
#   date=lista_liste[i]

# for i in range(10):
#   if i%2==0:
#     i+=3
#   print(i)

list=[[1,2],[2,3],[3,4],[4,7]]

for i,x in enumerate(list):
  for j,y in enumerate(list):
    if i!=j and x[0]==y[0]:
      raise Exception("DUPLICATO")

    if i<j and x[0]>y[0]:
      raise Exception("DISORDINE")
    



