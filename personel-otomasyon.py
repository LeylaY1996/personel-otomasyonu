def title():
    print("#################################################")
    print("#         PERSONEL OTOMASYON SİSTEMİ            #")
    print("#################################################")

def getChoice():
    return int(input("Menüden seciminizi yapınız:(1 ve 8 arasında secim yapınız.1 ve 8 dahil) \nSeciminiz:"))

def menu():
    print("\n\n*****************MENU*********************")
    print("*1.Personel Ekleme                       *")
    print("*2.Personel Güncelleme                   *")
    print("*3.Personel Arama                        *")
    print("*4.Personel Silme                        *")
    print("*5.Personel Maaş Hesaplama               *")
    print("*6.Personel Görüntüleme                  *")
    print("*7.Personel Dosyaya Yaz                  *")
    print("*8.Sistemden Çıkış                       *")
    print("**************************************   *")


personel_dict = {
    0: {
        "Personel Adı": "denme",
        "Personel Yaşı": 25,
        "Personel Departman": "Mühendis",
        "Personel Adres": "njkjk",
        "Personel Telefon": 000000000,
        "Personel Maaşı": 3500,
        "Personelin Bildiği Programlama Dilleri": ['Python', 'Php']
    },
    1: {
        "Personel Adı": "Ford",
        "Personel Yaşı": 25,
        "Personel Departman": "Mühendis",
        "Personel Adres": "njkjk",
        "Personel Telefon": 000000000,
        "Personel Maaşı": 3500,
        "Personelin Bildiği Programlama Dilleri": ['Python', 'Php']
    }

}

# calısıyor
def personel_ekleme(personel_dict):
    print("Yeni Personel Eklemek için:")
    print("Doldurmanız gereken bilgiler")
    id = int(input("id degeri giriniz:"))

    if (id in personel_dict):
        print("Girdiğiniz id degeri bulunmaktadır başka bir id degeri giriniz")
        personel_ekleme(personel_dict)
    else:
        personel_dict[id] = {}
        personel_dict[id]['Personel Adı'] = str(input("Personel ad ve soyad degeri giriniz:"))
        personel_dict[id]['Personel Yaşı'] = int(input("yas degeri giriniz:"))
        personel_dict[id]['Personel Departman'] = str(input("departman degeri giriniz:"))
        personel_dict[id]['Personel Telefon'] = str(input("telefon degeri giriniz:"))
        personel_dict[id]['Personel Maaşı'] = int(input("maas degeri giriniz:"))
        personel_dict[id]['Personelin Bildiği Programlama Dilleri'] = str(input("dil degeri giriniz:"))

        # personel yeni eklenen deger
        print(personel_dict[id])

    # sözlükteki tüm degerler
    for item in personel_dict:
        print("Personel ID'si : {} , Değerleri : {}".format(item, personel_dict[item]))
    menuden_cikis()

# çalışmıyor
def personel_guncelleme(personel_dict):
    print("Personel Güncelleme gelecek olan fonk")
    # sözlükteki tüm degerler
    for item in personel_dict:
        print("Key : {} , Value : {}".format(item, personel_dict[item]))

    print("\n\n")
    id = int(input("id degeri giriniz:"))

    if (id in personel_dict):
        guncelleme_secim = int(input("Personel Adı icin 1\n"
              "Personel Yaşı icin 2\n"
              "Personel Departman icin 3\n"
              "Personel Adres icin 4\n"
              "Personel Telefon icin 5\n"
              "Personel Maaşı icin 6\n"
              "Personel bildiği diller icin 7 secimi yapınız:"))

        if(guncelleme_secim == 1):
            ad = str(input("Personel adını giriniz:"))
            yeni_ad = personel_dict[id][ad]
            personel_dict[id]["Personel Adı"].update(yeni_ad)
        elif(guncelleme_secim == 2):
            yas = int(input("Personel yaşını giriniz:"))
            yeni_yas = personel_dict[id][yas]
            personel_dict[id]["Personel Yaşı"].update(yeni_yas)
        elif (guncelleme_secim == 3):
            departman = str(input("Personel departman giriniz:"))
            yeni_departman = personel_dict[id][departman]
            personel_dict[id]["Personel Departman"].update(yeni_departman)
        elif (guncelleme_secim == 4):
            adres = str(input("Personel adres giriniz:"))
            yeni_adres = personel_dict[id][adres]
            personel_dict[id]["Personel Adres"].update(yeni_adres)

            # sözlükteki tüm degerler
            for item in personel_dict:
                print("Personel ID'si : {} , Değerleri : {}".format(item, personel_dict[item]))

    else:
        print("aranılan id değeri personel sözlüğümüzde bulunmamakktadır\n\n")
        return False


# çalışıyor
def personel_goruntuleme(personel_dict):
    for p_id, p_info in personel_dict.items():
        print("\nPerson ID:", p_id)

        for key in p_info:
            print(key + ':', p_info[key])
    menuden_cikis()
# çalışıyor
def dosyaya_yaz(personel_dict):
    print("Dosyayaa yazma fonk")
    f = open("deneme.txt", "w")
    for k, v in personel_dict.items():
        s = str(k) + "   " + str(v) + "\n"
        b = f.write(s)

    f.close()
    menuden_cikis()

