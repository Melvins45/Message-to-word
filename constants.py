import os
import Ui_excel, Ui_pdf, Ui_word

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
GLOBAL_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = {
    "word" : os.path.join(GLOBAL_DIR, "word.ui"),
    "excel" : os.path.join(GLOBAL_DIR, "excel.ui"),
    "pdf" : os.path.join(GLOBAL_DIR, "pdf.ui"),
}

PAGES_UI = {
    "word" : Ui_word.Ui_wordForm(),
    "excel" : Ui_excel.Ui_excelForm(),
    "pdf" : Ui_pdf.Ui_pdfForm()
}

PAGES_INDEX = {
    "word" : 0,
    "excel" : 1,
    "pdf" : 2
}

PAGES_TITLES = {
    "word" : 'Compilez vers Word - Message To Doc',
    "excel" : 'Compilez vers Excel - Message To Doc',
    "pdf" : 'Compilez vers PDF - Message To Doc',
}

FILE_DIALOG_CAPTION = "Enregistrez sous - Message To Doc"

DEFAULT_TITLES_DOC = {
    "word" : "Document",
    "excel" : "Classeur",
    "pdf" : "DOcument"
}