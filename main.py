#!/usr/bin/env python

from runtime import basic_container
from runtime import python27_container


def main():
    print("Start lambda-docker service")
    test()
    print("End lambda-docker service")


def test():

    #basicContainer = python27_container.Python27Container()
    basicContainer = basic_container.BasicContainer()

    # TODO(tobe): Test other runtime containers.
    runtime="python"
    user_code_path = "/home/tobe/code/lambda-docker/example/"
    container_memory="1g"
    container_cpu_shares=1024

    container = basicContainer.create_lambda_container(user_code_path, container_memory, container_cpu_shares)
    basicContainer.start_lambda_container(container)


if __name__ == "__main__":
    main()
