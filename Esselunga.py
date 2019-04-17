# -*- coding: utf-8 -*-
"""
Created on Wed Mar 06 17:13

@author: Ehsan Hosseini
Firma: RATIONAL AG
Projekt: Auswertung Italien Esselunga
Arbeitspacket: 09
Task: Diagramm entwerfen
"""

# supress warnings message
import warnings;

warnings.simplefilter("ignore");
warnings.filterwarnings("ignore")

import inspect
import math

import os, sys

import numpy as np
import pandas as pd
import tkinter as tk
#import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
#import urllib

# replace inf values with 0
math.inf
pd.describe_option("use_inf_as_null")
# for each df with inf values -> df = df.replace(np.inf,0)

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
#import xlwt
#from xlwt import Workbook
# import easygui as eg
from math import *
from datetime import datetime
#from datetime import timedelta
#from itertools import groupby
#from collections import Counter
#from collections import namedtuple
#from matplotlib.ticker import MaxNLocator
from matplotlib import style
#from pandas import read_csv
from pandas import Series
from matplotlib import pyplot
#from time import sleep

# Scipy.org Linear Algebra Matrix and Vectors
from scipy.linalg import norm

#   string pattern recognition
import re

# convert str to int
import ast

# Machine Learning
from sklearn.feature_selection import SelectKBest  # feature selection Univariate selection
from sklearn.feature_selection import chi2  # Univariate selection chi squered

from statsmodels.tsa.stattools import adfuller  # Manually configuring ARIMA
from statsmodels.graphics.tsaplots import plot_acf  # plot ACF(Autocorrelation function)
from pandas.plotting import autocorrelation_plot  # autocorrelation plot of time series
from statsmodels.graphics.tsaplots import plot_pacf  # plot PACF(Partial Autocorrelation function)
from statsmodels.tsa.arima_model import ARIMA  # ARIMA model
from sklearn.metrics import mean_squared_error  # mse
from statsmodels.tsa.arima_model import ARIMAResults

# Decision-Tree Regression
# Combine Models into Ensemble Predictions Bagging Algorithms
# Random Forest Classification

# Bossting Algorithms
# AdaBoost Classification
# Stochastic Gradient Boosting
# Bagging Classification
# Extra Trees

#path = os.path.abspath(__file__)
#dir_path = os.path.dirname(path)
#sys.path.append('/')
#sys.path.extend('./')
#os.path.join('/')
import sys; print('Python %s on %s' % (sys.version, sys.platform))
#sys.path.extend(['C:\\Users\\hoeh\\PycharmProjects\\SAP_import_daten', \
#                 'C:/Users/hoeh/PycharmProjects/SAP_import_daten', \
#                 'C:/Users/hoeh/PycharmProjects/SAP_import_daten/pack/'])
#from serviceCall import ServiceCall

#from serviceCall import Service_call # class Service_call -> to draw a diagramm for Esselunga Italien
#service_call = Service_call()

#from .serviceCall import Service_call
#from venv.serviceCall import Service_call
#from .venv import Service_call
#from pack.serviceCall import ServiceCall
#from pack.serviceCall import ServiceCall



# monkey patch around bug in ARIMA class
def __getnewargs__(self):
    return ((self.endog), (self.k_lags, self.k_diff, self.k_ma))


ARIMA.__getnewargs__ = __getnewargs__

# tensorflow libraries(Neural network)
import tensorflow as tf
from tensorflow.keras import layers

# import warnings filters try Exception warnings ignoring
np.warnings.filterwarnings("ignore")
np.warnings.resetwarnings()
np.seterr(divide='ignore')
np.seterr(all='ignore')

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def calender(string_var, str_var_limit_year, str_var_limit_month, flag_year):
    import calendar

    cal = tk.Tk()
    cal.geometry("350x350")
    cal.wm_title("calendar")

    # entry_year = ttk.Entry(cal)
    # entry_year.pack()

    def callback_year(event):
        calender.year = event.widget.get()  # get year

        # reset limit_month
        if (flag_year == True) and (calender.year > str_var_limit_year.get()):
            str_var_limit_month.set(1)

        if calender.year > str_var_limit_year.get():
            calender.combobox_month.config(value=[*range(1, 13)])

        date = event.widget.get()  # get date
        date = datetime.strptime(date, "%Y")  # format date

        calender.year = date.year  # get year of formated date
        calender.month = date.month  # get month of formated date

        print("year in callback_year of func calender  = ", calender.year)

        if flag_year == True:
            str_var_limit_year.set(calender.year)  # set limit_year of caller class

    def callback_show(event):
        # year= entry_year.get()
        # month= entry_month.get()

        month = event.widget.get()

        if flag_year == True:
            str_var_limit_month.set(month)  # set limit_month of caller class

        year = calender.year
        print("year = ", year)
        print("month = ", month)
        cal_x = calendar.month(int(year), int(month), w=2, l=1)
        print("cal_x", cal_x)
        cal_out = tk.Label(cal, text=cal_x, font=('courier', 12, 'bold'), bg='lightblue')
        cal_out.pack(padx=3, pady=10)
        global year_month_str
        year_month_str = str(year) + '.' + str(month)
        print("year_month_str = ", year_month_str)

    # year
    label_year = ttk.Label(cal, text="year:")
    label_year.pack()

    #   assign limit_year
    limit_year = str_var_limit_year.get()  # get date year
    limit_year = datetime.strptime(limit_year, "%Y")  # format year
    limit_year = limit_year.year  # get year of formated date

    # limit_year is according to last field_date from caller class and by default equal 2009, limited by fertigung_start, must be greater than fertigung_start
    combobox_year = ttk.Combobox(cal, values=[*range(limit_year, current_year + 1)], state='readonly', width=7)
    combobox_year.bind('<<ComboboxSelected>>', callback_year)
    combobox_year.current(0)
    combobox_year.pack()

    # assign limit_month
    limit_month = str_var_limit_month.get()  # get date month
    limit_month = datetime.strptime(limit_month, "%m")  # format month
    limit_month = limit_month.month  # get month of formated date
    # month
    label_month = ttk.Label(cal, text="month:")
    label_month.pack()
    calender.combobox_month = ttk.Combobox(cal, values=[*range(limit_month, 13)], state='readonly', width=5)
    calender.combobox_month.bind('<<ComboboxSelected>>', callback_show)
    calender.combobox_month.current(0)
    calender.combobox_month.pack()

    # entry_month = ttk.Entry(cal)
    # entry_month.pack()

    # callback_show func

    def callback_submit():
        string_var.set(year_month_str)
        cal.destroy()

    # button_show = ttk.Button(cal, text="show date", command=callback_show)
    # button_show.pack()

    button_Ok = ttk.Button(cal, text="Submit Date", command=callback_submit)
    button_Ok.pack()

    cal.mainloop()


def animate(df, field_name):
    Meldungen, Equipments, MTFF, df = func_MTFF_nach_X(df_filter_XY, field_name,
                                                       failure_start_field_name=str('Störungsbeginn (Dat)_punkt'))
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    # a.plot(df_Geraete_große_temp)
    a.clear()
    a.plot(df.index, df.iloc[:, 0:1], "#00A3E0", label="Days")
    a.plot(df.index, df.iloc[:, 1:2], "#183A54", label="Count")
    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
    a.set_title('Bar_chart ' + field_name)
    a.set_xlabel(field_name)


def view_chart(caller, df, field_name):
    columns = df.columns
    Meldungen, Equipments, MTFF, df = func_MTFF_nach_X(df_filter_XY, field_name,
                                                       failure_start_field_name=str('Störungsbeginn (Dat)_punkt'))
    df.columns = columns

    # erste 5 kritische baugruppen falls field_name Baugruppe ist
    if field_name == str('Baugruppe'):
        df = PageOne.manipulate_df_BauGr(caller, df)

    fieldName = field_name

    # fig, ax = plt.subplots()
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    ax.clear()
    index = df.index
    ind = np.arange(len(df))  # the x locations for the groups
    bar_width = 0.45  # the width of the bars

    mean = df['F_t_Fail_time_days']  # mean = df.iloc[: , 0:1].values

    count = df['count']  # count = df.iloc[: , 1:2].values

    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = ax.bar(ind, mean, bar_width, alpha=opacity, color='b', error_kw=error_config, label='Mean time to failure')
    rects2 = ax.bar(ind + bar_width, count, bar_width, alpha=opacity, color='r', error_kw=error_config,
                    label='number of Equipment')

    # fig.set_figwidth(7) # set figure width
    # fig.set_figheight(5) # set figure height
    # add some  text for lables, title and axes ticks
    ax.set_xlabel(fieldName)
    ax.set_ylabel('amount')
    ax.set_title('Mean time to first Failure by' + fieldName)
    ax.set_xticks(ind + bar_width / 2)  # + bar_width / 2
    ax.set_xticklabels(index)
    ax.legend()

    fig.tight_layout()

    def autolable(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center', va='bottom')

    autolable(rects1)
    autolable(rects2)
    # plt.show()

    canvas = FigureCanvasTkAgg(fig, caller)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, caller)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Rational(tk.Tk):
    def __init__(self, *args,
                 **kwargs):  # * collects all the positional arguments in a tuple(list). ** collects all the keyword arguments in a dictionary.
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "RATIONAL AG")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Home Page", command=lambda: self.show_frame(StartPage))
        # filemenu.add_command(label="Save setting", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_command(label="Export filter",
                             command=lambda: self.action_save(title="Please select a file name for saving:",
                                                              as_file=True))
        filemenu.add_separator()
        filemenu.add_command(label="import Excel",
                             command=lambda: self.action_import_xlsx(title="Please select a file name to importing"))
        filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=quit)
        filemenu.add_command(label="Exit", command=lambda: self.action_exit())
        menubar.add_cascade(label="File", menu=filemenu)

        filtermenu = tk.Menu(menubar, tearoff=1)
        # filtermenu.add_command(label="nach Land", command=lambda: func_filter_nach_X(df_sorted,))
        filtermenu.add_command(label="nach Land", command=lambda: self.show_frame(PageOne))
        filtermenu.add_command(label="nach Baugruppe", command=lambda: self.show_frame(PageTwo))
        filtermenu.add_command(label="nach Ketten", command=lambda: self.show_frame(PageThree))
        filtermenu.add_command(label="nach Geräte_Große", command=lambda: self.show_frame(PageFour))
        filtermenu.add_command(label="nach Equipment", command=lambda: self.show_frame(PageFive))
        menubar.add_cascade(label="Graph", menu=filtermenu)

        callendarmenu = tk.Menu(menubar, tearoff=1)
        callendarmenu.add_command(label="show callendar", command=lambda: self.show_frame(Calender))
        menubar.add_cascade(label="callendar", menu=callendarmenu)

        evaluationmenu = tk.Menu(menubar, tearoff=1)
        evaluationmenu.add_command(label="Service call", command=lambda: self.show_frame(ServiceCall))
        menubar.add_cascade(label="evaluation", menu=evaluationmenu)
        evaluationmenu.add_separator()


        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (ServiceCall, StartPage, Calender, PageOne, PageTwo, PageThree, PageFour, PageFive):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def popupmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title("RATIONAL!")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def action_import_xlsx(self, title=None, file_name=None, dir_name=None, file_Ext=".xlsx", file_types=None,
                           reset_index=True):
        file = filedialog.askopenfilename(filetypes=[('Excel files', '.xlsx')])
        if file:
            try:
                data = load_excelFile_all_sheets(file, reset_index=reset_index)
                print(data.head(5))
                messagebox.showinfo('Importing Data', 'importing excel Completed!')
            except NameError as e:
                messagebox.showerror('Error importing Excel Data', 'Unable to import file: %r' % file)

        return True

    # file_Ext = file extension
    def action_save(self, title=None, file_name=None, dir_name=None, file_Ext=".xlsx", file_types=None, as_file=False):
        # self.topLevel.update_idletasks()
        if file_types is None:
            # build a list of tuples for each file type the file dialog should display
            file_types = [('all files', '*.*'), ('text files', '*.txt'), ('python files', '*.py'),
                          ('excel files', '*.xlsx'), ('json files', '*.JSON')]

        # define options
        options = {}
        options['defaultextension'] = file_Ext
        options['filetypes'] = file_types
        options['initialdir'] = os.getcwd()
        options['initialfile'] = file_name
        options['title'] = title

        if messagebox.askokcancel('Save Option', 'Save Data?'):
            '''
            # ask to select folder
            answer = filedialog.askdirectory(parent=self, initialdir=os.getcwd(), title="Please select a folder:")
            # ask to select file
            answer = filedialog.askopenfilename(parent=self, initialdir=os.getcwd(), title="Please selcet a file:", filetypes=file_types)
            # ask to select one or more file names
            answer = filedialog.askopenfilenames(parent=self, initialdir=os.getcwd(), title="Please select one or more files:", fieltypes=file_types)
            # '''

            '''
            # ask to select a single file name for saving
            #answer = filedialog.asksaveasfilename(parent=self, initialdir=os.getcwd(), title="Please select a file name for saving:", filetypes=file_types)
            if as_file:
                file = filedialog.asksaveasfilename(parent=self, **options)

                if answer is None: # asksaveasfilename return None if Dialog closed with "cancel".
                    return


                if file_name.endswith('.xlsx'):
                    try:
                        #with open (file_name, 'w') as out_file:
                        write_to_excel(df_filter_XY, answer.initialdir, answer.filename, str(answer))                                        
                    except Exception as e:
                        messagebox.showerror('Error Saving Data', 'Unable to open file: %r' % answer)
            #'''
            file = filedialog.asksaveasfilename(filetypes=[('excel files', '*.xlsx')])
            print('file-> save aktion : %r ' % file)
            if file:
                try:
                    # document = Workbook()
                    # insert_sheet = document.add_sheet('Sheet_01')
                    # change = insert_sheet.set_portrait(False)
                    # data = df_filter_XY.copy(deep=True)
                    (directory, file_name) = os.path.split(file)
                    directory = directory + '/'
                    print("path -> %r " % directory)
                    print("file_name -> %r " % file_name)

                    write_to_excel(df_filter_XY, directory, str(file_name) + '.xlsx', "Sheet_01")
                    messagebox.showinfo('save Data', 'saving excel completed')
                    # savefile = filedialog.asksaveasfilename(mode="w", filetypes = file_types)
                    # document.save(str(file)+".xlsx")
                    print(str(file) + ".xlsx")
                    '''
                    if (file is not None) and (len(file)!=0):
                        #document.save(str(file)+".xlsx")
                        #data_file = open(file, "w")
                        (path, file_name) = os.path.split(file)
                        print("path -> %r " % path)
                        print("file_name -> %r " % file_name)
                        write_to_excel(data, path, file_name, "Sheet_01")
                        #data_file.close()
                    '''
                except Exception as e:
                    messagebox.showerror('Error Saving Data', 'Unable to save file: %r' % file)
        return True

    def action_exit(self):
        if messagebox.askyesno('Exit App', 'Really Exit?'):
            Rational.destroy(self)

