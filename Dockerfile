FROM phusion/baseimage:focal-1.2.0

# Set correct environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV WINEARCH=win64
ENV DISPLAY=:0.0
ENV WINEPREFIX=/home/root/.wine
ENV HOME=/home/root/
ENV NOVNC_HOME=/usr/libexec/noVNCdim

# Updating and upgrading a bit.
# Install vnc, window manager and basic tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    language-pack-zh-hant \
    x11vnc \
    xdotool \
    wget \ 
    supervisor \ 
    fluxbox \
    git \ 
    sudo \
    apt-transport-https \
    ca-certificates \
    cabextract \
    gnupg \
    gpg-agent \
    locales \
    p7zip \
    pulseaudio \
    pulseaudio-utils \
    tzdata \
    unzip\ 
    xz-utils \
    # Installation of winbind to stop ntlm error messages.
    winbind \
    zenity && \
    dpkg --add-architecture i386 && \
    # We need software-properties-common to add ppas.
    curl https://dl.winehq.org/wine-builds/winehq.key -o /tmp/Release.key && \
    apt-get install -y --no-install-recommends software-properties-common && \
    apt-key add /tmp/Release.key && \
    apt-add-repository 'https://dl.winehq.org/wine-builds/ubuntu/' && \
    add-apt-repository ppa:cybermax-dexter/sdl2-backport && \
    apt-get update && \
    apt-get install -y --no-install-recommends winehq-staging && \
    apt-get install -y --no-install-recommends xvfb python3 && \
    # Install winetricks
    curl -SL -k https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks  -o /usr/local/bin/winetricks && \
    chmod a+x /usr/local/bin/winetricks  && \
    # Create user for ssh
    # adduser \
    #         --home /home/docker \
    #         --disabled-password \
    #         --shell /bin/bash \
    #         --gecos "user for running application" \
    #         --quiet \
    #         docker && \
    echo "root:1234" | chpasswd && \
    # adduser docker sudo && \
    # Clone noVNC
    mkdir -p "${NOVNC_HOME}"/utils/websockify && \
    curl -L https://github.com/novnc/noVNC/archive/v1.3.0.tar.gz | tar xz --strip 1 -C "${NOVNC_HOME}" && \
    curl -L https://github.com/novnc/websockify/archive/v0.10.0.tar.gz | tar xz --strip 1 -C "${NOVNC_HOME}"/utils/websockify && \
    chmod +x -v "${NOVNC_HOME}"/utils/novnc_proxy && \
    ln -s "${NOVNC_HOME}"/vnc.html "${NOVNC_HOME}"/index.html && \
    chown -R root "${NOVNC_HOME}" && \
    # Cleaning up.
    apt-get autoremove -y --purge && \
    apt-get clean -y && \
    rm -rf /home/wine/.cache && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# 复制应用程序代码到工作目录
COPY . /home/root

COPY linux/bin /bin

COPY linux/.fluxbox /home/root/.fluxbox

# Add supervisor conf
COPY linux/conf.d/* /etc/supervisor/conf.d/

# Add entrypoint.sh
COPY linux/sh/entrypoint.sh /etc/entrypoint.sh


ENTRYPOINT ["/bin/bash","/etc/entrypoint.sh"]

# Expose Port
EXPOSE 8080 22 3001