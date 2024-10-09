import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Parameter
L = 1.0  # panjang sisi pita suara
c = 1.0  # kecepatan gelombang
A = 0.1  # amplitudo
T = 2.0  # total waktu simulasi
dx = dy = 0.01  # ukuran grid spasial
dt = 0.005  # ukuran grid waktu
nx, ny = int(L/dx), int(L/dy)
nt = int(T/dt)

# Kondisi awal
x = np.linspace(0, L, nx)
y = np.linspace(0, L, ny)
X, Y = np.meshgrid(x, y)
u0 = A * np.sin(np.pi * X / L) * np.sin(np.pi * Y / L)
u = u0.copy()
up = u0.copy()  # u di waktu sebelumnya
un = np.zeros((nx, ny))  # u di waktu selanjutnya

# Konstanta untuk perhitungan
coeff = (c * dt / dx)**2

# Fungsi untuk update u
def update_u():
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            un[i, j] = (2 * u[i, j] - up[i, j] + coeff * (
                        u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - 4 * u[i, j]))
    return un

# Simulasi
fig, ax = plt.subplots()
img = ax.imshow(u0, extent=(0, L, 0, L), vmin=-A, vmax=A, cmap='viridis')

def animate(frame):
    global u, up
    if frame > 1:
        u = update_u()
        up, u = u, un.copy()
    img.set_data(u)
    return img,

ani = animation.FuncAnimation(fig, animate, frames=nt, interval=50)
plt.colorbar(img)
plt.title('Simulasi Gelombang pada Pita Suara')
plt.show()
