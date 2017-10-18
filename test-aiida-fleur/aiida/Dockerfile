#TODO: specify a specific version here

FROM aiidateam/aiida_core_base:0.9.1
MAINTAINER AiiDA Team <info@aiida.net>

# Make directory (if COPY in the line below creates it automatically, it then will
# belong to root and therefore you have permission problems)
RUN mkdir /home/aiida/.dockerscripts

## Copy startup scripts, will be used later
COPY ./scripts/ /home/aiida/.dockerscripts/

# Prepare the folders - the next command will assign it to the correct
# user, so it works with proper permissions when I mount 
# an external named volume
RUN mkdir ~/.aiida/ && mkdir ~/.ssh/keys

# Make  sure all things created have the right permissions
USER root
RUN chown -R aiida:aiida /home/aiida/.dockerscripts && \
    chown -R aiida:aiida /home/aiida/.aiida && \
    chown -R aiida:aiida /home/aiida/.ssh 

USER aiida

WORKDIR /home/aiida/code
RUN mkdir fleur && cd fleur && \
    git clone https://github.com/broeder-j/aiida-fleur.git && \
    cd aiida-fleur && \
    git checkout develop && \
    cd ../ && \
    pip install --user -U -e aiida-fleur
    #git clone https://broeder-j@bitbucket.org/broeder-j/plot_methods.git && \
    #cd plot_methods/ && \
    #pip install -e plot_methods

WORKDIR /home

RUN echo 'eval "$(/home/aiida/.local/bin/verdi completioncommand)"' >> $HOME/.bashrc
    #echo 'alias xcrysden=/home/tutorial_data/xcrysden-1.5.60-bin-semishared/xcrysden' >>/$HOME/.bashrc
EXPOSE 8888


# TO CHECK: also because we need to start the web service and install Apache
# expose https port (for rest? or maybe instead expose jupyter?)
#EXPOSE 443

# Important to end as user root (to run the init script)
USER root

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
