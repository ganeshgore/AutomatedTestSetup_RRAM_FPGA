# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Description   : This script demostrate the use of  WGFMUPYLIB
# Author        : Ganesh Gore
# Email         : ganesh.gore@utah.edu
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
import os
import wgfmupylib as wgfmupylib
import wgfmupylib_const as WG

# Assign WGFMU dll path to following variable
DLL_PATH = "" or "C:\\Windows\\SysWOW64\\wgfmu"
GPIB_CONN_STR = b"" or b"GPIB0::17::INSTR"

# If your DLL path is oter tha 'C:\\Windows\\SysWOW64\\wgfmu'
# Executute followin funtion with correct path
wgfmupylib.LoadDLL(DLL_PATH)

try:
    assert not wgfmupylib.WGFMU_openSession(GPIB_CONN_STR)
    assert not wgfmupylib.WGFMUlib.WGFMU_closeSession()
except:
    print("Failed to connect to WGFMU")
    exit(1)
print("Succefully connected to WGFMU")