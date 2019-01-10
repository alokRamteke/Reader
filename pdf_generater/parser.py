import re

from .pdf_parser import PdfParser

def clean_data_pdf_file(file_path, pages=None):
    # cols = ['DEF01', 'DEF02', 'PLA01', 'PLA02', 'DEC01', 'PET01', 'RSP01', 'ATY01']
    # data = {
    #     'case_status_date':'',
    #     'case_list':[]
    # }
    file_path1 = '/home/rails/Projects/Alok/pdf_reader/pdf_reader'+file_path
    parser = PdfParser(file_path=file_path1)
    raw_text = parser.convert_pdf_to_text(pages=pages)
    all_rows = re.split(r'[\n\r]+', raw_text)
    for line in all_rows:

        # Capture one-or-more characters of non-whitespace after the initial match
        match = re.search(r'story (\S+)', line)

        # Did we find a match?
        if match:
            # Yes, process it
            weather = match.group(1)
            print('weather: {}'.format(weather))
    import pdb;pdb.set_trace()