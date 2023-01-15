import pygame ,sys, pygame_gui
from pygame.locals import * 
import pygame as pg 


pygame.init()

# ekran ayalarma
en,boy = 564 ,650
ekran =pygame.display.set_mode((999,666))

# ekran ismi (pencere ismi)
pygame.display.set_caption('Final Projesi')

# icon ayarlama
icon = pg.image.load("görseller/ampulikon.png")
pg.display.set_icon(icon)
running = True


# yazi tipi ayarlama

font =pygame.font.Font("font.ttf" , 20)

#MANAGERS
voltaj1= pygame_gui.UIManager((en , boy ))
direnc1 = pygame_gui.UIManager((en , boy ))
MANAGER = pygame_gui.UIManager((en , boy ))
voltajbul = pygame_gui.UIManager((en,boy))
voltajmanager = pygame_gui.UIManager((en,boy))
direncvoltaji =pygame_gui.UIManager((en,boy))
direncakimi= pygame_gui.UIManager((en,boy))

# CLOCK
mainClock= pygame.time.Clock()
UI_REFRESH_RATE= mainClock.tick(60)/1000


# input yerleri

TEXT_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((190,70 ), (200,50)), manager=MANAGER,  object_id='#main_text_entry'  )

# akımı hesaplarken kullanılanlar:                                            
direnc_input= pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60),(200,50)), manager=direnc1, object_id='#giris')

voltaj_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60), (200,50)),manager=voltaj1, object_id='#voltaj')

#voltaj hesaplarken kullanılanlar:
akim_direce = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60),(200,50)),manager=voltajbul,object_id='#voltajibul')

voltajdaki_akim = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60),(200,50)),manager=voltajmanager,object_id='#yuhbe')
#direnc hesaplanırken kullanılanlar:

direncteki_voltaj = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60),(200,50)),manager= direncvoltaji, object_id='#direnctekivoltaj')

direncteki_akim = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((400,60),(200,50)),manager=direncakimi , object_id='#direnctekiakim')


# arka plan ayarlamak için gerekli yer
class Background(pg.sprite.Sprite):

    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#kullanıcı ismi ekleme kısmı 
