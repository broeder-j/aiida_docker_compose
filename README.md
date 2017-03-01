# aiida_docker_compose

This repository contains some examples of docker-compose configurations to

- create Docker images specific to a given code and plugin

- start automatically AiiDA and all related services

- run some basic tests to check functionality

# Learning more

Read the README files in each folder, or look at what Travis 
does at each test (in the `.travis.yml` file).

As an example, the `test-aiida-qepw` folder contains an example
that builds a full system with quantum espresso, runs a simple test
with pw.x, and performs a basic check to verify if the result is the
expected one.

# Repository location

https://github.com/aiidateam/aiida_docker_compose