class ServiceCall(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Service Call Esselunga Italien", font=LARGE_FONT)
        label.pack(side='top')
        button2 = ttk.Button(self, text="Import source Excel Data", command=lambda: self.action_import_xlsx(title='Please select a filename to importing!'))
        button2.pack()
        button3 = ttk.Button(self, text="Back to Home", command=lambda: PageThree.back_home(self, controller, self.canvas, self.toolbar))#controller.show_frame(StartPage))
        button3.pack()
        button4 = ttk.Button(self, text="View Bar Chart Land",
                             command=lambda:  self.call_viewer())#self.view_chart(df_land_temp, field_name=str('Land')))
        button4.pack()
        self.path = data_path

    def view_chart(self, df=None, field_name=None):
        df = self.evaluation_service_call()
        '''
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.clear()
        a.plot(df)
        a.plot(df.index, df.iloc[: , 0:1] , "#00A3E0", label="Days")
        a.plot(df.index, df.iloc[: , 1:2] , "#183A54", label="Count")
        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
        a.set_title('Bar_chart ' + field_name)
        a.set_xlabel(field_name)
        '''
        # df = df_Geraete_große.copy(deep=True)
        # fieldName = 'Geräte_große'
        #fieldName = field_name

        # fig, ax = plt.subplots()

        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)

        ax.clear()

        #line_1, = ax.plot(df['Wear_and_Tear'], color='red', label='Wear & Tear [€]', linestyle='--')
        #line_2, = ax.plot(df['Serviceparts'], color='blue', label='Serviceparts [€]')
        #line_3, = ax.plot(df['Technician'], color='green', label='Technician/labour [€]', linewidth='2')

        # Legends if existence in Data
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)

        index = df.index
        ind = np.arange(len(df))  # the x locations for the groups
        bar_width = 0.25  # the width of the bars

        wear_and_tear = df['Wear_and_Tear']

        serviceparts = df['Serviceparts']

        technician = df['Technician']

        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        rects1 = ax.bar(ind, wear_and_tear, bar_width, alpha=opacity, color='g', error_kw=error_config,
                        label='Wear & Tear [€]')
        rects2 = ax.bar(ind + bar_width, serviceparts, bar_width, alpha=opacity, color='r', error_kw=error_config,
                        label='Serviceparts [€]') # ind + bar_width
        rects3 = ax.bar(ind + bar_width*2, technician, bar_width, alpha=opacity, color='b', error_kw=error_config,
                        label='Technician/labour [€]') # ind + bar_width*2

        # fig.set_figwidth(7) # set figure width
        # fig.set_figheight(5) # set figure height
        # add some  text for lables, title and axes ticks
        ax.set_xlabel('Unit age [y]')
        ax.set_ylabel('cost of servicecall [€]')
        ax.set_title('Auswertung Esselunga Italien :)')
        ax.set_xticks(ind + bar_width / 2)  # + bar_width / 2
        ax.set_xticklabels(index, rotation=10)  # rotation=x degree set rotation for ticks
        ax.legend()

        fig.tight_layout()

        def autolable(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center',
                        va='bottom')

        autolable(rects1)
        autolable(rects2)
        autolable(rects3)
        # plt.show()

        # global canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # global toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        return canvas, toolbar

    def call_viewer(self):
        self.canvas, self.toolbar = ServiceCall.view_chart(self)

    def action_import_xlsx(self, title=None, file_name=None, dir_name=None, file_Ext=".xlsx", file_types=None,
                           reset_index=True):
        file = filedialog.askopenfilename(filetypes=[('Excel files', '.xlsx')])
        if file:
            try:
                (directory, file_name) = os.path.split(file)
                directory = directory + '/'
                print("path -> %r " % directory)
                print("file_name -> %r " % file_name)
                sheetnames = {'s1': 'Wichtig', 's2': 'List of ServiceCalls', 's3': 'Tabelle1', 's4': 'Parts',
                                 's5': 'Breakdown', 's6': 'Maintenance'}
                self.ls_dfs = service_call_import_daten(path= directory, filename= file_name, **sheetnames)
                print("serviceCall Esselunga", self.ls_dfs[0].shape)
                messagebox.showinfo('Importing Data', 'importing excel Completed!')
            except NameError as e:
                messagebox.showerror('Error importing Excel Data', 'Unable to import file: %r' % file)
                #vars()['df_0'] = str(cnt) to change variable values
        return True

    def evaluation_service_call(self):
        df_2 = self.ls_dfs[2] # ls_dfs[2] -> Tabelle1
        # ls_dfs[0] -> Wichtig, ls_dfs[1] ->List of ServiceCalls
        # Check if a columns exist in pandas df:
        if 'Gerätealter [y] Ende Service' not in df_2:
            try:
                df_2['Gerätealter [y] Ende Service'] = df_2['Gerätealter [m]'] // 12
            except NameError as e:
                print("There is no column name -> 'Gerätealter [m]' ")

        fields = ['ID', 'Serial number', 'Gerätealter [y] Ende Service', 'Positions Part number', 'Net Total [€]']
        df_tmp = df_2.groupby(fields).size().reset_index(name='count')
        df_tmp['Net Total [€]'][(df_tmp['Gerätealter [y] Ende Service'] == 0)].sum(0) # Service Kosten in erstes Jahr
        df_total = df_tmp.groupby(['Gerätealter [y] Ende Service']).agg({'Net Total [€]': 'sum'})

        wear_and_tear = [
            '16.01.526',
            '16.01.662',
            '24.00.149',
            '24.00.187',
            '40.00.093',
            '40.00.094',
            '40.03.994',
            '50.00.303',
            '20.00.398P',
            '20.00.399P',
            '20.02.549P',
            '20.02.550P',
            '20.02.551P',
            '20.02.552P',
            '20.02.553P',
            '24.00.142',
            '24.00.142P',
            '24.00.194',
            '24.02.959',
            '24.02.990',
            '24.03.190',
            '24.03.192',
            '3024.0201P',
            '40.00.091',
            '40.00.091S',
            '40.02.684',
            '40.04.771',
            '60.72.428',
            '60.72.429',
            '60.72.556',
            '60.74.403',
            '87.00.085',
            '87.00.086',
            '87.00.605',
            '10.00.675',
            '20.00.992',
            '20.00.993',
            '40.00.091V']

        df_wear_and_tear = pd.DataFrame(wear_and_tear)
        df_out = pd.DataFrame()
        for item in df_wear_and_tear[0]:
            df_out = df_out.append(df_2[(df_2['Positions Part number'] == str(item))])

        #df_2[(df_2['Positions Part number'] == [str(x) for x in df_wear_and_tear[0]])] # ValueError: Arrays were different lengths: 16916 vs 38

        df_total['Wear_and_Tear'] = df_out.groupby(['Gerätealter [y] Ende Service']).agg({'Net Total [€]': 'sum'})
        # Technician
        ls_technicia = list()
        for item in range(len(df_2)):
            var = df_2['Positions Part number'][item]
            var = str(var)
            if var[0:2].isalpha() == True: # first two charachter are string
                ls_technicia.append(var) # collect Baugruppen with first two char if is alphabet that also are worktime

        df_tmp = df_2[(df_2['Positions Part number'].str[0:4] == '9999')]# .groupby(['Gerätealter [y] Ende Service']).agg({'Net Total [€]': 'sum'})
        df_tmp = df_tmp.append(df_2[(df_2['Positions Part number'].isin(ls_technicia))] )
        df_total['Technician'] = df_tmp.groupby(['Gerätealter [y] Ende Service']).agg({'Net Total [€]': 'sum'})

        df_total = df_total.fillna(0) # remove nan values from result of aggregate

        df_total['Serviceparts'] = df_total['Net Total [€]'] - (df_total['Wear_and_Tear'] + df_total['Technician'])

        return df_total

    def join_service_call_data(self, ls_dfs):
        df_joint = pd.DataFrame()
        for df in ls_dfs:
            if df_joint.empty:
                df_joint = df
            else:
                df_joint = df_joint.join(df.set_index('ID'), on='ID', how='left', rsuffix='_K')
        return df_joint

    def laender_code(self):
        ls_filenames = self.import_files()
        file_name_laendercode = self.pattern_recognize(ls_filenames, 'Laender')  # recognize filename
        df_laender_code = load_excelFile_all_sheets(file_name=file_name_laendercode, reset_index=False)
        df_iso_code = pd.DataFrame()
        df_iso_code['Land'] = df_laender_code['LANDX']
        df_iso_code['iso_code_land'] = df_laender_code['INTCN3']
        df_iso_code['AB_Land'] = df_laender_code['INTCA']
        return df_iso_code

    def import_files(self, path=None, ext=None):
        # ext is file extension
        #progress.join()
        import os
        import glob
        if path is None:
            path = self.path
        if ext is None:
            ext = 'xlsx'
        try:
            filenames = glob.glob(path + '*[*a-z*A-Z0-9*_]*' + '.' + ext)
            ls_filenames = list()
            for data in range(len(filenames)):
                #progress.__reduce__()
                (dir_path, filename) = os.path.split(filenames[data])
                ls_filenames.append(filename)
                print("Detected Excel data: \n '{}' \n in input path: \n '{}' ".format(filename, path))
        except NameError as e:
            print("Destination {} or extension {} does not found".format(path, ext))
        print("Filenames importing completed!")
        return ls_filenames

    def pattern_recognize(self, ls_filenames, pattern):
        #progress.join()
        for filename in range(len(ls_filenames)):
            reg_exp = re.compile(r'(.*)'+pattern+r'(.*)')
            find_string = re.search(reg_exp, ls_filenames[filename])
            if find_string:
                return find_string.string
        if find_string is None:
            print("Pattern '{}' or filename '{}' does not found!".format(pattern, pattern))
            return False


    def decoding_values(self, df, decode_fieldname, df_iso_code, iso_code_fieldname):
        df_laender_iso_code = self.laender_code()
        #TODO umformatieren Laender mit ISO code -> zwei Ansatz: 1. Join , 2. ersetzung durch Loopschleife

        # 1. Ansatz:
        df = df.reset_index() # reset indexes to set this from 0 to end beacause of for loop
        for item in range(len(df)):
            df['Land'][item] = [df_laender_iso_code['iso_code_land'][x] for x in
                                    df_laender_iso_code[(df_laender_iso_code['Land'] == str(df['Land'][item]))].index]

        df['Land'] = df['Land'].str.get(0) #  convert each columns value to value remove square bracket [] from values

        # 2. Ansatz:
        df = df.join(df_laender_iso_code.set_index('Land'), on='Land', how='left', rsuffix='_iso')
        df = df.drop(columns='AB_Land') # drop Laender Abkurzung
        df['Land'] = df['iso_code_land'] # Ersetzung 'Land' durch 'iso_code_land'
        df = df.drop(columns='iso_code_land') # drop 'iso_code_land'
        return df


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=(""" Mean Time to First Failure """), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # global df_filter_XY
        # df_filter_XY = df_sorted.copy(deep=True)
        # df_filter_XY = pd.DataFrame()

        '''
        #initialize df_temp_s
        df_land_temp = pd.DataFrame()
        df_ketten_zeich_temp = pd.DataFrame()
        df_Geraete_große_temp = pd.DataFrame()
        df_Baugruppe_temp = pd.DataFrame()
        '''

        # df_land_temp = df_ketten_zeich_temp = df_Geraete_große_temp = df_Baugruppe_temp = pd.DataFrame()

        self.ls_children = list()
        self.ls_children = ['Land', 'ketten_zeich', 'Geräte_große', 'Baugruppe', 'Equipment']

        # button = ttk.Button(self, text="Graph nach Land", command=lambda: controller.show_frame(PageOne.view_chart(self, df_land, field_name=str('land_test_view'))))
        button_filter = ttk.Button(self, text="Filter Anwenden", command=lambda: self.call_func_filterXY())
        button_filter.pack()
        self.widget_set_position(button_filter, button_filter, 750, False, 40, True)  # widget set position an Form

        button_reset = ttk.Button(self, text="Reset", command=lambda: self.reset_func(ls_laender))  # reset Button
        # button_reset.grid(row=1, column=1)
        button_reset.pack(side='left', padx=5, pady=5)
        button_reset.place(x=10, y=10)

        self.ls_selected_countries = list()
        self.ls_selected_ketten = list()
        self.ls_selected_geraete_große = list()
        self.ls_selected_baugruppe = list()

        ''' Component Land '''
        ls_laender = list()
        for item in df_land.index:
            ls_laender.append(item)

        label_land = tk.Label(self, text="choose Country")
        label_land.pack()
        self.widget_set_position(button_reset, label_land, 10, False, 45, True)  # widget set position an Form
        # label_land.place(x=15, y=20)

        self.v_land = tk.StringVar()  # a string variable to hold user selection
        combobox_land = ttk.Combobox(self, textvariable=self.v_land, values=ls_laender,
                                     postcommand=self.updtlistbox_ketten)
        combobox_land.pack()
        self.widget_set_position(label_land, combobox_land, 10, False, 70, True)  # widget set position an Form
        # combobox_land.place(x=15, y = 25)
        combobox_land.current(0)
        combobox_land.bind("<<ComboboxSelected>>", self.callback_land)

        label_laender = tk.Label(self, text="selected Countries:")
        label_laender.pack()
        self.widget_set_position(combobox_land, label_laender, 10, False, 90, True)  # widget set position an Form
        # label_laender.place(x=15, y = 30)

        self.str_var_listbox_land = tk.StringVar(
            value=self.ls_selected_countries)  # option value=my_list ist optional no ncessary->initial values
        self.str_var_listbox_land.set(
            self.ls_selected_countries)  # StringVar str_var_listbox_land associated(fill) with str_var_listbox_land
        self.listbox_land = tk.Listbox(self, listvariable=self.str_var_listbox_land)
        self.listbox_land.pack()
        self.widget_set_position(label_laender, self.listbox_land, 10, False, 110, True)  # widget set position an Form
        # self.listbox_land.place(x=15, y=35)

        # self.listbox_land.insert(tk.END, combobox_land.get())
        # for i in range(len(ls_laender)):
        #    listbox_land.insert(tk.END, ls_laender[i])

        ''' component ketten '''
        self.ls_ketten = list()
        for item in df_ketten_zeich.index:
            self.ls_ketten.append(item)

        label_kette = tk.Label(self, text="choose Kette", bg="pink", fg="white")
        label_kette.pack()
        self.widget_set_position(button_reset, label_kette, 200, False, 45, True)  # widget set position an Form

        self.v_ketten = tk.StringVar()
        self.combobox_ketten = ttk.Combobox(self, textvariable=self.v_ketten, values=self.ls_ketten, state='readonly')
        self.combobox_ketten.pack()
        self.widget_set_position(button_reset, self.combobox_ketten, 200, False, 70,
                                 True)  # widget set position an Form
        self.combobox_ketten.current(0)
        self.combobox_ketten.bind("<<ComboboxSelected>>", self.callback_ketten)

        label_ketten = tk.Label(self, text="selected Ketten")
        label_ketten.pack()
        self.widget_set_position(button_reset, label_ketten, 200, False, 90, True)  # widget set position an Form

        self.scrollbar = tk.Scrollbar(self, orient='vertical')
        self.str_var_listbox_ketten = tk.StringVar(
            value=self.ls_selected_ketten)  # option value=my_list ist optional->initial values
        self.listbox_ketten = tk.Listbox(self, listvariable=self.str_var_listbox_ketten
                                         , yscrollcommand=self.scrollbar.set
                                         ,
                                         selectmode=tk.EXTENDED)  # StringVar associated with a listbox's listvariable option
        self.str_var_listbox_ketten.set(
            self.ls_selected_ketten)  # StringVar str_var_listbox_ketten associated(fill) with str_var_listbox_ketten
        self.scrollbar.config(command=self.listbox_ketten.yview)
        self.listbox_ketten.pack()
        self.widget_set_position(button_reset, self.listbox_ketten, 200, False, 110,
                                 True)  # widget set position an Form

        ''' component Geräte_Große '''
        self.ls_geraete_große = list()
        for item in df_Geraete_große.index:
            self.ls_geraete_große.append(item)

        label_geraete_große = tk.Label(self, text="choose Device size", bg="blue", fg="white")
        label_geraete_große.pack()
        self.widget_set_position(button_reset, label_geraete_große, 400, False, 45, True)  # widget set position an Form

        self.v_geraete_große = tk.StringVar()
        self.combobox_geraete_große = ttk.Combobox(self, textvariable=self.v_geraete_große,
                                                   values=self.ls_geraete_große, state='readonly')
        self.combobox_geraete_große.current(0)
        self.combobox_geraete_große.bind("<<ComboboxSelected>>", self.callback_geraete_große)
        self.widget_set_position(button_reset, self.combobox_geraete_große, 400, False, 70,
                                 True)  # widget set position an Form

        label_geraeten_großen = tk.Label(self, text="selected Device size")
        label_geraeten_großen.pack()
        self.widget_set_position(button_reset, label_geraeten_großen, 400, False, 90,
                                 True)  # widget set position an Form

        self.str_var_listbox_geraete_große = tk.StringVar()
        self.listbox_geraete_große = tk.Listbox(self, listvariable=self.str_var_listbox_geraete_große)
        self.str_var_listbox_geraete_große.set(self.ls_selected_geraete_große)
        self.widget_set_position(button_reset, self.listbox_geraete_große, 400, False, 110,
                                 True)  # widget set position an Form

        ''' component Baugruppe '''
        self.ls_baugruppe = list()
        for item in df_Baugruppe.index:
            self.ls_baugruppe.append(item)

        label_baugruppe = tk.Label(self, text="choose module", bg="green", fg="white")
        label_baugruppe.pack()
        self.widget_set_position(button_reset, label_baugruppe, 600, False, 45, True)  # widget set position an Form

        self.v_baugruppe = tk.StringVar()
        self.combobox_baugruppe = ttk.Combobox(self, textvariable=self.v_baugruppe, values=self.ls_baugruppe,
                                               state='readonly')  # für die änderungen on combobox reicht es combobox.config(values=new values)
        self.combobox_baugruppe.current(0)
        self.combobox_baugruppe.bind("<<ComboboxSelected>>", self.callback_baugruppe)
        self.widget_set_position(button_reset, self.combobox_baugruppe, 600, False, 70,
                                 True)  # widget set position an Form

        label_baugruppen = tk.Label(self, text="selected modules")
        label_baugruppe.pack()
        self.widget_set_position(button_reset, label_baugruppen, 600, False, 90, True)  # widget set position an Form

        self.str_var_listbox_baugruppe = tk.StringVar()
        self.listbox_baugruppe = tk.Listbox(self, listvariable=self.str_var_listbox_baugruppe)
        self.str_var_listbox_baugruppe.set(
            self.ls_selected_baugruppe)  # immer is set to ls_selected_baugruppe, bei änderungen in ls_selected_baugruppe wirkt automatisch on diese StringVar
        self.widget_set_position(button_reset, self.listbox_baugruppe, 600, False, 110,
                                 True)  # widget set position an Form

        ''' MTFF Infos '''
        label_MTFF = tk.Label(self, text=("MTFF(days): "), font=NORM_FONT)
        # label_MTFF.place(y=150, x=50)
        # label_MTFF.pack(side='right')
        self.widget_set_position(button_reset, label_MTFF, 900, False, 30, True)  # widget set position an Form
        self.str_var_entry_MTFF = tk.IntVar()
        self.entry_MTFF = tk.Entry(self, textvariable=self.str_var_entry_MTFF, justify='center', state='readonly')
        # entry_MTFF.place(y=150, x=60)
        # entry_MTFF.pack(side='right')
        self.widget_set_position(button_reset, self.entry_MTFF, 900, False, 50, True)  # widget set position an Form

        ''' Anzahl der Equipments '''
        label_Equipments = tk.Label(self, text=("Number of Equipments: "), font=NORM_FONT)
        # label_MTFF.place(y=150, x=50)
        # label_Equipments.pack(side='right')
        self.widget_set_position(button_reset, label_Equipments, 900, False, 70, True)  # widget set position an Form
        self.str_var_entry_Equipments = tk.IntVar()
        self.entry_Equipments = tk.Entry(self, textvariable=self.str_var_entry_Equipments, justify='center')
        # entry_MTFF.place(y=150, x=60)
        # entry_Equipments.pack(side='right')
        self.widget_set_position(button_reset, self.entry_Equipments, 900, False, 90,
                                 True)  # widget set position an Form

        ''' Anzahl der Meldungen '''
        label_Meldungen = tk.Label(self, text=("Number of Meldungen: "), font=NORM_FONT)
        # label_MTFF.place(y=150, x=50)
        # label_Meldungen.pack(side='right')
        self.widget_set_position(button_reset, label_Meldungen, 900, False, 110, True)  # widget set position an Form
        self.str_var_entry_Meldungen = tk.IntVar()
        self.entry_Meldungen = tk.Entry(self, textvariable=self.str_var_entry_Meldungen, justify='center')
        # entry_MTFF.place(y=150, x=60)
        # entry_Meldungen.pack(side='right')
        self.widget_set_position(button_reset, self.entry_Meldungen, 900, False, 130,
                                 True)  # widget set position an Form

        ''' Zeiträume '''

        self.str_year_start = tk.StringVar()
        self.str_month_start = tk.StringVar()

        self.str_year_end = tk.StringVar()
        self.str_month_end = tk.StringVar()

        self.str_var_limit_year = tk.StringVar()
        # limit_year = 2009
        self.str_var_limit_month = tk.StringVar()

        ''' zeitraum Start Fertigungsdatum '''
        label_zeitraum_fertigung_start = tk.Label(self, text="FertigungsBegin")
        label_zeitraum_fertigung_start.place(x=10, y=400)
        self.str_var_entry_zeitraum_fertigung_start = tk.StringVar()
        entry_zeitraum_fertigung_start = tk.Entry(self, textvariable=self.str_var_entry_zeitraum_fertigung_start,
                                                  justify='center')
        entry_zeitraum_fertigung_start.place(x=150, y=400)
        button_show_calender_fertigung_start = tk.Button(self, text="show calender", command= \
            lambda: calender(self.str_var_entry_zeitraum_fertigung_start, self.str_var_limit_year, \
                             self.str_var_limit_month, flag_year=True))
        button_show_calender_fertigung_start.place(x=300, y=400)

        ''' zeitraum Ende Fertigungsdatum '''
        label_zeitraum_fertigung_ende = tk.Label(self, text="FertigungsEnde")
        label_zeitraum_fertigung_ende.place(x=10, y=450)
        self.str_var_entry_zeitraum_fertigung_ende = tk.StringVar()
        entry_zeitraum_fertigung_ende = tk.Entry(self, textvariable=self.str_var_entry_zeitraum_fertigung_ende,
                                                 justify='center')
        entry_zeitraum_fertigung_ende.place(x=150, y=450)
        button_show_calender_fertigung_ende = tk.Button(self, text="show calender", command= \
            lambda: calender(self.str_var_entry_zeitraum_fertigung_ende, self.str_var_limit_year, \
                             self.str_var_limit_month, flag_year=False))
        button_show_calender_fertigung_ende.place(x=300, y=450)

        ''' zeitraum Start Störungbeginn'''
        label_zeitraum_meldung_start = tk.Label(self, text="Störungsbegin")
        label_zeitraum_meldung_start.place(x=10, y=500)
        self.str_var_entry_zeitraum_meldung = tk.StringVar()
        entry_zeitraum_meldung = tk.Entry(self, textvariable=self.str_var_entry_zeitraum_meldung, justify='center')
        entry_zeitraum_meldung.place(x=150, y=500)
        button_show_calender_start = tk.Button(self, text="show calender", command= \
            lambda: calender(self.str_var_entry_zeitraum_meldung, self.str_var_limit_year, \
                             self.str_var_limit_month, flag_year=True))
        button_show_calender_start.place(x=300, y=500)

        # button_show_calender = tk.Button(self, text="show calender", command = lambda: controller.show_frame(Calender)  )
        # button_show_calender.place(x = 300, y = 500)

        # button_import_date = tk.Button(self, text="import_date", command = lambda: self.get_date_from_Calender(self.str_var_entry_zeitraum_meldung)  )
        # button_import_date.place(x = 500, y = 500)

        ''' zeitraum Ende Störungsende'''
        label_zeitraum_meldung_ende = tk.Label(self, text="Störungsende")
        label_zeitraum_meldung_ende.place(x=10, y=550)
        self.str_var_entry_zeitraum_meldung_ende = tk.StringVar()
        entry_zeitraum_meldung_ende = tk.Entry(self, textvariable=self.str_var_entry_zeitraum_meldung_ende,
                                               justify='center')
        entry_zeitraum_meldung_ende.place(x=150, y=550)
        button_show_calender_ende = tk.Button(self, text="show calender", command= \
            lambda: calender(self.str_var_entry_zeitraum_meldung_ende, self.str_var_limit_year, \
                             self.str_var_limit_month, flag_year=False))
        button_show_calender_ende.place(x=300, y=550)

        # button_import_date_ende = tk.Button(self, text="import_date", command = lambda: self.get_date_from_Calender(self.str_var_entry_zeitraum_meldung_ende)  )
        # button_import_date_ende.place(x = 500, y = 550)

        '''
        end_date = self.str_var_entry_zeitraum_meldung_ende.get()
        end_date = datetime.strptime(end_date, "%Y.%m" )
        end_year = end_date.year
        end_month = end_date.month
        '''

        # Call reset_func to refresh df_land und ketten und Geraete_große und Baugruppe
        self.reset_func(ls_laender)

    def get_date_from_Calender(self, string_var_entry):
        print("get_date_from_Calender func")
        string_var_entry.set(year_month_str)

        # def create_component(self,component_name, ls_X, label_X, var_X, combobox_X, label_Xn, str_var_Xn,listbox_Xn):

    def create_component(self, df, component_name, callback_func, ls_selected_items, var_X, listbox_Xn):
        ls_X = list()
        for item in df.index:
            ls_X.append(item)
        label_X = tk.Label(self, text="choose " + component_name)
        label_X.pack()
        var_X = tk.StringVar()
        combobox_X = ttk.Combobox(self, textvariable=var_X, values=ls_X)
        combobox_X.pack()
        combobox_X.current(0)
        combobox_X.bind("<<ComboboxSelected>>", callback_func)
        label_Xn = tk.Label(self, text="selected " + component_name)
        label_Xn.pack()
        str_var_Xn = tk.StringVar()
        listbox_Xn = tk.Listbox(self, listvariable=str_var_Xn)
        str_var_Xn.set(ls_selected_items)
        listbox_Xn.pack()
        return ls_X, label_X, var_X, combobox_X, label_Xn, str_var_Xn, listbox_Xn

    def widget_set_position(self, last_widget, cur_widget, x_plus, x_flag, y_plus, y_flag):
        # get self position & height
        lv_x = last_widget.winfo_rootx()
        lv_y = last_widget.winfo_rooty()
        lv_width = last_widget.winfo_width()
        lv_height = last_widget.winfo_height()
        # set self new position & height
        if x_flag == True:
            cur_widget.place(x=(lv_x + lv_width + x_plus), y=(lv_y + y_plus))
        elif y_flag == True:
            cur_widget.place(x=(lv_x + x_plus), y=(lv_y + lv_height + y_plus))
        elif x_flag == True and y_flag == True:
            cur_widget.place(x=(lv_x + lv_width + x_plus), y=(lv_y + lv_height + y_plus))
        else:
            cur_widget.place(x=(lv_x + x_plus), y=(lv_y + y_plus))

    def combobox_ketten_contents(self, ls_selected_items):
        # df = func_filter_nach_XY(df_sorted, 'Land', self.ls_selected_countries)
        df = func_filter_nach_XY(df_sorted, 'Land', ls_selected_items)
        sr_ketten = df.ketten_zeich.drop_duplicates()

        ls = list()
        for item in sr_ketten.values:
            ls.append(item)

        self.ls_ketten = ls
        self.combobox_ketten.config(values=ls)

        # Waterfall effect on kombobox child -> Geraete_große

    def updtlistbox_ketten(self):
        self.listbox_ketten.delete(0, tk.END)  # clear listbox ketten
        self.str_var_listbox_ketten.set("")  # clear StringVar listbox_ketten
        self.ls_selected_ketten.clear()  # clear values of list selected ketten

    ''' Reset function '''

    def reset_func(self, ls_laender):

        # del df_land_temp
        # del df_ketten_zeich_temp
        # del df_Geraete_große_temp
        # del df_Baugruppe_temp

        self.listbox_land.delete(0, tk.END)  # clear listbox land
        self.str_var_listbox_land.set("")  # clear StringVar listbox_land
        self.ls_selected_countries.clear()  # clear values of list ls_selected_countries
        self.updtlistbox_ketten()  # call func updtlistbox_ketten to remove listbox_ketten contents
        self.combobox_ketten_contents(ls_laender)  # call func combobox_ketten_contents to reset combobox values
        # call func updtlistbox_X to remove listbox_geraete_große contents
        self.updtlistbox_X(self.listbox_geraete_große, self.str_var_listbox_geraete_große,
                           self.ls_selected_geraete_große)
        # call func combobox_child_contents to reset combobox_geraete_große values
        ls = self.combobox_child_contents('Land', ls_laender, 'Geräte_große')
        # print("ls_Geräte_große in reset_func= ", ls)
        self.ls_geraete_große = ls
        self.combobox_geraete_große.config(values=ls)

        # reset component baugruppe by laender
        ls = self.combobox_child_contents('Land', ls_laender, 'Baugruppe')
        # print("ls_beschränkte_Baugruppe = ", ls)
        self.ls_baugruppe = ls
        self.combobox_baugruppe.config(values=ls)
        # ^ oder
        # self.combobox_baugruppe_contents(self.ls_laender)
        self.updtlistbox_X(self.listbox_baugruppe, self.str_var_listbox_baugruppe, self.ls_selected_baugruppe)

        self.str_var_entry_MTFF.set(0)
        self.str_var_entry_Equipments.set(0)
        self.str_var_entry_Meldungen.set(0)

        # self.entry_MTFF.delete(0,tk.END)
        # self.entry_Equipments.delete(0,tk.END)
        # self.entry_Meldungen.delete(0,tk.END)

        # reset entry zeitraeume
        self.str_var_entry_zeitraum_meldung.set("")
        self.str_var_entry_zeitraum_meldung_ende.set("")

        # reset entry zeitraeume fertigungsbegin und ende
        self.str_var_entry_zeitraum_fertigung_start.set("")
        self.str_var_entry_zeitraum_fertigung_ende.set("")

        # reset str_year and  str_month -> both start and end
        self.str_year_start.set("")
        self.str_month_start.set("")

        self.str_year_end.set("")
        self.str_month_end.set("")

        self.str_var_limit_year.set(2009)
        self.str_var_limit_month.set(1)

    def callback_land(self, event):  # function called when '<<ComboboxSelected>>' event is triggered
        existens_item_listbox_land = self.str_var_listbox_land.get()  # all existens item in listbox_land
        selected_item = event.widget.get()  # selected item in combobox_land to add in listbox_land
        if selected_item not in existens_item_listbox_land:  # to avoid insert duplicate item in listbox and list_selected_laender

            self.listbox_land.insert(tk.END, self.v_land.get())
            print("event.widget.get() land = ", event.widget.get())
            print("self.v_land.get() = ", self.v_land.get())
            self.ls_selected_countries.append(event.widget.get())
            self.str_var_listbox_land.set(self.ls_selected_countries)
            self.combobox_ketten_contents(self.ls_selected_countries)

            ls = self.combobox_child_contents('Land', self.ls_selected_countries, 'Geräte_große')
            print("ls_beschränkte_Geräte_große= ", ls)
            self.ls_geraete_große = ls
            self.combobox_geraete_große.config(values=ls)
            # clear listbox_geraete_große
            self.updtlistbox_X(self.listbox_geraete_große, self.str_var_listbox_geraete_große,
                               self.ls_selected_geraete_große)

            '''     # hier wollte ich Wasserfall die wirkung auf nächste combobox schreiben aber letztendlich sollte die einine Feldern selbst geschrieben werden
            ls = self.ls_children.copy()
            parent = 'Land'
            child=""
            index_parent = ls_children.index(parent)
            child = ls_children.pop(index_parent+1)
            print("child of %s = %s" % (parent, child))
            '''

            # refresh and update component baugruppe by land
            ls = self.combobox_child_contents('Land', self.ls_selected_countries, 'Baugruppe')
            print("ls_beschränkte_Baugruppe = ", ls)
            self.ls_baugruppe = ls
            self.combobox_baugruppe.config(values=ls)
            # ^ oder
            # self.combobox_baugruppe_contents(self.ls_selected_countries)
            self.updtlistbox_X(self.listbox_baugruppe, self.str_var_listbox_baugruppe, self.ls_selected_baugruppe)

    def callback_ketten(self,
                        event):  # function called when '<<ComboboxSelected>>' event is triggered  ->click on element in combobox to add into listbox
        existens_item_listbox_ketten = self.str_var_listbox_ketten.get()  # all existens item in listbox_ketten
        print("existens item in listbox_ketten", existens_item_listbox_ketten)
        selected_item = event.widget.get()  # selected item in combobox_ketten to add in listbox_ketten
        #  ^  oder
        # selected_item = self.v_ketten.get()      #selected item in combobox_ketten to add in listbox_ketten
        if selected_item not in existens_item_listbox_ketten:  # to avoid insert duplicate item in listbox and list_selected_ketten

            self.listbox_ketten.insert(tk.END, selected_item)
            # ^  oder:
            # self.listbox_ketten.insert(tk.END, self.v_ketten.get())

            print("event.widget.get() ketten = ", event.widget.get())
            print("self.v_ketten.get() = ", self.v_ketten.get())
            print("selected_item from combobox_ketten = ", selected_item)

            my_list = self.ls_selected_ketten.append(selected_item)
            # ^  oder:
            # my_list = self.ls_selected_ketten.append(event.widget.get())

            ##self.str_var_listbox_ketten.set(my_list)      # is not be necessary
            ls = self.combobox_child_contents('ketten_zeich', self.ls_selected_ketten, 'Geräte_große')
            print("ls_beschränkte_Geräte_große= ", ls)
            self.ls_geraete_große = ls
            self.combobox_geraete_große.config(values=ls)
            # clear listbox_geraete_große
            self.updtlistbox_X(self.listbox_geraete_große, self.str_var_listbox_geraete_große,
                               self.ls_selected_geraete_große)

            # refresh and update component baugruppe by ketten
            ls = self.combobox_child_contents('ketten_zeich', self.ls_selected_ketten, 'Baugruppe')
            self.ls_baugruppe = ls
            self.combobox_baugruppe.config(values=ls)
            # ^ oder
            # self.combobox_baugruppe_contents(self.ls_selected_ketten)
            self.updtlistbox_X(self.listbox_baugruppe, self.str_var_listbox_baugruppe, self.ls_selected_baugruppe)

    def updtlistbox_X(self, listbox_x, str_var_x, ls_selected_x):
        listbox_x.delete(0, tk.END)  # clear listbox
        str_var_x.set("")  # clear StringVar listbox_x
        ls_selected_x.clear()  # clear values of list selected items

    def combobox_child_contents(self, str_parent_name, ls_selected_items, str_child_name):
        df = func_filter_nach_XY(df_sorted, str_parent_name, ls_selected_items)
        sr_child = df[str_child_name].drop_duplicates()  # Series
        ls = list()
        for item in sr_child.values:
            ls.append(item)
        return ls

    def callback_geraete_große(self, event):
        print("callback_geraete_große")
        existens_item = self.str_var_listbox_geraete_große.get()
        print("existens item listbox Geräte große", existens_item)
        selected_item = event.widget.get()
        print("combo geräte große selected item = ", selected_item)
        if selected_item not in existens_item:
            print("self.v_geraete_große.get() =", self.v_geraete_große.get())  # equivalent to call event.widget.get()
            self.listbox_geraete_große.insert(tk.END, self.v_geraete_große.get())  # self.v_geraete_große.get()
            self.ls_selected_geraete_große.append(selected_item)
            # self.str_var_listbox_geraete_große.set(ls_selected_geraete_große)

            # refresh and update component baugruppe by geraete_große
            ls = self.combobox_child_contents('Geräte_große', self.ls_selected_geraete_große, 'Baugruppe')
            self.ls_baugruppe = ls
            self.combobox_baugruppe.config(values=ls)
            # ^ oder
            # self.combobox_baugruppe_contents(self.ls_selected_geraete_große)
            self.updtlistbox_X(self.listbox_baugruppe, self.str_var_listbox_baugruppe, self.ls_selected_baugruppe)

    def callback_baugruppe(self, event):
        print("callback_baugruppe")
        existens_item = self.str_var_listbox_baugruppe.get()
        print("existens item listbox baugruppe", existens_item)
        selected_item = event.widget.get()  # equivalent to call self.v_baugruppe.get()
        print("combo baugruppe selected item = ", selected_item)
        if selected_item not in existens_item:
            self.listbox_baugruppe.insert(tk.END, self.v_baugruppe.get())
            self.ls_selected_baugruppe.append(selected_item)
            # child component functions:

    def combobox_baugruppe_contents(self, ls_selected_items):
        df = func_filter_nach_XY(df_sorted, 'Geräte_große', ls_selected_items)
        sr_baugruppe = df.Baugruppe.drop_duplicates()

        ls = list()
        for item in sr_baugruppe.values:
            ls.append(item)

        self.ls_baugruppe = ls
        self.combobox_baugruppe.config(values=ls)

    def view_chart(self, df, field_name):
        Meldungen, Equipments, MTFF, df = func_MTFF_nach_X(df_filter_XY, field_name,
                                                           failure_start_field_name=str('Störungsbeginn (Dat)_punkt'))

        # top 5 baugruppen falls field_name Baugruppe ist
        if field_name == str('Baugruppe'):
            df = PageOne.manipulate_df_BauGr(df)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.clear()
        a.plot(df)
        a.plot(df.index, df.iloc[:, 0:1], "#00A3E0", label="Days")
        a.plot(df.index, df.iloc[:, 1:2], "#183A54", label="Count")
        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
        a.set_title('Bar_chart ' + field_name)
        a.set_xlabel(field_name)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def func_filter_by_date(self, df, field_name, str_var_entry_zeitraum_start, str_var_entry_zeitraum_ende):
        # convert string entry zeitraeume to year and month separate
        if str_var_entry_zeitraum_start.get() != '':
            Calender.convert_date(self, str_var_entry_zeitraum_start, self.str_year_start, self.str_month_start)
        else:
            self.str_year_start.set(datetime.now().year)
            self.str_month_start.set(datetime.now().month)

        if str_var_entry_zeitraum_ende.get() != '':
            Calender.convert_date(self, str_var_entry_zeitraum_ende, self.str_year_end, self.str_month_end)
        else:
            self.str_year_end.set(datetime.now().year)
            self.str_month_end.set(datetime.now().month)

        # fieldName = str('Störungsbeginn (Dat)_punkt')      #field_name determiend the field of Start of Failure, entweder 'Störungsbeginn (Dat)_punkt' oder 'Meldungsdatum'
        fieldName = field_name

        # sorting df_filter_XY by date field 'Störungsbeginn (Dat)_punkt'
        df['sorted_Date'] = pd.to_datetime(df[fieldName])
        df = df.sort_values(['Equipment', 'sorted_Date'], ascending=True)

        # format start_date
        start_date_string = '01' + '.' + self.str_month_start.get() + '.' + self.str_year_start.get()
        start_date = datetime.strptime(start_date_string, '%d.%m.%Y').date()  # strptime is string parser
        # start_date = datetime.date(self.str_year_start.get(), self.str_month_start.get(), 1)
        start_date = start_date.strftime("%d.%m.%Y")

        # format end_date
        end_date_string = '01' + '.' + self.str_month_end.get() + '.' + self.str_year_end.get()
        end_date = datetime.strptime(end_date_string,
                                     '%d.%m.%Y').date()  # string parser liefert datetime.date(year , month, 1)
        # end_date = datetime.date(self.str_year_end.get(), self.str_month_end.get(), 1)
        end_date = end_date.strftime("%d.%m.%Y")

        '''
        # date formating test in console :
        current_date = datetime.now()
        last_date = datetime.date(current_date) - timedelta(days=365)
        current_date = datetime.date(current_date)
        last_date = datetime.date(last_date)
        current_date = current_date.strftime("%d.%m.%Y")
        last_date = last_date.strftime("%d.%m.%Y")
        #end date formating '''

        # truncate df : by default truncate index rows : return between strat_ and end_date
        df = func_filter_nach_X(df, 'sorted_Date', end_date, 'lt')  # less than end_date
        df = func_filter_nach_X(df, 'sorted_Date', start_date, 'gt')  # greater than start

        # remove extra field sorted_Date
        df = df.drop(columns='sorted_Date')
        df = df.reset_index(drop=True)

        return df

    def call_func_filterXY(self):
        # Rational.popupmsg(self,"Rational class call_func_filterXY")     # call popupmsg from Rational class
        # poppumsg("call_func_filterXY")     #call popupmsg from func popupmsg außerhalb von classes

        global df_filter_XY, Meldungen, Equipments, MTFF
        # global df_land_temp, df_ketten_zeich_temp, df_Geraete_große_temp, df_Baugruppe_temp

        # initialize df_temp_s
        global df_land_temp
        df_land_temp = df_land.copy(deep=True)
        global df_ketten_zeich_temp
        df_ketten_zeich_temp = df_ketten_zeich.copy(deep=True)
        global df_Geraete_große_temp
        df_Geraete_große_temp = df_Geraete_große.copy(deep=True)
        global df_Baugruppe_temp
        df_Baugruppe_temp = df_Baugruppe.copy(deep=True)

        # initial df_filter_XY
        df_filter_XY = df_sorted.copy(deep=True)

        # filter nach Dates

        if (
                self.str_var_entry_zeitraum_fertigung_start.get() != '' or self.str_var_entry_zeitraum_fertigung_ende.get() != ''):
            # call filter by date -> truncate before and after eingegebene zeitraum
            df_filter_XY = self.func_filter_by_date(df_filter_XY, 'Fertigungsdatum',
                                                    self.str_var_entry_zeitraum_fertigung_start,
                                                    self.str_var_entry_zeitraum_fertigung_ende)
            print("str_year_start fertigung in class owner func_filter = ", self.str_year_start.get())
            print("str_month_start fertigung in class owner func_filter = ", self.str_month_start.get())

            print("str_year_end fertigung in class owner func_filter = ", self.str_year_end.get())
            print("str_month_end fertigung in class owner func_filter = ", self.str_month_end.get())

        if (self.str_var_entry_zeitraum_meldung.get() != '' or self.str_var_entry_zeitraum_meldung_ende.get() != ''):
            # call filter by date -> truncate before and after eingegebene zeitraum
            df_filter_XY = self.func_filter_by_date(df_filter_XY, 'Störungsbeginn (Dat)_punkt',
                                                    self.str_var_entry_zeitraum_meldung,
                                                    self.str_var_entry_zeitraum_meldung_ende)

            print("str_year_start Meldung in class owner func_filter = ", self.str_year_start.get())
            print("str_month_start Meldung in class owner func_filter = ", self.str_month_start.get())

            print("str_year_end Meldung in class owner func_filter = ", self.str_year_end.get())
            print("str_month_end Meldung in class owner func_filter = ", self.str_month_end.get())

        ls_dfs = [df_land_temp, df_ketten_zeich_temp, df_Geraete_große_temp, df_Baugruppe_temp]

        str_var_land = self.str_var_listbox_land.get()
        str_var_ketten_zeich = self.str_var_listbox_ketten.get()
        str_var_geraete_große = self.str_var_listbox_geraete_große.get()
        str_var_baugruppe = self.str_var_listbox_baugruppe.get()

        ls_sel_countries = self.ls_selected_countries
        ls_sel_ketten = self.ls_selected_ketten
        ls_sel_geraete = self.ls_selected_geraete_große
        ls_sel_baugruppe = self.ls_selected_baugruppe

        ls_df_str_var_field_ls_sel = list()
        ls_df_str_var_field_ls_sel = [(df_land_temp, str_var_land, 'Land', ls_sel_countries),
                                      (df_ketten_zeich_temp, str_var_ketten_zeich, 'ketten_zeich', ls_sel_ketten), (
                                      df_Geraete_große_temp, str_var_geraete_große, 'Geräte_große',
                                      ls_sel_geraete)]  # , (df_Baugruppe_temp, str_var_baugruppe , 'Baugruppe', ls_sel_baugruppe)
        # 'Unnamed: 6'
        empty_flag = True
        # index=0
        for df, str_var, field, ls_sel in ls_df_str_var_field_ls_sel:
            # if ls_df_str_var_field_ls_sel.count(df, str_var,field, ls_sel) ==0 :
            # index +=1
            df_field_temp = ls_dfs.pop(0)
            if ls_sel != []:
                empty_flag = False
                # string combination of variables and lists and df
                string_comb_var = "df is{}, str_var is {}, field is {}, ls_sel is {} ".format(df, str_var, field,
                                                                                              ls_sel)
                print(" string combination df variables ls =  ", string_comb_var)
                df_filter_XY = func_filter_nach_XY(df_filter_XY, str(field), ls_sel)
                Meldungen, Equipments, MTFF, df = func_MTFF_nach_X(df_filter_XY, field_name=str(field),
                                                                   failure_start_field_name=str(
                                                                       'Störungsbeginn (Dat)_punkt'))
                print("ls selected %s -> %s" % (str(field), ls_sel))

                df_field_temp = df.copy(deep=True)
                print("df_field_temp =  ", df_field_temp)

            ls_dfs.append(df_field_temp)

        if empty_flag == True:
            print("please select at least one field!")
            popupmsg("please selcet at least one field!")
        else:
            self.str_var_entry_MTFF.set(MTFF)
            self.str_var_entry_Equipments.set(Equipments)
            self.str_var_entry_Meldungen.set(Meldungen)
            # assign dfs_temp to avoid in view_chart recall MTFF_func
            self.func_assignment_dfs(
                ls_dfs)  # if other class this method called, this must be StartPage.func_assignment_dfs(ls_dfs) writen

    def func_assignment_dfs(self, ls):
        df_land_temp = ls.pop(0)
        df_ketten_zeich_temp = ls.pop(0)
        df_Geraete_große_temp = ls.pop(0)
        df_Baugruppe_temp = ls.pop(0)


