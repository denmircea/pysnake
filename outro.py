import os
def outro():
    os.system('cls' if os.name=='nt' else 'clear')
    print("""                      _           _   
                     | |         | |  
  _   _  ___  _   _  | | ___  ___| |_ 
 | | | |/ _ \| | | | | |/ _ \/ __| __|
 | |_| | (_) | |_| | | | (_) \__ \ |_ 
  \__, |\___/ \__,_| |_|\___/|___/\__|
   __/ |                              
  |___/                               """)

    i=input()
    while(i!="pa"):
        i=input()
    sys.exit()
