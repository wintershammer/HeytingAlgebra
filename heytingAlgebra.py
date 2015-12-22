from itertools import chain, combinations

class Poset:

    def __init__(self,baseSet,relation):
        self.baseSet = baseSet
        self.relation = relation


    def meet(self,X): #i should checking if X is subset of P!
        'Calculates greatest lower bound of X in the underlying set'
        lowerBounds = []
        for y in self.baseSet:
            flag = True
            for x in X:
                #print(y," <= ",x," ?",": ",self.relation(y,x))
                if self.relation(y,x) != True:
                    flag = False
            if (flag):
                lowerBounds.append(y)
        glb = None
        for y in lowerBounds: #for every y,z E lowerBounds
            bFlag = True
            for z in lowerBounds: 
                if self.relation(z,y) == False: #if z is not less than y
                    bFlag = False #then y is not the greatest lower bound
            if bFlag == True:
                glb = y
        return glb


    def join(self,X): #i should checking if X is subset of P!
        upperBounds = []
        for y in self.baseSet:
            flag = True
            for x in X:
                #print(y," <= ",x," ?",": ",self.relation(y,x))
                if self.relation(x,y) != True:
                    flag = False
            if (flag):
                upperBounds.append(y)
        lub = None
        for y in upperBounds: #for every y,z E lowerBounds
            bFlag = True
            for z in upperBounds: 
                if self.relation(y,z) == False: #if z is not less than y
                    bFlag = False #then y is not the greatest lower bound
            if bFlag == True:
                lub = y
        return lub
            
############ EXAMPLES OF POSETS #####################        
        


def powsetGen(i):
    toReturn = []
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        toReturn.append(subset)
    return toReturn


def subset(x,y):
    return set(x).issubset(y)


a = Poset(powsetGen(["a","b","c"]),subset) #powerset of a,b,c ordered by subset relation


def prefix(x,y):
    if x == y:
        return True
    else:
        return str(y).startswith(str(x))


binary3 = ["","1","0","10","00","01","11","000","001","010","011","100","101","110","111"]

binaryStrings = Poset(binary3,prefix) #The binary strings of length <= 3, ordered by the prefix relation (assuming a string is a prefix of itself)


