import pygame
import pygame_menu as pm
import tkinter as tk

#not sure why we need these arguments but it breaks if we dont have them
def selectnext(useless, args):
    curr = menu.get_current()
    if(curr.get_selected_widget()==curr.get_widgets()[1]):
        curr.select_widget(curr.get_widgets()[2])
    else:
        curr.select_widget(curr.get_widgets()[1])
    

root =tk.Tk()
SCREEN_DIMENSIONS = (root.winfo_screenwidth(), root.winfo_screenheight())

MODES = [
    ("Addition","ADD"),
    ("Subtraction","SUB"),
    ("Multiplication","MULTI"),
    ("Division","DIV")]

pygame.init()
surface = pygame.display.set_mode(SCREEN_DIMENSIONS)

#defining menus
menu = pm.Menu( title="Main Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
                columns=4,
                rows=1,
                theme= pm.themes.THEME_BLUE)

playmodemenu = pm.Menu( title="Play Mode Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)

speedrunmenu = pm.Menu( title="Speed Run Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)

mtgmenu = pm.Menu( title="Mind the Gap Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)   

pracmodemenu = pm.Menu( title="Practice Mode Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
                columns=3,
                rows=1,
                theme= pm.themes.THEME_BLUE)

flashmenu = pm.Menu( title="Flashcard Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
                columns=4,
                rows=1,
                theme= pm.themes.THEME_BLUE)

learningmenu = pm.Menu( title="Learning Menu",
                width=SCREEN_DIMENSIONS[0] * 0.75,
                height=SCREEN_DIMENSIONS[1] * 0.75,
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

speedrunmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onreturn= selectnext
)
speedrunmenu.add.button("Play!") #when Speed run is fully developed put the function here
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
learningmenu.add.button("Play!") #when Flashcard is fully developed put the function here
learningmenu.add.button("Go Back",pm.events.BACK)

menu.add.button("Play mode",playmodemenu)
menu.add.button("Practice mode",pracmodemenu)
menu.add.button("Leaderboards")
menu.add.button("Exit",pm.events.EXIT)

menu.mainloop(surface)
