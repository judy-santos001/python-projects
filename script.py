class Player:
  def _init_(self, name):
    self.name = name

class Computer(Player):
  def _init_(self):
    super()._init_("NPC")

  def respond(self, player):
    print("Hello", player.name, "I am", self.name)

class User(Player):
  def _init_(self, name, level):
    super()._init_(name)
    self.level = level

  def greet(self):
    print("Hi! What is your name?")

computer = Computer()
user = User("User", 1)
user.greet()
computer.respond(user)
print('hello')