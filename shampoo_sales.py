def sum_csv(file_name):
  values=[]
  for line in file_name:
    elements=line.split(',')

    if elements[0] != 'Date':
      value=elements[1]

      values.append(float(value))


  file_name.close()
  return  sum(values)



