
FROM fedora:39

WORKDIR /root

RUN dnf update -y \
        && dnf groupinstall -y "LXDE" \
        && dnf install -y wine wget xrdp git xorg-x11-server-Xvfb xauth \
        && dnf clean all

RUN wget https://github.com/danni-cool/wechatbot-provider-windows/releases/download/3.9.11.25/python-3.12.4-amd64.exe -O python-installer.exe

RUN xvfb-run --auto-servernum --server-args='-screen 0 1024x768x24' wine python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 \
        && rm -f python-installer.exe

RUN wget https://github.com/danni-cool/wechatbot-provider-windows/releases/download/3.9.11.25/WeChatSetup-3.9.11.25.exe -O WeChatSetup.exe && \
        xvfb-run --auto-servernum --server-args='-screen 0 1024x768x24' wine WeChatSetup.exe /S && \
        rm -f WeChatSetup.exe

ENV PATH="/root/.wine/drive_c/Program Files/Tencent/WeChat:/root/.wine/drive_c/Program Files/Python312:${PATH}"

COPY ./docker ./install

RUN echo "root:123" | chpasswd \
        && mkdir ./Desktop \
        && mkdir ./logs \
        && mkdir ./sdk \
        && mv install/sh/*.desktop ./Desktop \
        && mv install/sh/*.sh . \
        && mv install/sdk/* ./sdk \
        && mv install/app/* . \
        && chmod +x ./entrypoint.sh

RUN     xvfb-run --auto-servernum --server-args='-screen 0 1024x768x24' wine install.bat /S && \ 
        rm -f install.bat

RUN chmod +x start.sh

EXPOSE 3389
EXPOSE 10086
EXPOSE 10087

ENTRYPOINT ["./entrypoint.sh"]
CMD ["bash"]
