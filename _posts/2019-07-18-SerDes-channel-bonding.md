---
title: SerDes channel bonding
categories: FPGA接口设计
date: 2019-07-17 15:57:23
---
# 通道绑定作用
Channel bonding：通道绑定。SerDes每个通道如果不是完全等长，那么不同通道的数据的到达时间就不同。通道绑定就是用来消除通道间的数据偏移。设置channel bonding后，gtx/gth将会同时发送channel bonding character（or a sequence of character），接收通道在接收到后便可以借此调整通道间的数据偏移。
RX channel bonding只支持8B/10B编码。
因为channel bonding需要使用RX弹性缓冲，所以需要启用RX buf。
启用改功能的步骤如下：
![pic1](https://github.com/njustzsqimq/njustzsqimq.github.io/blob/master/_posts/images/channel_bonding_use.png)

