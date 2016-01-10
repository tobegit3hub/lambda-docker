
import basic_container

class RustContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "schickling/rust"
	self.command = 'sh -c "rustc main.rs -o main && ./main"'
	self.file_extension = ".rs"

