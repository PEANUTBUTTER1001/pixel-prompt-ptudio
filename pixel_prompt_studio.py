import os
import sys
import tkinter as tk
import customtkinter as ctk

# Helper for PyInstaller resource loading
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

PRESETS = {
    "gersang": {
        "style_idx": 0,
        "custom_style": "",
        "char_type": "cute chibi anime girl",
        "hair_style": "brown straight bangs and bob haircut",
        "eyes_detail": "large sparkling brown eyes",
        "expression": "soft peach blush, cute happy open smile showing teeth",
        "headwear": "red Santa hat tilted with fluffy white brim",
        "outfit": "red Santa outfit with fluffy white fur collar",
        "props": "visibly holding a glowing golden star wand on the bottom left, sparkling stars",
        "framing": "Close-up square avatar icon, face nicely filling the 1:1 frame",
        "background": "clean solid dark vignette background, clean edges for cutout",
        "neg_text": True,
        "neg_watermark": True,
        "neg_blur": True,
        "opt_outlines": True,
        "opt_vibrant": True,
        "neg_photo": True,
    },
    "wizardCat": {
        "style_idx": 0,
        "custom_style": "magical glowing particles",
        "char_type": "cute fantasy cat creature",
        "hair_style": "fluffy white calico fur with soft markings",
        "eyes_detail": "large round emerald green eyes full of curiosity",
        "expression": "mysterious cute smile with tiny fangs",
        "headwear": "pointed navy blue wizard hat adorned with miniature golden stars",
        "outfit": "navy blue arcane robe with gold trim and ribbon tie",
        "props": "holding a floating crystal glass orb wand, soft magical glow",
        "framing": "Close-up square avatar icon, face nicely filling the 1:1 frame",
        "background": "clean solid dark vignette background, clean edges for cutout",
        "neg_text": True,
        "neg_watermark": True,
        "neg_blur": True,
        "opt_outlines": True,
        "opt_vibrant": True,
        "neg_photo": True,
    },
    "cyberpunk": {
        "style_idx": 2,
        "custom_style": "cyberpunk neon glow highlights",
        "char_type": "brave young knight",
        "hair_style": "neon cyan and black asymmetrical spiky haircut",
        "eyes_detail": "glowing bionic amber eyes with cyber visor hud",
        "expression": "confident smirk, subtle cybernetic cheek line",
        "headwear": "sleek carbon fiber tech visor headset",
        "outfit": "matte black high-tech combat jacket with neon piping",
        "props": "holding a micro energy dagger emitting turquoise light",
        "framing": "Bust portrait avatar, perfectly centered in square frame",
        "background": "solid plain background, high contrast, clean sharp borders",
        "neg_text": True,
        "neg_watermark": True,
        "neg_blur": True,
        "opt_outlines": True,
        "opt_vibrant": True,
        "neg_photo": True,
    },
}

STYLE_OPTIONS = [
    "High-resolution pixel art, 16-bit / 32-bit retro RPG style, crisp detailed dot design",
    "Classic 16-bit SNES pixel art, nostalgic arcade sprite style, clean dithering",
    "High-definition pixel art, modern indie game aesthetic, vibrant pixel shading",
]

CHAR_TYPES = [
    "cute chibi anime girl",
    "cute chibi anime boy",
    "cute fantasy cat creature",
    "brave young knight",
    "mystic wizard pupil",
]

FRAMING_OPTIONS = [
    "Close-up square avatar icon, face nicely filling the 1:1 frame",
    "Bust portrait avatar, perfectly centered in square frame",
    "Full-body miniature pixel character sprite, centered",
]

BG_OPTIONS = [
    "clean solid dark vignette background, clean edges for cutout",
    "solid plain background, high contrast, clean sharp borders",
    "subtle pastel geometric grid background",
]


