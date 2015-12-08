# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define p = Character("")
define intd = Character("Old Man")
define ar = Character('IBM 5150', color="#00ff00", what_color="#009900", window_yminimum=300)

image introDude = "om.png"

image bg black = "black.png"
image bg town = "town.png"

init python hide:

    class LeftListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_LEFT,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.left_listener = LeftListener('left_code')

    def left_overlay():
        ui.add(store.left_listener)

    config.overlay_functions.append(left_overlay)

init python hide:

    class UpListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_UP,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
            
    store.up_listener = UpListener('up_code')
    def up_overlay():
        ui.add(store.up_listener)

    config.overlay_functions.append(up_overlay)

init python hide:

    class RightListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_RIGHT,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)

    store.right_listener = RightListener('right_code')

    def right_overlay():
        ui.add(store.right_listener)

    config.overlay_functions.append(right_overlay)



init python hide:

    class DownListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_DOWN,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.down_listener = DownListener('down_code')

    def down_overlay():
        ui.add(store.down_listener)

    config.overlay_functions.append(down_overlay)



init python hide:

    class SpaceListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_SPACE,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.space_listener = SpaceListener('space_code')

    def space_overlay():
        ui.add(store.space_listener)

    config.overlay_functions.append(space_overlay)

init python hide:

    class WListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_w,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    store.w_listener = WListener('w_code')

    def w_overlay():
        ui.add(store.w_listener)

    config.overlay_functions.append(w_overlay)


