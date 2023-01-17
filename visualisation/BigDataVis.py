import tkinter as tk
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import cufflinks as cf
import chart_studio.plotly as py
import seaborn as sns
import plotly.express as px

#GLOBAL VARIABLES
HEIGHT = 810
WIDTH = 1000
#CREATING THE APP WINDOW
window = tk.Tk()
window.title("Big Data Project")
window.minsize(height = str(HEIGHT), width = str(WIDTH))
window.maxsize(height = str(HEIGHT), width = str(WIDTH))

def main_menu():
    
    def CLC_analisys(okno_stare):

        def button_6G_create():
            clear_frame()
            fig = px.bar(df_CLC, x = 'Amount', y = '6G', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Capital Letter Counter - 6G')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_6G_100G_create():
            clear_frame()
            fig = px.bar(df_CLC, x = 'Amount', y = ['6G', '100G'], labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, text = 'value', title = 'Capital Letter Counter - 6G and 100G', barmode = 'group')
            fig.update_traces(texttemplate = '%{text:.2s}', textposition = 'outside')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_100G_create():
            clear_frame()
            fig = px.bar(df_CLC, x = 'Amount', y = '100G', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Capital Letter Counter - 100G')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_Norm_create():
            clear_frame()
            fig = px.bar(df_CLC, x = 'Amount', y = ['6G_NORM', '100G_NORM'], labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Capital Letter Counter - 6G and 100G Normalised', text = 'value', barmode = 'group')
            fig.update_traces(texttemplate = '%{text:0.3f}', textposition = 'outside')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def display_image():
            frame.picture = ImageTk.PhotoImage(Image.open('grafiki/fig1.png'))
            frame.label = tk.Label(frame, image=frame.picture)
            frame.label.pack()

        def clear_frame():
            for widget in frame.winfo_children():
                widget.destroy()
        def back():
            CLC_window.pack_forget()
            okno_stare.pack()

        okno_stare.pack_forget()
        CLC_window = tk.Frame(window, height = str(HEIGHT), width = str(WIDTH))

        
        #TWORZENIE NAPISU I PRZYCISKÓW
        label_CLC_analisys = tk.Label(CLC_window, text = "Capital Letter Counter", height = str(0), width = str(0), font = ("timesnewroman", 20, "bold"))
        label_add_data = tk.Label(CLC_window, text = "Dodaj dane", height = str(0), width = str(0), font = ("timesnewroman", 15, "bold"))
        button_6G = tk.Button(CLC_window, text="6 G", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_create())
        button_100G = tk.Button(CLC_window, text="100 G", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_100G_create())
        button_6G_100G = tk.Button(CLC_window, text="oba", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_100G_create())
        button_Norm = tk.Button(CLC_window, text="NORM", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_Norm_create())
        przycisk_powrót = tk.Button(CLC_window, text="Powrót", width='15', height='3', font = ("timesnewroman", 15, 'bold'), command=lambda: back())

        label_CLC_analisys.pack()
        label_CLC_analisys.place(x = WIDTH/2 - 200, y = HEIGHT/2 - 350, anchor="center")
        label_add_data.pack()
        label_add_data.place(x = WIDTH/2 + 350, y = HEIGHT/2 - 300, anchor="center")
        button_6G.pack()
        button_6G.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 250, anchor="center")
        button_100G.pack()
        button_100G.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 250, anchor="center")
        button_6G_100G.pack()
        button_6G_100G.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 200, anchor="center")
        button_Norm.pack()
        button_Norm.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 200, anchor="center")

        
        przycisk_powrót.pack()
        przycisk_powrót.place(x= WIDTH/2 + 360, y=HEIGHT/2 + 300, anchor="center")

        frame = tk.Frame(CLC_window, highlightthickness = 2,  width=600, height=600, highlightbackground = "black")
        frame.pack()
        frame.place( x = WIDTH/2 - 600, y = HEIGHT/2 - 400, anchor='center', relx=0.5, rely=0.5)
        CLC_window.pack()

    def DEC_analisys(okno_stare):

        def button_6G_create():
            clear_frame()
            fig = px.bar(df_DEC, x = 'Amount', y = '6G', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Digits End Counter - 6G')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_6G_100G_create():
            clear_frame()
            fig = px.bar(df_DEC, x = 'Amount', y = ['6G', '100G'], labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, text = 'value', barmode = 'group', title = 'Digits End Counter - 6G and 100G')
            fig.update_traces(texttemplate = '%{text:.2s}', textposition = 'outside')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_100G_create():
            clear_frame()
            fig = px.bar(df_DEC, x = 'Amount', y = '100G', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Digits End Counter - 100G')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_Norm_create():
            clear_frame()
            fig = px.bar(df_DEC, x = 'Amount', y = ['6G_NORM', '100G_NORM'], labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, text = 'value', barmode = 'group', title = 'Digits End Counter - 6G and 100G Normalised')
            fig.update_traces(texttemplate = '%{text:0.3f}', textposition = 'outside')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def display_image():
            frame.picture = ImageTk.PhotoImage(Image.open('grafiki/fig1.png'))
            frame.label = tk.Label(frame, image=frame.picture)
            frame.label.pack()

        def clear_frame():
            for widget in frame.winfo_children():
                widget.destroy()
        def back():
            CLC_window.pack_forget()
            okno_stare.pack()

        okno_stare.pack_forget()
        CLC_window = tk.Frame(window, height = str(HEIGHT), width = str(WIDTH))

        
        #TWORZENIE NAPISU I PRZYCISKÓW
        label_CLC_analisys = tk.Label(CLC_window, text = "Digits End Counter", height = str(0), width = str(0), font = ("timesnewroman", 20, "bold"))
        label_add_data = tk.Label(CLC_window, text = "Dodaj dane", height = str(0), width = str(0), font = ("timesnewroman", 15, "bold"))
        button_6G = tk.Button(CLC_window, text="6 G", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_create())
        button_100G = tk.Button(CLC_window, text="100 G", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_100G_create())
        button_6G_100G = tk.Button(CLC_window, text="oba", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_100G_create())
        button_Norm = tk.Button(CLC_window, text="NORM", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_Norm_create())
        przycisk_powrót = tk.Button(CLC_window, text="Powrót", width='15', height='3', font = ("timesnewroman", 15, 'bold'), command=lambda: back())

        label_CLC_analisys.pack()
        label_CLC_analisys.place(x = WIDTH/2 - 300, y = HEIGHT/2 - 350, anchor="center")
        label_add_data.pack()
        label_add_data.place(x = WIDTH/2 + 350, y = HEIGHT/2 - 300, anchor="center")
        button_6G.pack()
        button_6G.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 250, anchor="center")
        button_100G.pack()
        button_100G.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 250, anchor="center")
        button_6G_100G.pack()
        button_6G_100G.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 200, anchor="center")
        button_Norm.pack()
        button_Norm.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 200, anchor="center")

        
        przycisk_powrót.pack()
        przycisk_powrót.place(x= WIDTH/2 + 360, y=HEIGHT/2 + 300, anchor="center")

        frame = tk.Frame(CLC_window, highlightthickness = 2,  width=600, height=600, highlightbackground = "black")
        frame.pack()
        frame.place( x = WIDTH/2 - 600, y = HEIGHT/2 - 400, anchor='center', relx=0.5, rely=0.5)
        CLC_window.pack()

    def DSC_analisys(okno_stare):

        def button_6G_create():
            clear_frame()
            fig = px.bar(df_DSC, x = 'Amount', y = '6G', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Digits Start Counter - 6G')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_6G_100G_create():
            clear_frame()
            fig = px.bar(df_DSC, x = 'Amount', y = ['6G', '100G'], labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, text = 'value', barmode = 'group', title = 'Digits Start Counter - 6G and 100G')
            fig.update_traces(texttemplate = '%{text:.2s}', textposition = 'outside')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_100G_create():
            clear_frame()
            fig = px.bar(df_DSC, x = 'Amount', y = '100G', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Digits Start Counter - 100G')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_Norm_create():
            clear_frame()
            fig = px.bar(df_DSC, x = 'Amount', y = ['6G_NORM', '100G_NORM'], labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, text = 'value', barmode = 'group', title = 'Digits Start Counter - 6G and 100G Normalised')
            fig.update_traces(texttemplate = '%{text:0.3f}', textposition = 'outside')
            fig.write_image("grafiki/fig1.png")
            display_image()

        def display_image():
            frame.picture = ImageTk.PhotoImage(Image.open('grafiki/fig1.png'))
            frame.label = tk.Label(frame, image=frame.picture)
            frame.label.pack()

        def clear_frame():
            for widget in frame.winfo_children():
                widget.destroy()
        def back():
            CLC_window.pack_forget()
            okno_stare.pack()

        okno_stare.pack_forget()
        CLC_window = tk.Frame(window, height = str(HEIGHT), width = str(WIDTH))

        
        #TWORZENIE NAPISU I PRZYCISKÓW
        label_CLC_analisys = tk.Label(CLC_window, text = "Digits Start Counter", height = str(0), width = str(0), font = ("timesnewroman", 20, "bold"))
        label_add_data = tk.Label(CLC_window, text = "Dodaj dane", height = str(0), width = str(0), font = ("timesnewroman", 15, "bold"))
        button_6G = tk.Button(CLC_window, text="6 G", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_create())
        button_100G = tk.Button(CLC_window, text="100 G", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_100G_create())
        button_6G_100G = tk.Button(CLC_window, text="oba", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_100G_create())
        button_Norm = tk.Button(CLC_window, text="NORM", width='5', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_Norm_create())
        przycisk_powrót = tk.Button(CLC_window, text="Powrót", width='15', height='3', font = ("timesnewroman", 15, 'bold'), command=lambda: back())

        label_CLC_analisys.pack()
        label_CLC_analisys.place(x = WIDTH/2 - 300, y = HEIGHT/2 - 350, anchor="center")
        label_add_data.pack()
        label_add_data.place(x = WIDTH/2 + 350, y = HEIGHT/2 - 300, anchor="center")
        button_6G.pack()
        button_6G.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 250, anchor="center")
        button_100G.pack()
        button_100G.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 250, anchor="center")
        button_6G_100G.pack()
        button_6G_100G.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 200, anchor="center")
        button_Norm.pack()
        button_Norm.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 200, anchor="center")

        
        przycisk_powrót.pack()
        przycisk_powrót.place(x= WIDTH/2 + 360, y=HEIGHT/2 + 300, anchor="center")

        frame = tk.Frame(CLC_window, highlightthickness = 2,  width=600, height=600, highlightbackground = "black")
        frame.pack()
        frame.place( x = WIDTH/2 - 600, y = HEIGHT/2 - 400, anchor='center', relx=0.5, rely=0.5)
        CLC_window.pack()

    def DLC_analisys(okno_stare):

        def button_6G_2_create():
            clear_frame()
            fig = px.bar(df_DLC, x = 'Record_2', y = '6G_2', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Duplicated Digits Counter - 6G')
            fig.update_xaxes(tickangle = 45, title_text = "Values", title_font = {'size':10})
            fig.update_layout(xaxis = dict( tickfont = dict(size=5)))
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_6G_3_create():
            clear_frame()
            fig = px.bar(df_DLC, x = 'Record_3', y = '6G_3', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Trippled Digits Counter - 6G')
            fig.update_xaxes(tickangle = 45, title_text = "Values", title_font = {'size':10})
            fig.update_layout(xaxis = dict( tickfont = dict(size=5)))
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_100G_2_create():
            clear_frame()
            fig = px.bar(df_DLC, x = 'Record_2', y = '100G_2', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Duplicated Digits Counter - 100G')
            fig.update_xaxes(tickangle = 45, title_text = "Values", title_font = {'size':10})
            fig.update_layout(xaxis = dict( tickfont = dict(size=5)))
            fig.write_image("grafiki/fig1.png")
            display_image()

        def button_100G_3_create():
            clear_frame()
            fig = px.bar(df_DLC, x = 'Record_3', y = '100G_3', labels = {'x': 'Ilośc wielkich liter w haśle', 'y':'Liczba haseł'}, title = 'Trippled Digits Counter - 100G')
            fig.update_xaxes(tickangle = 45, title_text = "Values", title_font = {'size':10})
            fig.update_layout(xaxis = dict( tickfont = dict(size=5)))
            fig.write_image("grafiki/fig1.png")
            display_image()

        def display_image():
            frame.picture = ImageTk.PhotoImage(Image.open('grafiki/fig1.png'))
            frame.label = tk.Label(frame, image=frame.picture)
            frame.label.pack()

        def clear_frame():
            for widget in frame.winfo_children():
                widget.destroy()
        def back():
            CLC_window.pack_forget()
            okno_stare.pack()

        okno_stare.pack_forget()
        CLC_window = tk.Frame(window, height = str(HEIGHT), width = str(WIDTH))

        
        #TWORZENIE NAPISU I PRZYCISKÓW
        label_CLC_analisys = tk.Label(CLC_window, text = "Duplicated/Trippled Digits Counter", height = str(0), width = str(0), font = ("timesnewroman", 20, "bold"))
        label_add_data = tk.Label(CLC_window, text = "Dodaj dane", height = str(0), width = str(0), font = ("timesnewroman", 15, "bold"))
        button_6G_2 = tk.Button(CLC_window, text="6G_2", width='6', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_2_create())
        button_6G_3 = tk.Button(CLC_window, text="6G_3", width='6', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_100G_2_create())
        button_100G_2 = tk.Button(CLC_window, text="100G_2", width='6', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_6G_3_create())
        button_100G_3 = tk.Button(CLC_window, text="100G_3", width='6', height='1', font = ("timesnewroman", 15, 'bold'), command=lambda: button_100G_3_create())
        przycisk_powrót = tk.Button(CLC_window, text="Powrót", width='15', height='3', font = ("timesnewroman", 15, 'bold'), command=lambda: back())

        label_CLC_analisys.pack()
        label_CLC_analisys.place(x = WIDTH/2 - 300, y = HEIGHT/2 - 350, anchor="center")
        label_add_data.pack()
        label_add_data.place(x = WIDTH/2 + 350, y = HEIGHT/2 - 300, anchor="center")
        button_6G_2.pack()
        button_6G_2.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 250, anchor="center")
        button_6G_3.pack()
        button_6G_3.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 250, anchor="center")
        button_100G_2.pack()
        button_100G_2.place(x = WIDTH/2 + 300, y = HEIGHT/2 - 200, anchor="center")
        button_100G_3.pack()
        button_100G_3.place(x = WIDTH/2 + 390, y = HEIGHT/2 - 200, anchor="center")
        przycisk_powrót.pack()
        przycisk_powrót.place(x= WIDTH/2 + 360, y=HEIGHT/2 + 300, anchor="center")

        frame = tk.Frame(CLC_window, highlightthickness = 2,  width=600, height=600, highlightbackground = "black")
        frame.pack()
        frame.place( x = WIDTH/2 - 600, y = HEIGHT/2 - 400, anchor='center', relx=0.5, rely=0.5)
        CLC_window.pack()

    main_menu_window = tk.Frame(window, height = str(HEIGHT), width = str(WIDTH))

    #CREATING BUTTONS AND TEXTS
    main_menu_text = tk.Label(main_menu_window, text = "MAIN MENU", height = str(0), width = str(0), font = ("timesnewroman", 20, "bold"))
    button_CLC = tk.Button(main_menu_window, text = "Capital Letter Counter", width = '40', height = '3', font = ("timesnewroman", 15, 'bold'), command = lambda: CLC_analisys(main_menu_window))
    button_DEC = tk.Button(main_menu_window, text = "Digits End Counter", width = '40', height = '3', font = ("timesnewroman", 15, 'bold'), command = lambda: DEC_analisys(main_menu_window))
    button_DSC = tk.Button(main_menu_window, text = "Digits Start Counter", width = '40', height = '3', font = ("timesnewroman", 15, 'bold'), command = lambda: DSC_analisys(main_menu_window))
    button_DLC = tk.Button(main_menu_window, text = "Duplicated/Trippled Charakters Counter", width = '40', height = '3', font = ("timesnewroman", 15, 'bold'), command = lambda: DLC_analisys(main_menu_window))
    button_finish = tk.Button(main_menu_window, text = "Finish", width = '40', height = '3', font = ("timesnewroman", 15, 'bold'), command = lambda: window.destroy())

    main_menu_text.pack()
    main_menu_text.place(x = WIDTH/2, y = HEIGHT/2 - 300, anchor = "center")
    button_CLC.pack()
    button_CLC.place(x = WIDTH/2, y = HEIGHT/2 - 200, anchor = "center")
    button_DEC.pack()
    button_DEC.place(x = WIDTH/2, y = HEIGHT/2 - 100, anchor = "center")
    button_DSC.pack()
    button_DSC.place(x = WIDTH/2, y = HEIGHT/2, anchor = "center")
    button_DLC.pack()
    button_DLC.place(x = WIDTH/2, y = HEIGHT/2 + 100, anchor = "center")
    button_finish.pack()
    button_finish.place(x = WIDTH/2, y = HEIGHT/2 + 200, anchor = "center")
    
    main_menu_window.pack()

df_CLC = pd.read_pickle('dfs/df_CLC.pkl')
df_DEC = pd.read_pickle('dfs/df_DEC.pkl')
df_DSC = pd.read_pickle('dfs/df_DEC.pkl')
df_DLC = pd.read_pickle('dfs/df_DLC.pkl')

main_menu()
window.mainloop()