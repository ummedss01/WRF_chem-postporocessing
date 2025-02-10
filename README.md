# Extracting 3D Variables from WRF/WRF-Chem Output Files

## Overview

This Python code facilitates the extraction of one or more 3D variables from multiple `wrfout_*.nc` files. The extracted variable is stored in NetCDF format. this will help in map generation and data analysis.

## Required Python Packages

*   `xarray`
*   `wrf-python`
*   `netCDF4`

## How to Use This Code

1.  **WRF Output Path:** Define the directory containing the `wrfout_*.nc` files in the `wrfoutoperInd` variable.
2.  **Variable Selection:** Specify the name(s) of the 3D variable(s) you wish to extract in the `variables_3d` list.  This can be a single variable name or a list of multiple variable names.

## Annimated map with PM2.5 ground concetration with hourly value from WRF-chem output 
 - https://github.com/user-attachments/assets/1a0c5610-9110-436a-8add-60daf972cfe4
## References

