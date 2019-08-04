class ClassicEcho: # Define a collection of methods
    @staticmethod 
    # Indicate this method is not part of a specific instance of the class
    def create_echo(input : str = "echo "
        ,repeat_num_times : int = 3
        ,trim_last_space : bool = True) -> str: 
        # Define a method with parameters, the types of those parameters,
        # the default input for each parameter, and the return type
        result = input * repeat_num_times 
        # repeat the string input multiplied by the integer repeat_num_times
        if trim_last_space == True: 
            result = result[0:-1] 
            # If trim_last_space is true, return everything from the first
            # to the second to last character with -1
        return result 
        # Return the modified result if the last condition was true,
        # or the original result after multiplications