class Calender(tk.Frame):
    import calendar
    # variable = 123
    # Calender.variable -> 123
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # controller.wm_title(self, "Calender")

        # self.parent = parent

        # self.variable = 456 #refer to class Calender variable da oben declarated
        # cal = Calender -> make an instance of class --- cal.variable -> 456

        label_year = tk.Label(self, text="year:")
        label_year.pack(side='top')

        self.entry_year = tk.Entry(self)
        self.entry_year.pack(side='top')

        label_month = tk.Label(self, text="month:")
        label_month.pack()

        self.entry_month = tk.Entry(self)
        self.entry_month.pack(side='top')

        button_show = tk.Button(self, text="show date", command=self.cal)
        button_show.pack(side='top')

        self.year = self.entry_year.get()
        self.month = self.entry_month.get()

        button_Ok = tk.Button(self, text="Ok", command=lambda: controller.show_frame(StartPage))
        button_Ok.pack(side='top')

    def convert_date(self, str_year_month, str_year, str_month):  # get date and split to year and month
        date = str_year_month.get()  # get date
        date = datetime.strptime(date, "%Y.%m")  # format date

        year = date.year  # get year of formated date
        str_year.set(year)  # set year of parent class
        print("year in method convert_date class Calender  = ", year)

        month = date.month  # get month of formated date
        str_month.set(month)  # set month of parent class
        print("month in method convert_date class Calender  = ", month)

    def cal(self):
        # import calendar
        year = self.entry_year.get()
        month = self.entry_month.get()
        print("year = ", year)
        print("month = ", month)
        cal_x = self.calendar.month(int(year), int(month), w=2, l=1)
        print("cal_x", cal_x)
        cal_out = tk.Label(self, text=cal_x, font=('courier', 12, 'bold'), bg='lightblue')
        cal_out.pack(padx=3, pady=10)
        global year_month_str
        year_month_str = str(year) + '.' + str(month)
        print("year_month_str = ", year_month_str)
        ##self.parent.str_var_entry_zeitraum_meldung.set(year_month_str)
        ##year_month = f'{year:02}.{month}'
        ##print("year_month = ", year_month)
        # self.parent.str_var_entry_zeitraum_meldung.set(year_month)
        # return year,month

    def get_date(self):
        return self.year, self.month

    def info(self):
        self.fetch_name = self.parent.ent.get()

    def set_parent_date(self):
        # year=self.entry_year.get()
        # month=self.entry_month.get()
        year, month = self.get_date()
        year_month = f'{year:02}.{month}'
        self.parent.str_var_entry_zeitraum_meldung.set(year_month)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One nach Land!!!", font=LARGE_FONT)
        label.pack(side='top')
        button1 = ttk.Button(self, text="Back to Home", command=lambda: PageThree.back_home(self, controller, self.canvas, self.toolbar))#controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two nach Baugruppe", command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="View Line Chart Land ",
                             command=lambda: StartPage.view_chart(self, df_land_temp, field_name=str('Land')))
        button3.pack()
        button4 = ttk.Button(self, text="View Bar Chart Land",
                             command=lambda:  self.call_viewer())#self.view_chart(df_land_temp, field_name=str('Land')))
        button4.pack()


        #button5 = ttk.Button(self, text="View Bar chart func view_chart",
        #                     command=lambda: view_chart(self, df_land_temp, field_name=str('Land')))
        #button5.pack()

    def manipulate_df_BauGr(df):
        # write correct values of 'count'
        ls_count = list()
        for item in range(len(df)):
            var = df_Baugruppe_temp['count'][df_Baugruppe_temp.index == df.index[item]]
            if var.empty is False:
                ls_count.append(var.values[0])  # or var.iloc[0] return value of count
                # var.index[0] return value of index -> Baugruppe ziffer
            else:
                ls_count.append(0)
        df['count'] = ls_count

        df = df.sort_values('count', ascending=False)
        df = df.iloc[:5, :]

        ls_Bau_Gr_kennz = list()
        # list_df_index = df.index.tolist() # a list of values in index of dataframe
        for item in range(len(df)):
            var = df_sorted.Bau_Gr_kennz[(df_sorted['Baugruppe'] == df.index[item])]
            ls_Bau_Gr_kennz.append(var.values[0])

        df['Bau_Gr_kennz'] = ls_Bau_Gr_kennz
        df = df.set_index(df['Bau_Gr_kennz'])
        df = df.drop(columns='Bau_Gr_kennz')

        # df = df_new.copy(deep=True)
        # df = df.assign(Bau_Gr_kennz = ls_Bau_Gr_kennz)
        # df['Bau_Gr_kennz'] = map(lambda x : x==df.index.get_value, df_filter_XY['Bau_Gr_kennz'].values)
        return df

    def view_chart(self, df, field_name):
        columns = df.columns
        Meldungen, Equipments, MTFF, df = func_MTFF_nach_X(df_filter_XY, field_name,
                                                           failure_start_field_name=str('Störungsbeginn (Dat)_punkt'))
        df.columns = columns

        # erste 5 kritische baugruppen
        if field_name == str('Baugruppe'):
            df = PageOne.manipulate_df_BauGr(df)

        '''
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.clear()
        a.plot(df)
        a.plot(df.index, df.iloc[: , 0:1] , "#00A3E0", label="Days")
        a.plot(df.index, df.iloc[: , 1:2] , "#183A54", label="Count")
        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
        a.set_title('Bar_chart ' + field_name)
        a.set_xlabel(field_name)
        '''
        # df = df_Geraete_große.copy(deep=True)
        # fieldName = 'Geräte_große'
        fieldName = field_name

        # fig, ax = plt.subplots()

        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)

        ax.clear()
        index = df.index
        ind = np.arange(len(df))  # the x locations for the groups
        bar_width = 0.45  # the width of the bars

        mean = df['F_t_Fail_time_days']  # mean = df.iloc[: , 0:1].values

        count = df['count']  # count = df.iloc[: , 1:2].values

        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        rects1 = ax.bar(ind, mean, bar_width, alpha=opacity, color='b', error_kw=error_config,
                        label='Mean time to failure')
        rects2 = ax.bar(ind + bar_width, count, bar_width, alpha=opacity, color='r', error_kw=error_config,
                        label='number of Equipment')

        # fig.set_figwidth(7) # set figure width
        # fig.set_figheight(5) # set figure height
        # add some  text for lables, title and axes ticks
        ax.set_xlabel(fieldName)
        ax.set_ylabel('amount')
        ax.set_title('Mean time to first Failure by' + fieldName)
        ax.set_xticks(ind + bar_width / 2)  # + bar_width / 2
        ax.set_xticklabels(index, rotation=10)  # rotation=x degree set rotation for ticks
        ax.legend()

        fig.tight_layout()

        def autolable(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center',
                        va='bottom')

        autolable(rects1)
        autolable(rects2)
        # plt.show()

        # global canvas
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # global toolbar
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        return canvas, toolbar

    def call_viewer(self):
        self.canvas, self.toolbar = PageOne.view_chart(self, df_land_temp, field_name=str('Land'))


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two nach Baugruppe!!!", font=LARGE_FONT)
        label.pack(side='top')
        button1 = ttk.Button(self, text="Back to Home", command=lambda: self.back_home(parent, controller))
        # button1.place(x=5, y=50)
        button1.pack()

        button2 = ttk.Button(self, text="Page One nach Land", command=lambda: controller.show_frame(PageOne))
        # button2.place(x=150, y=50)
        button2.pack()
        button3 = ttk.Button(self, text="View Line Chart Baugruppe",
                             command=lambda: StartPage.view_chart(self, df_Baugruppe_temp, field_name=str('Baugruppe')))
        # button3.place(x=300, y=50)
        button3.pack()
        button4 = ttk.Button(self, text="View Bar Chart Baugruppe", command=lambda: self.call_viewer())
        button4.pack()

    def call_viewer(self):
        self.canvas, self.toolbar = PageOne.view_chart(self, df_Baugruppe_temp, field_name=str('Baugruppe'))

    def back_home(self, parent, controller):
        controller.show_frame(StartPage)
        # self.destroy
        # PageTwo.destroy
        # PageTwo.pack_forget
        # self.canvas.delete("all")
        # self.delete(self.canvas)
        # self.canvas.delete(all)
        '''# destroy all widget of Frame:
        for widget in PageTwo.winfo_children(self):
            widget.destroy()
        '''
        # self.refresh()
        self.canvas.get_tk_widget().pack_forget()
        self.toolbar.destroy()

        for widget in PageTwo.winfo_children(self):
            # print("PageTwo children values ->>>", PageTwo.children.values(self))
            print("PageTwo widgets -->>>>", widget)
            # controller.canvas.destroy()
            print("controller children values =>>>>> ", self.children.values())
            # print("controller canvas ->>", PageTwo.fig.destroy)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Three nach ketten_zeichen!!!", font=LARGE_FONT)
        label.pack(side='top')
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: self.back_home(controller, self.canvas, self.toolbar))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two nach Baugruppe", command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="View Line Chart ketten_zeich",
                             command=lambda: StartPage.view_chart(self, df_ketten_zeich_temp,
                                                                  field_name=str('ketten_zeich')))
        button3.pack()
        button4 = ttk.Button(self, text="View Bar Chart ketten zeich", command=lambda: self.call_viewer())
        button4.pack()

    def call_viewer(self):
        self.canvas, self.toolbar = PageOne.view_chart(self, df_ketten_zeich_temp, field_name=str('ketten_zeich'))

    def back_home(self, controller, canvas, toolbar):
        controller.show_frame(StartPage)
        canvas.get_tk_widget().pack_forget()
        toolbar.destroy()


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Four nach Geräte Große!!!", font=LARGE_FONT)
        label.pack(side='top')
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: PageThree.back_home(self, controller, self.canvas, self.toolbar))
        button1.pack()
        button2 = ttk.Button(self, text="Page Three nach Ketten_zeichen",
                             command=lambda: controller.show_frame(PageThree))
        button2.pack()
        button3 = ttk.Button(self, text="View Line Chart Geraete_große",
                             command=lambda: StartPage.view_chart(self, df_Geraete_große_temp,
                                                                  field_name=str('Geräte_große')))
        button3.pack()
        button4 = ttk.Button(self, text="View Bar Chart geraete_große", command=lambda: self.call_viewer())
        button4.pack()

    def call_viewer(self):
        self.canvas, self.toolbar = PageOne.view_chart(self, df_Geraete_große_temp, field_name=str('Geräte_große'))


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Five nach Equipment!!!", font=LARGE_FONT)
        label.pack(side='top')
        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Four nach Geräte_geroße", command=lambda: controller.show_frame(PageFour))
        button2.pack()
        button3 = ttk.Button(self, text="View Bar chart Geräte_geroße animation",
                             command=lambda: self.call_animation(df_Geraete_große_temp, field_name=str('Geräte_große')))
        button3.pack()

    def call_animation(self, df, field_name):
        ani = animation.FuncAnimation(f, animate(df, field_name), interval=5000)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


