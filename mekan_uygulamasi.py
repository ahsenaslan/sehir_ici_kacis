from typing import List, Optional

class Kullanici:
    def __init__(self, kullanici_adi: str):
        self.kullanici_adi = kullanici_adi
        self.favoriler: List[Mekan] = []

class Sehir:
    def __init__(self, ad: str):
        self.ad = ad
        self.ilceler: List[Ilce] = []

class Ilce:
    def __init__(self, ad: str, sehir: Sehir):
        self.ad = ad
        self.sehir = sehir
        self.mekanlar: List[Mekan] = []

class Kategori:
    def __init__(self, ad: str):
        self.ad = ad

class Mekan:
    def __init__(self, ad: str, kategori: Kategori, ilce: Ilce):
        self.ad = ad
        self.kategori = kategori
        self.ilce = ilce
        self.puanlar: List[int] = []
        self.yorumlar: List[Yorum] = []
        self.rezervasyonlar: List[Rezervasyon] = []

    def ortalama_puan(self) -> float:
        return sum(self.puanlar) / len(self.puanlar) if self.puanlar else 0

class Yorum:
    def __init__(self, kullanici: Kullanici, icerik: str):
        self.kullanici = kullanici
        self.icerik = icerik

class Rezervasyon:
    def __init__(self, kullanici: Kullanici, mekan: Mekan, tarih: str):
        self.kullanici = kullanici
        self.mekan = mekan
        self.tarih = tarih

def ornek_veri_olustur():
    # Kategoriler
    kafe = Kategori("Kafe")
    restoran = Kategori("Restoran")
    muze = Kategori("Müze")

    # Şehir ve ilçeler
    istanbul = Sehir("İstanbul")
    kadikoy = Ilce("Kadıköy", istanbul)
    besiktas = Ilce("Beşiktaş", istanbul)
    istanbul.ilceler.extend([kadikoy, besiktas])

    ankara = Sehir("Ankara")
    kizilay = Ilce("Kızılay", ankara)
    ankara.ilceler.append(kizilay)

    # Mekanlar
    mekan1 = Mekan("Moda Kafe", kafe, kadikoy)
    mekan2 = Mekan("Beşiktaş Restoran", restoran, besiktas)
    mekan3 = Mekan("Ankara Müzesi", muze, kizilay)
    kadikoy.mekanlar.append(mekan1)
    besiktas.mekanlar.append(mekan2)
    kizilay.mekanlar.append(mekan3)

    # Kullanıcı
    kullanici1 = Kullanici("ahmet")

    return {
        "sehirler": [istanbul, ankara],
        "kategoriler": [kafe, restoran, muze],
        "kullanicilar": [kullanici1]
    }

def mekanlari_listele(sehir_adi=None, ilce_adi=None, kategori_adi=None):
    veri = ornek_veri_olustur()
    sehirler = veri["sehirler"]
    mekanlar = []
    for sehir in sehirler:
        if sehir_adi and sehir.ad != sehir_adi:
            continue
        for ilce in sehir.ilceler:
            if ilce_adi and ilce.ad != ilce_adi:
                continue
            for mekan in ilce.mekanlar:
                if kategori_adi and mekan.kategori.ad != kategori_adi:
                    continue
                mekanlar.append(mekan)
    return mekanlar

turkiye_sehirleri = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

def secim_yap():
    print("Türkiye'deki Şehirler:")
    for i, sehir in enumerate(turkiye_sehirleri, 1):
        print(f"{i}. {sehir}")
    sehir_no = int(input("Bir şehir seçin (numara): "))
    secilen_sehir = turkiye_sehirleri[sehir_no-1]

    # Örnek ilçeler ve kategoriler (gerçek projede veritabanı ile genişletilebilir)
    ornek_ilceler = {
        "İstanbul": ["Kadıköy", "Beşiktaş", "Üsküdar"],
        "Ankara": ["Kızılay", "Çankaya", "Keçiören"],
        "İzmir": ["Konak", "Bornova", "Karşıyaka"]
    }
    ilceler = ornek_ilceler.get(secilen_sehir, ["Merkez"])
    print(f"\n{secilen_sehir} için ilçeler:")
    for i, ilce in enumerate(ilceler, 1):
        print(f"{i}. {ilce}")
    ilce_no = int(input("Bir ilçe seçin (numara): "))
    secilen_ilce = ilceler[ilce_no-1]

    kategoriler = ["Kafe", "Restoran", "Müze"]
    print("\nKategoriler:")
    for i, kat in enumerate(kategoriler, 1):
        print(f"{i}. {kat}")
    kat_no = int(input("Bir kategori seçin (numara): "))
    secilen_kat = kategoriler[kat_no-1]

    print(f"\nSeçiminiz: {secilen_sehir} / {secilen_ilce} / {secilen_kat}")
    return secilen_sehir, secilen_ilce, secilen_kat

# Örnek kullanım:
if __name__ == "__main__":
    sehir, ilce, kategori = secim_yap()
    print(f"\nSeçtiğiniz kriterlere uygun mekanlar:")
    mekanlar = mekanlari_listele(sehir_adi=sehir, ilce_adi=ilce, kategori_adi=kategori)
    if mekanlar:
        for mekan in mekanlar:
            print(f"- {mekan.ad}")
    else:
        print("Uygun mekan bulunamadı.")

        #kdmkedmekfn
        
    

