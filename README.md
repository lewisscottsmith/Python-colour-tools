# Python Tools
Various tools for use in python


#### Setup & importing the module
To beable to import the module, the pythonTools folder needs to be added to the site packages.

First find the path of site packages by opening a python interpurter and running the following:
```bash
>>>from sys import path
>>>print(path)
```
This should print out a list of paths, look for the one ending in `/site-packages`.
Then copy the `pythonTools` folder into `sitepackages` like so (as super user):
```bash
cp -r pythonTools/ /usr/lib/python3.6/site-packages
```

(Assuming you are in the `python-tools` directory)

You can then import any of the modules (`from pythonTools import colourTools as ct`)


