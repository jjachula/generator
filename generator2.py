imie = input("imię: ")
nazwisko = input ("nazwisko: ")
domena = input("domena: ")

bp = domena.find("http://")
if bp<0:
    domena = domena
else:
    domena = domena.replace("http://", "")

bp1 = domena.find("https://")
if bp1<0:
    domena = domena
else:
    domena = domena.replace("https://", "")

bp2 = domena.find("www.")
if bp2<0:
    domena = domena
else:
    domena = domena.replace("www.", "")

ukosnik = domena.find("/")
if ukosnik<0:
    domena = domena
else:
    domena = domena[0:ukosnik]


def generator (imie, nazwisko, domena):

        def male_litery():
            nonlocal imie, nazwisko
            imie = imie.lower()
            nazwisko = nazwisko.lower()
            return imie, nazwisko
        male_litery()

        def pl_znaki():
            nonlocal imie, nazwisko
            pl = "ŻÓŁĆĘŚĄŹŃżółćęśąźń"
            bezpl = "ZOLCESAZNzolcesazn"
            trantab = str.maketrans(pl, bezpl)
            imie = imie.translate(trantab)
            nazwisko = nazwisko.translate(trantab)
            return imie, nazwisko
        pl_znaki()

        def zdrobnienia():
            nonlocal imie
            full_name = "joanna"
            if imie == full_name:
                zd = "asia"
            else:
                zd = imie
            return zd
        zdrobnienie = zdrobnienia()

        #dict = {'Joanna': 'Asia'}
        #print(dict.keys())


        formatka1 = imie + "." + nazwisko + "@" + domena                 #joanna.jachula@righthello.com
        formatka2 = imie + "@" + domena                                  #joanna@righthello.com
        formatka3 = nazwisko + "@" + domena                              #jachula@righthello.com
        formatka4 = imie[0] + "." + nazwisko + "@" + domena              #j.jachula@righthello.com
        formatka5 = imie[0] + nazwisko + "@" + domena                    #jjachula@righthello.com
        formatka6 = imie[0:2] + nazwisko[0] + "@" + domena               #joj@righthello.com
        formatka7 = imie[0] + nazwisko[0:2] + "@" + domena               #jja@righthello.com
        formatka8 = imie + nazwisko + "@" + domena                       #joannajachula@righthello.com
        formatka9 = nazwisko + "." + imie + "@" + domena                 #jachula.joanna@righthello.com
        formatka10 = imie[0] + nazwisko[0] + "@" + domena                #jj@righthello.com
        formatka11 = imie[0] + "@" + domena                              #j@righthello.com
        formatka12 = imie + "_" + nazwisko + "@" + domena                #joan_jachula@righthello.com
        formatka13 = zdrobnienie + "." + nazwisko + "@" + domena         #asia.jachula@righthello.com

        return formatka1, formatka2, formatka3, formatka4, formatka5, formatka6, formatka7, formatka8, formatka9, formatka10, formatka11, formatka12, formatka13

formatki = generator(imie, nazwisko, domena)

for index, formatka in enumerate(formatki, start=1):
    print(index, formatka)

input()