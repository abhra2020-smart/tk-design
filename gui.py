import tkinter


def make_gui(parent):
    sidebar = tkinter.Frame(parent, width=250, bg='grey', height=500, borderwidth=2)
    sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
    gap = tkinter.Label(sidebar, text='\n\n\n\n\n\n\n\n\n', background='grey')
    gap.pack()
    labels = tkinter.Label(sidebar, text='\t  Labels \t\t', background='#7b777d')
    labels.pack()
    label = tkinter.Label(sidebar, text='\t   Label\t\t', background='#7b777d')
    label.pack()
    gap3 = tkinter.Label(sidebar, text='\n', background='grey')
    gap3.pack()
    buttons = tkinter.Label(sidebar, text='\t Buttons\t\t', background='#7b777d')
    buttons.pack()
    button = tkinter.Label(sidebar, text='\t Button\t\t', background='#7b777d')
    button.pack()
    topbar = tkinter.Frame(parent, width=300, bg='lightgrey', height=125, borderwidth=2)
    topbar.pack(expand=False, fill='both', side='top', anchor='nw')
