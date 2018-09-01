from pythonTools import colourTools as ct

ct.print_info("This is an example of using ct to print an info message ")
# ct.print_note("This is an example of using ct to print a note message")
ct.print_error("This is an example of using ct to print an error message")
ct.print_warning("This is an example of using ct to print a warning message")
ct.print_ok("This is an example of using ct to print a ok message")
ct.print_done("This is an example of using ct to print a done message")
ct.print_complete("This is an example of using ct to print a complete message")
ct.print_update("This is an example of using ct to print an update message")
ct.print_status("This is an example of using ct to print a status message")

ct.print_custom("This is an example of using ct to print a custom message with a tag saying test",tag='test', colour=ct.purple,msg_style=ct.underline)

ct.print_info("This is an info message that has been indented using the indent parameter",indent="\t")