def show_user_name(user_name):

    #ekran en boy renk ayarı        
    run = True 
    ekran_renk = 50,0,50
    en , boy = 564 ,  650 
    ekran =pygame.display.set_mode((en, boy ))
    while run:
 
        #arkaplan resminin belirlendiği kod
        a , b  = pygame.mouse.get_pos()
        BackGround = Background('görseller/arkaplanmenu.jpg', [0,0])
        ekran.blit(BackGround.image, BackGround.rect)

        #kullanıcı ismi alınırken kullannılan butonların kordinatlari 
        surf1 =font.render('ÇIK', True , 'white')
        surf2 = font.render('BAŞLA',True , 'white')
        button_1 = pygame.Rect(190,300,200,100)
        button_2 = pygame.Rect(190,450,200,100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
           #klavye tuşlarının görevlerinin atanması
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
                    arayuz() 
                 

        #mouse pozisyonuna bağlı olarak buton renginin değişmesi 
        
        if button_1.x <= a <= button_1.x +200 and button_1.y <= b <= button_1.y +100:
            pygame.draw.rect(ekran,(38, 140, 7),button_1)
        else:
            pygame.draw.rect(ekran,(255,0,0),button_1)
        ekran.blit(surf2, (button_1.x +50, button_1.y +35))

        if button_2.x <= a <=button_2.x +200  and button_2.y <= b <= button_2.y + 100:
            pygame.draw.rect(ekran ,(38, 140, 7),button_2)
        else: 
            pygame.draw.rect(ekran ,(255,0,0),button_2 )
        ekran.blit(surf1, (button_2.x +75 , button_2.y+40))

        new_text = pygame.font.Font("font.ttf", 30).render(f"Merhaba, {user_name}", True, "white")
        new_text_rect = new_text.get_rect(center=(290, 100))


        ekran.blit(new_text,new_text_rect)
        pygame.display.update()

        #ekran yenileme hızı 
        mainClock.tick(60)

# ekrana yazı yazmak için gerekli kod kısmı 
def yazi_yaz(yazi , font , renk , surface ,x , y ):
    textobj= font.render(yazi, 1 ,renk  )
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


#ana menü ayarlarının yapılması 
def main_menu():
    run = True 
    ekran_renk = 50,0,50
    en= 564
    boy = 650
    ekran = pygame.display.set_mode((en,boy))
    

    while run:

        #menü arkaplanının ayarlanması 
        BackGround = Background('görseller/arkaplanmenu.jpg', [0,0])
        ekran.blit(BackGround.image, BackGround.rect)
        
        
        # kullanıcı isminin yazıldığı bosluğu tanımlama 
        yazi_yaz('Adınızı giriniz: ', font , (255,25,25),ekran, 140 , 45)

        
       #mouse pozisyonu alma 
        a , b  = pygame.mouse.get_pos()
                
        #menü butolarının kordinatlaının belirlenmesi 
        surf1 =font.render('ÇIK', True , 'white')
        surf2 = font.render('BAŞLA',True , 'white')
        button_1 = pygame.Rect(190,300,200,100)
        button_2 = pygame.Rect(190,450,200,100)
        UI_REFRESH_RATE= mainClock.tick(60)/1000



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        #klavye tuşlarının görevlerinin atanması 
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
                   arayuz() 
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry'):
                show_user_name(event.text)
            MANAGER.process_events(event)



        #mouse pozisyonuna bağlı olarak buton renginin değişmesi 

        if button_1.x <= a <= button_1.x +200 and button_1.y <= b <= button_1.y +100:
            pygame.draw.rect(ekran,(38, 140, 7),button_1)
        else:
            pygame.draw.rect(ekran,(255,0,0),button_1)
        ekran.blit(surf2, (button_1.x +50, button_1.y +35))

        if button_2.x <= a <=button_2.x +200  and button_2.y <= b <= button_2.y + 100:
            pygame.draw.rect(ekran ,(38, 140, 7),button_2)
        else: 
            pygame.draw.rect(ekran ,(255,0,0),button_2 )
        ekran.blit(surf1, (button_2.x +75 , button_2.y+40))




        MANAGER.draw_ui(ekran)
        print(a,b)
        pygame.display.update()
        mainClock.tick(60)
        MANAGER.update(UI_REFRESH_RATE)
        
#bulunması istenen elemanın seçildiği kod 
def arayuz():
    kos= True
    # en boy ayarı
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    while kos:
        
        # ekran renginin ayarlanması
        ekran.fill((44, 143, 163))
        #yazı tipi tanımlama 
        font_esc =pygame.font.Font("font.ttf" , 10)
     
        #talimatları ekrana yazma
        yazi_yaz("GERİ GİTMEK İÇİN: ESC BASINIZ", font_esc,(255,0,0),ekran,20,20)
        yazi_yaz("BULMAK İSTEDİĞİNİZ ELEMANI SEÇİNİZ:",font , (255,255,255),ekran,140,300)

        (mx , my) = pygame.mouse.get_pos()
        #ekrandaki butonarın e işe yaradığı
        surf_voltaj =font.render('VOLT', True , 'white')
        surf_akim =font.render('AKIM', True , 'white')
        surf_direnc = font.render('DİRENÇ',True,'white')

         # ekrandaki butonların kordinatlarının ayralanması 
        button_voltaj= pygame.Rect(150,350,150,100)
        button_akim=pygame.Rect(400,350,150,100)
        button_direnc=pygame.Rect(650,350,150,100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                kos = False
                
        #klavye tuşlarının görevlerinin atanması 
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            
            
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if button_akim.collidepoint(event.pos):
                    game()

                if button_voltaj.collidepoint(event.pos):
                    akimdan_diren()

                if button_direnc.collidepoint(event.pos):
                        direncin_1_loop()

                    
                    
        #mouse pozisyonuna bağlı olarak buton renginin değişmesi       
        if button_akim.x <= mx  <= button_akim.x + 150   and button_akim.y <= my <= button_akim.y + 100:
            pygame.draw.rect(ekran,(38, 140, 7),button_akim)
        else:
            pygame.draw.rect(ekran ,(255,0,0),button_akim)
        ekran.blit(surf_akim, (button_akim.x + 40, button_akim.y + 35))

        if button_voltaj.x <= mx <= button_voltaj.x +  150 and button_voltaj.y <= my <= button_voltaj.y + 100:
            pygame.draw.rect(ekran,(38, 140, 7),button_voltaj)
        else:
            pygame.draw.rect(ekran,(255,0,0),button_voltaj)
        ekran.blit(surf_voltaj,(button_voltaj.x + 20 , button_voltaj.y + 35))

        if button_direnc.x <= mx <= button_direnc.x + 150 and button_direnc.y <= my <= button_direnc.y + 100:
            pygame.draw.rect(ekran,(38, 140, 7),button_direnc)
        else:
            pygame.draw.rect(ekran,(255,0,0),button_direnc)
        ekran.blit(surf_direnc,(button_direnc.x + 20,button_direnc.y + 35))

        pygame.display.update()
        pygame.display.flip()


# game arayüzünü kullanırsak  direnc ve voltajı girip  akımı elde ederiz
# akımın 1. loopu
def game():
    #en boy ayarları 
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))


    a , b = pygame.mouse.get_pos()

    calis = True
    while calis:

        
        # ekran renginin ayarı 
        ekran.fill((54, 128, 247))
            
        #kullanılan resimlerin sistem tarafından aktive edilmesi 
        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0


        yazi_yaz("Direnç giriniz: ",font,siyah ,ekran ,100,75,)






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                calis = False
        #klavye tuşlarının görevlerinin atanması
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#giris'):
                global direnc__
                direnc__ = (event.text)  
                direnc(event.text)
            direnc1.process_events(event)
        direnc1.update(UI_REFRESH_RATE)



        direnc1.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)

