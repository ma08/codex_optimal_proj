

import numpy as np
import matplotlib.pyplot as plt

# データのパラメータ
N = 256            # サンプル数
dt = 0.01          # サンプリング間隔
fq = 5             # 周波数
fs = 1 / dt        # サンプリング周波数
t = np.arange(0, N*dt, dt)  # 時間軸
freq = np.linspace(0, 1.0/dt, N)  # 周波数軸

# 信号を生成（周波数10の正弦波）
f = np.sin(2*np.pi*fq*t)

# 高速フーリエ変換
F = np.fft.fft(f)

# 振幅スペクトルを計算
Amp = np.abs(F)

# パワースペクトルを計算
Pow = Amp ** 2

# 振幅スペクトルを整形
Amp_amp = Amp / N * 2  # 交流成分は2倍不要
Amp_amp[0] = Amp_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要

# パワースペクトルを整形
Pow_amp = Pow / N
Pow_amp[0] = Pow_amp[0] / 2  # 直流成分（今回は扱わないけど）は2倍不要

# 波形を描画
plt.subplot(311)  # 3行1列のグラフの1番目の位置にプロット
plt.plot(t, f)
plt.xlabel("Time")
plt.ylabel("Signal")

# 振幅スペクトルを描画
plt.subplot(312)  # 3行1列のグラフの2番目の位置にプロット
plt.plot(freq, Amp_amp)
plt.xlabel("Frequency")
plt.ylabel("Amplitude spectrum")

# パワースペクトルを描画
plt.subplot(313)  # 3行1列のグラフの3番目の位置にプロット
plt.plot(freq, Pow_amp)
plt.xlabel("Frequency")
plt.ylabel("Power spectrum")

plt.show()