print(__doc__)
print(tk.TkVersion)

# path is where that code is runing
#data_path = './'
data_path = 'C:/Users/hoeh/Desktop/Ehsan_Hosseini_Masterarbeit/Data Analysis Abteilung/Erste Arbeitspacket/Daten/Datenaustausch/'
# file_name = 'Punktediagramm 10_2018 inkl. RSP.xlsx'
file_name_Punktediagramm = '2019_02_27_Punktediagramm_2009-2018_inkl._RSP.xlsx'
file_name_Punktediagramm_alt = 'Punktediagramm 10_2018 inkl. RSP.xlsx'
file_name_Installationsdatum_customer = 'SAP_Meldungsnummer_Installationsdatum_Customer.xlsx'
file_name_Meldung_Beginn_Ende = 'Meldungsnummer Beginn Ende.xlsx'
file_name_joint_df = 'Joint_punktediagramm_and_installationsdatum.xlsx'
file_name_kundeninfo = 'Kundeninfos v1.xlsx'

# sheet_name = '2018'
global current_year
current_year = datetime.now().year
# global limit_year
# limit_year = 2009
sheet_name = list(range(2009, current_year + 1))  # in range 2009 to include 2018


# load df from excel method 1 -- laden ist langsam
def load_from_excel(data_path, file_name, sheet_name):
    path_name = data_path + file_name
    Excel_file = pd.ExcelFile(path_name)
    df = Excel_file.parse(sheet_name)
    return df


