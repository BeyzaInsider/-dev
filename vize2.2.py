def harf_notu(vize1, vize2, final):
    sonuc = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
    
   
    
    if sonuc >= 90:
        return "AA"
    elif sonuc >= 85:
        return "BA"
    elif sonuc >= 80:
        return "BB"
    elif sonuc >= 75:
        return "CB"
    elif sonuc >= 70:
        return "CC"
    elif sonuc >= 65:
        return "DC"
    elif sonuc >= 60:
        return "DD"
    elif sonuc >= 55:
        return "FD"
    else:
        return "FF"

vize1 = float(input("Vize 1 notunu girin: "))
vize2 = float(input("Vize 2 notunu girin: "))
final = float(input("Final notunu girin: "))

# Harf notunu hesapla ve yazdır
print("Harf notunuz:", harf_notu(vize1, vize2, final))