import pygame,sys,time,math
from pygame.locals import *
import _elementtree
import xml.etree.ElementTree as ET

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

def quit_map():
    pygame.quit()
    quit()

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        splashscreen = pygame.image.load('assets/splashscreen.png')
        screen.blit(splashscreen,(0,0))
        button('START',(255,255,255),300,330,100,50,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),main_loop) #no () for display_map
        button('QUIT',(255,255,255),600,330,100,50,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),quit_map)
        pygame.display.update()
        clock.tick(15)
        
        #time.sleep(2)
        #break

def circular_button(text,text_colour,x_center,y_center,radius,color_inactive,color_active,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() #return [left,scroll,right] (1 for click)
    mouse_x = float(mouse[0])
    mouse_y = float(mouse[1])
    if math.sqrt((mouse_x-x_center)**2+(mouse_y-y_center)**2) <= float(radius): 
        pygame.draw.circle(screen, color_active, (x_center,y_center),radius) #(top,left,width,height)
        if click[0] ==1 and action != None: #when you click and have predefined action
            action() #add()
    else:
        pygame.draw.circle(screen, color_inactive, (x_center,y_center),radius)
    message_display(text,30,text_colour,(x_center),(y_center))

def move_left():
    global map_blit_x
    map_blit_x += 10
    screen.fill(white)
    screen.blit(NTUmap,(map_blit_x,map_blit_y))

def move_right():
    global map_blit_x
    map_blit_x -= 10
    screen.fill(white)
    screen.blit(NTUmap,(map_blit_x,map_blit_y))

def move_up():
    global map_blit_y
    map_blit_y += 10
    screen.fill(white)
    screen.blit(NTUmap,(map_blit_x,map_blit_y))

def move_down():
    global map_blit_y
    map_blit_y -= 10
    screen.fill(white)
    screen.blit(NTUmap,(map_blit_x,map_blit_y))

def zoom_in():
    global map_width
    global map_height
    global NTUmap
    map_width += 50
    map_height += 50
    screen.fill(white)
    NTUmap = pygame.image.load("assets/NTUmap_view.png")
    NTUmap = pygame.transform.scale(NTUmap,(map_width,map_height))
    screen.fill(white)
    screen.blit(NTUmap,(map_blit_x,map_blit_y))

def zoom_out():
    global map_width
    global map_height
    global NTUmap
    map_width -= 50
    map_height -= 50
    screen.fill(white)
    NTUmap = pygame.image.load("assets/NTUmap_view.png")
    NTUmap = pygame.transform.scale(NTUmap,(map_width,map_height))
    screen.fill(white)
    screen.blit(NTUmap,(map_blit_x,map_blit_y))

def reset_map():
    global NTUmap
    global map_blit_x
    global map_blit_y
    global map_width
    global map_height
    NTUmap = pygame.image.load("assets/NTUmap_view.png")
    map_width = width
    map_height = height
    NTUmap = pygame.transform.scale(NTUmap,(map_width,map_height))
    screen.fill(white)
    screen.blit(NTUmap,(0,0))
    map_blit_x = 0
    map_blit_y = 0

def search_view():
    global active_map_view
    screen.fill(black)
    active_map_view = False

def move_map():
    global active_map_view
    global gui_length
    global ntumap_length
    global ntumap_width
    global width
    global height
    global screen
    global map_width
    global map_height
    global map_blit_x
    global map_blit_y
    global NTUmap
    active_map_view = True
    width = 900
    height = 690
    map_width = width
    map_height = height
    map_blit_x = 0
    map_blit_y = 0
    NTUmap = pygame.image.load("assets/NTUmap_view.png")
    NTUmap = pygame.transform.scale(NTUmap,(map_width,map_height))
    screen = pygame.display.set_mode((width,height))
    screen.blit(NTUmap,(map_blit_x,map_blit_y))
    while active_map_view == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
        button("reset",red,810,530,80,40,color_inactive,color_active,reset_map)
        circular_button("<",black,750,630,20,color_inactive,color_active,move_left)
        circular_button(">",black,810,630,20,color_inactive,color_active,move_right)
        circular_button("^",black,780,600,20,color_inactive,color_active,move_up)
        circular_button("v",black,780,660,20,color_inactive,color_active,move_down)
        circular_button("+",black,870,600,20,color_inactive,color_active,zoom_in)
        circular_button("-",black,870,660,20,color_inactive,color_active,zoom_out)
        button("search",red,810,480,80,40,color_inactive,color_active,search_view)
        pygame.display.update()
        clock.tick(15)
    screen.fill(black)
    gui_length = 250
    ntumap_length = 800
    ntumap_width = 589
    width = ntumap_length + gui_length
    height = ntumap_width
    screen = pygame.display.set_mode((width,height))
    redraw()

"""Marcus"""

def splashscreen(sleeptime):#Marcus
    splashscreen = pygame.image.load('assets/splashscreen.png')
    screen.blit(splashscreen,(0,0))
    pygame.display.update()
    time.sleep(sleeptime)

def redraw():#Marcus - redraws all static elements on the screen. Use draw_GUI for static GUI elements.
    global node_connections
    draw_NTU()
    draw_GUI()
    DrawNodes()
    drawConnections(node_connections,(128,0,0))
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

def textbox():#textbox system
    global active
    global textbox_active_mouseover
    global input_box
    global inputbox_text
    font_size = 28
    textbox_img = pygame.image.load('assets/textbox_bg.png')
    input_box = pygame.Rect(5, 5, 235, 40) #(left,top,width,height): store rectangle coordinates
    color_active = pygame.Color('lightskyblue3') #color when the input_box is inactive: blurred blue
    color_inactive = pygame.Color('dodgerblue2') #color when the input_box is active
    color_font = (255,255,255)
    color = color_active if active or textbox_active_mouseover else color_inactive#if active else color_inactive
    font_textbox = pygame.font.SysFont('Segoe UI Semibold', font_size)
    text_width,text_height = font_textbox.size(inputbox_text)
    while text_width > 225:
        font_size -= 1
        font_textbox = pygame.font.SysFont('Segoe UI Semibold', font_size)
        text_width,text_height = font_textbox.size(inputbox_text)
    txt_surface = font_textbox.render(inputbox_text, True, color_font)
    screen.blit(textbox_img,(5,5))
    screen.blit(txt_surface, (input_box.x+5, input_box.y))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.update() 

def mode_button():
    global active_modebutton
    global active_mouseover_modebutton
    global mode
    modebutton_fontsize = 28
    modebutton_img = pygame.image.load('assets/textbox_bg.png')
    
    
    
    
def MouseClickDisplayDotPos():#Marcus
    dot_pos_display = [dot_pos[0]-250,dot_pos[1]]
    font_gui_currentpos = pygame.font.SysFont('Segoe UI', 25)
    gui_currentpos = font_gui_currentpos.render("Current Position: " + str(dot_pos_display), True, (0, 0, 0))
    screen.blit(gui_currentpos,(5,50))
    if dot_pos[0] > gui_length:
        pygame.draw.circle(screen, (255,0,0), dot_pos, 5)
        font_map_youarehere = pygame.font.SysFont('Segoe UI', 15)
        display_mousedot = font_map_youarehere.render("You are here!", True, (255, 0, 0))
        screen.blit(display_mousedot, (dot_pos[0]+10,dot_pos[1]-10))

def MouseClickSavePosition():
    global dot_pos
    dot_pos = pygame.mouse.get_pos()
    dot_pos_display_value = [dot_pos[0]-250,dot_pos[1]]

def DrawNodes():
    global root
    lst = []
    for child in root:
        xypos = []
        for value in child:
            if value.tag == 'posx':
                xypos.append(int(value.text))
            if value.tag == 'posy':
                xypos.append(int(value.text))
        lst.append(xypos)
        font_nodename = pygame.font.SysFont('Segoe UI Semibold',10)
        nodename = font_nodename.render(child.attrib['name'][-3:],True,(255,0,0))
        screen.blit(nodename,(xypos[0]+255,xypos[1]))
    for c in lst:
        pygame.draw.circle(screen,(255,0,0),(c[0]+250,c[1]),5)

def GenerateConnections():
    global root
    connectionlist = []
    dct = {}
    for child in root:
        for value in child:
            if value.tag == 'posx':
                posx = int(value.text)
            elif value.tag == 'posy':
                posy = int(value.text)
        dct[str(child.attrib['name'])] = (posx,posy)
    print(dct)
    for child in root:
        for value in child:
            if value.tag == 'connected' and value.text != None:
                connectionlist.append((dct[str(child.attrib['name'])], dct[value.text]))
    for pair in connectionlist:
        if (pair[1],pair[0]) not in connectionlist:
            connectionlist.append((pair[1],pair[0]))
    return connectionlist

def GenerateNodes():
    global root
    nodelist = []
    for child in root:
        xypos = []
        name = child.attrib['name']
        for value in child:
            if value.tag == 'posx':
                posx = int(value.text)
            elif value.tag == 'posy':
                posy = int(value.text)
        xypos = (posx,posy)
        nodelist.append((name,xypos))
    return nodelist

def drawConnections(connectionlist,colour):
    for pair in connectionlist:
        pygame.draw.line(screen,colour,(pair[0][0]+250,pair[0][1]),(pair[1][0]+250,pair[1][1]),3)

def findNearestNode(node_check,nodelist):
    global dot_pos_display_value
    nearestNodes = []
    distancelist = []
    for node in nodelist:
        distance = math.sqrt(((abs(node_check[0]-node[1][0]))**2) + (abs(node_check[1]-node[1][1]))**2)
        distancelist.append((distance,node[1]))
    print (min(distancelist))
    return min(distancelist)

def graphSearch(initial_node,final_node,connections, weight_start,weight_end,weight_variation,denom):
    connections_collection = []
    total_distance = []
    for k in range(weight_start,weight_end,weight_variation):
        nodequeue = [initial_node]
        result_connection = []
        result_connection_intermediate = []
        searched_nodes = []
        distance = {}
        internalconnectionlist = {}
        totaldistance_path = 0
        prev_node = initial_node
        for n in connections:
            internalconnectionlist[n[0]] = []
        for n in connections:
            internalconnectionlist[n[0]].append(n[1])
        for n in connections:
            distance[n[0]] = math.sqrt(abs(final_node[0]-n[0][0])**2+abs(final_node[1]-n[0][1])**2)
        while nodequeue != []:
            current_node = nodequeue[0]
            nodequeue.pop(0)
            searched_nodes.append(current_node)
            result_connection_intermediate.append(current_node)
            if current_node == final_node:
                break
            distancelist = []
            for c in internalconnectionlist[current_node]:
                if c not in searched_nodes and c not in nodequeue:
                    nodequeue.append(c)
            distancelist = []
            for c in nodequeue:
                distancelist.append((((k*distance[c])+(denom*math.sqrt(abs(current_node[0]-c[0])**2+abs(current_node[1]-c[1])**2))),c))
            distancelist.sort()
            nodequeue = []
            for c in distancelist:
                    nodequeue.append(c[1])
            totaldistance_path += math.sqrt(abs(current_node[0]-prev_node[0])**2+abs(current_node[1]-prev_node[1])**2)
            prev_node = current_node
        for i in range(len(result_connection_intermediate)-1):
            result_connection.append((result_connection_intermediate[i],result_connection_intermediate[i+1]))
        connections_collection.append((totaldistance_path,result_connection))
    connections_collection.sort()
    return(connections_collection[0][1])

def closestCanteen(initial_node):
    global root



def main_loop():
    move_map()
    redraw()
    global active
    global inputbox_text
    global textbox_active_mouseover
    global input_box
    global click_box
    global nodes
    global node_connections
    global instance_node_connections
    global instance_nodes
    
    while True:
        button("map view",black,940,530,100,40,color_inactive,color_active,move_map)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if input_box.collidepoint(event.pos): #test if mouse is in textbox
                    textbox_active_mouseover = True
                    textbox()
                else:
                    textbox_active_mouseover = False
                    textbox()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  click_box.collidepoint(event.pos) and event.button == 1:#test if mouse is on map
                    instance_node_connections = GenerateConnections()
                    instance_nodes = GenerateNodes()
                    instance_node_connections.append(((event.pos[0]-250,event.pos[1]),findNearestNode((event.pos[0]-250,event.pos[1]),instance_nodes)[1]))
                    instance_nodes.append(('MousePos',(event.pos[0]-250,event.pos[1])))
                    print(instance_node_connections)
                    redraw()
                    MouseClickSavePosition()
                    MouseClickDisplayDotPos()
                    solution_connection = graphSearch((event.pos[0]-250,event.pos[1]),(416,241),instance_node_connections,1,10,1,5)
                    drawConnections(solution_connection,(255,0,0))
                    pygame.display.update()
                if input_box.collidepoint(event.pos): #test if mouse is in textbox
                    active = True
                    textbox()
                else:
                    active = False
                    textbox()
            if event.type == pygame.KEYDOWN and active:#update text box
                if event.key == pygame.K_RETURN: #press Enter
                    inputbox_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    inputbox_text = inputbox_text[:-1]
                else:
                    inputbox_text += event.unicode #add the character that has already translated from keypress           
                textbox()
       

#initialize all variables and objects
pygame.init()#initialize pygame
pygame.font.init()#-initialize font library for pygame
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
graph = ET.parse('node_data.xml')
root = graph.getroot()
gui_length = 250
ntumap_length = 800
ntumap_width = 589
node_connections = GenerateConnections()
nodes = GenerateNodes()
instance_node_connections = []
instance_nodes = []
current_connections = []
input_box = pygame.Rect(5, 5, 200, 40)
click_box = pygame.Rect(250,0,800,589)
mode_button_box = pygame.Rect(5,50,235,50)
width = ntumap_length + gui_length
height = ntumap_width
inputbox_text = ""
dot_pos = (2000,2000)
dot_pos_display_value = (2000,2000)
pygame.key.set_repeat(200,75)
screen = pygame.display.set_mode((width,height)) #initialize screen area with width*height pixels
pygame.display.set_caption('CZ1003 Mini-Project')
active = False
textbox_active_mouseover = False
active_modebutton = False
active_mouseover_modebutton = False
mode = 1
print(nodes)
splashscreen(2)
intro()
main_loop()
