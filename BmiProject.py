#bilgi kısmı
print("BMI hesaplamaya hoşgeldiniz!")
print("***********************")
print("     İDEAL BMI")
print(" YAŞ           BMI")
print("19-24         19-24")
print("25-34         20-25")
print("35-44         21-26")
print("45-54         22-27")
print("55-64         23-28")
print("65+           24-29")
print("***********************")

# 1- İlk olarak, kullanıcıdan yaşını, kilosunu ve boyunu alalım:
yas = int(input("yaşınız nedir: "))
kilo = float(input("kilonuz(kg) nedir: "))
boy = float(input("boyunuz(x.xx cm) nedir: "))

# 2- Şimdi kullanıcının Beden Kitle İndeksi'ni (BMI) hesaplayalım:
bmi= kilo/(boy*boy)
print("BMI değeriniz: ", round(bmi, 2)) #round virgülden sonra kaç basamak olacağını söylüyor1
# 3- Şimdi BMI değerine göre sağlık durumunu değerlendirelim:
if(bmi>=35):
    print("aşırı obez")
elif(bmi>=30 and bmi<35):
    print("obez")
elif(bmi>=25 and bmi<30):
    print("kilolu")
elif(bmi>=18.5 and bmi<25):
    print("normal")
else:
    print("zayıf")

# 4- Son olarak, kullanıcının ideal kilodan ne kadar uzak olduğunu söyleyelim:
ideal_kilo = 22 * (boy ** 2)
kilo_farki = kilo - ideal_kilo
if (kilo_farki > 0):
    print("İdeal kilonuzun üzerindesiniz. İdeal kiloya ulaşmak için", round(abs(kilo_farki), 2), "kg vermelisiniz.") #abs eğer eksili bi ifade çıkarsa diye mutlak işaret içine alıyor
elif (kilo_farki < 0):
     print("İdeal kilonuzun altındasınız. İdeal kiloya ulaşmak için", round(abs(kilo_farki), 2), "kg almalısınız.")
else:
    print("Tebrikler! İdeal kilodasınız!")

