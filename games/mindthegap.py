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

MODE_MAX = [12]
MODE_MIN = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TITLE_FONT = pygame.font.SysFont('comicsans',60)
QUESTION_FONT = pygame.font.SysFont('comicsans',30)
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

#the end menu
def end_menu(score):
    screen.fill((215,215,215))
    title_text = TITLE_FONT.render("Times up!",1,(0,0,0))
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2,150))

    score_text = INFO_FONT.render("Your Score was: " + str(score),1,(0,0,0))
    screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2,350))  

    pygame.display.flip() 
    while True: 
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                return False
            elif event.type == QUIT:
                return False

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

#this sets the maximum for the answer scaling
def set_MODE_MAX(mode): 
    if(mode == 'ADD'):
        MODE_MAX[0] = 24
        return
    if(mode == 'MULTI'): 
        MODE_MAX[0] = 144
        return
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
def generate(mode):
    a , b = 0 , 0
    while(1):
        a = randint(0,12)
        b = randint(0,12)
        if(check(mode,a,b)):
            break
    return a , b



#TODO instructions
#draw any updates to the screen
def draw_screen(mode,useranswer,userscore,question_list):
    
    
    screen.fill((0,95,170))
    
    titlesurf = pygame.Surface((SCREEN_WIDTH,140)).fill((0,0,0))
    pygame.draw.rect(screen,(0,65,120),titlesurf)
    title_text = TITLE_FONT.render("Mind the Gap",1,(255,255,255))
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2,titlesurf.height/2 -title_text.get_height()/2))
    
    playsurf = pygame.Rect(
        0,
        SCREEN_HEIGHT/2 + titlesurf.height/2 - SCREEN_WIDTH*(3/16), 
        SCREEN_WIDTH,
        SCREEN_WIDTH*(3/8) 
        )
    pygame.draw.rect(screen,(255,255,255),playsurf)

    for bar in question_list:
        newbar = pygame.Rect(
            bar[0],
            SCREEN_HEIGHT/2 + 70 - SCREEN_WIDTH*(3/16), 
            40,
            SCREEN_WIDTH*(3/8)
        )            
        pygame.draw.rect(screen,(0,190,0),newbar)

        answer = operation(mode,bar[1],bar[2])
        
        answer_cube = pygame.Rect(
            bar[0],
            newbar.top + ((SCREEN_WIDTH*(3/8)-60)*(MODE_MAX[0]-answer)/MODE_MAX[0]),    #scaling algorithm
            40,
            60
        )   
        pygame.draw.rect(screen,(255,255,255),answer_cube)   #same color as background
        #display each question    
        if(mode == 'ADD'):
            question = str(bar[1]) + " + " +str(bar[2])
        if(mode =='SUB'): 
            question = str(bar[1]) + " - " +str(bar[2])
        if(mode == 'MULTI'): 
            question = str(bar[1]) + " x " +str(bar[2])
        if(mode == 'DIV'): 
            question = str(bar[1]) + " " + chr(247) + " " + str(bar[2])
        question_text = QUESTION_FONT.render(question,1,(0,0,0))
        screen.blit(question_text,(newbar.centerx - question_text.get_width()/2 ,newbar.bottom))


    ua_cube = pygame.Rect(
        SCREEN_WIDTH*(3/16),
        playsurf.top + ((SCREEN_WIDTH*(3/8)-60)*(MODE_MAX[0]-useranswer)/MODE_MAX[0]) +10,
        40,
        40
    )
    pygame.draw.rect(screen,(255,0,0),ua_cube)
    useranswer_text = QUESTION_FONT.render(str(useranswer),1,(0,0,0))
    screen.blit(useranswer_text,(ua_cube.centerx - useranswer_text.get_width()/2,ua_cube.centery - useranswer_text.get_height()/2))
    # first_text = QUESTION_FONT.render(str(first),1,(0,0,0))
    # modetext = 0
    # if(mode == 'ADD'):
    #     modetext = QUESTION_FONT.render('+',1,(0,0,0))
    # elif(mode == 'SUB'):
    #     modetext = QUESTION_FONT.render('-',1,(0,0,0))
    # elif(mode == 'MULTI'):
    #     modetext = QUESTION_FONT.render('x',1,(0,0,0))
    # elif(mode == 'DIV'):
    #     modetext = QUESTION_FONT.render(chr(247),1,(0,0,0))
    # else: 
    #     print(" invalid mode: "+ str(mode))
    #     exit()
    # second_text = QUESTION_FONT.render(str(second),1,(0,0,0))
    # answer_text = QUESTION_FONT.render(str(useranswer),1,(0,0,0))

    score_text = INFO_FONT.render("Score: "+ str(userscore),1,(0,0,0))
    screen.blit(score_text,(30,titlesurf.height + 15))

    # Update the display
    pygame.display.flip()

#this will eventually contain everything
def game():

    
    mode = utils.MODE[0]
    set_MODE_MAX(mode)

    #initialize game
    pygame.init()

    running = True

    #first , second = generate(mode)
    useranswer = 0
    userscore = 0
    question_list = []  #this will store the x position of the bar as well as the number in the equation

    first , second = generate(mode)
    question_list.append([SCREEN_WIDTH-60,first,second])

    clock = pygame.time.Clock()
    counter = 0
    pygame.time.set_timer(pygame.USEREVENT,100)     #1000 would be 1 sec

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
            if event.type == pygame.USEREVENT:
                #if there is a bar already on the screen, then move it
                if question_list:
                    for bar in question_list:
                        bar[0] -= 4

                #number in the if statement should be 10x the amount of seconds
                if counter % 70 ==0 and counter != 0: 
                    #generate new bar here
                    first , second = generate(mode)
                    question_list.append([SCREEN_WIDTH-60,first,second])


                counter += 1 

            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False

            if question_list[0][0] < (SCREEN_WIDTH*(3/16) + 35):    #if the leftmost bar reaches the answer cube
                if useranswer == operation(mode, question_list[0][1],question_list[0][2]):
                    userscore += 1
                    question_list.pop(0)
                else:
                    running = end_menu(userscore)
                    continue

        draw_screen(mode,useranswer,userscore,question_list)
        clock.tick(60)

    #probably dont want to call this as it might end the menu too
    #pygame.quit()
