import time
""" A simple OOP script.

This script demot the concept of OOP in Python
and including comment to comment it with Java. 
"""

# Initilaizing a Horse class:
class Horse:

 
  """ Initializing constructor
  
  Including self, name (input_name as in example).
  You can specify an default value by assigning the args in __init__ a number. 
  For example, we will set the default age to 0. 

  Compare to Java, this method/function incoperate 
  the attribute declration and the constructor into one.
  """
  def __init__(self, input_name, input_age = 0, isWhite = True):
    # The 'self' keyword means the CURRENT instance
    # In this line, for instance, the name this instance is input_name
    self.name = input_name

    self.age = input_age

    self.isWhite = isWhite
    
    # Initializing a list of enemies:
    # As an empty list: 
    self.enemy_list = []
    
  """ Initializing action
  
  In Python, methods are use to describe what an instance of a object
  can do.
  
  For example, we initalizing the action of 'Introducing',
  which prints out its information.
  """
  def introduce(self):
    print("My name is {name} and I'm {age} years old!".format(name = self.name, age = self.age))
    
  """Initializing multi-instance action
  
  A method can involve another instance as well.
  For example, a horse can have a list of enemies. 
  
  An enemy is defined as different in skin color.
  So a white horse will fight a black horse, and vice versa. 
  
  In the process, another instance, other_horse,
  is created. 
  
  Agrs: self, other_horse
  """
  
  def fight_enemy(self, other_horse):
    # Check if the horse is the same race:
    if (other_horse.isWhite == False):
      # The current horse add the other horse to enemy list:
      self.enemy_list.append(other_horse)
      
      # The other horse also add the current horse as an enemy:
      other_horse.enemy_list.append(self)
      
      # Print out a message:
      print("{Horse_name} is added to enemy list!".format(Horse_name = other_horse.name))

# Create a new pet
horse_1 = Horse(str(input("Enter a name: ")), int(input("Enter age: ")), False)

# As a 2 second delay:
time.sleep(2)
horse_2 = Horse(str(input("Enter a name: ")), int(input("Enter age: ")), True)

# Add as enemy:
horse_2.fight_enemy(horse_1)

