#A tool by What_A_Legend27

version = "0.1.0"

import time

from dependencies import check_for_dependencies
from logger import create_error_log

#Checks if module dependencies are installed:
# - Magic
# - Validators
# - FFprobe
#If these are not installed, this function installs them
check_for_dependencies()

import magic, validators, ffprobe
