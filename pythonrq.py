#python mi ez mi az

#print
print("Hello world") #standard print

sugar = 3 #változó, eltárolja a hármas számot
print('A kör kerülete: ', 2 * sugar * 3.14, ', területe: ', sugar ** 2 * 3.14, '.', sep='')
  
#for ciklus
for i in range(10): #(0-9 ig a számo)
    print(i)#egymás alá      
    print(i, end="") #  egymás mellé
  
#while ciklus
    
szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1
  
#lista
tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
    print(tantargy)      
#,
honapok = ['január', 'február','március', 'április', 'május', 'június']

for index, honap in enumerate(honapok): #
    print(index, honap)

#listaelemek leképzése
eredeti = [11, 19, 7, -3]

eredmeny = [x * 2 for x in eredeti]

eredmeny_szurve = [x * 2 for x in eredeti if x > 0]
  

#if, elif, else(kivételkezelés)
szam = int(input('Adj meg egy számot! ')) #változók fő típusai: int(szám), str(string), bool(true, false érték)
if szam < 0:
    print('A megadott szám negatív.')
elif szam == 0:
    print('A megadott szám nulla.')
else:
    print('A megadott szám pozitív.')
print('>> A program vége! <<')

# Eljárás definíciója
def koszont_nevvel(nev):
        print('Szia '+ nev +', üdv a fedélzeten!')

# Eljárás hívása    
koszont_nevvel('Ádám')

# Függvény definíciója
def festek_kalkulator(x, y):
    '''
    Kiszámolja az adott falfelület festéséhez
    szükséges festék mennyiségét
    '''
    t = x * y
    l = t * 0.13
    return l


# Függvény hívása
liter = festek_kalkulator(5, 2)

# A függvény hívása lehet egy kifejezés része is
ar = festek_kalkulator(5, 2) * 700

#random
#import randomot a kód legelejére írtuk
import random

random_szam = random.randint(1,10)
print(random_szam)

#and or not
x = 5
y = -3

if x < 0 and y < 0:
print('mindkettő negatív')

if x < 0 or y < 0:
print('van köztük negatív')

if not x <= 0:
print('x pozitív')  
  