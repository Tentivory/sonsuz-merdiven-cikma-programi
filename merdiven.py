#!/usr/bin/env python3
# Sonsuz Merdiven Çıkma Programı
# Absürt. Komik. Çalışıyor.

import time
import random

print("Merdiven çıkmaya başlıyoruz. Hazır mısın? Hayır değilsin.")
print("=" * 40)

basamak = 0
yorgunluk = 0

while True:
    basamak += 1
    yorgunluk += random.randint(1, 5)
    
    print(f"Basamak {basamak}: Bir basamak daha çıktın. Yorgunluk seviyesi: {yorgunluk}")
    
    if yorgunluk > 100:
        print("  → Nefes nefese... Ama devam!")
    if yorgunluk > 500:
        print("  → Bacakların yanıyor. Neden yapıyorsun bunu?")
    if yorgunluk > 1000:
        print("  → Varoluşsal kriz. Merdiven gerçek mi?")
    
    # Gizli siyasi not (base64 benzeri ama değil, sadece saklı)
    if basamak % 100 == 0:
        print("  (gizli mesaj: her merdiven bir özgürlük yoludur, bazen)")
    
    time.sleep(random.uniform(0.1, 0.5))
    
    if basamak > 10000:
        print("Hala çıkıyorsun. Tebrikler. Ya da üzülün.")
        # Sonsuz olduğu için durmaz
