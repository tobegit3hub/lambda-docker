
import basic_container

class LuaContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	# Refer to https://github.com/abaez/lua
	self.image = "abaez/lua"
        self.command = "lua main.lua"
        self.file_extension = ".lua"
