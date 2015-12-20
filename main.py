#!/usr/bin/env python

import docker


def create_docker_client():
    client = docker.Client(base_url="unix:///var/run/docker.sock",
                           version="auto")
    return client


def create_lambda_container(client):

    runtime_image = "python"
    command = "/lambda/main.py"

    lambda_function_path = "/home/tobe/code/lambda-docker/example/"
    container_function_path = "/lambda"

    container_memory = "1g"
    container_cpu_shares = 1024

    container = client.create_container(image=runtime_image,
                                        command=command,
                                        volumes=["/lambda"],
                                        host_config=client.create_host_config(
                                            binds={
                                                lambda_function_path: {
                                                    "bind": container_function_path,
                                                    "mode": "ro",
                                                }
                                            },
                                            mem_limit=container_memory,
                                        ),
                                        cpu_shares=container_cpu_shares,
                                        )

    return container


def main():
    print("Start lambda-docker service")

    client = create_docker_client()

    container = create_lambda_container(client)

    container_id = container.get("Id")
    print(container_id)

    client.start(container_id)
    print(client.logs(container_id))

    print("End lambda-docker service")


if __name__ == "__main__":
    main()
