def get_S1_metadata(image_name):

	"""
	Retrieve metadata of a Sentinel-1 image based on the file name.

	Args:
	    file_name (str): The name of the Sentinel-1 image file.

	Returns:
	    dict: A dictionary containing metadata information.

	Example:
	    >>> get_sentinel1_metadata('file name')
	    {
	        'sensor': 'S1A',
	        'Beam': 'IW',
	        'Product_Type': 'GRDH',
	        'Resolution': '1SDV',
	        'Start_date_time': '2021-06-16T18:06:50',
	        'Stop_date_time': '2021-06-16T18:07:15',
	        'Absolute_orbit_Number': '038321',
	        'Mission_Data_ID': '0477D0',
	        'Product_Unique_ID': '1C',
	    }
	"""
	metadataList = {}

	# Split the image name by underscores
	parts = image_name.split('_')

	# Extract metadata from the image name
	metadataList['sensor'] = parts[0]
	metadataList['Beam'] = parts[1]
	metadataList['Product_Type'] = parts[2]
	metadataList['Resolution'] = parts[3]
	metadataList['Start_date_time'] = parts[4]
	metadataList['Stop_date_time'] = parts[5]
	metadataList['Absolute_orbit_Number'] = parts[6]
	metadataList['Mission_Data_ID'] = parts[7]
	metadataList['Product_Unique_ID'] = parts[8]
	return metadataList