init python:
    
    import random
      
    #Parameters
    SIZE = 5
      
    #Choice Database
    stdChoiceList = [("Move",0),("Look",1),("Interact",2),("Meditate",3),("View Stats",4)];
    stdMoveList = [("Up",0),("Right",1),("Down",2),("Left",3)]
    stdBack = ("Back",-1)
    
    stdRaces = [("Human",0),("Elf",1),("Dwarf",2),("Xylrr",3)]
    stdClasses = [("Fighter",0),("Rogue",1),("Mage",2)]
      
    class Item:
        name = None
        worth = None
        rarity = None
        
        def __init__(self, name, worth, rarity):
            self.name = name
            self.worth = worth
            self.rarity = rarity
        
    class Weapon(Item):
        attack = None
        
        def __init__(self, name, worth, rarity, attack):
            Item.__init__(self, name, worth, rarity)
            self.attack = attack
        
    class Armor(Item):
        armor = None
        
        def __init__(self, name, worth, rarity, armor):
            Item.__init__(self, name, worth, rarity)
            self.armor = armor
        
    class Trinket(Item):
        
        def __init__(self, name, worth, rarity):
            Item.__init__(self, name, worth, rarity)
        
    class Chest:
        contents = None
        lockToughness = None
        
        def __init__(self, contents, lockToughness):
            self.contents = contents
            self.lockToughness = lockToughness
            
        def __init__(self, lockToughness):
            self.lockToughness = lockToughness
            self.contents = []
            for x in range(0,random.randint(0,lockToughness)):
                self.contents.append(stdItems[random.randint(0,len(stdItems)-1)])
                #TODO replace with actual random generation
    
    #Items
    stdItems = [Weapon("Weapon 1",1,0,1),Weapon("Weapon 2",1,0,1),Trinket("Trinket 1",1,0), \
        Armor("Armor 1",1,0,1),Weapon("Weapon 3",1,0,1),Weapon("Weapon 4",1,0,1), \
        Armor("Armor 2",1,0,1),Weapon("Weapon 5",1,0,1),Trinket("Trinket 2",1,0), \
        Item("Pile of Gold",1,0),Item("Pile of Gold",1,0),Item("Pile of Gold",1,0)]
    
    stdChests = [Chest(1)]
    
    class Enemy:
        name = None
        hp = None
        attack = None
        minLevel = None
        possibleLoot = None
        
        def __init__(self, name, hp, attack, minLevel, possibleLoot):
            self.name = name
            self.hp = hp
            self.attack = attack
            self.minLevel = minLevel
            self.possibleLoot = possibleLoot
      
    #Enemies
    stdEnemies = [Enemy("ENEMY!!!",1,1,0,[])]
    
    #Descriptors
    descRoomShape = ["circular", "hexagonal","","",""];
    descRoomSize = ["tiny", "", "", "small", "", "humble", "large", "huge", "gargantuan"];
    descRoomModifiers = ["creepy", "", "", "smelly", "", "decrepit", "disgusting", "cold", "dark"];
    
    
    def pickFromList(src):
        return src[random.randint(0,len(src)-1)]
    
    def genRandDescription():
        shape = pickFromList(descRoomShape)
        size = pickFromList(descRoomSize)
        modifier = pickFromList(descRoomModifiers)
        
        return "You appear to be in a " + size + " " + modifier + " " + shape + " room." 
    
    def genConnections():
        cons = []
        
        for dir in range(0,4):
            if random.choice([True, False]):
                cons.append(dir)
                
        if len(cons) > 2:
            return cons
        else:
            return genConnections()
    
    class Room:
        description = None
        connections = None
        minLevel = None
        enemies = None
        
        def addLoot(self):
            minLevel
            
        def addEnemies(self):
            minLevel
        
        #def __init__(self,description, connections, minLevel):
        #    self.description = description;
        #    self.connections = connections;
        #    self.minLevel = minLevel;
        
        def __init__(self): #TODO fix this shit!
            self.description = genRandDescription()
            self.connections = genConnections()
            self.minLevel = 0;
        
        def setAsEmpty(self):
            self.description = "EMPTY"
            self.connections = []
            self.minLevel = 0
        
        def getDescription(self):
            return self.description
            
        def getConnections(self):
            return self.connections
        
        def getMinLevel(self):
            return self.minLevel
            
        def hasConnection(self, connection):
            return connection in self.connections
        
        
    #Rooms
    emptyRoom = Room()
    emptyRoom.setAsEmpty()
    
    class Player:
        name = None
        race = None
        pclass = None
        xPos = None
        yPos = None
        alive = True
        hp = 10
        energy = 10
        attack = 5
        defense = 5
        food = 10
        skillLockPick = 0
    
        def setName(self, name):
            self.name = name
            
        def setRace(self, race):
            self.race = race
            
        def setClass(self, pclass):
            self.pclass = pclass
            
        def setPosition(self, xPos, yPos):
            self.xPos = xPos
            self.yPos = yPos
            
        def getStats(self):
            statBlock = self.name + " (" + self.race + " " + self.pclass + ")\nHP: " + str(self.hp) + \
                "\nEnergy: " + str(self.energy) + "\nAttack: " + str(self.attack) + \
                "\nDefense: " + str(self.defense)
                
            
            return statBlock
    
    #Player
    player = Player()
    
    
    #Level Info
    levelNum = 0
    levelLayout = []
    
    def choice(choices):
        return menu(choices, True, "Select an Action")
        
    def getRandomRoom(connection):
        if connection == [] or connection == None:
            return Room()
        else:
            room = emptyRoom
            while not room.hasConnection(connection):
                room = Room()
            return room
        
    def getActionsAvailable(player, levelLayout):
        actionsAvailable = []
        currentRoom = levelLayout[player.xPos][player.yPos]
        
        
        actionsAvailable.append(stdChoiceList[0]) #Movement
        actionsAvailable.append(stdChoiceList[1]) #Look
        actionsAvailable.append(stdChoiceList[3]) #Play RL
        actionsAvailable.append(stdChoiceList[4]) #Check Stats
        
        return actionsAvailable
        
        
    def getMovementActionsAvailable(player, levelLayout):
        actionsAvailable = []
        currentRoom = levelLayout[player.xPos][player.yPos]
        
        actionsAvailable.append(stdBack)
        
        #Up
        if player.yPos > 0 and currentRoom.hasConnection(0):
            actionsAvailable.append(stdMoveList[0])
        
        #Down    
        if player.yPos > 4 and currentRoom.hasConnection(2):
            actionsAvailable.append(stdMoveList[2])
        
        #Left    
        if player.xPos > 0 and currentRoom.hasConnection(3):
            actionsAvailable.append(stdMoveList[3])
        
        #Right    
        if player.xPos < 4 and currentRoom.hasConnection(1):
            actionsAvailable.append(stdMoveList[1])
            
        return actionsAvailable
        
    def newLevel():
        
        levelLayout[:] = []
        
        for x in range(0,SIZE):
            row = []
            for y in range(0,SIZE):
                row.append(emptyRoom)
            levelLayout.append(row)
        
        startX = random.randint(1,SIZE-2)
        startY = random.randint(1,SIZE-2)
        
        player.setPosition(startX,startY)
        
        for x in range(0,SIZE):
            for y in range(0,SIZE):
                levelLayout[x][y] = getRandomRoom([])
        
        #TODO add logic for good rooms?
        #levelLayout[startX][startY] = getRandomRoom([])

    def getCurrentRoom(player):
        return levelLayout[player.xPos][player.yPos]


