# mid

import tkinter as tk

# 메인 윈도우 생성
window = tk.Tk()

# 윈도우 제목 설정
window.title("메모장")

# 윈도우 크기 설정
window.geometry("600x400")

# 윈도우가 화면에 표시되도록 유지
window.mainloop()

--- a/notepad.py
+++ b/notepad.py
@@ -1,14 +1,56 @@
 import tkinter as tk
+from tkinter import filedialog
+
+# 새 파일
+def new_file():
+    text_area.delete(1.0, tk.END)
+
+# 파일 열기
+def open_file():
+    file_path = filedialog.askopenfilename(filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
+    if file_path:
+        with open(file_path, "r", encoding="utf-8") as file:
+            text_area.delete(1.0, tk.END)
+            text_area.insert(tk.END, file.read())
+
+# 파일 저장
+def save_file():
+    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
+    if file_path:
+        with open(file_path, "w", encoding="utf-8") as file:
+            file.write(text_area.get(1.0, tk.END))
 
 # 메인 윈도우 생성
 window = tk.Tk()
 
 # 윈도우 제목 설정
-window.title("메모장")
+window.title("Gemini 메모장")
 
 # 윈도우 크기 설정
 window.geometry("600x400")
 
+# 메뉴바 생성
+menu_bar = tk.Menu(window)
+
+# 파일 메뉴 생성
+file_menu = tk.Menu(menu_bar, tearoff=0)
+file_menu.add_command(label="새 파일", command=new_file)
+file_menu.add_command(label="열기", command=open_file)
+file_menu.add_command(label="저장", command=save_file)
+file_menu.add_separator()
+file_menu.add_command(label="종료", command=window.quit)
+
+# 메뉴바에 파일 메뉴 추가
+menu_bar.add_cascade(label="파일", menu=file_menu)
+
+# 윈도우에 메뉴바 설정
+window.config(menu=menu_bar)
+
+# 텍스트 입력 영역 생성
+text_area = tk.Text(window, wrap=tk.WORD)
+text_area.pack(expand=True, fill='both')
+
+
 # 윈도우가 화면에 표시되도록 유지
 window.mainloop()
