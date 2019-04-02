import visa
import numpy as np
import time as time
import matplotlib.pyplot as plt

# Input values
awg_address = 'USB0::0x0957::0x0407::MY44043483::0::INSTR'  # Waveform Generator Address
dmm_address = 'USB0::0x2A8D::0xB318::MY58160107::0::INSTR'  # Digital Multimeter Address

Vmin = 0  # LowerDMMDCOutputVoltage(Volts)
Vmax = 10  # UpperDMMDCOutputVoltage(Volts)
N_Volts = 51  # Number of voltages between V min and V max

# Define voltage and current vectors
V = np.linspace(Vmin, Vmax, N_Volts)
V1 = np.linspace(Vmin, Vmax, 10 * N_Volts + 1)
Imeas = np.zeros(N_Volts)

# Initiate communications with and open instruments
rm = visa.ResourceManager()
awg = rm.open_resource(awg_address)
dmm = rm.open_resource(dmm_address)

# Place waveform generator in High−Z awg.write(”OUTP:LOAD INF”)
awg.write("OUTP:LOAD INF")

# Conduct Measurements
count = 0
for K in V:
    print ("Applying % f Volts" % K)
    awg.write("APPL:DC DEF, DEF, % f" % K)
    time.sleep(1)
    Imeas[count] = dmm.query("MEAS:CURR:DC? 1e−1,1e−5")
    count = count + 1

# Calcuate resistor value and estimated current vector
Rest = V.dot(V) / V.dot(Imeas)
Iest = V1 / Rest

# Plot Current vs . Voltage
plt.plot(V, Imeas * 1000, 'bo', markersize=4, label='Measured')
plt.plot(V1, Iest * 1000, 'r−', linewidth=2, label='Fitted')
plt.grid()
plt.legend()
plt.xlabel("Voltage(V)")
plt.ylabel("Current(mA)")
plt.title("Estimated Resistance = " + '{:.0f}'.format(Rest) + r'$\Omega$', Rest)
plt.show()  # Make plot visible
