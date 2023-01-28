def sum_list(lista):
  if not len(lista):
    return None
  return sum(lista)


def read_csv(file_name):
  my_file=open(file_name, 'r')
  values=[]
  for line in my_file:
    elements= line.split(',')
    if elements[0]!='Date':
      values.append(elements[1])
  return values

def convert_list(values):
  list=[]
  for item in values:
    try:
      list.append(float(item))
    except:
      None
  return list

def sum_csv(file_name):
  file=read_csv(file_name)
  list=convert_list(file)
  sum_file=sum_list(list)
  return sum_file

nome='shampoo_sales.csv'
print(sum_csv(nome))