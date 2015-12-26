#!/bin/bash

curl -X POST -d '{"runtime":"python", "user_code_path":"/home/tobe/code/lambda-docker/example/"}' 0.0.0.0:8080

#curl -X POST -d '{"runtime":"python", "user_code_path":"/home/tobe/temp/a/"}' 0.0.0.0:8080
