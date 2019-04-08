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


"""Search"""

def result_display(text,size,colour,x,y):
    font2 = pygame.font.Font('freesansbold.ttf',size)

    TextSurf = font2.render(text, True, colour)
    TextRect = TextSurf.get_rect()
    TextRect.topleft = (x,y)
    #Draw the text on the screen with at (x,y)
    screen.blit(TextSurf, TextRect)

    pygame.display.update() #display rectangles


def search_by_price(max_price):
    output_list = []
    for canteen in root2:
        count = 0
        for food in canteen:
            if float(food[1].text) <= float(max_price):
                name = food[0].text
                price = food[1].text
                if count == 0:
                    output_list.append((canteen.attrib['name'],name.title(),price))
    print(output_list)

def sort_by_rank(foodname):
    rank_results = []
    for canteen in root2:
        for food in canteen:
            if foodname.lower() in food[0].text:
                rank_results.append(int(canteen.attrib['rank']))
                break                
    rank_results.sort()
    return rank_results

def display_by_rank(foodname):
    rank_results = sort_by_rank(foodname)
    result = 0
    line_y = 108
    result_display("Results for "+inputbox_text+" by rank:",12,black,0,line_y)
    for ranking in rank_results:
        for canteen in root2:
            count = 0
            if ranking == int(canteen.attrib['rank']):
                for food in canteen:
                    if foodname.lower() in food[0].text:
                        name = food[0].text
                        price = food[1].text
                        if count == 0:
                            line_y += 20
                            result_display(canteen.attrib['name']+' (rank: '+canteen.attrib['rank']+')',12,black,0,line_y)
                            line_y += 20
                            result_display('-'+name.title()+'($'+price+')',12,black,0,line_y)
                            count=1
                            result += 1
                        else:
                            line_y += 20
                            result_display('-'+name.title()+'($'+price+')',12,black,0,line_y)
                            result += 1
    line_y += 20
    result_display("=> Total:"+str(result)+"results",12,black,0,line_y)


def connectionDistance(node_name):
    global root
    global instance_node_connections
    posx = 0
    posy = 0
    for child in root:
        if child.attrib['name'] == node_name:
            for value in child:
                if value.tag == 'posx':
                    posx = int(value.text)
                elif value.tag == 'posy':
                    posy = int(value.text)
    returnval = graphSearch((mouse_pos[0]-250,mouse_pos[1]),(posx,posy),instance_node_connections,1,10,1,5)[0]
    return round(returnval,0)

def search_food_byClosestCanteen(foodname,initial_node):
    result = 0
    line_y = 108
    result_display("Results for "+inputbox_text,12,black,0,line_y)
    canteen_results = []
    distance_dct = {}
    canteen_sorted = []
    distance_sorted = []
    for canteen in root2:
        for food in canteen:
            if foodname.lower() in food[0].text:
                canteen_results.append(canteen.attrib['name'])
                break
    for i in range(len(canteen_results)):
        for canteen in root:
            if canteen_results[i] == canteen.attrib['name']:
                distance = connectionDistance(canteen_results[i])
                distance_dct[canteen_results[i]] = distance
                distance_sorted.append(distance)
                break
    distance_sorted.sort()
    for i in range(len(distance_sorted)):
        for canteen in distance_dct:
            if distance_dct[canteen] == distance_sorted[i]:
                canteen_sorted.append(canteen)
                break
            else:
                print(0)
    for canteen in canteen_sorted:
        for canteen_data in root2:
            if canteen == canteen_data.attrib['name']:
                count = 0
                for food in canteen_data:
                    if foodname.lower() in food[0].text:
                        name = food[0].text
                        price = food[1].text
                        if count == 0:
                            line_y += 20
                            result_display(canteen_data.attrib['name'],12,black,0,line_y)
                            line_y += 20
                            result_display('- '+name.title()+' ($'+price+')',12,black,0,line_y)
                            count=1
                            result += 1
                        else:
                            line_y += 20
                            result_display('- '+name.title()+' ($'+price+')',12,black,0,line_y)
                            result += 1
                break
    line_y += 20                
    result_display("=> Total: "+str(result)+" results",12,black,0,line_y)

