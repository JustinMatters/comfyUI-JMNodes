from .nodes.JMIntegerToBooleans import *
from .nodes.JMNumberList import *
from .nodes.JMSwitchablePrompt import *
from .nodes.JMBinaryNot import *

NODE_CLASS_MAPPINGS = {
    "JMIntegerToBooleans": JMIntegerToBooleans,
    "JMNumberList": JMNumberList,
    "JMSWitchablePrompt": JMSwitchablePrompt,
    "JMBinaryNot": JMBinaryNot,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "JMIntegerToBooleans": "Integer to Boolean Values JM",
    "JMNumberList": "Create List of Numbers JM",
    "JMSwitchablePrompt": "Switchable Prompt JM",
    "JMBinaryNot": "Binary Not JM",
}


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']