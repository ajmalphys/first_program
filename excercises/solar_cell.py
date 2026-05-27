import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
q = 1.602e-19  # Electron charge (C)
kB = 1.381e-23  # Boltzmann constant (J/K)
T = 300  # Temperature (K)
Vth = (kB * T) / q  # Thermal voltage (~0.0259 V)


# 1. Define the IV function (Explicit approximation for visualization)
def calculate_iv(IL, I0, n, Rs, Rsh):
    # Generate a voltage array from 0V to an estimated Voc
    V = np.linspace(0, 0.8, 500)

    # Using an iterative approach to solve the implicit diode equation accurately
    I = np.zeros_like(V)
    for i, v in enumerate(V):
        # Quick Newton-Raphson or fixed-point iteration to find I for each V
        current_I = IL  # initial guess
        for _ in range(10):  # 10 iterations is usually plenty for convergence
            f = IL - I0 * (np.exp((v + current_I * Rs) / (n * Vth)) - 1) - (v + current_I * Rs) / Rsh - current_I
            df = -I0 * (Rs / (n * Vth)) * np.exp((v + current_I * Rs) / (n * Vth)) - (Rs / Rsh) - 1
            current_I = current_I - f / df
        I[i] = current_I

    # Clip negative values so the graph looks clean past Voc
    I = np.clip(I, 0, None)
    return V, I


# 2. Set up the initial parameters
init_IL = 0.040  # Photocurrent (A) -> e.g., 40 mA
init_I0 = 1e-10  # Dark saturation current (A)
init_n = 1.2  # Diode ideality factor
init_Rs = 1.0  # Series resistance (Ohms)
init_Rsh = 1000.0  # Shunt resistance (Ohms)

# 3. Create the plot interface
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(left=0.15, bottom=0.35)  # Make room for sliders

V, I = calculate_iv(init_IL, init_I0, init_n, init_Rs, init_Rsh)
line, = ax.plot(V, I * 1000, lw=2, color='blue')  # Convert I to mA for plotting

ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (mA)')
ax.set_title('Interactive Solar Cell I-V Curve')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlim(0, 0.8)
ax.set_ylim(0, 45)

# 4. Create UI Sliders
ax_IL = plt.axes([0.15, 0.23, 0.65, 0.03])
ax_n = plt.axes([0.15, 0.18, 0.65, 0.03])
ax_Rs = plt.axes([0.15, 0.13, 0.65, 0.03])
ax_Rsh = plt.axes([0.15, 0.08, 0.65, 0.03])

s_IL = Slider(ax_IL, 'I_L (A)', 0.01, 0.06, valinit=init_IL)
s_n = Slider(ax_n, 'n', 1.0, 2.5, valinit=init_n)
s_Rs = Slider(ax_Rs, 'R_s ($\Omega$)', 0.0, 10.0, valinit=init_Rs)
s_Rsh = Slider(ax_Rsh, 'R_sh ($\Omega$)', 10, 5000, valinit=init_Rsh, valfmt='%0.0f')


# 5. Define update logic when sliders move
def update(val):
    # Get current values from sliders
    IL = s_IL.val
    n = s_n.val
    Rs = s_Rs.val
    Rsh = s_Rsh.val
    I0 = init_I0  # Keeping I0 static for simpler scaling, but can be slider-driven too

    # Recalculate and redraw
    new_V, new_I = calculate_iv(IL, I0, n, Rs, Rsh)
    line.set_xdata(new_V)
    line.set_ydata(new_I * 1000)
    fig.canvas.draw_idle()


# Link sliders to the update function
s_IL.on_changed(update)
s_n.on_changed(update)
s_Rs.on_changed(update)
s_Rsh.on_changed(update)

plt.show()