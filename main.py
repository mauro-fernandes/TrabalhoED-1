
"""
Código:
Mauro Fernandes de Almeida
ED 2021.2
"""

class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0,item)
    def removeFront(self):
        if self.isEmpty():
            return
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def first(self):
        if len(self.items) < 1:
            return None
        return self.items[len(self.items) - 1]
    def last(self):
        if len(self.items) < 1:
            return None
        return self.items[0]
    def show(self):
        return self.items
    def goTo_min(self):
        for i in range(len(self.items)):
            if self.items[len(self.items) - 1] == min(self.items):
                return
            self.addRear(self.removeFront())
    def goTo_max(self):
        for i in range(len(self.items)):
            if self.items[len(self.items) - 1] == max(self.items):
                return
            self.addRear(self.removeFront())
    def reverse(self):
        self.items = self.items[::-1]
    def inject(self, iterable):
        for i in iterable:
            self.addRear(i)
    def rotate(self, n):
        for _ in range(n):
            self.addRear(self.removeFront())
    def doJob(self):
        if self.isEmpty():
            print('empty deque!')
            return
        if self.items[0] == []:
            del self.items[0]
        return self.items[-1].pop()
    def del1stProc(self):
        del self.items[-1]
    def delLastProc(self):
        del self.items[0]



###########
# FUNÇÕES #
###########

def deYodafy(W):
    punctuation = W[-1]
    phrase = W[:-1].split(' ')
    newPhrase = phrase[::-1]
    out = ' '.join(newPhrase) + punctuation
    return out


def halt():
    
    if processDeque.isEmpty():
        print(f'{0} processo(s) e {0} comando(s) órfão(s).')
        return
    pQueue = processDeque.show()
    orphProcs = len(pQueue)
    orphComms = 0
    for procs in pQueue:
        for comm in procs:
            orphComms += 1
    print(f'{orphProcs} processo(s) e {orphComms} comando(s) órfão(s).')
    return


def add(n):
    """
    input: integer number (n) of commands,
    then add process to queue (one input command per line)
    output: (command, args) tuple
    """
    processReq = []
    temp = []
    for i in range(n):
        inpt = input().split()
        command = inpt[0]
        arg = ' '.join(inpt[1:])
        #print('comando solicitado: ', command, arg)
        temp.append([command, arg])
        processReq.append([command, arg])
    #print('requisição de processo: ', processReq) #
    processReq = processReq[::-1]
    processDeque.addRear(processReq)
    log.append([temp])
    #print ('fila atualizada: ', processDeque.show()) #



    
def cryptoSort(S, n):
    cont=0
    while cont < len(S):
        cont = 0
        for i in range(len(S)):
            if S[i] == '-':
                if n[i] < n[i + 1]:
                    n[i], n[i + 1] = n[i + 1], n[i]
                else:
                    cont += 1
            else:
                if n[i] > n[i + 1]:
                    n[i], n[i + 1] = n[i + 1], n[i]
                else:
                    cont += 1
    return n

                    

def crypto(S):
    nums = [1,2,3,4,5,6,7,8,9]
    tam = len(S) + 1
    useDgts = nums[:tam]
    #print('useDgts: ', useDgts)
    listCode = cryptoSort(S, useDgts)   
    code = ''
    for i in listCode:
        code += str(i)
    return code

                    

def merge(I):
    I = I.strip('[]').split('] [')
    intervals = []
    for iStr in I:
        a, b = map(int, (iStr.split(', ')))
        intervals.append([a,b])
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    #print('sorted intervals: ', intervals)
    #print('initMerged: ', merged)    
    for j in intervals:
        #print('elementos do intervalo: ', j)
        last = merged[-1]
        if min(j) <= last[1]:
            last[1] = max(last[1],j[1])
        else:
            #print('novo intervalo adicionado: ', j)
            merged.append(j)    
    return merged




def process():
    if processDeque.isEmpty():
        #print('Empty Process Deque. Try add process')
        return
    if processDeque.first() == []:
        process.Deque.del1stProc()
    
    queueJob = processDeque.doJob()
    if queueJob == None or len(queueJob) == 0:
        print('Erro! Não há comando a processar')
    processDeque.rotate(1)
    
    if processDeque.first() == []:
        #print('processo exaurido... Próximo:') #
        processDeque.del1stProc()
    
    if processDeque.last() == []:
        #print('processo exaurido... Próximo:') #
        processDeque.delLastProc()
    
    
    #print('req in queueJob: ', queueJob) #
    
    if queueJob[0] == 'crypto':
        S = crypto(queueJob[1])
        print(S)
    elif queueJob[0] == 'deYodafy':
        #print('Yoda instructions to BAT2: ')
        W = (deYodafy(queueJob[1]))
        print(W)
    elif queueJob[0] == 'merge':
        #print('Merging sequences: ')
        I = merge(queueJob[1])
        print(*I)
    else:
        print('Comando não reconhecido') 
    return


    
#####################
# Program Beginning:
#####################

    
#print('A força está com você!!!') #

log = []
processDeque = Deque()
while True:
    inpt = input().split()
    
    if inpt == []:
        print('Insira um comando') 
        continue

    if inpt[0] == 'add':
        n = int(inpt[1])
        #print('reqs: ', reqs, 'adicione os processos para a fila: ')
        add(n)
        
    elif inpt[0] == 'halt':
        halt()
        break
    
    elif inpt[0] == 'process':
        process()
    
    elif inpt[0] == 'showpd':
        pd = processDeque.show()
        print(pd)
        
    elif inpt[0] == 'log':
        print(log)
    
    else:
        print('Comando não reconhecido.')
        continue
   


# test inputs:
"""
add 1
crypto ---
add 2
crypto -+-
merge [1, 3] [3, 4] [5, 8] [6, 10]
add 1
deYodafy contra-atacar deve Império!
add 1
merge [1, 3] [6, 10] [3, 4] [5, 8]
add 2
crypto +-+-
merge [1, 3] [6, 10] [3, 4] [5, 8]
add 1
deYodafy faça não ou faça.
add 2
crypto -+-
merge [1, 7] [2, 5] [5, 10] [8, 9]
"""

