# Yaptığımız işlemler sonucunda asker sayılarımızı daha rahat görebilmek için işlemden sonra birkaç saniye duraksama
# olması için time.sleep komutunu kullandım. Bu yüzden time modulünü import ettim.
import time

# Çeşitli askerlerden listeler oluşturdum.
kilicliAsker = []
mizrakliAsker = []
okcuAsker = []
atliAsker = []
mancinik = []

# asker sınıfı oluşturdum.
# HP Sağlık, SP Saldırı Puanı, SV savunma puanı.
# Bu kodda şimdilik HP'nin önemi olmayacak. Öylesine ekledim.
class Asker:
    def __init__(self, HP, SP, SV):
        self.HP = HP
        self.SP = SP
        self.SV = SV

# Asker Ekleme Fonksiyonu
def AskerEkle():
    # 1 ile 5 arasında bir menu tercihi yapılacak. Yoksa istenilen değer alınana kadar döngü devam edecek.
    menuSecim = int(
        input("Hangi asker türünden ekleme yapmak istiyorsunuz?:\n1-Kılıçlı\n2-Mızraklı\n3-Okçu\n4-Atlı\n5-Mancınık\n"))

    while menuSecim < 1 or menuSecim > 5:
        menuSecim = int(input(
            "Lütfen 1 ile 5 arasında değer girin:\n1-Kılıçlı\n2-Mızraklı\n3-Okçu\n4-Atlı\n5-Mancınık\n"))

    # Girdiğimiz a değerine göre bir for döngüsü olacak ve her seferinde kilicliBirim adında bir asker nesnesi üretecek.
    # Bu kilicliBirim askerleri yukarıda oluşturduğum kilicliAsker[] listesinin içine eklenecek.
    # Len komutu sayesinde kaç tane askerimiz olduğunu görmüş olacağız. 1 saniye bekleyip tekrar işleme devam edeceğiz.
    if menuSecim == 1:
        a = int(input("Kaç tane kılıçlı asker istiyorsunuz: "))
        for i in range(0, a):
            kilicliBirim = Asker(20, 35, 20)
            kilicliAsker.append(kilicliBirim)
        print("Kılıçlı asker sayısı: ", len(kilicliAsker))
        time.sleep(1)

    if menuSecim == 2:
        a = int(input("Kaç tane mızraklı asker istiyorsunuz: "))
        for i in range(0, a):
            mizrakliBirim = Asker(25, 15, 35)
            mizrakliAsker.append(mizrakliBirim)
        print("Mızraklı asker sayısı: ", len(mizrakliAsker))
        time.sleep(1)

    if menuSecim == 3:
        a = int(input("Kaç tane okçu asker istiyorsunuz: "))
        for i in range(0, a):
            okcuBirim = Asker(15, 40, 40)
            okcuAsker.append(okcuBirim)
        print("Okçu asker sayısı: ", len(okcuAsker))
        time.sleep(1)

    if menuSecim == 4:
        a = int(input("Kaç tane atlı asker istiyorsunuz: "))
        for i in range(0, a):
            atliBirim = Asker(50, 60, 40)
            atliAsker.append(atliBirim)
        print("Atlı asker sayısı: ", len(atliAsker))
        time.sleep(1)

    if menuSecim == 5:
        a = int(input("Kaç tane mancınık istiyorsunuz: "))
        for i in range(0, a):
            mancinikBirim = Asker(10, 100, 50)
            mancinik.append(mancinikBirim)
        print("Mancınık sayısı: ", len(mancinik))
        time.sleep(1)

# asker çıkarma işlemi
def AskerCikar():
    # 1 ile 5 arasında bir değer alacağız. Fazlası ya da az olursa döngüye girecek.
    menuSecim = int(
        input("Hangi asker türünden terhis yapmak istiyorsunuz?:\n1-Kılıçlı\n2-Mızraklı\n3-Okçu\n4-Atlı\n5-Mancınık\n"))

    while menuSecim < 1 or menuSecim > 5:
        menuSecim = int(input(
            "Lütfen 1 ile 5 arasında değer girin:\n1-Kılıçlı\n2-Mızraklı\n3-Okçu\n4-Atlı\n5-Mancınık\n"))

    # b değişkenine çıkarmak istediğimiz miktarı giriyoruz.
    # kilicliAsker listesinden girdiğimiz değer kadar eleman çıkarmış oluyoruz.
    # Eğer ":" işareti b'nin önünde olsaydı ([b:]) girdiğimiz değer kadar askerimiz olacaktı.
    # Bu da yanlış olacaktı. Bu kısıma dikkat edin.
    # Daha sonra silme işlemini yaptıktan sonra birimimizin yeni miktarını görüyoruz.
    # 1 saniye bekledikten sonra program çalışmaya devam ediyor.
    if menuSecim == 1:
        b = int(input("Kaç tane kılıçlı asker çıkaracaksınız: "))
        del kilicliAsker[:b]
        print("{} tane Kılıçlı terhis edildi.Kılıçlı asker sayısı: ".format(b), len(kilicliAsker))
        time.sleep(1)

    if menuSecim == 2:
        b = int(input("Kaç tane mızraklı birim çıkaracaksınız: "))
        del mizrakliAsker[:b]
        print("{} tane Mızraklı terhis edildi.Mızraklı asker sayısı: ".format(b), len(mizrakliAsker))
        time.sleep(1)

    if menuSecim == 3:
        b = int(input("Kaç tane okçu birim çıkaracaksınız: "))
        del okcuAsker[:b]
        print("{} tane Okçu terhis edildi.Okçu asker sayısı: ".format(b), len(okcuAsker))
        time.sleep(1)

    if menuSecim == 4:
        b = int(input("Kaç tane atlı birim çıkaracaksınız: "))
        del atliAsker[:b]
        print("{} tane Atlı terhis edildi.Atlı asker sayısı: ".format(b), len(atliAsker))
        time.sleep(1)

    if menuSecim == 5:
        b = int(input("Kaç tane mancınık çıkaraksınız: "))
        del mancinik[:b]
        print("{} Mancınık terhis edildi. Mancınık sayısı: {}".format(b, str(len(mancinik))))
        time.sleep(1)

# Bilgi görme ekranı oluşturduğumuz birliklerin güncel halini bize gösteriyor. Sadece Print komutnu kullandık.
# Miktarları 2 saniye boyunca gördükten sonra tekrar program işleyişine devam ediyor.
def BilgiGor():
    print(f"""
Kılıçlı Asker   :{len(kilicliAsker)} Adet
Mızraklı Asker  :{len(mizrakliAsker)} Adet
Okçu Asker      :{len(okcuAsker)} Adet
Atlı Asker      :{len(atliAsker)} Adet
Mancınık        :{len(mancinik)} Adet
TOPLAM          :{len(kilicliAsker) + len(mizrakliAsker) + len(okcuAsker) + len(atliAsker) + len(mancinik)} Adet Birim
""")
    # Birliğin toplam savaş gücünü gösteren kod.
    ToplamSP = sum(tp.SP for tp in kilicliAsker) + sum(tp.SP for tp in mizrakliAsker) + sum(
        tp.SP for tp in okcuAsker) + sum(tp.SP for tp in atliAsker) + sum(tp.SP for tp in mancinik)
    print("Toplam Savaş Gücü:", ToplamSP)
    time.sleep(2)