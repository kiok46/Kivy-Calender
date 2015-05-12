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
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.event import EventDispatcher

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


# class for dates.kv file
class Dates(GridLayout):
    now = datetime.datetime.now()
    c  = calendar.monthcalendar(2015,5)
    def __init__(self,**kwargs):
        super(Dates,self).__init__(**kwargs)
        self.cols = 7
        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(Button(text = '{j}'.format(j='')))
                else:
                    self.add_widget(Button(text = '{j}'.format(j=j)))
            
    def get_month(self):
        pass


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
        self.title = "Kivy-Calender"
        self.load_kv('calender.kv')
        Clock.schedule_interval(self.update,1)
        return Calender()

# BoilerPlate
if __name__ =='__main__':
    app = mainApp()
    app.run()