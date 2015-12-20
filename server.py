#!/usr/bin/env python

import json

import web

urls = (
        '/', 'index'
    )

class index:
    '''
    TODO(tobe): Provide the web form to run user script.
    '''
    def GET(self):
        return "Welcome to lambda-docker!"

    '''
    Post to start container to run user code
    '''
    def POST(self):

        data = web.data()
        print(data)
        parameters = json.loads(data)
        print(parameters)
        user_code_path = parameters.get("user_code_path")

        from runtime import basic_container
        basicContainer = basic_container.BasicContainer()

        # TODO(tobe): Test other runtime containers.
        #runtime="python"
        #user_code_path = "/home/tobe/code/lambda-docker/example/"
        container_memory="1g"
        container_cpu_shares=1024

        container = basicContainer.create_lambda_container(user_code_path, container_memory, container_cpu_shares)
        basicContainer.start_lambda_container(container)

        return "abc"


    if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()
