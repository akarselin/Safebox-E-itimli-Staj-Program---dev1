class FilmKaydetme:
    def kaydet(self, film):
        with open('filmler.txt', 'a') as dosya:
            dosya.write(film + '\n')
        print("Film kaydedildi!")

class FilmArama:
    def ara(self, film):
        with open('filmler.txt', 'r') as dosya:
            filmler = dosya.readlines()
            filmler = [film.strip() for film in filmler]
            if film in filmler:
                print("Film mevcut.")
            else:
                print("Film bulunamadı.")

class FilmIslemleri:
    def baslat(self):
        kaydetme = FilmKaydetme()
        arama = FilmArama()

        while True:
            print("1. Film kaydetme")
            print("2. Film arama")
            print("3. Çıkış")
            secim = int(input("Seçiminizi yapın (1-3): "))

            if secim == 1:
                film = input("Kaydedilecek filmi girin: ")
                kaydetme.kaydet(film)
            elif secim == 2:
                film = input("Aranacak filmi girin: ")
                arama.ara(film)
            elif secim == 3:
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz bir seçim yaptınız. Tekrar deneyin.")

film_islemleri = FilmIslemleri()
film_islemleri.baslat()
