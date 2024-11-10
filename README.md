# wechatbot-provider-windows

这是一个可以使用 docker 部署的 pc 版微信，对外暴露了 rpc 调用的钩子，适配 wechatFerry 的 rpc 调用

## 免责声明

本开源作品（以下简称“作品”）由 [danni-cool](https://github.com/danni-cool)（以下简称“作者”）开发并维护, 作者在此声明，使用本作品的任何人（以下简称“使用者”）应当遵守以下条款和条件：

**1. 法律风险**：使用者在使用和编译本作品时，应当自行承担可能的法律风险。作者不对使用者因使用本作品而引发的任何法律纠纷、诉讼或处罚承担任何责任。

**2. 禁止盈利**：本作品仅供非商业用途。使用者不得以任何形式将本作品用于盈利目的，包括但不限于销售、租赁、广告和其他商业活动。

**3. 禁止危害社会**：使用者不得将本作品用于任何可能危害社会公共利益的活动，包括但不限于传播虚假信息、进行网络攻击和其他危害社会安全的行为。

**4. 禁止宣扬政治立场**：使用者不得利用本作品进行任何形式的政治宣传或表达政治立场的活动。

**5. 禁止传播色情和暴力**：使用者不得利用本作品传播任何形式的色情、暴力内容或其他不良信息。

作者保留对本作品的所有权利。使用者在使用本作品时，视为同意本免责声明的所有条款。如有任何违反上述条款的行为，使用者应当立即停止使用本作品，并自行承担相应的法律责任。

# 硬件要求：

- 磁盘：构建的镜像大小约 7G。长期使用将持续扩大；
  - Wine 第一次启动，自动初始化后容器占用 1.49G；
  - 微信安装后，初始状态占用 1.41G。
  - 微信长期使用，磁盘占用会持续增加；
- 内存：
  - 桌面登录后，总占用 194M；
  - 微信启动，总占用约 1.7G，微信登录后，总占用约 4.9G。 宿主机需要预留充足的内存空间；
- CPU: x86/amd64 架构

# 安装

## 1. 启动容器

```bash
docker run -itd \
    -p 13389:3389 \
    -p 10086:10086 \
    -p 10087:10087 \
    --ulimit nofile=8192 \
    --name DESKTOP \
    dannicool/wechatbot-provider-windows
```

- rpc 推消息端口是 10086
- rpc 收消息端口是 10087

目录挂载：
- 程序文件： ./wechat/program => /root/.wine/drive_c/Program\ Files/Tencent/WeChat
- 用户数据： ./wechat/user_dat => /root/.wine/drive_c/users/root/AppData/Roaming/Tencent/WeChat
将程序和用户数据目录挂载到宿主机，可避免在容器重置后再次安装程序。

## 2. 使用 rdp 连接

1. 推荐 [Microsoft remote desktop](https://apps.microsoft.com/detail/9wzdncrfj3ps?hl=en-US&gl=US)，端口是 13389，默认`root` 密码为`123`

## 3. 点击 startService 等待唤起微信登陆


**其他说明**

- wechat 常规配置，左下角 Settings：
- Notifications：关闭所有
- General -> General：不选所有
- Manage Files -> Auto-Download：不选

启动并登录后，直接关闭远程桌面，不要 Logout。因为登出后图形界面下运行的所有程序都会退出。

## QA

- 故障现象：不同环境现象不同，目前遇到以下几种
  - 启动过程中 Wine 报错并退出
  - Wine 启动立即报错并退出
  - xRDP 连接报错
- 故障分析：
  - 目前启动异常的情况，常见于使用旧发行版系统的服务器， 如：CentOS 7 (kernel 4.x)。
  - 经验证，使用较新发行版系统的服务器，都可以正常运行。 如：Fedora 39/40 (kernel 6.x) 具体原因暂不明确，
  - 推测与内核版本有关。
- 解决方案：
  - 建议使用较新的 Linux 发行版。


# 鸣谢

本项目只是对以下两个项目的整合，并保证最新的服务可用，最终的贡献是属于以下两位大佬的项目

- [wechat_box](https://github.com/Saroth/docker_wechat)
- [WeChatFerry](https://github.com/lich0821/WeChatFerry)
