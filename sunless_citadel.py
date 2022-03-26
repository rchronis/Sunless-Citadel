from sys import exit
import random
from tkinter.messagebox import YESNOCANCEL


def d20_roll():
    print("What is your modifier?")
    mod = int(input("~ "))
    roll = random.randint(1,20)
    return mod + roll


def d12_roll():
    print("What is your modifier?")
    mod = int(input("~ "))
    roll = random.randint(1,12)
    return mod + roll


def d10_roll():
    print("What is your modifier?")
    mod = int(input("~ "))
    roll = random.randint(1,10)
    return mod + roll


def d8_roll():
    print("What is your modifier?")
    mod = int(input("~ "))
    roll = random.randint(1,8)
    return mod + roll


def d6_roll():
    print("What is your modifier?")
    mod = int(input("~ "))
    roll = random.randint(1,6)
    return mod + roll


def d4_roll():
    print("what is your modifier?")
    mod = int(input("~ "))
    roll = random.randint(1,4)
    return mod + roll


def d100_roll():
    roll = random.randint(1,100)
    return roll


def character_attack():
    print("It is your turn to attack.")
    roll = d20_roll()
    print(roll)
    return roll

def room_12():
    print("""
    Violet marble tiles cover the floor and walls,
    though all are cracked or broken,
    reavealing the rough- hewn stone beneath.

    Sconces are attached to the walls at each corner.
    one holds a torch that burns greenish fire.

    A marble sarcophagus, easily nine feet long, lie's in the room's center
    The coffin is carved with dragon imagery,
    amd the head of the sarcophagus resembles a dragon's head.
    Rusting iron clasps firmly lock down the lid.\n""")
    print("What do you do?")

    choice = input("~ ")
    if "torch" in choice:
        print("The greenish fire is a CONTINUAL FLAME spell.\n")
        room_12()
    elif "sarcophagus" in choice:
        print("""\tSix rusted iron latches hold down the sarcophagus lid.
        Opening a single latch requires a STR [DC 15] check.""")
        first_latch()
    else:
        print("I don't know what that means.")

def first_latch():
    print("Can you get the first latch open?")
    latch_one = d20_roll()
    if latch_one >= 15:
        print("Congratulations! Only 5 to go!")
        second_latch()
    else:
        print("Oh no! Maybe try again?")
        first_latch()

def second_latch():
    print("Can you get the second latch done now?")
    latch_two = d20_roll()
    if latch_two >= 15:
        print("Congratulations! Only 4 more to go!")
        third_latch()
    else:
        print("Oh no! Maybe Try again?")
        second_latch()

def third_latch():
    print("Can you get the third latch open?")
    latch_three = d20_roll()
    if latch_three >= 15:
        print("Congratulations! Only 3 more to go!")
        fourth_latch()
    else:
        print("On no! Maybe try again?")
        third_latch()

def fourth_latch():
    print("Can you get the fourth latch open?")
    latch_four = d20_roll()
    if latch_four >= 15:
        print("Congratulations! Only 2 more to go!")
        fifth_latch()
    else:
        print("Oh no! Maybe try again?")
        fourth_latch()

def fifth_latch():
    print("Can you get the fifth latch open?")
    latch_five = d20_roll()
    if latch_five >= 15:
        print("Congratulations! Only 1 more to go!")
        sixth_latch()
    else:
        print("Oh no! Maybe try again?")
        fifth_latch()

def sixth_latch():
    print("Can you get the last latch open?")
    latch_six = d20_roll()
    if latch_six >= 15:
        print("Congratulations! You've opened the sarcophagus!")
        sarcophagus()
    else:
        print("Oh no! Maybe try again?")
        sixth_latch()

def sarcophagus():
    print("""
    A flash of green light flares when the sarcophagus is opened.
    In the coffin is a troll!
    It's dressed in rotted finery, but its jewelry and rings adorned with
    tiny silver dragons still sparkle.
    The creature's body is shrunken and elongated,
    and it's flesh is a rubbery, putrid green.
    its black hair is long, thick and ropy.
    Its beady black eyes flash open, and it snarls.\n""")
    troll()

