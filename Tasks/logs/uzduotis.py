
import math
import logging

# logging.basicConfig(filename="uzduotis_8_logai.log", level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')  # sukurem basic config su leveliu INFO ir formatu , i ji irasineja visus logus


# Kuriam savo logeri
#handleris gali but steramas, gali but i faila. Handleriu galima tureti daug. Galima nuo skirtingu leveliu i skirtingus failus kaupt. pvz critical ar dar kokiu kitokiu lygiu ir i atksirus failus viska loginam. Galim pasirinkt kiek laiko laikyt failus, pvz debug kas diena valom , info faila laikom menesi cia kaip pvz.

logger = logging.getLogger(__name__) # kam tas __name__ ??? kokia jo paskirtis
file_handler = logging.FileHandler('uzduotis_8_logai_2.log')
logger.addHandler(file_handler) # pridedam musu sukurta handleri 
logger.setLevel(logging.INFO) # priskiriam info leveli 
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s') # sukurem kokiu formatu mums atvaizduos
file_handler.setFormatter(formatter) # pridejom formata i musu file_handleri

stream_handler = logging.StreamHandler()  # padarem consoles logeri - stream handleri
stream_handler.setFormatter(formatter) # pridejom jam formata
logger.addHandler(stream_handler)




def paduotu_skaiciu_suma(*args):
    logger.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

def paduoto_skaiciaus_saknis(skaicius):
    try:
        logger.info(f"Skaiciaus {skaicius} saknis lygi {math.sqrt(skaicius)}")
    except:
        logger.exception("Paduotas stringas. Turi buti paduotas sveikas skaicius. ")
    else:
        return math.sqrt(skaicius)

def paduoto_sakinio_simboliu_kiekis(sakinys):
    logger.info(f"Sakinio {sakinys} ilgis lygus {len(sakinys)} simboliu")
    return len(sakinys)

def x_dalyba_is_y(x,y):
    try:
        logger.info(f"{x} padalinta is {y} lygu {x / y}")
    except ZeroDivisionError:
        logger.exception("Dalyba is 0 negalima")
    else:
        return x / y

print(paduotu_skaiciu_suma(4, 5, 7, 8, 9, 9,43556,45,34,534,534,5345,345,3))
print(paduoto_skaiciaus_saknis(49))
print(paduoto_sakinio_simboliu_kiekis("Labas rytas Code Academy!"))
print(x_dalyba_is_y(10, 5))
print(paduoto_skaiciaus_saknis("Aleliujaaaa"))
print(x_dalyba_is_y(2,0))

