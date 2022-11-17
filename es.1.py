def sum_list(my_list):
    somma= 0
    for item in my_list:
       somma += item
    return somma  

my_list=[]
print('Risultato {}'.format(sum_list(my_list)))