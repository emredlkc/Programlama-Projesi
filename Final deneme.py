import pygame as pg 
import sys
import random

pg.init()
clock = pg.time.Clock()

# ekran boyu ayarlaması
ekran = pg.display.set_mode((900,600))

#Uygulama ismi ayarlaması 
pg.display.set_caption("FİNAL PROJESİ")


#Uygulama resmi ayralanması 
icon = pg.image.load("ampul.png")
pg.display.set_icon(icon)
running = True

# arka plan ayarlamak için gerekli kısım
class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



#ekran en boy ayarı ve renk seçenekleri 
en , boy = 900 , 600
gri = 125,125,125
beyaz = 255 ,255, 255
kirmizi = 255,0,0
siyah = 5 ,5 ,5 
sari = 174, 242, 15
mavi = 72, 15, 242
yesil = 26, 138, 4

ekran = pg.display.set_mode( (en,boy)  )

# ekarana çizilen dikdortgen/kare nin en ve boy oranı
kareler = []
kare_en = 500
kare_boy = 250

for i in range(en//kare_en * boy//kare_boy) :
    kareler.append((i * kare_en % en, (i * kare_en // en)*kare_boy ))

#yazı tipi ve yazı boyutu seçme 
    font = pg.font.SysFont('timesnewroman' , 18)

# ekrana yazı yazma kodu 
    def ekrana_yazi_yaz(ekran,metin,tx,ty,renk):
        global font 
        text = font.render(metin , True , renk )
        textReckt = text.get_rect()
        textReckt.centerx = tx
        textReckt.centery = ty
        ekran.blit(text , textReckt)

# direnç a voltaj b amper c
a=random.randrange(1,10)
b=random.randrange(1,10)
c = b/a

#resimleri program hafızasına yükleme kodu
pil_img = pg.image.load('pil_30.png')
direnc_img = pg.image.load('direnc_11.png')
voltmetre_img = pg.image.load("voltmetre_10.png")
ampermetre_img = pg.image.load("ampermetre_10.png")
ampuldevre_img = pg.image.load("ampuldevre_15.png")


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    
    # arka plan resmini seçtiğimiz kısım 
    BackGround = Background('arkaplann.png', [0,0])
    ekran.blit(BackGround.image, BackGround.rect)

    # resim eklemek için gerekli kod
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    
    # şekil çizimi 
    for cord in kareler:
        pg.draw.rect(ekran,siyah,(190,180,kare_en,kare_boy), 5 )
    
    #Programda kullanılan resimleri ekrana ekleme
    ekran.blit(pil_img, (395,400))
    ekran.blit(direnc_img, (270, 166))
    ekran.blit(voltmetre_img, (355, 425))
    ekran.blit(ampermetre_img, (200, 398))
    ekran.blit(ampuldevre_img, (400, 150))

    #ekrana yazılan degerler
    ekrana_yazi_yaz(ekran,"Voltaj =",750,50,siyah)# ikinci slota yazılanlar ekranda gözükecektir
    ekrana_yazi_yaz(ekran,"Amper =",750,100,siyah)
    ekrana_yazi_yaz(ekran,"Direnç =",750,150,siyah)
    ekrana_yazi_yaz(ekran,str(a),800,150,siyah)
    ekrana_yazi_yaz(ekran,str(c),800,100,siyah)
    ekrana_yazi_yaz(ekran,str(b),800,50,siyah)
    
    pg.display.flip()
    clock.tick(1)














