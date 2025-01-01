import tkinter as tk
import random
import time

def quick_sort_visual(data, canvas, delay, low=0, high=None):
    if high is None:
        high = len(data) - 1

    if low < high:
        # パーティションを分ける
        pivot_index = partition(data, low, high, canvas, delay)
        # 左側を再帰的にソート
        quick_sort_visual(data, canvas, delay, low, pivot_index - 1)
        # 右側を再帰的にソート
        quick_sort_visual(data, canvas, delay, pivot_index + 1, high)

def partition(data, low, high, canvas, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_bars(data, canvas, ["red" if x == i or x == j else "blue" for x in range(len(data))])
            time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    draw_bars(data, canvas, ["green" if x == i + 1 else "blue" for x in range(len(data))])
    time.sleep(delay)
    return i + 1

def draw_bars(data, canvas, colors):
    canvas.delete("all")
    c_width = canvas.winfo_width()
    c_height = canvas.winfo_height()
    bar_width = c_width / len(data)

    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = c_height - value
        x1 = (i + 1) * bar_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i], outline="")
    canvas.update()

def start_sort():
    global data
    quick_sort_visual(data, canvas, delay=0.0001)

# 線の本数を設定
num_bars = 1000  # 本数を変更すると動的に調整される
max_height = 1000  # 最大高さ

# ウィンドウのサイズを線の本数に基づいて計算
canvas_width = max(800, num_bars * 2)  # 最小幅800px、線が増えるごとに拡張
canvas_height = max_height

# メインウィンドウの設定
root = tk.Tk()
root.title("クイックソート アニメーション")
root.geometry(f"{canvas_width}x{canvas_height + 100}")  # 下部の余白を確保

# キャンバスの設定
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# ランダムな重複なしデータの生成
data = random.sample(range(1, canvas_height + 1), num_bars)
draw_bars(data, canvas, ["blue" for _ in range(len(data))])

# ボタンの設定（背景を透明風に見せる）
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
start_button = tk.Button(button_frame, text="ソート開始", command=start_sort)
start_button.pack()

# メインループ開始
root.mainloop()
