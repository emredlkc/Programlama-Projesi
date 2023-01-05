import pygame 
import sys
import pygame_gui
from pygame.locals import * 
from subprocess import call
import pygame as pg 
pygame.init()

en , boy = 1000 ,  700 
ekran =pygame.display.set_mode((en, boy ))
pygame.display.set_caption('text inputlama')
font =pygame.font.Font("font.ttf" , 20)

voltaj1= pygame_gui.UIManager((en , boy ))
direnc1 = pygame_gui.UIManager((en , boy ))
MANAGER = pygame_gui.UIManager((en , boy ))
mainClock= pygame.time.Clock()
UI_REFRESH_RATE= mainClock.tick(60)/1000
TEXT_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((275,100 ), (500,50)), manager=MANAGER, 
                                                        object_id='#main_text_entry'  )
direnc_input= pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60),(200,50)), manager=direnc1, object_id='#giris')
voltaj_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60), (200,50)),manager=voltaj1, object_id='#voltaj')





class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



def show_user_name(user_name):


        
    run = True 
    ekran_renk = 50,0,50

    
    while run:

        ekran.fill((ekran_renk))

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



    a , b = pygame.mouse.get_pos()

    UI_REFRESH_RATE= mainClock.tick(60)/1000
    calis = True
    while calis:

        

        ekran.fill((52,70,100))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.2.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(30,120))
        ekran.blit(pil_img, (640,220))
        ekran.blit(direnc_img, (600,595))
        ekran.blit(voltmetre_img, (600, 250))
        ekran.blit(ampermetre_img, (340, 590))
        ekran.blit(ampuldevre_img, (430, 210))
        siyah = 0,0,0

        # yazi_yaz("Voltaj =",font,siyah, ekran, 100,55,)# ikinci slota yazılanlar ekranda gözükecektir
        # yazi_yaz("Amper =",font,siyah ,ekran , 100,105,)
        yazi_yaz("Direnç giriniz: ",font,siyah ,ekran ,100,75,)






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                calis = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#giris'):
                direnc(event.text)
            direnc1.process_events(event)
        direnc1.update(UI_REFRESH_RATE)



        direnc1.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)





def direnc(direnc_1):

    a , b = pygame.mouse.get_pos()
    go = True
    while go:

        

        ekran.fill((52,70,100))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.2.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(30,120))
        ekran.blit(pil_img, (640,220))
        ekran.blit(direnc_img, (600,595))
        ekran.blit(voltmetre_img, (600, 250))
        ekran.blit(ampermetre_img, (340, 590))
        ekran.blit(ampuldevre_img, (430, 210))
        siyah = 0,0,0

        global direnc

        yazi_yaz("Voltaj giriniz: ",font,siyah ,ekran ,100,75,)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                go= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    game()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#voltaj'):
                voltaj(event.text)
            voltaj1.process_events(event)
        voltaj1.update(UI_REFRESH_RATE)
        pygame.display.update





        new_text = pygame.font.Font("font.ttf", 20).render(f"Direnç={direnc_1}", True, "white")
        new_text_rect = new_text.get_rect(center=(120, 300))
        ekran.blit(new_text,new_text_rect)
        pygame.display.update()
        
        voltaj1.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)


def voltaj(voltaj_1):
    running = True

    a , b = pygame.mouse.get_pos()
    while running:
        ekran.fill((52,70,100))
        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.2.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(30,120))
        ekran.blit(pil_img, (640,220))
        ekran.blit(direnc_img, (600,595))
        ekran.blit(voltmetre_img, (600, 250))
        ekran.blit(ampermetre_img, (340, 590))
        ekran.blit(ampuldevre_img, (430, 210))
        siyah = 0,0,0

        yazi_yaz(f"Direnç=" ,font, (255,255,255) ,ekran ,20,300)
        new_text = pygame.font.Font("font.ttf", 20).render(f"Voltaj={voltaj_1}", True, "white")
        new_text_rect = new_text.get_rect(center=(120, 350))
        ekran.blit(new_text,new_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    direnc()




        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)
main_menu()
