# A Top Level script to call the package/module below
# The layout is Folder/Folder/File/Class for the "from" statements
from sound.effects.echo import ClassicEcho
from sound.formats.wav_write import WavWrite

phrase = 'L1 '
repeat_number_of_times = 3
trim_space = True
# define arguments to be passed into create_echo.

echo_phrase = ClassicEcho.create_echo(phrase,repeat_number_of_times,trim_space)

encoded_phrase = WavWrite.wav_encode(echo_phrase)
# Call the WavWrite class and use the wav_encode method with the phrase passed in

print(f'The result is: {encoded_phrase}')
