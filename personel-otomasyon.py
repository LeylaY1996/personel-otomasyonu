def baslik():
    print("############################################")
    print("#     PERSONEL OTOMASYON SİSTEMİ           #")
    print("############################################")

def secimYap():
    return int(input("Menüden seciminizi yapınız:(1 ve 8 arasında secim yapınız.1 ve 8 dahil) \nSeciminiz:"))

def menu():
    print("\n\n***************MENU*******************")
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
# çalışıyor
def personel_goruntuleme(personel_dict):
    for p_id, p_info in personel_dict.items():
        print("\nPerson No:", p_id)

        for key in p_info:
            print(key + ':', p_info[key])
    menuden_cikis()

def personel_ekleme(personel_dict):
    print("Yeni Personel Eklemek için doldurmanız gereken bilgiler:")
    id = int(input("Personel No'sunu giriniz:"))

    if (id in personel_dict):
        print("Girdiğiniz Personel No'su bulunmaktadır!Başka bir Personel No'su giriniz..")
        personel_ekleme(personel_dict)
    else:
        personel_dict[id] = {}
        personel_dict[id]['Personel Adı'] = str(input("Personelin Adını Soyadını giriniz:"))
        personel_dict[id]['Personel Yaşı'] = int(input("Yaşını giriniz:"))
        personel_dict[id]['Personel Departman'] = str(input("Departmanı giriniz:"))
        personel_dict[id]['Personel Adres'] = str(input("Adresini giriniz:"))
        personel_dict[id]['Personel Telefon'] = str(input("Telefon Numarasını giriniz:"))
        personel_dict[id]['Personel Maaşı'] = int(input("Maaşını giriniz:"))
        personel_dict[id]['Personelin Bildiği Programlama Dilleri'] = str(input("Bildiği Programlama dillerini giriniz:"))

        # personel yeni eklenen deger
        print("Yeni Eklenen Personel Bilgileri:")
        print(personel_dict[id])
    # sözlükteki tüm degerler
    print("Tüm Personeller\n")
    for item in personel_dict:
        print("Personel No'su : {} , Bilgileri : {}".format(item, personel_dict[item]))
    menuden_cikis()



# çalışmıyor
def personel_guncelleme(personel_dict):
    # sözlükteki tüm degerler
    print("Tüm Personeller\n")
    for item in personel_dict:
        print("Personel No'su : {} , Bilgileri : {}".format(item, personel_dict[item]))

    print("\n\n")
    id = int(input("Güncellenecek Personel No'sunu giriniz:"))

    if (id in personel_dict):
        guncelleme_secim = int(input("Personel Adını Güncellemek için 1,\n"
              "Personel Yaşını Güncellemek için 2,\n"
              "Personel Departmanı Güncellemek için 3,\n"
              "Personel Adresini Güncellemek için 4,\n"
              "Personel Telefon Numarasını Güncellemek için 5,\n"
              "Personel Maaşını Güncellemek için 6,\n"
              "Personel Bildiği Dilleri Güncellemek için 7 seçimini yapınız:"))

        if(guncelleme_secim == 1):
            ad = input("Güncellenecek Personelin Adını ve Soyadını giriniz:")
            personel_dict[id]["Personel Adı"].update(ad)
        elif(guncelleme_secim == 2):
            yas = input("Güncellenecek Personelin Yaşını giriniz:")
            personel_dict[id]['Personel Yaşı'].update(yas)
        elif (guncelleme_secim == 3):
            departman = str(input("Güncellenecek Personelin Departmanını giriniz:"))
            personel_dict[id]["Personel Departman"].update(departman)
        elif (guncelleme_secim == 4):
            adres = str(input("Güncellenecek Personelin Adresini giriniz:"))
            personel_dict[id]["Personel Adres"].update(adres)
        elif (guncelleme_secim == 5):
            telefon = int(input("Güncellenecek Personelin Telefon giriniz:"))
            personel_dict[id]["Personel Adres"].update(telefon)
        elif (guncelleme_secim == 6):
            maas = int(input("Güncellenecek Personelin Maaşını giriniz:"))
            personel_dict[id]["Personel Adres"].update(maas)
        elif (guncelleme_secim == 7):
            dil = str(input("Güncellenecek Personelin Bildiği dilleri giriniz:"))
            personel_dict[id]["Personel Adres"].update(dil)


            # sözlükteki tüm degerler
            for item in personel_dict:
                print("Personel No'su : {} , Bilgileri : {}".format(item, personel_dict[item]))

    else:
        print("Aranılan personelin no'su personel sözlüğümüzde bulunmamaktadır!\n\n")
        return False



# çalışıyor
def dosyaya_yaz(personel_dict):
    f = open("deneme.txt", "w")
    for k, v in personel_dict.items():
        s = str(k) + "   " + str(v) + "\n"
        b = f.write(s)

    f.close()
    menuden_cikis()

