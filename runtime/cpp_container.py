
import basic_container

class CppContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "gcc"
	self.command = 'sh -c "g++ main.cpp -o main && ./main"'
	self.file_extension = ".cpp"

