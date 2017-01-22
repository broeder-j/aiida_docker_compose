# Brief summary

This is a docker-compose setup to have three containers:

- aiida: AiiDA (using Django backend), connected to 

- db: a postgres DB, 
  
and with ssh keys preconfigured to connect to 

- torquessh: a machine with torque installed, where the user aiida on container
  aiida can connect already passwordless to app@torquessh.
  I reuse torquessh-base, and I install Quantum ESPRESSO

# How to start everything

Run the script startup_firsttime.sh, that will generate ssh keys and 
passwords, start the services, and setup AiiDA

# Data persistence

The following data is persistent:

- volume "dbdata": all DB data (tables, etc.) from postgres
- volume "aiidalogs": the .aiida folder
- volume "aiidarepo": the AiiDA file repository
- folder ~/.ssh/keys, mounted from the host folder init/sshkeys/sharedfolder,
  created in step 1 (actually this is needed only at the first start)

Currently, after starting everything you need to do

``docker-compose exec --user aiida aiida bash``

if you want to connect and use the machine.

# To shutdown everything

Use `docker-compose down`. Note that this will keep the data.
If you want to kill also the data (i.e. the named data volumes), use
`docker-compose down -v`

# Todo

In the short term:

  - move pulled images from 'giovannipizzi' docker hub account to 'aiidateam'

In the mid term:

  - start the AiiDA REST, and use it to control AiiDA from the outside? or jupyter?

