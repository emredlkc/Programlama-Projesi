import pygame 
import sys
# intialize the pygame: 

pygame.init()


# ekranı oluşturma:
screen = pygame.display.set_mode((1200,1000))

# BAŞLIK AYARLAMA VE BAŞLIĞIIN YANINDAKİ LOGOYU AYARLAMA 

pygame.display.set_caption("deneme oyunu ")
icon =pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# ekrana  malzeme ekleme resimli bir şeyler ekleme    

playerImg=pygame.image.load("roket.png")

playerX =370
playerY= 480 
playerX_change= 0
playerY_change = 0 

# ekrana eklemek istediğimiz şeyi tanımlamımız için bir fonksiyon oluşturmamız gerekli
def player(x,y):
    screen.blit(playerImg ,(x ,y))




# GAME LOOP   anahatlarıyla  oyuunun yada uygulamnın içeriğini yerleştidiğimiz bölüm


running = True

while running:
    
# EKRANI AYARLAMA  

    screen.fill((0,0,0))  # ekranın rengini ayarlama ... 
   

#    KOYMUŞ OLDUGUMUZ İMGELERİ OTOMATİK HARAKET ETTİRME 
    # if playerX < 800:
    #     playerX += 0.1

    # if playerY > 0:
    #     playerY -= 0.1



# ANAHATLARI 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False



#  eğer bir tuşa bastıpımızda sağa yada sola gideceğini ayarlama 

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
          
            if event.key== pygame.K_RIGHT:
                playerX_change = +0.1


    if event.type == pygame.KEYUP:
                if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change= 0


    # oyunucunun yönünü ayarladığımız elemanı girelim     
    
    playerX += playerX_change  
    
    #  yaptığımız oyuncunun yukarı yada aşağı gideceğini ayarlama
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.1
          
            if event.key== pygame.K_DOWN:
                playerY_change = +0.1


    if event.type == pygame.KEYUP:
                if event.key== pygame.K_DOWN or event.key == pygame.K_UP:
                    playerY_change= 0

    playerY += playerY_change





# tanımlamış oldugumuz oyuncu (player) fonksiyonunu yerleştirme işlemi 
    player(playerX , playerY)

    
    pygame.display.update()


