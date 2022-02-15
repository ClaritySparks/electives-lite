DAYS_IN_WEEK = 3


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
    """
    This function 
    1. Return True, if the rent time exceed the number of days in a week
    2. Return False, vice versa
    """
    return self.__time_in_days >= DAYS_IN_WEEK

  def receieve_rent(self, total_week):
    """
    This function decrease receive the rent payment including:
    1. Decrease rent time in days based on number of total week
    2. If the decreased time is negative, reset to 0
    """
    self.__time_in_days -= total_week * DAYS_IN_WEEK
    if self.__time_in_days < 0:
      self.__time_in_days = 0
    
  def check_in_rent(self):
    """
    This function increment the counter of rent time by 1 day
    """
    self.__time_in_days += 1

  def start_rent(self):
    """
    This function is called when the sim is created and pick a house
    """
    self.__time_in_days = 0

  """
  We can also override the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    return f"House {self.__name} | {self.__description} | {self.__area} m2 | Rent per week ${self.__rent_per_week} | Rent time {self.__time_in_days} day(s)"