# 智能物联网实验室官网

前后端分离的实验室官方网站，用于展示研究方向、团队成员、论文成果和新闻动态。

## 技术栈

- **前端**: React + Vite + TypeScript
- **后端**: Python + Flask
- **数据库**: SQLite
- **Python 环境管理**: uv

## 项目结构

```
demo02/
├── frontend/                # 前端项目
│   ├── src/
│   │   ├── components/      # 组件
│   │   ├── hooks/           # 自定义 hooks
│   │   ├── types/           # TypeScript 类型定义
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── index.html
│   ├── vite.config.ts
│   └── package.json
├── backend/                 # 后端项目
│   ├── app.py               # Flask 应用入口
│   ├── init_db.py           # 数据库初始化脚本
│   ├── lab_homepage.db      # SQLite 数据库文件
│   ├── pyproject.toml       # Python 项目配置
│   └── uv.lock              # 依赖锁定文件
├── .gitignore
└── README.md
```

## 快速开始

### 环境要求

- Python 3.10+
- Node.js 18+
- [uv](https://github.com/astral-sh/uv)（Python 包管理器）

### 1. 安装后端依赖

```bash
cd backend
uv sync
```

### 2. 初始化数据库

```bash
cd backend
uv run python init_db.py
```

执行后会创建 `lab_homepage.db` 文件，并插入演示数据。

### 3. 启动后端

```bash
cd backend
uv run python app.py
```

后端运行在 `http://localhost:3001`。

### 4. 安装前端依赖并启动

```bash
cd frontend
npm install
npm run dev
```

前端运行在 `http://localhost:5173`，API 请求自动代理到后端 3001 端口。

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/members | 获取团队成员列表 |
| GET | /api/papers | 获取论文成果列表 |
| GET | /api/news | 获取新闻动态列表 |
| GET | /api/research | 获取研究方向列表 |
| POST | /api/news | 新增新闻动态 |
| POST | /api/members | 新增团队成员 |

## 数据库表结构

### members（团队成员）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| name | TEXT | 姓名 |
| role | TEXT | 角色/职位 |
| avatar | TEXT | 头像 URL |
| bio | TEXT | 个人简介 |
| email | TEXT | 邮箱 |

### papers（论文成果）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| title | TEXT | 论文标题 |
| authors | TEXT | 作者列表 |
| journal | TEXT | 期刊/会议名称 |
| year | INTEGER | 发表年份 |
| abstract | TEXT | 摘要 |
| doi | TEXT | DOI 编号 |

### news（新闻动态）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| title | TEXT | 标题 |
| date | TEXT | 日期 |
| summary | TEXT | 摘要 |
| content | TEXT | 正文内容 |

### research（研究方向）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| name | TEXT | 方向名称 |
| description | TEXT | 方向描述 |
| icon | TEXT | 图标（emoji） |
