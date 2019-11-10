# In[1]:
import pyvisa
import logging
import sys
import os
import time
from pprint import pprint
from quantiphy import Quantity as QE

# Configure Logger
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s- [%(lineno)d] - %(message)s')
lg = logging.getLogger(__name__)

# ==================== Configuration Section ====================
b1500_conn_str = 'GPIB0::17::INSTR'
SMU_1, SMU_2, SMU_3, SMU_4 = 2, 3, 4, 5

VDD_PIN  = SMU_1
PMOS_PIN = SMU_2

vdd_v, comp_i= 1.2, 100E-6

# In[2]:
# Setting up PyVISA interface
rm = pyvisa.ResourceManager()

# = = = = = = = = = Setting up B1500 = = = = = = = = =
b1500 = rm.open_resource(b1500_conn_str)
device_name = b1500.query("*IDN?")
b1500.write("*RST")  # Reset B1500 to initial state
b1500.write("FMT 1")  # Set IO Format
print(f"Connected to {device_name}")
b1500.write(f"CL")  # Open All switches

# In[3]:

lg.info("############### Running MUX01 VDD Test ###############")
# This section performs read measurement using SMU only
VR, VG, VS, VY = 0.3, 3, 0, 5.5
Icomp = 100E-6

# Open Channel Switch
b1500.write(f"CL")
b1500.write(f"CN")
b1500.write("DV %d,0,%.2f,%.2E" % (PMOS_PIN, vdd_v, Icomp))
time.sleep(0.1)
b1500.write("DV %d,0,%.2f,%.2E" % (VDD_PIN, vdd_v, Icomp))
# Measure Current
time.sleep(0.1)
vdd_curr = b1500.query(f"TI {VDD_PIN}")
gate_curr = b1500.query(f"TI {PMOS_PIN}")
b1500.write("DV %d,0,%.2f,%.2E" % (VDD_PIN, 0, Icomp))
time.sleep(0.1)
b1500.write("DV %d,0,%.2f,%.2E" % (PMOS_PIN, 0, Icomp))
b1500.write(f"CL")
time.sleep(1)
lg.info("Error Codes : " + b1500.query("ERR?").strip())
lg.info("VDD Current %s", QE(vdd_curr[4:], "A"))
lg.info("PMOS Gate Current %s", QE(gate_curr[4:], "A"))

time.sleep(2)
b1500.close()