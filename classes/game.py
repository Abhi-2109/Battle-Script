#This will contain two classes colors for terminals and class person for enemies and for ourself character

import random

#color class

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    #we need to initailse it with some stats ie hitpoints, attack power, defence , magic etc
    # hp-> Hitpoints,mp->magic points atk->Attack Power df->Defence magic->magic spells
    #magic is a list of dictionaries which conatin different spells with their properties like name, cost, damage

    def __init__(self,name, hp, mp, atk, df, magic,items):
        self.maxhp = hp   #maximum hit points of the characer
        self.hp = hp    #This will be changed during the game
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10     #atkl---> attack low (lower bound of attcaking powwer)
        self.atkh = atk + 10    #atkh--->Heigher bound of attacking power
        self.df = df
        self.magic = magic  #It will conatin a dictionary of different magic spells we have
        self.items = items
        self.action = ["Attack", "Magic", "Items"]
        self.name=name

    # Now we need to create some utility methods to handle diffrent actions that we can anticipate during the battle

    # So we want our player and the ememy to take the damage. So in order to genertate the damage we will use random
    # The following two function will genertae regular damage and spell damge
    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)    #It will choose a random number between attack high and attack low

    #Now do the same things for spell damage. So lets create some of the spells.
    #it is done in spell class

    #Now create a function to heal the player

    def heal(self,point):
        self.hp += point
        if self.hp > self.maxhp :
            self.hp = self.maxhp


    #Now we will create a function that take damage

    def take_damage(self,dmg):
        self.hp -= dmg              #we decrease the hp by dmg

        #if self hp becomes neagtive we need to assign it to zero
        if self.hp < 0 :
            self.hp =0

        return self.hp

    #Additional utility functions

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    #Now when we use the spells it will take a cost so we need to reduce the magic point ie. mp

    def reduce_mp(self,cost):
        self.mp -= cost


    #Now we need two methods to choose between magic and attack.
    # One more function to choose which spells we use for the magic

    def choose_action(self):
        i=1
        print(bcolors.OKBLUE + bcolors.BOLD +"    Action " + bcolors.ENDC)
        for item in self.action:
            print("        " + str(i)+":",item)
            i+=1
        print()

    def choose_magic(self):
        i=1
        print("\n"+bcolors.OKBLUE + bcolors.BOLD+ "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic :
            print("        " + str(i)+":",spell.name,"(cost:",str(spell.cost)+", damage: " + str( spell.dmg ), ")")
            i+=1
        print()

    def choose_item(self):
        i=1
        print("\n"+bcolors.OKGREEN + bcolors.BOLD +"    ITEMS: " + bcolors.ENDC)
        for item in self.items :
            print("        " + str(i)+".",item["item"].name,':', item["item"].description, " (x" + str(item["quantity"]) +" )")
            i+=1
        print()

    def choose_target(self,enemies):
        i=1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET: " + bcolors.ENDC)
        for enemy in enemies :
            print("        " + str(i)+"." + enemy.name)
            i+=1


    def get_stats(self):
        #making logic for the spaces and color to fill

        hp_bar=""
        bar_ticks = (self.hp/self.maxhp)*100/4

        while bar_ticks > 0:
            hp_bar +='█'
            bar_ticks-=1
        while len(hp_bar)<25:
            hp_bar+=' '

        #same logic for mp_bar

        mp_bar =""
        mp_ticks = (self.mp / self.maxmp)*10

        while mp_ticks > 0 :
            mp_bar +="█"
            mp_ticks-=1

        while len(mp_bar) < 10 :
            mp_bar+=' '
        # To check for the spaces if hp aur mp lenth varies

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        while len(hp_string) < 9 :
            hp_string = " " + hp_string

        mp_string = str(self.mp) + '/' + str(self.maxmp)
        while len(mp_string) < 7:
            mp_string = " "+ mp_string


        print("                            _________________________                __________ ")
        print( bcolors.BOLD + self.name +":            "+hp_string+"|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|       " + mp_string +"|" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    def get_enemy_stats(self):
        hp_string = str(self.hp)+'/'+str(self.maxhp)
        while len(hp_string) < 11 :
            hp_string = ' ' + hp_string

        hp_ticks = int((self.hp/self.maxhp)*50)

        hp_bar = '█'*hp_ticks
        while len(hp_bar) < 50 :
            hp_bar +=' '

        print("                            __________________________________________________")
        print(bcolors.BOLD + self.name + ":          " + hp_string + "|" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        pct = (self.hp / self.maxhp )*100
        ctr =0
        if (self.mp < spell.cost) or (spell.type =="white" and pct >= 50):
            return self.choose_enemy_spell()
        else :
            return spell, magic_dmg