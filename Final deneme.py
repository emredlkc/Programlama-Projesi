import pygame as pg 
import sys

pg.init()
clock = pg.time.Clock()

# ekran boyu ayarlaması
ekran = pg.display.set_mode((900,600))

#Uygulama ismi ayarlaması 
pg.display.set_caption("FİNAL PROJESİ")

#Uygulama resmi ayralanması 
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)
running = True


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


#arka plan rengi ve şekil çizimi
#ekrana yazılan degerler
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    ekrana_yazi_yaz(ekran,"deneme =",750,50,siyah)# ikinci slota yazılanlar ekranda gözükecektir
    ekrana_yazi_yaz(ekran,"deneme2 =",750,100,siyah)
    for cord in kareler:
        pg.draw.rect(ekran,beyaz,(150,150,kare_en,kare_boy), 3 )

    pg.display.flip()
    clock.tick(1)



