# 任务清单: gptmail

> **@status:** completed | 2026-01-22 17:44

目录: `helloagents/archive/2026-01/202601221728_gptmail/`

---

## 任务状态符号说明

| 符号 | 状态 | 说明 |
|------|------|------|
| `[ ]` | pending | 待执行 |
| `[√]` | completed | 已完成 |
| `[X]` | failed | 执行失败 |
| `[-]` | skipped | 已跳过 |
| `[?]` | uncertain | 待确认 |

---

## 执行状态
```yaml
总任务: 12
已完成: 12
完成率: 100%
```

---

## 任务列表

### 1. 后端（Python / FastAPI）

- [√] 1.1 在 `core/gptmail_client.py` 中实现 GPTMailClient（生成邮箱、拉取邮件、提取验证码）
  - 验证: 单元测试 `tests/test_gptmail_client.py`

- [√] 1.2 在 `core/config.py` 中新增 GPTMail 配置项（base_url/api_key/verify_ssl）
  - 依赖: 1.1

- [√] 1.3 在 `core/register_service.py` 中支持 `mail_provider=gptmail`
  - 依赖: 1.1, 1.2

- [√] 1.4 在 `core/login_service.py` 中支持 `mail_provider=gptmail`（不依赖邮箱密码）
  - 依赖: 1.1, 1.2

- [√] 1.5 在 `main.py` 中扩展：
  - `POST /admin/register/start` 增加 `mail_provider`
  - `GET/PUT /admin/settings` 暴露/保存 GPTMail 配置
  - 依赖: 1.2, 1.3

### 2. 前端（Vue 管理面板）

- [√] 2.1 在 `frontend/src/views/Settings.vue` 中增加 GPTMail 配置项
  - 依赖: 1.5

- [√] 2.2 在 `frontend/src/views/Accounts.vue` 中支持选择邮箱服务（DuckMail/GPTMail）并将参数传给后端
  - 验证: 前端可构建，注册请求体包含 `mail_provider`

- [√] 2.3 在 `frontend/src/views/Accounts.vue` 中支持导入格式 `gptmail----email`

### 3. 文档与验证

- [√] 3.1 更新文档（README、免责声明、前端说明页）并补充 GPTMail 使用说明

- [√] 3.2 运行基础验证（Python 单测与语法检查）

### 4. 知识库与归档

- [√] 4.1 更新 `helloagents/modules/email_providers.md` 与 `helloagents/CHANGELOG.md`
- [√] 4.2 迁移方案包到 `helloagents/archive/YYYY-MM/` 并更新索引

---

## 执行备注

> 执行过程中的重要记录

| 任务 | 状态 | 备注 |
|------|------|------|
