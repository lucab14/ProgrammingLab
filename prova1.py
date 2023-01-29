class CSVFile:
  def __init__(self, name):
    self.name=name

  def get_data(self):
    try:
      file=open(self.name, 'r')
      lists=[]
      for line in file:
        elements=line.strip('\n').split(',')
        if elements[0]!='Date':
          data=elements[0]
          value=elements[1]
          lists.append([data, value])
      file.close()
    except Exception as e:
      return print('Errore {}'.format(e))
    return lists

class NumericalCSVFile(CSVFile):
  def get_data(self):
    lista=[]
    numeric=super().get_data()
    for value in numeric:
      newlist=[]
      if value[0]:
        newlist.append(value)    
      else:
        for item in value:
          try:
            valore=float(item)
            lista.append(valore)
          except Exception:
            print('Errore di conversione')
            break
    return sum(lista)
        
    

    

file_name=NumericalCSVFile('shampoo_sales.csv')
print(file_name.get_data())