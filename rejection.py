# Estimate Pi by throwing darts at a circle
import math
import random
import matplotlib.pyplot as plt
plt.ion()

# do 1000 random darts
N = 1000

# initialize some lists to store the good and bad
X_good = []
Y_good = []
X_bad = []
Y_bad = []

# do for each dart
for i in range(N):
    # generate point in [0,1] x [0,1]
    x = random.random()
    y = random.random()
    # Check if inside a circle of radius 1
    if x**2 + y**2 < 1:
        X_good.append(x)
        Y_good.append(y)
    else:
        X_bad.append(x)
        Y_bad.append(y)


# plot the good and bad in separate markers
plt.scatter(X_good, Y_good, marker='x', c='orange', label='Good')
plt.scatter(X_bad, Y_bad, marker='+', c='blue', label='Bad')
plt.legend()

## mimic a circle
K = 64
cx = [math.cos(2*math.pi*i/K) for i in range(K+1)]
cy = [math.sin(2*math.pi*i/K) for i in range(K+1)]
plt.plot(cx, cy, 'k-')

# A = pi r**2
# Area spanned by all random points is 2x2=4
pi_est = 4*len(X_good)/N
print(pi_est)
