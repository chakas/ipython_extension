from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
from IPython.core.magic_arguments import (argument, magic_arguments,
    parse_argstring)

@register_line_magic
def sflogin(line):
    data = line.split(" ")
    d = {}
    for i in data:
        d[i.split("=")[0]] = i.split("=")[1]
    
    if ( "-user" in  d or "-u" in  d):
            print "Got username",d["-u"] or d["-u"]
    else:
            return "Please input user"
            
    if ( "-passowrd" in  d or "-p" in  d):
            print "Got password",d["-p"] or d["-password"]
    else:
            return "Please input password"
            
    if ( "-token" in  d or "-t" in  d):
            print "Got username",d["-t"] or d["-token"]
    else:
            return "Please input security token"
            
    if ( "-url" in  d or "-sfUrl" in  d):
            print "Got username",d["-url"] or d["-sfUrl"]
    else:
            return "Please input Salesforce url"
