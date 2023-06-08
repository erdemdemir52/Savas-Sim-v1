import AskerModul
import SavasModul

sistemDurum = True

while sistemDurum:
    try:
        menuSec = int(input("Hangi işlemi yapmak istiyorsunuz:"
                            "\n1-Asker Ekle\n2-Asker Çıkar\n3-Birliği Gör\n4-Savaşa Gir\n5-Çıkış"))
        while menuSec < 1 or menuSec > 5:
            menuSec = int(input("Lütfen 1 ile 5 arasında bir değer giriniz:"
                                "\n1-Asker Ekle\n2-Asker Çıkar\n3-Birliği Gör\n4-Savaşa Gir\n5-Çıkış"))
    except:
        menuSec = int(input("Lütfen sayısal değer giriniz:"
                            "\n1-Asker Ekle\n2-Asker Çıkar\n3-Birliği Gör\n4-Savaşa Gir\n5-Çıkış"))

    if menuSec == 1:
        AskerModul.AskerEkle()

    if menuSec == 2:
        AskerModul.AskerCikar()

    if menuSec == 3:
        AskerModul.BilgiGor()

    if menuSec == 4:
        SavasModul.SavasGir()

    if menuSec == 5:
        print("Sistemden çıkılıyor.")
        sistemDurum = False