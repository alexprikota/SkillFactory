import numpy as np
import matplotlib.pyplot as plt

Tstart = 0.0
Tend=10.0
dT=0.1

#print("тип данных t_cur:",type(t_cur))
#print("тип данных Tend:",type(Tend))
#print("тип данных dT:",type(dT))


Tsize = int(Tend/dT) + 1
print(Tsize)
#exit()

T_arr = np.zeros((Tsize,), dtype=np.float64)
F_arr = np.zeros((Tsize,), dtype=np.float64)
IC=0.0
T_arr[0]=Tstart
F_arr[0]=IC
ind=1
t_cur = Tstart+dT
while t_cur<=Tend:
    T_arr[ind] = t_cur
    F_arr[ind] = F_arr[ind-1]+(T_arr[ind]-T_arr[ind-1])*t_cur
    t_cur = t_cur+dT
    ind = ind + 1

print(T_arr)
print(F_arr)


plt.plot([1, 2, 3], [1, 2, 3], 'go-', label='line 1', linewidth=2)
plt.plot([1, 2, 3], [1, 4, 9], 'rs', label='line 2')

plt.show()

#exit()












