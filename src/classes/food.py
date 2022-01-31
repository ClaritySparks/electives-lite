class Food:
  def __init__(self, name: str, description: str, price: float, energy: int):
    self.__name = name
    self.__description = description
    self.__price = price
    self.__energy = energy
  
  @property
  def name(self):
    return self.__name
  
  @property
  def energy(self):
    return self.__energy

  @property
  def price(self):
    return self.__price

  """
  We can also override the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    return f"Food {self.__name} | {self.__description} | ${self.__price} | {self.__energy} hunger points"


  """
  Ref: https://www.pythontutorial.net/python-oop/python-__eq__/
  """
  def __eq__(self, other):
    return self.__energy == other.energy and self.__price == other.price and self.__name == other.name