# calısıyor
def personel_arama(personel_dict):
    print("Personel arama gelecek fonk")
    print("Aramak istediğiniz id seicn gereken bilgiler")

    id = int(input("id degeri giriniz:"))
    if (id in personel_dict):
        print("aranılan id değeri personel sözlüğümüzde bulunmaktadır")
        print("Aramak istediğiniz value seicn gereken bilgiler")

        arama_secim = int(input("Personel Adı icin 1\n"
                                "Personel Yaşı icin 2\n"
                                "Personel Departman icin 3\n"
                                "Personel Adres icin 4\n"
                                "Personel Telefon icin 5\n"
                                "Personel Maaşı icin 6\n"
                                "Personel bildiği diller icin 7 secimi yapınız:"))

        if(arama_secim == 1):
            isim = str(input("aradığınız isim degerini giriniz:"))
            if (isim in personel_dict[id]['Personel Adı']):
                print("aranılan isim degeri bulunmaktadır")
            elif (isim not in personel_dict[id]['Personel Adı']):
                print("aranılan value degeri bulunmamaktadır")
        elif(arama_secim == 2):
            yas = int(input("aradığınız yas degerini giriniz:"))
            if (yas in personel_dict[id]['Personel Yaşı']):
                print("aranılan isim degeri bulunmaktadır")
            elif (yas not in personel_dict[id]['Personel Yaşı']):
                print("aranılan isim degeri bulunmamaktadır")
        elif (arama_secim == 3):
            departman = str(input("aradığınız departman degerini giriniz:"))
            if (departman in personel_dict[id]['Personel Departman']):
                print("aranılan departman degeri bulunmaktadır")
            elif (departman not in personel_dict[id]['Personel Departman']):
                print("aranılan departman degeri bulunmamaktadır")
        elif (arama_secim == 4):
            adres = str(input("aradığınız adres degerini giriniz:"))
            if (adres in personel_dict[id]['Personel Adres']):
                print("aranılan adres degeri bulunmaktadır")
            elif (adres not in personel_dict[id]['Personel Adres']):
                print("aranılan adres degeri bulunmamaktadır")
        elif (arama_secim == 5):
            telefon = int(input("aradığınız telefon degerini giriniz:"))
            if (telefon in personel_dict[id]['Personel Telefon']):
                print("aranılan telefon degeri bulunmaktadır")
            elif (telefon not in personel_dict[id]['Personel Telefon']):
                print("aranılan telefon degeri bulunmamaktadır")
        elif (arama_secim == 6):
            maas = int(input("aradığınız maas degerini giriniz:"))
            if (maas in personel_dict[id]['Personel Maaşı']):
                print("aranılan maaş degeri bulunmaktadır")
            elif (maas not in personel_dict[id]['Personel Maaşı']):
                print("aranılan maaş degeri bulunmamaktadır")
        elif (arama_secim == 7):
            dil = str(input("aradığınız maas degerini giriniz:"))
            if (dil in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
                print("aranılan dil degeri bulunmaktadır")
            elif (dil not in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
                print("aranılan dil degeri bulunmamaktadır")
        return True
    else:
        print("aranılan id değeri personel sözlüğümüzde bulunmamakktadır")
        return False


# calısıyor
def personel_silme(personel_dict):
    # sözlükteki tüm degerler
    for item in personel_dict:
        print("Key : {} , Value : {}".format(item, personel_dict[item]))

    print("Personel silme gelecek olan fonk")
    print("Silmek istediğiniz id seicn gereken bilgiler")

    id = int(input("id degeri giriniz:"))
    del personel_dict[id]
    print("yeni liste")
    for item in personel_dict:
        print("Key : {} , Value : {}".format(item, personel_dict[item]))
    menuden_cikis()


# çalışıyr
def personel_maas_hesaplama(personel_dict):
    print("Personel Maaş hesaplama gelecek fonk")
    ocak = mart = mayıs = temmuz = agustos = ekim = aralık = 31
    nisan = haziran = eylül = kasım = 30
    şubat = 28
    id = int(input("Maasini hesaplamak istediginiz personelin idsinni giriniz:"))
    personel_gunluk_ucret = 150

    izin_alınan_gün_sayisi = int(input("izin alınan gün sayısını giriniz"))
    maas_kesinti = personel_gunluk_ucret * izin_alınan_gün_sayisi
    dönem = str(
        input("hangi aya ait maasi hesaplamak istersiniz?(Lütfen ay adını tamamı kücük harf olacak sekilde giriniz)"))
    ay = eval(dönem)

    maas_hesabı = (ay * personel_gunluk_ucret) - maas_kesinti
    print(maas_hesabı)
    personel_dict[id]['Personel Maaşı'].update(maas_hesabı)
    for item in personel_dict:
        print("Key : {} , Value : {}".format(item, personel_dict[item]))
    menuden_cikis()

# çalışıyor
def menuden_cikis():
    tekrar = str(input("\nMenüye geri dönmek isterseniz e,cıkmak icin h ye basın: \n"))
    if (tekrar.lower() == 'e'):
        main()
    else:
        print("\nGoodbye...........")
        exit()


# main_function(personel_dict)
def main():
    title()
    menu()
    secim = getChoice()
    while True:
        if (secim < 10 and secim > 0):
            if (secim == 1):
                personel_ekleme(personel_dict)
            elif (secim == 2):
                personel_guncelleme(personel_dict)
            elif (secim == 3):
                personel_arama(personel_dict)
            elif (secim == 4):
                personel_silme(personel_dict)
            elif (secim == 5):
                personel_maas_hesaplama(personel_dict)
            elif (secim == 6):
                personel_goruntuleme(personel_dict)
            elif (secim == 7):
                dosyaya_yaz(personel_dict)
            elif (secim == 8):
                menuden_cikis()
        else:
            print("Doğru seçim yapınız")


if __name__ == '__main__':
    main()
