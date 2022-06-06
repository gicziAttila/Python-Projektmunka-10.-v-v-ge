﻿import time  # Importáljuk az időt ezzel tudunk késleltetni

#Rájönni hogyan válaszolhat a felhasználó a különböző esetekben
valasz_A = ["A", "a"]
valasz_B = ["B", "b"]
valasz_C = ["C", "c"]
valasz_D = ["D", "d"]
valasz_E = ["E", "e"]



#A felhasználó csak a megadott választásokkal válaszolhasson
szukseges = ("\nCsak a megadott betűkombinációkat használd!\n")
szukseges2 = ("\n A következő kérdésnél saját választ kell megadnod! Minden választ nagy betűvel kezdj hogy elfogadja a játék!")
#Bemutatkozás
def intro():
 print("Üdv!")
 time.sleep(0.5)
 print("Örülök, hogy újra itt vagy! A legutóbbi kis találkánk után kételkedtem benne, hogy viszont látjuk egymást, de ezek szerint nem igaz, hogy „a villám nem csap kétszer ugyanoda”.")
 time.sleep(2)
 print("""Ismét hoztam egy játékot. Alapjaiban hasonlít az előző kalandunkhoz, de a játékszabályok 
kicsit megváltoztak. Használnod kell a józan ítélőképességed és sokszor kell a tudásodra támaszkodnod, nem mindig fogok választási lehetőségeket adni.
Sok esetben érdemes észben tartani a következőt: nincs jó, vagy rossz választási lehetőség. Döntés van, és az azzal járó következmények.""")
 time.sleep(5)
 print("A változatosság, na meg a móka kedvéért forgatókönyvi stílusban fogom tálalni a dolgokat.")
 time.sleep(1)
 print("Ne is ragozzuk tovább a dolgokat, kezdjük el!")
 time.sleep(5)
 print("""Külső – Városi vasút – NAPPAL
Kívülről láthatunk egy személyvonatot. Az utasok nyugodtan zötykölődnek a lepukkant vasparipa falai között. Látszólag szokványos járatnak tűnik.""")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Látszólag szokványos járat is. Azonban – hogy adjak némi motivációt a játékhoz- elrejtettem egy kis meglepetést a vonaton, ami lehet, hogy megnehezíti néhány ember utazását, vagy életben maradását.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("De cseppet se aggódj! Könnyedén megmentheted őket. Viszonylag könnyedén. Adok neked néhány feladványt, neked pedig jó választ kell adnod! Érthető? Remélem.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Egyébként a nevem mellett a v.o. (voice over) narrációt jelent egy forgatókönyvben. Ezt még le akartam tisztázni.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Kezdhetjük?")
 print ("""A. Igen
B. Nem """)
#1. választási lehetősége a játékosnak
 choice = input(">>> ")
 if choice in valasz_A:
     valasztas_kezdes()
 elif choice in valasz_B:
    print("\n  Biztos vagyok benne, hogy érdekelni fog téged. Veszíteni valód nincsen, nem igaz? Na ugye! Szerintem el is kezdhetjük! Showtime!")
    time.sleep(5)
    valasztas_kezdes()
 else:
    print (szukseges)