def room_12treasure():
    print("""
    The dragon priest has an ornate ceremonial dagger [worth 125 gp],
    two silver rings [worth 15 gp each], and a silver amulet [worth 15 gp].
    Scattered across the sarcophagus is 220 sp, 50 gp and four spell scrolls.
    The scrolls are for:
    COMMAND
    CURE WOUNDS
    INFLICT WOUNDS
    GUIDING BOLT""")
    print("\nRoll a perception check to see if there's anything else in the room.")
    perception = d20_roll()
    if perception >= 20:
        print("""
        There is a trapdoor on the floor.
        The door opens by pulling upward.
        It leads to a 3x3 foot crawl space.""")
        print("You crawl down the passageway.")
        room_11()
    else:
        print("There is nothing else in the room.")

def troll_attack():
        print("The troll swipes it's claws at you.")
        claws = random.randint(1,20) + 7
        print(f"Does {claws} hit you?")
        ans = input("~ ")
        if 'yes' in ans:
            print("You take 11 damage.")
        elif 'no' in ans:
            print("He missed, and it's a good thing too. That looked dangerous.")
        roll = character_attack()
        if roll >= 15:
            print("You hit! Miracuously, you kill it!")
            room_12treasure()
        else:
            print("Oh no, you missed. That's not good.")
            troll_attack()

def troll():
    print("The troll tries to eat your face.")
    first_attack = random.randint(1,20) + 7
    print(f"Does {first_attack} hit you?")
    ans = input("~ ")
    if 'yes' in ans:
        print("You take 7 damage.")
        troll_attack()
    elif 'no' in ans:
        print("He missed, and boy does his breath smell BAD.")
    roll = character_attack()
    if roll >= 15:
        print("You hit the troll! Good job!")
        print("It wasn't enough though...")
        troll_attack()
    else:
        print("Uh Oh, You missed. That's not good.")
        troll_attack()


def room_11():
    print("""
    Dust coats the contents of this tiny chamber,
    obscurring runes inscribed on the southern wall.""")

    print("What would you like to do?")
    ans = input("~ ")
    if 'runes' in ans:
        print("Do you speak Draconic?")
        draconic = input("~ ")
        if 'yes' in draconic:
            print("""It says:
            A dragonpriest entombed alive for transgressions of the Law
            still retains the honor of his position.""")
            room_11()
        else:
            print("You've no idea what it says.")
            room_11()
    else:
        print("Roll a perception check to see if there's anything else in the room.")
        perception = d20_roll()
        if perception >= 20:
            print("""There is a trapdoor on the floor.
            The door opens by pulling upward.
            It leads to a 3x3 foot crawl space.""")
            room_10()
        else:
            print("There is nothing else in the room.")

def room_10():
    print("""
    Dust cloaks the contents of this twenty-foot-wide hall.
    Six alcoves line the walls, three to the north and three to the south.
    Each alcove except the southwest one holds a humanoid figure
    carved of red-veined white marble.
    The figures resemble tall elves in plate armor.
    A stone archway at the west end of the hall opens into a wide room
    from which a greenish light grows.
    A dark pit is situation before the archway.""")

    print("What would you like to do?")
    ans = input("~ ")
    if 'southwest' in ans:
        print("Roll perception.")
        perception = d20_roll()
        if perception >= 10:
            print("""
            Dust in the room is disturbed by tracks
            that start in the southwest alcove,
            though the tracks are filled in enough
            to have occured dozens of years ago.""")
            room_10()
        else:
            print("You find nothing of significance.")
            room_10()
    elif ' alcove' in ans:
        print("Roll perception.")
        perception = d20_roll()
        if perception >= 10:
            print("""
            Dust in the room is disturbed by tracks
            that start in the southwest alcove,
            though the tracks are filled in enough
            to have occured dozens of years ago.""")
            room_10()
        else:
            print("You find nothing of significance.")
            room_10()
    elif 'pit' in ans:
        print("""
        The pit is 10 feet deep, and it's bottom is filled with spikes.
        The walls of the pit are rough,
        and they offer handholds to climbers.""")
        room_10pit()
    elif 'search' in ans:
        print("Roll perception.")
        perception = d20_roll()
        if perception >= 20:
            print("You find a secret door! The door opens with a simple push.")
            room_11()
        else:
            print("You found nothing of significance.")
            room_10()
    else:
        print("There is nothing of significance.")
        room_10()


