import pygame,sys,time
from button import *
from text_input import *
pygame.init()

pygame.display.set_caption("calculator")

screen = pygame.display.set_mode((400,600))

def main(run=True):
    last_time = time.time()
    dt = time.time() - last_time
    last_time = time.time()
    
    buttons = []
    
    rgb_background={"standard":(48.7,87.4,92.4)}
    rgb_font={"standard":(0,0,0)}
    rgb_button={"standard":(35.9,56.7,43.7)}
    
    
    input=TextInput(50,50,200,75,rgb_font=rgb_font["standard"],maxl_size=3)
    
    #buttons.append(Button(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],rgb_font["standard"],rgb_button["standard"],0))
    #buttons.append(Button(50,150,rgb_font["standard"],rgb_button["standard"],0))
    #buttons.append(Button(42, 241-100,rgb_font["standard"],rgb_button["standard"],0,button_size=(170,65),font_size=int(60 * 0.9)))
    for j in range(3):
        for i in range(3):
            buttons.append(Button(82*i, 241+j*100,rgb_font["standard"],rgb_button["standard"],i+j*3+1))
    local_symbols=["+","*","-","/"]
    for j in range(2):
        for i in range(2):
            buttons.append(Button(82*(i+3), 241+j*100,rgb_font["standard"],rgb_button["standard"],local_symbols[i+j*2]))
    buttons.append(Button(82*3-10, 445,rgb_font["standard"],rgb_button["standard"],"=",button_size=(82*2,65)))
    buttons.append(Button(30, 550,rgb_font["standard"],rgb_button["standard"],"x",button_size=(90,45)))
    buttons.append(Button(142, 550,rgb_font["standard"],rgb_button["standard"],0,button_size=(70,45)))
    buttons.append(Button(142+70+10, 550,rgb_font["standard"],rgb_button["standard"],".",button_size=(70,45)))
    buttons.append(Button(142+140+20, 515,rgb_font["standard"],rgb_button["standard"],"√",button_size=(70,80)))
    while run:
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()
        
        events=pygame.event.get()
        
        
        for event in events:
            if event.type == pygame.QUIT:
                run=False
                sys.exit()
            if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run=False
                sys.exit()
        #warstwy
        screen.fill(rgb_background["standard"])
        
        input.tick(time.time(),events)
        input.draw(screen)
        
        for button in buttons:
            button.draw(screen)
            if button.active==True:
                input.add_unicode(str(button.returned))
                button.active=False
               
        #buttons[0].set_pos(pygame.mouse.get_pos())
        #buttons[0].draw(screen)   
              
              
        pygame.display.update()

if __name__ == "__main__":
    main()