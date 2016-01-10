
import basic_container

class ElixirContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	# Refer to https://github.com/msaraiva/elixir
	self.image = "msaraiva/elixir"
        self.command = "elixir main.exs"
        self.file_extension = ".exs"
