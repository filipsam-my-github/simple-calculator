import pygame
import numpy as np
class TextInput:
    def __init__(self, x_cord, y_cord, width, height, maxl_size=-1, placeholder="input",rgb_font=(0,0,0)):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        
        
        self.font = pygame.font.SysFont("papyrus", 48)
        self.text = ""
        self.font_image = pygame.font.Font.render(self.font, self.text, True, rgb_font)
        
        
        self.placeholder = placeholder
        self.placeholder_img = pygame.font.Font.render(self.font, placeholder, True, (100, 100, 100))
        
        self.maxl_size = maxl_size

        self.cursor = pygame.rect.Rect(self.x_cord + 5, self.y_cord + 15, 2, 50)
        self.cursor_vis = True

        self.numbers=[None,None]
        self.operators=[None]
        self.equal=False
        
        
        
    def add_unicode(self,unicode):
        
        try:
            if len(self.text) < self.maxl_size or self.maxl_size == -1:
                local=int(unicode)
                self.text += unicode
        except:
            pass
        if -999<=TextInput.math(None,[self.text,0],True)<=999 and self.maxl_size != -1:
            if unicode==".":
                self.text += unicode
            if unicode=="+"and self.equal==False:
                self.uppdate_operators(unicode)
                self.uppdate_numbers()
            if unicode=="-"and  self.equal==False:
                self.uppdate_operators(unicode)
                self.uppdate_numbers()
            if unicode=="*"and  self.equal==False:
                self.uppdate_operators(unicode)
                self.uppdate_numbers()
            if unicode=="/"and  self.equal==False:
                self.uppdate_operators(unicode)
                self.uppdate_numbers()
        if unicode=="√" and self.equal==False:
            self.uppdate_numbers("√")      
        if unicode=="=" and self.equal:
            self.uppdate_numbers(True)
        if unicode=="x":
            self.text = ""
            self.numbers=[None,None]
            self.operators=[None]
            self.equal=False                            
                            
                
        self.font_image = pygame.font.Font.render(self.font, self.text, True, (0, 0, 0))
        text_x = self.font_image.get_width()
        self.cursor = pygame.rect.Rect(self.x_cord + 5 + text_x, self.y_cord + 15, 2, 50)
        
        
    def tick(self, clock, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:
                    return self.text
                
                elif event.key == pygame.K_BACKSPACE:
                    if len(self.text)<1:
                        self.text=""
                    else:
                        self.text = self.text[:-1]
                    
                elif len(self.text) < self.maxl_size or self.maxl_size == -1:
                    print(event.unicode)
                    try:
                        local=int(event.unicode)
                        self.text += event.unicode
                    except:
                        if event.unicode==".":
                            self.text += event.unicode
                if -999<=TextInput.math(None,[self.text,0],True)<=999:
                    if event.unicode=="+"and self.equal==False:
                        self.uppdate_operators(event.unicode)
                        self.uppdate_numbers()
                    if event.unicode=="-"and  self.equal==False:
                        self.uppdate_operators(event.unicode)
                        self.uppdate_numbers()
                    if event.unicode=="*"and  self.equal==False:
                        self.uppdate_operators(event.unicode)
                        self.uppdate_numbers()
                    if event.unicode=="/"and  self.equal==False:
                        self.uppdate_operators(event.unicode)
                        self.uppdate_numbers()
                if event.unicode=="=" and self.equal:
                    
                    self.uppdate_numbers(True)
                if event.unicode=="x":
                    self.text = ""
                    self.numbers=[None,None]
                    self.operators=[None]
                    self.equal=False
                            
                            
                        
                self.font_image = pygame.font.Font.render(self.font, self.text, True, (0, 0, 0))
                text_x = self.font_image.get_width()
                self.cursor = pygame.rect.Rect(self.x_cord + 5 + text_x, self.y_cord + 15, 2, 50)

        if round(clock) % 2 == 0:
            self.cursor_vis = True
        else:
            self.cursor_vis = False


    def draw(self, screen):
        pygame.draw.rect(screen, (4, 207, 222),(self.x_cord - 4, self.y_cord - 4, self.width + 8, self.height + 8),border_radius=20)
        pygame.draw.rect(screen, (255, 255, 255),(self.x_cord, self.y_cord, self.width, self.height),border_radius=20)
        
        if self.text:
            self.font_image = pygame.font.Font.render(self.font, self.text, True, (0, 0, 0))
            screen.blit(self.font_image, (self.x_cord + 5, self.y_cord + 15))
            
        else:
            screen.blit(self.placeholder_img, (self.x_cord + 5, self.y_cord + 15))

        if self.cursor_vis:
            pygame.draw.rect(screen, (90, 90, 90), self.cursor)
    
    
    def uppdate_operators(self,add_symbol=""):
        if add_symbol !="":
            if self.operators[0]==None:
                self.operators[0]=add_symbol
                
    
    
    def uppdate_numbers(self,equall=False):
        if equall=="√":
            self.text=TextInput.math(equall,[self.text,0])
            print(self.text)
            self.operators[0]=None
            
            self.numbers=[None,None]
            self.equal=False
        elif self.numbers[0]==None:
            self.numbers[0]=self.text
            self.text=""
            self.equal=True
        elif equall==True:
            self.numbers[1]=self.text
            print(TextInput.math(self.operators[0],self.numbers))
            self.numbers=[TextInput.math(self.operators[0],self.numbers),None]
            
            self.text=self.numbers[0]
            self.operators[0]=None
            
            self.numbers=[None,None]
            self.equal=False
    
    def math(symbol,numbers,to_float=False):
        for i in range(2):
            try:
                print(numbers)
                numbers[i]=float(numbers[i])
            except:
                print(numbers)
                numbers[i] = numbers[i][:-1]
                if numbers[i]=="":
                    numbers[i]="0"
                numbers[i]=float(numbers[i])
                
        if to_float:
            return numbers[0]
        
        max_size_number=7
        match symbol:
            case "+":
                aut_put=str((numbers[0]+numbers[1]))
                if len(aut_put)>6:
                    local_str=""
                    for i in range(max_size_number):
                        local_str+=aut_put[i]
                    aut_put=local_str
                
                return aut_put
            case "-":
                aut_put=str((numbers[0]-numbers[1]))
                if len(aut_put)>6:
                    local_str=""
                    for i in range(max_size_number):
                        local_str+=aut_put[i]
                    aut_put=local_str
                
                return aut_put
            case "*":
                aut_put=str((numbers[0]*numbers[1]))
                if len(aut_put)>6:
                    local_str=""
                    for i in range(max_size_number):
                        local_str+=aut_put[i]
                    aut_put=local_str
                
                return aut_put
            case "/":
                aut_put=str((numbers[0]/numbers[1]))
                if len(aut_put)>6:
                    local_str=""
                    for i in range(max_size_number):
                        local_str+=aut_put[i]
                    aut_put=local_str
                
                return aut_put
            case "√":
                aut_put=str((np.sqrt(numbers[0])))
                if len(aut_put)>6:
                    local_str=""
                    for i in range(max_size_number):
                        local_str+=aut_put[i]
                    aut_put=local_str
                
                return aut_put