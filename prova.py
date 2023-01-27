def sum_csv(file_name):
  my_file=open(file_name, 'r')
  values=[]
  for line in my_file:
    elements=line.split(',')
    if elements[0] != 'Date' :
      value=float(elements[1])
      values.append(value)

  my_file.close()
  return sum(values)

file='shampoo_sales.csv'
print(sum_csv(file))
  