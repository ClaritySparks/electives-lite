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
    self.__lifetime_in_hours = 0
  
  @property
  def dead(self):
    return self.__dead

  @property
  def inventory(self):
    return self.__inventory
  
  @property
  def house(self):
    return self.__house
  
  def regulate_body(self):
    self.__bladder -= 4
    self.__hygiene -= 6
    self.__energy -= 5
    self.__hunger -= 3
    self.__lifetime_in_hours += 1
    if self.__lifetime_in_hours % 24 == 0:
      self.__house.check_in_rent()
    if self.__energy <= 0 and self.__hunger <= 0:
      self.__dead = True
  
  def drink(self):
    self.regulate_body()
    self.__bladder -= 6
    self.__hunger += 6
    if self.__hunger > FULL_POINT:
      self.__hunger = FULL_POINT
  
  def eat(self, food: Food):
    self.regulate_body()
    if food in self.__inventory:
      self.__hunger += food.energy
      if self.__hunger > FULL_POINT:
        self.__hunger = FULL_POINT
      self.__inventory.remove(food)
    else:
      print('Sim doesn\'t have the food in inventory. Please cook first.')
  
  def cook(self, food: Food):
    for _ in range(3):
      self.regulate_body()
    if self.__simoleons < food.price:
      print('Sim cannot afford {food}')
    else:
      self.__simoleons -= food.price
      self.__inventory.append(food)

  def shower(self):
    self.regulate_body()
    self.__hygiene = FULL_POINT
  
  def sleep(self, total_hour: int):
    for _ in range(total_hour):
      self.regulate_body()
      self.__energy += 15
    if self.__energy > FULL_POINT:
      self.__energy = FULL_POINT

  def use_toilet(self):
    self.regulate_body()
    self.__bladder = FULL_POINT
  
  def work(self, total_hour: int):
    for _ in range(total_hour):
      self.regulate_body()
    self.__simoleons += self.__job.calculate_salary(total_hour)

  def new_job(self, new_job: Job):
    self.__job = new_job
  
  def pay_rent(self, total_week: int):
    total_rent = self.__house.rent_per_week * total_week
    if self.__simoleons < total_rent:
      print('Sim cannot pay rent')
    else:
      self.__simoleons -= total_rent 
      self.__house.receieve_rent(total_rent)
  
  def reset(self):
    self.__simoleons = 100
    self.__bladder = FULL_POINT
    self.__energy = FULL_POINT
    self.__hunger = FULL_POINT
    self.__hygiene = FULL_POINT
    self.__dead = False
    self.__lifetime_in_hours = 0
  
  """
  We can also overr3ide the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    status = ""
    if self.__dead:
      status = "| Dead ⚱️"
    elif self.__energy <= 20:
      status = "| Sleepy 🤬"
    elif self.__hunger <= 20:
      status = "| Hungry 😡"
    elif self.__bladder <= 20:
      status = "| Need to use toilet 😠"
    elif self.__hygiene <= 20:
      status = "| Need a shower 😞"
    else:
      status = "| Happy 😊"
    due_status = "🚩🚩🚩 Your rent is on due 🚩🚩🚩" if self.__house.is_due() else "No due"
    lifetime_days = self.__lifetime_in_hours // 24
    lifetime_hours = self.__lifetime_in_hours % 24
    lifetime_status = f"Your lifetime: {lifetime_days} day(s) {lifetime_hours} hour(s)"
    inventory_items = ""
    for thing in self.__inventory:
      inventory_items += f"\n- {thing}"
    return f"""Sim {self.__first_name} {self.__last_name} {status}
--------------------------------------------------------------------------------------------------------
Total simoleons ${self.__simoleons}
Energy {self.__energy}% | Hunger {self.__hunger}% | Bladder {self.__bladder}% | Hygiene {self.__hygiene}% 
Lifetime: {lifetime_status}
Rent due: {due_status}
House: {self.__house}
Job: {self.__job}
Inventory: {inventory_items}
--------------------------------------------------------------------------------------------------------"""