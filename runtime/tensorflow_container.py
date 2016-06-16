
import basic_container

class TensorFlowContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "tensorflow/tensorflow"
	self.command = "python main.py"
	self.file_extension = ".py"

