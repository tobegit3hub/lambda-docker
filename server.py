#!/usr/bin/env python

import os
import time

import web
from web import form

from runtime import basic_container

render = web.template.render('templates/')

myform = form.Form(
    form.Dropdown('Runtime', ['python:2.7', 'python:3.5', 'golang']),
    form.Textbox("User code path"),
    form.Checkbox('Use online script'),
    form.Textarea('Script content'))

urls = (
        '/', 'index'
    )

class index:

    '''
    Return web form to trigger lambda service.
    '''
    def GET(self):
        form = myform()

        return render.formtest(form)

    '''
    Post to start container to run user code
    '''
    def POST(self):

        # Parse post parameter
        parameters = web.input()
        print(parameters)

        # Example: "python:2.7"
        runtime = parameters.get("Runtime")

        is_use_online_script = parameters.has_key("Use online script")
        if is_use_online_script:
            script_content = parameters.get("Script content")

            # Example: "/home/tobe/code/lambda-docker/"
            user_code_path = os.getcwd()
            with open("main.py", "w") as text_file:
                text_file.write(script_content)
        else:
            # Example: "/home/tobe/code/lambda-docker/example/"
            user_code_path = parameters.get("User code path")

        # Start lambda container
        # TODO(tobe): Test other runtime containers.
        basicContainer = basic_container.BasicContainer()

        container_memory="1g"
        container_cpu_shares=1024

        container = basicContainer.create_lambda_container(user_code_path, container_memory, container_cpu_shares)
        basicContainer.start_lambda_container(container)

        # Wait for logs of container
        time.sleep(2)

        log = basicContainer.get_container_log(container)
        if log:
            return log
        else:
            return "Success to run lambda container"


    if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()
