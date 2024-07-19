# wechatbot-provider-windows
这是一个可以使用 docker 部署的 pc 版微信，对外暴露了 rpc 调用的钩子，适配 wechatFerry 的rpc调用


# 免责声明

本开源作品（以下简称“作品”）由 [danni-cool](https://github.com/danni-cool)（以下简称“作者”）开发并维护, 作者在此声明，使用本作品的任何人（以下简称“使用者”）应当遵守以下条款和条件：

**1. 法律风险**：使用者在使用和编译本作品时，应当自行承担可能的法律风险。作者不对使用者因使用本作品而引发的任何法律纠纷、诉讼或处罚承担任何责任。

**2. 禁止盈利**：本作品仅供非商业用途。使用者不得以任何形式将本作品用于盈利目的，包括但不限于销售、租赁、广告和其他商业活动。

**3. 禁止危害社会**：使用者不得将本作品用于任何可能危害社会公共利益的活动，包括但不限于传播虚假信息、进行网络攻击和其他危害社会安全的行为。

**4. 禁止宣扬政治立场**：使用者不得利用本作品进行任何形式的政治宣传或表达政治立场的活动。

**5. 禁止传播色情和暴力**：使用者不得利用本作品传播任何形式的色情、暴力内容或其他不良信息。

作者保留对本作品的所有权利。使用者在使用本作品时，视为同意本免责声明的所有条款。如有任何违反上述条款的行为，使用者应当立即停止使用本作品，并自行承担相应的法律责任。


# 硬件要求：

  - 磁盘：构建的镜像大小约5G。安装微信后达到7G，长期使用将持续扩大；
  - 内存：正常运行是2-3g，初始化安装程序会占用到7g，所以给一个8g的内存比较稳妥
  - CPU：只支持 X86 架构（amd64），频率至少 1Ghz吧

# 安装

## 1. 拉取镜像

```bash

docker pull dannicool/wechatbot-provider-windows
```

## 2. 准备资源

1. 创建一个本地文件夹install，用来存放安装的资源文件。
2. 下载 [必要资源](https://github.com/danni-cool/wechatbot-provider-windows/releases/tag/v3.9.10.27)，一个是 python，另一个是 wechat-setup, 都先放到本地文件夹 install

## 3. 启动容器

```bash
docker run -itd \
    -p 13389:3389 \
    -p 10086:10086 \
    -p 10087:10087 \
    -v install:/root/res/install \
    --ulimit nofile=8192 \
    --name DESKTOP \
    dannicool/wechatbot-provider-windows
```

- rpc推消息端口是 10086
- rpc收消息端口是 10087

## 4. 使用 rdp 连接

1. 推荐 [Microsoft remote desktop](https://apps.microsoft.com/detail/9wzdncrfj3ps?hl=en-US&gl=US)，端口是 13389，默认`root` 密码为`123`

## 5.安装应用

连接上远程桌面后

1.点击 1.python3Setup，**安装 python3 环境**, 需要勾选 `Add python.exe to PATH`

<img src="https://github.com/user-attachments/assets/f7bb6a99-113e-4dbc-bb43-bca079278a0c" width=300 />

2.点击 2.WeChatSetup，**安装 wechat 应用**，并登录

3.点击 3.StartService，启动python程序暴露rpc地址，程序转为守护运行状态

后续日常重启后，只要点击桌面 wechat 图标登陆后 重复步骤 3 即可

**其他说明**

- wechat 常规配置，左下角Settings：
- Notifications：关闭所有
- General -> General：不选所有
- Manage Files -> Auto-Download：不选

启动并登录后，直接关闭远程桌面，不要Logout。因为登出后图形界面下运行的所有程序都会退出。

# 鸣谢

本项目只是对以下两个项目的整合，并保证最新的服务可用，最终的贡献是属于以下两位大佬的项目

- [wechat_box](https://github.com/Saroth/docker_wechat)
- [WeChatFerry](https://github.com/lich0821/WeChatFerry)
