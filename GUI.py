import tkinter as tk
from tkinter import ttk, filedialog
import os
from Config import write_to_config, load_from_config,  \
    generate_empty_config
from Base import Generator
from StructureBase import StructureGenerator
from load_zatman_template import insert_into_html


class MainWindow(object):
    """docstring for MainWindow."""

    def __init__(self, minsize=(360,100), icon = 'gui.png',
        title="SEDI Zatman Updater"):
        super(MainWindow, self).__init__()

        # Initialize root window
        root = tk.Tk()
        root.title(title)

        self.minsize = minsize
        root.minsize(minsize[0],minsize[1])
        # root.maxsize(860,300)
        self.root = root

        self.icon = icon
        photoicon = tk.PhotoImage(file = icon)
        root.iconphoto(False, photoicon)

    def run(self):
        self.root.mainloop()


class ExcelFrame(ttk.Frame):
    """docstring for ExcelFrame."""

    def __init__(self, *args, **kwargs):
        super(ExcelFrame, self).__init__(*args, **kwargs)
        # self.arg = arg
        self.output_html_file = "output.html"

        change_database_button = ttk.Button(self, text="Load Database File",
            command= self.__change_database, padding = 5)

        write_html_button = ttk.Button(self, text= "Write HTML File",
            command = self.__write_html, padding = 5)

        self.databaseLabel =  LabelFrame(self, "Database")

        self.__load_config(configfile="config.ini")
        self.__update_labels_and_config()

        # self.__update_excel_file(self.config["filename"])

        # gridding
        self.grid()
        self.databaseLabel.grid(row=0)
        change_database_button.grid(column=0, row =2, padx = 10, pady= 10)
        write_html_button.grid(column=1, row= 2, padx = 10, pady= 10)

    def __dialog_database(self):
        name = filedialog.askopenfilename(filetypes=(("Excel File", "*.xlsx"),))
        # if the filedialog was closed without picking a file, name will be
        # returned as an empty tuple
        if isinstance(name, tuple) == True:
            name = ""
        return name

    def __change_database(self):
        """ method to be called on button press for changing the officers file
        """
        name = self.__dialog_database()
        self.config["database"] = name
        self.__update_labels_and_config()

    def __update_labels_and_config(self):
        """ all updating of labels and the config after getting new values
        for the committee and officer file
        """
        database = self.config["database"]
        reduced_database = os.path.basename(database)
        # rename the labels
        self.databaseLabel.set_filename(reduced_database)
        write_to_config(configfile="config.ini", database =database)

    def __load_config(self, configfile = "config.ini"):
        """ function that loads the configfile and binds it to the instance.
        if the configfile does not exist, create a new empty one
        """
        try:
            self.config = load_from_config(configfile)
        except:
            print("--- No config.ini file found. Generating new one... ---")
            generate_empty_config(configfile)
            self.config = load_from_config(configfile)

    def set_html_output(self, html_output):
        self.output_html_file = html_output

    def __write_html(self):
        table_database = self.config["database"]

        table_generator = StructureGenerator(table_database)
        table = table_generator.generate_html_table()
        html = insert_into_html(table)
        with open(self.output_html_file, "w") as file:
            file.write(html)

class LabelFrame(ttk.Frame):
    """docstring for LabelFrame.
    db_description is a one-word description of the database"""
    def __init__(self, parent, db_description, **kwargs):
        super(LabelFrame, self).__init__(parent, **kwargs)
        # append white space for db_description if it does not have one already
        if db_description[-1] != " ":
            db_description += " "
        # what happens if db_description is an empty string?

        self.current_filename_display = tk.StringVar()

        database_label = ttk.Label(self,
            text=f"Current {db_description}Database:")
        current_database_label = ttk.Label(self, textvariable =
            self.current_filename_display)

        database_label.grid(column = 0, row = 0, padx = 10, pady= 10)
        current_database_label.grid(column=1, row=0, padx = 10, pady= 10)

    def set_filename(self, name):
        reduced_name = os.path.basename(name)
        self.current_filename_display.set(reduced_name)






gui = MainWindow()
frame = ExcelFrame(gui.root)
frame.set_html_output("zatman.html")
gui.run()

base = tk.Tk()
root=ttk.Frame(base)
