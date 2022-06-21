import pygame
import utils
import controls 

# Serial
from serial import Serial
from time import localtime, strftime

from random import randint
from pygame.locals import ( 
    QUIT,
)

# Custom event for serial communication
# The event ID for serial is 26
EVENT_SERIAL = pygame.USEREVENT + 2

pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TITLE_FONT = pygame.font.SysFont('comicsans',60)
QUESTION_FONT = pygame.font.SysFont('comicsans',50)
INFO_FONT = pygame.font.SysFont('comicsans',35)

#the pause menu
def pause_menu(ser):
    screen.fill((215,215,215))
    title_text = TITLE_FONT.render("Game Paused",1,(0,0,0))
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2,150))

    instruction_text = INFO_FONT.render("Press pause to resume play",1,(0,0,0))
    literally_just_the_word_OR = INFO_FONT.render("OR" ,1,(0,0,0))
    instruction_text2 = INFO_FONT.render("Press main menu to exit",1,(0,0,0))
    screen.blit(instruction_text, (SCREEN_WIDTH/2 - instruction_text.get_width()/2,350))   
    screen.blit(literally_just_the_word_OR, (SCREEN_WIDTH/2 - literally_just_the_word_OR.get_width()/2,350+instruction_text.get_height()))   
    screen.blit(instruction_text2, (SCREEN_WIDTH/2 - instruction_text2.get_width()/2,350+instruction_text.get_height()+literally_just_the_word_OR.get_height()))   

    pygame.display.flip()
    while True: 
        line = ser.readline()
        if (line.decode() == controls.arrowMenu):
            return False
        elif (line.decode() == controls.arrowPause):
            return True
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

#this performs the operation depending on the mode
def operation(mode,a,b): 
    if(mode == 'ADD'):
        return a + b
    if(mode =='SUB'): 
        return a - b
    if(mode == 'MULTI'): 
        return a * b
    if(mode == 'DIV'): 
        return a / b
    print("How did you put in a wrong operation?!")

#check operation is valid
#no negatives, no fractions/decimals, no dividing by 0
def check(mode, a, b): 
    if(mode == 'SUB' and b>a): return False
    if(mode == 'DIV' and b==0): return False
    if(mode == 'DIV' and a%b!=0): return False
    return True

#TODO update division algorithm
#create a valid operation
def generate(mode,b):
    a  = 0 
    while(1):
        a = randint(0,12)
        if mode == "SUB":
            a += b
        if mode == "DIV":
            a *= b
        if(check(mode,a,b)):
            break
    return a 

def display_answer(mode,first,second,ser):
    draw_screen(mode,first,second,0,True)
    
    while True: 
        line = ser.readline()
        if (line.decode() == controls.arrowEnter):
            return False
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

