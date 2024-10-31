# Workshop: Chat-base AI coding with LLM

最后更新：Oct 15, 2024 at 18:09:15

> [!NOTE]
>
> per-act-list 中，标志 $\checkmark$ 的表示在 workshop 开始前预先完成。
>


| Act                   | 内容                                                                                                                  | 对象                                                                                                                                                                   | VPN |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|                       | 推荐使用谷歌帐号关联注册或登陆下述平台                                                                                                 | Google<br />https://www.google.com                                                                                                                                   | Y   |
|                       |                                                                                                                     | openAI ChatGPT<br />https://chatgpt.com                                                                                                                              | Y   |
|                       |                                                                                                                     | Anthropic Claude<br />https://claude.ai                                                                                                                              | Y   |
|                       |                                                                                                                     | google gemini<br />https://gemini.google.com                                                                                                                         | Y   |
| 1. $\large\checkmark$ | 需有 openai 帐户<br />充值获取 API                                                                                          | openAI API<br />https://platform.openai.com/playground                                                                                                               | Y   |
| 2. $\large\checkmark$ | 需要有 anthropic 帐户<br />充值获取 API                                                                                      | Anthropic API<br />https://console.anthropic.com/dashboard                                                                                                           | Y   |
|                       | 有一定免费额度使用，用于测试开源 LLM                                                                                                | nvidia.AI<br />https://build.nvidia.com/nim                                                                                                                          | Y   |
|                       | 有一定免费额度使用，用于测试开源 LLM                                                                                                | google cloud API<br />https://console.cloud.google.com                                                                                                               | Y   |
| 3. $\large\checkmark$ | 注册帐户                                                                                                                | GitHub<br />https://www.github.com                                                                                                                                   | -   |
| 4. $\large\checkmark$ | 需要校园网 IP ，申请 Education Lic后，可免费使用（推荐）                                                                               | <span style="background-color: #99f900; color: black;">GitHub Copilot </span><br />https://github.com/education                                                      | -   |
| 5. $\large\checkmark$ | 1.安装 Miniconda, python 版本大于 3.10 即可<br />2.minconda 安装完成后 pip 命令安装相关 python 库<br />`jupyter notebook`,  `pandas`    | minconda - python<br />[官方地址 Latest ](https://docs.anaconda.com/miniconda/)<br />or [清华源 - 24.7.1](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/?C=M&O=A) | -   |
| 6. $\large\checkmark$ | 1. 安装完 vscode 后<br />2. 安装 vscode 插件<br />`python`<br />`github copilot`<br />`cline`<br />`jupyter notebook`<br /> | VScode<br />https://code.visualstudio.com/                                                                                                                           | -   |
| 7.$\large\checkmark$  | 已安装 vscode 的，此处可导入 vscode 配置的方式完成 cursor的安装与配置                                                                      | Cursor<br />https://www.cursor.com                                                                                                                                   | -   |
|                       | Google Colaboratory 在线版 jupyter noteboook<br />打开https://drive.google.com 界面(左上角)： 新建/更多/关联更多应用                     | google colaboratory<br />https://drive.google.com                                                                                                                    | Y   |
| 8.$\large\checkmark$  | LLM 本地部署,电脑配置运行内存需大于8G。<br />ollama 主要用于部署大型语言模型 ，构建                                                                | ollama<br />https://ollama.com                                                                                                                                       |     |
| 9.$\large\checkmark$  | 下载安装<br />运行 web app 必要的容器（环境）                                                                                      | Docker<br />https://www.docker.com                                                                                                                                   |     |
| 10.$\large\checkmark$ | 下载安装<br />本地端运行 LLM 的 web app                                                                                       | open webUI<br />https://docs.openwebui.com                                                                                                                           |     |
| 11.$\large\checkmark$ | 下载<br /> LLM model （比如 llama3.1:8B ..)                                                                              | ollama model<br />https://ollama.com/library                                                                                                                         |     |


> [!NOTE]
>
> ## ollama 安装 & LLM 本地部署
>

```video
https://github.com/user-attachments/assets/0b6a264e-0ade-4f4e-bbf5-bbadb150c137
```

[![video](https://github.com/user-attachments/assets/0b6a264e-0ade-4f4e-bbf5-bbadb150c137)](https://github.com/user-attachments/assets/0b6a264e-0ade-4f4e-bbf5-bbadb150c137)