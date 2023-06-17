import rasterio
from rasterio.plot import show
import os
import numpy as np
import matplotlib
from rasterio.plot import show_hist
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
import fiona
from fiona.crs import from_epsg
# import pycrs
from rasterio.crs import CRS
from writeRasterFunction import writeRaster

def clipRasterSHP(locationRaster,locationSHP):
	"""
	Clips a shapefile using a raster file.

	Args:
	    locationSHP (str): Path to the shapefile.
	    locationRaster (str): Path to the raster file.

	Returns:
	    output_image_numpyarray, output_metadata, epsg_code

	Example:
	    >>> raster_file = 'path/to/input_raster.tif'
	    >>> shape_file = 'path/to/shapefile.shp' in WGS 1984
	    >>> clipped_numpy_array = clipRasterSHP(raster_file, shape_file)
	"""

	with fiona.open(locationSHP, "r") as shapefile:
		shapes = [feature["geometry"] for feature in shapefile]	
	with rasterio.open(locationRaster) as src:
		out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
		out_meta = src.meta
		epsg_code = int(src.crs.data['init'][5:])
	out_meta.update({"driver": "GTiff",
	                 "height": out_image.shape[1],
	                 "width": out_image.shape[2],
	                 "transform": out_transform,
	                 "count":1,
	                 "dtype":'float32',
	                 "crs": CRS.from_epsg(epsg_code)})

	return out_image,out_meta,epsg_code
