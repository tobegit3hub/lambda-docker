
import basic_container

# Refer to https://clojurebridge.github.io/community-docs/docs/getting-started/helloworld/
class ClojureContainer(basic_container.BasicContainer):

    def __init__(self):
	super(self.__class__, self).__init__()
        
	self.image = "clojure"
	self.command = 'sh -c "lein new main && lein run"'
	self.file_extension = ".clj"

