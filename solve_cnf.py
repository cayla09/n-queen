from pysat.solvers import Minisat22
from pysat.formula import CNF
import math

################ using minisat to solve n-queens #############
#file1= open("queen2sat.cnf","a");
formula = CNF(from_file = 'queen2sat.cnf')
#print(formula.clauses)
m = Minisat22(bootstrap_with=formula.clauses,use_timer=True)
#m.solve()
control = False
while(m.solve()==True):
    s=(m.get_model())
    int_list = [ i*-1 for i in s]
    #print(s)
    #print('{0:.2f}s'.format(s.time()))
    print('{0:.5f}s'.format(m.time_accum()))
    with open('require_input','r')as fr:
        read_data = fr.read()
    rd=read_data.split(' ')
    #print(read_data)
    rd=[int(i) for i in rd]
    #print(rd)
    rd_set=set(rd)
    ans=set(s)
    result = rd_set.intersection(ans)
    #print(result)
    if rd[0]==0:
        print("No given queen's position")
        break
    elif len(result) == len(rd):
        print("True")
        control = True
        ctr = s
    else:
        print("False")
        if control == True:
            control = True
        else:
            control=False
    m.add_clause(int_list)
    #if fulls!="": 
        #file1.write(fulls)
        #m.add_clause(fulls)
        #print(fulls)
        #formula = CNF(from_file = 'queen2sat.cnf')
        #m = Minisat22(bootstrap_with=formula.clauses)

#s=(m.get_model())
#file1.close()
#print(s)
#s = s.split(' ')
m.delete()
############### find where's the queen's position ############
if control == True:
    s = ctr
    #print(s)
    print("Find Solution")
elif control == False:
    print("NO Solution")
for i in range(len(s)):
    if(int(s[i])<0):
        s[i] = 0
    else:
        s[i] = 1

n = math.sqrt(len(s))
n =int(n) 
def get_answer(s,n):
    for i in range(0,len(s)-1,n):
        yield s[i:i+n]
s = list(get_answer(s,n))
f = open('ans.txt','w')
for i in range(len(s)):
    f.write(str(s[i]))
    f.write('\n')

f.close()

