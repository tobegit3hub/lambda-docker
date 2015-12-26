
import basic_container

class Python27Container(basic_container.BasicContainer):

    def __init__(self):
	super(Python27Container, self).__init__()
        
	self.image = "python:2.7"
	self.command = "python /tmp/main.py"
	self.file_extension = ".py"

