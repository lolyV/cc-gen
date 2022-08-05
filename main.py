def main():


  def ccn():

    list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list5 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list6 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list7 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list8 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list10 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list11 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list12 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list13 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list14 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list15 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    list16 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    import random

    r = random

    r1 = r.choice(list1)
    r2 = r.choice(list2)
    r3 = r.choice(list3)
    r4 = r.choice(list4)
    r5 = r.choice(list5)
    r6 = r.choice(list6)
    r7 = r.choice(list7)
    r8 = r.choice(list8)
    r9 = r.choice(list9)
    r10 = r.choice(list10)
    r11 = r.choice(list11)
    r12 = r.choice(list12)
    r13 = r.choice(list13)
    r14 = r.choice(list14)
    r15 = r.choice(list15)
    r16 = r.choice(list16)

    cclist = "Credit Card Number: "+r1+r2+r3+r4+" - "+r5+r6+r7+r8+" - "+r9+r10+r11+r12+" - "+r12+r13+r14+r15

    print(cclist)

  def cvc():

    list01 = ["1", "2","3","4","5","6","7","8","9","0"]
    list02 = ["1", "2","3","4","5","6","7","8","9","0"]
    list03 = ["1", "2","3","4","5","6","7","8","9","0"]

    import random

    random01 = random.choice(list01)
    random02 = random.choice(list02)
    random03 = random.choice(list03)

    cvclist = "CVC: "+random01+random02+random03

    print(cvclist)

  def exp():

    list001 = ["1", "2","3","4","5","6","7","8","9","10","11","12"]
    list002 = ["22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37"]

    import random

    random001 = random.choice(list001)
    random002 = random.choice(list002)

    explist = "Expiration Date: "+random001+" / "+random002 
    print(explist)
    
    print("""
 /$$                            /$$$$$$  /$$   /$$ /$$    /$$$$$$   /$$$$$$   /$$$$$$    /$$  
| $$                           /$$__  $$| $$  / $$/ $$   /$$$_  $$ /$$$_  $$ /$$$_  $$ /$$$$  
| $$        /$$$$$$   /$$$$$$ | $$  \__/| $$ /$$$$$$$$$$| $$$$\ $$| $$$$\ $$| $$$$\ $$|_  $$  
| $$       /$$__  $$ /$$__  $$| $$$$    | $$|   $$  $$_/| $$ $$ $$| $$ $$ $$| $$ $$ $$  | $$  
| $$      | $$$$$$$$| $$$$$$$$| $$_/    |__/ /$$$$$$$$$$| $$\ $$$$| $$\ $$$$| $$\ $$$$  | $$  
| $$      | $$_____/| $$_____/| $$          |_  $$  $$_/| $$ \ $$$| $$ \ $$$| $$ \ $$$  | $$  
| $$$$$$$$|  $$$$$$$|  $$$$$$$| $$       /$$  | $$| $$  |  $$$$$$/|  $$$$$$/|  $$$$$$/ /$$$$$$
|________/ \_______/ \_______/|__/      |__/  |__/|__/   \______/  \______/  \______/ |______/
                                                                                              
                                                                                              
                                                                                              
""")
  whichone = int(input("Which part do you want? 1: CCN. 2: CVC. 3: EXP. 4: SET? "))

  if whichone == 1:
    
    howmany = int(input("How many CCN's do you want: "))
    for x in range(1,howmany):
      ccn()

  if whichone == 2:

    howmany = int(input("How many CVC's do you want: "))
    for x in range(0,howmany):
      cvc()

  if whichone == 3:
    howmany = int(input("How many EXP's do you want: "))
    for x in range(0,howmany):
      exp()

  if whichone == 4:
    howmany = int(input("How many sets do you want: "))
    for x in range(0,howmany):
      ccn()
      cvc()
      exp()
  elif (whichone != 1 and 2 and 3 and 4):
    print("Option not valid. Please restart program or type `main()` then enter!")

main()
