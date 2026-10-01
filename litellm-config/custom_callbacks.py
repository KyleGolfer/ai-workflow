import litellm
from litellm.integrations.custom_logger import CustomLogger

class VeniceTransformCallback(CustomLogger):
    def __init__(self):
        super().__init__()
    
    def log_pre_api_call(self, model, messages, kwargs):
        """Transform messages before sending to API"""
        # Check if this is a Venice model
        if not ("venice" in model.lower() or model in ["venice-fast", "venice/premium"]):
            return
        
        # Transform each message
        for message in messages:
            content = message.get("content")
            
            # Convert array content to string
            if isinstance(content, list):
                text_parts = []
                for part in content:
                    if isinstance(part, dict):
                        if part.get("type") == "text":
                            text_parts.append(part.get("text", ""))
                        elif part.get("type") == "image_url":
                            continue
                message["content"] = " ".join(text_parts) if text_parts else ""
        
        return

# Instantiate the callback
venice_transform_callback = VeniceTransformCallback()
