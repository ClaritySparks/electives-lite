class House:
  def __init__(self, name: str, description: str, area: float, rent_per_week: float):
    self.__name = name
    self.__description = description
    self.__area = area
    self.__rent_per_week = rent_per_week
    self.__time_in_days = 0

  @property
  def rent_per_week(self):
    return self.__rent_per_week

  def is_due(self):
    return self.__time_in_days >= 3

  def receieve_rent(self, total_week):
    self.__time_in_days -= total_week * 3
    if self.__time_in_days < 0:
      self.__time_in_days = 0
    
  def check_in_rent(self):
    self.__time_in_days += 1

  """
  We can also override the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    return f"House {self.__name} | {self.__description} | {self.__area} m2 | Rent per week ${self.__rent_per_week}"