# random modülü düşmana rastgelee asker üretmesi için kullanıyoruz.
# time modülü de işlemleri rahat takip edeiblmek için arada kodları 1 saniyeliğine durdurmak için çağırdım.
import random
import time
# AskerModül dosyası ile düşman askerlerini oluşturmak için kullandım.
import AskerModul

# Savaşa girmeyi istediğimizde çalışacak fonksiyon.
def SavasGir():

    # Fonksiyon çalıştırıldığın ilk önce random şekilde düşman ordusu oluşturucak.
    dusmanKilicli = []
    dusmanMizrakli = []
    dusmanOkcu = []
    dusmanAtli = []
    dusmanMancinik = []

    # düşman kılıçlı birim üretimi
    # random bir adet sayısı belirliyoruz. Sonra Asker sınıfından bir nesne türetip miktarını arttırıyoruz.
    kilicliAdet = random.randint(30, 121)
    for i in range(kilicliAdet):
        dusmanKilicliBirim = AskerModul.Asker(20, 35, 20)
        dusmanKilicli.append(dusmanKilicliBirim)

    # düşman mızraklı birim üretimi
    mizrakliAdet = random.randint(30,121)
    for i in range(mizrakliAdet):
        dusmanMizrakliBirim = AskerModul.Asker(25, 15, 35)
        dusmanMizrakli.append(dusmanMizrakliBirim)

    # düşman okçu birim üretimi
    okcuAdet = random.randint(30, 121)
    for i in range(okcuAdet):
        dusmanOkcuBirim = AskerModul.Asker(15, 40, 15)
        dusmanOkcu.append(dusmanOkcuBirim)

    # düşman atlı birim üretimi
    atliAdet = random.randint(30, 121)
    for i in range(atliAdet):
        dusmanAtliBirim = AskerModul.Asker(50, 60, 40)
        dusmanAtli.append(dusmanAtliBirim)

    # düşman mancınık birim üretimi
    mancinikAdet = random.randint(1, 11)
    for i in range(mancinikAdet):
        dusmanMancinikBirim = AskerModul.Asker(10, 100, 50)
        dusmanMancinik.append(dusmanMancinikBirim)

    # Düşman askerlerinin toplam savunma Puanı hesaplanıyor.
    dusmanToplamSV = sum(tp.SV for tp in dusmanKilicli) + sum(tp.SV for tp in dusmanMizrakli) + sum(
        tp.SV for tp in dusmanOkcu) + sum(tp.SV for tp in dusmanAtli) + sum(tp.SV for tp in dusmanMancinik)

    # Bizim savunma puanlarımızı tekrardan buraya tanımlıyorum.
    ToplamSP = sum(tp.SP for tp in AskerModul.kilicliAsker) + sum(tp.SP for tp in AskerModul.mizrakliAsker) + sum(
        tp.SP for tp in AskerModul.okcuAsker) + sum(tp.SP for tp in AskerModul.atliAsker) + sum(tp.SP for tp in AskerModul.mancinik)

    AskerModul.BilgiGor()
    print("")
    print(f"""Düşman Birlik Sayısı: 
Kılıçlı Asker   :{len(dusmanKilicli)} Adet
Mızraklı Asker  :{len(dusmanMizrakli)} Adet
Okçu Asker      :{len(dusmanOkcu)} Adet
Atlı Asker      :{len(dusmanAtli)} Adet
Mancınık        :{len(dusmanMancinik)} Adet
TOPLAM          :{len(dusmanKilicli) + len(dusmanMizrakli) + len(dusmanOkcu) + len(dusmanAtli) + len(dusmanMancinik)} Adet Birim

Toplam Savunma Puanı: {dusmanToplamSV}
""")
    # bundan sonrası savaşın başladığı kısım.
    time.sleep(1)
    print("")
    print("Savaş Başladı")
    time.sleep(1)
    print("Savaş Devam Ediyor.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(0.5)

    if ToplamSP > dusmanToplamSV:
        print("Tebrikler! Savaşı Kazandınız.")
    else:
        print("Savaşı kaybettiniz!")