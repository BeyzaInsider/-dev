
def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
    tam_bolunenler = []  
    sayi_adedi = 0 
    

    for sayi in range(min_sayi, max_sayi + 1):
        if sayi % bolen_sayi == 0:
            tam_bolunenler = tam_bolunenler + [sayi]  
            sayi_adedi = sayi_adedi + 1  
    
    return tam_bolunenler, sayi_adedi


min_sayi = 10
max_sayi = 50
bolen_sayi = 5
tam_bolunenler, sayi_adedi = bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi)

print(f"{min_sayi} ile {max_sayi} arasinda {bolen_sayi} ile tam bölünebilen sayılar:")
print(tam_bolunenler)
print(f"Bu araliktaki tam bölünebilen sayi adedi: {sayi_adedi}")