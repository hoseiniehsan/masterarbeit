import tkinter as tk
import numpy as np
import os
import sys

from tkinter import ttk
from matplotlib import style
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg, FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog

# import warnings filters try Exception warnings ignoring
np.warnings.filterwarnings("ignore")
np.warnings.resetwarnings()
np.seterr(divide='ignore')
np.seterr(all='ignore')

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
style.use("ggplot")


path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
sys.path.append('/')
#sys.path.extend('/')
#os.path.join('/')

from pack.Esselunga import PageThree
from pack.Esselunga import load_excelFile_all_sheets
from pack.Esselunga import messagebox

os.path.join('/Esselunga')


class ServiceCall(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Service Call Esselunga Italien", font=LARGE_FONT)
        label.pack(side='top')
        button2 = ttk.Button(self, text="Import source Excel Data", command=lambda: ServiceCall.action_import_xlsx())
        button2.pack()
        button3 = ttk.Button(self, text="Back to Home", command=lambda: PageThree.back_home(self, controller, self.canvas, self.toolbar))#controller.show_frame(StartPage))
        button3.pack()
        button4 = ttk.Button(self, text="View Bar Chart Land",
                             command=lambda:  self.call_viewer())#self.view_chart(df_land_temp, field_name=str('Land')))
        button4.pack()


    def view_chart(self, df, field_name):
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
        self.canvas, self.toolbar = ServiceCall.view_chart(self, df_land_temp, field_name=str('Land'))

    def action_import_xlsx(self, title=None, file_name=None, dir_name=None, file_Ext=".xlsx", file_types=None,
                           reset_index=True):
        file = filedialog.askopenfilename(filetypes=[('Excel files', '.xlsx')])
        if file:
            try:
                self.data = load_excelFile_all_sheets(file, reset_index=reset_index)
                print(self.data.head(5))
                messagebox.showinfo('Importing Data', 'importing excel Completed!')
            except NameError as e:
                messagebox.showerror('Error importing Excel Data', 'Unable to import file: %r' % file)

        return True