# akımın 2. loopu
def direnc(direnc_1):

    # en boy ayarı 
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    a , b = pygame.mouse.get_pos()
    go = True
    while go:

          # ekran renginin ayralanması 
        ekran.fill((54, 128, 247))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")


        #kullanılan resimleri sistem tarafından aktive edilmesi 
        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0


        # hangi değerin girileceğinin belirtilmesi 
        yazi_yaz("Voltaj giriniz: ",font,siyah ,ekran ,100,75,)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                go= False
        # klavye tuşlarının görevlerinin atanması
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    game()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#voltaj'):
                  global voltaj__
                  voltaj__= (event.text)
                  voltaj(event.text)
            voltaj1.process_events(event)
        pygame.display.update





        new_text = pygame.font.Font("font.ttf", 20).render(f"Direnç={direnc__}Ω", True, "white")
        new_text_rect = new_text.get_rect(center=(120, 300))
        ekran.blit(new_text,new_text_rect)

        
        voltaj1.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)
        voltaj1.update(UI_REFRESH_RATE)

# akımın 3. loopu
def voltaj(voltaj_1):
    running = True
    #ekran  boyutunun ayarlanması
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    a , b = pygame.mouse.get_pos()
    while running:
        #ekran renginin ayarlanması 
        ekran.fill((54, 128, 247))
        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")


         #kullanılan resimleri sistem tarafından aktive edilmesi 
        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0
       # girilen değerlerin ekrana yazılması  
        yazi_yaz(f"Direnç={direnc__}Ω" ,font, (255,255,255) ,ekran ,20,300)
        yazi_yaz(f"Voltaj={voltaj__}V",font ,(255,255,255),ekran,20 , 350)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()
        if voltaj__ == float and direnc__ == float :
            akim_degeri = float(voltaj__)/float(direnc__)

            yazi_yaz(f"★AKIM:{akim_degeri} AMPER★",font ,(77, 237, 52),ekran,5,400) 
        else:
            deger_giriniz()

        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)

#voltajın 1. loopu
def akimdan_diren():
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))


    a , b = pygame.mouse.get_pos()
    go = True
    while go:


        ekran.fill((54, 128, 247))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0



        yazi_yaz("Direnç giriniz: ",font,siyah ,ekran ,100,75,)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                go= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#voltajibul'):
                  global voltaj_hesaplanirken_direnc
                  voltaj_hesaplanirken_direnc= (event.text)
                  voltajsonu(event.text)
            voltajbul.process_events(event)
        pygame.display.update






        
        voltajbul.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)
        voltajbul.update(UI_REFRESH_RATE)

# voltajın 2. loopu
def voltajsonu(voltajsonu):
    calis = True
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    while calis:

        

        ekran.fill((54, 128, 247))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0

        yazi_yaz(f"Direnç={voltaj_hesaplanirken_direnc} Ω" ,font, (255,255,255) ,ekran ,20,300)
        yazi_yaz("Akım giriniz: ",font,siyah ,ekran ,100,75,)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                go= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()
            

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#yuhbe'):
                  global voltaj_hesaplanirken_akim
                  voltaj_hesaplanirken_akim= (event.text)
                  voltaj_hesaplandi(event.text)
            voltajmanager.process_events(event)
        pygame.display.update


        voltajmanager.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)
        voltajmanager.update(UI_REFRESH_RATE)

