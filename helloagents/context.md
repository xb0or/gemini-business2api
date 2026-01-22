# 项目上下文

## 1. 基本信息

```yaml
名称: gemini-business2api
描述: 将 Gemini Business 转换为 OpenAI 兼容接口的服务，包含管理面板与多账号能力
类型: Web 服务
状态: 维护中
```

## 2. 技术上下文

```yaml
语言: Python, TypeScript
框架: FastAPI, Vue 3
包管理器: pip, npm
构建工具: Vite
```

### 主要依赖
| 依赖 | 版本 | 用途 |
|------|------|------|
| fastapi | 0.110.0 | 后端 API |
| uvicorn | 0.29.0 | ASGI 服务器 |
| httpx | 0.27.0 | HTTP 客户端 |
| requests | 2.32.3 | 第三方服务调用（邮箱） |
| Vue | 3 | 前端管理面板 |

## 3. 项目概述

### 核心功能
- OpenAI API 兼容的聊天/多模态接口
- 账号管理：注册/刷新/禁用与统计
- 邮箱集成：用于自动化注册与验证码获取

### 项目边界
```yaml
范围内:
  - 提供 OpenAI 兼容接口
  - 管理面板配置与账号运维
  - 集成临时邮箱服务用于自动化流程
范围外:
  - 提供通用邮箱服务平台代理（非项目主目标）
```

## 4. 开发约定

### 测试要求
```yaml
测试框架: Python unittest
测试文件位置: tests/
```

