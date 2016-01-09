
import basic_container

class PerlContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "perl"
	self.command = "perl main.pl"
	self.file_extension = ".pl"