# The game starts here.
label start:
    
    scene bg black
    play music "shia.wav"
    
    python:
        race = choice(stdRaces);
        pclass = choice(stdClasses);
        
        if race == 0: #Human
            player.setRace(stdRaces[0][0])
            player.hp = player.hp + 2
            player.attack = player.attack + 2
            
        elif race == 1: #Elf
            player.setRace(stdRaces[1][0])
            player.energy = player.energy + 2
            
        elif race == 2: #Dwarf
            player.setRace(stdRaces[2][0])
            player.hp = player.hp + 5
            player.defense = player.defense + 2
            player.energy = player.energy - 4
            
        elif race == 3: #Xylrr
            player.setRace(stdRaces[3][0])
            player.hp = player.hp - 1
            player.energy = player.energy + 4
            
        if pclass == 0: #Fighter
            player.setClass(stdClasses[0][0])
            player.hp = player.hp + 4
            player.attack = player.attack + 3
            player.defense = player.defense + 5
            
        if pclass == 1: #Rogue
            player.setClass(stdClasses[1][0])
            player.hp = player.hp + 1
            player.attack = player.attack + 7
            player.defense = player.defense + 1
            
        if pclass == 2: #Mage
            player.setClass(stdClasses[2][0])
            player.energy = player.energy + 15
            player.attack = player.attack - 2
            player.defense = player.defense - 2
    
    scene bg town
    show introDude
    with fade
    
    intd "Greetings, brave adventurer! Thank you for heeding our call! I fear that our time may have been short if you hadn't..."
        
    $ player.setName(renpy.input("May I have your name?","",None,None,None,None))
    
    intd "They come from the ruins to the north. They are unrelenting!"
    intd "Please! Help us!"
    intd "Go forth and save us all, [player.name]!"
    
    hide introDude
    scene bg black
    with fade
    
    $ newLevel()
    
    jump loop

    return
    
label loop:
    
    python:
        
        playerChoice = choice(getActionsAvailable(player, levelLayout))
        
        if playerChoice == 0:
            moveDir = choice(getMovementActionsAvailable(player, levelLayout))
            
            if moveDir == 0: #Up
                player.setPosition(player.xPos, player.yPos - 1)
            elif moveDir == 1: #Right
                player.setPosition(player.xPos + 1, player.yPos)
            elif moveDir == 2: #Down
                player.setPosition(player.xPos, player.yPos + 1)
            elif moveDir == 3: #Left
                player.setPosition(player.xPos - 1, player.yPos)
            elif moveDir == -1: #Back
                renpy.jump("loop")
            
        elif playerChoice == 1:
            renpy.say(p,getCurrentRoom(player).getDescription())
        elif playerChoice == 4:
            renpy.say(p,player.getStats())
        elif playerChoice == 3:
            renpy.say(p,"You close your mind and find yourself in your inner sanctum...")
            renpy.call("launchRL")
            renpy.say(p,"The world fades back into existence...")
    if player.alive:
        jump loop

    return

