
from kivy_garden.mapview import MapView, clustered_marker_layer
from kivy_garden.mapview.view import MapMarker, MapMarkerPopup, MarkerMapLayer 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
import time

class MapViewApp(App):

       
    def build(self):
        wifi_csv = pd.read_csv("wifi.csv", encoding='cp949')
        box_layout = BoxLayout()
        mapview = MapView(zoom=17, lat=37.390875171289345, lon=127.07846795319912)
        mapview.map_source = "osm"
        box_layout.add_widget(mapview)
        markers = []

        
        for i in range(len(wifi_csv.index)):
            lat = float(wifi_csv.iloc[i]['lat'])
            lon = float(wifi_csv.iloc[i]['lon'])
            if lat > 0 and lon > 0:
                mapview.add_marker(MapMarker(lat=lat, lon=lon,  source = 'wifi_marker_image.png'))
            else:
                continue
            
            print(i)
        

            
    
        return box_layout
        
if __name__ == '__main__':

        MapViewApp().run()
