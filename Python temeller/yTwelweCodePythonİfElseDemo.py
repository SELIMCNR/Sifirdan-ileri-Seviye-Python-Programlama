



# 1- Enerji hesabı kw/saat 
#Aktif Enerji Birim Fiyatı X kWh = Aktif Enerji Bedeli (A)
#Dağıtım Bedeli Birim Fiyatı X kWh = Dağıtım Bedeli (D)
#Aktif Enerji Bedeli (A) x %5 = Elektrik Tüketim Vergisi Bedeli (T)
watt = float(input("Saatlik Kullanılan  watt: "))
saat = float(input("Kullanılan saat: "))
kullanıcı = input("kullanıcı adı:     örnek(ev,isyeri)")
kwh = watt * saat /1000
aktifenerji = kwh * 0.218
dagitim = kwh * 0.546
vergi = aktifenerji * 0.05
enerjitutarı = aktifenerji + dagitim + vergi


if (kullanıcı =="ev"):
    enerjitutarı = enerjitutarı * 0.8
elif (kullanıcı == "isyeri"):
    enerjitutarı = enerjitutarı * 1.18

print("Hesaplamak istediğiniz saateki elektrik tüketim bedeliniz : ",enerjitutarı)        
