# Python TCP Server
This is a first attempt of a TCP Server written in python to learn python. 
So no guarantee on correctness or other things.

## Start
Just call the `main.py` with the following command: 

> python main.py

The within the code predefined Address and Port is:
> 127.0.0.1 : 42424

Now you can connect to the Server with for example netcat:

> nc 127.0.0.1 42424

The Server will send u your message as replay back. You can exit & shutdown the server when you send `exit`

## Tested
It works under Python `version 2.7.10`


