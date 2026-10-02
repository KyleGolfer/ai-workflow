import litellm
from litellm.integrations.custom_logger import CustomLogger

class VeniceTransformCallback(CustomLogger):
    def __init__(self):
        super().__init__()
    
    def log_pre_api_call(self, model, messages, kwargs):
        """Transform messages before sending to API"""
        model_str = str(model).lower()
        if not ("venice" in model_str or model in ["venice-fast", "venice/premium"]):
            return
        
        # Handle 'messages' format (chat completions)
        if messages and isinstance(messages, list):
            for message in messages:
                self._transform_message(message)
        
        # Handle 'input' format (responses API)
        if "input" in kwargs and isinstance(kwargs["input"], list):
            for item in kwargs["input"]:
                self._transform_message(item)
    
    def _transform_message(self, message):
        """Transform a single message's content from array to string"""
        if not isinstance(message, dict):
            return
        
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
    
    # Required methods for LiteLLM callback interface
    async def async_log_success_event(self, kwargs, response_obj, start_time, end_time):
        pass
    
    async def async_log_failure_event(self, kwargs, response_obj, start_time, end_time):
        pass
    
    def log_success_event(self, kwargs, response_obj, start_time, end_time):
        pass
    
    def log_failure_event(self, kwargs, response_obj, start_time, end_time):
        pass

# Create instance
venice_transform_callback = VeniceTransformCallback()

# Function for direct callback usage
def venice_transform(request_data: dict, **kwargs) -> dict:
    """Direct transform function"""
    model = request_data.get("model", "")
    model_str = str(model).lower()
    
    if not ("venice" in model_str or model in ["venice-fast", "venice/premium"]):
        return request_data
    
    # Transform messages format
    if "messages" in request_data:
        for msg in request_data["messages"]:
            if isinstance(msg, dict):
                content = msg.get("content")
                if isinstance(content, list):
                    text_parts = []
                    for part in content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            text_parts.append(part.get("text", ""))
                    msg["content"] = " ".join(text_parts) if text_parts else ""
    
    # Transform input format (responses API)
    if "input" in request_data:
        for item in request_data["input"]:
            if isinstance(item, dict):
                content = item.get("content")
                if isinstance(content, list):
                    text_parts = []
                    for part in content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            text_parts.append(part.get("text", ""))
                    item["content"] = " ".join(text_parts) if text_parts else ""
    
    return request_data
