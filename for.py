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