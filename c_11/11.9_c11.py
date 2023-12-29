arrivals = ['adele','fleda','owen','may','mona','gillbert','ford']

def party_late(arrivals,name):
    if (arrivals.index(name)+1) == len(arrivals):
            return False
    if (arrivals.index(name)+1) > (len(arrivals)/2):
            return True
    else:
            return False
        
print(party_late(arrivals,name='gillbert'))
print(party_late(arrivals,name='ford'))
print(party_late(arrivals,name='mona'))