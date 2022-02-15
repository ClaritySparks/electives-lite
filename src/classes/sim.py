from classes.house import House
from classes.job import Job
from classes.food import Food

MAX_POINT = 100
HOURS_IN_DAY = 24


class Sim:
  def __init__(self, first_name: str, last_name: str, house: House, job: Job):
    self.__first_name = first_name
    self.__last_name =  last_name
    self.__simoleons = 100
    self.__bladder = MAX_POINT
    self.__energy = MAX_POINT
    self.__hunger = MAX_POINT
    self.__hygiene = MAX_POINT
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
  
  def __regulate_body(self):
    """
    This function regulate sim body for each hour. Things happened during regulation:
    1. Decreasing value of hunger, bladder, energy and hygiene
    2. Increasing value of lifetime in hours, and rent check in for one day
    3. Dead status update if energy AND hunger is less than 0

    This function would be called during the actions and cannot be called outside the class.
    """
    self.__hunger -= 3
    self.__bladder -= 4
    self.__energy -= 5
    self.__hygiene -= 6
    
    self.__lifetime_in_hours += 1
    if self.__lifetime_in_hours % HOURS_IN_DAY == 0:
      self.__house.check_in_rent()
    
    if self.__energy <= 0 and self.__hunger <= 0:
      self.__dead = True
  
  def drink(self):
    """
    This function performs sim doing drink actions which include:
    1. Regulate the body first, so the refilled result is not affected by the regulate
    2. Decrease bladder level
    3. Increase hunger level
    4. If the hunger reach more than MAX_POINT, it will be reset to MAX_POINT
    """
    self.__regulate_body()
    self.__bladder -= 6
    self.__hunger += 6
    if self.__hunger > MAX_POINT:
      self.__hunger = MAX_POINT
  
  def eat(self, food: Food):
    """
    This function performs sim doing eat actions which include:
    1. Check if the selected food is in the inventory
    3. If the selected food is not in inventory, print error message
    4. If the selected food is in inventory,
       a. Regulate the body first, so the refilled result is not affected by the regulate
       b. Increase the hunger according to food energy.
       c. If the hunger reach more than MAX_POINT, it will be reset to MAX_POINT
    """
    if food in self.__inventory:
      self.__regulate_body()
      self.__hunger += food.energy
      if self.__hunger > MAX_POINT:
        self.__hunger = MAX_POINT
      self.__inventory.remove(food)
    else:
      print('Sim doesn\'t have the food in inventory. Please cook the food first.')
  
  def cook(self, food: Food):
    """
    This function performs sim doing cook actions which include:
    1. Check if the selected food price is affordable
    2. If the selected food is not affordable, print error message
    3. If the selected food is affordable,
       a. Regulate body for 3 hours (default cooking duration)
       b. Decrease simoleons with food price
       c. Add the cooked food to sim inventory
    """
    if self.__simoleons < food.price:
      print('Sim cannot afford {food}')
    else:
      for _ in range(3):
        self.__regulate_body()
      self.__simoleons -= food.price
      self.__inventory.append(food)

  def shower(self):
    self.__regulate_body()
    self.__hygiene = MAX_POINT
  
  def sleep(self, sleep_duration: int):
    """
    This function performs sim doing sleep actions which include:
    1. Regulate sim body as long as sleep duration
    2. Increase energy per hour for as long as sleep duration
    3. If the energy reach MAX_POINT, reset to MAX_POINT
    """
    for _ in range(sleep_duration):
      self.__regulate_body()
      self.__energy += 15
    if self.__energy > MAX_POINT:
      self.__energy = MAX_POINT

  def use_toilet(self):
    self.__regulate_body()
    self.__bladder = MAX_POINT
  
  def work(self, work_duration: int):
    """
    This function performs sim doing work actions which include:
    1. Regulate sim body as long as work duration
    2. Increase simoleons based on calculated salary
    """
    for _ in range(work_duration):
      self.__regulate_body()
    self.__simoleons += self.__job.calculate_salary(work_duration)

  def new_job(self, new_job: Job):
    self.__job = new_job
  
  def pay_rent(self, total_week: int):
    """
    This function performs sim doing pay rent actions which include:
    1. Checking if the total rent is pay-able
    2. If the simoleons cannot afford the rent, print error message
    3. If the simoleons can afford the rent, 
       a. Decrease the simoleons based on the total rent
       b. Call House.receive_rent based on total week
    """
    total_rent = self.__house.rent_per_week * total_week
    if self.__simoleons < total_rent:
      print('Sim cannot pay rent')
    else:
      self.__simoleons -= total_rent 
      self.__house.receieve_rent(total_week)
  
  def reset_body_status(self):
    """
    This function reset all of the sim body status
    """
    self.__bladder = MAX_POINT
    self.__energy = MAX_POINT
    self.__hunger = MAX_POINT
    self.__hygiene = MAX_POINT
    self.__dead = False
    self.__lifetime_in_hours = 0
  
  """
  We can also overr3ide the default function __str__() from class
  Ref: https://realpython.com/lessons/how-and-when-use-str/
  """
  def __str__(self):
    # Determine the sim status
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
    
    # Determine due status to be displayed
    due_status = "🚩🚩🚩 Your rent is on due 🚩🚩🚩" if self.__house.is_due() else "No due"
    lifetime_days = self.__lifetime_in_hours // 24

    # Determine lifetime status to be displayed
    lifetime_hours = self.__lifetime_in_hours % 24
    lifetime_status = f"Your lifetime: {lifetime_days} day(s) {lifetime_hours} hour(s)"
    
    # Prepare inventory list to be displayed
    inventory_items = ""
    for thing in self.__inventory:
      # \n will append a newline to the string, while {thing} will return Food.__str__ result
      inventory_items += f"\n- {thing}"

    # Return due to a template  
    return f"""Sim {self.__first_name} {self.__last_name} {status}
--------------------------------------------------------------------------------------------------------
Energy {self.__energy}% | Hunger {self.__hunger}% | Bladder {self.__bladder}% | Hygiene {self.__hygiene}%
Total simoleons\t: ${self.__simoleons} 
Lifetime\t: {lifetime_status}
Rent due\t: {due_status}
House\t\t: {self.__house}
Job\t\t: {self.__job}
Inventory\t: {inventory_items}
--------------------------------------------------------------------------------------------------------"""