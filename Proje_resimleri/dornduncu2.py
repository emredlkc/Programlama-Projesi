#FUNCTIONS

#f(x) = 2x+5
# x=3
# functıon = defnine ( def)

# def fx() :
#     print(2 + 5)

# fx()

# def f(x) :
#     print( 2 *x + 5 )

# f(5)
# f(10)
# f(20)

# def diskriminant ( a , b , c) :
#     print(b*b - 4*a*c)

#2x^2 + 10x -9 = 0 
#diskriminant(2,10,-9)

#  def iki_katı () :
#      #global x
#      x = 2 
#      x =  2 * x
#      return x

#x = 5 
#print(iki_katı())
#x = iki_katı(x)
#print(x)



#return None

#print(iki_katı (iki_katı(23)))

# import math

# def final_hesapla (vize):
#     if vize <50 :
#         final_icin_gerkelı_not =( 50 - 0.4 * vize ) / 0.6
#         print("Final için alımas gereken not :"  , math.ceil(final_icin_gerkelı_not))
#     if vize >= 50 :
#         print("Final için almanız erken not: 50")
# final_hesapla(35)



#varsayılan degerli parametre / arguman 
#def ussunu_al (sayı=2,us): # hata , çünkü varsayılandegere atanırsa sonrakilerdede varsayılan deger olmalı
def ussunu_al (sayı="", us=""):
    "fonkla ilgilibilgiler"
    return sayı**us

# print(ussunu_al(5,3))
# print(ussunu_al(5) )
# print(ussunu_al())
# print(ussunu_al(us=5))

# yaz=print
# yaz("mal")

print(ussunu_al(2,4))
print(ussunu_al(3,3))