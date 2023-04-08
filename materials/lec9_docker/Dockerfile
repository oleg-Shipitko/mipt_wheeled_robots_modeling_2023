FROM ros:melodic-ros-base
FROM ros:melodic-robot
FROM ros:melodic-perception

RUN sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
    sudo apt update && sudo apt install -y ros-melodic-desktop-full wget zsh tree

# zsh and oh-my-zsh installation
RUN set -uex; \
    wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh; \
    sh ./install.sh; \
    rm ./install.sh

# vs code installation
RUN sudo apt install --yes apt-utils libasound2 curl; \
    echo "deb [arch=amd64] http://packages.microsoft.com/repos/vscode stable main" | sudo \
    tee /etc/apt/sources.list.d/vs-code.list; \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg; \
    sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg; \
    sudo apt update; \
    sudo apt install --yes code

ADD ./signal_generator_node.py /signal_generator_node.py 
ADD ./signal_filter_node.py /signal_filter_node.py

ADD ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
