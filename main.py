
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
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.utils import platform
KV = '''
<IconListItem>




MDScreen

    MDTextField:
        id: field
        pos_hint: {'center_x': .5, 'center_y': .6}
        size_hint_x: None
        width: "200dp"
        hint_text: "Password"
        on_focus: if self.focus: app.menu.open()
'''

class MapViewApp(MDApp):
    def run(self):
        if platform == 'android':
            from android.permissions import Permission, request, permissions
            def callback(permissions, results):
                if all([res for res in results]):
                    print("ok")
                else:
                    print('No')
            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)
        if platform == 'android' or platform == 'ios':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
            on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)
    def updata_blinker_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon = kwargs["lon"]

        print(my_lat, my_lon)
    def on_auth_status(self, general_status, status_message):
        if general_status == 'provider-enabled':
            pass
        else:
            self.open_gps_access_popup()
    
    def open_gps_acess_popup(self):
        dialog_gps = MDDialog(title="GPS 권한 오류", text="GPS 권한을 허용해야합니다.")
        dialog_gps.size_hint = [.8,.8]
        dialog_gps.pos_hint = {'center_x': .5, 'center_y': .5}
        dialog_gps.open()

    def build(self): 
        
        box_layout = BoxLayout()
        num = 0

        def click(self):
            num = btns.index(self)
            bs = MDListBottomSheet()
            bs.add_item("[b]%s[/b]" % wifi_csv.iloc[num]['SSID'], lambda x: x)
            bs.add_item("[font=data/fonts/NanumGothic.ttf] 설치 장소명:[/font]"+
                    "[font=data/fonts/NanumGothic.ttf] %s (%s)[/font]" % (wifi_csv.iloc[num]['loc'], wifi_csv.iloc[num]['loc1']), lambda x: x)
            bs.add_item("[font=data/fonts/NanumGothic.ttf][b] 위치:[/b][/font]"+
                    "[font=data/fonts/NanumGothic.ttf] %s[/font]" % wifi_csv.iloc[num]['loc2'], lambda x: x)
            
            bs.add_item("[font=data/fonts/NanumGothic.ttf] 서비스 제공사[/font]"+
                    "[font=data/fonts/NanumGothic.ttf] %s[/font]" % wifi_csv.iloc[num]['services'], lambda x: x)
        
            bs.open()


        wifi_csv = pd.read_csv("wifi.csv", encoding='cp949')

        btns = []

        mapview = MapView(zoom=17, lat=37.390875171289345, lon=127.07846795319912)
        mapview.map_source = "osm"
        box_layout.add_widget(mapview)

        markers = []

        for i in range(len(wifi_csv.index)-25800):
            lat = float(wifi_csv.iloc[i]['lat'])
            lon = float(wifi_csv.iloc[i]['lon'])
            if lat > 0 and lon > 0:
                marker = MapMarkerPopup(lat=lat, lon=lon,source = 'wifi_marker_image.png')
                btns.append(Button(text=wifi_csv.iloc[i]['SSID']+"\n\n\n > 자세히 보기",font_context='system://myapp', font_name='data/fonts/NanumGothic.ttf',background_normal='normal.png',border=(30,30,30,30) ))
                marker.add_widget(btns[i])
                btns[i].bind(on_press=click)
                mapview.add_widget(marker)

            else:
                continue
            
            print(i)
    
        return box_layout
        
if __name__ == '__main__':
        Window.size = (375, 812)
        MapViewApp().run()
