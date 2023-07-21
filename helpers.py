import sys
import os
import re
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import (QFile, QIODevice)
from PySide2.QtUiTools import QUiLoader
import constants as gc
import textwrap
from fpdf import FPDF
    
def load_ui(file_name:str) -> QWidget:
    """Load an ui file in a QWidget and return it

    Args:
        file_name (str): The name of the specified ui file

    Returns:
        QWidget: The resulted QWidget
    """    
    ui_page_file = QFile(gc.PAGES[file_name])
    if not ui_page_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {file_name} : {ui_page_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_page_file)
    ui_page_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    return window  

def load_py(file_name:str) -> QWidget:
    """Load python compiled ui file in QWidget

    Args:
        file_name (str): The name of the compiled python file from ui file

    Returns:
        QWidget: The resulted QWidget
    """    
    class _Window(QWidget):
        def __init__(self, parent=None):
            super(_Window, self).__init__(parent)

            self.m_ui = gc.PAGES_UI[file_name]
            self.m_ui.setupUi(self)
    return _Window()

def treat_text(_text: str) :
    """Treat a text and return a list of paragraphs

    Args:
        _text (str): a multiline string

    Returns:
        list[str]: list of paragraphs
    """    
    text = _text.split('\n')
    return [ i for i in text if i!='' and bool(re.search(r'\d', i)) ]

def  take_title(_paragraph: str) :
    """Take the title of paragraph or string

    Args:
        _string (str): A paragraph or string

    Returns:
        str, str: The title of the paragraph or string, The content of the paragraph
    """    
    left_delimiter = re.findall(r'^\d{1,3}\. ', _paragraph)
    right_delimiter = re.findall(r':(.*)$', _paragraph)
    pattern_string = ( re.escape(left_delimiter[0]) if len(right_delimiter) != 0 else '' ) + "(.*)" + ( re.escape(right_delimiter[0]) if len(right_delimiter) != 0 else '' )
    pattern = re.compile(pattern_string)
    return pattern.findall(_paragraph)[0], right_delimiter

def treat_text_excel(_text: str, delimiter: str = ',') -> list[list[str]] :
    """Give an array of each line of a text, where each line are them-selves splitted by a delimiter character

    Args:
        _text (str): The specified text to double-splt
        delimiter (str, optional): The delimiter character to split each line of the text. Defaults to ','.

    Returns:
        list[list[str]]: The resulted array of lines which are them-selves array of string
    """    
    delimiter = ',' if delimiter == '' else delimiter
    return [ i.split(delimiter) for i in _text.split('\n') ]

def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')