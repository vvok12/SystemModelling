import random
import math
import numpy
import matplotlib.pyplot as plt

graf = numpy.array([
    [0,1,1,1], #poisson stream intensity to pass to states [s0, s1, s2, s3]
    [0,0,2,0],
    [2,1,0,4],
    [1,0,9,0]
    ])

TIME = 20 # moment to show
AGENTS_AMOUNT = 10**4

states_amount = len(graf)
states_start_pos = numpy.array([1/states_amount for i in range(states_amount)])

states_start_cum_pos = numpy.array([sum(states_start_pos[:i+1:]) for i in range(len(states_start_pos))])

result_state_calculator = []

def rTime(r, l):
    return (-1/l)*math.log(1 - r)

def random_state(r):
    for i,v in enumerate(states_start_cum_pos):
        if (r<v):
            return i

agents = ([random_state(random.random()), 0] for i in range(AGENTS_AMOUNT))

#run agents
for a in agents:
    while True:
        s = a[0] #current state
        pt = numpy.where(graf[s]>0)#possible transitions from state s
        if (len(pt[0])==0):
            a[1]+= TIME
        else:    
            ptt = numpy.array(list( ##possible transitions time
                map(rTime, numpy.random.random(len(pt[0])), graf[s, pt[0]])
                ))
        
            ns = numpy.argmin(ptt) ## next state wich has min transition time
            nst = ptt[ns] ## its time
            a[1] += nst

        if (a[1]<TIME):
            a[0] = pt[0][ns];
        else:
            result_state_calculator.append(s)
            break


result_states = list(set(result_state_calculator))
result_freq = [result_state_calculator.count(i)/len(result_state_calculator) for i in result_states]
plt.plot(result_states, result_freq, marker ="d")
plt.ylim(0,1)
for a,b in zip(result_states, result_freq):
    plt.text(a,b+0.02,str(b))
plt.show()
