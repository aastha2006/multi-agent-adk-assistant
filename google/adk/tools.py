from typing import Callable, Any

class Tool:
    def __init__(self, name: str, description: str, func: Callable[..., Any]):
        self.name = name
        self.description = description
        self.func = func
        
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
