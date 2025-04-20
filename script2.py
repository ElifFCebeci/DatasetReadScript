import pandas as pd
from collections import defaultdict
import os

# İşlenecek dosyanın tam yolu
dosya_yolu = r"C:\Users\Elif\OneDrive\Masaüstü\03-11\Syn.csv"  # <- buraya kendi dosya yolunu gir

sütun_sayac = defaultdict(int)
benign_toplam = 0
syn_toplam = 0

dosya = os.path.basename(dosya_yolu)

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

    # BENIGN ve SYN sayımı
    if " Label" in df.columns:
        benign_sayisi = (df[" Label"] == "BENIGN").sum()
        syn_sayisi = (df[" Label"] == "Syn").sum()
        benign_toplam += benign_sayisi
        syn_toplam += syn_sayisi
        print(f"{dosya} içinde BENIGN: {benign_sayisi}, SYN: {syn_sayisi}")
    else:
        print(f"{dosya} içinde ' Label' sütunu bulunamadı.")

except Exception as e:
    print(f"{dosya} okunurken hata oluştu: {e}")

print("\nToplam BENIGN sayısı:", benign_toplam)
print("Toplam SYN sayısı:", syn_toplam)

print("\nSütun (Etiket) Sayıları:")
for sutun, sayi in sütun_sayac.items():
    print(f"{sutun}: {sayi} kez bulundu")
