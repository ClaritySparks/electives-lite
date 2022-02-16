class Sim:
  def __init__(self, first_name: str, last_name: str, age: int):

    # Public attributes
    self.first_name = first_name
    self.last_name = last_name
    
    # Private attributes
    self.__age = age
    self.__energy = 100

  @property
  def age(self):
    return self.__age

# Instansiasi sebuah objek dari kelas Sim
deborah = Sim('Deborah', 'Tampubolon', 23)
print(deborah)
