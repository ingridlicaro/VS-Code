import netCDF4
import numpy as np
import matplotlib.pyplot as plt

# Define the path to the NetCDF file
file_path = r"C:/Users/lizet/OneDrive/Documentos/Benthic Ecology/NetCDF/Hidrografico_Tides_Copernicus/IR_TS_TG_VianaDoCasteloTG.nc"

# Open NetCDF
dataset = netCDF4.Dataset(file_path, mode='r')

# Print the dataset information
print(dataset)

# Get variable names
var_names = list(dataset.variables.keys())
print("Variable names:", var_names)

# Extract data from the first variable
variable_name = var_names[0]  
var_data = dataset.variables[variable_name][:]
print(f"Data from {variable_name}:", var_data)

time_data = dataset.variables['TIME'][:]
slev_data = dataset.variables['SLEV'][:, 0]

# Close NetCDF
dataset.close()

plt.figure(figsize=(10, 5))
plt.plot(time_data, slev_data, label='Sea level')
plt.xlabel('Time')
plt.ylabel('Sea level')
plt.title('Level Sea Over Time')
plt.legend()
plt.show()