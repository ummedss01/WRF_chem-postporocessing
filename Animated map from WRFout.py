import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.animation as animation

# Load wrfout Dataset 
ds=xr.open_dataset('/Users/trailWRF_3D_PM2_5_DRY.nc')
# Extract variables
pm25 = ds.PM2_5_DRY[:, 0, :, :]  # Select only ground level (level=0)
time = ds.time.values
lats = ds.lat.values
lons = ds.lon.values

# Setup Figure
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={"projection": ccrs.PlateCarree()})

# Create colorbar axis
cbar_ax = fig.add_axes([0.85, 0.3, 0.02, 0.4])  # Position for colorbar (right side)

# Function to plot each frame
def plot_frame(i):
    ax.clear()
    ax.set_title(f"PM2.5 Concentration at Ground Level\nTime: {np.datetime_as_string(time[i], unit='h')}")
    
    # Add map features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    
    # Plot PM2.5 concentration
    img = ax.contourf(lons, lats, pm25[i, :, :], levels=20, cmap="inferno", transform=ccrs.PlateCarree())

    # Update colorbar
    cbar_ax.clear()
    fig.colorbar(img, cax=cbar_ax, orientation="vertical", label="PM2.5 (µg/m³)")

    return img

# Create animation for all time steps
ani = animation.FuncAnimation(fig, plot_frame, frames=len(time), interval=500)

# Save animation video in directory
ani.save("/Users/pm25_ground_hourly_level.mp4", writer="ffmpeg", dpi=200)

plt.show()