def room_10pit():
    print("Are you using light to guide your path?")
    ans = input("~ ")
    if 'yes' in ans:
        quasit_ready = True
    else:
        quasit_ready = False

    print("Roll athletics to climb down the pit without falling.")
    athletics = d20_roll()
    if athletics >= 10:
        print("You successfully make it to the bottom.")
    else:
        print("You fall. Take 11 damage.")

    print("Roll another athletics to climb up without falling.")
    athletics = d20_roll()
    if athletics >= 10:
        print("You successfully make it to the top.")
        if quasit_ready == True:
            print("When you reach the top, a creature attacks you.")
            quasit_attack()
    else:
        print("You fall and take 11 damage. Then climb to the top.")
        if quasit_ready == True:
            print("When you reach the top, a creature attacks you.")
            quasit_attack()
    print("""
    Once you step foot on the other side you hear breathing,
    looking above you, you see a tiny green creature clinging to the arch.
    It has long horns on the top of it's head, and large black eyes.
    When it sees you it growls meanacingly.""")
    print("Roll a Wisdom save to not be frightened.")
    wisdom = d20_roll()
    if wisdom >= 10:
        print("Congratulations! You are not frightened.")
    else:
        print("Oh no! It's presence terrifies you.")
        print("This allows the creature to attack you immediately.")
        quasit_attack()

    roll = character_attack()
    if roll >= 13:
        print("You hit it! Good job!")
        print("It looks less than happy.")
        quasit_attack()
    else:
        print("You missed. That's not good.")
        quasit_attack()




def quasit_attack():
    print("The tiny creature attempts to hit you with it's claws.")
    attack_roll = random.randint(1,20) + 4

    print(f"Does a {attack_roll} hit you?")
    ans = input("~ ")
    if 'yes' in ans:
        print("You take 5 damage, and 5 poison damage.")
    elif 'no' in ans:
        print("It missed, what luck!")
    roll = character_attack()
    if roll >= 13:
        print("You hit! Congratulations!")
        print("It makes a horrible shriek as it dies.")
        room_12()
    else:
        print("You missed, unfortunately.")
        quasit_attack()


def room_9():
    print("""
    Dust fills this hall like a layer of gray snow.
    In the rounded northern end of the chamber stands a ten- foot- tall sculpture
    of a coiled dragon carved from a red-viened white marble.""")
    print("What do you do?")
    ans = input("~ ")
    if 'dragon' in ans:
        dragon_riddle()
    else:
        print("Roll a perception check.")
        perception = d20_roll()
        if perception >= 20:
            print("You find a door!")
            print("With a simple push you go into the next room.")
            room_10()
        else: 
            print("There is nothing significant here.")



def dragon_riddle():
    print("""
        As you move within 5 feet of the sculpture,
        the mouth opens to utter the following riddle in Common:
        \tWe come at night without being fetched;
        \twe disappear by day without being stolen.
        \tWhat are we?""")
    ans = input("~ ")
    if ans == 'stars':
        print("When you say stars aloud a door to your right opens.")
        room_10()
    else:
        print("Nothing seems to happen.")

def room_8():
    print("""
    The air is stale in this twenty- foot- long corridor,
    which leads to another closed door.""")
    print("What do you do?")
    ans = input("~ ")
    if 'search' in ans:
        print("Roll investigation.")
        investigation = d20_roll()
        if investigation >= 15:
            print("You see a pressure plate in the center of the room.")
            print("To get 'around' it you'll have to disable it.")
            room_8trap()
        else:
            print("You step on a pressure plate and an arrow shoots at you.")
            print("You take 5 damage.")
            print("You otherwise walk tot he next room.")
            room_9()
    else:
        print("You step on a pressure plat in ther center of the room.")
        print("You take 5 damage from an arrow that shoots you.")
        print("You otherwise walk to the next room.")
        room_9()

def room_8trap():
    print("Roll another intelligence.")
    intelligence = d20_roll()
    if intelligence >= 15:
        print("You put a piece of debris under the plate to keep it from triggering.")
        print("You walk throught the room ot the next.")
        room_9()
    else:
        print("While fiddling with it you set off the trap.")
        print("You take 5 damage from an arrow.")
        print("Since that's triggered you can walk to the next room.")
        room_9()

