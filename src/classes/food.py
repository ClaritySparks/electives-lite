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
    """
    This function is used to print out an object. It will be called automatically whenever we print the object.
    
    For instance,
    food1 = Food(name='pizza', price=20, energy=20)
    
    The result of print(food1) fill be Food pizza | | $20 | 20 hunger points
    """
    return f"Food {self.__name} | {self.__description} | ${self.__price} | {self.__energy} hunger points"


  """
  Ref: https://www.pythontutorial.net/python-oop/python-__eq__/
  """
  def __eq__(self, other):
    """
    This function is used to compare two objects and determine whether it is an equal object or not.
    This function is called automatically if we perform equal symbol (==).
    
    For instance,
    food1 = Food(name='pizza', price=20, energy=20)
    food2 = Food(name='pizza', price=20, energy=20)

    The result of food1 == food2 will be True because we only compare these three attributes.
    """
    return self.__energy == other.energy and self.__price == other.price and self.__name == other.name