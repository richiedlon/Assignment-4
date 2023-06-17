import rasterio
def writeRaster(out_img,out_meta,out_tif): # Input numpy array of the biophysical output, metadata of clipped raster, output location
	"""
		    Write a NumPy array to a raster file.

		    Args:
		    	out_img = numpy array
		    	out_meta = meta data (one of the return from clip_withBB_function and clip_withSHP_function)
		    	out_tif = 'path/to/input_raster.tif'

	"""
	with rasterio.open(out_tif, "w", **out_meta) as dest:
		dest.write(out_img)