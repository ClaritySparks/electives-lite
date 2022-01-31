from classes.house import House
from classes.job import Job
from classes.food import Food

FULL_POINT = 100

class Sim:
  def __init__(self, first_name: str, last_name: str, house: House, job: Job):
    self.__first_name = first_name
    self.__last_name =  last_name
    self.__simoleons = 100
    self.__bladder = FULL_POINT
    self.__energy = FULL_POINT
    self.__hunger = FULL_POINT
    self.__hygiene = FULL_POINT
    self.__inventory = []
    self.__house = house
    self.__job = job
    self.__dead = False
  
  @property
  def dead(self):
    return self.__dead
  
  def regulate_body(self):
    self.__bladder -= 4
    self.__hygiene -= 8
    self.__energy -= 2
    self.__hunger -= 3
    if self.__energy <= 0 and self.__hunger <= 0:
      self.__dead = True
  
  def drink(self):
    self.__bladder -= 6
    self.__hunger += 6
    if self.__hunger > FULL_POINT:
      self.__hunger = FULL_POINT
  
  def eat(self, food: Food):
    if food in self.__inventory:
      self.__hunger += food.energy
      if self.__hunger > FULL_POINT:
        self.__hunger = FULL_POINT
      self.__inventory.remove(food)
    else:
      print('Sim doesn\'t have the food in inventory. Please cook first.')
  
  def cook(self, food: Food):
    if self.__simoleons < food.price:
      print('Sim cannot afford {food}')
    else:
      self.__simoleons -= food.price
      self.__inventory.append(food)

  def shower(self):
    self.__hygiene = FULL_POINT
  
  def sleep(self):
    self.__energy = FULL_POINT

  def use_toilet(self):
    self.__bladder = FULL_POINT
  
  def work(self, total_hour: int):
    self.__simoleons += self.__job.calculate_salary(total_hour)

  def new_job(self, new_job: Job):
    self.__job = new_job
  
  def pay_rent(self, total_week: int):
    total_rent = self.__house.rent_per_week * total_week
    if self.__simoleons < total_rent:
      print('Sim cannot pay rent')
    else:
      self.__simoleons -= total_rent 
  
  """
  We can also overr3ide the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    dead_status = "⚱️" if self.__dead else "😊"
    return f"""Sim {self.__first_name} {self.__last_name} {dead_status}
--------------------------------------------------------------------------------------------------------
Total simoleons ${self.__simoleons}
Energy {self.__energy}% | Hunger {self.__hunger}% | Bladder {self.__bladder}% | Hygiene {self.__hygiene}% 
House: {self.__house}
Job: {self.__job}
Inventory: {self.__inventory}
--------------------------------------------------------------------------------------------------------"""