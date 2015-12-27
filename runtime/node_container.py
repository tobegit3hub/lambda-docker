
import basic_container

class NodeContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "node"
	self.command = "node main.js"
	self.file_extension = ".js"

