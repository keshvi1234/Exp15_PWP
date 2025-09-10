import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Parameters
fs = 1000   # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # Time array (1 second, 1000 samples)

# Generate two sine waves
f1 = 5   # Frequency of first sine wave
f2 = 10  # Frequency of second sine wave
sine1 = np.sin(2 * np.pi * f1 * t)
sine2 = np.sin(2 * np.pi * f2 * t)

# Add the two signals
combined_signal = sine1 + sine2

# Plot the signals
plt.figure(figsize=(12, 8))

# First sine wave
plt.subplot(3, 1, 1)
plt.plot(t, sine1, label="5 Hz Sine Wave", color="b")
plt.title("5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# Second sine wave
plt.subplot(3, 1, 2)
plt.plot(t, sine2, label="10 Hz Sine Wave", color="g")
plt.title("10 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# Combined signal
plt.subplot(3, 1, 3)
plt.plot(t, combined_signal, label="Combined Signal (5 Hz + 10 Hz)", color="r")
plt.title("Combined Signal (5 Hz + 10 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()






# b.	Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500   # Sampling frequency
duration = 2  # seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)  # Time array

# Generate signals
f1 = 5   # Frequency of sine wave
f2 = 10  # Frequency of cosine wave
sine_wave = np.sin(2 * np.pi * f1 * t)
cosine_wave = np.cos(2 * np.pi * f2 * t)

# Multiply signals element-wise
product_signal = sine_wave * cosine_wave

# Plot the signals
plt.figure(figsize=(12, 8))

# 5 Hz sine wave
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, color="b")
plt.title("5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# 10 Hz cosine wave
plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave, color="g")
plt.title("10 Hz Cosine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# Product signal
plt.subplot(3, 1, 3)
plt.plot(t, product_signal, color="r")
plt.title("Product Signal (Sine × Cosine)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()





# c.	Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds. Plot the original and shifted signals on the same graph for comparison.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000   # Sampling frequency
duration = 1  # seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)  # Time array

# Generate 5 Hz sine wave
f = 5  # Frequency
sine_wave = np.sin(2 * np.pi * f * t)

# Shifted signal by 0.1 seconds
time_shift = 0.1  # seconds
shifted_sine_wave = np.sin(2 * np.pi * f * (t - time_shift))

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original 5 Hz Sine Wave", color="b")
plt.plot(t, shifted_sine_wave, label="Shifted 5 Hz Sine Wave (0.1s)", color="r", linestyle="--")
plt.title("Time Shifted Signal Comparison")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()






# d.	Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot the original and scaled signals together.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000   # Sampling frequency
duration = 1  # seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)  # Time array

# Generate 10 Hz sine wave
f = 10  # Frequency
sine_wave = np.sin(2 * np.pi * f * t)

# Scale amplitude by factor of 3
scaled_sine_wave = 3 * sine_wave

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original 10 Hz Sine Wave", color="b")
plt.plot(t, scaled_sine_wave, label="Scaled 10 Hz Sine Wave (×3)", color="r", linestyle="--")
plt.title("Amplitude Scaling of a 10 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()





# e.	Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. 
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000   # Sampling frequency
duration = 1  # seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)  # Time array

# Generate 5 Hz sine wave
f = 5
sine_wave = np.sin(2 * np.pi * f * t)

# Time reversal: reverse the signal
reversed_signal = sine_wave[::-1]

# Corresponding reversed time axis
t_reversed = t[::-1]

# Plot both signals
plt.figure(figsize=(10, 5))
plt.plot(t, sine_wave, label="Original 5 Hz Sine Wave", color="b")
plt.plot(t_reversed, reversed_signal, label="Time-Reversed 5 Hz Sine Wave", color="r", linestyle="--")
plt.title("Time Reversal of a 5 Hz Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
