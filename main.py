from classes.game import bcolors, Person
from classes.magic import Spell
from classes.Inventory import Item

import random
import re

#create Black Magic

fire =Spell("Fire",25,600,"black")
thunder =Spell("Thunder",28,700,"black")
blizzard =Spell("Blizzard",30,800,"black")
meteor =Spell("Meteor",40,1200,"black")
quake =Spell("Quake",32,1000,"black")

#create white magic
# which will help us to heal and we will decide that by the help of spell type if we choose black magic it will destroy enemy and if we will chose white it will heal the player.
cure =Spell("Cure", 25, 620, "white")
cura =Spell("Cura",38,1500,"white")
curaga = Spell("Curaga",50,6000, "white")

#create some items

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("SuperPotion", "potion", "Heals 500 HP", 500)

elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member",9999)
hielixer = Item("Mega Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage ", 500)

player_spells=[fire,thunder,blizzard,meteor,cure,cura]
enemy_spells =[fire,meteor,curaga]
#make  a list of dictionaries where items should have certain quantites


player_items =[{"item" :potion, "quantity": 15},{"item" :hipotion, "quantity": 5},
                {"item" :superpotion, "quantity": 5},{"item" :elixer, "quantity": 5},
                {"item" :hielixer, "quantity": 2},{"item" :grenade, "quantity": 5}]


# Instantiate Players
player1= Person("THOR ",2330,132,260,34,player_spells,player_items)
player2= Person("TONY ",4620,188,360,34,player_spells,player_items)
player3= Person("FLASH",4630,165,300,34,player_spells,player_items)

#Making the List of PLayers

players =[player1,player2,player3]

#Instantiate Enemies
enemy1 = Person("Imp  ",3200,132,300,325,enemy_spells,[])
enemy2 = Person("Vagus",12000,701,545,25,enemy_spells,[])
enemy3 = Person("Cric ",8000,180,555,325,enemy_spells,[])

#making a list of enemies

enemies = [enemy1,enemy2,enemy3]

running = True

# This print statement is just used for coloring the text so that our applicatio will look better
#If we need to color we also need to stop it so bcolors.ENDC is used
print(bcolors.FAIL + bcolors.BOLD + "RPG Combat Script Game" + bcolors.ENDC)
print(bcolors.OKGREEN + bcolors.BOLD + "Lets start the game :" + bcolors.ENDC)



