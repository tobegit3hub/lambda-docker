
import basic_container

class SwiftContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	# Refer to https://github.com/swiftdocker/docker-swift
	self.image = "swiftdocker/swift"
        self.command = "swift main.swift"
        self.file_extension = ".swift"
