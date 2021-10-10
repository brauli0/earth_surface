import numpy as np

print('Loading data...')
data = np.load("data.npz")
_lat = data['lat']
_lon = data['lon']
_mask = data['mask']
print('Data loaded')

class EarthSurface:
    def lat_to_index(lat):
        lat = np.array(lat)
        if np.any(lat>90):
            raise ValueError('latitude must be <= 90')
        
        if np.any(lat<-90):
            raise ValueError('latitude must be >= -90')
        
        lat[lat > _lat.max()] = _lat.max()
        lat[lat < _lat.min()] = _lat.min()
        return ((lat - _lat[0])/(_lat[1]-_lat[0])).astype('int')

    def lon_to_index(lon):
        lon = np.array(lon)
        if np.any(lon > 180):
            raise ValueError('longitude must be <= 180')
        
        if np.any(lon < -180):
            raise ValueError('longitude must be >= -180')
        
        lon[lon > _lon.max()] = _lon.max()
        lon[lon < _lon.min()] = _lon.min()
        return ((lon - _lon[0]) / (_lon[1] - _lon[0])).astype('int')
    
    def earth_surface_by_point(lat, lon):
        lat_i = EarthSurface.lat_to_index(lat)
        lon_i = EarthSurface.lon_to_index(lon)
        result = 'ocean' if _mask[lat_i,lon_i] else 'land'
        response = {
            'latitude': lat,
            'longitude': lon,
            'surface': result
        }
        return response

class Business:
    def hello_world():
        return 'Hello world! - This is my awesome API to know if a point is land or water'