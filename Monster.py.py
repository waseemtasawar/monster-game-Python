import random
import time

from abc import ABC, abstractmethod


class Monster(ABC):

    
    
    @abstractmethod
    def __init__(self,name, health=100, description = 'Dangrous', basicAttackDamage=0, specialAttackDamage=0, defenseDamage=0, basicAttackName='BasicAttack', specialAttackName='speciaAttack', defenseName='DefenceAttack'):
        pass
        
    @abstractmethod 
    def __str__(self):
        pass
        
    
    @abstractmethod 
    def getName(self):
        pass
        
    @abstractmethod
    def getDescription(self):
        pass
        
    
    @abstractmethod 
    def basicAttack(self,enemy):
        pass
    
    # Print the name of the attack used
    @abstractmethod 
    def getBasicName(self):
        pass
    #Get the basic attack damage amount.
    @abstractmethod
    def getBasicAttackDamage(self):
        pass
    
    
    @abstractmethod 
    def defenseAttack(self,enemy):
        pass
        
    #Print out the name of the attack used
    @abstractmethod 
    def getDefenseName(self):
        pass
    #Get the defnse attack damage amount
    @abstractmethod
    def getDefenseAttackDamage(self):
        pass
        
 
    @abstractmethod 
    def specialAttack(self,enemy):
        pass
        
    #get the special attack's name
    @abstractmethod 
    def getSpecialName(self):
        pass
    
    #get the special attack damage amount
    @abstractmethod
    def getSpecialAttackDamage(self):
        pass    
    
   
    @abstractmethod 
    def getHealth(self):
        pass
    
    #This returns the maximum health set at creation.
    @abstractmethod
    def getMaximumHealth(self):
        pass
   
    @abstractmethod 
    def doDamage(self,damage):
        pass
        
    #Reset Health for next match
    @abstractmethod 
    def resetHealth(self):
        pass

class CustomMonster(Monster):
    def __init__(self, n, health=100, description = 'Dangrous', basicAttackDamage=0, specialAttackDamage=0, defenseDamage=0, basicAttackName='BasicAttack', specialAttackName='specialAttack', basicDefenseName='Defence'):
        self.__name = n
        self.__maximumHealth = int(health)
        self.__health = int(health)
        self.__description = description
        self.__basicAttackDamage = basicAttackDamage
        self.__specialAttackDamage = specialAttackDamage
        self.__defenseDamage = defenseDamage
        self.__basicAttackName = basicAttackName
        self.__specialAttackName = specialAttackName
        self.__basicDefenseName = basicDefenseName
        
    def __str__(self):
        return "{}".format(self.__description)
    
    def getName(self):
        return "{}".format(self.__name)
    
    def getDescription(self):
        return "{}".format(self.__description)
    
    def getBasicName(self):
        return "{}".format(self.__basicAttackName)
    
    def getBasicAttackDamage(self):
        return self.__basicAttackDamage
    
    def getDefenseName(self):
        return "{}".format(self.__basicDefenseName)
    
    def getDefenseAttackDamage(self):
        return self.__defenseDamage
    
    def getSpecialName(self):
        return "{}".format(self.__specialAttackName)
    
    def getSpecialAttackDamage(self):
        return self.__specialAttackDamage
    
    def getHealth(self):
        return self.__health
    
    def getMaximumHealth(self):
        return self.__maximumHealth
    
    def doDamage(self, damage):
        self.__health = self.__health - damage
        
    def basicAttack(self, enemy):
        enemy.doDamage(self.getBasicAttackDamage())
    
    def defenseAttack(self, enemy):
        enemy.doDamage(self.getDefenseAttackDamage())
    
    def specialAttack(self, enemy):
        enemy.doDamage(self.getSpecialAttackDamage())
        
    def resetHealth(self):
        self.__health = self.__maximumHealth
 

