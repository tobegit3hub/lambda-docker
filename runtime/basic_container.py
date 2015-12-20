import docker


class BasicContainer:

    def __init__(self):
        self.client = self.create_docker_client()
        self.image = "python"
        self.command = "python /lambda/main.py"


    '''
    Connect with docker daemon.

    TODO(tobe): Make it configurable to connect with remote docker daemon.
    '''
    def create_docker_client(self):
        client = docker.Client(base_url="unix:///var/run/docker.sock",
                               version="auto")
        return client

    '''
    Create lambda container.
    '''
    def create_lambda_container(self, user_file_path, container_memory="1g", container_cpu_shares=1024):

        container_function_path = "/lambda"

        container = self.client.create_container(image=self.image,
                                            command=self.command,
                                            volumes=[container_function_path],
                                            host_config=self.client.create_host_config(
                                                binds={
                                                    user_file_path: {
                                                        "bind": container_function_path,
                                                        "mode": "ro",
                                                        }
                                                },
                                                mem_limit=container_memory,
                                            ),
                                            cpu_shares=container_cpu_shares,
                                            )

        return container


    '''
    Start container.
    '''
    def start_lambda_container(self, container):

        container_id = container.get("Id")
        print(container_id)
        self.client.start(container_id)
        print(self.client.logs(container_id))


    '''
    Get logs of container.
    '''
    def get_container_log(self, container):
        container_id = container.get("Id")
        log = self.client.logs(container_id)

        return log

