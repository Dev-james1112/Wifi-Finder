
from kivy_garden import mapview
from kivy_garden.mapview import MapView, clustered_marker_layer
from kivy_garden.mapview.view import MapMarker, MapMarkerPopup, MarkerMapLayer 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
import time
from kivy.core.text import Label as CoreLabel
from kivy.uix.button import Button
from kivy.core.text import FontContextManager as FCM
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.text.markup import *
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.banner import MDBanner
from kivymd.uix.bottomnavigation import MDTab,MDBottomNavigation
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.utils import platform
from kivy.clock import Clock
from kivy_garden.mapview import MapMarkerPopup
import sqlite3

KV = '''
'''

    
class MapViewApp(MDApp):
    def build(self): 
        
        box_layout = BoxLayout()
        num = 0
        def click(self):
            wifi_csv = pd.read_csv("wifi.csv", encoding='cp949')
            bs = MDListBottomSheet()
            bs.add_item("[b]%s[/b]" % wifi_csv.iloc[num]['SSID'], lambda x: x)
            bs.add_item("[font=data/fonts/NanumGothic.ttf] 설치 장소명:[/font]"+
                    "[font=data/fonts/NanumGothic.ttf] %s (%s)[/font]" % (wifi_csv.iloc[num]['loc'], wifi_csv.iloc[num]['loc1']), lambda x: x)
            bs.add_item("[font=data/fonts/NanumGothic.ttf][b] 위치:[/b][/font]"+
                    "[font=data/fonts/NanumGothic.ttf] %s[/font]" % wifi_csv.iloc[num]['loc2'], lambda x: x)
            
            bs.add_item("[font=data/fonts/NanumGothic.ttf] 서비스 제공사:[/font]"+
                    "[font=data/fonts/NanumGothic.ttf] %s[/font]" % wifi_csv.iloc[num]['services'], lambda x: x)
            bs.open()


        wifi_csv = pd.read_csv("wifi.csv", encoding='cp949')

        btns = []

        mapview = MapView(zoom=17, lat=37.390875171289345, lon=127.07846795319912)
        mapview.map_source = "osm"
        box_layout.add_widget(mapview)


        markers = []
        
        for i in range(len(wifi_csv.index)):
            lat = wifi_csv.iloc[i]['lat']
            lon = wifi_csv.iloc[i]['lon']
            lat = float(lat)
            lon = float(lon)
            if lat > 0 and lon > 0:
                marker = MapMarkerPopup(lat=lat, lon=lon,source = 'wifi_marker_image.png')
                btns.append(Button(text=str(wifi_csv.iloc[i]['SSID'])+"\n\n\n > 자세히 보기",font_context='system://myapp', font_name='data/fonts/NanumGothic.ttf',background_normal='normal.png',border=(16,16,16,16) ))
                btns[i].bind(on_press = click)
                marker.add_widget(btns[i])
                mapview.add_widget(marker)
                print(i)
                num = i
                
            else:
                btns.append("")
                print('불량',i,wifi_csv.iloc[i]['SSID'])
                continue
        print(wifi_csv.iloc[0]['lat'])
            
            
        
        return box_layout
            
    
if __name__ == '__main__':
        Window.size = (375, 812)
        MapViewApp().run()


