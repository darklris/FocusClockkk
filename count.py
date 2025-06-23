import tkinter as tk
from tkinter import messagebox, simpledialog
import time
from threading import Thread
import argparse
from datetime import datetime, timedelta

# 倒计时类
class CountdownApp(tk.Tk):
    def __init__(self, countdown_minutes=5):
        super().__init__()

        # 获取屏幕宽高
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # 窗口配置
        self.title("悬浮倒计时")
        self.geometry("200x80")
        self.configure(bg='black')
        self.overrideredirect(True)              # 去掉标题栏
        self.attributes('-topmost', True)        # 始终置顶
        self.attributes('-alpha', 0.85)          # 透明度

        # 窗口放在右下角
        x_pos = screen_width - 210
        y_pos = screen_height - 150
        self.geometry(f"200x80+{x_pos}+{y_pos}")

        # 时间标签
        self.time_label = tk.Label(self, font=("Helvetica", 30), bg='black', fg='white')
        self.time_label.pack(expand=True, fill="both")

        # 拖动事件
        self.bind("<B1-Motion>", self.move_window)

        # 点击暂停/恢复
        self.time_label.bind("<Button-1>", self.toggle_pause)

        self.countdown_minutes = countdown_minutes
        self.remaining_time = countdown_minutes * 60
        self.paused = False  # 添加暂停状态

        self.start_countdown_thread()

    def start_countdown_thread(self):
        self.thread = Thread(target=self.countdown)
        self.thread.daemon = True
        self.thread.start()

    def countdown(self):
        while self.remaining_time >= 0:
            if not self.paused:
                mins, secs = divmod(self.remaining_time, 60)
                time_format = f"{mins:02}:{secs:02}"
                self.time_label.config(text=time_format)

                self.update_idletasks()
                time.sleep(1)
                self.remaining_time -= 1
            else:
                time.sleep(0.1)  # 避免占用 CPU

        # 弹窗提示继续
        self.after(0, self.ask_continue)

    def toggle_pause(self, event):
        self.paused = not self.paused
        if self.paused:
            self.time_label.config(fg='gray')  # 改变颜色提示暂停
        else:
            self.time_label.config(fg='white')  # 恢复颜色

    def ask_continue(self):
        result = messagebox.askyesno("时间到！", "倒计时结束，是否继续？")
        if result:
            new_minutes = simpledialog.askinteger("新的倒计时", "请输入新的倒计时时长（分钟）：", minvalue=1, maxvalue=1440)
            if new_minutes:
                self.remaining_time = new_minutes * 60
                self.start_countdown_thread()
            else:
                self.destroy()
        else:
            self.destroy()

    def move_window(self, event):
        x, y = self.winfo_pointerxy()
        self.geometry(f"+{x - 100}+{y - 40}")


# 主函数
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="悬浮倒计时工具")
    parser.add_argument("-m", type=int, default=5, help="倒计时时长（单位：分钟）")
    parser.add_argument("-t", type=str, help="目标时间（格式：HH:MM），如 16:00")
    args = parser.parse_args()

    if args.t:
        try:
            now = datetime.now()
            target_time = datetime.strptime(args.t, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
            if target_time < now:
                target_time += timedelta(days=1)
            delta = target_time - now
            countdown_minutes = int(delta.total_seconds() // 60)
        except ValueError:
            print("时间格式错误，请使用 HH:MM 格式，例如 16:00")
            exit(1)
    else:
        countdown_minutes = args.m

    app = CountdownApp(countdown_minutes=countdown_minutes)
    app.mainloop()
