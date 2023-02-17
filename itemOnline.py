class Grocery_Item:
  def _init_(self, name, price, discount):
    self.name = name
    self.price = price
    self.has_discount = discount

  def display_info(self):
    print(self.name, "is $", self.price)

apple = Grocery_Item("apple", 1, False)
cheerios = Grocery_Item("cheerios", 4, True)

apple.display_info()
cheerios.display_info()
print("does", apple.name, "have a discount?", apple.has_discount)