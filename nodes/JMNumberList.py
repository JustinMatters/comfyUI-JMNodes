class JMNumberList:
    """
    JMNumberList node which delivers a list of numbers from 0 up to the specified number (max 1023)
    Useful for creating boolean permutations of prompts in combination with JMIntegerToBooleans and JMSwitchablePrompt.
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
                "input_integer": ("INT", {
                    "default": 0, 
                    "min": 0,
                    "max": 1023,
                    "step": 1,
                    "display": "number",
                }),
            },
        }

    RETURN_TYPES = ("INT",)

    # ensure the output list of numbers is processed sequentially by downstream nodes
    OUTPUT_IS_LIST = (True,)

    FUNCTION = "generate_integer_list"

    CATEGORY = "JMNodes"

    def generate_integer_list(self, input_integer):
        """
        returns  a list of numbers from 0 up to the specified number (max 1023)

        Inputs:
            input_integer: the number up to which we will geenrate a list of integers

        Outputs:
            list(integers): the required list of integers
        """
        # create our list of values
        values = list(range(input_integer + 1))
        return (values, )



