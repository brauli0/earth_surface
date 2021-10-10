from flask import Flask, abort
from flask_restful import Resource, Api, reqparse
from business import Business, EarthSurface

app = Flask(__name__) 
api = Api(app)

class HelloWorld(Resource):
   def get(self):
      return Business.hello_world()

class GetSurface(Resource):
   def get(self):
      parser = reqparse.RequestParser()
      parser.add_argument('lat', type=str)
      parser.add_argument('lon', type=str)
      args = parser.parse_args()
      
      print(args)
      
      try:
         lat = float(args['lat'])
      except:
         abort(400, description = 'latitude value is invalid [lat]')
      try:
         lon = float(args['lon'])
      except:
         abort(400, description = 'longitude value is invalid [lon]')

      return EarthSurface.earth_surface_by_point(lat, lon) # 42.985699, -7.837807

api.add_resource(HelloWorld, '/helloworld')
api.add_resource(GetSurface, '/getsurface')

# curl "http://localhost/getsurface?lat=42.985699&lon=-7.837807"

if __name__ == '__main__':
   app.run(debug=True)