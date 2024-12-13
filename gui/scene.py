class Scene():
    def clear_fields(self, fields):
        for field in fields:
            field.delete(0, "end")

    def highlight_field(self, field, is_error):
        ERROR_COLOR = 'pink'
        DEFAULT_COLOR = 'white'
    
        color = ERROR_COLOR if is_error else DEFAULT_COLOR
        field.config(bg=color)

    def strip_string(self, string):
        return string.lower().strip().replace(" ", "")
