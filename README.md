# Agent Capability Atlas · Agent 工具图谱

[English](README.en.md) · **简体中文**

一份面向个人电脑与 Agent 的实用工具清单，记录好用的工具、适用场景、使用边界与官方来源。**只做收录，不提供安装教程。**

**87 项工具与运行环境 · 14 个能力领域 · 21 项近期热门**

**在线浏览**：<https://jingao-shen.github.io/agent-capability-atlas/>

[![Link check](https://github.com/JingAo-Shen/agent-capability-atlas/actions/workflows/link-check.yml/badge.svg)](https://github.com/JingAo-Shen/agent-capability-atlas/actions/workflows/link-check.yml)

**分类**：[运行底座](#运行底座) · [Agent 框架与技能](#agent-框架与技能) · [浏览器与桌面](#浏览器与桌面) · [文档与 OCR](#文档与-ocr) · [数据与记忆](#数据与记忆) · [语音能力](#语音能力) · [音视频与图像](#音视频与图像) · [本地模型与生成](#本地模型与生成) · [逆向与诊断](#逆向与诊断) · [3D 与工程](#3d-与工程) · [科学计算](#科学计算) · [文件与备份](#文件与备份) · [接口与编排](#接口与编排) · [前端与设计](#前端与设计)

## 如何浏览

直接访问上面的在线版本，或用现代浏览器打开根目录的 `index.html`。页面不依赖 CDN 或外部脚本，离线也能搜索和筛选。

- **近期热门**：近几个月 GitHub 关注度最高的新项目，按收藏数排序。
- **按场景找工具**：办公研究、语音视频、开发逆向、创作工程四组工作流。
- **筛选**：分类、系统、接口、资源门槛，以及「入门优先」「仅看收藏」。
- **收藏与导出**：收藏保存在浏览器本地；导出时可选择收藏、当前筛选或全部工具，先预览再下载 Markdown。

## 工具清单

下表中的工具名可直接点击，跳转到对应的官方项目或文档。

### 运行底座

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [uv + Python](https://github.com/astral-sh/uv) | CLI | Win / macOS / Linux | 轻量 | 给 Agent 提供隔离的 Python 环境，运行解析、计算和自动化脚本。 |
| [Node.js](https://nodejs.org/en/about) | CLI | Win / macOS / Linux | 轻量 | 运行 JavaScript 工具、本地服务和大量 npm 分发的 MCP 服务。 |
| [Git](https://git-scm.com/) | CLI | Win / macOS / Linux | 轻量 | 让 Agent 的代码与文本修改可追踪、可比较、可回退。 |
| [Docker Desktop](https://docs.docker.com/desktop/) | CLI / API | Win / macOS / Linux | 中等 | 在电脑上启动隔离的数据库、服务与可复现运行环境。 |
| [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/about) | CLI | Windows | 中等 | 让 Windows 使用 Linux 工具链与部分仅面向 Linux 的依赖。 |
| [cc-switch](https://github.com/farion1231/cc-switch) | GUI | Win / macOS / Linux | 轻量 | 在一个桌面应用里管理 Claude Code、Codex、OpenCode 等 Agent 的 API 供应商、MCP、技能与提示词。 |

### Agent 框架与技能

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | CLI | Win / macOS / Linux | 中等 | 插件化的 Agent 运行框架：模型、工具与界面都可替换，适合搭自己的本地 Agent 环境。 |
| [OpenClaw](https://github.com/openclaw/openclaw) | CLI / API | Win / macOS / Linux | 中等 | 强调真正执行任务的个人 AI 助手，跨系统运行，数据留在自己的设备与账号里。 |
| [Anthropic Skills](https://github.com/anthropics/skills) | Agent 技能 | Win / macOS / Linux | 轻量 | Anthropic 公开的 Agent Skills 仓库：可复用的技能定义与示例，覆盖文档、设计与开发流程。 |
| [Superpowers](https://github.com/obra/superpowers) | Agent 技能 | Win / macOS / Linux | 轻量 | Agent 技能框架与开发方法论：把头脑风暴、计划、实现与评审拆成可复用的技能。 |
| [OpenCode](https://github.com/anomalyco/opencode) | CLI / TUI | Win / macOS / Linux | 中等 | 开源编码 Agent，提供终端界面与多模型接入，可读写项目、运行命令并管理会话。 |
| [odysseus](https://github.com/odysseus-dev/odysseus) | Web / Docker | Win / macOS / Linux | 中等 | 自托管的 AI 工作台：把对话、Agent、研究、文档、邮件、笔记、日历与本地模型放在一个界面里。 |
| [security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Agent 技能 | Win / macOS / Linux | 轻量 | Cloudflare 开源的安全审计技能：让编码 Agent 按侦察、覆盖、验证、复核等阶段做漏洞审计。 |

### 浏览器与桌面

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP | Win / macOS / Linux | 中等 | 让 Agent 浏览网页、点击表单、读取结构并完成浏览器验证。 |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP | Win / macOS / Linux | 中等 | 向 Agent 暴露 Chrome 调试、网络请求和性能诊断能力。 |
| [pywinauto](https://github.com/pywinauto/pywinauto) | Python | Windows | 轻量 | 按控件与窗口属性操作 Windows 桌面软件。 |
| [AutoHotkey](https://github.com/AutoHotkey/AutoHotkey) | CLI / GUI | Windows | 轻量 | 把快捷键、窗口操作和重复输入变成可调用脚本。 |
| [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) | Python | Win / macOS / Linux | 轻量 | 为缺少接口的软件补充鼠标、键盘与截图自动化。 |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | Python / API | Win / macOS / Linux | 中等 | 把网页抓取为便于模型阅读的 Markdown 与结构化结果。 |
| [moli](https://github.com/lexmount/moli) | CLI / API | Win / macOS / Linux | 轻量 | 为 AI Agent 设计的无头浏览器：结构优先、按需取像素，Rust 编写，体积小、启动快。 |
| [browser-use](https://github.com/browser-use/browser-use) | Python / CLI | Win / macOS / Linux | 中等 | 开源浏览器 Agent 库：模型通过 Python REPL 与 Chrome DevTools 协议在真实浏览器里完成任务。 |
| [Agent-Reach](https://github.com/Panniantong/Agent-Reach) | CLI / MCP | Win / macOS / Linux | 轻量 | 给 Agent 补上读取互联网的能力：通过一个 CLI 搜索和阅读 X、Reddit、YouTube、小红书等平台。 |

### 文档与 OCR

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [Pandoc](https://pandoc.org/) | CLI | Win / macOS / Linux | 轻量 | 转换 Markdown、HTML、DOCX、EPUB 等文档格式。 |
| [MarkItDown](https://github.com/microsoft/markitdown) | CLI / Python / MCP | Win / macOS / Linux | 轻量 | 把常见文档转成 Markdown，方便 Agent 阅读和检索。 |
| [Docling](https://github.com/docling-project/docling) | CLI / Python | Win / macOS / Linux | 中等 | 解析文档结构、表格与阅读顺序，适合知识库预处理。 |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python / CLI | Win / macOS / Linux | 模型相关 | 识别图片文字，并通过相关管线解析文档版面。 |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | CLI | Win / macOS / Linux | 轻量 | 提供传统 OCR，适合清晰扫描文字的批量识别。 |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/) | CLI / Python | Win / macOS / Linux | 中等 | 给扫描 PDF 添加可搜索的文字层。 |
| [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) | Python | Win / macOS / Linux | 轻量 | 读取、渲染、拆分 PDF，提取文本和图片。 |
| [LibreOffice](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html) | CLI / API | Win / macOS / Linux | 中等 | 提供 Office 文档的本地打开、转换与排版引擎。 |
| [python-docx](https://python-docx.readthedocs.io/en/latest/) | Python | Win / macOS / Linux | 轻量 | 直接创建与修改 Word 文档的段落、表格和样式。 |
| [anydoc](https://github.com/firecrawl/anydoc) | CLI / Python / API | Win / macOS / Linux | 轻量 | Rust 编写的文档转换库，把 Word、PPT、Excel、EPUB、CSV 与 PDF 转成干净的 Markdown，毫秒级完成。 |
| [Filee](https://github.com/KnifeLemon/Filee) | CLI / GUI | Win / macOS / Linux | 轻量 | 离线文件转换器：拖拽即可在 263 种格式间转换图片、文档、音视频、电子书与压缩包，无需上传或安装 Office。 |
| [Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | Python | Win / macOS / Linux | 模型相关 | 面向长文档的一次性解析 OCR：整页、整册识别，减少分段拼接造成的上下文丢失。 |
| [MinerU](https://github.com/opendatalab/MinerU) | CLI / Python / API | Win / macOS / Linux | 模型相关 | 把复杂 PDF 与 Office 文档转成适合 LLM 的 Markdown / JSON，擅长公式、表格与多栏版面。 |
| [GenOffice](https://github.com/genspark-ai/genoffice) | GUI / CLI / MCP | Win / macOS / Linux | 中等 | 开源 AI 办公套件：在原生 docx、xlsx、pptx、PDF 与 Markdown 上编辑，内置 Agent、CLI 与 MCP。 |

### 数据与记忆

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/) | Python | Win / macOS / Linux | 轻量 | 读写 XLSX，设置单元格、公式、样式与图表。 |
| [DuckDB](https://github.com/duckdb/duckdb) | SQL / CLI / Python | Win / macOS / Linux | 轻量 | 在本机用 SQL 分析 CSV、Parquet 等数据。 |
| [SQLite](https://www.sqlite.org/cli.html) | SQL / CLI / Python | Win / macOS / Linux | 轻量 | 用单文件数据库保存 Agent 任务、结果和结构化记忆。 |
| [Qdrant](https://qdrant.tech/documentation/quickstart/) | API / Python | Win / macOS / Linux | 中等 | 提供向量检索与元数据过滤，构建个人语义资料库。 |
| [Chroma](https://github.com/chroma-core/chroma) | Python / API | Win / macOS / Linux | 中等 | 为本地 RAG 原型保存嵌入并执行语义检索。 |
| [Graphify](https://github.com/Graphify-Labs/graphify) | CLI / Agent 技能 | Win / macOS / Linux | 中等 | 把代码库、文档、SQL 结构与 PDF 变成可查询的知识图谱，为编码 Agent 提供跨会话的共享上下文。 |
| [xerj](https://github.com/xerj-org/xerj) | CLI / MCP | Win / macOS / Linux | 轻量 | 单二进制本地搜索引擎与 MCP 服务：为代码、文档、日志、JSONL/CSV 与 PDF 建立 BM25 全文索引。 |

### 语音能力

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Python | Win / macOS / Linux | 模型相关 | 把录音转成文本与时间片段，适合批量转写。 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | CLI / API | Win / macOS / Linux | 模型相关 | 提供 C/C++ 本地语音识别，适合轻量部署和 CPU 场景。 |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | CLI / Python | Win / macOS / Linux | 轻量 | 用本地语音模型把文字合成为音频。 |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | CLI / API / GUI | Win / macOS / Linux | 模型相关 | 本地优先的开源语音工作台：声音克隆、配音、口述、转写与有声书，覆盖 646 种语言，被视为 ElevenLabs 的开源替代。 |

### 音视频与图像

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [FFmpeg + ffprobe](https://github.com/FFmpeg/FFmpeg) | CLI | Win / macOS / Linux | 中等 | 转码、剪辑、混音、抽帧，并读取媒体参数。 |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | CLI / Python | Win / macOS / Linux | 轻量 | 下载可访问的网络音视频及字幕作为后续处理输入。 |
| [ImageMagick](https://imagemagick.org/command-line-processing/) | CLI | Win / macOS / Linux | 轻量 | 批量缩放、裁剪、拼图、转换图片格式。 |
| [OpenCV](https://docs.opencv.org/4.x/) | Python / C++ | Win / macOS / Linux | 中等 | 让 Agent 调用图像处理、视频分析和几何视觉算法。 |
| [OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | CLI / Agent 技能 | Win / macOS / Linux | 模型相关 | 面向 Agent 的开源视频生产系统：12 条制作流水线、100+ 工具与 700+ 技能文件，把编码 Agent 变成视频工作室。 |
| [PhotoCraft](https://github.com/storytold/photocraft) | GUI | Win / macOS / Linux | 轻量 | 纯 Rust 从零编写的开源照片编辑器，启动快、占用低，适合本地修图与调色。 |
| [Concat](https://github.com/jub0t/Concat) | MCP / GUI | Win / macOS / Linux | 中等 | 开源的 CapCut 替代品：离线优先的非线性视频剪辑器，基于 FFmpeg，并提供 MCP 接口。 |
| [Remotion](https://github.com/remotion-dev/remotion) | React / CLI / API | Win / macOS / Linux | 中等 | 用 React 以代码生成视频：组件、时间轴与渲染管线，适合批量生产字幕、片头与数据可视化视频。 |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | CLI / Agent 技能 | Win / macOS / Linux | 中等 | HeyGen 开源的 AI 视频编辑器与框架：用 HTML/CSS/JS 编排画面，确定性渲染成 MP4，专为 Agent 设计。 |

### 本地模型与生成

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | API | Win / macOS / Linux | 模型相关 | 把图像及相关生成模型组织成可复用工作流。 |
| [Ollama](https://docs.ollama.com/) | CLI / API | Win / macOS / Linux | 模型相关 | 在电脑上运行模型，为 Agent 提供本地推理与嵌入能力。 |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | CLI / API | Win / macOS / Linux | 模型相关 | 提供面向多种硬件的本地大模型推理与服务端。 |
| [colibri](https://github.com/JustVugg/colibri) | CLI / API | Win / macOS / Linux | 模型相关 | 面向超大 MoE 模型的分层推理引擎：热专家放显存、温专家放内存、冷专家流式读取 NVMe。 |
| [Strata](https://github.com/Niko1221/Strata) | API / GUI | Windows / Linux | 模型相关 | 一键在 Windows / Linux 上运行 Qwen3.8-Flash-Next，并在本机暴露 OpenAI / Anthropic 兼容接口。 |

### 逆向与诊断

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [REA](https://github.com/morluto/rea) | MCP / CLI | Win / macOS / Linux | 中等 | 把二进制、应用与运行行为分析工具接给 Agent。 |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | CLI / Python | Win / macOS / Linux | 中等 | 提供反汇编、反编译和程序分析底座。 |
| [radare2](https://rada.re/n/) | CLI / Python | Win / macOS / Linux | 中等 | 用命令行检查二进制结构、符号与反汇编。 |
| [Frida](https://frida.re/) | CLI / Python / JS | Win / macOS / Linux | 中等 | 观察运行中的程序，动态插桩与跟踪函数行为。 |
| [TShark](https://www.wireshark.org/docs/man-pages/tshark.html) | CLI | Win / macOS / Linux | 中等 | 把抓包与协议解析变成可脚本化的诊断过程。 |
| [Craft Anything](https://github.com/storytold/craft-anything) | Agent 技能 | Win / macOS / Linux | 中等 | 用 Agent 理解软件如何运作，并在弄清结构之后复刻或改造它。 |

### 3D 与工程

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [Blender](https://docs.blender.org/manual/en/5.0/advanced/command_line/arguments.html) | CLI / Python | Win / macOS / Linux | 中等 | 用脚本建模、布光、渲染和生成动画。 |
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | Python | Win / macOS / Linux | 中等 | 通过参数化建模生成可编辑的工程零件。 |
| [QGIS](https://qgis.org/) | Python / CLI | Win / macOS / Linux | 中等 | 提供地理数据处理、空间分析与地图制作能力。 |

### 科学计算

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [SymPy](https://docs.sympy.org/latest/index.html) | Python | Win / macOS / Linux | 轻量 | 执行符号运算、代数化简、微积分与方程求解。 |
| [Matplotlib](https://matplotlib.org/stable/) | Python | Win / macOS / Linux | 轻量 | 把数据转换为可复现、可导出的图表。 |

### 文件与备份

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [ripgrep](https://github.com/BurntSushi/ripgrep) | CLI | Win / macOS / Linux | 轻量 | 快速搜索本地代码、日志与文本资料。 |
| [jq](https://jqlang.org/) | CLI | Win / macOS / Linux | 轻量 | 筛选、转换和汇总 JSON，压缩 Agent 要读取的数据量。 |
| [rclone](https://rclone.org/) | CLI / API | Win / macOS / Linux | 轻量 | 在本地与云存储之间复制、同步和管理文件。 |
| [restic](https://restic.net/) | CLI | Win / macOS / Linux | 轻量 | 给工作目录建立加密、去重的快照备份。 |

### 接口与编排

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [n8n](https://docs.n8n.io/hosting/) | API | Win / macOS / Linux | 中等 | 把触发器、工具与数据处理连接成持续运行的流程。 |
| [FastMCP](https://gofastmcp.com/getting-started/welcome) | MCP / Python | Win / macOS / Linux | 轻量 | 把已有 Python 函数和服务封装成 Agent 可调用的 MCP 工具。 |
| [FastAPI](https://github.com/fastapi/fastapi) | API / Python | Win / macOS / Linux | 轻量 | 把本地脚本封装为有参数校验的 HTTP API。 |
| [Magpie](https://github.com/yetone/magpie) | API / CLI | Win / macOS / Linux | 轻量 | 把已付费的多个模型订阅池化，在一个本地端点里按可用性自动切换。 |

### 前端与设计

| 工具 | 接口 | 平台 | 资源 | 一句话说明 |
| --- | --- | --- | --- | --- |
| [Astryx](https://github.com/meta/astryx) | React / TypeScript | Win / macOS / Linux | 轻量 | Meta 开源的 Agent 友好设计系统：可完全定制的组件、令牌与主题，方便编码 Agent 直接产出统一界面。 |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | CLI / React | Win / macOS / Linux | 轻量 | 复制到项目里的组件集合：代码可改、可扩展，是编码 Agent 最熟悉的 React 组件来源之一。 |
| [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | Markdown / Agent 技能 | Win / macOS / Linux | 轻量 | 收集各大品牌设计系统的 DESIGN.md，放进项目即可让编码 Agent 生成风格匹配的界面。 |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | Agent 技能 | Win / macOS / Linux | 轻量 | 给编码 Agent 补上审美与设计判断：艺术方向、参考图与浏览器验收，减少模板化页面。 |
| [CopilotKit](https://github.com/CopilotKit/CopilotKit) | React / API | Win / macOS / Linux | 中等 | 面向 Agent 与生成式 UI 的前端栈：把聊天、工具调用和可交互组件接进 React、Angular 或移动端。 |
| [assistant-ui](https://github.com/assistant-ui/assistant-ui) | React | Win / macOS / Linux | 轻量 | 用于 AI 聊天的 React 组件库：消息流、输入框、附件与工具调用界面开箱可用。 |
| [Onlook](https://github.com/onlook-dev/onlook) | GUI / Agent | Win / macOS / Linux | 中等 | AI 优先的开源设计工具：在真实代码上可视化编辑样式与布局，并让 Agent 参与改动。 |

## 收录说明

- 收录标准：个人电脑可部署、能力边界清晰、存在可脚本化或 Agent 可连接的接口。
- 「近期热门」按 GitHub 收藏数与创建时间筛选，反映社区关注度，不代表质量排名或长期维护承诺。
- 资源标签、任务示例与工作流组合属于编辑判断，不是性能测试或厂商最低配置。
- 所有工具未逐一安装实测；软件、模型与云服务各有许可和费用条件。
- 查阅日期：2026-11-27。热门项目的收藏数取自当时的 GitHub API。

## 维护

| 文件 | 用途 |
| --- | --- |
| `data/tools.json` | 工具条目、官方链接、收藏数与热门标记 |
| `src/template.html` | 页面布局、样式与交互 |
| `scripts/build.py` | 校验数据并生成独立页面 |
| `scripts/check_links.py` | 检查全部官方链接；GitHub Actions 每周一自动运行 |
| `scripts/make_og.py` | 生成 1200×630 社交分享图（需 Pillow） |
| `assets/og.png` | 社交分享图 |
| `index.html` | 构建产物，也是分发入口 |

```sh
python scripts/build.py
python scripts/build.py --check
```

外链由 GitHub Actions 每周一检查一次。404 / 410 / 5xx 或连接失败会让工作流失败并自动开 Issue；403 / 429 视为站点反爬或限流，只记录警告。

必填字段：`name`、`cat`、`api`、`os`、`load`、`tier`、`desc`、`connect`、`note`、`task`、`url`；可选 `stars`（GitHub 收藏数）与 `hot`（是否列入近期热门）。修改数据或模板后重新构建，并一并提交 `index.html`。

## 说明

同名项目容易混淆：本清单中的 **VoiceStudio** 指 `debpalash/VoiceStudio`，**REA** 指 `morluto/rea`。本项目不隶属于所列工具的维护方，收录不代表授权转售或对兼容性的保证；第三方项目与模型继续适用各自许可。

类似目录：[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)、[awesome-ai-cli](https://github.com/vincentsch/awesome-ai-cli)、[awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)。
