# Check to see if this is the entry point of the program
# If so, import the OS and SYS modules, and append the working directory 
# to the sys.path variable, which lists all directories files
# might be accessed from. 
# os.getcwd() will get the Current Working Directory for your development,
# which looks something like [higher directory levels]/python-sibling-import.

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.getcwd())

class WavWrite: # Define a collection of methods
    @staticmethod # Indicates this is not an instance of a class method
    def wav_encode(input: str) -> str:
        result = f'I encoded {input} as a Wav!'
        return result
    # This method takes in a string parameter called input, 
    # and is expected to retrun a string as the output.
    # This uses the string literal format of f'' to insert variables

    @staticmethod
    def wav_echo_encode(input: str) -> str:
        from sound.effects.echo import ClassicEcho
        result_echo = ClassicEcho.create_echo(input)
        result = f'I encoded {result_echo} as a Wav!'
        return result
    # This method is similar to the one above, except that it creates
    # an echo for you with the detault options specified. Since the echo
    # effect is in a sibling folder, it will need an import to be used.
    # This import is achieved by being accessible from the top level file like
    # in top_level.py, or by adding the current working directory 
    # to the system path where scripts can be found. This method relies on
    # the working directory being the top level of the project. 

if __name__ == '__main__':
    print(WavWrite.wav_echo_encode('L3 '))
# If running this file rather than a higher level one, 
# the result will be printed here.