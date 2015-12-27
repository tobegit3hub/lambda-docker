
import basic_container

class PhpContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "php"
	self.command = "php main.php"
	self.file_extension = ".php"

