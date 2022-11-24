class CSVFile():
  def __init__(self, name):
    self.name=name
      
  def get_data(self):
    try:
      file= open(self.name, 'r')
      values=[]
      for line in file:
        elements=line.strip('\n').split(',')
        if elements[0]!='Date':
          values.append(elements)
      file.close()
      return values
    except Exception as e:
      print('Errore {}'.format(e))


class NumericalCSV(CSVFile):
  lista=[]
  lista= super.get_data()
  for item in lista:
    try:
      float(item[1])
    except ValueError as e:
      print('Errore {}'.format(e))

    except TypeError as e:
      print('Errore di TIPO, il valore era di tipo {}'.format(e))

    except Exception as e:
      print('Errore {}'.format(e))