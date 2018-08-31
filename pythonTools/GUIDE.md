#User Guide
## Contents
- [Colour tools]()

###Colour Tools
Colour tools user guide.
All example will assume the module has been imported as follow:

`from pythonTools import colourTools as ct`

##### Colour variables
The module includes 7 colour / style varibale that can be used in print statements to format the text. These are:
- purple
- blue
- green
- yellow
- red
- bold
- underline

(and can be refernced as such)

As well as a `normal` varibale to return to the default terminal formatting (this can also be done by calling `ct.reset()`. 

Example use:
```bash
print("hello " + ct.blue + "world!" + ct.normal)
```
> Note: It's important to end with `ct.normal` as this clears the formatting applied and ensures the rest of the terminal output will be as default

##### Print functions
There are multiple print_ functions that print specific messages.The general format is `print_info("some message")`. The info part of the function name can be changed based on what kind of formatting is required and what type of message it is. There are several pre set types of messages, these include:

Type | Name | Result
--- | --- | --- 
Info|print_info|[INFO] with blue text
error|print_error|[ERROR] with red text
warning|print_warning|[WARNING] with yellow text
ok|print_ok|[OK] with green text
done|print_done|[DONE] with green text
complete|print_complete|[COMPLETE] with green text
update|print_update|[UPDATE] with purple text
status|print_status|[STATUS] with purple text

All of the above function take the following form:

`print_info(msg,end="\n",msg_style=normal,join="",indent="",colour=blue))`

Parameter|Required|Default|Meaning
---|---|---|---
msg|Yes|n/a|The message that will be printed after the tag[]
end|No|"\n"|Similar to the python print function, it specifies how to end the print statement (allows for the next print to be on the same line by setting it to "")
msg_style|No|normal|Formatting option for the text of the message. (Allows for the text to be a differnet colour of style)
join|No|""|Set a join sting that will go between the tag and message (i.e. [TAG] join msg...)
indent|No|""|Set an indent for the start of the message (i.e. \t)
colour|No|depends on tag|Set the colour of the tag text, allows for the defualt colour to be overriden (e.g. for info: colour=blue)

The `print_custom` function allows for custom tags to be constucted using the following additional parameters (to the ones above)

|Parameter|Required|Default|Meaning
---|---|---|---
tag|Yes|n/a|The text to display in the tag brackets
colour|Yes|n/a|The colour of the tag text