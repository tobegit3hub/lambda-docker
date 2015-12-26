
import basic_container

class CentosContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "centos"
	self.command = "bash /tmp/main"
	self.file_extension = ""

