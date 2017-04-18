'''
Created on Apr 17, 2017

@author: ahmed.ch.90@gmail.com
'''

import sys
import argparse


ALONE = 0
BEGIN = 1
MIDDLE = 2
END = 3
LETTERS = {
    # ARABIC LETTER HAMZA
    'hh': ('hhA', '', '', 'hhE'),
    # ARABIC LETTER ALEF WITH MADDA ABOVE
    'am': ('amA', '', '', 'amE'),
    # ARABIC LETTER ALEF WITH HAMZA ABOVE
    'ae': ('aeA', '', '', 'aeE'),
    # ARABIC LETTER WAW WITH HAMZA ABOVE
    'wl': ('wlA', '', '', 'WlE'),
    # ARABIC LETTER ALEF WITH HAMZA BELOW
    'ah': ('ahA', '', '', 'ahE'),
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'al': ('alA', 'alB', 'alM', 'alE'),
    # ARABIC LETTER ALEF
    'aa': ('aaA', '', '', 'aaE'),
    # ARABIC LETTER BEH
    'ba': ('baA', 'baA', 'baM', 'baE'),
    # ARABIC LETTER TEH MARBUTA
    'teE': ('teeA', '', '', 'teeE'),
    'tee': ('teeA', '', '', 'teeE'),
    # ARABIC LETTER TEH
    'ta': ('taA', 'taB', 'taM', 'taE'),
    # ARABIC LETTER THEH
    'th': ('thA', 'thB', 'thM', 'thE'),
    # ARABIC LETTER JEEM
    'ja': ('jaA', 'jaB', 'jaM', 'jaE'),
    # ARABIC LETTER HAH
    'ha': ('haA', 'haB', 'haM', 'haE'),
    # ARABIC LETTER KHAH
    'kh': ('khA', 'khB', 'khM', 'khE'),
    # ARABIC LETTER DAL
    'da': ('daA', '', '', 'daE'),
    # ARABIC LETTER THAL
    'dh': ('dhA', '', '', 'dhE'),
    # ARABIC LETTER REH
    'ra': ('raA', '', '', 'raE'),
    # ARABIC LETTER ZAIN
    'za': ('zaA', '', '', 'zaE'),
    # ARABIC LETTER SEEN
    'se': ('seA', 'seB', 'seM', 'seE'),
    # ARABIC LETTER SHEEN
    'sh': ('shA', 'shB', 'shM', 'shE'),
    # ARABIC LETTER SAD
    'sa': ('saA', 'saB', 'saM', 'saE'),
    # ARABIC LETTER DAD
    'de': ('deA', 'deB', 'deM', 'deE'),
    # ARABIC LETTER TAH
    'to': ('toA', 'toB', 'toM', 'toE'),
    # ARABIC LETTER ZAH
    'zha': ('zhaA', 'zhaB', 'zhaM', 'zhaE'),
    # ARABIC LETTER AIN
    'ay': ('ayA', 'ayB', 'ayM', 'ayE'),
    # ARABIC LETTER GHAIN
    'gh': ('ghA', 'ghB', 'ghM', 'ghE'),
    # ARABIC LETTER FEH
    'fa': ('faA', 'faB', 'faM', 'faE'),
    # ARABIC LETTER QAF
    'ka': ('kaA', 'kaB', 'kaM', 'kaE'),
    # ARABIC LETTER KAF
    'ke': ('keA', 'keB', 'keM', 'keE'),
    # ARABIC LETTER LAM
    'la': ('laA', 'laB', 'laM', 'laE'),
    # ARABIC LETTER MEEM
    'ma': ('maA', 'maB', 'maM', 'maE'),
    # ARABIC LETTER NOON
    'na': ('naA', 'naB', 'naM', 'naE'),
    # ARABIC LETTER HEH
    'he': ('heA', 'heB', 'heM', 'heE'),
    # ARABIC LETTER WAW
    'wa': ('waA', '', '', 'waE'),
    # ARABIC LETTER ALEF MAKSURA
    'al': ('alA', '', '', 'alE'),
    # ARABIC LETTER YAA
    'ee': ('eeA', '', '', 'eeE'),
    # ARABIC LETTER YEH
    'ya': ('yaA', 'yaB', 'yaM', 'yaE'),
    'laaa': ('laBaaE', '', '', 'laMaaE'),
    'laae': ('laBaeE', '', '', 'laMaeE'),
    'laah': ('laBahE', '', '', 'laMahE'),
    
    }
    
def _connects_with_letter_before(letter):
    if letter not in LETTERS:
        return False
    forms = LETTERS[letter]
    return forms[END] or forms[MIDDLE]


def _connects_with_letter_after(letter):
    if letter not in LETTERS:
        return False
    forms = LETTERS[letter]
    return forms[BEGIN] or forms[MIDDLE]


def _connects_with_letters_before_and_after(letter):
    if letter not in LETTERS:
        return False
    forms = LETTERS[letter]
    return forms[MIDDLE]    
def reshape(input_text,skip):
    output = []
    FORM = 1
    LETTER = 0
    NOT_SUPPORTED = -1
    text = input_text.split(' ')
    for i in range(len(text)):
        if i < skip:
            letter = text[i]
            if letter not in LETTERS:
                output.append((letter, NOT_SUPPORTED))
            elif not output:
                output.append((letter, ALONE))
            else:
                previous_output = output[-1]
                if previous_output[FORM] == NOT_SUPPORTED:
                    output.append((letter, ALONE))
                elif not _connects_with_letter_before(letter):
                    output.append((letter, ALONE))
                elif not _connects_with_letter_after(previous_output[LETTER]):
                    output.append((letter, ALONE))
                elif (previous_output[FORM] == END
                      and not _connects_with_letters_before_and_after(
                        previous_output[LETTER]
                      )):
                    output.append((letter, ALONE))
                elif previous_output[FORM] == ALONE:
                    output[-1] = (previous_output[LETTER],
                                  BEGIN)
                    output.append((letter, END))
                # Otherwise, we will change the previous letter to connect to
                # the current letter
                else:
                    output[-1] = (previous_output[LETTER],
                                  MIDDLE)
                    output.append((letter, END))
        
    return ' '.join(
            map(
                lambda o: (
                    o[FORM] == NOT_SUPPORTED
                    and o[LETTER]
                    or LETTERS[o[LETTER]][o[FORM]]
                ),
                filter(lambda o: o[LETTER], output),
            )
        )    
def main():
    # parse command line options
    parser = argparse.ArgumentParser(description='Add Context dependency for Arabic transcripted text')
    parser.add_argument('-f','--file', help='Arabic transcription input file', required=True)
    parser.add_argument('-s','--skip', help='Skip text entities for each line (For structured files)', required=False)
    args = vars(parser.parse_args())
    
    with open(args['file']) as f:
        content = f.readlines()
    f = open(args['file'] +".ctx", 'w')
    for x in content:
        f.write(reshape(x.replace("\n", " \n"),args['skip']))
    f.close()
if __name__ == "__main__":
    main()