def room_7():
    print("""
    As the door opens, a hissing noise and a puff of dust
    around the door indicate that the chamber beyond
    has been sealed for ages.
    Dust, long undisturbed, covers every surface in this large gallery.
    The air here is stale.
    Three alcoves are on the north wall, and one is on the south wall.
    Each alcove contains a dust- covered stoen pedestal with a fist-size 
    crystalline globe resting on it.
    The globes in the northern alcoves are cracked and dark,
    but the globe in the southern alcove glows a soft blue light.
    Faint tinkling notes issue from it.""")
    print("What do you do?")
    ans = input("~ ")
    if 'globe' in ans:
        room_7globe()
    else:
        print("There is nothing of significance in this room.")
        room_8()

def room_7globe():
    print("Brooding music starts to play throughout the area.")
    print("Roll wisdom.")
    wisdom = d20_roll()
    if wisdom >= 15:
        print("""You know that the music was trying to chartm you and
        dissuade you from going any further into this dungeon.""")
        print("Unaffected, you m,ove to the next room.")
        room_8()
    else:
        print("You immediately walk out of this area.")

def room_6():
    print("""
    The masonry walls of this twenty- foot- wide hall are in poor repair.
    The far end has collapsed,
    filling the southern section with rubble.
    The western wall is in much better shape than the other walls,
    amd hp;ds a stone door with a rearing dragon carved in relief on it.
    The door has a single keyhole, situated in the rearing dragon's open mouth.""")
    print("In the center of the room, there is a rat.")
    rat_attack()

def rat_attack():
    print("The large rat attempts to bite you.")
    attack = random.randint(1,20) + 4
    print(f"Does a {attack} hit you?")
    ans = input("~ ")
    if 'yes' in ans:
        print("It bites you for 4 damage.")
    elif 'no' in ans:
        print("It missed, thankfully.")
    roll = character_attack()
    if roll >= 7:
        print("You hit, and it kills the rat.")
        dragon_door()
    else:
        print("You miss. That's not good.")
        rat_attack()

def dragon_door():
    print("You move to the door and inspect it.")
    print("Are going to use stength, thievery, or a spell to open the door?")
    ans = input("~ ")
    if 'strength' in ans:
        print("Roll strength.")
        strength = d20_roll()
        if strength >= 20:
            print("The door opens and you walk inside.")
            room_7()
        else:
            print("You do not open the door.")
            dragon_door()
    elif 'thievery' in ans:
        print("Roll sleight of hand.")
        sleight = d20_roll()
        if sleight >= 18:
            print("The door opens and you walk inside.")
            room_7()
        else:
            print("The door does not open.")
            dragon_door()
    elif 'spell' in ans:
        print("Roll sleight of hand.")
        sleight = d20_roll()
        if sleight >= 10:
            print("The door opens and you walk inside.")
            room_7()
        else:
            print("You cannot open the door.")
            dragon_door()

def room_5():
    print("""
    This chamber is damp and cold.
    The skeletons of three long- dead archers slump against
    rubble filled arrow slits along the east and south wall.""")
    print("""
    Immediately after surveying the room the 3 skeletons animate,
    They're eyes are red as they file in a line to attack you.""")
    skeleton_1()

def skeleton_1():
    print("The skeleton shoots an arrow at you.")
    attack = random.randint(1,20) - 4
    print(f"Does a {attack} hit you?")
    ans = input("~ ")
    if 'yes' in ans:
        print("It manages to hit you!")
        print("Take 5 damage.")
    else:
        print("It missed, thankfully.")
    roll = character_attack()
    if roll >= 13:
        print("You hit! And it dies. Good job.")
        skeleton_2()
    else:
        print("You missed, that's not good.")
        skeleton_1()

def skeleton_2():
    print("This skeleton pulls it's longsword on you.")
    attack = d20_roll() + 4
    print(f"Does a {attack} hit you?")
    ans = input("~ ")
    if 'yes' in ans:
        print("It manages to hit you.")
        print("Take 5 damage.")
    else:
        print("It missed, thankfully.")
    roll = character_attack()
    if roll >= 13:
        print("You hit! And it dies! Good job.")
        skeleton_3()
    else:
        print("You missed, that's not good.")
        skeleton_2()
    
