print("Program generujący życzenia urodzinowy.")

obecny_rok = 2024

imie_odbiorcy = input("Proszę podać imię odbiorcy: ")
rok_urodzenia_odbiorcy = int(input("Proszę podać rok urodzenia odbiorcy: "))
spersonalizowana_wiadomość = input("Napisz własną wiadomość dla odbiorcy: ")
imie_nadawcy = input("Proszę podać imię nadawcy: ")
wiek_odbiorcy = obecny_rok - rok_urodzenia_odbiorcy


szablon_zyczen = (f"\n{imie_odbiorcy}, wszystkiego najlepszego z okazji "
                  f"{wiek_odbiorcy} urodzin! \n\n{spersonalizowana_wiadomość}"
                  f"\n\n{imie_nadawcy}")

print(szablon_zyczen)