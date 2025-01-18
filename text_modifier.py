class TextModifier:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "find_text": ("STRING", {"default": ""}),
                "replace_text": ("STRING", {"default": ""}),
                "operation": (["replace", "delete"],),
                "case_sensitive": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING", "INT",)
    RETURN_NAMES = ("text", "count",)
    FUNCTION = "modify_text"
    CATEGORY = "SG11/text"

    def modify_text(self, text, find_text, replace_text, operation, case_sensitive):
        if not find_text:
            return (text, 0)
        
        count = 0
        
        if not case_sensitive:
            temp_text = text.lower()
            find_text_lower = find_text.lower()
            start = 0
            positions = []
            while True:
                pos = temp_text.find(find_text_lower, start)
                if pos == -1:
                    break
                positions.append(pos)
                start = pos + len(find_text_lower)
            
            count = len(positions)
            modified_text = text
            for pos in reversed(positions):
                original_match = modified_text[pos:pos + len(find_text)]
                if operation == "replace":
                    modified_text = modified_text[:pos] + replace_text + modified_text[pos + len(find_text):]
                else:  # delete
                    modified_text = modified_text[:pos] + modified_text[pos + len(find_text):]
        else:
            count = text.count(find_text)
            if operation == "replace":
                modified_text = text.replace(find_text, replace_text)
            else:  # delete
                modified_text = text.replace(find_text, "")
            
        return (modified_text, count)

NODE_CLASS_MAPPINGS = {
    "TextModifier": TextModifier
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextModifier": "Text Modifier (SG11)"
} 