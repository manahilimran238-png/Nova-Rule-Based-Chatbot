import tkinter as tk

from chatbot import detect_intent, get_response


class NovaGUI:
    def __init__(self, root):
        self.root = root

        # ==========================================
        # COLOR SCHEME
        # ==========================================
        self.bg_main = "#F8FAFB"          # Very light background
        self.bg_secondary = "#FFFFFF"     # White for chat area
        self.bg_input = "#F0F3F7"         # Light gray-blue for input
        self.color_primary = "#4A90E2"    # Vibrant blue
        self.color_primary_light = "#E8F0FE"  # Light blue
        self.color_nova = "#E8F0FE"       # Nova bubble background
        self.color_user = "#4A90E2"       # User bubble background
        self.text_dark = "#2C3E50"        # Dark text
        self.text_light = "#FFFFFF"       # Light text
        self.text_secondary = "#7F8C9A"   # Secondary text
        self.accent = "#6C63FF"           # Purple accent

        # ==========================================
        # WINDOW
        # ==========================================
        self.root.title("Nova - Rule-Based AI Assistant")
        self.root.geometry("760x680")
        self.root.minsize(650, 550)
        self.root.configure(bg=self.bg_main)

        self.typing_frame = None
        self.typing_after_id = None
        self.typing_step = 0

        # ==========================================
        # HEADER
        # ==========================================
        header = tk.Frame(
            root,
            bg=self.bg_secondary,
            height=85
        )
        header.pack(
            fill="x",
            padx=0,
            pady=0
        )
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="🤖  NOVA",
            font=("Segoe UI", 26, "bold"),
            bg=self.bg_secondary,
            fg=self.color_primary
        )
        title.pack(pady=(10, 0))

        subtitle = tk.Label(
            header,
            text="Rule-Based AI Assistant",
            font=("Segoe UI", 10),
            bg=self.bg_secondary,
            fg=self.text_secondary
        )
        subtitle.pack(pady=(2, 8))

        # ==========================================
        # CHAT CONTAINER
        # ==========================================
        chat_container = tk.Frame(
            root,
            bg=self.bg_main
        )
        chat_container.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=12
        )

        # Canvas for scrolling
        self.canvas = tk.Canvas(
            chat_container,
            bg=self.bg_secondary,
            highlightthickness=0,
            relief="flat"
        )
        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Scrollbar with better styling
        scrollbar = tk.Scrollbar(
            chat_container,
            orient="vertical",
            command=self.canvas.yview,
            bg=self.bg_main,
            activebackground=self.text_secondary
        )
        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        # Inner frame where messages live
        self.messages_frame = tk.Frame(
            self.canvas,
            bg=self.bg_secondary
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.messages_frame,
            anchor="nw"
        )

        self.messages_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        self.canvas.bind(
            "<Configure>",
            self.resize_message_area
        )

        # Enable mouse wheel scrolling for Windows/Laptops
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.root.bind_all("<MouseWheel>", self.on_mousewheel)
        self.messages_frame.bind_all("<MouseWheel>", self.on_mousewheel)

        # ==========================================
        # INPUT AREA
        # ==========================================
        input_container = tk.Frame(
            root,
            bg=self.bg_main
        )
        input_container.pack(
            fill="x",
            padx=12,
            pady=(0, 12)
        )

        self.input_box = tk.Entry(
            input_container,
            font=("Segoe UI", 12),
            bg=self.bg_input,
            fg=self.text_dark,
            relief="flat",
            insertbackground=self.color_primary,
            bd=1
        )
        self.input_box.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(5, 2),
            pady=5,
            ipady=5
        )

        self.send_button = tk.Button(
            input_container,
            text="Send  ➤",
            font=("Segoe UI", 11, "bold"),
            bg=self.color_primary,
            fg=self.text_light,
            activebackground=self.accent,
            activeforeground=self.text_light,
            relief="flat",
            cursor="hand2",
            command=self.send_message,
            bd=0,
            padx=3,
            pady=3
        )
        self.send_button.pack(
            side="right",
            padx=(8, 10),
            pady=5,
            ipadx=10,
            ipady=5
        )

        # ==========================================
        # BOTTOM BUTTONS
        # ==========================================
        bottom = tk.Frame(
            root,
            bg=self.bg_main,
            height=35
        )
        bottom.pack(
            fill="x",
            pady=(0, 10)
        )

        clear_button = tk.Button(
            bottom,
            text="🗑️  Clear Chat",
            font=("Segoe UI", 10),
            bg=self.bg_secondary,
            fg=self.text_secondary,
            relief="flat",
            cursor="hand2",
            command=self.clear_chat,
            bd=0,
            activebackground=self.color_primary_light,
            activeforeground=self.color_primary
        )
        clear_button.pack(
            side="left",
            padx=15,
            pady=5
        )

        exit_button = tk.Button(
            bottom,
            text="Exit  ✕",
            font=("Segoe UI", 10),
            bg=self.bg_secondary,
            fg=self.text_secondary,
            relief="flat",
            cursor="hand2",
            command=self.close_app,
            bd=0,
            activebackground=self.color_primary_light,
            activeforeground=self.color_primary
        )
        exit_button.pack(
            side="right",
            padx=15,
            pady=5
        )

        # ==========================================
        # KEYBOARD
        # ==========================================
        self.input_box.bind(
            "<Return>",
            self.send_message
        )

        self.input_box.focus()

        # ==========================================
        # WELCOME MESSAGE
        # ==========================================
        self.add_message(
            "Nova",
            "Hello! 👋 I'm Nova. How can I help you today?"
        )

    # ==========================================
    # SCROLLING
    # ==========================================
    def update_scroll_region(self, event=None):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

        self.canvas.after(
            10,
            lambda: self.canvas.yview_moveto(1.0)
        )

    def resize_message_area(self, event):
        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )

    # ==========================================
    # MOUSE WHEEL SCROLLING
    # ==========================================
    def on_mousewheel(self, event):
        """
        Handle mouse wheel scrolling.
        """
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(3, "units")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-3, "units")

    # ==========================================
    # ADD MESSAGE
    # ==========================================
    def add_message(self, sender, message):
        """
        Add a chat bubble with rounded corners.
        Nova = left
        You = right
        """

        # Outer row
        row = tk.Frame(
            self.messages_frame,
            bg=self.bg_secondary
        )

        row.pack(
            fill="x",
            pady=8,
            padx=12
        )

        # ==========================================
        # NOVA MESSAGE - LEFT
        # ==========================================
        if sender == "Nova":
            # Create a container with slight padding
            container = tk.Frame(
                row,
                bg=self.bg_secondary
            )
            container.pack(
                side="left",
                anchor="w",
                padx=(0, 10)
            )

            # Canvas for rounded bubble
            bubble_canvas = tk.Canvas(
                container,
                width=460,
                height=85,
                bg=self.bg_secondary,
                highlightthickness=0,
                relief="flat",
                bd=0
            )
            bubble_canvas.pack()

            # Draw rounded rectangle using arc and lines
            self._draw_rounded_rect(
                bubble_canvas,
                5, 5, 455, 80,
                radius=12,
                fill=self.color_nova,
                outline=""
            )

            # Create frame inside canvas for content
            bubble_frame = tk.Frame(
                container,
                bg=self.color_nova
            )
            bubble_canvas.create_window(
                230, 42,
                window=bubble_frame,
                width=430,
                height=65
            )

            name = tk.Label(
                bubble_frame,
                text="🤖 Nova",
                font=("Segoe UI", 9, "bold"),
                bg=self.color_nova,
                fg=self.color_primary
            )
            name.pack(
                anchor="w",
                pady=(2, 0),
                padx=5
            )

            text = tk.Label(
                bubble_frame,
                text=message,
                font=("Segoe UI", 11),
                bg=self.color_nova,
                fg=self.text_dark,
                justify="left",
                wraplength=410
            )
            text.pack(
                anchor="w",
                pady=(2, 2),
                padx=5
            )

        # ==========================================
        # USER MESSAGE - RIGHT
        # ==========================================
        else:
            # Create a container with slight padding
            container = tk.Frame(
                row,
                bg=self.bg_secondary
            )
            container.pack(
                side="right",
                anchor="e",
                padx=(10, 0)
            )

            # Canvas for rounded bubble
            bubble_canvas = tk.Canvas(
                container,
                width=300,
                height=70,
                bg=self.bg_secondary,
                highlightthickness=0,
                relief="flat",
                bd=0
            )
            bubble_canvas.pack()

            # Draw rounded rectangle using arc and lines
            self._draw_rounded_rect(
                bubble_canvas,
                5, 5, 295, 65,
                radius=12,
                fill=self.color_user,
                outline=""
            )

            # Create frame inside canvas for content
            bubble_frame = tk.Frame(
                container,
                bg=self.color_user
            )
            bubble_canvas.create_window(
                150, 35,
                window=bubble_frame,
                width=270,
                height=55
            )

            name = tk.Label(
                bubble_frame,
                text="You",
                font=("Segoe UI", 9, "bold"),
                bg=self.color_user,
                fg=self.text_light
            )
            name.pack(
                anchor="e",
                pady=(2, 0),
                padx=5
            )

            text = tk.Label(
                bubble_frame,
                text=message,
                font=("Segoe UI", 11),
                bg=self.color_user,
                fg=self.text_light,
                justify="right",
                wraplength=200
            )
            text.pack(
                anchor="e",
                pady=(2, 2),
                padx=5
            )

        self.root.update_idletasks()

        self.canvas.yview_moveto(1.0)

    # ==========================================
    # DRAW ROUNDED RECTANGLE
    # ==========================================
    def _draw_rounded_rect(self, canvas, x1, y1, x2, y2, radius=20, **kwargs):
        """
        Draw a rounded rectangle on canvas.
        """
        points = [
            x1+radius, y1,
            x1+radius, y1,
            x2-radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1+radius,
            x1, y1
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    # ==========================================
    # TYPING DOTS
    # ==========================================
    def show_typing(self):
        """
        Show animated floating dots on the left with rounded corners.
        """

        self.typing_frame = tk.Frame(
            self.messages_frame,
            bg=self.bg_secondary
        )

        self.typing_frame.pack(
            fill="x",
            pady=8,
            padx=12
        )

        # Canvas for rounded bubble
        bubble_canvas = tk.Canvas(
            self.typing_frame,
            width=100,
            height=65,
            bg=self.bg_secondary,
            highlightthickness=0,
            relief="flat",
            bd=0
        )
        bubble_canvas.pack(side="left", anchor="w")

        # Draw rounded rectangle
        self._draw_rounded_rect(
            bubble_canvas,
            5, 5, 95, 60,
            radius=12,
            fill=self.color_nova,
            outline=""
        )

        # Create frame for content
        bubble_frame = tk.Frame(
            self.typing_frame,
            bg=self.color_nova
        )
        bubble_canvas.create_window(
            50, 32,
            window=bubble_frame,
            width=80,
            height=50
        )

        self.typing_label = tk.Label(
            bubble_frame,
            text="•••",
            font=("Segoe UI", 13, "bold"),
            bg=self.color_nova,
            fg=self.color_primary
        )

        self.typing_label.pack()

        self.typing_step = 0

        self.animate_typing()

        self.root.update_idletasks()
        self.canvas.yview_moveto(1.0)

    # ==========================================
    # ANIMATE DOTS
    # ==========================================
    def animate_typing(self):

        if self.typing_frame is None:
            return

        states = [
            "•  ",
            "•• ",
            "•••",
            " ••",
            "  •",
            " ••",
            "•••",
            "•• "
        ]

        self.typing_label.config(
            text=states[self.typing_step]
        )

        self.typing_step = (
            self.typing_step + 1
        ) % len(states)

        self.typing_after_id = self.root.after(
            250,
            self.animate_typing
        )

    # ==========================================
    # REMOVE TYPING
    # ==========================================
    def remove_typing(self):

        if self.typing_after_id is not None:

            try:
                self.root.after_cancel(
                    self.typing_after_id
                )
            except tk.TclError:
                pass

            self.typing_after_id = None

        if self.typing_frame is not None:

            self.typing_frame.destroy()

            self.typing_frame = None

    # ==========================================
    # SEND MESSAGE
    # ==========================================
    def send_message(self, event=None):

        user_input = self.input_box.get().strip()

        # Don't send empty messages
        if not user_input:
            return

        # Show user's message
        self.add_message(
            "You",
            user_input
        )

        # Clear input
        self.input_box.delete(
            0,
            tk.END
        )

        # Disable input during response
        self.input_box.config(
            state="disabled"
        )

        self.send_button.config(
            state="disabled"
        )

        # ==========================================
        # SANITIZATION
        # ==========================================
        sanitized_input = (
            user_input
            .lower()
            .strip()
        )

        # ==========================================
        # INTENT DETECTION
        # ==========================================
        intent = detect_intent(
            sanitized_input
        )

        # ==========================================
        # GET RESPONSE
        # ==========================================
        response = get_response(
            intent
        )

        # ==========================================
        # SHOW TYPING DOTS
        # ==========================================
        self.show_typing()

        # ==========================================
        # RESPONSE DELAY
        # ==========================================
        self.root.after(
            600,
            lambda: self.show_response(
                response,
                intent
            )
        )

    # ==========================================
    # SHOW RESPONSE
    # ==========================================
    def show_response(self, response, intent):

        # Remove dots
        self.remove_typing()

        # Show Nova response
        self.add_message(
            "Nova",
            response
        )

        # Enable input again
        self.input_box.config(
            state="normal"
        )

        self.send_button.config(
            state="normal"
        )

        self.input_box.focus()

        # ==========================================
        # EXIT STRATEGY
        # ==========================================
        if intent == "goodbye":

            self.root.after(
                800,
                self.close_app
            )

    # ==========================================
    # CLEAR CHAT
    # ==========================================
    def clear_chat(self):

        self.remove_typing()

        for widget in self.messages_frame.winfo_children():
            widget.destroy()

        self.add_message(
            "Nova",
            "Chat cleared! 👋 How can I help you?"
        )

        self.input_box.focus()

    # ==========================================
    # CLOSE
    # ==========================================
    def close_app(self):

        self.remove_typing()

        self.root.destroy()


# ==============================================
# RUN NOVA
# ==============================================
if __name__ == "__main__":

    root = tk.Tk()

    app = NovaGUI(root)

    root.mainloop()