# load df from excel method 2 -- laden ist sehr schnell
def load_excelFile(file_name, sheet_name):
    data = pd.ExcelFile(file_name)
    all_excel_sheet_names = data.sheet_names
    df = data.parse(sheet_name=sheet_name)
    return df, all_excel_sheet_names


#   load df from excel File(use method 2(fast load method)) with all sheets
def load_excelFile_all_sheets(file_name, reset_index):
    first_timer = datetime.now()
    df = pd.DataFrame()
    data = pd.ExcelFile(file_name)
    for i in range(len(data.sheet_names)):
        df_temp = data.parse(sheet_name=data.sheet_names[i])
        df = df.append(df_temp)
    if (reset_index != False):
        df.reset_index(inplace=True, drop=True)

    second_timer = datetime.now()
    print("read xlsx in %s time" % (second_timer - first_timer))
    print("read xlsx successful and reset_index =", reset_index)
    return df


# df = load_from_excel(data_path, file_name, sheet_name)

def write_to_excel(df, data_path, file_name, sheet_name):
    writer = pd.ExcelWriter(data_path + file_name)  # file name and path
    df.to_excel(writer, sheet_name)  # writer and sheet name
    writer.save()
    return True


# input data from excel to dataframes and merge all sheet names
Vars_func_prepare_data = {}


def func_prepare_data(data_path, file_name_Punktediagramm, sheet_name):
    global Vars_func_prepare_data
    df_main_data = df_temp = pd.DataFrame()  # declare und initialize multiple df in single line
    for i in sheet_name:
        df_temp = load_from_excel(data_path, file_name_Punktediagramm, sheet_name=str(i))
        df_main_data = df_main_data.append(df_temp)

    del df_temp  # release memory df_temp
    # reset indexes before write to JSON is necessary
    df_main_data = df_main_data.reset_index(inplace=True,
                                            drop=True)  # reset indexes after vertical join to avoid same indexes
    print("prepration successful")
    Vars_func_prepare_data = inspect.currentframe().f_locals
    return df_main_data


# Write dataframes to JSON file which from Excel loaded
Vars_func_write_df_to_JSON = {}


def func_write_df_to_JSON(df, file_name):
    global Vars_func_write_df_to_JSON
    df.to_json(file_name + '.JSON')
    Vars_func_write_df_to_JSON = inspect.currentframe().f_locals
    return True


# read dataframe from JSON file
Vars_func_read_df_from_json = {}


def func_read_df_from_json(file_name):
    global Vars_func_read_df_from_json
    first_timer = datetime.now()

    df = pd.read_json(file_name + '.JSON')
    second_timer = datetime.now()
    print("read JSON successful in %s time" % (second_timer - first_timer))
    Vars_func_read_df_from_json = inspect.currentframe().f_locals
    return df


'''
# use dict :
# df = Vars_func_join_dfs['df']
'''
# join dataframes and drop useless fields and take new df to give appropriate df parameters for MTFF
Vars_func_join_dfs = {}


def func_join_dfs(df_1, df_2, df_3):
    global Vars_func_join_dfs

    #   df_1 = df_punktediagram
    #   df_2 = df_installationsdatum_customer
    #   df_3 = df_Meldung_Beginn_Ende

    df = pd.DataFrame()
    df['Service-Meldung'] = df_1['Service-Meldung']
    df['Equipment'] = df_1['Equipment']
    df['Src_meldung_Ursachencode'] = df_1['Servicemeldung Ursachencode']
    df['Baugruppe'] = df_1['Baugruppe']
    df['Bau_Gr_kennz'] = df_1['Unnamed: 3']
    ##df = df.groupby(['Service-Meldung', 'Equipment', 'Src_meldung_Ursachencode', 'Baugruppe', 'Bau_Gr_kennz' ]).size().reset_index(name='count')
    df['Land'] = df_1['Länderschlüssel (SMC']
    df['Germat Elektro/Gas ('] = df_1['Germat Elektro/Gas (']
    df['ketten_zeich'] = df_1['OEM-/Kettenkennzeichen']
    df['mat_Spannung'] = df_1['Germat Spannung (0MA']
    df['Anw-Status'] = df_1['Anw-Status']
    df['Invt_Nr'] = df_1['InventarNr']
    df['Fertigungsdatum'] = df_1['Fertigungsdatum']
    df['Störungsbeginn (Dat)_punkt'] = df_1['Störungsbeginn (Dat)']

    df_temp = pd.DataFrame()
    df_temp['Service-Meldung'] = df_2['Service-Meldung']
    df_temp['GewährlBeginn Datum'] = df_2['GewährlBeginn Datum']
    # df_temp['Fertigungsdatum']      =   df_2['Fertigungsdatum']
    df_temp['Störungsbeginn (Dat)'] = df_2['Störungsbeginn (Dat)']
    # join must be on same lenght
    # new_df = pd.merge(df, df_installationsdatum_customer_json, how='left', right_on=df_installationsdatum_customer_json['GewährlBeginn Datum'])
    df = df.set_index('Service-Meldung').join(df_temp.set_index('Service-Meldung'), on='Service-Meldung', how='left',
                                              rsuffix='_')

    # df.merge(df_installationsdatum_customer_json, on='Service-Meldung', how='left')    # muss am key
    # new_df = df.merge(df_temp, on='Service-Meldung', how='left')    # 4,591,587 records

    # new_df = df.combine_first(df_temp)     #richtig funktioniert - Anzahl der Datensätze = other
    ##df = df.join(df_temp, how='left', rsuffix='_')   # richtig funktioniert - Anzahl der Datensätze = caller
    ##df = df.drop(columns='Service-Meldung_')    # remove duplicate KEY

    # new_df = df.set_index('Service-Meldung').join(df_temp.set_index('Service-Meldung'))    # Anzahl der Datensätze = 4,591,587

    #   release memory
    del df_temp
    df_temp = pd.DataFrame()
    df_temp['Service-Meldung'] = df_3['Meldung']
    df_temp['Meldungsart'] = df_3['Meldungsart']
    df_temp['Meldungsdatum'] = df_3['Meldungsdatum']
    df_temp['StörBeginn'] = df_3['StörBeginn']
    df_temp['Störungsende'] = df_3['Störungsende']

    # df = df.join(df_temp, how='left', rsuffix='_M')   # richtig funktioniert - Anzahl der Datensätze = caller

    df = df.join(df_temp.set_index('Service-Meldung'), on='Service-Meldung', how='left', rsuffix='_M')
    df = df.fillna(
        0)  # remove null values after join with df_Meldungen because of records which there is not in df_Meldungen
    # df = df.join(df_temp, how='left', rsuffix='_WebID')
    # df_new = df_new.drop(columns=)

    #   release memory
    del df_temp

    #   Aggregate
    df = df.groupby(['Service-Meldung', 'Equipment', 'Src_meldung_Ursachencode', 'Baugruppe', 'Bau_Gr_kennz', 'Land',
                     'Germat Elektro/Gas (', 'ketten_zeich', 'mat_Spannung', 'Anw-Status', 'Invt_Nr', 'Fertigungsdatum',
                     'GewährlBeginn Datum', 'Störungsbeginn (Dat)_punkt', 'Störungsbeginn (Dat)', 'Meldungsart',
                     'Meldungsdatum', 'StörBeginn', 'Störungsende']).size().reset_index(name='count')

    #   df manipulation -> ganze df Records wo nan Values gibt auf null umschreiben
    # df [ pd.isna(df['StörBeginn']) ] = 0

    Vars_func_join_dfs = inspect.currentframe().f_locals
    return df


# join a df to anderen df with selected columns
Var_func_join_to_df = {}


def func_join_to_df(*dfs, **fields):
    global Var_func_join_to_df

    #   fields = { 'f3':'Kettenkunde', 'f4':'Unnamed: 6', 'f5':'Kunde', 'f6':'Unnamed: 8' , 'f7':'RSP-Nummer'} #    df_kundeninfo columns

    df_caller = dfs[0]  # df_joint 3 dfs
    df_other = dfs[1]  # df_kundeninfo

    df_caller = df_caller.drop(columns='count')  # remove last column 'count' exsitence in df_caller

    df_temp = pd.DataFrame()
    df_temp['Service-Meldung'] = df_other['Meldung']
    df_temp['Equipment'] = df_other['Equipment']
    df_temp['ketten_zeich'] = df_other['Unnamed: 6']
    df_temp['InvtNr'] = df_other['InventarNr']

    # manipulate field value  'Walmart' -> 'Walmalrt (WA)'
    df_temp.ketten_zeich[df_temp['ketten_zeich'] == 'Walmart'] = str('Walmalrt (WA)')

    #   join df_temp to df_caller
    df = df_caller.join(df_temp.set_index('Service-Meldung'), on='Service-Meldung', how='left',
                        rsuffix='_K')  # join df_caller and df_temp
    df = df.fillna(0)  # remove NaN values

    ls_other_fields = list()  # field(columns) names of df_kundeninfo
    for value in sorted(fields):
        ls_other_fields.append(fields[value])

    df_other = df_other.iloc[:, :10]  # remove last 4 columns of df_kundeninfo or take only first 10 columns with rows
    df_other = df_other.rename(index=str, columns={"Meldung": "Service-Meldung"})  # rename column name of df_kundeninfo

    df = df_caller.join(df_other.set_index('Service-Meldung'), on='Service-Meldung', how='left',
                        rsuffix='_K')  # join df_caller and df_kundeninfo
    df = df.fillna(0)  # remove NaN values

    ls_caller_columns = list()  # take columns name of df_caller
    for item in df_caller.columns:
        ls_caller_columns.append(item)

    for item in ls_other_fields:  # append some df_kundeninfo columns to df_caller columns
        ls_caller_columns.append(item)

    # df = df.drop(columns='count') # remove last column 'count' exsitence in df_caller
    df = df.groupby(ls_caller_columns).size().reset_index(name='count')

    #  release memory
    del df_temp
    del df_other
    del df_caller

    Var_func_join_to_df = inspect.currentframe().f_locals
    return df


