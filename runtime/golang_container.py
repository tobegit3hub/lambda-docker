
import basic_container

class GolangContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "golang"
	self.command = "go run /tmp/main.go"
	self.file_extension = ".go"

