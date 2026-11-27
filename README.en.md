# Agent Capability Atlas

**English** · [简体中文](README.md)

A curated list of practical tools for personal computers and agents: what each tool does, where it fits, its limits, and the official source. **A catalog, not an installation guide.**

**68 tools and runtimes · 13 capability areas · 14 recent trending projects**

## Browse

Open `index.html` in a modern browser. The page has no CDN or external script dependencies, so search and filters work offline.

- **Trending**: recent GitHub projects with the most stars.
- **By task**: office and research, voice and video, reverse engineering, creative work.
- **Filters**: category, operating system, interface, resource footprint, beginner-friendly, and favorites.
- **Favorites**: stored in browser localStorage and exportable as a Markdown list.

## Tools

Every tool name in the tables below links to its official project or documentation.

### Runtime foundations

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [uv + Python](https://github.com/astral-sh/uv) | CLI | Win / macOS / Linux | Light | Isolated Python environments for scripts and tooling. |
| [Node.js](https://nodejs.org/en/about) | CLI | Win / macOS / Linux | Light | Runtime for JS tools and many npm-based MCP servers. |
| [Git](https://git-scm.com/) | CLI | Win / macOS / Linux | Light | Version control for traceable, reversible changes. |
| [Docker Desktop](https://docs.docker.com/desktop/) | CLI / API | Win / macOS / Linux | Medium | Isolated databases and services with Compose. |
| [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/about) | CLI | Windows | Medium | Linux toolchain on Windows. |

### Agent frameworks & skills

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | CLI | Win / macOS / Linux | Medium | Plugin-based agent runtime. |
| [OpenClaw](https://github.com/openclaw/openclaw) | CLI / API | Win / macOS / Linux | Medium | Personal AI assistant that executes tasks across systems. |
| [Anthropic Skills](https://github.com/anthropics/skills) | Agent skill | Win / macOS / Linux | Light | Official reusable agent skill definitions. |
| [Superpowers](https://github.com/obra/superpowers) | Agent skill | Win / macOS / Linux | Light | Agent skills framework for software delivery. |

### Browser & desktop

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP | Win / macOS / Linux | Medium | Browser control for agents via accessibility trees. |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | MCP | Win / macOS / Linux | Medium | Chrome debugging, network and performance access. |
| [pywinauto](https://github.com/pywinauto/pywinauto) | Python | Windows | Light | Windows GUI automation through control handles. |
| [AutoHotkey](https://github.com/AutoHotkey/AutoHotkey) | 脚本 | Windows | Light | Windows hotkeys and desktop macros. |
| [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) | Python | Win / macOS / Linux | Light | Cross-platform mouse, keyboard and screen control. |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | Python / API | Win / macOS / Linux | Medium | Batch web crawling into LLM-ready Markdown. |
| [moli](https://github.com/lexmount/moli) | CLI / API | Win / macOS / Linux | Light | Headless browser for agents: structure first, pixels on demand. |

### Documents & OCR

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [Pandoc](https://pandoc.org/) | CLI | Win / macOS / Linux | Light | Universal converter for Markdown, Word, HTML and EPUB. |
| [MarkItDown](https://github.com/microsoft/markitdown) | CLI / Python / MCP | Win / macOS / Linux | Light | Extract text from PDF, Word, PPT and Excel. |
| [Docling](https://github.com/docling-project/docling) | CLI / Python | Win / macOS / Linux | Medium | Layout-aware document parsing with table support. |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Python / CLI | Win / macOS / Linux | Model-dependent | Strong Chinese and multilingual OCR. |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | CLI | Win / macOS / Linux | Light | Classic open-source OCR engine. |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/) | CLI / Python | Win / macOS / Linux | Medium | Add a searchable text layer to scanned PDFs. |
| [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) | Python | Win / macOS / Linux | Light | Fast PDF parsing, rendering and editing. |
| [LibreOffice](https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html) | CLI / UNO | Win / macOS / Linux | Medium | Headless Office format conversion. |
| [python-docx](https://python-docx.readthedocs.io/en/latest/) | Python | Win / macOS / Linux | Light | Read and write Word documents precisely. |
| [anydoc](https://github.com/firecrawl/anydoc) | CLI / Python / API | Win / macOS / Linux | Light | Fast Rust document-to-Markdown conversion. |
| [Filee](https://github.com/KnifeLemon/Filee) | CLI / GUI | Win / macOS / Linux | Light | Offline file converter covering 263 formats. |
| [Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | Python | Win / macOS / Linux | Model-dependent | One-shot OCR for long documents. |

### Data & memory

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/) | Python | Win / macOS / Linux | Light | Read and write Excel workbooks precisely. |
| [DuckDB](https://github.com/duckdb/duckdb) | SQL / CLI / Python | Win / macOS / Linux | Light | In-process SQL analytics over local files. |
| [SQLite](https://www.sqlite.org/cli.html) | SQL / CLI / Python | Win / macOS / Linux | Light | Embedded relational database. |
| [Qdrant](https://qdrant.tech/documentation/quickstart/) | API / Python | Win / macOS / Linux | Medium | Vector search for local knowledge bases. |
| [Chroma](https://github.com/chroma-core/chroma) | Python / API | Win / macOS / Linux | Medium | Lightweight embedding store for RAG. |

### Voice & speech

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Python | Win / macOS / Linux | Model-dependent | Fast local speech-to-text. |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | CLI / API | Win / macOS / Linux | Model-dependent | Whisper inference in portable C/C++. |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | CLI / Python | Win / macOS / Linux | Light | Lightweight local text-to-speech. |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | CLI / API / GUI | Win / macOS / Linux | Model-dependent | Local voice cloning, dubbing, dictation and transcription. |

### Audio, video & images

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [FFmpeg + ffprobe](https://github.com/FFmpeg/FFmpeg) | CLI | Win / macOS / Linux | Medium | Media conversion, trimming and inspection. |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | CLI / Python | Win / macOS / Linux | Light | Download audio and video from many sites. |
| [ImageMagick](https://imagemagick.org/command-line-processing/) | CLI | Win / macOS / Linux | Light | Batch image conversion and composition. |
| [OpenCV](https://docs.opencv.org/4.x/) | Python / C++ | Win / macOS / Linux | Medium | Image and video processing toolkit. |
| [OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | CLI / Agent skill | Win / macOS / Linux | Model-dependent | Agentic video production pipelines and tools. |
| [PhotoCraft](https://github.com/storytold/photocraft) | GUI | Win / macOS / Linux | Light | Fast Rust photo editor for local editing. |
| [Concat](https://github.com/jub0t/Concat) | MCP / GUI | Win / macOS / Linux | Medium | Open-source CapCut alternative with MCP. |

### Local models & generation

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | API | Win / macOS / Linux | Model-dependent | Node-based image generation workflows. |
| [Ollama](https://docs.ollama.com/) | CLI / API | Win / macOS / Linux | Model-dependent | Run local language models behind a simple API. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | CLI / API | Win / macOS / Linux | Model-dependent | Portable inference for local LLMs. |
| [colibri](https://github.com/JustVugg/colibri) | CLI / API | Win / macOS / Linux | Model-dependent | Hierarchical MoE inference on consumer hardware. |
| [Strata](https://github.com/Niko1221/Strata) | API / GUI | Windows / Linux | Model-dependent | One-click local model with OpenAI-compatible API. |

### Reverse engineering

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [REA](https://github.com/morluto/rea) | MCP / CLI | Win / macOS / Linux | Medium | Agent-driven reverse engineering from behavior to binaries. |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | CLI / 脚本 | Win / macOS / Linux | Medium | Software reverse engineering suite. |
| [radare2](https://rada.re/n/) | CLI / r2pipe | Win / macOS / Linux | Medium | Command-line binary analysis framework. |
| [Frida](https://frida.re/) | CLI / Python / JS | Win / macOS / Linux | Medium | Dynamic instrumentation and runtime hooking. |
| [TShark](https://www.wireshark.org/docs/man-pages/tshark.html) | CLI | Win / macOS / Linux | Medium | Command-line packet capture and analysis. |
| [Craft Anything](https://github.com/storytold/craft-anything) | Agent skill | Win / macOS / Linux | Medium | Agent workflow for understanding and rebuilding software. |

### 3D & engineering

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [Blender](https://docs.blender.org/manual/en/5.0/advanced/command_line/arguments.html) | CLI / Python | Win / macOS / Linux | Medium | Scriptable 3D modeling, rendering and video editing. |
| [FreeCAD](https://github.com/FreeCAD/FreeCAD) | Python | Win / macOS / Linux | Medium | Parametric CAD with Python scripting. |
| [QGIS](https://qgis.org/) | Python / CLI | Win / macOS / Linux | Medium | Desktop GIS with batch processing tools. |

### Scientific computing

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [SymPy](https://docs.sympy.org/latest/index.html) | Python | Win / macOS / Linux | Light | Symbolic mathematics in Python. |
| [Matplotlib](https://matplotlib.org/stable/) | Python | Win / macOS / Linux | Light | Publication-quality charts from data. |

### Files & backup

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [ripgrep](https://github.com/BurntSushi/ripgrep) | CLI | Win / macOS / Linux | Light | Fast recursive text search. |
| [jq](https://jqlang.org/) | CLI | Win / macOS / Linux | Light | Command-line JSON processing. |
| [rclone](https://rclone.org/) | CLI / API | Win / macOS / Linux | Light | Sync and mount cloud storage. |
| [restic](https://restic.net/) | CLI | Win / macOS / Linux | Light | Encrypted, deduplicated backups. |

### Interfaces & orchestration

| Tool | Interface | Platform | Footprint | What it does |
| --- | --- | --- | --- | --- |
| [n8n](https://docs.n8n.io/hosting/) | API / Webhook | Win / macOS / Linux | Medium | Visual workflow automation with AI nodes. |
| [FastMCP](https://gofastmcp.com/getting-started/welcome) | MCP / Python | Win / macOS / Linux | Light | Build MCP servers in Python. |
| [FastAPI](https://github.com/fastapi/fastapi) | API / Python | Win / macOS / Linux | Light | Typed HTTP APIs with automatic docs. |
| [Magpie](https://github.com/yetone/magpie) | API / CLI | Win / macOS / Linux | Light | Pool and fail over model subscriptions behind one endpoint. |

## Scope and caveats

- Included when deployable on a personal computer, with clear boundaries and a scriptable or agent-connectable interface.
- "Trending" is ranked by GitHub stars and creation date. It reflects community attention, not a quality ranking or a maintenance promise.
- Footprint labels, task examples and workflow groupings are editorial judgements, not benchmarks or vendor minimums.
- Tools were not installed and tested one by one. Software, models and cloud services carry their own licenses and costs.
- Catalog date: 2026-11-27. Star counts come from the GitHub API at that time.

## Maintenance

| File | Purpose |
| --- | --- |
| `data/tools.json` | Tool entries, official links, star counts and trending flags |
| `src/template.html` | Page layout, styles and interactions |
| `scripts/build.py` | Validate the catalog and render the standalone page |
| `index.html` | Build artifact and distribution entry point |

```sh
python scripts/build.py
python scripts/build.py --check
```

Required fields: `name`, `cat`, `api`, `os`, `load`, `tier`, `desc`, `connect`, `note`, `task`, `url`. Optional: `stars` (GitHub star count) and `hot` (show in the trending section). Rebuild and commit `index.html` after changing data or templates.

## Notes

**VoiceStudio** refers to `debpalash/VoiceStudio`; **REA** refers to `morluto/rea`. This project is not affiliated with any listed tool. Listing does not grant resale rights or guarantee compatibility; third-party projects and models keep their own licenses.

Similar directories: [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers), [awesome-ai-cli](https://github.com/vincentsch/awesome-ai-cli), [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills).
