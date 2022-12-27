#kullanılacak yazı tipini seçme

import pygame as pg 
import sys
pg.init()
clock=pg.time.Clock()

#ekran boyutunu ayarlama ve renk seçme
en , boy =  800 , 600
mavi = 20, 15, 133
siyah =2, 3, 3

ekran = pg.display.set_mode( (en,boy)  )

font = pg.font.SysFont('timesnewroman' , 32) # parantez içindeki lk kısım yazı tipi ikinci kısım yazı büyüklüğüdür

#yazı yazma komutunun kodu
def ekrana_yazi_yaz(ekran,metin,tx,ty,renk):
    global font 
    text = font.render(metin , True , renk )
    textReckt = text.get_rect()
    textReckt.centerx = tx
    textReckt.centery = ty
    ekran.blit(text , textReckt)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(mavi)
    ekrana_yazi_yaz(ekran,"deneme",400,300,siyah)# ikinci slota yazılanlar ekranda gözükecektir
    ekrana_yazi_yaz(ekran,"deneme2",200,500,siyah)

    pg.display.flip()
    clock.tick(1)

