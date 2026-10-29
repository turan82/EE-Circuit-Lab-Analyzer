import numpy as np
import matplotlib.pyplot as plt

def calculate_inductance(reactance, frequency):
    """
    Endüktif reaktans formülünden endüktansı (L) hesaplar: X_L = 2 * pi * f * L
    """
    return reactance / (2 * np.pi * frequency)

# --- ÖRNEK LABORATUVAR VERİLERİ (Bobin / Solenoid Testi) ---
frequencies = np.array([100, 500, 1000, 2000, 5000])  # Hz
reactances = np.array([3.14, 15.7, 31.4, 62.8, 157.0])  # Ohm

inductances = calculate_inductance(reactances, frequencies)
avg_inductance = np.mean(inductances)

print(f"Hesaplanan Ortalama Endüktans: {avg_inductance * 1e3:.2f} mH")

# --- GRAFİK ÇİZİMİ ---
plt.figure(figsize=(8, 5))
plt.plot(frequencies, reactances, 'ro-', label='Ölçülen Reaktans (X_L)')
plt.title('Bobin Frekans - Reaktans İlişkisi (Solenoid / Toroid Analizi)')
plt.xlabel('Frekans (Hz)')
plt.ylabel('Reaktans (Ω)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Grafiği kaydet
plt.savefig('inductance_plot.png')
print("Grafik 'inductance_plot.png' olarak kaydedildi.")





