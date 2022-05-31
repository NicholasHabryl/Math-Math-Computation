import pygame
import pygame_menu as pm
import tkinter as tk
import games.speedrun
import utils

#root =tk.Tk()
#SCREEN_DIMENSIONS = (root.winfo_screenwidth(), root.winfo_screenheight()) #full screen
SCREEN_DIMENSIONS = (800, 600)

MODES = [
    ("Addition","ADD"),
    ("Subtraction","SUB"),
    ("Multiplication","MULTI"),
    ("Division","DIV")]

#not sure why we need these arguments but it breaks if we dont have them
def selectnext(useless, args):
    
    curr = menu.get_current()

    print("selected is: " + curr.get_widget("speedselect").get_value()[0][1])
    if(curr.get_selected_widget()==curr.get_widgets()[1]):
        curr.select_widget(curr.get_widgets()[2])
    else:
        curr.select_widget(curr.get_widgets()[1])

def updatemode(value, difficulty: str):
    print(utils.MODE[0])
    utils.MODE[0] = difficulty
    print(utils.MODE[0])

pygame.init()

surface = pygame.display.set_mode(SCREEN_DIMENSIONS)

#defining menus
menu = pm.Menu( title="Main Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=4,
                rows=1,
                theme= pm.themes.THEME_BLUE)

playmodemenu = pm.Menu( title="Play Mode Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)

speedrunmenu = pm.Menu( title="Speed Run Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)

mtgmenu = pm.Menu( title="Mind the Gap Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)   

pracmodemenu = pm.Menu( title="Practice Mode Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)

flashmenu = pm.Menu( title="Flashcard Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=4,
                rows=1,
                theme= pm.themes.THEME_BLUE)

learningmenu = pm.Menu( title="Learning Menu",
                width=SCREEN_DIMENSIONS[0],
                height=SCREEN_DIMENSIONS[1],
                columns=4,
                rows=1,
                theme= pm.themes.THEME_BLUE)

#defining widgets in menus
playmodemenu.add.button("Speed Run",speedrunmenu)
playmodemenu.add.button("Mind the Gap",mtgmenu)
playmodemenu.add.button("Go Back",pm.events.BACK)

pracmodemenu.add.button("Flashcard",flashmenu)
pracmodemenu.add.button("Learning",learningmenu)
pracmodemenu.add.button("Go Back",pm.events.BACK)

#speedrunmenu.add.button()
speedrunmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onchange= updatemode,
    onreturn= selectnext,
    selector_id = "speedselect"
)
print(speedrunmenu.get_widget("speedselect").get_value()[0][1])
speedrunmenu.add.button("Play!",games.speedrun.game) #when Speed run is fully developed put the function here
speedrunmenu.add.button("Go Back",pm.events.BACK)

mtgmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onreturn= selectnext
)
mtgmenu.add.button("Play!") #when Mind the Gap is fully developed put the function here
mtgmenu.add.button("Go Back",pm.events.BACK)

flashmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onreturn= selectnext
)
flashmenu.add.selector(
    title = "Pick Number",
    items= [
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("5",5),
        ("6",6),
        ("7",7),
        ("8",8),
        ("9",9),
        ("10",10),
        ("11",11),
        ("12",12)
    ],
    onreturn= selectnext
)
flashmenu.add.button("Play!") #when Flashcard is fully developed put the function here
flashmenu.add.button("Go Back",pm.events.BACK)

learningmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onreturn= selectnext
)
learningmenu.add.selector(
    title = "Pick Number",
    items= [
        ("1",1),
        ("2",2),
        ("3",3),
        ("4",4),
        ("5",5),
        ("6",6),
        ("7",7),
        ("8",8),
        ("9",9),
        ("10",10),
        ("11",11),
        ("12",12)
    ],
    onreturn= selectnext
)
learningmenu.add.button("Play!") #when learningmenu is fully developed put the function here
learningmenu.add.button("Go Back",pm.events.BACK)

menu.add.button("Play mode",playmodemenu)
menu.add.button("Practice mode",pracmodemenu)
menu.add.button("Leaderboards")
menu.add.button("Exit",pm.events.EXIT)

menu.mainloop(surface)

