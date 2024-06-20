"""For output formatting.
Interact via the FancyObject() class (import as fncy for short or smth)
or grab format codes directly from the following classes:
    color()
    background()
    effects()
    fonts()
    ideogram()
and use like so: '\033[{format code}m'.
Chain them with semicolon, end with '\033[0m'
Example: '\033[31;1;4mHello\033[0m'
"""

escape         = '\033['       # Base escape sequence

resetAll       = '\033[0m'     # All attributes off


class FancyObject():
    """ Holds a string and its formattings,
    returns the formatted string.
    Does not currently resolve conflicts
    """
    
    def __init__(self, content, *formattings):
        self.content = content
        self.formattings = formattings
        
    def __str__(self):
        formatCode = escape
        for i, option in enumerate(self.formattings):
            # Seperator only if multiple codes
            if i >= 1:
                formatCode += ';'
            # Add the format code
            formatCode += f'{option}'
        # Cap off the format codes with 'm',
        #  add actual content and close by resetting all attributes
        formatCode += f'm{self.content}{resetAll}'
        return formatCode
        

class color():
    """ Text color """
    invert                = '7'       # Swap fore- and background
    resetInvert           = '27'      # 
    
    black                 = '30'      # 
    red                   = '31'      # 
    green                 = '32'      # 
    yellow                = '33'      # 
    blue                  = '34'      # 
    magenta               = '35'      # 
    cyan                  = '36'      # 
    white                 = '37'      # 
    
    brightBlack           = '90'      # Nonstandard
    brightRed             = '91'      # Nonstandard
    brightGreen           = '92'      # Nonstandard
    brightYellow          = '93'      # Nonstandard
    brightBlue            = '94'      # Nonstandard
    brightMagenta         = '95'      # Nonstandard
    brightCyan            = '96'      # Nonstandard
    brightWhite           = '97'      # Nonstandard
    
    reset                 = '39'      #
    
    def custom_256(colorValue):
        """ 0-255 """
        baseSequence = '38;5'
        return f'{baseSequence};{colorValue}'
    def custom_RGB(r, g, b):
        """ 0-255 each """
        baseSequence = '38;2'
        return f'{baseSequence};{r};{g};{b}'
    

class background():
    """ Text background """
    invert                = '7'       # Swap fore- and background
    resetInvert           = '27'      # 
    
    black                 = '40'      # 
    red                   = '41'      # 
    green                 = '42'      # 
    yellow                = '43'      # 
    blue                  = '44'      # 
    magenta               = '45'      # 
    cyan                  = '46'      # 
    white                 = '47'      #
    
    brightBlack           = '100'     # Nonstandard
    brightRed             = '101'     # Nonstandard
    brightGreen           = '102'     # Nonstandard
    brightYellow          = '103'     # Nonstandard
    brightBlue            = '104'     # Nonstandard
    brightMagenta         = '105'     # Nonstandard
    brightCyan            = '106'     # Nonstandard
    brightWhite           = '107'     # Nonstandard
    
    reset                 = '49'      # 
    
    def custom_256(colorValue):
        """ 0-255 """
        baseSequence = '48;5'
        return f'{baseSequence};{colorValue}'
    def custom_RGB(r, g, b):
        """ 0-255 each """
        baseSequence = '48;2'
        return f'{baseSequence};{r};{g};{b}'
    
    
