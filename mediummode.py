import random

OA = '  '
OB = '  '
OC = '  '
OD = '  '
OE = '  '
OF = '  '
OG = '  '
OH = '  '
TA = '  '
TB = '  '
TC = '  '
TD = '  '
TE = '  '
TF = '  '
TG = '  '
TH = '  '
THA = '  '
THB = '  '
THC = '  '
THD = '  '
THE = '  '
THF = '  '
THG = '  '
THH = '  '
FA = '  '
FB = '  '
FC = '  '
FD = '  '
FE = '  '
FF = '  '
FG = '  '
FH = '  '
FIA = '  '
FIB = '  '
FIC = '  '
FID = '  '
FIE = '  '
FIF = '  '
FIG = '  '
FIH = '  '
SA = '  '
SB = '  '
SC = '  '
SD = '  '
SE = '  '
SF = '  '
SG = '  '
SH = '  '
SEA = '  '
SEB = '  '
SEC = '  '
SED = '  '
SEE = '  '
SEF = '  '
SEG = '  '
SEH = '  '
EA = '  '
EB = '  '
EC = '  '
ED = '  '
EE = '  '
EF = '  '
EG = '  '
EH = '  '
main_screen = """
|    __ _ _ _ _                         ________________    _________________                    _____________      _____________                                ___________
|   |          \             /\                 |                   |           |               |                  /                    |             |    |    |           \           
|   |           |           /  \                |                   |           |               |                 /                     |             |    |    |            \           
|   |           |          /    \               |                   |           |               |                /                      |             |    |    |            /
|   |_ _ _ _ _ /          /      \              |                   |           |               |_____________   \                      |             |    |    |___________/
|   |          \         /__ _ __ \             |                   |           |               |_____________    \_____________        |_____________|    |    |           
|   |           \       /          \            |                   |           |               |                              \        |             |    |    |   
|   |            |     /            \           |                   |           |               |                               \       |             |    |    |
|   |            |    /              \          |                   |           |               |                               /       |             |    |    |
|   |_ _ _ _ _ _ /   /                \         |                   |           |__________     |_____________    _____________/        |             |    |    |
|                                                                                                           
"""
main_screen2 = main_screen.center(40,'-')
print(main_screen2)
pravila = 'Upute: Kada upisujete polje koje zelite pogoditi, pisite strukturom "broj_slovo". Ako bi htjeli provjeriti prvi red slovo A onda biste napisali "1a". Imate 8 pokusaje koja se trose svakim krivim poljem, a ako pogodite ispravno polje broj pokusaja vam se ne smanjuje. Trebate pogoditi 8 polja, Stisnite enter kako biste zapoceli igru. '
unospravila = input(pravila)
pobjeda = """       
    |    __________        _________         __________                             ___________    ___________
    |   |          |      /         \       |          \                     |     |              |           \               /\\
    |   |          |     /           \      |           |                    |     |              |            \             /  \\
    |   |          |    |             |     |           |                    |     |              |             |           /    \\
    |   |__________|    |             |     |__________/                     |     |              |             |          /      \\
    |   |               |             |     |          \                     |     |___________   |             |         /        \\  
    |   |               |             |     |           \                    |     |              |             |        /__________\\    
    |   |               |             |     |            \                   |     |              |             |       /            \\       
    |   |               |             |     |             |                  |     |              |             |      /              \\
    |   |                \           /      |             |     \            |     |              |            /      /                \\
    |   |                 \_________/       |____________/       \___________|     |___________   |___________/      /                  \\                     
    |                
    """

tries = 8
count = 0
def srednje():
    global tries
    global count
    global pobjeda
    listofv = [OA,OB,OC,OD,OE,TA,TB,TC,TD,TE,THA,THB,THC,THD,THE,FA,FB,FC,FD,FE,FIA,FIB,FIC,FID,FIE]
    formatlist = ['1a', '1b', '1c', '1d','1e','2a', '2b', '2c', '2d','2e','3a', '3b', '3c', '3d','3e', '4a', '4b', '4c', '4d','4e','5a', '5b', '5c', '5d','5e']
    listOfH = []
    while len(listOfH) < 8:
        listOfH.append(random.choice(formatlist))
        listOfH = list(set(listOfH))
    while len(listOfH) > 0 and tries > 0 and count != 8:
            ploca =""" 
            0   A   B   C   D   E
            1   {}  {}  {}  {}  {}
            2   {}  {}  {}  {}  {}
            3   {}  {}  {}  {}  {}
            4   {}  {}  {}  {}  {}
            5   {}  {}  {}  {}  {}

            """.format(*listofv)
            print(ploca)
            unos = input('Unesite polje:')
            if unos in listOfH:
                listOfH.remove(unos)
                listofv[formatlist.index(unos)] = 'H '
                count += 1
                print('POGODAK, imas jos {} pokusaja, a trebas pogoditi jos {} brodova'.format(tries, len(listOfH)))
            elif unos not in listOfH and unos in formatlist:
                listofv[formatlist.index(unos)] = 'X '
                tries -= 1
                print('FULO SI, imas jos {} pokusaja, a trebas pogoditi jos {} brodova'.format(tries, len(listOfH)))
            else:
                print('Nepostojuce polje')
                continue

main_menu ="""
:::::::::::::::::::::::::::::::::::::::::::::::
:::::::::: DOBRO DOSLI U BATTLESHIP :::::::::::
:::::::::::::: IZABERITE TEZINU :::::::::::::::
:::::::::::::: 1. Lagano(polje 4x4) :::::::::::
:::::::::::::: 2. Srednje(polje 5x5) ::::::::::
:::::::::::::: 3. Nemoguce(polje 6x6) :::::::::
:::::::::::::::::::::::::::::::::::::::::::::::
"""
main_menu_input = int(input(main_menu))
if main_menu_input == 2:
    srednje()

if count == 8:
    print(pobjeda)
  
    
elif count < 8 and tries == 0:
    print('IZGUBIO SI')