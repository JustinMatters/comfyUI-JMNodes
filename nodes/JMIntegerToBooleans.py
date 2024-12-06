class JMIntegerToBooleans:
    """
    JMIntegerToBooleans takes an integer input and outputs 10 boolean values corresponding to the 10 least significant 
    bits of the integer's boolean representation. This allows you to convert integers into their boolean representation. 
    This is useful for creating boolean permutations of prompts in combination with JMNumberList and JMSwitchablePrompt.
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
                    "min": 0, #Minimum value
                    "max": 1023, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number", # Cosmetic only: display as "number" or "slider"
                }),
            },
        }

    # Booleans corresponding to the (1,2,4,8,16,32,64,128,256,512) binary digits of the input
    RETURN_TYPES = (
        "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN", "BOOLEAN"
    )

    FUNCTION = "convert_to_booleans"

    CATEGORY = "JMNodes"

    def convert_to_booleans(self, input_integer):
        """
        returns a 10-tuple of boolean values starting with the least significant. 
        Thus the outputs represent a decimal number between 0 and 1023 in binary

        Inputs:
            input_intger (integer): an integer (any value above 1023 will only have the binary digits up to 512 considered)

        Outputs:
            tuple(booleans): a 10-tuple of binary values, least significant first
        """
        # catch type issues and prevent crashes
        if type(input_integer) is not int:
            input_integer = 0
        # Convert the integer to its binary representation (without the '0b' prefix)
        binary_str = bin(input_integer)[2:]
        # Convert the binary string to a list of boolean values starting with least significant 
        bool_list = [bool(int(bit)) for bit in binary_str]
        # reverse to begin with least significant
        reversed_list = list(reversed(bool_list))
        # pad to at least 10 values
        padded_list = reversed_list + ([False]*10)
        # take the 10 least significant values (we only cover 0-1023)
        trimmed_list = padded_list[0:10]
        # convert to a tuple for return as required by ComfyUI
        return tuple(trimmed_list)