# voltajın 3. loopu
def voltaj_hesaplandi(voltajhesaplandi):
    running = True
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    a , b = pygame.mouse.get_pos()
    while running:
        ekran.fill((54, 128, 247))
        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0
        
        yazi_yaz(f"Direnç={voltaj_hesaplanirken_direnc} Ω" ,font, (255,255,255) ,ekran ,20,300)
        yazi_yaz(f"Akım={voltaj_hesaplanirken_akim} A",font ,(255,255,255),ekran,20 , 350)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()
        if voltaj_hesaplanirken_akim == float and voltaj_hesaplanirken_direnc == float:
            voltaj_degeri= float(voltaj_hesaplanirken_akim)* float(voltaj_hesaplanirken_direnc)

            yazi_yaz(f"★VOLTAJ:{voltaj_degeri} VOLT★",font ,(77, 237, 52),ekran,5,400) 
        else : 
            deger_giriniz()

        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)

# direncin 1. loopu
def direncin_1_loop():
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    a , b = pygame.mouse.get_pos()

    calis = True
    while calis:

        

        ekran.fill((54, 128, 247))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0

        # yazi_yaz("Voltaj =",font,siyah, ekran, 100,55,)# ikinci slota yazılanlar ekranda gözükecektir
        # yazi_yaz("Amper =",font,siyah ,ekran , 100,105,)
        yazi_yaz("Voltaj giriniz:",font,siyah ,ekran ,100,75,)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                calis = False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()

            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#direnctekivoltaj'):
                global direnc_hesaplarken_voltaj
                direnc_hesaplarken_voltaj = (event.text)  
                direncin_2_loop(event.text)
            direncvoltaji.process_events(event)
        direncvoltaji.update(UI_REFRESH_RATE)



        direncvoltaji.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)
#direncin 2. loopu 
def direncin_2_loop(direncloop2):
    calis = True
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    while calis:

        

        ekran.fill((54, 128, 247))
            

        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0

        yazi_yaz(f"Voltaj={direnc_hesaplarken_voltaj}V" ,font, (255,255,255) ,ekran ,20,300)
        yazi_yaz("Akım giriniz:",font,siyah ,ekran ,100,75,)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                go= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()


            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#direnctekiakim'):
                  global direnc_hesaplanrken_akim
                  direnc_hesaplanrken_akim= (event.text)
                  direnc_3_loop(event.text)
            direncakimi.process_events(event)
        pygame.display.update


        direncakimi.draw_ui(ekran)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)
        direncakimi.update(UI_REFRESH_RATE)


# direncin 3. loopu 
def direnc_3_loop(direncloop3):
    running = True
    en,boy = 1000 ,700
    ekran =pygame.display.set_mode((en, boy ))
    a , b = pygame.mouse.get_pos()
    while running:
        ekran.fill((54, 128, 247))
        # EKRANDAKİ RESİMLER: 
        pil_img = pg.image.load('görseller/pil_30.png')
        direnc_img = pg.image.load('görseller/direnc_11.png')
        voltmetre_img = pg.image.load("görseller/voltmetre_10.png")
        ampermetre_img = pg.image.load("görseller/ampermetre_10.png")
        ampuldevre_img = pg.image.load("görseller/ampul.png")
        devre_img=pg.image.load("görseller/devre1.png")



        ekran.blit(devre_img,(260,220))
        ekran.blit(pil_img, (600,480))
        ekran.blit(direnc_img, (600,270))
        ekran.blit(voltmetre_img, (560, 505))
        ekran.blit(ampermetre_img, (380, 475))
        ekran.blit(ampuldevre_img, (430, 190))
        siyah = 0,0,0
        
        yazi_yaz(f"Voltaj={direnc_hesaplarken_voltaj} V" ,font, (255,255,255) ,ekran ,20,300)
        yazi_yaz(f"Akım={direnc_hesaplanrken_akim} A",font ,(255,255,255),ekran,20 , 350)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()
                    
        if  direnc_hesaplanrken_akim == float and  direnc_hesaplanrken_akim == float:
            direnc_degeri= float(direnc_hesaplarken_voltaj)/ float(direnc_hesaplanrken_akim)
            yazi_yaz(f"★DİRENÇ:{direnc_degeri} Ω★",font ,(77, 237, 52),ekran,5,400) 
        else :
            deger_giriniz()

        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)

def deger_giriniz():


    run  = True 
    while run:

        ekran.fill((54, 128, 247))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running= False

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    arayuz()
        font1 = pygame.font.Font("font.ttf", 20)
        font2 = pygame.font.Font("font.ttf",15)
        yazi_yaz ("LÜTFEN SAYISAL DEĞER GİRİNİZ",font1, (255,0,0), ekran , 250,300)
        yazi_yaz ("MENÜYE DÖNMEK İÇİN ESC TUŞUNA BASINIZ!", font2, (255,255,50),ekran , 10 , 20)
        pygame.display.update()
        pygame.display.flip()
        mainClock.tick(60)

main_menu()
