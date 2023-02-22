import pandas as pd
# from load_zatman_template import load_doornbos_template



class Generator(object):
    """Generator is the base class used to generate a new HTML table.
    It uses an excel spreadsheet with 2 columns. Future work on this class
    might improve this feature to variable column count"""

    def __init__(self, spreadsheet = ""):
        super(Generator, self).__init__()
        self.spreadsheet = spreadsheet
        self.database = ""
        # read the spreadsheet if it exists
        if self.spreadsheet[-5:] == ".xlsx":
            self.database = pd.read_excel(self.spreadsheet)

    def __generate_html_row(self, column1, column2):
            format_html = \
            f"""<tr>
                <td>{column1}</td>
                <td>{column2}</td>
            </tr>
            """
            return format_html


    def generate_html_table(self, frame=""):
        """
        function to generate the whole, custom-formatted HTML table
        """
        # alternative isinstance pd.dataframe check?
        if isinstance(frame, pd.DataFrame) == False:
            frame = self.database

        html_table = ""

        len_frame = frame.shape[0]

        for i in range(len_frame):
            column1 =  frame.iloc[i][0]
            column2 = frame.iloc[i][1]
            html_table += self.__generate_html_row(column1, column2)

        return html_table

    def write_to_file(self, filename):
        """ this function writes the complete HTML code into the specified
            filename
        """
        if isinstance(self.database, pd.DataFrame) == False:
                    print("Error: No valid database selected")
        else:
            html_table = self.generate_html_table(frame = self.database)
            page = __insert(insert=html_table)
            with open(filename, "w") as file:
                file.write(page)

    def __insert(self, insert):
        """ helper function to be overwritten in subclasses"""
        # insert_into_html(insert=html_table)
        page = None
        return page

    def set_database(self, filename):
        database = ""
        if filename[-5:] == ".xlsx":
            database = pd.read_excel(filename)

        if isinstance(database, pd.DataFrame) == True:
            self.database = database
        else:
            print("No valid database file presented. Is it a .xlsx file?")
