import os


DEFAULT_CATEGORY = os.getenv('TRACKMYWORK_DEFAULT_CATEGORY')
DEFAULT_PROJECT = os.getenv('TRACKMYWORK_DEFAULT_PROJECT')

# DEFAULT_STORAGE = os.getenv('TRACKMYWORK_DEFAULT_STORAGE', 'textfile')
STORAGE_PATH = os.getenv('TRACKMYWORK_STORAGE_PATH', os.path.expanduser('~/.trackmywork.txt'))
STORAGE_PATH_BACKUP = os.getenv('TRACKMYWORK_STORAGE_PATH_BACKUP', os.path.expanduser('~/.trackmywork.txt.bkp'))
