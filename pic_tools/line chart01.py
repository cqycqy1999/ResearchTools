import matplotlib.pyplot as plt

rounds = list(range(0, 150, 10))
# FedAvg = []

FedPer = [1.02, 32.42, 44.62, 42.20, 43.73, 41.84, 41.77, 41.64, 38.05, 41.52, 38.87, 37.98, 41.21, 39.80, 38.93,]
LG_FedAvg = [1.02, 30.83, 37.39, 35.96, 38.97, 38.08, 40.36, 39.79, 39.82, 38.11, 40.86, 43.33, 44.26, 41.90, 44.58,]
FedRoD = [1.47, 35.23, 40.90, 41.74, 44.53, 46.45, 46.81, 46.93, 44.89, 49.54, 49.39, 48.86, 49.37, 50.42, 50.92,]
GPFL = [1.02, 30.97, 37.02, 44.26, 44.84, 44.83, 45.42, 46.04, 46.83, 47.06, 47.96, 48.18, 48.93, 49.94, 50.82,]
FedALA = [1.02, 32.21, 40.36, 42.43, 44.5, 44.55, 46.6, 46.63, 46.66, 47.675, 47.69, 48.7, 48.705, 48.71, 48.72,]
FedCAC = [0.99, 29.24, 37.32, 40.395, 42.48, 43.525, 44.57, 44.615, 45.63, 45.645, 46.66, 47.675, 48.685, 49.87, 49.71,]
our_method = [1.02, 31.31, 44.4, 45.535, 46.55, 46.61, 46.67, 47.695, 48.72, 48.735, 49.75, 50.76, 51.765, 52.07, 52.82,]

plt.figure(figsize=(8, 6))
plt.ylim(0, 60)  
# plt.plot(rounds, FedAvg, marker='o', label='FedAvg')

plt.plot(rounds, FedPer, marker='x', label='FedPer')
plt.plot(rounds, LG_FedAvg, marker='P', label='LG-FedAvg')
plt.plot(rounds, FedRoD, marker='*', label='FedRoD')
plt.plot(rounds, GPFL, marker='s', label='GPFL')
plt.plot(rounds, FedCAC, marker='d', label='FedCAC')
plt.plot(rounds, FedALA, marker='^', label='FedALA')
plt.plot(rounds, our_method, marker='v', label='PFractaL')

plt.xlabel('Round', fontsize=14)
plt.ylabel('Test Accuracy (%)', fontsize=14)
plt.legend(fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)  
plt.grid(True)
plt.tight_layout()
plt.title('Performance Comparison on Dir~0.3 CIFAR-100', fontsize=14)
plt.show()
