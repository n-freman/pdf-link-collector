import os


class FilePathValidationError(Exception):
    pass


def is_pdf(file_path: str):
    if file_path.endswith('.pdf'):
        return
    raise FilePathValidationError('File should be a pdf file')


def does_exist(file_path: str):
    if os.path.exists(file_path):
        return
    raise FilePathValidationError('File does not exist')

