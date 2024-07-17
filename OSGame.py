import pygame

pygame.init()
SCREEN_WIDTH= 900
SCREEN_HEIGHT= 800

BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.font.init()
font = pygame.font.Font(None, 20)
buttonfont = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Fragmentation and Paging")

#-------------------------SETUP Stationary Rectangles-----------------------------------------------
RAM1 = pygame.Rect((20,20,100,400)) #each block is 50 height total 8 block
SSD = pygame.Rect((115,500,650,210)) #Container golding all the processes
texttitle = pygame.Rect((260,20,650,20)) #Container holding textbox title
textbox = pygame.Rect((260,30,650,450)) #Textbox for info
#nextbutton = pygame.Rect((265,40,600,300)) #Textbox for info

#----------------------------Static block Labels--------------------------------------------
RAMLabel = font.render("Main Memory", True, BLACK)
SSDLabel = font.render("Secondary Memory", True, BLACK)
txttitleLabel = font.render("READ ME !!! ", True, BLACK)

#---------------------------Static block labels_rect------------------------------------------
RAMLabel_rect = RAMLabel.get_rect(center=RAM1.center)
SSDLabel_rect = SSDLabel.get_rect(center=SSD.midtop)
SSDLabel_rect.y += 10
txttitleLabel_rect = txttitleLabel.get_rect(center=texttitle.midtop)
txttitleLabel_rect.y += 10
visiblestatus = True



#-------------------------Setup Process Blocks FOR No-Page-----------------------------------------------------
#Process blocks--> Edit heigt based on how many'pages' it has
P1 = pygame.Rect((155,510,100,200)) # Process 1 is height-->4pages (uses 2 seconds to finish)
P2 = pygame.Rect((265,610,100,100)) # Process 2 is height-->2pages (uses 3 seconds to finish)
P3 = pygame.Rect((375,560,100,150)) # Process 3 is height 3 (uses x seconds to finish)
P4 = pygame.Rect((485,560,100,150)) # Process 4 is height 3 (time taken is redundant)
P5 = pygame.Rect((595,510,100,200)) # Process 5 is height 5 (time taken is redundant)
dummy = pygame.Rect((0,0,1,1)) # Process 4 is height 3 (time taken is redundant)
processes=[P1,dummy,dummy,dummy,dummy,dummy,dummy]

#---------------------------No Paging Labels -----------------------------------------
P1Label = font.render("Process 1", True, BLACK)
P2Label = font.render("Process 2", True, BLACK)
P3Label = font.render("Process 3", True, BLACK)
P4Label = font.render("Process 4", True, BLACK)
P5Label = font.render("Process 5", True, BLACK)

#---------------------------No Paging Labels_rect -----------------------------------------
P1label_rect = P1Label.get_rect(center=P1.center)
P2label_rect = P2Label.get_rect(center=P2.center)
P3label_rect = P3Label.get_rect(center=P3.center)
P4label_rect = P4Label.get_rect(center=P4.center)
P5label_rect = P5Label.get_rect(center=P5.center)


#-------------------------Setup Process Blocks FOR Paging-----------------------------------------------------
RAM2 = pygame.Rect((130,20,100,400))

P1_1 = pygame.Rect((155,510,100,50))
P1_2 = pygame.Rect((155,560,100,50))
P1_3 = pygame.Rect((155,610,100,50))
P1_4 = pygame.Rect((155,660,100,50))

P2_1 = pygame.Rect((130,220,100,50))
P2_2 = pygame.Rect((130,270,100,50))

P3_1 = pygame.Rect((130,20,100,50))
P3_2 = pygame.Rect((130,70,100,50))
P3_3 = pygame.Rect((130,120,100,50))

P4_1 = pygame.Rect((485,560,100,50))
P4_2 = pygame.Rect((485,610,100,50))
P4_3 = pygame.Rect((485,660,100,50))

P5_1 = pygame.Rect((595,510,100,50))
P5_2 = pygame.Rect((595,560,100,50))
P5_3 = pygame.Rect((595,610,100,50))
P5_4 = pygame.Rect((595,660,100,50))
#P5_5 = pygame.Rect((595,710,100,50))

#--------------------------- Paging Labels_rect -----------------------------------------
P1_1Label = font.render("Process 1", True, BLACK)
P1_2Label = font.render("Process 1", True, BLACK)
P1_3Label = font.render("Process 1", True, BLACK)
P1_4Label = font.render("Process 1", True, BLACK)

