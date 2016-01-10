#!/usr/bin/env python

from runtime import basic_container
from runtime import python27_container
from runtime import python35_container
from runtime import golang_container
from runtime import ubuntu_container
from runtime import centos_container
from runtime import ruby_container
from runtime import erlang_container
from runtime import php_container
from runtime import node_container
from runtime import java9_container
from runtime import r_container
from runtime import haskell_container
from runtime import perl_container
from runtime import cpp_container
from runtime import c_container
from runtime import lua_container
from runtime import swift_container
from runtime import objectivec_container


def main():
    print("Start lambda-docker service")
    test()
    print("End lambda-docker service")


def test():

    #basicContainer = basic_container.BasicContainer()
    #basicContainer = python27_container.Python27Container()
    #basicContainer = python35_container.Python35Container()
    #basicContainer = ubuntu_container.UbuntuContainer()
    #basicContainer = centos_container.CentosContainer()
    #basicContainer = golang_container.GolangContainer()
    #basicContainer = ruby_container.RubyContainer()
    #basicContainer = erlang_container.ErlangContainer()
    #basicContainer = php_container.PhpContainer()
    #basicContainer = node_container.NodeContainer()
    #basicContainer = java9_container.Java9Container()
    #basicContainer = r_container.RContainer()
    #basicContainer = haskell_container.HaskellContainer()
    #basicContainer = perl_container.PerlContainer()
    #basicContainer = c_container.CContainer()
    #basicContainer = cpp_container.CppContainer()
    #basicContainer = lua_container.LuaContainer()
    #basicContainer = swift_container.SwiftContainer()
    basicContainer = objectivec_container.ObjectiveCContainer()

    # TODO(tobe): Test other runtime containers.
    #runtime="python"
    #user_code_path = "/home/tobe/code/lambda-docker/example/"
    user_code_path = "/root/code/lambda-docker/example/"
    container_memory="1g"
    container_cpu_shares=1024

    container = basicContainer.create_lambda_container(user_code_path, container_memory, container_cpu_shares)
    basicContainer.start_lambda_container(container)
    
    import time
    time.sleep(2)
    log = basicContainer.get_container_log(container)
    print(log)

if __name__ == "__main__":
    main()
