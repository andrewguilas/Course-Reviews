import tkinter


class Scene():
    def clear_fields(self, fields):
        for field in fields:
            if isinstance(field, tkinter.Entry):
                field.delete(0, "end")
            elif isinstance(field, tkinter.Text):
                field.delete("1.0", "end")

    def highlight_field(self, field, is_error):
        ERROR_COLOR = 'pink'
        DEFAULT_COLOR = 'white'
    
        color = ERROR_COLOR if is_error else DEFAULT_COLOR
        field.config(bg=color)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def strip_string(self, string):
        return string.lower().strip().replace(" ", "")
