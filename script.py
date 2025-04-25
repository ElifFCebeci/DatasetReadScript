import pandas as pd
import os
from collections import defaultdict

klasor_yolu = 
sütun_sayac = defaultdict(int)
uzantilar = [".csv", ".xlsx", ".xls"]


print("Bulunan dosyalar:", os.listdir(klasor_yolu))

for dosya in os.listdir(klasor_yolu):
    if any(dosya.endswith(ext) for ext in uzantilar):
        dosya_yolu = os.path.join(klasor_yolu, dosya)
        try:
            print(f"\nİşleniyor: {dosya}")
            if dosya.endswith(".csv"):
                df = pd.read_csv(dosya_yolu, low_memory=False)
            else:
                df = pd.read_excel(dosya_yolu)

            print(f"{dosya} satır sayısı: {len(df)}")
            print(f"{dosya} sütunları: {df.columns.tolist()}")

            # Sütun sayacı
            for sutun in df.columns:
                sütun_sayac[sutun.strip()] += 1


        except Exception as e:
            print(f"{dosya} okunurken hata oluştu: {e}")


print("\nSütun (Etiket) Sayıları (kaç dosyada bulunduğu):")
for sutun, sayi in sütun_sayac.items():
    print(f"{sutun}: {sayi} dosyada") 
