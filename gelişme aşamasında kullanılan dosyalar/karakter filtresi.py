#kötü karakter listesi 
kotu_kar = ["+","!","?","/"]
# test satırı 
test_satir = "m+e!r/h?a+b!a"

print("Orjinal giriş :" + test_satir)
#kötü karakterleri yer değiştirme komutu ile  filtreleme 
for i in kotu_kar :
    test_satir = test_satir.replace(i,"")

print("Filtre edlimiş hal :" + str(test_satir))