import os
import sys
import webview

def set_clipboard(text):
    """
    Windows Native Clipboard integration using Python.NET (System.Windows.Forms.Clipboard).
    Guarantees reliable 100% clipboard write without browser permission blocks.
    """
    try:
        import clr
        clr.AddReference("System.Windows.Forms")
        from System.Windows.Forms import Clipboard
        Clipboard.SetText(text)
        return True
    except Exception as e:
        print("Clipboard error:", e)
        return False

class JSApi:
    def copy_text(self, text):
        return set_clipboard(text)

def get_html_content():
    base_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    
    candidates = [
        os.path.join(base_dir, "ui.html"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "ui.html"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pixel_prompt_maker_prototype.html"),
    ]
    
    for path in candidates:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
            
    return "<h1>PixelPrompt Studio UI Not Found</h1>"

def main():
    base_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    
    icon_candidates = [
        os.path.join(base_dir, "app_icon.ico"),
        os.path.join(base_dir, "assets", "app_icon.ico"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_icon.ico"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "app_icon.ico"),
    ]
    icon_path = next((p for p in icon_candidates if os.path.exists(p)), None)

    html_content = get_html_content()
    api = JSApi()

    window = webview.create_window(
        title="👾 PixelPrompt Studio - 6단계 고해상도 도트 프롬프트 빌더",
        html=html_content,
        js_api=api,
        width=1180,
        height=780,
        min_size=(960, 640),
        background_color="#09090b",
        text_select=True,
    )

    webview.start(debug=False, icon=icon_path if icon_path else None)

if __name__ == "__main__":
    main()
