
import basic_container

class ObjectiveCContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	# Refer to https://hub.docker.com/r/nacyot/objectivec-gcc/
	self.image = "nacyot/objectivec-gcc:apt"
	self.command = 'sh -c "gcc main.m -o main && ./main"'
	self.file_extension = ".m"

