import matplotlib.pyplot as plt
import numpy as np

# Simulating Provo River June 2021 Data (Replace with actual CSV parsing as instructed)
dates_provo = np.arange(1, 31)  # 30 Days in June
y_1_provo = np.random.randint(200, 400, size=30)
y_2_provo = np.random.randint(150, 350, size=30)
y_3_provo = np.random.randint(100, 300, size=30)
y_4_provo = np.random.randint(50, 250, size=30)
y_5_provo = np.random.randint(20, 150, size=30)

print("Created simulated arrays for Provo River Streamflow Data.")

plt.figure(figsize=(12, 6))
plt.plot(dates_provo, y_1_provo, label='Site 10163000')
plt.plot(dates_provo, y_2_provo, label='Site 10155200')
plt.plot(dates_provo, y_3_provo, label='Site 10155500')
plt.plot(dates_provo, y_4_provo, label='Site 10154200')
plt.plot(dates_provo, y_5_provo, label='Site 10155000')

plt.title('Provo River Streamflow Data - June 2021')
plt.xlabel('Day of June')
plt.ylabel('Streamflow (cfs)')
plt.grid(True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()