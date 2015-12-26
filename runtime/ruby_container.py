
import basic_container

class RubyContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "ruby"
	self.command = "ruby main.rb"
	self.file_extension = ".rb"

