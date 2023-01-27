def sum_csv(file):
  values=[]
  for line in file:
    elements=line.split(',')
    if elements[0] != 'Date' :
      value=float(elements[1])
      values.append(value)

  file.close()
  return sum(values)


file=open('shampoo_sales.csv', 'r')
print(sum_csv(file))




  
  
  
  
  
  
  
  

  
  
#file="shampoo_sales.csv"
  