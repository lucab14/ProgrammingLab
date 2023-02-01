class ExamException(Exception):
  pass


class CSVFile:
  def __init__(self,name=""):
    self.name=name

  def get_data(self):
    try:
      my_file=open(self.name, 'r')
      
    except Exception as e:
      raise ExamException('Errore {}'.format(e))
    
    list_values=[]
    
    for line in my_file:
      elements=line.strip('\n').split(',')
      
      if elements[0]!='epoch':
        list_values.append(elements)
    
    if not len(list_values):
      raise ExamException("Errore, lista vuota")

    my_file.close()
    return list_values


class CSVTimeSeriesFile(CSVFile):

  def get_data(self):
    list_elements=super().get_data()
    parsed_list=[]
    
    for element in list_elements:
      add_new= True
      new_row=[]
      
      for index, column in enumerate(element):
        
        if index==0:
          
          try:
            new_row.append(int(column))
          
          except:
            
            try:
              data=float(column)
              new_row.append(int(data))
            
            except:
              add_new=False
              break #questo except serve per controllare input sporchi, come ad esempio stringhe non numeriche sulla colonna della data
        else:
          
          try:
            if len(new_row)<2:
              new_row.append(float(column))
              add_new=True
          
          except:
            add_new=False
            break

      if add_new is True:
        parsed_list.append(new_row)
        
    verified_list= self.verify_data(parsed_list)  
    return verified_list

  def verify_data(self, data):
    for i,day in enumerate(data):
      
      for j,next_day in enumerate(data):
        
        if i!=j and day[0]==next_day[0]:
          raise ExamException("Errore, valore duplicato")
        
        if i<j and day[0]>next_day[0]:
          raise ExamException("Errore, lista disordinata")

    return data
    #controlla se ci sono duplicati o disordine fra le date


def compute_daily_max_difference(time_series):
  verified_time_series=test(time_series)
  list_h=[]
  index=0
  
  for epoch in verified_time_series:
    epoch=time_series[index]
    temp_list=[]
    day_start_epoch=epoch[0]-(epoch[0]%86400)
    
    for lists in verified_time_series:
      new_day_start_epoch=lists[0]-(lists[0]%86400)
      
      if lists[0]>=epoch[0]:
        if new_day_start_epoch==day_start_epoch:
          temp_list.append(lists[1])
          index+=1
        
        else:
          break  
    
    list_h.append(temp_list)
    
    if index>len(verified_time_series)-1:
      break
  # TEST PER VERIFICARE LA LIST_H SE ERA CORRETTA(ELIMINARE)
  # for x in list_h:
  #   print(x)
  #   print('\n')
  lista_finale=[]
  
  for temperature in list_h:
    
    if len(temperature)>1:
      differenza_max= max(temperature)-min(temperature)
      lista_finale.append(differenza_max)
    
    else:
      lista_finale.append(None)
  
  return lista_finale


def test(ver_list):
  time_series=[]
  if not isinstance(ver_list, list) or not len(ver_list):
    raise ExamException("Errore, lista vuota")

  for row in ver_list:
    
    if type(row)!=list:
      continue
    
    if len(row)==0:
      continue
    
    if type(row[0])!=int:
      continue
    
    if type(row[1])!=float:
      continue
    
    else:
      time_series.append(row)

  if not len(time_series):
    raise ExamException("Errore, Lista vuota")

  return time_series

#esecuzione
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()

for element in time_series:
  print(element)

lists=compute_daily_max_difference(time_series)
#lists=compute_daily_max_difference([[None, 3.2],[2, 'x'], []])  
print('Escursioni termiche')
i=1

for element in lists:
  print("giorno numero_"+ str(i) + " = "+ str(element))
  i+=1