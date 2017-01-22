# TODO: replace this with the docker image on the account aiidateam
FROM giovannipizzi/aiida_core-base

MAINTAINER AiiDA Team <info@aiida.net>

# Make directory (if COPY in the line below creates it automatically, it then will
# belong to root and therefore you have permission problems)
RUN mkdir /home/aiida/.dockerscripts

## Prepare startup scripts
COPY ./scripts/wait-for-it.sh /home/aiida/.dockerscripts/wait-for-it.sh
COPY ./scripts/aiida_setup.sh /home/aiida/.dockerscripts/aiida_setup.sh
COPY ./scripts/computer-setup-input.txt /home/aiida/.dockerscripts/computer-setup-input.txt
COPY ./scripts/computer-configure-input.txt /home/aiida/.dockerscripts/computer-configure-input.txt
COPY ./scripts/code-setup-input.txt /home/aiida/.dockerscripts/code-setup-input.txt
COPY ./scripts/test_pw.py /home/aiida/.dockerscripts/test_pw.py
COPY ./scripts/data/ /home/aiida/.dockerscripts/data/

# Prepare the folder, the next command will assign it to the correct
# user, so it works when I mount an external named volume
RUN mkdir ~/.aiida/ && mkdir ~/.ssh/keys

# Make  sure all things created have the right permissions
USER root
RUN chown -R aiida:aiida /home/aiida/.dockerscripts && \
    chown -R aiida:aiida /home/aiida/.aiida && \
    chown -R aiida:aiida /home/aiida/.ssh 

# TO CHECK: also because we need to start the web service and install Apache
# expose https port (for rest? or maybe instead expose jupyter?)
#EXPOSE 443

# Important to end as user root (to run the init script)
USER root

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
