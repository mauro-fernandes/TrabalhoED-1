
def cryptoSort(S, n):
    cont=0
    while cont < len(S):
        cont = 0
        for i in range(len(S)):
            if S[i] == '-':
                if n[i] < n[i + 1]:
                    n[i], n[i + 1] = n[i + 1], n[i]
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
                    

def crypto(S):
    nums = [1,2,3,4,5,6,7,8,9]
    tam = len(S) + 1
    useDgts = nums[:tam]
    print('useDgts: ', useDgts)
    useDgts = useDgts[::-1]
    listCode = cryptoSort(S, useDgts)   
    code = ''
    for i in listCode:
        code += str(i)
    return code

                else:
                    cont += 1
            else:
                if n[i] > n[i + 1]:
                    n[i], n[i + 1] = n[i + 1], n[i]
                else:
                    cont += 1
                    

def crypto(S):
    nums = [1,2,3,4,5,6,7,8,9]
    tam = len(S) + 1
    useDgts = nums[:tam]
    print('useDgts: ', useDgts)
    useDgts = useDgts[::-1]
    listCode = cryptoSort(S, useDgts)   
    code = ''
    for i in listCode:
        code += str(i)
    return code

#code = crypto('-+-')
#print(code) 
    
# usar bubble sort 'dirigido' pelos sinais operadores

#if __name__ == "__main__":


signs = input('TESTE. entre com os sinais para encriptar: ')
code = crypto(signs)
print(code)























'''

    
    for j in range(len(useDgts) - 1):
        for i in range(len(useDgts) - 1):
            for h in S:
                if useDgts[i] > useDgts[i+1] and h == '+':
                    useDgts[i], useDgts[i+1] = useDgts[i+1], useDgts[i]
    return useDgts





code = ''      
permutacoes = ['123', '132', '213', '231', '312', '321' ]
seq = '-+'
candidatos = []



for s in permutacoes:
    for i in range(len(seq)):
        if s[i]> s[i+1]:
            if seq[i] == '-':
                candidatos.append(s)
        
        
        elif s[i] < s[i+1]:
            if seq[i] == '+':
                candidatos.append(s)
                
print('code: ', candidatos)
'''        
        



'''
for i in range(len(permutacoes)):
    print(permutacoes[i])
    for k in range(len(seq)):
        for j in range(len(permutacoes[i])):
            #print(permutacoes[i][j])
            #print(seq[k])
            if (j+1) > len(permutacoes[i])-1:
                break
            if k == '-':
                if permutacoes[i][j] > permutacoes[i][j+1]:
                    print(permutacoes[i][j])
                    candidatos.append(permutacoes[i][j])
            elif k == '+':
                if permutacoes[i][j] < permutacoes[i][j+1]:
                    print(permutacoes[i][j])
                    candidatos.append(permutacoes[i][j])
'''
                 




# alternativa:
# sort algorhitm with pivot
    
'''
    mid = (len(S) + 1)//2
    positives = 0
    negatives = 0
    
    if S[mid] == '+':
    for i in range(mid):
        if i == '+':
            midPositives += 1
        else:
            midNegatives += 1
'''
    
 