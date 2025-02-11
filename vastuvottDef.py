
def Loe_failist(fail:str)->list:
    """ reading e. ainult lugemiseks, faili kirjutada ei lasta

    :Failist lugemine
    
    """
f = open('kusim.txt','r')
for line in f:
        print(line)
