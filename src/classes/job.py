class Job:
  def __init__(self, name: str, description: str, pay_per_hour: float, max_hours: int):
    self.__name = name
    self.__description = description
    self.__pay_per_hour = pay_per_hour
    self.__max_hours = max_hours

  @property
  def pay_per_hour(self):
    return self.__pay_per_hour

  @property
  def max_hours(self):
    return self.__max_hours

  def calculate_salary(self, work_duration: int) -> float:
    """
    This function return calculated salary based on work duration.
    Due to maintaining work life balance, we avoid overtime, so there won't be overtime benefit.
    If the work duration exceed max work duration, it will return the max pay based on max work duration.

    """
    if work_duration >= self.__max_hours:
      return self.__max_hours * self.__pay_per_hour
    else:
      return work_duration * self.__pay_per_hour

  """
  We can also override the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    return f"{self.__name} | {self.__description} | Pay ${self.__pay_per_hour}/hr | Max work for {self.__max_hours} hr(s)"