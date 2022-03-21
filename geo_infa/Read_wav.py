import scipy.io.wavfile as wav
import matplotlib.pyplot as plt


fs, data = wav.read('signal.wav')
data = data[303*fs:304*fs]

plt.figure(figsize=(10,5))

plt.plot(data)
plt.xlabel("$Порядковый$ $номер$")
plt.ylabel("$Значение$ $сигнала$")
plt.title("$График$ $зависимости$ $значения$ $сигнала$ $от$ $его$ $порядкового$ $номера$")
# plt.show()
plt.savefig("T_n.png")