def valasztas_kezdes():
 print("Narrátor (V.O.)")
 print ("A történet elkezdéséhez mindenképpen szükséged lesz egy karakterre.")
 time.sleep(2)
 print("A gördülő személyvonat képe megáll, mintha egy videót állítottunk volna meg, majd egyszeriben ellepi a köd. Szürke ködfelhők tömkelege borítja be a képet.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Ha már úgy is feladványokat kell kitalálnod, legyél detektív, vagy nyomozó, ahogy tetszik. ")
 time.sleep(5)
 print("""A ködből felemelkedik egy alak, akinek csak a sziluettjét látjuk. Magas, izmos, és olybá tűnik, palásttal fedné testét. Fején két apró szarv virít, a köpeny alját és a lábát a ködfelhő eltakarja. A lényt körülvevő füstöt mintha egy robbanás idézte volna elő.
Az alak lassan közelít a kamera felé.""")
 time.sleep(5)
 print("NARRÁTOR(V.O.)")
 print("De nem olyan jelmezes igazságosztó féle, hanem egy kicsit hagyományosabb.")
 time.sleep(5)
 print("Az előző árny köddé válik, helyébe egy valamivel alacsonyabb ember lép, akinek szintjén csak körvonalait látjuk. Ballonkabátot hord, jobb kezében cigaretta ég, baljában jól kivehetően keresztet markol. Az őt körülölelő füst azonban sokkal inkább dohányfüstre vall.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Mint Poirot, vagy mittomén.")
 time.sleep(3)
 print("A második alak is eltűnik, a ködből David Suchet lép elő, pipázva.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("De ez most nem lényeg. Szóval nyomozgatsz. Éppen te is a vonton utazol, amikor egyszer csak…")
 time.sleep(3)
 print("A hangosbemondóba egy férfihang szólal meg.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Kedves utasaink! Remélem élvezik az utazást! Amennyiben igen, örömmel tájékoztatom önöket, hogy az egyes vagonok aljára robbanószert rögzítettem, és ha nem válaszolnak jól a feladványaimra, a levegőbe röpítem az egész kócerájt! ")
 time.sleep(5)
 print("PÁNIK fogja el az utasokat. Érthető módon.")
 time.sleep(2)
 print("Narrátor (V.O.)")
 #2. választási lehetőség a játékosnak
 print(szukseges2)
 print("Lássuk is az elsőt: hatvan gyermekem van, minden gyermekemtől hatvan unokám. Mi vagyok?")
 choice = input(">>> ")
 if choice == "Óra" or choice == "Egy óra":
     jo_valasz_1()
 elif choice != "Óra" or choice != "Egy óra":
     rossz_valasz_1()
def rossz_valasz_1(): 
 print("Narrátor (V.O.)")
 print("Ez sajnos nem talált. De mivel még jó kedvembe vagyok, adok egy második esélyt.")
 time.sleep(3)
 print("Az ajtó előtt álló utasok egyike hirtelen MEGSZÓLAL.")
 time.sleep(3)
 print("Random idős bácsi")
 print("Ha hatvan gyermeknek van hatvan gyermeke, az azt jelentheti, hogy van egy egész, ami hatvan egységre van tagolva, és egy ilyen egységen belül is van hatvan kisegység.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Jó fele kapizsgál az úr. Akkor még egyszer: hatvan gyermekem van, minden gyermekemtől hatvan unokám. Mi vagyok?")
 time.sleep(5)
 #3. választási lehetőség
 print("""A; 6 óra
       B; 1 óra
       C; 6 perc
       D; 1 perc""")
 choice = input(">>> ")
 if choice in valasz_B:
     jo_valasz_1()
 elif choice in valasz_A or choice in valasz_C or choice in valasz_D:
     halal()
def jo_valasz_1():
 print("Narrátor (V.O.)")
 print("Talált, süllyedt. Az első feladványom kitalálták. Jöjjön a következő.")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print(szukseges2)
 print("""Rőzsén élek,
Földön hálok,
Szárnyra kélek
Égen szállok,
Lepkét vonzok,
S álmot űzök. 
Mi vagyok?""")
 time.sleep(10)
#4. választási lehetőség a játékosnak
 choice = input(">>> ")
 if choice == "Tűz":
     jo_valasz_2()
 elif choice != "Tűz":
     rossz_valasz_2()
def rossz_valasz_2():
 print("""FŐSZEREPLŐ/DETEKTÍV
(magában motyogva)""")
 time.sleep(2)
 print("Nem, nem, talán mégsem ez a helyes válasz. Ha rőzsén, vagyis faágon él, földön alszik, vonzza a lepkét, ami szereti a fényt, akkor valami fényhatás lesz, aminek a keletkezéséhez fa kell, és ami olyan nagy is tud lenni, hogy messziről látni.")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Na, kapok még ma választ? Ne már, ez azért annyira nem nehéz! „Rőzsén élek”, „égre szállok”, „lepkét vonzok”,… csak rá lehet jönni!")
 time.sleep(5)
 print(szukseges2)
 print("""Rőzsén élek,
Földön hálok,
Szárnyra kélek
Égen szállok,
Lepkét vonzok,
S álmot űzök. 
Mi vagyok?""")
 time.sleep(10)
#5. választási lehetőség a játékosnak
 choice = input(">>> ")
 if choice == "Tűz":
     jo_valasz_2()
 elif choice != "Tűz":
     halal()
def jo_valasz_2():
 print("Narrátor (V.O.)")
 print("Ez igen, nyomozó! Tuti okosabb, mint egy másodikos. Tudtam én, hogy akad majd játszótársam! ")
 time.sleep(5)
 print("Narrátor (V.O.)")
 print("Teszteljük le, mennyire vág jól az esze! Lépjen előre, katona!")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Innentől a játék privát! A nyomozó átmegy a másik vagonba, a többiek lekopnak. Ha valaki ellenkezik, annak súlyos ára lesz!")
 time.sleep(5)
 print("A tömeg aggodalmasan FIGYELI, ahogy a nyomozó ÁTLÉP a másik szerelvénybe. ")
 time.sleep(4)
 print("Amint a főhős BELÉP az ajtón, az BEZÁRUL mögötte, majd egy hangos KATTANÁS jelzi, hogy innen már nincs visszaút.")
 time.sleep(4)
 print("Magát a vasúti kocsit teljes sötétség borítja, nem látni semmit, ráadásul a vonat ZÖTYKÖLŐDÉSE az egyetlen hangforrás. ")
 time.sleep(5)
 print("Kis szünet után a NARRÁTOR hangja töri meg a csendet. ")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Üdvözlöm az „atyában”, detektív! ")
 time.sleep(3)
 print("A vagonban felgyúl négy vörösen fénylő lámpa. Most már tisztán látszik a vagon közepén elhelyezkedő éttermi asztal, két oldalán két székkel.")
 time.sleep(3)
 print("Narrátor (V.O.)")
 print("Foglaljon helyet!")
 #6. választási lehetőség a játékosnak
 print(""" A. Helyet foglal
B. Nem foglal helyet""")
 choice = input(">>> ")
 if choice in valasz_A:
   jo_valasz_3()
 elif choice in valasz_B:
    rossz_valasz_3()
 else:
    print(szukseges)
def rossz_valasz_3():
 print("FŐSZEREPLŐ/DETEKTÍV")
 print("Nem fog belecsalni még egy feladványba, nem fog nekem feltenni további rébuszokat! Engedje leszállni az utasokat és vessen véget ennek a beteg játéknak!")
 time.sleep(4) 
 print("Az asztal közepén KÖDFELHŐ jelenik meg, ami lassan körbe-körbe KAVAROG, mint egy tornádó. ")  
 time.sleep(2)
 print("NARRÁTOR")
 print("Úgy érzem, szerepet tévesztett. Nem maga szabja a cselekményt, mert nem maga a mesélő. A maga szerepe pusztán befolyásolni az események menetét.")
 time.sleep(4)
 print("A ködfelhő egyre vészjóslóbban, egyre veszélyesebben KAVAROG")
 time.sleep(2)
 print("NARRÁTOR")
 print("Megkérem még egyszer, utoljára. Foglaljon. Helyet.")
 time.sleep(3)
 print("FŐSZEREPLŐ/DETEKTÍV")
 print("Nincs az az Isten!")
 time.sleep(2)
 print("A köd hirtelen sebességgel ELNYELI az asztalt, székestül, majd ismét MEGÁLL, és lassan FOROG KÖRBE.")
 time.sleep(4)
 print("A narrátor hangja a következőkben már nem a hangszórókból jön.")
 time.sleep(2)
 print("NARRÁTOR(V.O.)")
 print("Akkor hát… Ég önnel, detektív!")
 time.sleep(6)
 print("A DETEKTÍV SZEMSZÖGÉBŐL")
 print("A köd egy szemvillanás alatt ellepi a kamerát, ezzel együtt a DETEKTÍVET is.")
 time.sleep(5)
 print("VÉGE.")
 
 halal()
def jo_valasz_3():
    
 print("A NYOMOZÓ odasétál az asztalhoz, aminek a közepén egy GYERTYA ég, világítás gyanánt. KIHÚZZA a széket, majd leül.")
 time.sleep(3)
 print("Vele szemben, az asztal másik oldalán egy üres szék foglal helyet.")
 time.sleep(2)
 print(" NARRÁTOR ")
 print("Van-e ötlete, miért hívom ezt a szerelvényt „atyának”?")

 print("""A.Van.
B. Nincs""")
 choice = input(">>> ")
 if choice in valasz_A:
     choice = input(">>> ")
     if choice == "Apa" or choice == "Édesapa" or choice =="Isten" or choice == "isten":
      jo_valasz_4()
 elif choice in valasz_B or choice != "Apa" and choice != "Édesapa" and choice !="Isten" and choice != "isten":
      rossz_valasz_4()
 #kérdéses
def rossz_valasz_4():
    print("NARRÁTOR")
    print("Ejnye. Valami jó, vagy jobb tippje csak van!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Az atya a köztudatban, mint Isten szinonimája van jelen.")
    time.sleep(3)
    print("NARRÁTOR")
    print("Kiváló meglátás, közel jár, közel jár!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Emellett az atya régiesebb stílusban az édesapát is jelenti.")
    time.sleep(2)
    jo_valasz_4()
    
def jo_valasz_4():    
    print("NARRÁTOR")
    print("Ding, ding, ding! Helyben is volnánk!")
    time.sleep(3)
    print("Az eddig üresen álló széket KÖD fedi be, majd ELTŰNIK, és a széken már egy KISFIÚ foglal helyet.")
    time.sleep(3)
    print("NARRÁTOR")
    print("A következő feladvány kicsit eltér majd a többitől. A kis lurkó lesz a beszélgetőpartnere, aki számos mesélni valóval érkezett ide, magának pedig csak és kizárólag annyi a dolga, hogy jó szülőként támogassa. Nem tűnik nehéznek, ugye?")
    time.sleep(5)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nos…")
    time.sleep(1)
    print("NARRÁTOR")
    print("Nem hát. Akkor Showtime!")
    time.sleep(2)
    print("Egy pillanat alatt ELLEPI a vagont a már jól ismert füst, de ahogy megérkezik, úgy el is TŰNIK. A háttér egyszeriben MEGVÁLTOZIK, egy vagon belseje helyett már egy ÉTTERMI környezetben láthatjuk a szereplőket. Az asztalra étel, ital és szalvéta is került.")
    time.sleep(5)
    print("A DETEKTÍV láhatóan FESZENG a szituációtól, de elfogadja, hogy nincs más választása.")
    time.sleep(2)
    print("FIÚ")
    print("(bal kezével a fejét támasztva, villájával a tányérján lévő borsót bökdösve)")
    print("Képzeld, apu, ma végre volt bátorságom megmondani Hannah-nak, hogy tetszik.")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("I… igen? És öhm… hogy ment?")
    time.sleep(2)
    print("FIÚ")
    print("Ő nem kedvel engem.")
    time.sleep(2)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Miért?")
    time.sleep(2)
    print("FIÚ")
    print("Mert bogarasnak tart. Furának. Szerinte beteges az, hogy csináltam neki egy pénztárcát macskabőrből.")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Te… megnyúztál egy macskát a bőréért?")
    time.sleep(3)
    print("FIÚ")
    print("(flegmán)")
    print("Talán problémád van vele? ")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nem, dehogy. Vagyis hát… tudod, ez… megértem, ha ez egyes embereket megijeszt.")
    time.sleep(3)
    print("FIÚ")
    print("(agresszívan)")
    print("Szerintem azok a betegek, akik nem képesek értékelni egy ajándékot, amivel sokat szenvedtem. Tudod, milyen nehéz megnyúzni egy cicát?")
    time.sleep(5)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nem… még sosem próbáltam.")
    time.sleep(3)
    print("FIÚ")
    print("És ki akarod próbálni?")
    
    print(""" A.a)	Nem, mert az állatkínzás undorító és beteges dolog
B. Nem, mert én nem tartom helyesnek az állatkínzást""")
    choice = input(">>> ")
    if choice in valasz_A:
        a_opcio1()
    elif choice in valasz_B:
        b_opcio1()
    else:
        print(szukseges)
    
    
def a_opcio1():
    print("FIÚ")
    print("Szóval akkor te is úgy gondolod, hogy beteg vagyok?")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nézd, kölyök, amit tettél, az nagyon csúnya dolog. Gusztustalan. Ilyet csak a rossz emberek csinálnak, a nagyon rossz emberek.")
    time.sleep(3)
    print("FIÚ")
    print("(önelégülten)")
    print("De legalább csináltam belőle egy menő pénztárcát.")
    time.sleep(2)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("ÉS EZÉRT KÉPES VOLTÁL MEGNYÚZNI EGY KIBASZOTT MACSKÁT?!")
    time.sleep(5)
    print("Az egész étterem LEDERMED. Síri csend uralkodik el az egyébként dugig tömött vendéglőben.")
    time.sleep(4)
    print("A gyerek arcára félelem és szomorúság ül. ")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Ne haragudj, kölyök, de--")
    time.sleep(2)
    print("A FIÚ kirohan az étteremből.")
    time.sleep(2)
    print("Az étterem köddé válik, visszakerülünk a jól megszokott vagon falai közé.")
    time.sleep(2)
    print("NARRÁTOR(V.O.)")
    print("Szép volt nyomozó, gratula. ")
    time.sleep(2)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Mit kellett volna tennem?!")
    time.sleep(2)
    print("NARRÁTOR(V.O.)")
    print("Finomabban is helyre rakhatta volna a gyereket.")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Abból ő nem értene. Nem látta? A gyerek egy pszichopata! Ha finom vagyok vele, abból semmit nem tanulna. Csak így tudta—")
    time.sleep(2)
    print("A köd elnyeli A DETEKTÍVET.")
    time.sleep(2)
    print("NARRÁTOR(V.O.)")
    print("Már csak ezért a hozzáállásért is megérdemli ezt, detektív.")
    time.sleep(5)
    print("VÉGE.")
    
    halal()
    
def b_opcio1():
 time.sleep(3)
 print("FIÚ")
 print("Nem fájt neki. Elaltattam, mielőtt… tudod.")
 time.sleep(3)
 print("FŐSZEREPLŐ/DETEKTÍV")
 print("Elaltattad? ")
 time.sleep(2)
 print("FIÚ")
 print("Aha.")
 time.sleep(2)
 print("FŐSZEREPLŐ/DETEKTÍV")
 print("Hogyan?")
 time.sleep(2)
 print("FIÚ")
 print("Vízbe fojtottam.")
 time.sleep(2)
 print("A DETEKTÍV KIAKAD, de igyekszik leplezni indulatát.")
 time.sleep(2)
 print("FIÚ")
 print("De mindegy is. Ha egy medvét nyírok ki a bundájáért, akkor sem tudnám felkelteni az érdeklődését, mert annak a boszinak a „suli királya” kell.")
 time.sleep(3)
 print("FŐSZEREPLŐ/DETEKTÍV")
 print("Kicsoda?")
 time.sleep(2)
 print("FIÚ")
 print("A suli királya? Nem tudom pontosan. Annyit tudok, hogy felettünk jár, elvileg felsős is, és ő csicskáztat mindenkit. Semmi esze, de viszonylag izmos, ezért a legtöbben félnek tőle. Ez tetszik szívem szerelmének.")
 time.sleep(5)
 print("A FIÚ MEGMARKOLJA a kését, és az asztalba SZÚRJA.")
 time.sleep(3)
 print("FIÚ")
 print("Legszívesebben azt a gyökeret is megnyúznám! Hátha azt értékeli Ms. Hatalommánia. Sőt, ezzel még példát is statuálhatnék.")
 
 print("""A.Van, amikor egyedül már csak az erőszak a megoldás
B. Ez egy nagyon buta ötlet""")
 choice = input(">>>")
 if choice in valasz_A:
     a_opcio2()
 elif choice in valasz_B:
     b_opcio2()
 else:
    print(szukseges)
   
def a_opcio2():
    print("FIÚ")
    print("Tényleg úgy gondolod?")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nem akarlak erre buzdít—")
    time.sleep(1)
    print("FIÚ")
    print("Teljesen igazad van, apa! Meg kell állítanom azt a gyereket!")
    time.sleep(3)
    print(" FŐSZEREPLŐ/DETEKTÍV")
    print("Ez a beszéd!")
    time.sleep(2)
    print("FIÚ")
    print("És ha a dolgok odáig fajulnak, akkor -de csak is akkor – kénytelen leszek bántani.")
    time.sleep(4)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("De csak is a legvégső esetben.")
    time.sleep(3)
    print("FIÚ")
    print("Persze persze. Most azonnal elmegyek hozzá.")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Vigyázz magadra! És ne feledd, csak a végső esetben alkalmazz erőszakot!")
    time.sleep(4)
    print("A FIÚ FELPATTAN az asztaltól, felkapja a KÉSÉT, és KIVIHARZIK az étteremből.")
    time.sleep(4)
    print("Ekkor KÖDFELHŐ emelkedik fel, eltűnik az étterem, és ismét a vonaton találjuk magunkat.")
    time.sleep(2)
    print("NARRÁTOR(V.O.)")
    print("Felelősségteljes apuka maga, csessze meg!")
    time.sleep(2)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Ezt most miért mondja? A kölyök szembeszáll az igazságtalansággal! Kiáll magáért és másokért.")
    time.sleep(3)
    print("NARRÁTOR")
    print("Az első dolga az lesz, hogy cafatokra késeli azt a felsős fiút! Utána meg bosszút áll azon a Hannah nevű lányon!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Ez csak spekuláció.")
    time.sleep(2)
    print("NARRÁTOR")
    print("A GYEREK MEGNYÚZOTT EGY MACSKÁT EGY KISBICSKÁVAL!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("…")
    time.sleep(3)
    print("NARRÁTOR")
    print("MAGA MEG EGY ÉLES KÉSSEL ÚTJÁRA BOCSÁTOTTA, HOGY „BESZÉLJÉK MEG” A GONDJAIKAT AZZAL A SRÁCCAL, AKI ÉPPEN A SZERELMÉNEK TETSZIK!!!")
    time.sleep(4)
    print("NARRÁTOR")
    print("HOL HORDJA MAGA AZ ESZÉT?! A NADRÁGJÁBAN?!")
    time.sleep(4)
    print("KÖD szökik fel a padlóról és a DETEKTÍV köré gyűlik.")
    time.sleep(3)
    print("NARRÁTOR")
    print("Ezek után meg is érdemli, amit kap!")
    time.sleep(3)
    print("A KÖD ELNYELI a DETEKTÍVET.")
    time.sleep(2)
    print("VÉGE.")

    halal()
  
def b_opcio2():
    print("FIÚ")
    print("De hisz’ ő mindenkit az alattvalójának tart! Kihasznál mindenkit!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Az erőszak NEM megoldás! Nem ölhetsz meg valakit, csak azért, mert rossz ember!")
    time.sleep(3)
    print("FIÚ")
    print("De miért nem?! Ő rossz! Megérdemelné!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nem játszhatsz egyszemélyes ítélőszéket, kölyök! A sors majd megbünteti. Vagy majd lesz valaki, aki megveri helyetted.")
    time.sleep(4)
    print("FIÚ")
    print("Én akarok rajta bosszút állni!")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Ha megtennéd, se lenne jobb neked. A bosszúvágy kielégítésével nem jár feloldozás. Nem lesz jobb neked attól, ha elvered azt a pancsert!")
    time.sleep(5)
    print("FIÚ")
    print("Akkor mit csináljak?")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Próbálj meg beszélni vele.")
    time.sleep(3)
    print("FIÚ")
    print("(ironikusan)")
    print("Azzal biztos sokra mennék.")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Nem tudhatod. Sosem tudhatod, kinél elég a szó, és kinél nem.")
    time.sleep(3)
    print("FIÚ")
    print("Ezért kell mindig ütni!")
    time.sleep(1)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Ezért nem szabad soha ütni! Ha megteszed, nem leszel jobb ember nála. Ugyanolyan rossz leszel, mint ő.")
    time.sleep(4)
    print("FIÚ")
    print("És ha sok rosszat ütök meg?")
    time.sleep(2)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Ne akarj mindenáron verekedni. Nem visz előre. Neked előre kell menni, nem hátra.")
    time.sleep(4)
    print("A FIÚ megértette, amit mondtak neki.")
    time.sleep(2)
    print("FIÚ")
    print("Hát akkor tűröm tovább.")
    time.sleep(3)
    print("FŐSZEREPLŐ/DETEKTÍV")
    print("Hidd el nekem, kölyök, egyszer eljön a te időd. Na nem a bosszúra. Találsz majd egy másik lányt, és igazságosan – na meg törvényesen – legyőzöd majd a rosszakat.")
    time.sleep(6)
    print("FIÚ")
    print("Kösz, apu!")
    time.sleep(3)
    print("A FIÚ köddé válik, vele együtt az étterem is. Visszakerülünk a VAGON FALAI közé.")
    time.sleep(3)
    print("NARRÁTOR")
    print("Ez nagyon megható volt, komolyan. Majdnem könnyezni kezdtem. Gratulálok, detektív! Határozottan kiállta a próbámat!")
    time.sleep(5)
    print("A vagon elejében lévő ajtó KINYÍLIK.")
    time.sleep(3)
    print("NARRÁTOR")
    print("Haladjunk tovább, barátom!")
    
    
 