# wechatbot-provider-windows
这是一个可以使用 docker 部署的 pc 版微信，对外暴露了 rpc 调用的钩子。
当然你也可以 fork 项目继续完善代码用 http 实现，该项目集成了一个小型的 fastapi 服务端。


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
  - CPU：至少 1Ghz吧

# Install

## 1. 拉取镜像

## 2. 启动镜像

## 3. 安装应用


# 鸣谢

本项目只是对以下两个项目的整合，所以最终的贡献还是属于以下两位大佬的项目。

- [wechat_box](https://github.com/Saroth/docker_wechat)
- [WeChatFerry](https://github.com/lich0821/WeChatFerry)
