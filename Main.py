from dataclasses import dataclass
from random import randint
import yaml

with open("./random_encounter.yaml","r") as f:
  data = yaml.safe_load(f)

@dataclass
class GameData():
    enounters: []
    
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
  r, event = rollRandomEncounter(gameState)
  print(f"Roll:{r} - {event['result']}")
def roll2d6():
    return (randint(1,6)+randint(1,6))
def rollRandomEncounter(gameState):
  roll = roll2d6()
  for entry in data["tables"]["test_encounters"]:
        if entry["roll"] == roll:
            return roll, entry
  return roll, None
  '''match outcome:
    case 1:
      print("test 1")
    case 2:
      print("test 2")
    case 3:
      print("3")
    case 4:
      print("4")
    case 5:
      print("Great news, you gained money!")
      gameState.player.funds += 5
      print("Gold on person:", gameState.player.funds)
    case 6:
      print("A gazebo attacks you")
    case 7:
      print("A bandit attacks you")
    case 8:
      print("Great news, you gained money!")
      gameState.player.funds += 5
      print("Gold on person:", gameState.player.funds)
    case 9:
      print("9")
    case 10:
      print("10")
    case 11:
      print("11")
    case 12:
      print("12")'''
      
def getRandomTreasure():
  outcome = randint(1,10)
  match outcome:
    case 1:
      print("Test")
  return 0

def endDayCycle(day, player):
  # Steps of a day
  print("As you sleep, the world at large continues to shift")
  player.health +=10
  print(f"It is now day {day.day+1}")
  day.day += 1
  #return day+1
  
def playerInput():
  playerInput = input()
  return playerInput()
  
def hurtSelf(target):
  target.health -= 1
  print("You hurt yourself, today")

def playerChoicesCombat():
  return 0
def playerChoicesOverworld(gameState):
  player = gameState.player
  day = gameState.timeTracking
  
  choice = input("What would you do today")
  match choice:
    case "Status":
      print("Health: ", player.health)
      print("Gold: ", player.funds)
      print("Day: ", day.day)
    case "Attack": 
      attack("Hah","Haah")
    case "Journey":
      gameExplore(gameState)
    case "Sleep":
      endDayCycle(day, player)
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
