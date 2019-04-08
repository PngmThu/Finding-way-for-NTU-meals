import pygame, time, sys
from pygame.locals import *
import pygame as pg

"""Modules"""

"""Olris has added"""

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0)) #the diplayed text setup
    #create the coordinates(textRect) of the rect surrounding the text
    textRect = textSurface.get_rect()
    return textSurface, textRect

def message_display(text,size,colour,x_center,y_center):
    font2 = pygame.font.Font('freesansbold.ttf',size)

    TextSurf = font2.render(text, True, colour)
    TextRect = TextSurf.get_rect()
    
    #create the displayed text(TextSurf) with its coordinates of rect(TextRect)
    #TextSurf, TextRect = text_objects(text, font2)
    #set the center of the rect at (x,y): this is at the center of the screen display
    TextRect.center = (x_center,y_center)
    #Draw the text on the screen with at (x,y)
    screen.blit(TextSurf, TextRect)

    pygame.display.update() #display rectangles

def button(text,text_colour,x,y,width,height,color_inactive,color_active,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() #return [left,scroll,right] (1 for click)
    if x < mouse[0] < x+width and y < mouse[1] < y+height: #[0]: x, [1]: y
        pygame.draw.rect(screen, color_active, (x,y,width,height),3) #(top,left,width,height)
        if click[0] ==1 and action != None: #when you click and have predefined action
            action() #add()
    else:
        pygame.draw.rect(screen, color_inactive, (x,y,width,height),3)
    message_display(text,20,text_colour,(x+(width/2)),(y+(height/2)))

def map_view():
    pygame.display.set_caption('CZ1003 Mini-Project')
    splashscreen(2)
    redraw()

    UI_mode = 1

    while True:
        while UI_mode == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if input_box.collidepoint(event.pos): #test if mouse is in textbox
                        textbox_active_mouseover = True
                    else:
                        textbox_active_mouseover = False
                    textbox()
                    MouseClickDisplayDotPos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  click_box.collidepoint(event.pos) and event.button == 1:#test if mouse is on map
                        MouseClick()
                        MouseClickDisplayDotPos()
                        pygame.display.update()
                    if input_box.collidepoint(event.pos): #test if mouse is in textbox
                        active = True
                    else:
                        active = False
                    textbox()
                    MouseClickDisplayDotPos()
                if event.type == pygame.KEYDOWN and active:#update text box
                    if event.key == pygame.K_RETURN: #press Enter
                        inputbox_text = ''
                        textbox()
                    elif event.key == pygame.K_BACKSPACE:
                        inputbox_text = inputbox_text[:-1]
                    else:
                        inputbox_text += event.unicode #add the character that has already translated from keypress           
                    textbox()

def quit_map():
    pygame.quit()
    quit()
    

def intro():
    into = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        font3 = pygame.font.SysFont('arial', 100)
        intro_text, intro_rect = text_objects("Welcome to NTU map", font3)
        intro_rect.center = ((width/2),(height/2 - 80))
        screen.blit(intro_text,intro_rect)

        button('START',red,300,330,100,50,color_inactive,color_active,map_view) #no () for display_map
        button('QUIT',red,600,330,100,50,color_inactive,color_active,quit_map)


        
        pygame.display.update()
        clock.tick(15)
        
        #time.sleep(2)
        #break

"""Marcus"""


def splashscreen(sleeptime):#Marcus
    splashscreen = pygame.image.load('assets/splashscreen.png')
    screen.blit(splashscreen,(0,0))
    pygame.display.update()
    time.sleep(sleeptime)

def redraw():#Marcus - redraws all static elements on the screen. Use draw_GUI for static GUI elements.
    draw_NTU()
    draw_GUI()
    textbox()
    pygame.display.update()

def draw_GUI():#Marcus Add static gui elements here.
    def BG():
        GUIBG = pygame.image.load('assets/guibg.png')#loads grey-box background image for gui
        screen.blit(GUIBG,(0,0))#blits gui bg
    BG()

def draw_NTU():#Marcus Add static gui elements here.
    NTUmap = pygame.image.load('assets/NTUMap.png')#loads ntu map
    screen.blit(NTUmap,(gui_length,0))#blits ntu map

def textbox():#Olris
    global active
    global input_box
    global inputbox_text
    font_size = 25
    textbox_img = pygame.image.load('assets/textbox_bg.png')
    input_box = pygame.Rect(5, 5, 200, 40) #(left,top,width,height): store rectangle coordinates
    color_active = pygame.Color('lightskyblue3') #color when the input_box is inactive: blurred blue
    color_inactive = pygame.Color('dodgerblue2') #color when the input_box is active
    color = color_active if active or textbox_active_mouseover else color_inactive#if active else color_inactive
    font_textbox = pygame.font.SysFont('Segoe UI', font_size)
    text_width,text_height = font_textbox.size(inputbox_text)
    while text_width > 190:
        font_size -= 1
        font_textbox = pygame.font.SysFont('Segoe UI', font_size)
        text_width,text_height = font_textbox.size(inputbox_text)
    txt_surface = font_textbox.render(inputbox_text, True, color)
    screen.blit(textbox_img,(5,5))
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.update() 
                
def MouseClickDisplayDotPos():#Marcus
    redraw()
    dot_pos_display = [dot_pos[0]-250,dot_pos[1]]
    font_gui_currentpos = pygame.font.SysFont('Segoe UI', 25)
    gui_currentpos = font_gui_currentpos.render("Current Position: " + str(dot_pos_display), True, (0, 0, 0))
    screen.blit(gui_currentpos,(5,50))
    if dot_pos[0] > gui_length:
        pygame.draw.circle(screen, (255,0,0), dot_pos, 5)
        font_map_youarehere = pygame.font.SysFont('Segoe UI', 15)
        display_mousedot = font_map_youarehere.render("You are here!", True, (255, 0, 0))
        screen.blit(display_mousedot, (dot_pos[0]+10,dot_pos[1]-10))
    pygame.display.update()

def MouseClick():
    global dot_pos
    dot_pos = pygame.mouse.get_pos()
    dot_pos_display_value = [dot_pos[0]-250,dot_pos[1]]

class Node(): #for a*
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
        

"""Main"""    

pygame.init()
clock = pygame.time.Clock() #create an object to help track time
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

#Marcus#
pygame.font.init()#-initialize font library for pygame
gui_length = 250
ntumap_length = 800
ntumap_width = 589
width = ntumap_length + gui_length
height = ntumap_width
inputbox_text = ""
dot_pos = (2000,2000)
dot_pos_display_value = (2000,2000)
input_box = pygame.Rect(5, 5, 200, 40)
click_box = pygame.Rect(250,0,800,589)
search_input_box = pygame.Rect(205,5,45,40)
active = False
textbox_active_mouseover = False
pygame.key.set_repeat(200,100)
screen = pygame.display.set_mode((width,height))
#Marcus#

color_inactive = pygame.Color('lightskyblue3') #color when the button is inactive: blurred blue
color_active = pygame.Color('dodgerblue2') #color when the button is active

intro()

pygame.display.flip()
