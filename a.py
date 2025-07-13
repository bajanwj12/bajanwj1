from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# 强制屏幕居中（适应手机分辨率）
Window.size = (300, 500)  # 模拟手机竖屏尺寸

class MobileApp(App):
    def build(self):
        label = Label(
            text="1234",
            font_size=40,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(None, None)
        )
        return label

if __name__ == "__main__":
    MobileApp().run()