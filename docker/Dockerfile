# 基于 Fedora 39 的镜像
FROM fedora:39
LABEL describe="Fedora for WeChat hook, based on LXDE, Wine, xRDP, WeChatFerry."

WORKDIR /root

RUN dnf update -y \
        && dnf groupinstall -y "LXDE" \
        && dnf install -y wine wget xrdp git xorg-x11-server-Xvfb xauth \
        && dnf clean all

RUN wget https://github.com/danni-cool/wechatbot-provider-windows/releases/download/3.9.11.25/python-3.12.4-amd64.exe -O python-installer.exe

RUN xvfb-run --auto-servernum --server-args='-screen 0 1024x768x24' wine python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 \
        && rm -f python-installer.exe

ENV PATH="/root/.wine/drive_c/Program Files/Python312:${PATH}"

RUN wget https://github.com/danni-cool/wechatbot-provider-windows/releases/download/3.9.11.25/WeChatSetup-3.9.11.25.exe -O WeChatSetup.exe && \
        xvfb-run --auto-servernum --server-args='-screen 0 1024x768x24' wine WeChatSetup.exe /S && \
        rm -f WeChatSetup.exe

COPY ./docker/res ./res

RUN echo "root:123" | chpasswd \
        && mkdir ~/Desktop \
        && mv res/*.desktop ~/Desktop \
        && mv res/*.sh . \
        && chmod +x /root/entrypoint.sh
# && unzip -o res/v*.zip -d res


EXPOSE 3389
EXPOSE 10086
EXPOSE 10087

ENTRYPOINT ["./entrypoint.sh"]
CMD ["bash"]
