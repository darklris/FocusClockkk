# 🕒 FocusClockkk - 悬浮倒计时工具

> 一款为提高工作效率设计的「悬浮式倒计时工具」，帮助你在工作中保持专注，减少拖延，提升生产力。

* 🖥 **适用于电脑端用户**：专为长时间工作和任务管理设计。
* 💤 **支持一键暂停/恢复**：让你掌控倒计时进度。
* 🔁 **倒计时结束自动续时**：无需手动重启，每次结束后直接弹窗提示。
* 🎯 **支持自定义时长或目标时间**：根据你的工作任务灵活调整。

---



## 📦 使用方式

```bash
# 方式一：指定倒计时时长（单位：分钟）
python count.py -m 25

# 方式二：指定目标时间（24小时制 HH:MM）
python count.py -t 16:00
```

## 📷 预览效果图

✅ 右下角悬浮倒计时，完美适配工作桌面，随时查看进度
![image](https://github.com/user-attachments/assets/1df124fb-0d09-46b4-8718-dc10e33bf907)


## 🧩 安装依赖

无外部依赖，直接使用 `tkinter` 库，兼容 Python 3.6+ 环境。

如需安装 `tkinter`：

```bash
# Ubuntu/Debian 系统
sudo apt install python3-tk

# macOS（一般自带）
brew install python-tk

# Windows（默认已安装）
```
