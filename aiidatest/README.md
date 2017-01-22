# Brief summary

This is a docker-compose setup to have three containers:

- aiida: AiiDA (using Django backend), connected to 

- db: a postgres DB, 
  
and with ssh keys preconfigured to connect to 

- torquessh: a machine with torque installed, where the user aiida on container
  aiida can connect already passwordless to app@torquessh

# How to start everything

1. enter the folder 'init' and run the script "start_all_and_setup.sh"
   (it generates passwords and ssh keys)
2. go back to the top folder, and run 'docker-compose up --build' 
   (if you stop the machines, from the second time on, you don't need --build')

# Data persistence

The following data is persistent:

- volume "dbdata": all DB data (tables, etc.) from postgres
- volume "aiidalogs": the .aiida folder
- volume "aiidarepo": the AiiDA file repository
- folder ~/.ssh/keys, mounted from the host folder init/sshkeys/sharedfolder,
  created in step 1 (actually this is needed only at the first start)

Currently, after starting everything you need to do

``docker exec -it AIIDA_CONTAINER_ID /bin/bash``

to connect and use the machine.

# Todo
In the short term:

- add mpirun to torquessh

- improve AiiDA image to use git and choose a specific branch/commit (useful for testing?)

- put these images (aiida and torque) on docker-hub, probably on a different repo, and here just show an example of how to implement a specific addition (e.g. only install some plugin and the needed code on the torquessh image)

- improve the AiiDA entrypoint 

  - also setup the computer (probably requires to have 'verdi computer' to
    work in non-interactive mode, both 'setup' and 'configure')

  - probably also setup the code (and install some code on torquessh)

  - have an easy way to specify which tests to run (e.g., have a place you
    should put the test files, that is tested at startup)

  - Check how to integrate this with e.g. travis-ci, to start everything
    and then run the tests

In the mid term:

- start the AiiDA REST, and use it to control AiiDA from the outside? or jupyter?

- check if the daemon is running, otherwise run it (depending on an envvar)

