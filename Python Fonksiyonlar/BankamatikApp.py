# Bankamatik Uygulaması

SadıkHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '12345678',
    'bakiye': 3000,
    'ekHesap': 2000
}

SelimHesap={
    'ad': 'Selim Çınar',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h): ')
            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('Üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")    

paraCek(SadıkHesap,2000)
bakiyeSorgula(SadıkHesap)

