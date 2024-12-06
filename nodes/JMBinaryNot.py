class JMBinaryNot:
    """
    JMBinaryNot node which receives a binary True or False and inverts it.
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
                "boolean_input": ("BOOLEAN", 
                {
                    "default": False,
                }),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)

    FUNCTION = "invert_boolean"

    CATEGORY = "JMNodes"

    def invert_boolean(self, boolean_input):
        """
        returns the inverse of the boolean input received

        Inputs:
            boolean_input (boolean): input boolean value

        Outputs:
            boolean: the inverse of the input boolean value
        """
        if boolean_input:
            return (False, )
        else:
            return (True, )
