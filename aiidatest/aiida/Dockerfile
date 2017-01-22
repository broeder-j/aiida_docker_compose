# TODO: replace this with the docker image on the account aiidateam
FROM giovannipizzi/aiida_core-base

MAINTAINER AiiDA Team <info@aiida.net>

# Make directory (if COPY in the line below creates it automatically, it then will
# belong to root and therefore you have permission problems)
RUN mkdir /home/aiida/.dockerscripts

## Prepare startup scripts
COPY ./scripts/wait-for-it.sh /home/aiida/.dockerscripts/wait-for-it.sh
COPY ./scripts/aiida_setup.sh /home/aiida/.dockerscripts/aiida_setup.sh
COPY ./scripts/aiida_setup_init_script.sh /etc/my_init.d/ZZ_aiida_setup_init_script.sh

# Prepare the folder, the next command will assign it to the correct
# user, so it works when I mount an external named volume
RUN mkdir ~/.aiida/ && mkdir ~/.ssh/keys

# Make  sure all things created have the right permissions
USER root
RUN chown -R aiida:aiida /home/aiida/.dockerscripts && \
    chown -R aiida:aiida /home/aiida/.aiida && \
    chown -R aiida:aiida /home/aiida/.ssh && \

# TO CHECK: also because we need to start the web service and install Apache
# expose https port (for rest? or maybe instead expose jupyter?)
#EXPOSE 443

# Important to end as user root (to run the init script)
USER root

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