label launchRL:
    $dir = "ayyyy"
    scene bg_meta
    with fade
    
    
    #call screen argame
    #ar "[dir]"
    call rebut from _call_rebut
    while not medead:
        call arcade from _call_arcade
        if medead:
            ar "Game Over{w}"
            $ score = 0
            $ oldscore = 0
            $ health = 20
        else:
            call rebut from _call_rebut_1
    if medead:
        $ renpy.pause(2,None,None,True,False)
        ar "Game Over{w}"
        $ score = 0
        $ oldscore = 0
        $ health = 20
        
    scene bg black
    with fade
    
    return


label left_code:
    $ dir = "w"
    return
label up_code:
    $ dir = "n"
    return
label right_code:
    $ dir = "e"
    return
label down_code:
    $ dir = "s"
    return
label space_code:
    $ dir = "action1"
    return
label w_code:
    $ dir = "action2"
    return
    
label rebut:
    $ medead = False
    python:
        
        def fuserooms(rooms):
            tallest = 0
            totwidth = 0;
            for i in range(0,numrooms):
                totwidth += len(rooms[i])
                if len(rooms[i]) > tallest:
                    tallest = len(rooms[i])
                    
            fusedroom = [None] * tallest
            trueheights = [None] * numrooms
            for i in range (0,numrooms):
                lwidth = len(rooms[i][0])
                trueheights[i] = len(rooms[i])
                if not(fusedroom[0] is None):
                    oldx = len(fusedroom[0])
                    
                if len(rooms[i]) < tallest:
                    while len(rooms[i]) < tallest:
                        rooms[i].append([None] * lwidth)
                for yy in range(0,len(rooms[i])):
                    if fusedroom[yy] is None:
                        fusedroom[yy] = rooms[i][yy]
                    else:
                        fusedroom[yy] += rooms[i][yy]
                if i > 0:
                    shortest = trueheights[i]
                    if shortest > trueheights[i-1]:
                        shortest = trueheights[i-1]
                    doorheight = random.randint(1,shortest-2)
                    fusedroom[doorheight][oldx-1] = 1
                    fusedroom[doorheight][oldx] = 1
                        
            
            return fusedroom
        enemies=[]
        def genroom( dim ):
            width = dim[0]
            height = dim[1]
            room = [None] * (height+2)
            room[0] = [0] *(width+2)
            room[height+1] = [0] *(width+2)
            for yy in range(1,height+1):
                    row = [1] * (width+2)
                    row[0] = 0
                    row[width+1] = 0
                    for xx in range(1, width):
                        if random.randint(1,20) > 17:
                            if random.randint(1,10)>=7:
                                row[xx] = 4
                            else:
                                row[xx] = 3
                    room[yy] = row
            return room
        numrooms = random.randint(3,7)
        rooms = [None] * numrooms
        roomdim = [None] * numrooms
        for i in range(0, numrooms):
            roomdim[i] = [random.randint(2,7), random.randint(2,7)]
            rooms[i] = genroom(roomdim[i])
        q = 1
        while(rooms[0][q][q] != 1 and q < roomdim[0][0] and q<roomdim[0][1]):
            q+=1
        rooms[0][q][q] = 2
        x = q
        y = q
        
        exit = rooms[numrooms-1]
        ex = roomdim[numrooms-1][0]
        ey = roomdim[numrooms-1][1]
        done = False
        for yy in range(0,ey):
            for xx in range(0,ex):
                if exit[(ey - yy)-1][(ex - xx)-1]==1:
                    exit[(ey - yy)-1][(ex - xx)-1]=6
                    done = True
                    break
            if done:
                break
        
        
        
        endlevel = False
        fusedroom = fuserooms(rooms)   
    return
init:
    image bg_meta = im.Scale("trisqwall.jpg",800,600)
    $ import random
    $ score = 0
    $ oldscore = 0
    $ health = 20
    $ medead = False
    call rebut from _call_rebut_2
            
    

