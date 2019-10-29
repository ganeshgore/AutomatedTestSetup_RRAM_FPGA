# AutomatedTestSetup_RRAM_FPGA

Python Modules and Jupyter projects to check RRAM FPGA test chips



## Script filename and purpose

- **Simple_SMU_DSO_Check**: This script integrates the DSO and SMU setup using the python visa library. In hardware, all four channels of the SMU are connected to DSO.

- **WGFMU_Test** : Sample code to do fast measurement using WGFMU unit. It also demonstrats the integration of Spot measurement and Pulse spot measurement. 

- **NVFF_CMOS_functionality_check** : This script checks the functionality of the DFF by only considering the CMOS part. It performs 2 measurements 1. Connectivity test 2.VDD Current Test 3.DFF Read/Write functionality check


## Reference PDFs 

- [B1500A Programming Guide ](https://www.keysight.com/upload/cmc_upload/All/programming_guide_english.pdf) 
- [B1530A WGFMU Program LEarning Kit](https://www.keysight.com/upload/cmc_upload/All/B1530-90500.pdf) 
- [Rigol-DS1074 Digital Storage Oscilloscope](http://int.rigol.com/File/TechDoc/20151218/MSO1000Z&DS1000Z_ProgrammingGuide_EN.pdf)
