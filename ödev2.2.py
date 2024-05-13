def sayi_okunusu(sayi):
    birler = ['Sıfır', 'Bir', 'İki', 'Üç', 'Dört', 'Beş', 'Altı', 'Yedi', 'Sekiz', 'Dokuz']
    onlar = ['','On', 'Yirmi', 'Otuz', 'Kırk', 'Elli', 'Altmış', 'Yetmiş', 'Seksen', 'Doksan']

    onlar_basamagi = sayi // 10
    birler_basamagi = sayi % 10

    if birler_basamagi == 0:
        return onlar[onlar_basamagi]
    elif onlar_basamagi == 0:
        return birler[birler_basamagi]
    else:
        return onlar[onlar_basamagi] + " " + birler[birler_basamagi]

def sayi_atama(sayi):
    if 10 <= sayi <= 99:
        return sayi_okunusu(sayi)
    else:
        return "Lütfen iki basamakli bir sayi girin."

girilen_sayi = 7
okunus = sayi_atama(girilen_sayi)
print(f"{girilen_sayi} sayısının okunuşu: {okunus}")

