from tkinter import *
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.label import Label



KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "Press here to read Terms & Conditions"  
        font_size: 32                   
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''

class Disclaimer(MDApp):
    dialog = None
    
    def build(self):
        
        Window.borderless = True
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        
        
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        
        if not self.dialog:
            
            self.dialog = MDDialog(
                text="                                    Read the Terms & Conditions:\n\n\n      This app is to be used for information only and is not to be used for repairs on your vehicle. Follow all instructions to avoid injury. If you have questions, seek a professional at your local mechanics shop. Automotive LLC is not responsible for damages.\n\n\n\n                              Do you accept the Terms & Conditions?",
                
                
                buttons=[
                    MDFlatButton(
                        text="YES",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = lambda x: self.close_dialog(),
                    ),
                    MDFlatButton(
                        text="NO",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = lambda x: self.bye_dialog(), 
                        
                    ),
                ],
            )
        self.dialog.open()
           
    def close_dialog(self):
        self.stop() 
        
    def bye_dialog(self):
        self.dialog.dismiss()
    
Disclaimer().run()
 
KV = ''' 

<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Welcome"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Welcome"

        OneLineListItem:
            text: "Oil Level Check"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Oil Level Check"

        OneLineListItem:
            text: "Power Steering Fluid Check"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Power Steering Fluid Check"
                         
        OneLineListItem:
            text: "Winshield Washer Fluid Check"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Winshield Washer Fluid Check"
                
        OneLineListItem:
            text: "Brake FLuid Check"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Brake FLuid Check"
                
        OneLineListItem:
            text: "Coolant Level Check"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Coolant Level Check"
        
        OneLineListItem:
            text: "Tire Pressure Check"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Tire Pressure Check"
          
MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "Basic Automotive Maintenance"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

      

        
    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "Welcome"

                Image:
                    source:"images/welcome.png"   
                    keep_ratio: True
               
            MDScreen:
                name: "Oil Level Check"
                              
                Image:
                    source:"images/oil.jpg"  
                    keep_ratio: True
                    
            MDScreen:
                name: "Power Steering Fluid Check"
                   
                Image:
                    source:"images/steering.jpg" 
                    keep_ratio: True
            
            MDScreen:
                name: "Winshield Washer Fluid Check"
                                
                Image:
                    source:"images/windshield.jpg" 
                    keep_ratio: True
               
            MDScreen:
                name: "Brake FLuid Check"              
                    
                Image:
                    source:"images/brake.jpg" 
                    keep_ratio: True
                    
            MDScreen:
                name: "Coolant Level Check"
              
                Image:
                    source: "images/coolant.jpg" 
                    keep_ratio: True
            
            MDScreen:
                name: "Tire Pressure Check"
                
                Image:
                    
                    source: "images/tire.jpg" 
                    keep_ratio: True
                    
                     

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

    MDTopAppBar:
        pos_hint: {"bottom": 1}
        elevation: 4
        
'''

class ContentNavigationDrawer(MDScrollView):
    Window.borderless = False
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class BAMAppApp(MDApp):
    
    def build(self): 
          
        self.theme_cls.primary_palette = "LightBlue" 
        self.theme_cls.theme_style = "Light"
        self.icon = "images/logo.png" 
        return Builder.load_string(KV)


BAMAppApp().run()


