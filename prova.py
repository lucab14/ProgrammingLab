def sum_csv(file_name):
  values=[]
  for line in file_name:
    elements=line.split(',')
    if elements[0] != 'Date' :
      value=float(elements[1])
      values.append(value)

  file_name.close()
  return sum(values)

file=open('shampoo_sales.csv', 'r')
print(sum_csv(file))
  