def skeleton_3():
    print("This skeleton pulls it's longsword on you.")
    attack = d20_roll() + 4
    print(f"Does a {attack} hit you?")
    ans = input("~ ")
    if 'yes' in ans:
        print("It manages to hit you.")
        print("Take 5 damage.")
    else:
        print("It missed, thankfully.")
    roll = character_attack()
    if roll >= 13:
        print("You hit! And it dies! Good job.")
        skeleton_treasure()
    else:
        print("You missed, that's not good.")
        skeleton_3()

def skeleton_treasure():
    print("""
    Each skeleton has 20 arrows [60 total].
    Additionally each has one +1 magic arrow.
    They also carry 1 rusty longsword each.
    You find 3 gp and 14 cp strewn about the room.""")
    room_4()

def room_4():
    print("""
    This circular area is cobbled with cracked granite,
    upon which sprawl the bodies of four goblins,
    apparently slain in combat.
    One corpse stands with it's back against the western wall,
    the spear that killed it still skewering it and holding it upright.
    Three wooden doors lead from this area.
    A hollow tower pf loose masonry reaches thirty feet in the air,
    but intervening floors and stairs are gone,
    except for a few crumbled ledges.""")
    print("What do you do?")
    ans = input("~ ")
    if 'goblins' in ans:
        print("Do you read Draconic?")
        Draconic = input("~ ")
        if Draconic == 'yes':
            print("""
            The four goblins have been dead for quite awhile,
            When you move the one speared tot he wall,
            there are Darconic runes carved into the wall behind it.
            They say 'Ashardalon'.""")
            room_4()
        else:
            print("""
            The four goblins have been dead for quite awhile,
            The rats have gnawed on them.
            There is nothing of sigificance.""")
            room_4()
    elif 'search' in ans:
        print("Roll perception.")
        perception = d20_roll()
        if perception >= 20:
            print("You find a secret door!")
            secret_door()
            room_4()
        else:
            print("The room has two doors.")
    
    print("Which door would you like to go through?")
    print("The door to the left or to the right?")
    ans = input("~ ")
    if 'right' in ans:
        print("Ah, can't go here yet.")
        room_4()
    elif 'left' in ans:
        room_6()

def secret_door():
    print("""
    The door opens by way of a masonry block that also serves as a lever,
    which can be pushed in on the left side or pulled out fro the right.""")
    print("Make a perception check.")
    perception = d20_roll()
    if perception >= 15:
        print("You see a needle trap on the door.")
    else:
        print("Door does not seem to be locked.")
    print("As you reach the handle, a 3 inch needle springs towards your hand.")
    print("Roll dexterity.")
    dexterity = d20_roll()
    if dexterity >= 15:
        print("It missed your hand! That's good.")
    else:
        print("You weren't fast enough.")
        print("Take 1 damage.")
    room_5()

def room_3():
    print("""
    The narrow stairs empty into a small courtyard,
    apparently the top of what was once a crenellated battlement.
    The buried citadel has sunk so far into the earth
    that the battlement is now level with the surrounding floor.
    That floor stretches away to the north and south,
    composed of a layer of treacherous, crumbled masonry,
    which reaches to an unknown depth.
    To the west looms the surviving structure 
    of what must be the Sunless Citadel.
    A tower stands on the west side of the courtyard.""")
    print("""
    As you walk across the courtyard,
    you immediately note how unstable the masonry is underfoot.
    Roll dexterity to keep your footing.""")
    dexterity = d20_roll()
    if dexterity >= 15:
        print("You successfully keep your footing.")
        room_4()
    else:
        print("You fall a few times and take 3 damage.")
        print("Nonetheless you continue through the door.")
        room_4()

print("Hello adventurerer, what are you called?")
name = input("~ ")
print(f"Well {name}, would you like to venture into the dungeon?")
ans = input("~ ")
if 'yes' in ans:
    print("Off you go, good luck.")
    print("""
    In the breeze you hear
    'ee te ole 'ragoon from ees throne
    S' eenk wee enormous ruin down!
    it rises and falls with the wind slurring some words,
     making it hard to decipher.""")
    room_3()
else:
    print(f"Gods speed {name}, have safe travels elsewhere.")
    