class effects():
    """ Bold, italic, etc. """
    bold                          = '1'   # Or increased intensity
    faint                         = '2'   # Not widely supported.
    resetBoldFaint                = '22'  # Neither bold nor faint
    
    italic                        = '3'   # Not widely supported 
                                          #  sometimes treated as inverse.
    fraktur                       = '20'  # Hardly ever supported
    resetItalicFraktur            = '23'  # 
    
    underline                     = '4'   # 
    boldOffDoubleUnderline        = '21'  # Bold off not widely supported;
                                          #  Double underline hardly ever
    resetUnderline                = '24'  # Not singly or doubly underlined
    
    blinkSlow                     = '5'   # less than 150 per minute
    blinkRapid                    = '6'   # MS-DOS ANSI.SYS; 150+ per mnt; 
                                          #  not widely supported
    resetBlink                    = '25'  # 
    
    conceal                       = '8'   # Not widely supported.
    resetConceal                  = '28'  # Reveal
    
    crossedOut                    = '9'   # Not widely supported.
    resetCrossedOut               = '29'  # 
    
    framed                        = '51'  # 
    encircled                     = '52'  # 
    resetFramedEncircled          = '54'  # 
    
    overlined                     = '53'  # 
    resetOverlined                = '55'  # 
    
    


class fonts():
    """ Fonts """
    default         = '10'    # 
    alt1            = '11'    # Select alternate font n-10
    alt2            = '12'    # Select alternate font n-10
    alt3            = '13'    # Select alternate font n-10
    alt4            = '14'    # Select alternate font n-10
    alt5            = '15'    # Select alternate font n-10
    alt6            = '16'    # Select alternate font n-10
    alt7            = '17'    # Select alternate font n-10
    alt8            = '18'    # Select alternate font n-10
    alt9            = '19'    # Select alternate font n-10


class ideogram():
    """ Hardly ever supported """
    underline           = '60'      # hardly ever supported
    doubleUnderline     = '61'      # hardly ever supported
    overline            = '62'      # hardly ever supported
    doubleOverline      = '63'      # hardly ever supported
    stressMarking       = '64'      # hardly ever supported
    resetAttributes     = '65'      # reset the effects of all of 60-64


def test():
    """ Prints out a test 'sheet', showing all available formatting options
    """
    import os
    import time
    
    sections = {'color'     : color,
                'background': background,
                'effects' : effects,
                'fonts'     : fonts,
                'ideogram'  : ideogram,
                }
    subSections = {}
    os.system('clear')
    for section in sections.items():
        # Grab dictionary of possible
        #  modifications from class dictionaries
        name = section[0]
        classCall = section[1]
        attributes = dict(vars(classCall).copy())
        attributes.pop('__module__')
        attributes.pop('__doc__')
        attributes.pop('__weakref__')
        attributes.pop('__dict__')
        # Get rid of the functions
        if 'custom_256' in attributes:
            attributes.pop('custom_256')
            attributes.pop('custom_RGB')
        # Dictionary we're gonna use
        subSections.setdefault(name, attributes)
    # Print formattings
    for item in subSections.items():
        header = item[0]
        attributesDict = item[1]
        print(header)
        for attribute in attributesDict.items():
            key = attribute[0]
            value = attribute[1]
            print('\t', end='')
            print(FancyObject(key, value))
    # Print 256 colors
    print('8-bit colors')
    for i in range(256):
        if i < 10:
            output = f'00{i}'
        elif i < 100:
            output = f'0{i}'
        else:
            output = f'{i}'
        if i == 0 or i == 8 or \
                i >= 16 and i <= 24 or \
                i >=52 and i <= 60 or \
                i >= 88 and i <= 96 or \
                i >= 232 and i <= 244:
            swatch = FancyObject(output, background.custom_256(i), color.white)
        else:
            swatch = FancyObject(output, background.custom_256(i), color.black)
        print(f' {swatch} ', end='')
        # Line breaks
        if i == 15 or i == 231 or i == 255:
            print()
        if (i - 33) % 18 == 0:
            print()
    # Print RGB TrueColor
    character = '█'
    print('\n256*256*256 RGB True Color')
    input('\tTest ready, start on carriage return:')
    os.system('clear')
    for r in range(0,256,30):
        for g in range(0,256,30):
            for b in range(0,256,30):
                swatch = FancyObject(character, color.custom_RGB(r, g, b))
                for i in range(10):
                    print(f'{10 * swatch.__str__()}', end='')
                time.sleep(0.01)

if __name__ == '__main__':
    test()