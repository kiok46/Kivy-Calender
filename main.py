# Project made by: Kuldeep Singh
# Student at LNMIIT,Jaipur,India

# import Statements
import calendar
import time
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
        self.status = Status()
        self.up = Status(_change = self.status._change)
        self.status.bind(_change=self.setter('value'))
        
        

# ------------------------------------------------------------------------------------------------#


# class for status.kv file
class Status(BoxLayout,EventDispatcher):
    
    _change = StringProperty('')
    _tnd = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Status,self).__init__(**kwargs)
        
    def update(self,*args):
        self.time = time.asctime()
        self._change = str(self.time)
        print self.time
        
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
        self.d = Dates()
        self.p = self.sp.year_1_.text
        self.q = self.sp.year_2.text
        self.r = self.p+self.q
        self.r = int(self.r)
        self.c  = calendar.monthcalendar(0000,5)
        for i in self.c:
            for j in i:
                if j == 0:
                    self.add_widget(Button(text = '{j}'.format(j='')))
                else:
                    self.add_widget(Button(text = '{j}'.format(j=j)))


# ------------------------------------------------------------------------------------------------#

# class for months.kv file
class Months(BoxLayout):
    def __init__(self,**kwargs):
        super(Months,self).__init__(**kwargs)


# ------------------------------------------------------------------------------------------------#


# mainApp class
class mainApp(App):
    def build(self):
        self.title = "Kivy-Calender"
        self.load_kv('calender.kv')
        _get_date = Status()
        Clock.schedule_interval(_get_date.update,1)
        return Calender()

# BoilerPlate
if __name__ =='__main__':
    app = mainApp()
    app.run()