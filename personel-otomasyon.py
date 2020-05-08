def title():
    print("######################################################################################")
    print("# PERSONEL OTOMASYON SİSTEMİ                                                         #")
    print("######################################################################################")

def getChoice():
    return int(input("Menüden seciminizi yapınız:(1 ve 8 arasında secim yapınız.1 ve 8 dahil) \nNumara buraya yazinz:"))

def menu():
    print("\n\n*****************MENU*********************")
    print("*1.Personel Dosyaya Yaz                  *")
    print("*2.Personel Ekleme                       *")
    print("*3.Personel Güncelleme                   *")
    print("*4.Personel Arama                        *")
    print("*5.Personel Silme                        *")
    print("*6.Personel Maaş Hesaplama               *")
    print("*7.Menüden Çıkış veya Menüye geri dönüş  *")
    print("*8.Personel GÖrüntüleme                  *")
    print("*9.Exit                                  *")
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
        print("\nPerson ID:", p_id)

        for key in p_info:
            print(key + ':', p_info[key])


# çalışıyor
def dosyaya_yaz(personel_dict):
    print("Dosyayaa yazma fonk")
    f = open("deneme.txt", "w")
    for k, v in personel_dict.items():
        s = str(k) + "   " + str(v) + "\n"
        b = f.write(s)

    f.close()


# calısıyor
def personel_ekleme(personel_dict):
    print("Yeni Personel Eklemek için:")
    print("Doldurmanız gereken bilgiler")
    id = int(input("id degeri giriniz:"))
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
        print("Key : {} , Value : {}".format(item, personel_dict[item]))


# çalışmıyor
def personel_guncelleme(personel_dict):
    print("Personel Güncelleme gelecek olan fonk")
    # sözlükteki tüm degerler
    for item in personel_dict:
        print("Key : {} , Value : {}".format(item, personel_dict[item]))

    print("Personel arama gelecek fonk")
    print("Güncellemek istediğiniz id seicn gereken bilgiler")

    id = int(input("id degeri giriniz:"))
    if (id in personel_dict):
        print("Güncellenecek id değeri personel sözlüğümüzde bulunmaktadır")
        print("Güncellemek istediğiniz value seicn gereken bilgiler")

        value = str(input("value degeri giriniz:"))
        if (value in personel_dict[id]['Personel Adı']):
            personel_dict.update[id]['Personel Adı'] = "deneme"
            print("yeni personel adı:", personel_dict.update[id]['Personel Adı'])
        elif (value not in personel_dict[id]['Personel Adı']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Yaşı']):
            print("aranılan value degeri bulunmaktadır")
        elif (int(value) not in personel_dict[id]['Personel Yaşı']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Departman']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Departman']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Telefon']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Telefon']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Maaşı']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Maaşı']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
            print("aranılan value degeri bulunmamaktadır")
        return True
    else:
        print("aranılan id değeri personel sözlüğümüzde bulunmamakktadır")
        return False


# calısıyor
def personel_arama(personel_dict):
    print("Personel arama gelecek fonk")
    print("Aramak istediğiniz id seicn gereken bilgiler")

    id = int(input("id degeri giriniz:"))
    if (id in personel_dict):
        print("aranılan id değeri personel sözlüğümüzde bulunmaktadır")
        print("Aramak istediğiniz value seicn gereken bilgiler")

        value = str(input("value degeri giriniz:"))
        if (value in personel_dict[id]['Personel Adı']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Adı']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Yaşı']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Yaşı']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Departman']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Departman']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Telefon']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Telefon']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personel Maaşı']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personel Maaşı']):
            print("aranılan value degeri bulunmamaktadır")
        if (value in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
            print("aranılan value degeri bulunmaktadır")
        elif (value not in personel_dict[id]['Personelin Bildiği Programlama Dilleri']):
            print("aranılan value degeri bulunmamaktadır")
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


# çalışıyor
def menuden_cikis():
    tekrar = str(input("\nMenüye geri dönmek isterseniz e,cıkmak icin h ye basın: \n"))
    if (tekrar.lower() == 'e'):
        main()
    else:
        print("\nGoodbye...........")
        exit()

def main_function(personel_dict):
    personel_goruntuleme(personel_dict)
    secim = int(input("Menüden seciminizi yapınız:(1 ve 8 arasında secim yapınız.1 ve 8 dahil)"))
    if (secim < 9 and secim > 0):
        if (secim == 1):
            dosyaya_yaz(personel_dict)
        elif (secim == 2):
            personel_ekleme(personel_dict)
        elif (secim == 3):
            personel_guncelleme(personel_dict)
        elif (secim == 4):
            personel_arama(personel_dict)
        elif (secim == 5):
            personel_silme(personel_dict)
        elif (secim == 6):
            personel_maas_hesaplama(personel_dict)
        elif (secim == 7):
            menuden_cikis()
        elif (secim == 8):
            personel_goruntuleme(personel_dict)

    else:
        print("Doğru seçim yapınız")


# main_function(personel_dict)
def main():
    title()
    menu()
    secim = getChoice()
    while True:
        if (secim < 10 and secim > 0):
            if (secim == 1):
                dosyaya_yaz(personel_dict)
            elif (secim == 2):
                personel_ekleme(personel_dict)
            elif (secim == 3):
                personel_guncelleme(personel_dict)
            elif (secim == 4):
                personel_arama(personel_dict)
            elif (secim == 5):
                personel_silme(personel_dict)
            elif (secim == 6):
                personel_maas_hesaplama(personel_dict)
            elif (secim == 7):
                menuden_cikis()
            elif (secim == 8):
                personel_goruntuleme(personel_dict)
            elif (secim == 9):
                exit()
            menuden_cikis()
        else:
            print("Doğru seçim yapınız")


if __name__ == '__main__':
    main()
