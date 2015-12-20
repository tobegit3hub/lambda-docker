#!/usr/bin/env python

import main


def mock():
    print "Mock lambda-docker event"

    client = main.create_docker_client()

    container = main.create_lambda_container(client)

    container_id = container.get("Id")

    client.start(container_id)
    print(client.logs(container_id))

if __name__ == "__main__":
    mock()
