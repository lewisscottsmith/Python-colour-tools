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

def print_note(msg,end="\n",msg_style=normal,join="",indent="",colour=blue):
    print(indent + normal + bold + "[{}NOTE{}]{} {}".format(colour, normal + bold, join,normal + msg_style + msg + normal), end=end)

def print_error(msg,end="\n",msg_style=normal,join="",indent="",colour=red):
    print(indent + normal + bold + "[{}ERROR{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_warning(msg,end="\n",msg_style=normal,join="",indent="",colour=yellow):
    print(indent + normal + bold + "[{}WARNING{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_ok(msg,end="\n",msg_style=normal,join="",indent="",colour=green):
    print(indent + normal + bold + "[{}OK{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_done(msg,end="\n",msg_style=normal,join="",indent="",colour=green):
    print(indent + normal + bold + "[{}DONE{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_complete(msg,end="\n",msg_style=normal,join="",indent="",colour=green):
    print(indent + normal + bold + "[{}COMPLETE{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_update(msg,end="\n",msg_style=normal,join="",indent="",colour=purple):
    print(indent + normal + bold + "[{}UPDATE{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_status(msg,end="\n",msg_style=normal,join="",indent="",colour=purple):
    print(indent + normal + bold + "[{}STATUS{}]{} {}".format(colour,normal+bold,join, normal + msg_style+msg+normal),end=end)

def print_custom(msg,tag,colour,end="\n",msg_style=normal,join="",indent=""):
    print(indent + normal + bold + "[{}{}]{} {}".format(colour+tag.upper(),normal+bold,join, normal + msg_style+msg+normal),end=end)

def reset():
    print(normal)

def print_msg(msg,colour=normal,end="\n"):
    print(colour+msg+normal,end=end)

def get_msg(msg,colour):
    return colour + msg + normal