while running :
    print("================================================================================================")
    print("\n\n")
    print(bcolors.FAIL + bcolors.BOLD + "NAME                        " + bcolors.ENDC + bcolors.BOLD + bcolors.OKGREEN+  "HP                                     "+ bcolors.ENDC + bcolors.OKBLUE + bcolors.BOLD + "  MP" + bcolors.ENDC)

    #To print each the player stats everytime we play
    for player in players:
        player.get_stats()
    print()
    for enemy in enemies:
        enemy.get_enemy_stats()
    print()
    for player in players:
        print()
        print(bcolors.OKGREEN + bcolors.BOLD + player.name + ":"+bcolors.ENDC )
        player.choose_action()
        choice = int(re.sub('[a-zA-Z]' , '8' , input("Choose Action: ")))
        index =int(choice)-1

        if index == 0 :
            dmg=player.generate_damage()
            player.choose_target(enemies)           # To choose the target which enemy player wants to attack
            # Taking Input from the User which enemy it wants to attack
            enemy = int(re.sub('[a-zA-Z]','9',input("    Choose Target:"))) - 1
            if enemy >= len(enemies) or enemy < 0:
                print("Wrong choice selected Your chnace missed Try next tym")
                continue
            enemies[enemy].take_damage(dmg)
            print("You attack for ", dmg, "points of damage on ",enemies[enemy].name)

            if enemies[enemy].get_hp() == 0 :
                print(enemies[enemy].name, "has died.")
                del enemies[enemy]

            if len(enemies) == 0:
                print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
                running = False
                break
        elif index == 1:
            player.choose_magic()
            print("        If you want to go to the previous menu Press 0\n")
            magic_choice = int(re.sub('[a-zA-Z]','9', input("Choose Magic : ") )) - 1    #Indexing starts with 0 so -1

            if magic_choice < 0 or magic_choice >= len(player.magic) :
                print("Wrong choice selected. You miss your chance ")
                continue

            current_mp = player.get_mp()  #Mp is the total magic power if player uses the spell the mp gets reduced by its cost.

            #checking wheather it has sufficient money or not to buy the spell
            spell = player.magic[magic_choice]
            if spell.cost > current_mp :
                print(bcolors.FAIL + "\nNot Enough MP Your Chance missed\n" + bcolors.ENDC)
            else:
                magic_dmg =spell.generate_damage()

                #reducing the cost to buy the spell

                player.reduce_mp(spell.cost)
                #if the type is white player will heal and if type is black  it will attack enemy. so

                if spell.type =="white":
                    player.heal(magic_dmg)
                    print(bcolors.OKBLUE + '\n'+ spell.name + ' heals for', str(magic_dmg),"HP" + bcolors.ENDC)
                elif spell.type == 'black':
                    #Now enemy will take the damage
                    # Taking Input from the User which enemy it wants to attack
                    player.choose_target(enemies)
                    enemy = int(re.sub('[a-zA-Z]', '9', input("    Choose Target:"))) - 1
                    if enemy >= len(enemies) or enemy < 0:
                        print("Wrong choice selected Your chnace missed Try next tym")
                        continue
                      # To choose the target which enemy player wants to attack
                    enemies[enemy].take_damage(magic_dmg)
                    print(bcolors.OKBLUE + " \n" + spell.name + " deals", str(magic_dmg),"points of damage on ",enemies[enemy].name + bcolors.ENDC)
                    if enemies[enemy].get_hp() == 0:
                        print(bcolors.OKBLUE+ enemies[enemy].name, "has died." + bcolors.ENDC)
                        del enemies[enemy]

                if len(enemies) == 0:
                    print(bcolors.OKGREEN + "You Win!" + bcolors.ENDC)
                    running = False
                    break

        elif index == 2:
            player.choose_item()
            item_choice = int(re.sub('[a-zA-Z]','9',input("Enter choice:")))-1

            if item_choice >= len(player.items) or item_choice < 0 :
                print("Wrong Choice You missed your chance of attack this time.")
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0 :
                print(bcolors.FAIL+ "\n" + "Not Available Yor chance missed"+ bcolors.ENDC)

            else :

                player.items[item_choice]["quantity"]-=1         #To decrese the quantiy of item when it is used

                if item.type == "potion" :
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + '\n'+ item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

                elif item.type == "elixer":
                    if item.name =="Elixer":
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print(bcolors.OKBLUE + '\n' + item.name + " Fully restores HP/MP of "+ player.name + bcolors.ENDC)

                    elif item.name == "Mega Elixer":
                        for i in players :
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                        print(bcolors.OKBLUE + '\n' + item.name + " Fully restores HP/MP of all the Players " + bcolors.ENDC)


                elif item.type == "attack":
                    player.choose_target(enemies)  # To choose the target which enemy player wants to attack
                    enemy = int(re.sub('[a-zA-Z]', '9', input("    Choose Target:"))) - 1
                    if enemy >= len(enemies) or enemy < 0:
                        print("Wrong choice selected Your chnace missed Try next tym")
                        continue
                    enemies[enemy].take_damage(item.prop)
                    print(bcolors.FAIL + '\n' + item.name + " deals " + str(item.prop),"Points of damage on ", enemies[enemy].name + bcolors.ENDC)
                    if enemies[enemy].get_hp() == 0:
                        print(bcolors.OKBLUE + enemies[enemy].name , "has died." + bcolors.ENDC)
                        del enemies[enemy]
        else :
            print("Wrong choice selected OOPS Your Chance Missed ")

    #Check if all enemies are dead and you won

    if len(enemies) == 0:
        print(bcolors.OKGREEN + "You Win!"+ bcolors.ENDC)
        running = False
        continue

    #Enemy Phase
    print()
    for enemy in enemies:
        if enemy.mp < 25 :
            enemy_choice = 0
        else :
            enemy_choice = random.randrange(0,2)

        if enemy_choice == 0 :
            target = random.randrange(0,len(players))
            enemy_dmg=enemy.generate_damage()

            #Now we have to create a logic to decide which player gets attacked by enemy.

            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name +" attacks for", enemy_dmg, "Points of damage on ", players[target].name + bcolors.ENDC)

            if players[target].get_hp() == 0 :
                print(bcolors.FAIL + players[target].name, "has died." + bcolors.ENDC)
                del players[target]

            if len(players) == 0:
                print(bcolors.FAIL + "Your enemies have defeated you. ! You Lose!" + bcolors.ENDC)
                running = False
                break

        elif enemy_choice == 1 :
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.FAIL + '\n' + enemy.name + ' heals',spell.name,' for', str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == 'black':
                target = random.randrange(0, len(players))
                players[target].take_damage(magic_dmg)
                print(bcolors.FAIL+ enemy.name +" attacks for", magic_dmg, "Points of damage on ", players[target].name, 'with ', spell.name , 'for', str(magic_dmg),'HP' + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(bcolors.FAIL+players[target].name, "has died." + bcolors.ENDC)
                    del players[target]


                if len(players) == 0 :
                    print(bcolors.FAIL + "Your enemies have defeated you. ! You Lose!" + bcolors.ENDC )
                    running = False

