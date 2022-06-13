import pygame
import utils

from random import randint
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

pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TITLE_FONT = pygame.font.SysFont('comicsans',60)
QUESTION_FONT = pygame.font.SysFont('comicsans',50)
INFO_FONT = pygame.font.SysFont('comicsans',35)

#the pause menu
def pause_menu():
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
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                if event.key == K_e:
                    return True
                elif event.key == K_q:
                    return False
            elif event.type == QUIT:
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



#TODO instructions
#draw any updates to the screen
def draw_screen(mode, first,second,useranswer):
    
    
    screen.fill((0,95,170))
    
    titlesurf = pygame.Surface((SCREEN_WIDTH,140)).fill((0,0,0))
    pygame.draw.rect(screen,(0,65,120),titlesurf)
    title_text = TITLE_FONT.render("Speed Run",1,(255,255,255))
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
    answer_text = QUESTION_FONT.render(str(useranswer),1,(0,0,0))

    screen.blit(first_text, (firstrect.x + firstrect.width/2 - first_text.get_width()/2,firstrect.y + firstrect.height/2 - first_text.get_height()/2 ))
    screen.blit(modetext, (moderect.x + moderect.width/2 - modetext.get_width()/2,moderect.y + moderect.height/2 - modetext.get_height()/2 ))
    screen.blit(second_text, (secondrect.x + secondrect.width/2 - second_text.get_width()/2,secondrect.y + secondrect.height/2 - second_text.get_height()/2 ))
    screen.blit(answer_text, (answerrect.x + answerrect.width/2 - answer_text.get_width()/2,answerrect.y + answerrect.height/2 - answer_text.get_height()/2 ))

    # Update the display
    pygame.display.flip()

#this will eventually contain everything
def game():

    # curr = menu.get_current()
    # mode = curr.get_widget("speedselect").get_value()[0][1]
    #print("why father: " + utils.MODE[0])
    mode = utils.MODE[0]
    second = utils.FOCUS_NUM[0]
    #mode = "ADD"
    #initialize game
    pygame.init()

    running = True

    first = generate(mode,second)
    useranswer = 0

    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False

                #for the sake of testing, we will be using keys
                #once we get everything hooked up, this will have to receive inputs from the USB port

                elif event.key == K_w:  #the enter pad
                    if (operation(mode,first,second)==useranswer):
                        first = generate(mode,second)
                        useranswer = 0
                        #TODO: say it was correct, display graphics, say wrong is wrong
                elif event.key == K_z:  #the -10 pad
                    useranswer -= 10
                    if(useranswer < 0 ): 
                        useranswer = 0
                elif event.key == K_c:  #the -1 pad
                    useranswer -= 1
                    if(useranswer < 0 ): 
                        useranswer = 0
                elif event.key == K_a:  #the +10 pad
                    useranswer += 10
                elif event.key == K_d:  #the +1 pad
                    useranswer += 1
                elif event.key == K_x:  #the clear pad
                    useranswer = 0
                elif event.key == K_e:  #the pause pad
                    running = pause_menu()
                    if not running:
                        continue             

            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False

        draw_screen(mode,first,second,useranswer)

    #probably dont want to call this as it might end the menu too
    #pygame.quit()