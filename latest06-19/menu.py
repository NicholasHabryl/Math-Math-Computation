from sre_compile import isstring
import pygame
import pygame_menu as pm
import tkinter as tk
import games.flashcardmode
import games.learningmode
import games.mindthegap
import games.speedrun
import utils
import games.controls

# Serial
from serial import Serial
from time import localtime, strftime

from pygame.locals import ( #many of these K_whatevers can be removed once out of testing
    K_a,
    K_d,
    K_z,
    K_c,
    K_w,
    K_x,
    K_e,
    K_q,
    K_RETURN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Custom event for serial communication
# The event IDs for serial are 25, 26, 27, 28, 29
EVENT_UP = pygame.USEREVENT + 1
EVENT_LEFT = pygame.USEREVENT + 2
EVENT_RIGHT = pygame.USEREVENT + 3
EVENT_DOWN = pygame.USEREVENT + 4
EVENT_SERIAL = pygame.USEREVENT + 5

SCREEN_DIMENSIONS = (800, 600)

MODES = [
    ("Addition","ADD"),
    ("Subtraction","SUB"),
    ("Multiplication","MULTI"),
    ("Division","DIV")]

#not sure why we need these arguments but it breaks if we dont have them
def selectnext(useless, args):
    
    if isstring(args):
        utils.MODE[0] = args
    else:
        utils.FOCUS_NUM[0] = args

    curr = menu.get_current()

    print("selected is: " + curr.get_widget("modeselect").get_value()[0][1])
    if(curr.get_selected_widget()==curr.get_widgets()[1]):
        curr.select_widget(curr.get_widgets()[2])
    else:
        curr.select_widget(curr.get_widgets()[1])

def updatemode(value, mode: str):
    print(utils.MODE[0])
    utils.MODE[0] = mode
    print(utils.MODE[0])

def updatenum(value, num: int):
    print(utils.MODE[0])
    utils.FOCUS_NUM[0] = num
    print(utils.MODE[0])

def on_resize():
    window_size = surface.get_size()
    menu.resize(window_size[0], window_size[1])
    print(f'New menu size: {menu.get_size()}')

pygame.init()

surface = pygame.display.set_mode(SCREEN_DIMENSIONS,pygame.RESIZABLE)

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
    selector_id = "modeselect"
)
speedrunmenu.add.button("Play!",games.speedrun.game) #when Speed run is fully developed put the function here
speedrunmenu.add.button("Go Back",pm.events.BACK)

mtgmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onchange= updatemode,
    onreturn= selectnext,
    selector_id = "modeselect"
)
mtgmenu.add.button("Play!",games.mindthegap.game) #when Mind the Gap is fully developed put the function here
mtgmenu.add.button("Go Back",pm.events.BACK)

flashmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onchange= updatemode,
    onreturn= selectnext,
    selector_id = "modeselect"
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
    onchange = updatenum,
    onreturn= selectnext
)
flashmenu.add.button("Play!",games.flashcardmode.game) #when Flashcard is fully developed put the function here
flashmenu.add.button("Go Back",pm.events.BACK)

learningmenu.add.selector(
    title = "Pick Modes",
    items= MODES,
    onchange= updatemode,
    onreturn= selectnext,
    selector_id = "modeselect"
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
    onchange = updatenum,
    onreturn= selectnext
)
learningmenu.add.button("Play!",games.learningmode.game) #when learningmenu is fully developed put the function here
learningmenu.add.button("Go Back",pm.events.BACK)

menu.add.button("Play mode",playmodemenu)
menu.add.button("Practice mode",pracmodemenu)
menu.add.button("Leaderboards")
menu.add.button("Exit",pm.events.EXIT)

#this is what initially worked
#menu.mainloop(surface)

if __name__ == '__main__':
    # Setting up serial communication
    ser = Serial()
    ser.port = '/dev/cu.usbmodem14301'
    ser.baudrate = 9600
    ser.timeout = 0
    ser.open()
    while True:
        events = pygame.event.get()
        for event in events:
            # reading serial
            
            pygame.event.post(pygame.event.Event(EVENT_SERIAL))
            
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.VIDEORESIZE:
                # Update the surface
                surface = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                # Call the menu event
                on_resize()

            #these statements can be modified once serial input can be read
            # if event.type == EVENT_SERIAL:

            #     if (line.decode() == games.controls.arrowEnter):
            #         pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RETURN))
            #     if (line.decode() == games.controls.arrowPlusTen):
            #         pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_LEFT))
            #     if (line.decode() == games.controls.arrowPlusOne):
            #         pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RIGHT))
            #     if (line.decode() == games.controls.arrowClear):
            #         pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_BACKSPACE))
            if event.type == EVENT_SERIAL:
                line = ser.readline()
                # if event.key == K_w:
                if (line.decode() == games.controls.arrowEnter):
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RETURN))
                if (line.decode() == games.controls.arrowPlusTen):
                    print(line)
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=K_LEFT))
                if (line.decode() == games.controls.arrowPlusOne):
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RIGHT))
                if (line.decode() == games.controls.arrowClear):
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN,key=pygame.K_BACKSPACE))

        # Draw the menu
        surface.fill((25, 0, 50))

        menu.update(events)
        menu.draw(surface)

        pygame.display.flip()