# manipulate df such as falsch values
Vars_func_maintain_df = {}


def func_maintain_df(df_1, df_2):
    global Vars_func_maintain_df

    df_Meldung_Beginn_Ende = df_1.copy(deep=True)
    df_Meldung_Beginn_Ende_json = df_2.copy(deep=True)

    '''
    #       df_Meldung_Beginn_Ende_json Dates correction and gleich convert to standard format "%d.%m.%Y"
    NaT = pd.NaT
    df_Meldung_Beginn_Ende[ (df_Meldung_Beginn_Ende['Meldungsdatum'] ==  NaT) ] = 0
    df_Meldung_Beginn_Ende[ (df_Meldung_Beginn_Ende['StörBeginn'] == NaT) ] = 0
    df_Meldung_Beginn_Ende[ (df_Meldung_Beginn_Ende['Störungsende'] == NaT) ] = 0

    df_Meldung_Beginn_Ende[ (df_Meldung_Beginn_Ende['StörBeginn'] == NaT) ].count()
    '''

    #   df datetime format ändern
    df_Meldung_Beginn_Ende['Meldungsdatum'] = [datetime.strftime(x, "%d.%m.%Y") if not pd.isnull(x) else '' for x in
                                               df_Meldung_Beginn_Ende['Meldungsdatum']]
    df_Meldung_Beginn_Ende['StörBeginn'] = [datetime.strftime(x, "%d.%m.%Y") if not pd.isnull(x) else '' for x in
                                            df_Meldung_Beginn_Ende['StörBeginn']]
    df_Meldung_Beginn_Ende['Störungsende'] = [datetime.strftime(x, "%d.%m.%Y") if not pd.isnull(x) else '' for x in
                                              df_Meldung_Beginn_Ende['Störungsende']]

    df_Meldung_Beginn_Ende_json['Meldungsdatum'] = df_Meldung_Beginn_Ende['Meldungsdatum']
    df_Meldung_Beginn_Ende_json['StörBeginn'] = df_Meldung_Beginn_Ende['StörBeginn']
    df_Meldung_Beginn_Ende_json['Störungsende'] = df_Meldung_Beginn_Ende['Störungsende']

    df_Meldung_Beginn_Ende[(df_Meldung_Beginn_Ende['Meldung'] == 373257)]  # show Meldung Nr Records

    Vars_func_maintain_df = inspect.currentframe().f_locals
    return df_Meldung_Beginn_Ende, df_Meldung_Beginn_Ende_json


# Mean Time to First Failur (MTFF)
Vars_func_MTFF = {}


def func_MTFF(df,
              field_name):  # field_name determiend the field of Start of Stoerung, because of df_temp hier field_name must be 'Störungsbeginn (Dat)_punkt'
    global Vars_func_MTFF

    fieldName = field_name  # in groupby command occurs a problem with '_' in field_name

    '''
    df_MTFF = pd.DataFrame()
    df_MTFF['Installation_Dat'] = df['Fertigungsdatum']
    df_MTFF['Str_beginn'] = df['Störungsbeginn (Dat)']
    df_MTFF['Invt_Nr'] = df['Invt_Nr']
    '''
    # sort values by 'Equipment' and failureStart fields
    df['sorted_Date'] = pd.to_datetime(df[fieldName])
    df = df.sort_values(['Equipment', 'sorted_Date'], ascending=True)
    df = df.reset_index(drop=True)
    df = df.drop(columns='sorted_Date')

    try:
        #   remove rows with 0 or '#' value in filed df_X['GewährlBeginn Datum']  and then ready to calculate df_X['F_t_Fail_time_days']
        df = df[(df['GewährlBeginn Datum'].values != '#')]
        df = df[(df['GewährlBeginn Datum'].values != 0)]
    except ZeroDivisionError as e:
        pass

    df = df.reset_index(drop=True)

    # First Failure Time berechnen
    ls_F_Failure_time = list()
    for i in range(len(df)):
        if all(v == np.empty for v in df.iloc[i].values) is False:
            ls_F_Failure_time.append(abs((datetime.strptime(df[fieldName][i], "%d.%m.%Y") - datetime.strptime(
                df['GewährlBeginn Datum'][i], "%d.%m.%Y")).days))
        else:
            ls_F_Failure_time.append(0)

    df = df.assign(F_t_Fail_time_days=ls_F_Failure_time)  # create new column "F_t_Fail_time_days"
    # df_MTFF_Grp_count = df_MTFF.groupby(['Installation_Dat', 'Str_beginn', 'Invt_Nr', 'F_t_Fail_time_days']).size().reset_index(name = 'count')
    number_of_effective_Meldungen = len(df) - len(
        df[(df['F_t_Fail_time_days'] == 0)].count())  # Anzahl der Equipment ohne leere Meldungsdatum
    MTFF = df[
               'F_t_Fail_time_days'].sum() // number_of_effective_Meldungen  # calculate the Average -> Mean Time to first Failure

    ##MTFF = df['F_t_Fail_time_days'].mean()        # Wegen die Meldungsdatum mit null values diese Method liefert falsche durchschnitt, da es 1084 null values datum gibt
    # Histogram and Density Diagramm
    plt.figure(1)
    plt.xlabel('First time to Failure-> Days')
    plt.ylabel('number of devices')
    df['F_t_Fail_time_days'].hist()
    plt.title('First time to failure Histogram')
    plt.grid(True)
    plt.figure(2)
    plt.xlabel('Days')
    plt.title('First Time to Failure Density Diagram')
    plt.subplot(211, facecolor='W')
    df['F_t_Fail_time_days'].plot(kind='Kde')  # Density Diagramm
    plt.figure(3)
    plt.xlabel('Days')
    plt.ylabel('Device indexes')
    plt.title('First Time to Failure line Diagramm Devices -> 400 bis 900')
    df['F_t_Fail_time_days'][400:900].plot(kind='line', color='B')
    plt.show()
    # Line Diagram sorted Values
    df_first_time_to_failure_sorted = df.sort_values('F_t_Fail_time_days', ascending=True)
    plt.figure(4)
    df_first_time_to_failure_sorted['F_t_Fail_time_days'][400:500].plot(style=':', color='m')
    plt.show()

    print("Anzahl der Meldungen: %d" % df['count'].sum())
    print("Anzahl der Geräte: %d" % len(df))

    Vars_func_MTFF = inspect.currentframe().f_locals
    return MTFF, df


Vars_func_MTFF_nach_Land = {}


def func_MTFF_nach_Land(df,
                        field_name):  # field_name determiend the field of Start of Stoerung, because of df_temp hier field_name must be 'Störungsbeginn (Dat)_punkt'
    global Vars_func_MTFF_nach_Land

    fieldName = field_name  # in groupby command occurs a problem with '_' in field_name

    df_MTFF_nach_Land = df.copy(deep=True)
    # nach land
    df_MTFF_nach_Land = df_MTFF_nach_Land.sort_values('Land', ascending=True)

    df_MTFF_nach_Land = df_MTFF_nach_Land.reset_index(drop=True)

    df_MTFF_nach_Land = df_MTFF_nach_Land.groupby(
        ['Service-Meldung', 'Equipment', 'Land', 'GewährlBeginn Datum', fieldName]).size().reset_index(name='count')

    df_MTFF_nach_Land = df_MTFF_nach_Land.drop(columns='count')

    df_MTFF_nach_Land = df_MTFF_nach_Land.groupby(
        ['Equipment', 'Land', 'GewährlBeginn Datum', fieldName]).size().reset_index(name='count')

    number_of_Meldungen = df_MTFF_nach_Land['count'].sum()

    print("number of Meldungen: %d " % number_of_Meldungen)

    df_MTFF_nach_Land = df_MTFF_nach_Land.sort_values(fieldName, ascending=True)

    # sort values by 'Equipment' and failureStart fields
    df_MTFF_nach_Land['sorted_Date'] = pd.to_datetime(df_MTFF_nach_Land[fieldName])
    df_MTFF_nach_Land = df_MTFF_nach_Land.sort_values(['Equipment', 'sorted_Date'], ascending=True)
    df_MTFF_nach_Land = df_MTFF_nach_Land.reset_index(drop=True)
    df_MTFF_nach_Land = df_MTFF_nach_Land.drop(columns='sorted_Date')

    df_MTFF_nach_Land = df_MTFF_nach_Land.drop_duplicates('Equipment', keep='first')

    df_MTFF_nach_Land = df_MTFF_nach_Land.sort_values('Land', ascending=True)

    df_MTFF_nach_Land = df_MTFF_nach_Land.reset_index(drop=True)

    #   remove rows with 0 or '#' value in filed df_X['GewährlBeginn Datum']  and then ready to calculate df_X['F_t_Fail_time_days']
    df_MTFF_nach_Land = df_MTFF_nach_Land[(df_MTFF_nach_Land['GewährlBeginn Datum'].values != '#')]
    df_MTFF_nach_Land = df_MTFF_nach_Land[(df_MTFF_nach_Land['GewährlBeginn Datum'].values != 0)]
    df_MTFF_nach_Land = df_MTFF_nach_Land.reset_index(drop=True)

    ls_F_Failure_time = list()
    for i in range(len(df_MTFF_nach_Land)):
        if all(v == np.empty for v in df_MTFF_nach_Land.iloc[i].values) is False:
            ls_F_Failure_time.append(abs((datetime.strptime(df_MTFF_nach_Land[fieldName][i],
                                                            "%d.%m.%Y") - datetime.strptime(
                df_MTFF_nach_Land['GewährlBeginn Datum'][i], "%d.%m.%Y")).days))
        else:
            ls_F_Failure_time.append(0)

    df_MTFF_nach_Land = df_MTFF_nach_Land.assign(
        F_t_Fail_time_days=ls_F_Failure_time)  # create new column "F_t_Fail_time_days"

    number_of_effective_Meldungen = len(df_MTFF_nach_Land) - len(
        df_MTFF_nach_Land[(df_MTFF_nach_Land['F_t_Fail_time_days'] == 0)].count(1))
    print("number effective of Meldungen: %d " % number_of_effective_Meldungen)

    # df_test = df_test.dropna(how='any', axis=0)       # remove all rows from df in which one of the columns has a damy of value -> np.NaN

    df_MTFF_nach_Land = df_MTFF_nach_Land[(df_MTFF_nach_Land[
                                               'F_t_Fail_time_days'] != 0)]  # remove rows from df in which one of the columns has a value of 0

    df_MTFF_nach_Land = df_MTFF_nach_Land.drop(columns='count')

    df_MTFF_nach_Land = df_MTFF_nach_Land.groupby(['Land', 'F_t_Fail_time_days']).size().reset_index(name='count')

    df_MTFF_nach_Land = df_MTFF_nach_Land.groupby(['Land']).agg(
        {'F_t_Fail_time_days': {'mean_failure_time': 'mean'}, 'count': {'sum_count': 'sum'}})

    #   Barchart:
    '''
    fig, ax = plt.subplots()    #   ax : matplotlib axes object, default None
    index = df_MTFF_nach_Land.index
    bar_width = 0.35

    mean = df_MTFF_nach_Land['F_t_Fail_time_days'].values

    count = df_MTFF_nach_Land['count'].values

    opacity = 0.4
    error_config = {'ecolor':'0.3'}
    rects1 = ax.bar(index, mean, bar_width, alpha=opacity, color='b', error_kw=error_config, label='Mean time to failure')
    rects2 = ax.bar(index, count, bar_width, alpha=opacity, color='r', error_kw=error_config, label='number of Equipment')

    ax.set_xlabel('Land')
    ax.set_ylabel('amount')
    ax.set_title('Mean time to first Failure by country')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(str(index))
    ax.legend()

    fig.tight_layout()
    plt.show()
    '''

    #   Barchart
    plot = df_MTFF_nach_Land.plot.bar(figsize=(85, 35), fontsize=25, rot=85)
    plt.title('Mean time to first Failure by country')
    plt.xlabel('Länder')
    plt.legend = True
    plt.loglog = True
    plt.sort_columns = True
    fig = plot.get_figure()
    fig.savefig(fname='Mean_time_to_first_Failure_by_Land_barchart_autosave.jpg', dpi=95, quality=95)
    plt.close(fig)  # save chart but not show

    #   Pie chart
    plot = df_MTFF_nach_Land.plot(figsize=(85, 55), fontsize=15, rot=85, kind='pie', subplots=True)
    plt.title('Mean time to first Failure by country pie chart')
    plt.xlabel('Länder')
    plt.legend = True
    plt.loglog = True
    plt.sort_columns = True
    # fig = plot.imag()
    plt.savefig(fname='MTFF_by_Land_Pie_chart_autosave.jpg', dpi=95, quality=95)
    plt.close()

    # df_MTFF_nach_Land.plot(figsize=(35,35), fontsize=15, rot=85, kind='scatter', x = df_MTFF_nach_Land['F_t_Fail_time_days'], y =df_MTFF_nach_Land.index)
    write_to_excel(df_MTFF_nach_Land, data_path, file_name='MTFF_nach_Land.xlsx',
                   sheet_name='2009-' + str(current_year))

    Vars_func_MTFF_nach_Land = inspect.currentframe().f_locals
    return True


Vars_func_MTFF_nach_X = {}