P2_1Label = font.render("Process 2", True, BLACK)
P2_2Label = font.render("Process 2", True, BLACK)

P3_1Label = font.render("Process 3", True, BLACK)
P3_2Label = font.render("Process 3", True, BLACK)
P3_3Label = font.render("Process 3", True, BLACK)

P4_1Label = font.render("Process 4", True, BLACK)
P4_2Label = font.render("Process 4", True, BLACK)
P4_3Label = font.render("Process 4", True, BLACK)

P5_1Label = font.render("Process 5", True, BLACK)
P5_2Label = font.render("Process 5", True, BLACK)
P5_3Label = font.render("Process 5", True, BLACK)
P5_4Label = font.render("Process 5", True, BLACK)
#P5_5Label = font.render("Process 5 (3s)", True, BLACK)

#--------------------------Paging Labels_rect -----------------------------------------
P1_1_label_rect = P1_1Label.get_rect(center=P1_1.center)
P1_2_label_rect = P1_2Label.get_rect(center=P1_2.center)
P1_3_label_rect = P1_3Label.get_rect(center=P1_3.center)
P1_4_label_rect = P1_4Label.get_rect(center=P1_4.center)

P2_1_label_rect = P2_1Label.get_rect(center=P2_1.center)
P2_2_label_rect = P2_2Label.get_rect(center=P2_2.center)

P3_1_label_rect = P3_1Label.get_rect(center=P3_1.center)
P3_2_label_rect = P3_2Label.get_rect(center=P3_2.center)
P3_3_label_rect = P3_3Label.get_rect(center=P3_3.center)

P4_1_label_rect = P4_1Label.get_rect(center=P4_1.center)
P4_2_label_rect = P4_2Label.get_rect(center=P4_2.center)
P4_3_label_rect = P4_3Label.get_rect(center=P4_3.center)

P5_1_label_rect = P5_1Label.get_rect(center=P5_1.center)
P5_2_label_rect = P5_2Label.get_rect(center=P5_2.center)
P5_3_label_rect = P5_3Label.get_rect(center=P5_3.center)
P5_4_label_rect = P5_4Label.get_rect(center=P5_4.center)
#P5_5_label_rect = P5_5Label.get_rect(center=P5_5.center)


#-------------------------------------- set-up text box info-------------------------------------
textcontent = 'Time =0 second .Process 1 is needed for execution. Drag and Drop Process 1'
txt_surface = font.render(textcontent, True, BLACK)

#--------------------------------------------set up button---------------------------------------
button_rect = pygame.Rect(500, 350, 200, 50)
button_text = "Next"
button_surface = font.render(button_text, True, BLACK)
next_button = button_surface.get_rect(center=button_rect.center)
nextbtn_status = False
displayRam2 = False

#---------------------Process Block location settings------------------------------------------------
active_box = None #variable to indicate selected box
starting_coord=[20,20]
originalcoord=[(155,510),(265,610),(375,560),(485,560),(485,560),(485,610),(485,660)]
    
run = True

