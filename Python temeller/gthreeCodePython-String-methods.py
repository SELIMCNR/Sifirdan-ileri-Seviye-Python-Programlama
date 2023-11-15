message = " Hello There. My name is Selim Çınar."

message = message.upper() # upper() methodu string ifadenin tüm karakterlerini büyük harfe çevirir.
message = message.lower() # lower() methodu string ifadenin tüm karakterlerini küçük harfe çevirir.
message = message.title() # title() methodu string ifadenin tüm kelimelerinin ilk harfini büyük harfe çevirir.
message = message.capitalize() # capitalize() methodu string ifadenin sadece ilk harfini büyük harfe çevirir.
message = message.strip() # strip() methodu string ifadenin başındaki ve sonundaki boşlukları siler.
message = message.split(".") # split() methodu string ifadeyi boşluklardan ayırır ve bir liste haline getirir.
message = '---'.join(message) # join() methodu string ifadeyi birleştirir.
index = message.find('Selim') # find() methodu string ifade içinde aradığımız kelimenin index numarasını verir.
isFound = message.startswith('H') # startswith() methodu string ifadenin başlangıç karakterini kontrol eder.
isFound = message.endswith('r') # endswith() methodu string ifadenin bitiş karakterini kontrol eder.
message = message.replace('Selim','Çınar') # replace() methodu string ifade içindeki karakterleri değiştirir.
message = message.replace('' ,'*')
message = message.replace('ç','c').replace('ı','i').replace(' ','-')
message = message.center(50,'*') # center() methodu string ifadeyi ortalar.
#w3schools pythonda ayrıntılı methodlar var.
print(message)
print(message[2]) # splitten gelen listeyi index numarasına göre yazdırır.
message = " Hello There. My name is Selim Çınar."
#Replace methodu
message = message.replace(' ','-')
print(message)
message = message.replace('Hello-There.','Hi the')
print(message)

#strip methodu
message = " Hello There. My name is Selim Çınar."
message = message.strip()
print(message)

#split methodu
message = message.split(' ')
print(message)
print(message[0:5])