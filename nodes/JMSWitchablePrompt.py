class JMSWitchablePrompt:
    """
    A prompt which will be forwarded if the corresponding boolean value is True, otherwise the empty string will be sent
    This is useful for creating boolean permutations of prompts in combination with JMIntegerToBooleans and JMNumberList
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        Standard Class method for ComfyUI nodes specifying the inputs to the node. 
        See https://docs.comfy.org/essentials/custom_node_datatypes details on format
        """
        return {
            "required": {
                "prompt": ("STRING",
                {
                    "default": "",
                    "multiline": True,
                }
                ),
                "boolean_switch": ("BOOLEAN", 
                {
                    "default": False,
                }),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "prompt_switch"

    CATEGORY = "JMNodes"

    def prompt_switch(self, prompt, boolean_switch):
        """
        returns either the prompt or an empty string depending on boolean_switch

        Inputs:
            prompt: the prompt which will be forwarded if the boolean_switch is true
            boolean_switch: boolean value either True or False (default: False)

        Outputs:
            string: either the prompt or an empty string depending on boolean_switch
        """
        if boolean_switch:
            # pass on the prompt cleaned of newlines
            tidy_prompt = prompt.replace('\n', ' ')
            return (str(tidy_prompt), )
        else:
            return ("", )