# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Description   : This script demostrat basic idea of creating WinDLL binding
#                 in python
# Author        : Ganesh Gore
# Email         : ganesh.gore@utah.edu
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
import os
import ctypes

# Assign WGFMU dll path to following variable
DLL_PATH = "" or "C:\\Windows\\SysWOW64\\wgfmu"
GPIB_CONN_STR = "" or b"GPIB0::17::INSTR"

# Open DLL file
WGFMUlib = ctypes.WinDLL(DLL_PATH)

# Create Python prototype for the fucnction
# You can find the list of APIs in the following PDF
# http://literature.cdn.keysight.com/litweb/pdf/B1530-90000.pdf
# WGFMU_openSession API
WGFMUlib.WGFMU_openSession.restype = ctypes.c_int
WGFMUlib.WGFMU_openSession.argtypes = [ctypes.c_char_p]
# WGFMU_closeSession API
WGFMUlib.WGFMU_closeSession.restype = ctypes.c_int

try:
    assert not WGFMUlib.WGFMU_openSession(GPIB_CONN_STR)
    assert not WGFMUlib.WGFMU_closeSession()
except:
    print("Failed to connect to WGFMU")
    exit(1)
print("Succefully connected to WGFMU")