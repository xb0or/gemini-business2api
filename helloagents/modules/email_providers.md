# 模块: email_providers

## 职责

- 统一项目中的邮箱验证码获取能力，为自动注册/刷新流程提供支撑。
- 封装第三方邮箱服务的调用与日志输出。

## 实现概览

```yaml
DuckMail:
  代码: core/duckmail_client.py
  用途: 注册邮箱账号、登录获取 token、拉取邮件并提取验证码
GPTMail:
  代码: core/gptmail_client.py
  用途: 通过 API Key 生成临时邮箱地址、拉取邮件并提取验证码
Microsoft:
  代码: core/microsoft_mail_client.py
  用途: 通过 OAuth refresh_token 获取 access_token，经 IMAP 拉取邮件并提取验证码
```

## 配置项

```yaml
DuckMail:
  basic.duckmail_base_url
  basic.duckmail_api_key
  basic.duckmail_verify_ssl
GPTMail:
  basic.gptmail_base_url
  basic.gptmail_api_key
  basic.gptmail_verify_ssl
```

## 与业务流程的关系

- 自动注册：core/register_service.py 选择邮箱提供商生成邮箱 → core/gemini_automation*.py 轮询验证码。
- 自动刷新：core/login_service.py 按账号配置选择邮箱提供商 → 轮询验证码完成登录刷新。

