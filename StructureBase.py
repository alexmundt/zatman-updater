from Base import Generator
import pandas as pd

class StructureGenerator(Generator):
    """docstring for StructureGenerator.

    This is the class that implements the actual generation of the new table.
    So all custom html creation of the rows from the read database and the
    general table is done here. """

    def __init__(self, *args, **kwargs):
        super(StructureGenerator, self).__init__(*args, **kwargs)

    def __sanitize_pandas_readout(self, string):
        """ this helper method takes care of non-string readouts from the
        database"""
        output = string
        if isinstance(string, str) == False:
            output = ""
        if isinstance(string, int) == True:
            output = str(string)
        return string

    def __generate_html_row(self, year, lecturer, title):
        """ this method overwrites the method of the Base class to generate
        the HTML row information from the given inputs.
        """

        year = self.__sanitize_pandas_readout(year)
        lecturer = self.__sanitize_pandas_readout(lecturer)
        title = self.__sanitize_pandas_readout(title)

        """
    <tr>
        <td>2022</td>
        <td>L. Cobden</td>
        <td>Locating the iron spin transition in the lower mantle with
global adjoint tomography</td>
    </tr>
        """

        row_html = f'<tr><td>{year}</td> <td>{lecturer}</td> <td>{title}</td></tr>'

        return row_html


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
            year =  frame.iloc[i][0]
            lecturer = frame.iloc[i][1]
            title = frame.iloc[i][2]
            html_table += self.__generate_html_row(year, lecturer, title)

        return html_table
