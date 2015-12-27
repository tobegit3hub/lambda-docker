#!/usr/bin/env python

import os
import time

import web
from web import form

from runtime import basic_container
from runtime import python27_container
from runtime import python35_container
from runtime import ubuntu_container
from runtime import centos_container
from runtime import golang_container
from runtime import ruby_container
from runtime import erlang_container
from runtime import node_container
from runtime import php_container
from runtime import java9_container
from runtime import javaopenjdk9_container

render = web.template.render('static/templates/')

RUNTIME_PYTHON27 = "Python 2.7"
RUNTIME_PYTHON35 = "Python 3.5"
RUNTIME_GOLANG = "Golang"
RUNTIME_UBUNTU = "Linux/Ubuntu"
RUNTIME_CENTOS = "Linux/CentOS"
RUNTIME_RUBY = "Ruby"
RUNTIME_ERLANG = "Erlang"
RUNTIME_NODE = "NodeJS"
RUNTIME_PHP = "PHP"
RUNTIME_JAVA9 = "Java 9"
RUNTIME_JAVAOPENJDK9 = "Java OpenJDK 9"

myform = form.Form(
    form.Dropdown("Runtime", [RUNTIME_PYTHON27, RUNTIME_PYTHON35, RUNTIME_GOLANG, RUNTIME_UBUNTU, RUNTIME_CENTOS, RUNTIME_RUBY, RUNTIME_ERLANG, RUNTIME_NODE, RUNTIME_PHP, RUNTIME_JAVA9, RUNTIME_JAVAOPENJDK9]),
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

        # Example: "python27"
        runtime = parameters.get("Runtime")

        # Start lambda container
        if runtime == RUNTIME_PYTHON27:
            containerRuntime = python27_container.Python27Container()
        elif runtime == RUNTIME_PYTHON35:
            containerRuntime = python35_container.Python35Container()
        elif runtime == RUNTIME_GOLANG:
            containerRuntime = golang_container.GolangContainer()
        elif runtime == RUNTIME_UBUNTU:
            containerRuntime = ubuntu_container.UbuntuContainer()
        elif runtime == RUNTIME_CENTOS:
            containerRuntime = centos_container.CentosContainer()
        elif runtime == RUNTIME_RUBY:
            containerRuntime = ruby_container.RubyContainer()
        elif runtime == RUNTIME_ERLANG:
            containerRuntime = erlang_container.ErlangContainer()
	elif runtime == RUNTIME_NODE:
	    containerRuntime = node_container.NodeContainer()
	elif runtime == RUNTIME_PHP:
	    containerRuntime = php_container.PhpContainer()
	elif runtime == RUNTIME_JAVA9:
	    containerRuntime = java9_container.Java9Container()
	elif runtime == RUNTIME_JAVAOPENJDK9:
	    containerRuntime = javaopenjdk9_container.JavaOpenjdk9Container()
        else:
            containerRuntime = basic_container.BasicContainer()

	# Example: True if click the checkbox	
	is_edit_online_code = parameters.has_key("Edit online code")
		
	if is_edit_online_code == False:
            # Example: "/home/tobe/code/lambda-docker/example/"
            load_file_path = parameters.get("Load local file")
	    user_code_path = load_file_path

        else:
	    # Example: "print('test python runtime')"
            online_code = parameters.get("Online code")

            tmp_path = "/tmp/"
	    user_code_file_name = "main" + containerRuntime.file_extension
            with open(tmp_path + user_code_file_name, "w") as text_file:
                text_file.write(online_code)
	    user_code_path = tmp_path

        # Example: "python27"
        runtime = parameters.get("Runtime")

	# TODO(tobe): Make is configurable for users to set cpu and memory
        container_memory="1g"
        container_cpu_shares=1024

        # Start lambda container
        container = containerRuntime.create_lambda_container(user_code_path, container_memory, container_cpu_shares)
        containerRuntime.start_lambda_container(container)

        # Wait for logs of container
        time.sleep(1)

        log = containerRuntime.get_container_log(container)
        if log:
            return log
        else:
            return "Success to run lambda container"


    if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()
