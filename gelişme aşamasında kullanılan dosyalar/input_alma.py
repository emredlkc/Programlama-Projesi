import pygame 
import sys
import pygame_gui
from pygame.locals import * 

pygame.init()

en , boy = 1000 ,  700 
ekran =pygame.display.set_mode((en, boy ))
pygame.display.set_caption('text inputlama')
font =pygame.font.Font("font.ttf" , 20)

MANAGER = pygame_gui.UIManager((en , boy ))
mainClock= pygame.time.Clock()
TEXT_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((275,100 ), (500,50)), manager=MANAGER, object_id='#main_text_entry'  )

def show_user_name(user_name):

    run = True 
    ekran_renk = 50,0,50

    while run:

        ekran.fill((ekran_renk))

        # yazi_yaz('menü ', font , (255,25,25),ekran, 20 , 20)

        a , b  = pygame.mouse.get_pos()
                

        surf1 =font.render('ÇIK', True , 'white')
        surf2 = font.render('BAŞLA',True , 'white')
        button_1 = pygame.Rect(400,350,200,100)
        button_2 = pygame.Rect(400,500,200,100)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    run = False 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_2.collidepoint(event.pos):
                  pygame.quit()
                  run = False       

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):

                    game()    

        if button_1.x <= a <= button_1.x +200 and button_1.y <= b <= button_1.y +100:
            pygame.draw.rect(ekran,(255,0,0),button_1)
        else:
            pygame.draw.rect(ekran,(200,110,110),button_1)
        ekran.blit(surf2, (button_1.x +50, button_1.y +35))

        if button_2.x <= a <=button_2.x +200  and button_2.y <= b <= button_2.y + 100:
            pygame.draw.rect(ekran ,(255,0,0),button_2)
        else: 
            pygame.draw.rect(ekran ,(200,110,110),button_2 )
        ekran.blit(surf1, (button_2.x +75 , button_2.y+40))

        new_text = pygame.font.Font("font.ttf", 50).render(f"Merhaba, {user_name}", True, "white")
        new_text_rect = new_text.get_rect(center=(500, 250))

        ekran.blit(new_text,new_text_rect)
        pygame.display.update()

        

        mainClock.tick(60)



def yazi_yaz(yazi , font , renk , surface ,x , y ):
    textobj= font.render(yazi, 1 ,renk  )
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)



def main_menu():
    run = True 
    ekran_renk = 50,0,50

    while run:

        ekran.fill((ekran_renk))

        yazi_yaz('Adınızı giriniz: ', font , (255,25,25),ekran, 275 , 75)

        a , b  = pygame.mouse.get_pos()
                

        surf1 =font.render('ÇIK', True , 'white')
        surf2 = font.render('BAŞLA',True , 'white')
        button_1 = pygame.Rect(400,350,200,100)
        button_2 = pygame.Rect(400,500,200,100)
        UI_REFRESH_RATE= mainClock.tick(60)/1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    run = False 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_2.collidepoint(event.pos):
                  pygame.quit()
                  run = False       

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):

                    game()    
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry'):
                show_user_name(event.text)
            MANAGER.process_events(event)



        if button_1.x <= a <= button_1.x +200 and button_1.y <= b <= button_1.y +100:
            pygame.draw.rect(ekran,(255,0,0),button_1)
        else:
            pygame.draw.rect(ekran,(200,110,110),button_1)
        ekran.blit(surf2, (button_1.x +50, button_1.y +35))

        if button_2.x <= a <=button_2.x +200  and button_2.y <= b <= button_2.y + 100:
            pygame.draw.rect(ekran ,(255,0,0),button_2)
        else: 
            pygame.draw.rect(ekran ,(200,110,110),button_2 )
        ekran.blit(surf1, (button_2.x +75 , button_2.y+40))


        MANAGER.draw_ui(ekran)
        print(a,b)
        pygame.display.update()
        mainClock.tick(60)
        MANAGER.update(UI_REFRESH_RATE)


def game():
    calis = True
    while calis:

        ekran.fill((0,0,0))

        yazi_yaz('game', font ,(255,255,255),ekran , 20,20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        main_menu()

        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)

main_menu()