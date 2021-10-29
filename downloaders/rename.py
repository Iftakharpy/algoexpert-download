"""Given a file name make that valid for Linux/Windows Operating Systems"""

# https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names

# While these printable characters are invalid in windows,
# in Linux only "/" (forward slash) is invalid.
invalid_characters = set([ 
    "<",
    ">",
    ":",
    '"',
    "/",
    "\\", # backslash
    "|",
    "?",
    "*"
])

# For non-printable characters, only "\x00" (NULL byte - ASCII char code 0) is invalid in Linux
# Windows doesn't support  "\x00" to "\x31" (ASCII control characters - ASCII char codes 0-31)
# Windows also doesn't allow '.' or ' ' at the end of file names

# Applicable for windows reserved file names
# Note: Windows file names are case insensitive
reserved_names = set([
    "CON",
    "PRN",
    "AUX",
    "NUL",
    "COM1",
    "COM2",
    "COM3",
    "COM4",
    "COM5",
    "COM6",
    "COM7",
    "COM8",
    "COM9",
    "LPT1",
    "LPT2",
    "LPT3",
    "LPT4",
    "LPT5",
    "LPT6",
    "LPT7",
    "LPT8",
    "LPT9"
])


def make_file_name_valid(file_name:str):
    """Given file_name makes that valid for Linux/Windows Operating Systems.
    By removing all the invalid characters on Linux/Windows.

    After removing all the invalid characters if the file name is any of the 
    reserved keywords for Windows Throws ValueError
    """
    corrected_file_name = []

    for char in file_name:
        is_valid_char = not char in invalid_characters
        is_not_non_printable_characters = not ord(char)<=31

        # Adding only valid characters
        if is_valid_char and is_not_non_printable_characters:
            corrected_file_name.append(char)

    # Windows doesn't allow '.' or ' ' at the end of file names
    # Removing spaces and .(dots) from the end of name 
    while corrected_file_name[-1] in set([' ', '.']):
        corrected_file_name.pop()

    corrected_file_name = ''.join(corrected_file_name)

    if corrected_file_name.upper() in reserved_names:
        raise ValueError(f"File name \"{corrected_file_name}\" is a reserved keyword for Windows OS.")
    
    return corrected_file_name
