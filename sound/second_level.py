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

from sound.effects.echo import ClassicEcho
from sound.formats.wav_write import WavWrite

phrase = 'L2 '
repeat_number_of_times = 3
trim_space = True
# define arguments to be passed into create_echo.

echo_phrase = ClassicEcho.create_echo(phrase,repeat_number_of_times,trim_space)

encoded_phrase = WavWrite.wav_encode(echo_phrase)
# Call the WavWrite class and use the wav_encode method with the phrase passed in

print(f'The result is: {encoded_phrase}')