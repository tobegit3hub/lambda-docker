
import basic_container

class ErlangContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "erlang"
	self.command = 'sh -c "erlc main.erl && erl -noshell -s main start -s init stop"'
	self.file_extension = ".erl"

