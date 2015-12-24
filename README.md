# Lambda docker

## Introduction

Lambda-docker is the event-driven code runtime like [AWS Lambda](https://aws.amazon.com/lambda/) service.

You can run Python/Golang/Ruby/Java or any script without setting up servers.

## Usage

```
python ./server.py
```

Or run lambda-docker in container(Notice that can't save user code in Web UI).

```
docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 tobegit3hub/lambda-docker
```

## Demonstration

Run lambda-docker server and go to <http://127.0.0.1:8080>.

![](./example/lambda-docker-input.png)

The user script runs in container without any configuration.

![](./example/lambda-docker-output.png)



