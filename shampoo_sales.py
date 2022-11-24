def sum_csv(file_name):
  values=[]
  for line in file_name:
    elements=line.split(',')

    if elements[0] != 'Date':
      value=elements[1]

      values.append(float(value))



  return  sum(values)

file_name= open('shampoo_sales.csv', 'r')
print(sum_csv(file_name))
file_name.close()

