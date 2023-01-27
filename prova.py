def sum_csv(file_name):
  if len(file_name)!=0:
    return sum(values)
  else:
    return None

file=open('shampoo_sales.csv', 'r')
values=[]
for line in file:
  elements=line.split(',')
  if elements[0] != 'Date' :
    value=float(elements[1])
    values.append(value)

file.close()
print(sum_csv(values))
  