label arcade:
    # room info:
    # 0 = #
    # 1 = .
    # 2 = @
    # 3 = q
    # 4 = X
    # 5 = +
    # 6 = S
    # parse things
    python:
                width = len(fusedroom[0])
                height = len(fusedroom)
                terxt = ""
                for yy in range(0,height):
                    for xx in range(0, width):
                        if fusedroom[yy][xx] is None:
                            terxt += " "
                        elif fusedroom[yy][xx] == 0:
                            terxt += "#"
                        elif fusedroom[yy][xx] == 1:
                            terxt += "."
                        elif fusedroom[yy][xx] == 2:
                            terxt += "@"
                        elif fusedroom[yy][xx] == 3:
                            terxt += "q"
                        elif fusedroom[yy][xx] == 4:
                            en = False
                            for enemy in enemies:
                                if enemy[0] == yy and enemy[1] == xx:
                                    if (float(enemy[2])/float(enemy[3])) > (3.0/4.0):
                                        terxt += "X"
                                    elif (float(enemy[2])/float(enemy[3])) > (1.0/2.0):
                                        terxt += "Y"
                                    elif (float(enemy[2])/float(enemy[3])) > (1.0/4.0):
                                        terxt += "/"
                                    else:
                                        terxt+="-"
                                    en = True
                                    break
                            if not en:
                                ehealth = random.randint(9,15)
                                enemies.append([yy,xx,float(ehealth),ehealth])
                                terxt += "X"
                        elif fusedroom[yy][xx] == 5:
                            terxt += "+"
                        elif fusedroom[yy][xx] == 6:
                            terxt += "S"
                        else:
                            terxt += "?"

                    terxt += "\n"

    ar "[terxt] Score: [score] Health: [health]"
    
    
    python:
        def attack(yy, xx):
            global health
            global medead
            global score
            dead = False
            if(random.randint(1,3) >= 2):
                for enemy in enemies:
                    if enemy[0] == yy and enemy[1] == xx:
                        enemy[2] = enemy[2] - float(random.randint(1,4))
                        if enemy[2] <= 0.0:
                            enemies.remove(enemy)
                            dead = True
                            fusedroom[yy][xx] = 5
                        break;
            if not dead and random.randint(1,3) >= 2:
                health = health - random.randint(1,4)
                if health<=0:
                    medead = True
                
        oldx = x
        oldy = y
        if dir == "w":
            if fusedroom[y][x-1] == 1 or fusedroom[y][x-1] == 3 or fusedroom[y][x-1] == 5 or fusedroom[y][x-1] == 6:
                x-=1
            elif fusedroom[y][x-1] == 4:
                attack(y,x-1)
        if dir == "n":
            if fusedroom[y-1][x] == 1 or fusedroom[y-1][x] == 3 or fusedroom[y-1][x] == 5 or fusedroom[y-1][x] == 6:
                y-=1
            elif fusedroom[y-1][x] == 4:
                attack(y-1,x)
        if dir == "e":
            if fusedroom[y][x+1] == 1 or fusedroom[y][x+1] == 3 or fusedroom[y][x+1] == 5 or fusedroom[y][x+1] == 6:
                x+=1
            elif fusedroom[y][x+1] == 4:
                attack(y,x+1)
        if dir == "s":
            if fusedroom[y+1][x] == 1 or fusedroom[y+1][x] == 3 or fusedroom[y+1][x] == 5 or fusedroom[y+1][x] == 6:
                y+=1
            elif fusedroom[y+1][x] == 4:
                attack(y+1,x)
        dir = "o"
        fusedroom[oldy][oldx] = 1
        if fusedroom[y][x] == 3:
            score += 100
        if fusedroom[y][x] == 5:
            score += 200
        if fusedroom[y][x] == 6:
            endlevel = True  
        fusedroom[y][x] = 2
        if score - oldscore >= 1000:
            oldscore = score
            health += 10
    if not endlevel and not medead:
        call arcade from _call_arcade_1
    return