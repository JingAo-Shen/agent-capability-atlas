# Agent Capability Atlas · Agent 工具图谱

一份面向个人电脑与 Agent 的实用工具清单：记录好用的工具、它们适合做什么、边界在哪里，以及官方来源。

目前收录 **68 项工具与运行环境、13 个能力领域**，其中包含 14 个近几个月在 GitHub 上受到关注的新项目。这里只做收录与整理，不提供安装教程。

## 浏览方式

直接用现代浏览器打开根目录的 **index.html**。页面包含样式、数据与脚本，无 CDN 依赖，离线也能搜索与筛选。

- **近期热门**：按 GitHub 收藏数排列的新项目，例如 OpenMontage、VoiceStudio、DeepSeek Harness、colibri、moli。
- **按用途浏览**：13 个分类，从运行底座、文档解析、语音、音视频到本地模型与逆向分析。
- **筛选与收藏**：按系统、接口、资源门槛筛选；收藏保存在浏览器本地，可导出 Markdown 清单。
- **条目内容**：能力描述、接入方式、给 Agent 的任务示例、使用边界与官方链接。

## 收录范围

| 分类 | 例子 |
| --- | --- |
| 运行底座 | uv、Node.js、Git、Docker、WSL |
| Agent 框架与技能 | DeepSeek Harness、OpenClaw、Anthropic Skills、Superpowers |
| 浏览器与桌面 | Playwright MCP、Chrome DevTools MCP、Crawl4AI、moli |
| 文档与 OCR | MarkItDown、Docling、Pandoc、anydoc、Filee、PaddleOCR |
| 数据与记忆 | DuckDB、SQLite、Qdrant、Chroma |
| 语音能力 | VoiceStudio、faster-whisper、whisper.cpp、Piper |
| 音视频与图像 | FFmpeg、yt-dlp、OpenMontage、Concat、PhotoCraft |
| 本地模型与生成 | Ollama、llama.cpp、ComfyUI、colibri、Strata |
| 逆向与诊断 | REA、Ghidra、radare2、Frida、TShark |
| 3D 与工程 | Blender、FreeCAD、QGIS |
| 科学计算 | SymPy、Matplotlib |
| 文件与备份 | ripgrep、jq、rclone、restic |
| 接口与编排 | n8n、FastMCP、FastAPI、Magpie |

收录标准：个人电脑可部署、能力边界清晰、存在可脚本化或 Agent 可连接的接口；优先引用项目官方仓库与官方文档。

## 维护

页面是构建产物，数据与模板分离：

| 文件 | 用途 |
| --- | --- |
| `data/tools.json` | 工具条目与官方链接 |
| `src/template.html` | 页面布局、样式与交互 |
| `scripts/build.py` | 校验数据并生成独立页面 |
| `index.html` | 构建产物，也是分发入口 |

仅依赖 Python 3 标准库：

```sh
python scripts/build.py
python scripts/build.py --check
```

条目字段：`name`、`cat`、`api`、`os`、`load`、`tier`、`desc`、`connect`、`note`、`task`、`url`，可选 `stars`（GitHub 收藏数）与 `hot`（是否列入近期热门）。修改数据或模板后重新构建，并一并提交 `index.html`。

## 说明

资料查阅日期：2026-11-27。热门项目的收藏数取自当时的 GitHub API，之后会变化。

「近期热门」反映社区关注度，不代表质量排名或长期维护承诺。资源标签、推荐组合与任务示例属于编辑判断，不是性能测试或厂商最低配置。所有收录工具并未逐一安装实测；模型、软件与云服务各有许可及费用条件。

本项目不隶属于所列工具的维护方。第三方项目与模型继续适用各自许可；收录不代表授权转售或对兼容性的保证。
