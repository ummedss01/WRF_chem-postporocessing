
import os, sys, glob
from netCDF4 import Dataset
import wrf
import xarray as xr


variables_3d = [ 'PM2_5_DRY','o3', 'so2', 'nh3', 'co','no2' ]


wrfoutoperInd = '/home/beignias/data_analysis/'
for variable in variables_3d:
    ncfile = 'trailWRF_3D_' + variable + '.nc'
    print('Processing for 3D: ', variable)
    myVar = xr.concat([wrf.getvar(Dataset(file),variable) for file in sorted(glob.glob(wrfoutoperInd  + 'wrfout_d01_20*:00:00'))],dim='Time')
    data = myVar.data
    levels = myVar.bottom_top.data
    lons = myVar.XLONG[0,:].data
    lats = myVar.XLAT[:,0].data
    time = myVar.Time.data
    sss = xr.Dataset({variable: (("time","level","lat","lon"), data)},coords={"lat": lats, "lon": lons, "level":levels, "time":time},attrs = {"Long_Name":myVar.attrs['description'],"Units":myVar.attrs['units']})
    del myVar
    sss['level'].attrs = {'standard_name':'levels','long_name':'atmospheric_levels','units':'nounits','axis':'Z'}
    sss['lat'].attrs = {'standard_name':'latitude','long_name':'latitude','units':'degrees_north','axis':'Y'}
    sss['lon'].attrs = {'standard_name':'longitude','long_name':'longitude','units':'degrees_east','axis':'X'}
    sss.to_netcdf(ncfile)
    del sss