def func_MTFF_nach_X(df_X, field_name, failure_start_field_name):
    global Vars_func_MTFF_nach_X

    # field_name is MTFF by field_name
    field = field_name

    # failure_start_field_name determiend the field of Start of Failure, entweder 'Störungsbeginn (Dat)_punkt' oder 'Meldungsdatum'
    failureStart = failure_start_field_name  # in groupby command occurs a problem with '_' in failure_start_field_name
    df_X = df_X.drop(columns='count')  # remove count from df_sorted

    # nach X
    df_X = df_X.sort_values(field, ascending=True)

    df_X = df_X.reset_index(drop=True)

    df_X = df_X.groupby(
        ['Service-Meldung', 'Equipment', field, 'GewährlBeginn Datum', failureStart]).size().reset_index(name='count')

    number_of_Equipment = df_X['Equipment'].count()
    number_of_Meldungen = df_X['count'].sum()

    df_X = df_X.drop(columns='count')

    df_X = df_X.groupby(['Equipment', field, 'GewährlBeginn Datum', failureStart]).size().reset_index(name='count')

    #   Anzahl der Meldungen überprüfen
    df_X[(df_X['Equipment'] == 2248822)]['count'].sum()

    # number_of_Meldungen = df_X['count'].sum()

    print("number of Meldungen: %d " % number_of_Meldungen)

    df_X = df_X.sort_values(failureStart, ascending=True)

    # sort values by 'Equipment' and failureStart fields
    df_X['sorted_Date'] = pd.to_datetime(df_X[failureStart])
    df_X = df_X.sort_values(['Equipment', 'sorted_Date'], ascending=True)
    df_X = df_X.reset_index(drop=True)
    df_X = df_X.drop(columns='sorted_Date')

    df_X = df_X.drop_duplicates('Equipment', keep='first')

    # number_of_Equipment = df_X['Equipment'].count()
    print("Anzahl der Geräte: %d devices" % number_of_Equipment)

    df_X = df_X.sort_values(field, ascending=True)

    df_X = df_X.reset_index(drop=True)

    # test = df_sorted[df_sorted.index ==343676]     # hier verursacht eine ' 'int' object is not itterable' error, da die field value df_X['GewährlBeginn Datum'] ist 0

    try:
        #   remove rows with 0 or '#' value in filed df_X['GewährlBeginn Datum']  and then ready to calculate df_X['F_t_Fail_time_days']
        df_X = df_X[(df_X['GewährlBeginn Datum'].values != '#')]
        df_X = df_X[(df_X['GewährlBeginn Datum'].values != 0)]
    except ZeroDivisionError as e:
        pass

    df_X = df_X.reset_index(drop=True)

    ls_F_Failure_time = list()
    for i in range(len(df_X)):
        if all(v == np.empty for v in df_X.iloc[i].values) is False:
            ls_F_Failure_time.append(abs((datetime.strptime(df_X[failureStart][i], "%d.%m.%Y") - datetime.strptime(
                df_X['GewährlBeginn Datum'][i], "%d.%m.%Y")).days))
        else:
            ls_F_Failure_time.append(0)

    df_X = df_X.assign(F_t_Fail_time_days=ls_F_Failure_time)  # create new column "F_t_Fail_time_days"

    number_of_effective_Meldungen = len(df_X) - len(df_X[(df_X['F_t_Fail_time_days'] == 0)].count(1))
    print("number of effective Meldungen: %d " % number_of_effective_Meldungen)
    MTFF = df_X[
               'F_t_Fail_time_days'].sum() // number_of_effective_Meldungen  # calculate the Average -> Mean Time to first Failure
    print(
        "Mean Time to First Failure: %.3f days" % MTFF)  # df_test = df_test.dropna(how='any', axis=0)       # remove all rows from df in which one of the columns has a damy of value -> np.NaN

    df_X = df_X[(df_X['F_t_Fail_time_days'] != 0)]  # remove rows from df in which one of the columns has a value of 0

    df_X = df_X.drop(columns='count')

    df_X = df_X.groupby([field, 'F_t_Fail_time_days']).size().reset_index(name='count')

    df_X = df_X.groupby([field]).agg(
        {'F_t_Fail_time_days': {'mean_failure_time': 'mean'}, 'count': {'sum_count': 'sum'}})

    ''' #   27.11.2018
    #   Bar chart:
    plot = df_X.plot.bar(figsize=(85,35), fontsize=15, rot=85)
    plt.xlabel(field)
    plt.legend=True
    plt.loglog=True
    plt.sort_columns=True
    fig = plot.get_figure()
    fig.savefig(fname='MTFF_'+field+'_barchart_autosave.jpg', dpi=95, quality=95)
    plt.close(fig)  # save chart but not show


    #   Pie chart
    plot = df_X.plot(figsize=(85,55), fontsize=15, rot=85, kind='pie', subplots=True)
    plt.title('Mean time to first Failure by '+field + ' pie chart')
    plt.xlabel(field)
    plt.legend=True
    plt.loglog=True
    plt.sort_columns=True
    plt.savefig(fname='MTFF_by_'+field+'_Pie_chart_autosave.jpg', dpi=95, quality=95)
    plt.close()

    #   27.11.2018 '''

    if field_name == str('Baugruppe'):
        df_X = func_manipulate_df(df_X)
        # correct the columns name:
        # df_X.columns
        # output ->  Index(['('F_t_Fail_time_days', 'mean_failure_time')', '('count', 'sum_count')'], dtype='object')
        print("manipulate df_X")
        df_X.columns = ['F_t_Fail_time_days', 'count']
        # df_X = df_X.rename(index=str, columns={"('F_t_Fail_time_days', 'mean_failure_time')" : "F_t_Fail_time_days"})
        # df_X = df_X.rename(index=str, columns={"('count', 'sum_count')" : "count"})

    # df_MTFF_nach_Land.plot(figsize=(35,35), fontsize=15, rot=85, kind='scatter', x = df_MTFF_nach_Land['F_t_Fail_time_days'], y =df_MTFF_nach_Land.index)
    write_to_excel(df_X, data_path, file_name='MTFF_nach_' + field + '.xlsx', sheet_name='2009-' + str(current_year))

    Vars_func_MTFF_nach_X = inspect.currentframe().f_locals
    return number_of_Meldungen, number_of_Equipment, MTFF, df_X


def func_manipulate_df(df):
    df = df[(df.index.str[0:4] != '9999')]
    '''
    # If df is df_Baugruppe remove '9999.*' from df_X , '9999' is Fahrzeiten
    # ^ or under code
    # df = df.drop(df[ (df.index.str[0:4]=='9999')].index )
    # pattern = string.ascii_letters
    # ^ Out[384]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
    '''
    df_temp = pd.DataFrame()
    for i in range(len(df)):
        find_string = re.search('[*a-z*A-Z0-9#]', df.index[i])
        string_set = find_string.group(0)  # first char of search by pattern in index
        if string_set.isdigit():  # check if first char is digit
            df_temp = df_temp.append(df.iloc[i, :])  # make a new df contain of only correct Baugruppe

    # correct the columns name:
    # df_X.columns
    # output ->  Index(['('F_t_Fail_time_days', 'mean_failure_time')', '('count', 'sum_count')'], dtype='object')
    # print("manipulate df_temp")
    # df_temp = df_temp.rename(index=str, columns={"('F_t_Fail_time_days', 'mean_failure_time')" : "F_t_Fail_time_days"})
    # df_temp = df_temp.rename(index=str, columns={"('count', 'sum_count')" : "count"})

    return df_temp


Vars_func_filter_nach_X = {}


def func_filter_nach_X(df, col, val, op):
    global Vars_func_filter_nach_X
    import operator
    ops = {'eq': operator.eq, 'neq': operator.ne, 'gt': operator.gt, 'lt': operator.lt, 'le': operator.le}
    df = df[ops[op](df[col], val)]
    # df = df[ ( df['Land']== 'USA' ) & ( df['ketten_zeich']== 'Walmart (WA)' ) ]
    # df = df[ ( np.logical_and(*param) ) ]
    Vars_func_filter_nach_X = inspect.currentframe().f_locals
    return df


#   df_test = func_filter_nach_X(df_sorted, 'Land', 'Iran', 'eq')   #'eq' b.d. equal

Vars_func_filter_nach_XY = {}


def func_filter_nach_XY(df, col, val):
    global Vars_func_filter_nach_XY
    df = df[(df[col].isin(val))]
    #   df_test = df_sorted[ ( df_sorted.Land.isin( ['USA', 'Polen']) ) ]
    Vars_func_filter_nach_XY = inspect.currentframe().f_locals
    return df


#   df_test = func_filter_nach_XY(df_sorted, 'Land', ['USA','Polen'])
#   df_test = func_filter_nach_XY(df_sorted, 'Land', 'USA','Polen')   -> with call parameter *val , isin([*val])


def func_prepair_new_Daten_strukture(*dfs, **fields):
    df_caller = dfs[0]  # df_sorted
    df_other = dfs[1]  # df_kundeninfo

    df_caller = df_caller[(df_caller['ketten_zeich'] == 'Walmart (WA)')]
    df_other = df_other[(df_other['Unnamed: 6'] == 'Walmart')]

    return df


'''
# How to use class Feature_selection
# create an object of class
ml = Feature_selection(df = df_sorted.copy(deep=True))
oder
ml = Feature_selection(df_sorted)

# Use method of class
df_Equipment = Feature_selection.prepare_df(ml, 1)

# Use method of object of class
df_Stoerungen = ml.prepare_df(index_item=2)

'''


# feature_sel = Feature_selection(df_sorted) # create an Object of class
# df_Equipment = feature_sel.prepare_df(index_item = 1)
# df_Stoerungen = Feature_selection.prepare_df(feature_sel, 2)

# object is one of the instances of the class
class Feature_selection(object):
    # self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class
    # as df call df_sorted
    def __init__(self, df):
        # self._df = df indem _df wird auf der Stack definiert und nach dem authomatisch geht raus auf dem Stack
        self.df = df
        self.field_names = ['GewährlBeginn Datum', 'Störungsbeginn (Dat)_punkt']
        self.ls_fields = ['Service-Meldung', 'Equipment', 'Störungsbeginn (Dat)_punkt']

        # df_Equipment = self.prepare_df(index_item=1)
        # df_Stoerungen = self.prepare_df(index_item=2)

    def prepare_df(self, index_item):
        first_timer = datetime.now()
        df = self.df
        field_names = self.field_names
        ls_fields = self.ls_fields

        # field_names[0] -> 'GewährlBeginn Datum'
        try:
            #   remove rows with 0 or '#' value in filed df['GewährlBeginn Datum']  and then ready to calculate df_X['F_t_Fail_time_days'] and convert columns to to_datetime
            df = df[(df[field_names[0]].values != '#')]
            df = df[(df[field_names[0]].values != 0)]
        except ZeroDivisionError as e:
            pass

        # create new datetime columns to calculate Failure_time
        df['sorted_Installation'] = pd.to_datetime(df[field_names[0]])
        df['sorted_Störungsbegin'] = pd.to_datetime(df[field_names[1]])

        df = df.drop(columns='count')  # remove count from df_sorted
        # sorting nach index_item
        df = df.sort_values(ls_fields[index_item], ascending=True)
        df = df.reset_index(drop=True)

        ls_F_Failure_time = list()
        for i in range(len(df)):
            if all(v == np.empty for v in df.iloc[i].values) is False:
                ls_F_Failure_time.append(abs(df['sorted_Störungsbegin'][i] - df['sorted_Installation'][i]).days)
            else:
                ls_F_Failure_time.append(0)

        df = df.assign(Failure_time=ls_F_Failure_time)  # create new column "Failure_time"

        # ls_fields[index_item] is 'Service-Meldung' or 'Equipment' or items in ls_fields
        if index_item == 2:
            df = df.groupby(['sorted_Störungsbegin', 'Failure_time']).size().reset_index(
                name='count')  # mean of sum of the Equipment
            df = df.sort_values('sorted_Störungsbegin', ascending=True)
            df = df.set_index('sorted_Störungsbegin')
            df = df.resample('M').mean()  # upsampling und calculate mean 'Failure_time' und 'count'
            df = df.interpolate(method='linear')  # fill the empty monthes with linear method
            df = df.iloc[:-1, :]  # remove last row contain of current month
        else:
            df = df.groupby([ls_fields[index_item], 'Failure_time']).size().reset_index(name='count')
            df = df.sort_values('Failure_time', ascending=True)

        second_timer = datetime.now()
        print("read JSON successful in %s time" % (second_timer - first_timer))

        return df

    # Feature_selection.plot_Outliers(feature_sel, dataset) then musst be #df = df.drop(columns='count') done write
    def plot_Outliers(self, df):
        # df = df.drop(columns='count')
        annual_groups = df.groupby(pd.Grouper(freq='A'))  # Annualy grouper
        n_groups = len(annual_groups)
        years = pd.DataFrame()
        for name, group in annual_groups:
            # years[name.year]=group.agg('mean') #    mean Average
            if len(group.values) is 12:
                years[name.year] = group.values.tolist()  # convert each columns value to list
                years[name.year] = years[name.year].str.get(
                    0)  # convert each columns value to value remove square bracket [] from values

        years.boxplot()
        pyplot.show()

        return True

    def walk_forward_validation(self, X, best_cfg, bias):
        # Walk-forward validation
        train_size = int(len(X) * 0.50)
        train, test = X[0:train_size], X[train_size:]
        history = [x for x in train]
        predictions = list()
        # bias = bias
        for i in range(len(test)):
            # predict
            model = ARIMA(history, order=best_cfg)
            model_fit = model.fit(trend='nc', disp=0)
            yhat = bias + float(model_fit.forecast()[0])
            predictions.append(yhat)
            # observation compare last in train wirh first in test
            obs = test[i]
            history.append(obs)
        # summarize residual errors
        residuals = [test[i] - predictions[i] for i in range(len(test))]
        residuals = pd.DataFrame(residuals)
        # report performance
        print(residuals.describe())
        bias = residuals.describe()[0]  # Series with shape (8,)

        # save bias
        df_bias = pd.DataFrame(bias)
        func_write_df_to_JSON(df_bias, 'df_bias')  # save to JSON
        write_to_excel(df_bias, data_path, 'df_bias.xlsx', 'df_bias')  # save to Excel

        # bias is mean in residuals.describe -> bias[1]
        print('bias= %.3f' % bias[1])
        pyplot.figure()
        pyplot.subplot(211)
        residuals.hist(ax=pyplot.gca())
        pyplot.subplot(212)
        residuals.plot(kind='kde', ax=pyplot.gca())
        pyplot.show()
        # bias is mean in residuals.describe -> bias[1]
        return bias[1]

    # Feature_selection.arima(feature_sel, df_Stoerungen)
    def arima(self, df):
        df = df.drop(columns='count')
        # autocorrelation plot df_Stoerungen
        autocorrelation_plot(df)
        pyplot.title('Autocorrelation plot Time to Failure')
        pyplot.show()
        # Running the Test-Harness
        split_point = len(df) - 10
        dataset, validation = df[0:split_point], df[split_point:]
        write_to_excel(dataset, data_path, 'dataset.xlsx', 'Trainingsdata')
        write_to_excel(validation, data_path, 'validation.xlsx', 'Validationsdata')
        # Prepare data
        X = dataset.values
        X = X.astype('float32')
        # Walk-forward validation
        train_size = int(len(X) * 0.50)
        train, test = X[0:train_size], X[train_size:]
        history = [x for x in train]
        predictions = list()
        for i in range(len(test)):
            # predict
            yhat = history[-1]  # last row in list from train data
            predictions.append(yhat)
            # observation compare last in train wirh first in test
            obs = test[i]
            history.append(obs)
            print('>Predicted=%.3f, Expected=%3.f' % (yhat, obs))
        # report performance
        rmse = sqrt(mean_squared_error(test, predictions))
        print('RMSE: %.3f' % rmse)

        # summary statistics of dataset Time series
        print(dataset.describe())

        # line plot of Time series (dataset)
        dataset.plot()
        pyplot.show()

        # Density plot of time series datatset
        pyplot.figure(1)
        pyplot.subplot(211)
        dataset.hist()
        pyplot.show()
        pyplot.subplot(212)
        dataset.plot(kind='kde')
        pyplot.show()

        # plot boxplot die whisker and outliers
        self.plot_Outliers(dataset)

        # Manually Configuring ARIMA(Autoregressive Integrated Moving Average)
        # difference data
        stationary = self.difference(X)
        stationary.index = dataset.index[1:]
        # check if stationary
        result = adfuller(stationary)
        print('ADF Statistic: %f' % result[0])
        print('P-value: %f' % result[1])
        print('Critical Values: ')
        for key, value in result[4].items():
            print('\t%s: %.3f' % (key, value))
        # plot differenced data
        stationary = stationary.str.get(0)  # remove square bracket from df stationary
        stationary.plot()
        pyplot.show()
        # save
        func_write_df_to_JSON(stationary, 'stationary')

        # ACF(Autocorrelation Function) and PACF(Partial Autocorrelation Function) plot
        pyplot.figure()
        pyplot.subplot(211)
        plot_acf(dataset, ax=pyplot.gca())
        pyplot.show()  # plot separate ACF and PACF
        pyplot.subplot(212)
        plot_pacf(dataset, ax=pyplot.gca())
        pyplot.show()

        # evaluate parameters
        p_values = range(0, 4)
        d_values = range(0, 3)
        q_values = range(0, 4)

        best_cfg = self.evaluate_models(dataset.values, p_values, d_values, q_values)
        print('best_cfg= ', best_cfg)

        bias = self.walk_forward_validation(X, best_cfg, bias=0)  # first run without bias
        # bias is mean in residuals.describe -> bias[1]
        # second times bias is available
        bias = self.walk_forward_validation(X, best_cfg, bias)

        # finalize to save model
        self.finalize_model(X, bias, best_cfg)

        # make prediction with load saved model
        self.make_prediction(bias)

        # save best_cfg in form of string
        lst_best_cfg = list()  # create list
        lst_best_cfg.append(str(best_cfg))  # append string to list
        df_best_cfg = pd.DataFrame()  # create dataframe
        df_best_cfg[0] = lst_best_cfg  # assign first row to list
        func_write_df_to_JSON(df_best_cfg, 'df_best_cfg')  # save to JSON
        write_to_excel(df_best_cfg, data_path, 'df_best_cfg.xlsx', 'best_cfg')  # save to Excel

        # Make validation
        y, predictions = self.make_validation()

        '''#   distribute predictions to the end of y as validation set
        ls_y = list(y)
        ls_y = ls_y + predictions[-4:]
        # convert list to Series
        sr_y = Series(ls_y)
        # convert to DataFrame without columns name, only values
        validation = pd.DataFrame(sr_y.values.astype('float32'))
        #   save y as new validation
        write_to_excel(validation, data_path , 'validation.xlsx', 'Validationsdata')

        # Make new validation with longer validation
        y, predictions = self.make_validation()
        '''  # ende distribution validation

        return True

    def make_validation(self):
        # load validation dataframe
        validation = pd.read_excel('validation.xlsx')
        y = validation.values.astype('float32')
        # load dataset contain of Train and Test Data
        dataset = pd.read_excel('dataset.xlsx')
        X = dataset.values.astype('float32')
        train_size = int(len(X) * 0.50)
        train, test = X[0:train_size], X[train_size:]
        history = [x for x in train]
        predictions = list()

        # load bias
        bias = np.load('model_bias.npy')

        # load best_cfg
        df_best_cfg = pd.read_json('df_best_cfg.JSON')
        # df_best_cfg = pd.read_excel('df_best_cfg.xlsx') # or read from Excel file
        best_cfg = ast.literal_eval(df_best_cfg[0][0])

        # load model
        model_fit = ARIMAResults.load('model.pkl')
        # make first prediction
        predictions = list()
        yhat = bias + float(model_fit.forecast()[0])
        predictions.append(yhat)
        history.append(y[0])
        print('<Predictions=%.3f, Expected=%3.f' % (yhat, y[0]))
        # rolling forecasts in validation
        for i in range(1, len(y)):
            # predict
            model = ARIMA(history, order=best_cfg)
            model_fit = model.fit(trend='nc', disp=0)
            yhat = bias + float(model_fit.forecast()[0])
            predictions.append(yhat)
            # observation
            obs = y[i]
            history.append(obs)
            print('=> Prognose=%.3f, Erwartet=%3.f' % (yhat, obs))
        # report performance
        rmse = sqrt(mean_squared_error(y, predictions))
        print('RMSE: %.3f' % rmse)

        # save predictions
        df_predictions = pd.DataFrame(predictions)
        func_write_df_to_JSON(df_predictions, 'df_predictions')  # save to JSON
        write_to_excel(df_predictions, data_path, 'df_predictions.xlsx', 'df_predictions')  # save to Excel

        # first plot
        pyplot.plot(y, color='blue')
        pyplot.plot(predictions, color='red')
        pyplot.show()

        # second plot
        f = Figure(figsize=(5, 5), dpi=100)
        a = plt.subplot()
        a.clear()
        a.plot(y, "#00A3E0", label='Erwartet')
        a.plot(predictions, color='red')
        a.set_title('Time to Failure Prognose Diagramm')
        a.set_xlabel('Monat')
        a.set_ylabel('Tagen')
        a.label_outer()

        # third plot
        plt.figure(1)
        plt.subplot(211)
        plt.plot(y, "#00A3E0", label='Erwartet')
        plt.plot(predictions, color='red', label='Prognose')
        plt.yscale('linear')
        plt.title('Time to Failure Prognose Diagramm')
        plt.grid(True)
        # f.tight_layout()
        plt.show()

        # plot for tkinter
        f = Figure(figsize=(5, 5), dpi=100)
        f.suptitle('test subtitle')
        a = f.add_subplot(111)
        # a.clear()
        pyplot.plot(y, label='validation')
        a.plot(y, "#00A3E0", label='Erwartet')
        a.plot(predictions, color='blue', label='Prognose')
        a.set_title('Time to Failure Prognose Diagramm')
        a.set_xlabel('Jahren')
        pyplot.show()

        # plot train and test results
        pyplot.plot(train)
        # pyplot.plot(test)
        # pyplot.plot(y)
        # pyplot.plot(predictions)
        # pyplot.plot([None for i in train] + [x for x in test])
        pyplot.plot([None for i in test] + [x for x in y])
        # pyplot.plot([None for i in y] + [x for x in predictions])
        pyplot.show()

        # plot predictions and expected results
        pyplot.plot(y)
        # pyplot.plot(predictions)
        # pyplot.plot([None for i in train] + [x for x in test])
        # pyplot.plot([None for i in test] + [x for x in y])
        pyplot.plot([None for i in y] + [x for x in predictions])
        pyplot.show()

        # scipy.linear Algebra.norm
        norm(predictions)

        # save prediction
        df_predictions = pd.DataFrame(predictions)
        func_write_df_to_JSON(df_predictions, 'df_predictions')

        return y, predictions

    def finalize_model(self, X, bias, best_cfg):
        # save best_cfg
        lst_best_cfg = list()  # create list
        lst_best_cfg.append(str(best_cfg))  # append string to list
        df_best_cfg = pd.DataFrame()  # create dataframe
        df_best_cfg[0] = lst_best_cfg  # assign first row to list
        func_write_df_to_JSON(df_best_cfg, 'df_best_cfg')  # save to JSON
        write_to_excel(df_best_cfg, data_path, 'df_best_cfg.xlsx', 'best_cfg')  # save to Excel

        # save bias
        np.save('model_bias.npy', [bias])
        model = ARIMA(X, order=best_cfg)
        model_fit = model.fit(trend='nc', disp=0)
        # save model
        model_fit.save('model.pkl')
        return True

    def make_prediction(self, bias):
        # load finalized model and make a prediction
        model_fit = ARIMAResults.load('model.pkl')
        # show model_fit summary:
        model_fit.summary()
        model_fit.summary2()
        bias = np.load('model_bias.npy')
        # show saved bias
        print('saved bias= %.4f' % bias)
        yhat = bias + float(model_fit.forecast()[0])
        print('Predicted: %.3f' % yhat)
        return True

    # evaluate an ARIMA model for a given order (p,d,q) and return RMSE
    def evaluate_arima_models(self, X, arima_order):
        # X = dataset.values # dataset ist series contains Test and Train data
        # X = X.astype('float32')
        # Walk-forward validation
        train_size = int(len(X) * 0.50)
        train, test = X[0:train_size], X[train_size:]
        # history = np.array(train) # oder below two line code
        history = [x for x in train]  # history is list
        # history = np.asarray(history) # convert list to array float32 necessary for ARIMA
        # make predictions
        predictions = list()
        for t in range(len(test)):
            model = ARIMA(history, order=arima_order)
            # model_fit = model.fit(disp=0)
            # disable the automatic addition of a trend constant from the model
            # by setting the trend argument to nc for no constant when calling fit()
            model_fit = model.fit(trend='nc', disp=0)
            yhat = model_fit.forecast()[0]
            predictions.append(yhat)
            # history.append(test[t]) # observation obs # np.ndarray has no attribute append, solve this problem as below:
            history = np.append(history, test[t])

        # reconvert history to list
        # history = history.tolist()
        # calculate combinations of p, d and q values for an ARIMA model

        # convert prediction list to array
        # predictions = np.asarray(predictions)
        # convert predictions float64 to float32
        # predictions = predictions.astype('float32')

        rmse = sqrt(mean_squared_error(test, predictions))  # y_true, y_pred
        # print('rmse=%.3f' % rmse)
        return rmse

    # evaluate combination of p, d and q values for an ARIMA model
    def evaluate_models(self, dataset, p_values, d_values, q_values):
        dataset = dataset.astype('float32')
        best_score, best_cfg = float("inf"), None  # best_cfg is ARIMA order -> p,d,q
        for p in p_values:
            for d in d_values:
                for q in q_values:
                    order = (p, d, q)
                    # print('order= ', order) # test all orders
                    try:
                        rmse = self.evaluate_arima_models(dataset, order)
                        if rmse < best_score:
                            best_score, best_cfg = rmse, order
                            print('ARIMA%s RMSE=%.3f' % (order, rmse))
                    except:
                        continue
        print('Best ARIMA%s RMSE=%.3f' % (best_cfg, best_score))

        return best_cfg

    # create a differenced series
    def difference(self, dataset):
        diff = list()
        for i in range(1, len(dataset)):
            value = dataset[i] - dataset[i - 1]
            diff.append(value)

        return Series(diff)

    def univariate_selection(self, k):
        # df = df_sorted[df_sorted['Land']=='Polen']
        # df manipulation
        df = self.df
        df['Fertigungsdatum'] = pd.to_datetime(df['Fertigungsdatum'])
        df = df.drop(columns='Störungsbeginn (Dat)')
        df['Störungsbeginn (Dat)_punkt'] = pd.to_datetime(df['Störungsbeginn (Dat)_punkt'])
        df['Meldungsdatum'] = pd.to_datetime(df['Meldungsdatum'])
        df['StörBeginn'] = pd.to_datetime(df['StörBeginn'])
        df['Störungsende'] = pd.to_datetime(df['Störungsende'])

        X = df.iloc[:, 0:19]
        Y = df.iloc[:, 19]
        test = SelectKBest(score_func=chi2, k=10)
        fit = test.fit(X, Y)
        np.set_printoptions(precision=3)
        print(fit.score_)
        feature = fit.transform(X)
        return feature


