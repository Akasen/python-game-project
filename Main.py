from dataclasses import dataclass
@dataclass
class GameState():
  def __init__(self):
    self.player = Character()
    self.timeTracking = GameTime()
    self.running = True
    
@dataclass
class Character():
  name: str = "Pinding"
  health: int = 10
  funds: int = 0
  reputation: int = 0

@dataclass
class GameTime():
  day: int = 1
@dataclass
class Item():
  name: str = "newItem"
  
  
def charCreation(player):
  print("Welcome to a fantastical world of no imagination.")
  print("What is your name?\n")
  player.name = input("")
  print("A fine name", player.name)
  return 0

def gameExplore(gameState):
  print("You go out into the world. Nothing happens to you because I don't have jack")

def rollRandomEncounter():
  print("A gazebo attacks")

def endDayCycle(day):
  # Steps of a day
  print("As you sleep, the world at large continues to shift")
  print("It is now day ",day+1)
  return day+1

def playerInput():
  playerInput = input()
  return playerInput()
  
def hurtSelf(target):
  target.health -= 1
  print("You hurt yourself, today")

def playerChoicesCombat():
  return 0
def playerChoicesOverworld(gameState):
  choice = input("What would you do today")
  match choice:
    case "Attack": 
      attack("Hah","Haah")
    case "Journey":
      gameExplore(gameState)
    case "Sleep":
      gameState.timeTracking.day = endDayCycle(gameState.timeTracking.day)
    case "Shop":
      print("What should have been a quick shopping trip turns into a 5 hour quandry of book flipping")
    case "Quit":
      print("Stop it, get help.")
    case _:
      print("Invalid Option Chosen")
  return 1
      
# Gamplay commands
def attack(attacker, target):
  print("You attacks", target)
# Gamplay commands end

def mainGameLoop(gameState):
  playerChoicesOverworld(gameState)
  # Main game loop
  return 0

def newGame(gameState):
  # Whenever the player starts a new day
  # Implement later?
  return 0

def main():
  gameState = GameState()
  # player = Character()
  #timeTracking = GameTime()
  
  charCreation(gameState.player)
  
  print("Testing: ", gameState.player.name)
  while(gameState.running):
    mainGameLoop(gameState)
main()