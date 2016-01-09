
import basic_container

class HaskellContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "haskell"
	self.command = 'sh -c "ghc -o main main.hs && ./main"'
	self.file_extension = ".hs"