"""Marcus"""

def splashscreen(sleeptime):#Marcus
    splashscreen = pygame.image.load('assets/splashscreen.png')
    screen.blit(splashscreen,(0,0))
    pygame.display.update()
    time.sleep(sleeptime)

def redraw():#Marcus - redraws all static elements on the screen. Use draw_GUI for static GUI elements.
    global resultbutton_active
    global resultbutton_active_mouseover
    global resultbutton_img
    global node_connections
    draw_NTU()
    draw_GUI()
    textbox()
    modebutton()
    redrawButtons()
    button("map view",black,940,530,100,40,color_inactive,color_active,move_map)
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
    font_size = 30
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
    screen.blit(txt_surface, (input_box.x+5, ((input_box.y-text_height)//2)+20))
    pygame.draw.rect(screen, color, input_box, 2)

def modebutton():
    global modebutton_active_mouseover
    global mode
    global modebutton_box
    modebutton_font_size = 28
    modebutton_img = pygame.image.load("assets/modebutton_bg.png")
    modebutton_box = pygame.Rect(5, 50, 235, 50)
    modebutton_color_active = pygame.Color('lightskyblue3')
    modebutton_color_inactive = pygame.Color('dodgerblue2')
    modebutton_color_font = (255,255,255)
    modebutton_color = modebutton_color_active if modebutton_active_mouseover else modebutton_color_inactive
    font_modebutton = pygame.font.SysFont('Segoe UI Semibold',modebutton_font_size)
    if mode == 1:
        mode_text = "Distance"
    elif mode == 2:
        mode_text = "Maximum Price"
    elif mode == 0:
        mode_text = "Rank"
    modebutton_txt_surface = font_modebutton.render(mode_text, True, modebutton_color_font)
    modebutton_textwidth, foo = font_modebutton.size(mode_text)
    screen.blit(modebutton_img,(5,50))
    screen.blit(modebutton_txt_surface,((250-modebutton_textwidth)//2,modebutton_box.y+5))
    pygame.draw.rect(screen, modebutton_color, modebutton_box,2)

def MouseClickDisplayDotPos():#Marcus
    global debug_mode
    global node_connections
    dot_pos_display = [dot_pos[0]-250,dot_pos[1]]
    if debug_mode == True:
        font_gui_currentpos = pygame.font.SysFont('Segoe UI', 20)
        gui_currentpos = font_gui_currentpos.render("Current Position: " + str(dot_pos_display), True, (0, 0, 0))
        screen.blit(gui_currentpos,(255,5))
        debugmodestatus = font_gui_currentpos.render("Debug Mode : On",True, (0,0,0))
        screen.blit(debugmodestatus,(900,5))
        drawConnections(node_connections,(128,0,128))
        DrawNodes()
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

def drawMultipleConnections(connection_list_multiple,colour):
    for connectionlist in connection_list_multiple:
        for pair in connectionlist:
            pygame.draw.line(screen,colour,(pair[0][0]+250,pair[0][1]),(pair[1][0]+250,pair[1][1]),3)

def findNearestNode(node_check,nodelist):
    global dot_pos_display_value
    nearestNodes = []
    distancelist = []
    for node in nodelist:
        distance = math.sqrt(((abs(node_check[0]-node[1][0]))**2) + (abs(node_check[1]-node[1][1]))**2)
        distancelist.append((distance,node[1]))
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
    return(connections_collection[0][0],connections_collection[0][1])

def closestCanteenConnection(initial_node,number,connections):
    global root
    name = 'Canteen'
    nodelist = []
    distancelist = []
    returnlist = []
    distancereturnlist = []
    for child in root:
        if name in child.attrib['name']:
            posx = 0
            posy = 0
            for value in child:
                if value.tag == 'posx':
                    posx = int(value.text)
                elif value.tag == 'posy':
                    posy = int(value.text)
            nodelist.append((posx,posy))
    for final_node in nodelist:
        distancelist.append(graphSearch(initial_node,final_node,connections, 1,10,1,5))
    distancelist.sort()
    for c in range(number):
        returnlist.append(distancelist[c][1])
        distancereturnlist.append(distancelist[c][0])
    return distancereturnlist, returnlist

def generateResultButtonActiveMouseover(posx,posy,width,height,colour_active,colour_inactive,image,activeval,mouseoveractive_val,line1,line2,line3,line4,font_colour):
    button_colour = colour_active if activeval or mouseoveractive_val else colour_inactive
    longeststring = line1
    try:
        len(line2)
    except:
        pass
    else:
        if len(line2) > len(longeststring):
            longeststring = line2
    try:
        len(line3)
    except:
        pass
    else:
        if len(line3) > len(longeststring):
            longeststring = line3
    try:
        len(line4)
    except:
        pass
    else:
        if len(line4) > len(longeststring):
            longeststring = line4
    linecount = 0
    button_text_size = 50
    if line1 is not None:
        linecount += 1
    if line2 is not None:
        linecount += 1
    if line3 is not None:
        linecount += 1
    if line4 is not None:
        linecount += 1
    font_button = pygame.font.SysFont('Segoe UI Semibold',button_text_size)
    text_width, text_height = font_button.size(longeststring)
    while (linecount*text_height)+(linecount+1*5) > height:
        button_text_size -= 1
        font_button = pygame.font.SysFont('Segoe UI Semibold',button_text_size)
        text_width, text_height = font_button.size(longeststring)
    while text_width + 10 > width:
        button_text_size -= 1
        font_button = pygame.font.SysFont('Segoe UI Semibold',button_text_size)
        text_width, text_height = font_button.size(longeststring)
    screen.blit(image,(posx,posy))
    if line1 is not None:
        line1render = font_button.render(line1, True, font_colour)
        text_width1, text_height1 = font_button.size(line1)
        screen.blit(line1render,(posx+5,posy+5))
    if line2 is not None:
        line2render = font_button.render(line2, True, font_colour)
        text_width2, text_height2 = font_button.size(line2)
        screen.blit(line2render,(posx+5,posy+(text_height)+5))
    if line3 is not None:
        line3render = font_button.render(line3, True, font_colour)
        text_width3, text_height3 = font_button.size(line3)
        screen.blit(line3render,(posx+5,posy+(text_height*2)+5))
    if line4 is not None:
        line4render = font_button.render(line4, True, font_colour)
        text_width4, text_height4 = font_button.size(line4)
        screen.blit(line4render,(posx+5,posy + (text_height*3)+5))
    button_box = pygame.Rect(posx,posy,width,height)
    pygame.draw.rect(screen, button_colour, button_box,2)
    pygame.display.update()
    return(button_box)

def generateLastNode(connectionlist):
    returnnodelist = []
    for c in connectionlist:
        returnnodelist.append(c[len(c)-1][1])
    return(returnnodelist)

def generateLastNodeName(nodelist):
    returnnamelist = []
    for c in nodelist:
        returnnamelist.append(searchNodeNamebyPos(c[0],c[1]))
    return(returnnamelist)

def resultList(lastNodeConnectionList,lastNodeNameList,posx,posy,width,height):
    global closestcanteenvar
    global wordsearchvar
    global maximumpricevar
    global selection_value
    global activity_list
    global distances
    if mode == 1:
        for i,v in enumerate(lastNodeNameList):    
            generateResultButtonActiveMouseover(posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,v,"Distance : "+str(int(distances[i])),None,None,(255,255,255))
    elif mode == 2:
        for i,v in enumerate(lastNodeNameList):
            generateResultButtonActiveMouseover(posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,maximumprice_data[i][1].capitalize()+" ($"+format(maximumprice_data[i][0],'.2f')+")",maximumprice_data[i][2],None,None,(255,255,255))
    elif mode == 0:
        for i,v in enumerate(lastNodeNameList):
            generateResultButtonActiveMouseover(posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,wordsearch_data[i][1][0].capitalize(),wordsearch_data[i][1][2],None,None,(255,255,255))
    return lastNodeConnectionList[selection_value]

def updateButtonStates(button):    
    generateResultButtonActiveMouseover(button[0],button[1],button[2],button[3],button[4],button[5],button[6],button[7],button[8],button[9],button[10],button[11],button[12],button[13])

def updateConnectionsbyActivityList():
    global activity_list
    global active_connections
    active_connections = []
    truenumber = 0
    for c in activity_list:
        if c[0][7] == True:
            active_connections.append(c[2])
            break

def generateButtonList(lastNodeConnectionList,lastNodeNameList,posx,posy,width,height):
    global closestcanteenvar
    global maximumpricevar
    global selection_value
    global activity_list
    global distances
    activity_list = []
    if mode == 1:
        for i,v in enumerate(lastNodeNameList):    
            activity_list.append([[posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,v,"Distance : "+str(int(distances[i])),None,None,(255,255,255)],generateResultButtonActiveMouseover(posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,v,"Distance : "+str(int(distances[i])),None,None,(255,255,255)),lastNodeConnectionList[i]])
    elif mode == 2:
        for i,v in enumerate(lastNodeNameList):
            activity_list.append([[posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,maximumprice_data[i][1].capitalize()+" ($"+format(maximumprice_data[i][0],'.2f')+")",maximumprice_data[i][2],None,None,(255,255,255)],generateResultButtonActiveMouseover(posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,maximumprice_data[i][1].capitalize()+" ($"+format(maximumprice_data[i][0],'.2f')+")",maximumprice_data[i][2],None,None,(255,255,255)),lastNodeConnectionList[i]])
    elif mode == 0:
        for i,v in enumerate(lastNodeNameList):
            activity_list.append([[posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,wordsearch_data[i][1][0].capitalize(),wordsearch_data[i][1][2],None,None,(255,255,255)],generateResultButtonActiveMouseover(posx,posy+(i*55),width,height,pygame.Color('lightskyblue3'),pygame.Color('dodgerblue2'),resultbutton_img,False,False,wordsearch_data[i][1][0].capitalize(),wordsearch_data[i][1][2],None,None,(255,255,255)),lastNodeConnectionList[i]])
def redrawButtons():
    global activity_list
    for button in activity_list:
        generateResultButtonActiveMouseover(button[0][0],button[0][1],button[0][2],button[0][3],button[0][4],button[0][5],button[0][6],button[0][7],button[0][8],button[0][9],button[0][10],button[0][11],button[0][12],button[0][13])

def searchNodeNamebyPos(posx,posy):
    global root
    for child in root:
        internalposx = internalposy = False
        for value in child:
            if value.tag == 'posx' and int(value.text) == posx:
                internalposx = True
            if value.tag == 'posy' and int(value.text) == posy:
                internalposy = True
        if internalposx and internalposy:
            return child.attrib['name']

def searchNodebyName(name):
    global root
    posx = 0
    posy = 0
    for child in root:
        if child.attrib['name'] == name:
            for value in child:
                if value.tag == 'posx':
                    posx = int(value.text)
                elif value.tag == 'posy':
                    posy = int(value.text)
    return((posx,posy))

def connectionDistance(node_name):
    global root
    global instance_node_connections
    posx = 0
    posy = 0
    for child in root:
        if child.attrib['name'] == node_name:
            for value in child:
                if value.tag == 'posx':
                    posx = int(value.text)
                elif value.tag == 'posy':
                    posy = int(value.text)
    returnval = graphSearch((mouse_pos[0]-250,mouse_pos[1]),(posx,posy),instance_node_connections,1,10,1,5)[0]
    return returnval

def connectionDistancebyConnection(connection):
    global root
    global instance_node_connections
    totaldistance = 0
    for pair in connection:
        totaldistance += math.sqrt(((abs(pair[0][0]-pair[1][0]))**2)+((abs(pair[1][0]-pair[1][1]))**2))
    return totaldistance

def foodByMaxPrice(max_price,return_number):
    global root2
    returnlist = []
    for child in root2:
        for value in child:
            if len(returnlist) >= return_number:
                return returnlist
            value_name = ''
            value_price = 0
            for attrib in value:
                if attrib.tag == 'name':
                    value_name = str(attrib.text)
                elif attrib.tag == 'price':
                    value_price = float(attrib.text)
            if value_price <= max_price:
                returnlist.append((value_price,value_name,child.attrib['name']))
    returnlist.sort()
    returnlist = returnlist[::-1]
    return returnlist

def keywordGeneration(input_string):
    keywordlist = []
    current_keyword = ''
    for c in input_string:
        if c == ' ':
            keywordlist.append(current_keyword)
            current_keyword = ''
        else:
            current_keyword += c
    keywordlist.append(current_keyword)
    return keywordlist

def keywordScore(keyword1,keyword2):
    list1 = []
    list2 = []
    score = 0
    for c in keyword1:
        list1.append(c)
    for c in keyword2:
        list2.append(c)
    list, length = (list1, len(list1)) if len(list1) > len(list2) else (list2, len(list2))
    other_list = list1 if list2 == list else list2
    length_other = len(other_list)
    for c,v in enumerate(list):
        try:
            other_list[c]
            for v in range(c,length_other-1):
                if list[c] == other_list[v]:
                    score += 1/(v-c+1)
                    break
                else:
                    pass
        except:
            pass
    return(score)

def generateKeyWordList():
    global root2
    namelist = []
    invalid_characters = "!@#$%^&*()_+}{:1234567890\/.;'[]\-="
    for child in root2:
        for value in child:
            var = [0,0,child.attrib['name']]
            for attrib in value:
                if attrib.tag == 'name':
                    var[0] = attrib.text
                elif attrib.tag == 'price':
                    var[1] = attrib.text
            namelist.append(var)
    for iter in namelist:
        iter.append(keywordGeneration(iter[0]))
    for iter in namelist:
        for index,keyword in enumerate(iter[3]):
            if keyword in invalid_characters:
                iter[3].pop(index)
    return(namelist)

def keywordScoreSort(keyword_list,mainlist,number):
    finallist = []
    resultlist = []
    for iteration, keywordlist in enumerate(mainlist):
        list,other_list,length,other_length = (keyword_list,keywordlist[3],len(keyword_list),len(keywordlist[3])) if len(keyword_list) > len(keywordlist[3]) else (keywordlist[3],keyword_list,len(keywordlist[3]),len(keyword_list))
        score = 0
        for i,v in enumerate(list):
            for iter,value in enumerate(other_list):
                score += keywordScore(list[i],other_list[iter])**((iter+1)/(i+1))
        resultlist.append((score,mainlist[iteration]))
        resultlist.sort()
        resultlist = resultlist[::-1]
    for i in range(number):
        finallist.append(resultlist[i])
    return(finallist)

def errorCheck():
    global mode
    global inputbox_text
    if mode == 2:
        try:
            float(inputbox_text)
        except BaseException:
            return False
        else:
            return True
    if mode == 0:
        return True

def appendGraphSearchResultMaxPrice(foodbyMaxPrice):
    global instance_node_connections
    global mouse_pos
    returnlist = []
    for c in foodbyMaxPrice:
        returnlist.append(graphSearch((mouse_pos[0]-250,mouse_pos[1]),searchNodebyName(c[2]),instance_node_connections,3,7,1,5)[1])
    return returnlist

def appendGraphSearchResultWordSearch(foodbyWord):
    global instance_node_connections
    global mouse_pos
    returnlist = []
    for c in foodbyWord:
        returnlist.append(graphSearch((mouse_pos[0]-250,mouse_pos[1]),searchNodebyName(c[1][2]),instance_node_connections,3,7,1,5)[1])
    return returnlist

def userPrompt(message):
    redraw()
    font_size = 25
    userPrompt_font = pygame.font.SysFont('Segoe UI Semibold',  font_size)
    text_width,text_height = userPrompt_font.size(message)
    while text_width > 225:
        font_size -= 1
        font_textbox = pygame.font.SysFont('Segoe UI Semibold', font_size)
        text_width,text_height = userPrompt_font.size(message)
    userPrompt_txt_surface =  userPrompt_font.render(message, True, (255,255,255))
    screen.blit(userPrompt_txt_surface, (5,583-text_height))
    pygame.display.update()

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
    global modebutton_active_mouseover
    global modebutton_box
    global mode
    global closestcanteenvar
    global maximumpricevar
    global wordsearchvar
    global maximumprice_data
    global wordsearch_data
    global debug_mode
    global active_connections
    global mouse_pos
    global activity_list
    global distances
    global selection_value
    global map_view
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if map_view.collidepoint(event.pos):
                    button("map view",black,940,530,100,40,color_inactive,color_active,move_map)
                else:
                    button("map view",black,940,530,100,40,color_inactive,color_active,move_map)
                if modebutton_box.collidepoint(event.pos):
                    modebutton_active_mouseover = True
                    modebutton()
                    pygame.display.update()
                else:
                    modebutton_active_mouseover = False
                    modebutton()
                    pygame.display.update()
                if input_box.collidepoint(event.pos): #test if mouse is in textbox
                    textbox_active_mouseover = True
                    textbox()
                    pygame.display.update()
                else:
                    textbox_active_mouseover = False
                    textbox()
                    pygame.display.update()
                for c in activity_list:
                    if c[1].collidepoint(event.pos):
                        c[0][8] = True
                        updateButtonStates(c[0])
                    else:
                        c[0][8] = False
                        updateButtonStates(c[0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if not((pygame.Rect(940,530,100,40)).collidepoint(event.pos) and event.button == 1):
                if map_view.collidepoint(event.pos):
                    button("map view",black,940,530,100,40,color_inactive,color_active,move_map)
                    break
                if  click_box.collidepoint(event.pos) and event.button == 1:#test if mouse is on map
                    if mode == 2 and inputbox_text == '':
                        continue
                    mouse_pos = event.pos
                    instance_node_connections = GenerateConnections()
                    instance_nodes = GenerateNodes()
                    instance_node_connections.append(((event.pos[0]-250,event.pos[1]),findNearestNode((event.pos[0]-250,event.pos[1]),instance_nodes)[1]))
                    instance_nodes.append(('MousePos',(event.pos[0]-250,event.pos[1])))
                    draw_NTU()
                    MouseClickSavePosition()
                    pygame.display.update()
                    if mode == 1 and mouse_pos is not None:
                        ##button("map view",black,940,530,100,40,color_inactive,color_active,move_map)  ###
                        distances,closestcanteenvar = closestCanteenConnection((mouse_pos[0]-250,mouse_pos[1]),8,instance_node_connections)
                        active_connections = [resultList(closestcanteenvar,generateLastNodeName(generateLastNode(closestcanteenvar)),5,105,235,50)]
                        drawMultipleConnections(active_connections,(0,255,0))
                        generateButtonList(closestcanteenvar,generateLastNodeName(generateLastNode(closestcanteenvar)),5,105,235,50)
                        draw_NTU
                        MouseClickDisplayDotPos()
                    elif mode == 0 and mouse_pos is not None:
                        ##button("map view",black,940,530,100,40,color_inactive,color_active,move_map)  ###
                        wordsearch_data = keywordScoreSort(keywordGeneration(inputbox_text),generateKeyWordList(),8)
                        wordsearchvar = appendGraphSearchResultWordSearch(wordsearch_data)
                        if mouse_pos is not None or input_box == '':
                            active_connections = []
                        else:
                            active_connections = [resultList(wordsearchvar,generateLastNodeName(generateLastNode(wordsearchvar)),5,105,235,50)]
                        drawMultipleConnections(active_connections,(0,255,0))
                        generateButtonList(wordsearchvar,generateLastNodeName(generateLastNode(wordsearchvar)),5,105,235,50)
                        redraw()
                        MouseClickDisplayDotPos()
                    elif mode == 2 and mouse_pos is not None and errorCheck():
                        maximumprice_data = foodByMaxPrice(float(inputbox_text),8)
                        maximumpricevar = appendGraphSearchResultMaxPrice(maximumprice_data)
                        if mouse_pos is not None or input_box == '':
                            active_connections = []
                        else:
                            active_connections = [resultList(maximumpricevar,generateLastNodeName(generateLastNode(maximumpricevar)),5,105,235,50)]
                        drawMultipleConnections(active_connections,(0,255,0))
                        generateButtonList(maximumpricevar,generateLastNodeName(generateLastNode(maximumpricevar)),5,105,235,50)
                        redraw()
                        MouseClickDisplayDotPos()
                    else:
                        redraw()
                    pygame.display.update()
                if input_box.collidepoint(event.pos): #test if mouse is in textbox
                    active = True
                    textbox()
                    pygame.display.update()
                else:
                    active = False
                    textbox()
                    pygame.display.update()
                if modebutton_box.collidepoint(event.pos):
                    mode = (mode + 1)%3
                    modebutton_active_mouseover = True
                    modebutton()
                    if mode == 1 and mouse_pos is not None:
                        distances,closestcanteenvar = closestCanteenConnection((mouse_pos[0]-250,mouse_pos[1]),8,instance_node_connections)
                        active_connections = [resultList(closestcanteenvar,generateLastNodeName(generateLastNode(closestcanteenvar)),5,105,235,50)]
                        drawMultipleConnections(active_connections,(0,255,0))
                        generateButtonList(closestcanteenvar,generateLastNodeName(generateLastNode(closestcanteenvar)),5,105,235,50)
                        redraw()
                        MouseClickDisplayDotPos()
                    elif mode == 0 and mouse_pos is not None:
                        wordsearch_data = keywordScoreSort(keywordGeneration(inputbox_text),generateKeyWordList(),8)
                        wordsearchvar = appendGraphSearchResultWordSearch(wordsearch_data)
                        if mouse_pos is not None or input_box == '':
                            active_connections = []
                        else:
                            active_connections = [resultList(wordsearchvar,generateLastNodeName(generateLastNode(wordsearchvar)),5,105,235,50)]
                        drawMultipleConnections(active_connections,(0,255,0))
                        generateButtonList(wordsearchvar,generateLastNodeName(generateLastNode(wordsearchvar)),5,105,235,50)
                        redraw()
                        MouseClickDisplayDotPos()
                    elif mode == 2 and mouse_pos is not None and errorCheck():
                        maximumprice_data = foodByMaxPrice(float(inputbox_text),8)
                        maximumpricevar = appendGraphSearchResultMaxPrice(maximumprice_data)
                        if mouse_pos is not None or input_box == '':
                            active_connections = []
                        else:
                            active_connections = [resultList(maximumpricevar,generateLastNodeName(generateLastNode(maximumpricevar)),5,105,235,50)]
                        drawMultipleConnections(active_connections,(0,255,0))
                        generateButtonList(maximumpricevar,generateLastNodeName(generateLastNode(maximumpricevar)),5,105,235,50)
                        redraw()
                        MouseClickDisplayDotPos()
                    else:
                        redraw()
                    pygame.display.update()
                else:
                    modebutton_active_mouseover = False
                    modebutton()
                    pygame.display.update()
                for c in activity_list:
                    if c[1].collidepoint(event.pos):
                        draw_NTU()
                        c[0][7] = True
                        updateButtonStates(c[0])
                        updateConnectionsbyActivityList()
                        redrawButtons()
                        drawMultipleConnections(active_connections,(0,255,0))
                        MouseClickDisplayDotPos()
                        pygame.display.update()
                    else:
                        c[0][7] = False
                        pygame.display.update()
            if event.type == pygame.KEYDOWN and active:#update text box
                if event.key == pygame.K_RETURN: #press Enter'
                    if mouse_pos is not None and inputbox_text != '':
                        if mode == 2 and errorCheck(): #search by maximum price
                            maximumprice_data = foodByMaxPrice(float(inputbox_text),8)
                            maximumpricevar = appendGraphSearchResultMaxPrice(maximumprice_data)
                            active_connections = [resultList(maximumpricevar,generateLastNodeName(generateLastNode(maximumpricevar)),5,105,235,50)]
                            drawMultipleConnections(active_connections,(0,255,0))
                            generateButtonList(maximumpricevar,generateLastNodeName(generateLastNode(maximumpricevar)),5,105,235,50)
                        elif mode == 0: #search by rank:                        
                            wordsearch_data = keywordScoreSort(keywordGeneration(inputbox_text),generateKeyWordList(),8)
                            wordsearchvar = appendGraphSearchResultWordSearch(wordsearch_data)
                            active_connections = [resultList(wordsearchvar,generateLastNodeName(generateLastNode(wordsearchvar)),5,105,235,50)]
                            drawMultipleConnections(active_connections,(0,255,0))
                            generateButtonList(wordsearchvar,generateLastNodeName(generateLastNode(wordsearchvar)),5,105,235,50)
                        inputbox_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    inputbox_text = inputbox_text[:-1]
                else:
                    inputbox_text += event.unicode #add the character that has already translated from keypress           
                textbox()
                pygame.display.update()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
                debug_mode = not debug_mode
                redraw()
                pygame.display.update()
    clock.tick(30)

#initialize all variables and objects
pygame.init()#initialize pygame
pygame.font.init()#-initialize font library for pygame
resultbutton_img = pygame.image.load("assets/resultbutton_bg.png")
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
graph = ET.parse('node_data.xml')
foodlist = ET.parse('foodlist_data.xml')
root2 = foodlist.getroot()
root = graph.getroot()
"""debug goes here"""

"""debug ends here"""
gui_length = 250
ntumap_length = 800
ntumap_width = 589
node_connections = GenerateConnections()
nodes = GenerateNodes()
instance_node_connections = []
instance_nodes = []
current_connections = []
closestcanteenvar = []
maximumpricevar = []
wordsearchvar = []
active_connections = []
maximumprice_data = []
wordsearch_data = []
input_box = pygame.Rect(5, 5, 200, 40)
click_box = pygame.Rect(250,0,800,589)
modebutton_box = pygame.Rect(5,50,235,50)
search_input_box = pygame.Rect(205,5,45,40)
width = ntumap_length + gui_length
height = ntumap_width
inputbox_text = ""
map_view = pygame.Rect(940,530,100,40)
dot_pos = (2000,2000)
dot_pos_display_value = (2000,2000)
pygame.key.set_repeat(200,75)
screen = pygame.display.set_mode((width,height)) #initialize screen area with width*height pixels
pygame.display.set_caption('CZ1003 Mini-Project')
active = False
textbox_active_mouseover = False
modebutton_active_mouseover = False
debug_mode = False
resultbutton_active = False
resultbutton_active_mouseover = False
selection_value = 0
activity_list = []
mouse_pos = None
mode = 1
splashscreen(2)
intro()
main_loop()