#TODO instructions
#draw any updates to the screen
def draw_screen(mode, first,second,useranswer,learningflag):
      
    screen.fill((0,95,170))
    
    titlesurf = pygame.Surface((SCREEN_WIDTH,140)).fill((0,0,0))
    pygame.draw.rect(screen,(0,65,120),titlesurf)
    title_text = TITLE_FONT.render("Learning Mode",1,(255,255,255))
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2,titlesurf.height/2 -title_text.get_height()/2))
    
    questionsurf = pygame.Rect(
        SCREEN_WIDTH*(1/8), #1/8
        SCREEN_HEIGHT/2 + titlesurf.height/2 - SCREEN_WIDTH*(3/30), #3/32
        SCREEN_WIDTH*(3/4), #3/4
        SCREEN_WIDTH*(3/14) #3/16
        )
    firstrect= pygame.Rect(
        SCREEN_WIDTH*(1/8),
        SCREEN_HEIGHT/2 + titlesurf.height/2 - SCREEN_WIDTH*(3/30),
        SCREEN_WIDTH*(3/16),
        SCREEN_WIDTH*(3/14) #3/16
    )
    moderect= pygame.Rect(
        SCREEN_WIDTH*(1/8) + firstrect.width,
        SCREEN_HEIGHT/2 + titlesurf.height/2 - SCREEN_WIDTH*(3/30),
        SCREEN_WIDTH*(3/32),
        SCREEN_WIDTH*(3/14) #3/16
    )
    secondrect= pygame.Rect(
        SCREEN_WIDTH*(1/8) + firstrect.width + moderect.width,
        SCREEN_HEIGHT/2 + titlesurf.height/2 - SCREEN_WIDTH*(3/30),
        SCREEN_WIDTH*(3/16),
        SCREEN_WIDTH*(3/14) #3/16
    )
    answerrect= pygame.Rect(
        SCREEN_WIDTH*(1/8) + 2*firstrect.width + 2*moderect.width,
        SCREEN_HEIGHT/2 + titlesurf.height/2 - SCREEN_WIDTH*(3/30),
        SCREEN_WIDTH*(3/16),
        SCREEN_WIDTH*(3/14) #3/16
    )
    #pygame.draw.rect(screen,(255,255,255),questionsurf)
    pygame.draw.rect(screen,(230,230,230),firstrect)
    pygame.draw.rect(screen,(230,230,230),moderect)
    pygame.draw.rect(screen,(230,230,230),secondrect)
    pygame.draw.rect(screen,(230,230,230),answerrect)

    first_text = QUESTION_FONT.render(str(first),1,(0,0,0))
    modetext = 0
    if(mode == 'ADD'):
        modetext = QUESTION_FONT.render('+',1,(0,0,0))
    elif(mode == 'SUB'):
        modetext = QUESTION_FONT.render('-',1,(0,0,0))
    elif(mode == 'MULTI'):
        modetext = QUESTION_FONT.render('x',1,(0,0,0))
    elif(mode == 'DIV'):
        modetext = QUESTION_FONT.render(chr(247),1,(0,0,0))
    else: 
        print(" invalid mode: "+ str(mode))
        exit()
    second_text = QUESTION_FONT.render(str(second),1,(0,0,0))

    if learningflag:
        answer_text = QUESTION_FONT.render(str(operation(mode,first,second)),1,(210,0,0))
    else:
        answer_text = QUESTION_FONT.render(str(useranswer),1,(0,0,0))

    screen.blit(first_text, (firstrect.x + firstrect.width/2 - first_text.get_width()/2,firstrect.y + firstrect.height/2 - first_text.get_height()/2 ))
    screen.blit(modetext, (moderect.x + moderect.width/2 - modetext.get_width()/2,moderect.y + moderect.height/2 - modetext.get_height()/2 ))
    screen.blit(second_text, (secondrect.x + secondrect.width/2 - second_text.get_width()/2,secondrect.y + secondrect.height/2 - second_text.get_height()/2 ))
    screen.blit(answer_text, (answerrect.x + answerrect.width/2 - answer_text.get_width()/2,answerrect.y + answerrect.height/2 - answer_text.get_height()/2 ))

    # Update the display
    pygame.display.flip()

#this will eventually contain everything
def game():
    # Setting up serial communication
    ser = Serial()
    ser.port = '/dev/cu.usbmodem14301'
    ser.baudrate = 9600
    ser.open()

    mode = utils.MODE[0]
    second = utils.FOCUS_NUM[0]
    #mode = "ADD"
    #initialize game
    pygame.init()

    running = True

    first = generate(mode,second)
    useranswer = 0
    display_answer(mode,first,second,ser)

    while running:
        # reading serial
        line = ser.readline()
        pygame.event.post(pygame.event.Event(EVENT_SERIAL))

        # for loop through the event queue
        for event in pygame.event.get():
            # # Check for KEYDOWN event
            if event.type == EVENT_SERIAL:
                # If the Menu button is pressed, then exit the main loop
                if (line.decode() == controls.arrowMenu):
                    running = False
                elif (line.decode() == controls.arrowEnter):  #the enter pad
                    if (operation(mode,first,second)==useranswer):
                        first = generate(mode,second)
                        useranswer = 0
                        display_answer(mode,first,second,ser)
                        #TODO: say it was correct, display graphics, say wrong is wrong
                elif (line.decode() == controls.arrowMinsTen):  #the -10 pad
                    useranswer -= 10
                    if(useranswer < 0 ): 
                        useranswer = 0
                elif (line.decode() == controls.arrowMinsOne):  #the -1 pad
                    useranswer -= 1
                    if(useranswer < 0 ): 
                        useranswer = 0
                elif (line.decode() == controls.arrowPlusTen):  #the +10 pad
                    useranswer += 10
                elif (line.decode() == controls.arrowPlusOne):  #the +1 pad
                    useranswer += 1
                elif (line.decode() == controls.arrowClear):  #the clear pad
                    useranswer = 0
                elif (line.decode() == controls.arrowPause):  #the pause pad
                    running = pause_menu(ser)
                    if not running:
                        continue             

            # Check for QUIT event. If QUIT, then set running to false.
            if event.type == QUIT:
                running = False

        draw_screen(mode,first,second,useranswer,False)

    #probably dont want to call this as it might end the menu too
    #pygame.quit()

game()