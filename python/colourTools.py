# Colour values
purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
bold = '\033[1m'
underline= '\033[4m'

normal = '\033[0m'

def print_info(msg,end="\n",msg_style=normal,join="",indent="",colour=blue):
    print(indent + normal + bold + "[{}INFO{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_error(msg,end="\n",msg_style=normal,join="",indent="",colour=red):
    print(indent + normal + bold + "[{}ERROR{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_custom(msg,tag,end="\n",msg_style=normal,join="",indent="",colour=blue):
    print(indent + normal + bold + "[{}{}]{} {}".format(colour+tag.upper(),normal+bold,join, normal + msg_style+msg+normal),end=end)

def reset():
    print(normal)