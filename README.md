# Agent Capability Atlas · Agent 能力图谱

面向个人电脑用户的 Agent 外部能力指南：按用途找到工具，理解接入方式，再从一套精简方案开始使用。

目前收录 **53 项工具与运行环境、12 个领域**，覆盖文档、音视频、图像、浏览器、语音、数据检索、逆向分析等。

## 先用哪一套？

日常推荐：**MarkItDown + Pandoc + FFmpeg + ImageMagick**。

| 工具 | 日常用途 |
| --- | --- |
| MarkItDown | 提取文本型 PDF、Word、PPT、Excel 的内容 |
| Pandoc | 将整理后的内容转换为 Word、HTML、EPUB |
| FFmpeg / ffprobe | 视频压缩、剪辑、抽帧、音频提取与媒体参数检查 |
| ImageMagick | 批量缩放、格式转换、拼图 |

基础包不包含扫描件 OCR、语音识别、生图模型或 PDF 排版引擎。这套用法不要求独显。Agent 必须具备本机命令执行能力；纯聊天客户端不能仅靠安装这些软件获得调用能力。

## 打开页面

下载后用现代浏览器打开根目录的 **index.html**。文件包含样式、数据、脚本和安装脚本下载内容，无 CDN 依赖，离线也能搜索与筛选。访问官方来源、首次安装工具需要网络。

页面功能：

- 精选四件套、安装提示词、任务示例。
- 按分类、系统、接口和资源门槛筛选。
- 浏览器本地收藏，导出 Markdown 清单。
- 每项工具的用途、接入方式、边界和官方来源。

也可在仓库目录中启动本地预览：

```sh
python -m http.server 8765 --bind 127.0.0.1
```

然后打开 http://127.0.0.1:8765/ 。用完按 Ctrl+C 停止服务。

## Windows 安装助手

面向 Windows 10/11 x64。在仓库目录打开 PowerShell：

```powershell
# 只检查当前命令是否可用
powershell -NoProfile -File .\install-agent-starter.ps1

# 补齐组件，再执行小样本验收
powershell -NoProfile -File .\install-agent-starter.ps1 -Install
```

脚本通过 WinGet 安装缺失的 uv、FFmpeg、Pandoc、ImageMagick；通过 uv 的隔离环境安装 MarkItDown 和所需文档依赖，按需获取 Python 3.12。已有命令优先复用；MarkItDown 环境按所选依赖配置。不会安装本地大模型或改动 Agent 模型配置。

安装可能需要确认许可、管理员提示以及更新用户 PATH。完成后重新启动 Agent。若系统阻止脚本运行，将错误交给 Agent 或管理员处理，不必永久降低执行策略。默认检测发现缺项时返回非零退出码；这不是已经安装失败的证明。

安装模式会在新建的 `starter-check-*` 目录中验证 Markdown→DOCX→Markdown、图片生成、音频生成与探测。验证仅代表这些样本通过，不保证全部格式兼容。脚本已做语法与检测模式验证，**尚未在全新电脑上完成安装实测**。

## 修改与构建

构建仅依赖 Python 3 标准库，不需要 npm 安装。

```sh
python scripts/build.py
python scripts/build.py --check
```

| 文件 | 用途 |
| --- | --- |
| `data/tools.json` | 工具条目与来源链接 |
| `src/template.html` | 页面布局、样式与交互 |
| `install-agent-starter.ps1` | Windows 安装及检测脚本 |
| `scripts/build.py` | 校验数据，将数据和安装脚本嵌入页面 |
| `index.html` | 构建产物；可直接打开，也是分发入口 |

修改数据、模板或安装脚本后，重新构建并一并提交 `index.html`。收藏保存在浏览器 localStorage，不写回仓库。静态页面没有账号、服务器数据库或自动安装权限。

## 收录与来源

目录资料查阅日期：2026-10-24；精简方案整理日期：2026-10-27。优先引用官方项目与文档，具体来源见每项工具。资源负担标签、推荐组合与使用场景属于编辑判断，不是性能测试或厂商最低配置。所有收录工具并未逐一安装实测；模型、软件与云服务各有许可及费用条件。

类似目录可参考：

- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)：MCP 服务目录。
- [awesome-ai-cli](https://github.com/vincentsch/awesome-ai-cli)：供 Agent 使用的命令行工具目录。
- [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)：Agent 工作流与技能合集。

本项目不隶属于所列工具的维护方。第三方项目与模型继续适用各自许可；收录不代表授权转售或对兼容性的保证。