#----------------------------Code Runs in this Loop----------------------------------------------
while run:
    #inside the game
    screen.fill('black')
    pygame.draw.rect(screen,(255, 255, 255),texttitle)
    pygame.draw.rect(screen, (255,255,255), textbox)
    pygame.draw.rect(screen,(232, 228, 100),RAM1)
    pygame.draw.rect(screen,(255, 255, 255),SSD)
    #pygame.draw.rect(screen,(255, 255, 255),texttitle)
    pygame.draw.rect(screen,(127, 245, 239),P1)
    pygame.draw.rect(screen,(127, 157, 245),P2)
    pygame.draw.rect(screen,(9, 47, 237),P3)
    if visiblestatus:
        pygame.draw.rect(screen,(230, 64, 199),P4)
    pygame.draw.rect(screen,(39, 242, 17),P5)
    #pygame.draw.rect(screen, (255,255,255), textbox)
    
    screen.blit(P1Label,P1label_rect)
    screen.blit(P2Label,P2label_rect)
    screen.blit(P3Label,P3label_rect)
    if visiblestatus:
        screen.blit(P4Label,P4label_rect)
    screen.blit(P5Label,P5label_rect)
    screen.blit(RAMLabel,RAMLabel_rect)
    screen.blit(SSDLabel,SSDLabel_rect)
    screen.blit(txttitleLabel,txttitleLabel_rect)
    screen.blit(txt_surface,(260,40))
    #screen.blit(button_surface, button_rect)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, process in enumerate(processes):
                    if process.collidepoint(event.pos):
                        active_box = num
                        break
                if button_rect.collidepoint(event.pos):
                        textcontent = 'On the Right is how RAM and process look like when Paging Occurs. Drag Process 4 into RAM!'
                        txt_surface = font.render(textcontent, True, BLACK)
                        displayRam2 = True
                        visiblestatus = False
                        nextbtn_status = False
                        processes[3] = dummy
                        processes[4] = P4_1
                        
                        
                        

                        
        if event.type ==pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if active_box is not None:
                    
                    # Placing Process 1 inside the RAM
                    if active_box == 0:
                        if processes[active_box].colliderect(RAM1):
                        #return the block to its original point
                            if (starting_coord[1] + processes[active_box].height) > (RAM1.y + RAM1.height):
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                            else:
                                processes[active_box].x = starting_coord[0]
                                processes[active_box].y = starting_coord[1]
                                starting_coord[1] += processes[active_box].height    
                                #del processes[active_box]
                                processes[active_box] = dummy
                                #del originalcoord[active_box]
                                #after process 1 is in RAM, enable clickability for Process 2
                                processes[1] = P2
                                textcontent = 'Time =1st second. Process 1 completed. Now Process 2 is needed, Drag and Drop process 2'
                                txt_surface = font.render(textcontent, True, BLACK)
                        else:
                            # Reset to original position if not colliding with RAM
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]

                    #Placing Process 2 inside the RAM
                    elif active_box ==1:
                        if processes[active_box].colliderect(RAM1):
                        #supposed to return the block to its original point
                            if (starting_coord[1] + processes[active_box].height) > (RAM1.y + RAM1.height):
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                            else:
                                processes[active_box].x = starting_coord[0]
                                processes[active_box].y = starting_coord[1]
                                starting_coord[1] += processes[active_box].height    
                                #del processes[active_box]
                                processes[active_box] = dummy
                                #del originalcoord[active_box]
                                #enable clickability for Proccess 3 after Process 2 is added
                                processes[2] = P3
                                #shift process 1 back to SSD
                                processes[0] = P1
                                processes[0].x = originalcoord[0][0]
                                processes[0].y = originalcoord[0][1]
                                processes[0] = dummy
                                textcontent = 'Time=2nd second. Process 1 is completed.Now process 3 is needed. Drag and drop Process 3'
                                txt_surface = font.render(textcontent, True, BLACK)
                        else:
                            # Reset to original position if not colliding with RAM
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]
                    
                    # Placeing Process 3 inside RAM
                    elif active_box ==2:
                        if processes[active_box].colliderect(RAM1):
                            #return the block to its original point if process cannot fit in RAM
                            if (30 + processes[active_box].height) > (RAM1.y + RAM1.height):
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                            else:
                                processes[active_box].x = starting_coord[0]
                                processes[active_box].y = starting_coord[1]
                                starting_coord[1] += processes[active_box].height    
                                #del processes[active_box]
                                #del originalcoord[active_box]
                                processes[active_box].x = 20
                                processes[active_box].y = 20
                                processes[3] = P4
                                processes[2] = dummy 
                                textcontent = 'Time = 3rd second. Empty spaces are fragmented spaces. Now add Process 4'
                                txt_surface = font.render(textcontent, True, BLACK)
                        else:
                            # Reset to original position if not colliding with RAM
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]
                    
                    #Placing Process 4 inside RAM
                    elif active_box ==3:
                        if processes[active_box].colliderect(RAM1):
                        #supposed to return the block to its original point
                            if (starting_coord[1] + processes[active_box].height) > (RAM1.y + RAM1.height):
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                                textcontent = 'Process 4 is too big to fit into fragmented space. Hit next to see Paging'
                                txt_surface = font.render(textcontent, True, BLACK)
                                nextbtn_status = True
                                
                            else:
                                processes[active_box].x = starting_coord[0]
                                processes[active_box].y = starting_coord[1]
                                starting_coord[1] += processes[active_box].height   
                                #del processes[active_box]
                                #del originalcoord[active_box]

                        else:
                            # Reset to original position if not colliding with RAM
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]
                    
                    elif active_box == 4:
                        if processes[active_box].colliderect(RAM2):
                            if not displayRam2:
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                            else:
                                processes[active_box].x = 130
                                processes[active_box].y = 170
                                textcontent = 'Drag next page of Process 4'
                                txt_surface = font.render(textcontent, True, BLACK)
                                processes[4] = dummy
                                processes[5] = P4_2         
                        else:
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]
                    
                    elif active_box == 5:
                        if processes[active_box].colliderect(RAM2):
                            if not displayRam2:
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                            else:
                                processes[active_box].x = 130
                                processes[active_box].y = 320
                                textcontent = 'Drag last page of Process 4'
                                txt_surface = font.render(textcontent, True, BLACK)
                                processes[5] = dummy
                                processes[6] = P4_3
                        else:
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]
                    
                    elif active_box == 6:
                        if processes[active_box].colliderect(RAM2):
                            if not displayRam2:
                                processes[active_box].x = originalcoord[active_box][0]
                                processes[active_box].y = originalcoord[active_box][1]
                            else:
                                processes[active_box].x = 130
                                processes[active_box].y = 370
                                textcontent = 'As seen, Paging Splits processes to smaller chunk to fit in the RAM, Maximising Memory'
                                txt_surface = font.render(textcontent, True, BLACK)
                                processes[6] = dummy
                        else:
                            processes[active_box].x = originalcoord[active_box][0]
                            processes[active_box].y = originalcoord[active_box][1]

                            
                            
                    
                
                active_box = None #release box from selection

        if event.type == pygame.MOUSEMOTION:
            if active_box !=None:
                processes[active_box].move_ip(event.rel)
                
        
        if event.type == pygame.QUIT:
            run=False
    
    # Update labels' positions
    P1label_rect = P1Label.get_rect(center=P1.center)
    P2label_rect = P2Label.get_rect(center=P2.center)
    P3label_rect = P3Label.get_rect(center=P3.center)
    P4label_rect = P4Label.get_rect(center=P4.center)
    if nextbtn_status:
        screen.blit(button_surface, button_rect)
    
    if displayRam2:
        pygame.draw.rect(screen,(232, 228, 100),RAM2)
        pygame.draw.rect(screen,(127, 245, 239),P1_1)
        pygame.draw.rect(screen,(127, 245, 239),P1_2)
        pygame.draw.rect(screen,(127, 245, 239),P1_3)
        pygame.draw.rect(screen,(127, 245, 239),P1_4)
        pygame.draw.rect(screen,(127, 157, 245),P2_1)
        pygame.draw.rect(screen,(127, 157, 245),P2_2)
        pygame.draw.rect(screen,(9, 47, 237),P3_1)
        pygame.draw.rect(screen,(9, 47, 237),P3_2)
        pygame.draw.rect(screen,(9, 47, 237),P3_3)
        pygame.draw.rect(screen,(230, 64, 199),P4_1)
        pygame.draw.rect(screen,(230, 64, 199),P4_2)
        pygame.draw.rect(screen,(230, 64, 199),P4_3)
        pygame.draw.rect(screen,(39, 242, 17),P5_1)
        pygame.draw.rect(screen,(39, 242, 17),P5_2)
        pygame.draw.rect(screen,(39, 242, 17),P5_3)
        pygame.draw.rect(screen,(39, 242, 17),P5_4)
        
        
        screen.blit(P1_1Label,P1_1_label_rect)
        screen.blit(P1_2Label,P1_2_label_rect)
        screen.blit(P1_3Label,P1_3_label_rect)
        screen.blit(P1_4Label,P1_4_label_rect)
        
        screen.blit(P2_1Label,P2_1_label_rect)
        screen.blit(P2_2Label,P2_2_label_rect)
        
        
        screen.blit(P3_1Label,P3_1_label_rect)
        screen.blit(P3_2Label,P3_2_label_rect)
        screen.blit(P3_3Label,P3_3_label_rect)
        
        screen.blit(P4_1Label,P4_1_label_rect)
        screen.blit(P4_2Label,P4_2_label_rect)
        screen.blit(P4_3Label,P4_3_label_rect)
        
        screen.blit(P5_1Label,P5_1_label_rect)
        screen.blit(P5_2Label,P5_2_label_rect)
        screen.blit(P5_3Label,P5_3_label_rect)
        screen.blit(P5_4Label,P5_4_label_rect)
        
    P4_1_label_rect = P4_1Label.get_rect(center=P4_1.center)
    P4_2_label_rect = P4_2Label.get_rect(center=P4_2.center)
    P4_3_label_rect = P4_3Label.get_rect(center=P4_3.center)
    
    pygame.display.flip()
    pygame.display.update()
    
pygame.quit()