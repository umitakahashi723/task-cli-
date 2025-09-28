# 任务管理命令行工具

欢迎使用任务管理命令行工具！这是一个帮助你高效管理个人任务的 CLI 工具。

## 功能特性

- 增删改查任务
- 设置任务优先级（高、中、低）
- 彩色输出，直观展示任务状态

## 安装指南

### 从源码安装
克隆项目仓库：
```bash
git clone https://github.com/umitakahashi723/task-cli-.git
cd task-cli-

安装项目依赖
pip3 install -r requirements.txt

使用预编译的轮子安装
直接安装预编译的  .whl  文件：
pip3 install https://github.com/umitakahashi723/task-cli-/releases/download/v1.0.0/task_cli_umitakahashi723-1.0.0-py3-none-any.whl

使用方法

添加任务
task add "？？？" -p high/medium

列出所有任务
task list

标记任务完成
task done 1

删除任务
task delete 2

贡献指南
欢迎贡献代码！请先阅读 CONTRIBUTING.md 了解如何参与项目。
联系方式
如有任何问题或建议，请通过 GitHub Issues 与我们联系。

