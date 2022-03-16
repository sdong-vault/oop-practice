
class Ingredient:
  def __init__(self, name, price, calories, is_vegetarian, is_vegan):
    self.name = name
    self.price = price
    self.calories = calories
    self.is_vegetarian = is_vegetarian
    self.is_vegan = is_vegan

class Kale(Ingredient):
  def __init__(self):
      super(Kale, self).__init__("kale", 5, 5, True, True)

class Chicken(Ingredient):
  def __init__(self):
      super(Chicken, self).__init__("chicken", 3, 100, False, False)

class Parmesan(Ingredient):
  def __init__(self):
      super(Parmesan, self).__init__("parmesan", 3, 100, True, False)


class SaladBowl:
  def __init__(self, name, ingredients):
    self.name = name
    if ingredients is None or len(ingredients) == 0:
      self.ingredients = list()
    else:
      self.ingredients = ingredients
    
  def add_ingredient(self, ingredient):
    self.ingredients.append(ingredient)
  
  def calculate_price(self):
    sum = 0
    for ingredient in self.ingredients:
      sum += ingredient.price
    return sum
  
  def calculate_calories(self):
    sum = 0
    for ingredient in self.ingredients:
      sum += ingredient.calories
    return sum


def main():
  print("Hello world!")
  salad_bowl = SaladBowl("my salad bowl", [])
  salad_bowl.add_ingredient(Kale())
  salad_bowl.add_ingredient(Chicken())
  salad_bowl.add_ingredient(Parmesan())
  print(f"price - ${salad_bowl.calculate_price()}")
  print(f"calories - {salad_bowl.calculate_calories()} cal")

if __name__ == "__main__":
  main()
