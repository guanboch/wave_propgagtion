#%%
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline

cc = 3e8
freq1 = 2.4e9
freq2 = 2.41e9
freq3 = 2.42e9
# %%
lambd1 = cc/freq1
lambd2 = cc/freq2
lambd3 = cc/freq3 

k1 = 2*np.pi/lambd1
k2 = 2*np.pi/lambd2
k3 = 2*np.pi/lambd3

dz = lambd1/20

t_s = 1/10e9
t = np.arange(0,2000*t_s, t_s)
z = np.arange(0,4000*dz,dz)

tv,zv = np.meshgrid(t,z)



s1 = np.sin(2*np.pi*freq1*tv - k1*zv)
s2 = np.sin(2*np.pi*freq2*tv - k2*zv)
s3 = np.sin(2*np.pi*freq3*tv - k3*zv)

s = s1+s2+s3
# %% signal at different spatial point

plt.figure(1)
plt.plot(z, s[:,0])
plt.xlabel('distance')
plt.ylabel('amplitude')
plt.title('Envelope of signal, when t= 0')

plt.figure(11)
plt.plot(z, s[:,100])
plt.xlabel('distance')
plt.ylabel('amplitude')
plt.title('Envelope of signal, when t= 100')

# %%

plt.figure(2)
plt.plot(t,s[0,:])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('time domain signal at spatial point z = 0')

plt.figure(22)
plt.plot(t,s[1000,:])
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('time domain signal at spatial point z = 1000')

# %%



plt.figure(3)
plt.plot(z[0:20],s1[:20,0])

# %%
fig = plt.figure(4)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(tv,zv,s)

 
 
 
# %%