# calısıyor
def personel_arama(personel_dict):
    print("Aramak istediğiniz Personel No'sunu giriniz..")

    id = int(input("Personel No'sunu giriniz:"))
    if (id in personel_dict):
        print("Aranılan Personel No'su personel sözlüğümüzde bulunmaktadır.\n")

        arama_secim = int(input("Personel Ad Soyadını aramak için 1,\n"
                                "Personel Yaşını aramak için 2,\n"
                                "Personel Departmanı aramak için 3\n"
                                "Personel Adresini Aramak için 4\n"
                                "Personel Telefonu Aramak için 5\n"
                                "Personel Maaşını Aramak için 6\n"
                                "Personel bildiği diller icin 7 secimi yapınız:"))

        if(arama_secim == 1):
            isim = str(input("Aradığınız Personel Ad Soyad giriniz:"))
            if (isim in personel_dict[id]['Personel Adı']):
                print("Aranılan Personel Ad Soyad bulunmaktadır")
            else:
                if(isim not in personel_dict[id]['Personel Adı']):
                    print("Aranılan Personel Ad Soyad bulunmamaktadır")

        elif(arama_secim == 2):
            yas = int(input("Aradığınız Personelin Yaşını giriniz:"))
            if (yas in personel_dict[id]['Personel Yaşı']):
                print("Aradığınız Personelin Yaşı bulunmaktadır")
            else:
                if (yas not in personel_dict[id]['Personel Yaşı']):
                    print("Aradığınız Personelin Yaşı bulunmamaktadır")

        elif (arama_secim == 3):
            departman = str(input("Aradığınız Personelin departmanını giriniz:"))
            if (departman in personel_dict[id]['Personel Departman']):
                print("Aradığınız Personelin departmanı bulunmaktadır")
            else:
                if (departman not in personel_dict[id]['Personel Departman']):
                    print("Aradığınız Personelin departmanı bulunmamaktadır")
        elif (arama_secim == 4):
            adres = str(input("Aradığınız Personelin adresini giriniz:"))
            if (adres in personel_dict[id]['Personel Adres']):
                print("Aradığınız Personelin adresi bulunmaktadır.")
            else:
                if(adres not in personel_dict[id]['Personel Adres']):
                    print("Aradığınız Personelin adresi bulunmamaktadır.")

        elif (arama_secim == 5):
            telefon = int(input("Aradığınız Personelin Telefon Numarasını giriniz:"))
            if (telefon in personel_dict[id]['Personel Telefon']):
                print("Aradığınız Personelin Telefon Numarası bulunmaktadır.")
            else:
                if(telefon not in personel_dict[id]['Personel Telefon']):
                 print("Aradığınız Personelin Telefon Numarası bulunmamaktadır.")
            menuden_cikis()

        elif (arama_secim == 6):
            maas = int(input("Aradığınız Personelin Maaşını giriniz:"))
            if (maas in personel_dict[id]['Personel Maaşı']):
                print("Aradığınız Personelin Maaşı bulunmaktadır")
            else:
                if(maas not in personel_dict[id]['Personel Maaşı']):
                 print("Aradığınız Personelin Maaşı bulunmamaktadır")

        elif (arama_secim == 7):
            dil = str(input("Aradığınız Personelin Bildiği programlama dillerini giriniz:"))
            if (dil in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
                print("Aradığınız Personelin Bildiği programlama dilleri bulunmaktadır")
            else:
                if(dil not in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
                    print("Aradığınız Personelin Bildiği programlama dilleri bulunmamaktadır")
            menuden_cikis()

    else:
        print("Aranılan Personel No'su sözlüğümüzde bulunmamaktadır!")
        return False


# calısıyor
def personel_silme(personel_dict):
    # sözlükteki tüm degerler
    for item in personel_dict:
        print("Personel No'su : {} , Bilgileri : {}".format(item, personel_dict[item]))

    id = int(input("Silmek istediğiniz Personel No'sunu giriniz:"))
    del personel_dict[id]
    print("Yeni liste")
    for item in personel_dict:
        print("Personel No'su : {} , Bilgileri : {}".format(item, personel_dict[item]))
    menuden_cikis()


# çalışıyr
def personel_maas_hesaplama(personel_dict):
    ocak = mart = mayıs = temmuz = agustos = ekim = aralık = 31
    nisan = haziran = eylül = kasım = 30
    şubat = 28
    id = int(input("Maaşını hesaplamak istediginiz Personelin No'sunu giriniz:"))
    personel_gunluk_ucret = 150

    izin_alınan_gün_sayisi = int(input("İzin alınan gün sayısını giriniz"))
    maas_kesinti = personel_gunluk_ucret * izin_alınan_gün_sayisi
    dönem = str(
        input("Hangi aya ait maaşı hesaplamak istersiniz?(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)"))
    ay = eval(dönem)

    maas_hesabı = (ay * personel_gunluk_ucret) - maas_kesinti
    print(maas_hesabı)
    personel_dict[id]['Personel Maaşı'].update(maas_hesabı)
    for item in personel_dict:
        print("Personel No'su : {} , Bilgileri : {}".format(item, personel_dict[item]))
    menuden_cikis()

# çalışıyor
def menuden_cikis():
    tekrar = str(input("\nMenüye geri dönmek isterseniz e,cıkmak icin h ye basın: \n"))
    if (tekrar.lower() == 'e'):
        main()
    else:
        print("\nGoodbye...........")
        exit()


def main():
    baslik()
    menu()
    secim = secimYap()
    while True:
        if (secim < 9 and secim > 0):
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
