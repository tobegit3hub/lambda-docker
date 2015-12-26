#!/usr/bin/env python

import os
import time

import web
from web import form

from runtime import basic_container

render = web.template.render('static/templates/')

myform = form.Form(
    form.Dropdown("Runtime", ["python:2.7", "python:3.5", "golang", "ubuntu", "centos", "ruby", "javascript", "erlang"]),
    form.Textbox("Load local file"),
    form.Checkbox("Edit online code"),
    form.Textarea("Online code"))

urls = (
        '/', 'index'
    )

class index:

    '''
    Return web form to trigger lambda service.
    '''
    def GET(self):
        form = myform()

        return render.index(form)

    '''
    Post to start container to run user code
    '''
    def POST(self):

        # Parse post parameter
        parameters = web.input()
        print(parameters)

        # Example: "python:2.7"
        runtime = parameters.get("Runtime")
	
	is_edit_online_code = parameters.has_key("Edit online code")
		
	if is_edit_online_code == False:
            # Example: "/home/tobe/code/lambda-docker/example/"
            load_file_path = parameters.get("Load local file")
	    user_code_path = load_file_path

        else:
            submit_code = parameters.get("Online code")

            tmp_path = "/tmp"
            with open("/tmp/main.py", "w") as text_file:
                text_file.write(submit_code)
	    user_code_path = "/tmp/main.py"

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
