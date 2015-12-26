
import basic_container

class Python35Container(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "python:3.5"
        self.command = "python main.py"
        self.file_extension = ".py"
