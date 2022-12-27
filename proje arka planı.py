import pygame as pg
import sys
pg.init()
clock = pg.time.Clock()

# ekran en boy arka plan renkleri
en , boy = 800 , 600
gri = 125,125,125
beyaz = 255 ,255, 255
kzm = 255,0,0

ekran = pg.display.set_mode( (en,boy)  )

#çizilen dikdörtgen/karenin en ve boy oranı 
karolar = []
karo_en = 500
karo_boy = 250

for i in range(en//karo_en * boy//karo_boy) :
    karolar.append((i * karo_en % en, (i * karo_en // en)*karo_boy ))

#çizimin nereye yapılacağı
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(gri)
    for cord in karolar:
        pg.draw.rect(ekran,beyaz,(150,150,karo_en,karo_boy), 3 )
    
    pg.display.flip()
    clock.tick(1)