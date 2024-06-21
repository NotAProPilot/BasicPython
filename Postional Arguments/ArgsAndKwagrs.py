"""
A short snippet demonstating 
"""

def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
  print(appetizer)
  print(entrees)
  print(sides)
  print(dessert_scoops)

# Invoking the function:
single_prix_fixe_order('Baby Beets',
                       'Salmon','Scallops',
                       # For agrs, the args name must be precise
                       sides='Mashed Potatoes', 
                       # For kwagrs of desert scoops, name can be anything
                       # And there can be multiple args
                       # Since they will be stored as dictionary
                       dest1= 'Vanilla', 
                       dest2 = 'Cookies and Cream')