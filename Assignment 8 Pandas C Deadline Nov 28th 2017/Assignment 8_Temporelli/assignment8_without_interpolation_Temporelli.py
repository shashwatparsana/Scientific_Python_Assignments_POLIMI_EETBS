import os
import numpy as np
import pandas as pd
os.chdir("C:\Users\Proprietario\Desktop\Ingegneria Magistrale\Building systems\Python lessons\lesson8 (pandas+excel)")

# Excel files reading
windows_DF = pd.read_csv("windows.csv",sep=";",index_col=0)
BeamIrradiance_DF = pd.read_csv("BeamIrradiance.csv",sep=";",index_col=0)
DiffuseIrradiance_DF = pd.read_csv("DiffuseIrradiance.csv",sep=";",index_col=0)


# Defining a function that calculate PXI
def PXI_calculator(latitude_location,windowID):
    BeamIrradiace_value = BeamIrradiance_DF[latitude_location][windowID]
    DiffuseIrradiance_value = DiffuseIrradiance_DF[latitude_location][windowID]
    PXI_value = BeamIrradiace_value+DiffuseIrradiance_value
    return PXI_value
       
# Latitude for Piacenza (RLF example I)
latitude_location = "45"

# writing a for loop to do the look up of PXI for all windows using the developed function
PXI_values=[]
for index in windows_DF.index.tolist():
    print index
    PXI_values = np.append(PXI_values,PXI_calculator(latitude_location,windows_DF["Direction"][index]))
    
#windows.csv updating
windows_DF["PXI"] = np.array(PXI_values)
windows_DF.to_csv("windows_completed_with_PXI.csv",sep=";")
windows_DF.to_html("windows_completed_with_PXI.html")
    
        