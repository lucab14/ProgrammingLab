class ExamException:
  pass

class MovingAverage:
  def __init__(self, lenght):#len=2
    self.lenght=lenght

  def compute(self, list_value): #[2,4,8,16]
    lista_media=[]
    if not len(list_value):
      raise ExamException("Errore, lista valori vuota")
    if len(list_value)<self.lenght:
      raise ExamException("Errore, lista valori piccola")
    for i in range(len(list_value)):
      somma=0
      for j in range(self.lenght):
        try:
          if type(list_value[j])==str:
            raise ExamException("Errore, valore stringa")
          if list_value[i+self.lenght-1]:
            somma+=list_value[i+j]
        except IndexError:
          break
      media=somma/self.lenght
      lista_media.append(media)
    return lista_media


moving_average=MovingAverage(2)
result=moving_average.compute([2,4,8,16])
print(result)