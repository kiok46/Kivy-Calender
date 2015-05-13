# Project made by: Kuldeep Singh
# Student at LNMIIT,Jaipur,India

# import Statements
import calendar
import time
import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.event import EventDispatcher
from kivy.uix.textinput import TextInput

# Builder used to load all the kivy files to be loaded in the main.py file
Builder.load_file('months.kv')
Builder.load_file('dates.kv')
Builder.load_file('select.kv')
Builder.load_file('status.kv')
Builder.load_file('days.kv')

# class for calender.kv file
class Calender(BoxLayout):
    def __init__(self,**kwargs):
        super(Calender,self).__init__(**kwargs)
        
        

# ------------------------------------------------------------------------------------------------#


# class for status.kv file
class Status(BoxLayout,EventDispatcher):
    
    def __init__(self,**kwargs):
        super(Status,self).__init__(**kwargs)
        
        
        
        
# ------------------------------------------------------------------------------------------------#


# class for select.kv file
class Select(BoxLayout):
    
    n = ListProperty()
    year_1_ = ObjectProperty(None)
    year_2 = ObjectProperty(None)
    lbl_ = ObjectProperty(None)
    btn = ObjectProperty(None)
    global count
    
    def __init__(self,**kwargs):
        super(Select,self).__init__(**kwargs)
        self.count = 0 
    def get_years(self):
        if self.count == 0:
            for i in range(0,100):
                if i<10:
                    self.n.append('0'+str(i))
                else:
                    self.n.append(str(i))
        self.count = 1
        self.year_1_.values = self.n
        self.year_2.values = self.n


# ------------------------------------------------------------------------------------------------#


# class for Reminder in Dates
class Reminder(BoxLayout):
    def __init__(self,**kwargs):
        super(Reminder,self).__init__(**kwargs)
        
        self.orientation = 'vertical'
        self.add_widget(TextInput())
        self.b = BoxLayout(orientation = 'horizontal' , size_hint = (1,.15))
        self.add_widget(self.b)
        self.b.add_widget(Button(on_release = self.on_release,text = "OK!"))
        
    def on_release(self,event):
        print "OK clicked!"

# ------------------------------------------------------------------------------------------------#
'''
class get_months(GridLayout):
    def __init__(self,c,**kwargs):
        super(get_months,self).__init__(**kwargs)
        self.cols = 7
        self.c  = calendar.monthcalendar(2015,5)
        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(Button(on_release = self.on_release,text = '{j}'.format(j='')))
                else:
                    self.add_widget(Button(on_release = self.on_release, text = '{j}'.format(j=j)))
    
    def on_release(self,args):
        pass
        
        
'''
# class for dates.kv file
class Dates(GridLayout):
    now = datetime.datetime.now()
    
    
    def __init__(self,**kwargs):
        super(Dates,self).__init__(**kwargs)
        self.cols = 7
        self.c  = calendar.monthcalendar(2015,5)
        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(Button(on_release = self.on_release,text = '{j}'.format(j='')))
                else:
                    self.add_widget(Button(on_release = self.on_release, text = '{j}'.format(j=j)))
        
    def get_month(self):
        pass
    
    def on_dismiss(self, arg):
        # Do something on close of popup
        pass
    
    def on_release(self,event):
        print "date clicked :" + event.text
        event.background_color = 1,0,0,1
        self.popup = Popup(title= "Set Reminder :",
        content = Reminder(),
        size_hint=(None, None), size=(self.width*3/4, self.height))
        self.popup.bind(on_dismiss = self.on_dismiss)
        self.popup.open() 


# ------------------------------------------------------------------------------------------------#

# class for months.kv file
class Months(BoxLayout):
    def __init__(self,**kwargs):
        super(Months,self).__init__(**kwargs)


# ------------------------------------------------------------------------------------------------#


# mainApp class
class mainApp(App):
    time = StringProperty()
    
    def update(self,*args):
        self.time = str(time.asctime())
        
    def build(self):
        self.title = "Kivy-Calendar"
        self.load_kv('calender.kv')
        Clock.schedule_interval(self.update,1)
        return Calender()

# BoilerPlate
if __name__ =='__main__':
    app = mainApp()
    app.run()