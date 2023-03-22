import pygame
pygame.font.init()
pygame.init()
class Button:
    mouse_rect=pygame.rect.Rect(pygame.mouse.get_pos(),(1,1))
    def __init__(self,x_cord,y_cord,rgb_font,rgb_box,returned,button_size=(60,85),font_size=None) -> object:
        self.box_rgb=rgb_box
        
        self.rect=pygame.rect.Rect((x_cord,y_cord),button_size)
        
        if font_size==None:
            font_size = int(button_size[0] * 0.9)
        font = pygame.font.SysFont("papyrus", font_size)
        self.box_text = font.render(str(returned), True, rgb_font)
        
        text_width, text_height = font.size(str(returned))
        x_offset = (button_size[0] - text_width) // 2
        y_offset = (button_size[1] - text_height) // 2
        self.text_pos = (self.rect.x + x_offset, self.rect.y + y_offset)
        
        self.couldown=True
        self.active=False
        self.returned=returned
    def draw(self, screen):
        Button.mouse_rect.x,Button.mouse_rect.y=pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()==(0,0,0):
            self.couldown=True
            
        if Button.mouse_rect.colliderect(self.rect):
            if self.couldown and pygame.mouse.get_pressed()!=(0,0,0):
                self.couldown=False
                self.active=True
        
        pygame.draw.rect(screen, self.box_rgb, self.rect)
        screen.blit(self.box_text, self.text_pos)
        
    def set_pos(self, list_cord):
        self.rect.x = list_cord[0]
        self.rect.y = list_cord[1]
        
#a = Button(50, 150, (26,31,28), (26,31,28), 1)
#pygame.init()
#screen = pygame.display.set_mode((400, 400))
#a.draw(screen)
#pygame.display.flip()
#pygame.time.wait(2000)