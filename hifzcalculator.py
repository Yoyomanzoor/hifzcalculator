import datetime as dt
from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
import math

label_layout = widgets.Layout(width='100px',height='30px')

def ui():
    pages = 30*20
    lines = pages*15
    
    d0 = widgets.DatePicker(
        description='Start date',
        disabled=False
    )
    d1 = widgets.DatePicker(
        description='End date',
        disabled=False
    )
    init = widgets.BoundedFloatText(
        value=0,
        min=0,
        max=30,
        description='Number of ajza memorized:',
        disabled=False,
        style= {'description_width': 'initial'}
    )
    
    def f(start, end, init):
        if start and end:
            if start>=end:
                print("")
            else:
                delta = end-start
                remainder = (pages-(init*20))/delta.days
                print(f'Pages to memorize per day: {remainder}\nLines to memorize per day: {remainder*15}')
        else:
            print('select start and end dates')
    
    out = widgets.interactive_output(f, {'start':d0, 'end':d1, 'init':init})
    
    box1 = widgets.HBox([d0,d1])
    box2 = widgets.VBox([init, out])
    
    #####

    dayone = widgets.DatePicker(
        description='Start date',
        disabled=False
    )
    initial = widgets.BoundedFloatText(
        value=0,
        min=0,
        max=30,
        description='Number of ajza memorized:',
        disabled=False,
        style= {'description_width': 'initial'}
    )
    ppd = widgets.BoundedFloatText(
        value=1,
        min=0,
        max=600,
        description='Pages to memorize per day:',
        disabled=False,
        style= {'description_width': 'initial'}

    )
    lpd = widgets.BoundedFloatText(
        value=15,
        min=0,
        max=9000,
        description='Lines to memorize per day:',
        disabled=False,
        style= {'description_width': 'initial'}
    )
    perdaytab = widgets.Tab(children=[ppd,lpd])
    perdaytab.set_title(0, 'pages/day')
    perdaytab.set_title(1, 'lines/day')
    
    # l = widgets.link((ppd, 'value'), (lpd, 'value'))
    
    def change_a(_):
        lpd.value = ppd.value*15
    
    ppd.observe(change_a)
    
    daysoff = widgets.BoundedFloatText(
        value=0,
        min=0,
        max=6,
        description='Review days per week:',
        disabled=False,
        style= {'description_width': 'initial'}
    )
    
    
    def f2(start, init, ppd, lpd, daysoff):
        if start:
            remainder = lines-(init*20*15)
            daysleft = remainder/lpd
            adjusteddays = daysleft+(daysleft*(daysoff/7))
            completedate = start+dt.timedelta(days=adjusteddays)
            print(f'number of days left: {math.ceil(adjusteddays)}\nestimated completion date: {completedate.strftime("%m/%d/%Y")}')
        else:
            print('select a start date')
    
    out2 = widgets.interactive_output(f2, {'start':dayone, 'init':initial, 'ppd':ppd, 'lpd':lpd, 'daysoff':daysoff})
    
    pbox1 = widgets.HBox([perdaytab, widgets.VBox([dayone, initial])])
    pbox2 = widgets.VBox([daysoff, out2])
    
    
    #####
    
    tab2 = widgets.VBox([box1, box2])
    tab1 = widgets.VBox([pbox1, pbox2])
    
    tab = widgets.Tab(children=[tab1, tab2])
    tab.set_title(1, 'pages per day')
    tab.set_title(0, 'estimated completion date')
    return(widgets.VBox(children=[tab]))