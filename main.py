#!/usr/bin/env python

import docker


def main():
    print("Start lambda-docker service")

    client = docker.Client(base_url="unix:///var/run/docker.sock",
                           version="auto")

    runtime_image = "python"
    command = "ls /lambda"

    function_path = ""
    container_path = ""

    container = client.create_container(image=runtime_image,
                                        command=command,
                                        volumes=["/lambda"],
                                        host_config=client.create_host_config(
                                            binds=[
                                                "/etc/vim/:/lambda:ro",
                                            ])
                                        )

    container_id = container.get("Id")

    client.start(container_id)
    print(client.logs(container_id))

    print("End lambda-docker service")


if __name__ == "__main__":
    main()
