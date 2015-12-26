
import basic_container

class UbuntuContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "ubuntu"
	self.command = "bash main"
	self.file_extension = ""

