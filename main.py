from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('months.kv')
Builder.load_file('dates.kv')
Builder.load_file('select.kv')
Builder.load_file('status.kv')

class calender(BoxLayout):
    pass

class dates():
    pass

class status():
    pass

class select():
    pass

class mainApp(App):
    def build(self):
        self.title = "Kivy-Calender"
        self.load_kv('calender.kv')
        return calender()
    
if __name__ =='__main__':
    app = mainApp()
    app.run()