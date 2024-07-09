import pygame

pygame.init()
SCREEN_WIDTH= 900
SCREEN_HEIGHT= 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#before the game
RAM = pygame.Rect((30,20,100,400)) #each block is 50 height total 8 block
PTable = pygame.Rect((265,500,500,210)) #Container golding all the processes

#Process blocks--> Edit heigt based on how many'pages' it has
P1 = pygame.Rect((275,510,100,200)) # Process 1 is height 4 (uses 2 seconds to finish)
P2 = pygame.Rect((385,610,100,100)) # Process 2 is height 2 (uses 3 seconds to finish)
P3 = pygame.Rect((495,560,100,150)) # Process 3 is height 3 (uses x seconds to finish)
P4 = pygame.Rect((605,560,100,150)) # Process 4 is height 3 (time taken is redundant)
processes=[]
processes.append(P1)
processes.append(P2)
processes.append(P3)
processes.append(P4)
active_box = None
starting_coord=[30,20]
run = True


while run:
    #inside the game
    screen.fill('black')
    pygame.draw.rect(screen,(232, 228, 100),RAM)
    pygame.draw.rect(screen,(255, 255, 255),PTable)
    pygame.draw.rect(screen,(127, 245, 239),P1)
    pygame.draw.rect(screen,(127, 157, 245),P2)
    pygame.draw.rect(screen,(9, 47, 237),P3)
    pygame.draw.rect(screen,(230, 64, 199),P4)
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, process in enumerate(processes):
                    if process.collidepoint(event.pos):  #maybe this area
                        active_box = num
                        
        if event.type ==pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if active_box is not None:
                    processes[active_box].colliderect(RAM)
                    processes[active_box].x = starting_coord[0]
                    processes[active_box].y = starting_coord[1]
                    starting_coord[1] += processes[active_box].height
                    #del processes[active_box]
                    
                active_box = None #release box from selection

        if event.type == pygame.MOUSEMOTION:
            if active_box !=None:
                processes[active_box].move_ip(event.rel)
                
        
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()