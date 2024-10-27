from .nodes.JMIntegerToBooleans import *
from .nodes.JMNumberList import *
from .nodes.JMSWitchablePrompt import *
# from .nodes.JMSWitchablePrompt import *

NODE_CLASS_MAPPINGS = {
    "JMIntegerToBooleans": JMIntegerToBooleans,
    "JMNumberList": JMNumberList,
    "JMSWitchablePrompt": JMSWitchablePrompt,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "JMIntegerToBooleans": "Integer to Boolean Values JM",
    "JMNumberList": "Create List of Numbers JM",
    "JMSWitchablePrompt": "Switchable Prompt JM",
}


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']