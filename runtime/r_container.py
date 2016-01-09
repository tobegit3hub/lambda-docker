
import basic_container

class RContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "r-base"
	self.command = "Rscript main.R"
	self.file_extension = ".R"