class PixelPromptStudio(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PixelPrompt Studio - 도트 아이콘 프롬프트 메이커")
        self.geometry("1100x740")
        self.minsize(980, 650)

        # Set Icon if available
        icon_path = resource_path("app_icon.ico")
        if not os.path.exists(icon_path):
            alt_icon = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "app_icon", "app_icon.ico")
            if os.path.exists(alt_icon):
                icon_path = alt_icon

        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        # Variables
        self.style_var = tk.IntVar(value=0)
        self.custom_style_var = tk.StringVar()
        self.char_type_var = tk.StringVar(value=CHAR_TYPES[0])
        self.hair_style_var = tk.StringVar(value="brown straight bangs and bob haircut")
        self.eyes_detail_var = tk.StringVar(value="large sparkling brown eyes")
        self.expression_var = tk.StringVar(value="soft peach blush, cute happy open smile showing teeth")
        self.headwear_var = tk.StringVar(value="red Santa hat tilted with fluffy white brim")
        self.outfit_var = tk.StringVar(value="red Santa outfit with fluffy white fur collar")
        self.props_var = tk.StringVar(value="visibly holding a glowing golden star wand on the bottom left, sparkling stars")
        self.framing_var = tk.StringVar(value=FRAMING_OPTIONS[0])
        self.bg_var = tk.StringVar(value=BG_OPTIONS[0])

        self.neg_text_var = tk.BooleanVar(value=True)
        self.neg_watermark_var = tk.BooleanVar(value=True)
        self.neg_blur_var = tk.BooleanVar(value=True)
        self.opt_outlines_var = tk.BooleanVar(value=True)
        self.opt_vibrant_var = tk.BooleanVar(value=True)
        self.neg_photo_var = tk.BooleanVar(value=True)

        # Bind tracing for live update
        for v in [
            self.style_var,
            self.custom_style_var,
            self.char_type_var,
            self.hair_style_var,
            self.eyes_detail_var,
            self.expression_var,
            self.headwear_var,
            self.outfit_var,
            self.props_var,
            self.framing_var,
            self.bg_var,
            self.neg_text_var,
            self.neg_watermark_var,
            self.neg_blur_var,
            self.opt_outlines_var,
            self.opt_vibrant_var,
            self.neg_photo_var,
        ]:
            v.trace_add("write", lambda *_: self.update_prompt())

        self.setup_ui()
        self.update_prompt()

    def setup_ui(self):
        # Header Frame
        header = ctk.CTkFrame(self, height=54, corner_radius=0, fg_color="#18181b")
        header.pack(fill="x", side="top")

        title_lbl = ctk.CTkLabel(
            header,
            text="👾 PixelPrompt Studio",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#f43f5e",
        )
        title_lbl.pack(side="left", padx=(18, 8), pady=12)

        subtitle_lbl = ctk.CTkLabel(
            header,
            text="| 5단계 구조 기반 고해상도 픽셀 아트 프롬프트 빌더",
            font=ctk.CTkFont(size=13),
            text_color="#a1a1aa",
        )
        subtitle_lbl.pack(side="left", pady=12)

        # Main Split Frame
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=16, pady=12)

        # Left: Scrollable 5-Step Option Selectors (60% width)
        left_frame = ctk.CTkScrollableFrame(main_container, fg_color="#121215", corner_radius=12)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Right: Output & Controls (40% width)
        right_frame = ctk.CTkFrame(main_container, width=420, fg_color="#18181b", corner_radius=12)
        right_frame.pack(side="right", fill="both", expand=False)
        right_frame.pack_propagate(False)

        # Build Left Options
        self.build_step1(left_frame)
        self.build_step2(left_frame)
        self.build_step3(left_frame)
        self.build_step4(left_frame)
        self.build_step5(left_frame)

        # Build Right Output
        self.build_right_panel(right_frame)

    # STEP 1
    def build_step1(self, parent):
        card = ctk.CTkFrame(parent, fg_color="#1e1e24", corner_radius=10)
        card.pack(fill="x", pady=(0, 10), padx=4, ipady=4)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(10, 4))
        ctk.CTkLabel(
            header,
            text="1",
            width=22,
            height=22,
            corner_radius=11,
            fg_color="#f43f5e",
            text_color="white",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(
            header,
            text="기본 스타일 & 게임 세대 (Style & Era)",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(side="left")

        styles = [
            "16/32비트 명작 RPG (고해상도 섬세한 도트 - 추천)",
            "16비트 슈퍼패미컴 (클래식 아케이드 룩)",
            "모던 인디 HD 도트 (선명하고 화려한 색감)",
        ]
        for idx, text in enumerate(styles):
            rb = ctk.CTkRadioButton(
                card,
                text=text,
                variable=self.style_var,
                value=idx,
                font=ctk.CTkFont(size=12),
                radiobutton_height=18,
                radiobutton_width=18,
            )
            rb.pack(anchor="w", padx=20, pady=3)

        c_frame = ctk.CTkFrame(card, fg_color="transparent")
        c_frame.pack(fill="x", padx=18, pady=(6, 8))
        ctk.CTkLabel(c_frame, text="추가 스타일:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").pack(side="left", padx=(0, 6))
        ctk.CTkEntry(
            c_frame,
            textvariable=self.custom_style_var,
            placeholder_text="예: pastel color palette, soft lighting",
            font=ctk.CTkFont(size=12),
        ).pack(side="left", fill="x", expand=True)

    # STEP 2
    def build_step2(self, parent):
        card = ctk.CTkFrame(parent, fg_color="#1e1e24", corner_radius=10)
        card.pack(fill="x", pady=(0, 10), padx=4, ipady=4)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(10, 4))
        ctk.CTkLabel(
            header,
            text="2",
            width=22,
            height=22,
            corner_radius=11,
            fg_color="#f59e0b",
            text_color="black",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(
            header,
            text="캐릭터 외형 & 표정 (Character & Face)",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(side="left")

        grid = ctk.CTkFrame(card, fg_color="transparent")
        grid.pack(fill="x", padx=14, pady=4)
        grid.columnconfigure((0, 1), weight=1)

        # Char Type & Hair
        ctk.CTkLabel(grid, text="캐릭터 유형:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=0, column=0, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkComboBox(grid, values=CHAR_TYPES, variable=self.char_type_var, font=ctk.CTkFont(size=12)).grid(row=1, column=0, sticky="ew", padx=4, pady=(0, 6))

        ctk.CTkLabel(grid, text="헤어 스타일 / 털:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=0, column=1, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkEntry(grid, textvariable=self.hair_style_var, font=ctk.CTkFont(size=12)).grid(row=1, column=1, sticky="ew", padx=4, pady=(0, 6))

        # Eyes & Expression
        ctk.CTkLabel(grid, text="눈동자 & 눈빛:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=2, column=0, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkEntry(grid, textvariable=self.eyes_detail_var, font=ctk.CTkFont(size=12)).grid(row=3, column=0, sticky="ew", padx=4, pady=(0, 6))

        ctk.CTkLabel(grid, text="표정 & 볼터치:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=2, column=1, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkEntry(grid, textvariable=self.expression_var, font=ctk.CTkFont(size=12)).grid(row=3, column=1, sticky="ew", padx=4, pady=(0, 6))

    # STEP 3
    def build_step3(self, parent):
        card = ctk.CTkFrame(parent, fg_color="#1e1e24", corner_radius=10)
        card.pack(fill="x", pady=(0, 10), padx=4, ipady=4)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(10, 4))
        ctk.CTkLabel(
            header,
            text="3",
            width=22,
            height=22,
            corner_radius=11,
            fg_color="#10b981",
            text_color="black",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(
            header,
            text="의상, 모자 & 소품 (Outfit & Props)",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(side="left")

        grid = ctk.CTkFrame(card, fg_color="transparent")
        grid.pack(fill="x", padx=14, pady=4)
        grid.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(grid, text="모자 / 악세사리:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=0, column=0, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkEntry(grid, textvariable=self.headwear_var, font=ctk.CTkFont(size=12)).grid(row=1, column=0, sticky="ew", padx=4, pady=(0, 6))

        ctk.CTkLabel(grid, text="착용 의상 / 옷깃:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=0, column=1, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkEntry(grid, textvariable=self.outfit_var, font=ctk.CTkFont(size=12)).grid(row=1, column=1, sticky="ew", padx=4, pady=(0, 6))

        ctk.CTkLabel(card, text="손에 든 소품 / 지팡이 (Props):", font=ctk.CTkFont(size=12), text_color="#a1a1aa").pack(anchor="w", padx=18, pady=(2, 0))
        ctk.CTkEntry(card, textvariable=self.props_var, font=ctk.CTkFont(size=12)).pack(fill="x", padx=18, pady=(0, 8))

    # STEP 4
    def build_step4(self, parent):
        card = ctk.CTkFrame(parent, fg_color="#1e1e24", corner_radius=10)
        card.pack(fill="x", pady=(0, 10), padx=4, ipady=4)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(10, 4))
        ctk.CTkLabel(
            header,
            text="4",
            width=22,
            height=22,
            corner_radius=11,
            fg_color="#06b6d4",
            text_color="black",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(
            header,
            text="구도 & 배경 (Composition & Background)",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(side="left")

        grid = ctk.CTkFrame(card, fg_color="transparent")
        grid.pack(fill="x", padx=14, pady=4)
        grid.columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(grid, text="화면 구도:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=0, column=0, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkComboBox(grid, values=FRAMING_OPTIONS, variable=self.framing_var, font=ctk.CTkFont(size=12)).grid(row=1, column=0, sticky="ew", padx=4, pady=(0, 6))

        ctk.CTkLabel(grid, text="배경 스타일:", font=ctk.CTkFont(size=12), text_color="#a1a1aa").grid(row=0, column=1, sticky="w", padx=4, pady=(2, 0))
        ctk.CTkComboBox(grid, values=BG_OPTIONS, variable=self.bg_var, font=ctk.CTkFont(size=12)).grid(row=1, column=1, sticky="ew", padx=4, pady=(0, 6))

    # STEP 5
    def build_step5(self, parent):
        card = ctk.CTkFrame(parent, fg_color="#1e1e24", corner_radius=10)
        card.pack(fill="x", pady=(0, 10), padx=4, ipady=4)

        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=12, pady=(10, 4))
        ctk.CTkLabel(
            header,
            text="5",
            width=22,
            height=22,
            corner_radius=11,
            fg_color="#a855f7",
            text_color="white",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).pack(side="left", padx=(0, 8))
        ctk.CTkLabel(
            header,
            text="금지 요소 & 품질 튜닝 (Negative & Quality)",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(side="left")

        c_box = ctk.CTkFrame(card, fg_color="transparent")
        c_box.pack(fill="x", padx=14, pady=4)

        ctk.CTkCheckBox(c_box, text="텍스트/글자 제거", variable=self.neg_text_var, font=ctk.CTkFont(size=12)).grid(row=0, column=0, sticky="w", padx=8, pady=4)
        ctk.CTkCheckBox(c_box, text="워터마크 제거", variable=self.neg_watermark_var, font=ctk.CTkFont(size=12)).grid(row=0, column=1, sticky="w", padx=8, pady=4)
        ctk.CTkCheckBox(c_box, text="블러/흐림 방지", variable=self.neg_blur_var, font=ctk.CTkFont(size=12)).grid(row=0, column=2, sticky="w", padx=8, pady=4)

        ctk.CTkCheckBox(c_box, text="칼같은 픽셀 윤곽선", variable=self.opt_outlines_var, font=ctk.CTkFont(size=12)).grid(row=1, column=0, sticky="w", padx=8, pady=4)
        ctk.CTkCheckBox(c_box, text="선명한 색감", variable=self.opt_vibrant_var, font=ctk.CTkFont(size=12)).grid(row=1, column=1, sticky="w", padx=8, pady=4)
        ctk.CTkCheckBox(c_box, text="실사/3D 렌더링 배제", variable=self.neg_photo_var, font=ctk.CTkFont(size=12)).grid(row=1, column=2, sticky="w", padx=8, pady=4)

    # RIGHT PANEL
    def build_right_panel(self, parent):
        # Preset Buttons
        preset_frame = ctk.CTkFrame(parent, fg_color="transparent")
        preset_frame.pack(fill="x", padx=14, pady=(12, 6))

        ctk.CTkLabel(preset_frame, text="⚡ 빠른 프리셋:", font=ctk.CTkFont(size=12, weight="bold"), text_color="#a1a1aa").pack(anchor="w", pady=(0, 4))
        btn_bar = ctk.CTkFrame(preset_frame, fg_color="transparent")
        btn_bar.pack(fill="x")

        ctk.CTkButton(
            btn_bar,
            text="🎅 마음이",
            width=90,
            height=28,
            fg_color="#e11d48",
            hover_color="#be123c",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self.load_preset("gersang"),
        ).pack(side="left", padx=(0, 5))

        ctk.CTkButton(
            btn_bar,
            text="🧙‍♂️ 냥마법사",
            width=90,
            height=28,
            fg_color="#7c3aed",
            hover_color="#6d28d9",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self.load_preset("wizardCat"),
        ).pack(side="left", padx=(0, 5))

        ctk.CTkButton(
            btn_bar,
            text="⚡ 사이버",
            width=90,
            height=28,
            fg_color="#0891b2",
            hover_color="#0e7490",
            font=ctk.CTkFont(size=11, weight="bold"),
            command=lambda: self.load_preset("cyberpunk"),
        ).pack(side="left")

        # Output Box
        out_header = ctk.CTkFrame(parent, fg_color="transparent")
        out_header.pack(fill="x", padx=14, pady=(8, 4))
        ctk.CTkLabel(
            out_header,
            text="📝 최종 조합 프롬프트",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(side="left")
        self.word_count_lbl = ctk.CTkLabel(
            out_header,
            text="단어 수: 0",
            font=ctk.CTkFont(size=11),
            text_color="#71717a",
        )
        self.word_count_lbl.pack(side="right")

        self.prompt_text = ctk.CTkTextbox(
            parent,
            font=ctk.CTkFont(family="Consolas", size=12),
            wrap="word",
            fg_color="#0f0f12",
            border_width=1,
            border_color="#27272a",
        )
        self.prompt_text.pack(fill="both", expand=True, padx=14, pady=(0, 10))

        # Copy & Reset Buttons
        action_frame = ctk.CTkFrame(parent, fg_color="transparent")
        action_frame.pack(fill="x", padx=14, pady=(0, 8))

        self.copy_btn = ctk.CTkButton(
            action_frame,
            text="📋 프롬프트 원클릭 복사",
            height=38,
            fg_color="#f43f5e",
            hover_color="#e11d48",
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.copy_prompt,
        )
        self.copy_btn.pack(side="left", fill="x", expand=True, padx=(0, 6))

        ctk.CTkButton(
            action_frame,
            text="초기화",
            width=70,
            height=38,
            fg_color="#27272a",
            hover_color="#3f3f46",
            font=ctk.CTkFont(size=12),
            command=lambda: self.load_preset("gersang"),
        ).pack(side="right")

        # Negative Prompt Panel
        neg_frame = ctk.CTkFrame(parent, fg_color="#141417", corner_radius=8)
        neg_frame.pack(fill="x", padx=14, pady=(0, 12))

        neg_header = ctk.CTkFrame(neg_frame, fg_color="transparent")
        neg_header.pack(fill="x", padx=8, pady=(6, 2))
        ctk.CTkLabel(
            neg_header,
            text="부정 프롬프트 (Negative Prompt)",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#a1a1aa",
        ).pack(side="left")
        ctk.CTkButton(
            neg_header,
            text="복사",
            width=40,
            height=20,
            font=ctk.CTkFont(size=10),
            fg_color="#3f3f46",
            hover_color="#52525b",
            command=self.copy_negative,
        ).pack(side="right")

        self.neg_label = ctk.CTkLabel(
            neg_frame,
            text="",
            font=ctk.CTkFont(family="Consolas", size=10),
            text_color="#71717a",
            wraplength=380,
            justify="left",
        )
        self.neg_label.pack(fill="x", padx=8, pady=(0, 8))

    def update_prompt(self):
        # 1. Style
        s_idx = self.style_var.get()
        style_base = STYLE_OPTIONS[s_idx] if 0 <= s_idx < len(STYLE_OPTIONS) else STYLE_OPTIONS[0]
        c_style = self.custom_style_var.get().strip()

        parts = []

        # Part 1: Style
        combined_style = style_base
        if c_style:
            combined_style += f", {c_style}"
        if self.opt_outlines_var.get():
            combined_style += ", crisp pixel shading, sharp outlines"
        if self.opt_vibrant_var.get():
            combined_style += ", vibrant colors"
        parts.append(combined_style)

        # Part 2: Character
        char_desc = [self.char_type_var.get()]
        if self.hair_style_var.get().strip():
            char_desc.append(f"with {self.hair_style_var.get().strip()}")
        if self.eyes_detail_var.get().strip():
            char_desc.append(self.eyes_detail_var.get().strip())
        if self.expression_var.get().strip():
            char_desc.append(self.expression_var.get().strip())
        parts.append(", ".join(char_desc))

        # Part 3: Outfit & Props
        outfit_desc = []
        if self.headwear_var.get().strip():
            outfit_desc.append(f"wearing {self.headwear_var.get().strip()}")
        if self.outfit_var.get().strip():
            outfit_desc.append(self.outfit_var.get().strip())
        if self.props_var.get().strip():
            outfit_desc.append(self.props_var.get().strip())
        if outfit_desc:
            parts.append(", ".join(outfit_desc))

        # Part 4: Framing & BG
        parts.append(f"{self.framing_var.get()}, {self.bg_var.get()}")

        # Part 5: Negatives in prompt
        neg_main = []
        if self.neg_text_var.get():
            neg_main.append("no text")
        if self.neg_watermark_var.get():
            neg_main.append("no watermark")
        if neg_main:
            parts.append(", ".join(neg_main))

        full_prompt = ". ".join(parts) + "."

        self.prompt_text.delete("1.0", "end")
        self.prompt_text.insert("1.0", full_prompt)

        words = len(full_prompt.split())
        self.word_count_lbl.configure(text=f"단어 수: {words}")

        # Dedicated Negative
        neg_list = []
        if self.neg_text_var.get():
            neg_list.extend(["text", "letters", "subtitles", "alphabet"])
        if self.neg_watermark_var.get():
            neg_list.extend(["watermark", "signature", "logo", "username"])
        if self.neg_blur_var.get():
            neg_list.extend(["blur", "anti-aliasing", "soft gradients", "unfocused"])
        if self.neg_photo_var.get():
            neg_list.extend(["realistic photograph", "3d render", "clay", "smooth vector"])

        self.neg_label.configure(text=", ".join(neg_list))

    def load_preset(self, key):
        p = PRESETS.get(key)
        if not p:
            return
        self.style_var.set(p["style_idx"])
        self.custom_style_var.set(p["custom_style"])
        self.char_type_var.set(p["char_type"])
        self.hair_style_var.set(p["hair_style"])
        self.eyes_detail_var.set(p["eyes_detail"])
        self.expression_var.set(p["expression"])
        self.headwear_var.set(p["headwear"])
        self.outfit_var.set(p["outfit"])
        self.props_var.set(p["props"])
        self.framing_var.set(p["framing"])
        self.bg_var.set(p["background"])

        self.neg_text_var.set(p["neg_text"])
        self.neg_watermark_var.set(p["neg_watermark"])
        self.neg_blur_var.set(p["neg_blur"])
        self.opt_outlines_var.set(p["opt_outlines"])
        self.opt_vibrant_var.set(p["opt_vibrant"])
        self.neg_photo_var.set(p["neg_photo"])

    def copy_prompt(self):
        text = self.prompt_text.get("1.0", "end").strip()
        self.clipboard_clear()
        self.clipboard_append(text)
        orig = self.copy_btn.cget("text")
        self.copy_btn.configure(text="✅ 복사 완료!")
        self.after(1500, lambda: self.copy_btn.configure(text=orig))

    def copy_negative(self):
        text = self.neg_label.cget("text").strip()
        self.clipboard_clear()
        self.clipboard_append(text)


if __name__ == "__main__":
    app = PixelPromptStudio()
    app.mainloop()