def Playing():
   # player Data entring
    Playername = input("Enter Player name(string): ")
    Playerhealth = int(input("\nEnter player  health(integer): "))
    Playerdescription = input("\nEnter Player description(string): ")
    basic = int(input("\nDamage of basic attack of Player(integer): "))
    special = int(input("\nDamage of special attack of Player(integer): "))
    defence = int(input("\ndamage of Defense attack of Player(integer): "))
    PlayerBasicAttackName = input("\nName of basic attack of player(string): ")
    PlayerspecialAttackName = input("\nName of special attack of Palyer(string): ")
    PlayerdefenceAttackName = input("\nName of  defense Attack of player(string): ")
    Player = CustomMonster(Playername, Playerhealth, Playerdescription, basic, special, defence, PlayerBasicAttackName, PlayerspecialAttackName, PlayerdefenceAttackName)  #this should be an instance of your CustomMonster class
        
    # Monster Data entring
    Monstername = input("\nEnter Monster name(string):")
    Monsterhealth = int(input("\nEnter Monster  health: "))
    Monsterdescription = input("\nEnter Monster description:")
    Mbasic = int(input("\nDamage of basic attack of Monster: "))
    Mspecial = int(input("\nDamage of special attack of Monster: "))
    Mdefence = int(input("\ndamage of Defense attack of Monster: "))
    MonsterBasicAttackName = input("\nName of basic attack of Monster: ")
    MonsterpecialAttackName = input("\nName of special attack of Monster: ")
    MonsterfenceAttackName = input("\nName of  defense Attack of Monster: ")
    Monster = CustomMonster(Monstername, Monsterhealth, Monsterdescription, Mbasic, Mspecial, Mdefence, MonsterBasicAttackName, MonsterpecialAttackName, MonsterfenceAttackName)  #this should be an instance of your CustomMonster class
  
    winner = monster_battle(Player,Monster)

#This function has two monsters fight and returns the winner
def monster_battle(p, m):

    #first reset everyone's health!
    #####TODO######
    p.resetHealth
    m.resetHealth

    #next print out who is battling
    print("\nStarting Battle Between")
    print(p.getName()+": "+p.getDescription())
    print(m.getName()+": "+m.getDescription())
    
    
    #Whose turn is it?
    attacker = None
    defender = None
    
 
    rand = random.randint(0,1)
    if rand == 0:
        attacker = p
        defender = m
    else :
        attacker = m
        defender = p
    
    print(attacker.getName()+" goes first.")
    #Loop until either monster is unconscious (health < 1) or choose to stop.
    while( p.getHealth() > 0 and m.getHealth() > 0):
        #Ask the user a move among special attack, basic attack, defense or the stop.
        move = input('Pick one of these (s)Special attack, (b)Basic attack, (d)Defense or (p)To Stop Battle:')        

        #It will be nice for output to record the damage done
        before_health=defender.getHealth()
        
 
        #basic attack
        if( move.lower() == "b"):
            # Attacker uses basic attack on defender 

            ######TODO######
            attacker.basicAttack(defender)
            print_results(attacker, defender, attacker.getBasicName(), attacker.getBasicAttackDamage())
        #defense attack
        elif move.lower() == "d":


            attacker.defenseAttack(defender)
            print_results(attacker, defender, attacker.getDefenseName(), attacker.getDefenseAttackDamage())
        #special attack
        elif move.lower() == "s":


            attacker.specialAttack(defender)
            print_results(attacker, defender, attacker.getSpecialName(), attacker.getSpecialAttackDamage())
        elif move.lower() == "p":
            #stop the fight
            break
        
        #Swap attacker and defender

        temp = attacker
        attacker = defender
        defender = temp
        
        #Print the names and healths after this round
        defenderName = defender.getName()
        defenderHeath = str(defender.getHealth())
        print("{} at {}".format(defenderName, defenderHeath))
        
        attackername = attacker.getName()
        attackerhealth = str(attacker.getHealth())
        print("{} at {}".format(attackername, attackerhealth))
                   
    # Print out who won.
    if p.getHealth() > m.getHealth():
      
        print("{} The Winner is! ".format(p.getName()))
        victor = p
    else :
   
        print("{} The Winner is! ".format(m.getName()))
        victor = m
        
    
    return victor


def print_results(attacker,defender,attack,hchange):
    
    attackerName = attacker.getName()
    defenderName = defender.getName()
    dmg = str(hchange)
    
    print("{} used {} on {}".format(attackerName, attack, defenderName))
    print("The attack did {} damage.".format(dmg))

#----------------------------------------------------
if __name__=="__main__":
    #Ideally every battle will be differen
    
    random.seed(0)
    Playing()