'''
Anwendung der Forecast:

forecast = Forecast(df = df_Stoerungen)

'''


class Forecast(object):
    def __init__(self, df):
        self.df = df

    def make_forecast(self, epoch, unit, out_unit):
        df = self.df

        print(tf.VERSION)
        print(tf.keras.__version__)

        model = tf.keras.Sequential()
        # create layers:
        model.add(layers.Dense(unit, activation='relu'))  # unit = 64
        model.add(layers.Dense(unit, activation='relu'))  # unit = 64
        model.add(layers.Dense(out_unit, activation='softmax'))  # out_unit = 10

        # configure the layers
        layers.Dense(64, activation='sigmoid')
        # Or:
        # layers.Dense(64, activation=tf.sigmoid)
        layers.Dense(64, kernel_regularizer=tf.keras.regularizers.l1(0.01))
        layers.Dense(64, bias_regularizer=tf.keras.regularizers.l2(0.01))
        layers.Dense(64, kernel_initializer='orthogonal')
        layers.Dense(64, bias_initializer=tf.keras.initializers.constant(2.0))

        # Set up training
        model.compile(optimizer=tf.train.AdamOptimizer(0.001),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

        model.compile(optimizer=tf.train.AdamOptimizer(0.01),
                      loss='mse',
                      metrics=['mae'])

        model.compile(optimizer=tf.train.RMSPropOptimizer(0.01),
                      loss=tf.keras.losses.categorical_crossentropy,
                      metrics=[tf.keras.metrics.categorical_accuracy])

        tens = len(df) * 10 // 100
        data = df.iloc[:-tens, :]
        two_thirds = len(df) * 2 // 3
        labels = np.random.random(two_thirds)

        val_data = df.iloc[-tens:, :]
        thirds = len(df) // 3
        val_labels = np.random.random(thirds)

        model.fit(data, labels, epochs=epoch, batch_size=32,
                  validation_data=(val_data, val_labels))

        return df

def write_df_to_HDF5(df, filename ,output_path=None, mode=None):
    first_timer = datetime.now()
    if mode is None:
        mode='w'
    if output_path is None:
        output_path = data_path
    try:
        df.to_hdf(output_path +'HDF5_'+ str(filename) + '.h5', key='hdf5_' + str(filename),
                  mode=mode)  # write dataframe to HDF5 format with '.h5' Extenssion
        second_timer = datetime.now()
        running_time = second_timer - first_timer
        print("Convert dataframe '{}' to HDF5 as filename '{}.h5' Format \n in path '{}' with '{}' time succesfull completed!".format(df, filename, output_path, running_time))
        return True
    except NameError as e:
        print("Sorry! converting dataframe '{}' to HDF5 as filename '{}.h5' Format \n in path '{}' was wrong! Check output path and dataframe".format(df, filename, output_path))
        return False

def read_HDF(filename, input_path=None, key=None , mode=None):
    first_timer = datetime.now()
    if mode is None:
        mode = 'r'
    if input_path is None:
        input_path = data_path
    try:
        hdf = pd.read_hdf(str(input_path) + 'HDF5_' + str(filename) + '.h5', key=key, mode=mode)
        second_timer = datetime.now()
        running_time = second_timer - first_timer
        print(
            "Reading HDF as filename 'HDF5_{}.h5' format \n in path '{}' with '{}' time succesfull completed!".format(
                filename, input_path, running_time))
        return hdf
    except NameError as e:
        print(
            "Sorry! read HDF5 as filename 'HDF5_{}.h5' format \n in path '{}' was wrong! Check input path and HDF5 existence".format(
                filename, input_path))
        return False

def service_call_import_daten(path, filename, **sheetnames):
    #**sheetnames = {'s1':'Wichtig', 's2': 'List of ServiceCalls', 's3':'Tabelle1', 's4':'Parts', 's5':'Breakdown', 's6':'Maintenance'}

    ls_sheetnames = list() # extract sheetnames
    for sheetname in sorted(sheetnames):
        ls_sheetnames.append(sheetnames[sheetname])

    ls_dfs = [] # extract a dataframe for each sheetname
    for item in ls_sheetnames:
        df = load_excelFile(path + '\\' + filename, item)
        df = df[0] # take only dataframe, df[1] is items -> ALL sheetnames
        ls_dfs.append(df)
    return ls_dfs
#ls_dfs = service_call_import_daten(path, filename, **sheetnames)

# main program
Vars_main = {}
def main():
    global Vars_main
    print("second timer", datetime.now())  # second timer

    # 27.02.2019 haupt df ist hier

    # ab hier kann man main function kompileren anfangen:
    #df = func_read_df_from_json(data_path + file_name_joint_df)
    df = read_HDF(file_name_joint_df, data_path)

    print("third timer",datetime.now() ) # third timer

    #   create data dictionary
    #data_dict=df.set_index('Service-Meldung').to_dict()


    global df_sorted

    ''''# df_sorted 15.03.2019
    df_sorted = pd.DataFrame()

    field_name = str('Störungsbeginn (Dat)_punkt')      #field_name determiend the field of Start of Failure, entweder 'Störungsbeginn (Dat)_punkt' oder 'Meldungsdatum'
    fieldName = field_name      # in groupby command occurs a problem with '_' in field_name # wrong!
    df_sorted = df.sort_values(['Equipment', fieldName], ascending=True)     # sorting values by the 'Störungsbeginn (Dat)_punkt' -> field_name

    df_sorted['sorted_Date'] = pd.to_datetime(df_sorted[fieldName])
    df_sorted = df_sorted.sort_values(['Equipment', 'sorted_Date'], ascending=True)
    df_sorted = df_sorted.drop(columns='sorted_Date')
    df_sorted = df_sorted.reset_index(drop=True)
    ##df_sorted['Geräte_große'] = df_sorted['Invt_Nr'].str[1] + df_sorted['Invt_Nr'].str[2]   # create device size field
    df_sorted['Geräte_große'] = df_sorted['Invt_Nr'].str[1] + df_sorted['Invt_Nr'].str[2]  # create device size field

    write_df_to_HDF5(df_sorted, 'df_sorted', output_path=data_path)
    '''# df_sorted 15.03.2019

    df_sorted = read_HDF('df_sorted', data_path)

    global MTFF

    print("fourth timer", datetime.now())  # fourth timer

    global df_land, df_ketten_zeich, df_Geraete_große, df_Baugruppe

    #   read mentioned above dfs from xlsx faster than each time to compiling
    df_land = load_excelFile_all_sheets(data_path + 'df_land.xlsx', reset_index=False)  # read from excel method_2 faster method
    df_ketten_zeich = load_excelFile_all_sheets(data_path + 'df_ketten_zeich.xlsx',
                                                reset_index=False)  # read from excel method_2 faster method
    df_Geraete_große = load_excelFile_all_sheets(data_path + 'df_Geraete_große.xlsx',
                                                 reset_index=False)  # read from excel method_2 faster method
    df_Baugruppe = load_excelFile_all_sheets(data_path + 'df_Baugruppe.xlsx',
                                             reset_index=False)  # read from excel method_2 faster method

    df_land[df_land.index == 'Land']
    # after write to and read from excel appeared nan und damy in mentioned above dfs -> remove nan und Land from index of dfs land, ketten_zeich, Geraete_große, Baugruppe
    df_land = df_land.iloc[2:, :]
    df_ketten_zeich = df_ketten_zeich.iloc[2:, :]
    df_Geraete_große = df_Geraete_große.iloc[2:, :]

    # df_Baugruppe Ausnahmweise hat keine nan & damy Values, is not important to remove first 2 rows
    # df_Baugruppe = df_Baugruppe.iloc[2:, :]

    '''
    in normale fälle muss hier ausgebländet sein
    df_sorted['Geräte_große'] = df_sorted['Invt_Nr'].str[1] + df_sorted['Invt_Nr'].str[2]  # create device size field
    '''


    print("fifth timer", datetime.now())  # fifth timer

    Vars_main = inspect.currentframe().f_locals
    return True

def close_objects():
    import gc
    import h5py
    for obj in gc.get_objects(): # Browse through ALL objects
        if isinstance(obj, h5py.File): # Just HDF5 files
            try:
                obj.close()
            except:
                pass # was already closed

if __name__ == '__main__':

    #%%time
    first_timer = datetime.now()
    print("first timer", first_timer)  # first timer
    main()
    sixth_timer = datetime.now()
    print("sixth timer", sixth_timer)  # sixth timer
    print("main func total time : %s" % (sixth_timer - first_timer))
    app = Rational()
    app.geometry("1280x720")
    # ani = animation.FuncAnimation(f, animate(df_Geraete_große, field_name= str('Geräte_große')), interval=5000)
    app.mainloop()
    print("last timer", datetime.now())  # last timer

    # close ALL opened objects
    close_objects()

