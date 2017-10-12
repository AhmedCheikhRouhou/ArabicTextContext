# -*- coding: utf-8 -*-

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
ARABIC = 4
LETTERS = {
    # ARABIC LETTER HAMZA
    'hh': ('hhA', '', '', 'hhE','ء'),
    # ARABIC LETTER ALEF WITH MADDA ABOVE
    'am': ('amA', '', '', 'amE','آ'),
    # ARABIC LETTER ALEF WITH HAMZA ABOVE
    'ae': ('aeA', '', '', 'aeE','أ'),
    # ARABIC LETTER WAW WITH HAMZA ABOVE
    'wl': ('wlA', '', '', 'WlE','ؤ'),
    # ARABIC LETTER ALEF WITH HAMZA BELOW
    'ah': ('ahA', '', '', 'ahE','إ'),
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'al': ('alA', 'alB', 'alM', 'alE','ئ'),
    # ARABIC LETTER ALEF
    'aa': ('aaA', '', '', 'aaE','ا'),
    # ARABIC LETTER BEH
    'ba': ('baA', 'baB', 'baM', 'baE','ب'),
    # ARABIC LETTER TEH MARBUTA
    'teE': ('teeA', '', '', 'teeE','ة'),
    'tee': ('teeA', '', '', 'teeE','ة'),
    # ARABIC LETTER TEH
    'ta': ('taA', 'taB', 'taM', 'taE','ت'),
    # ARABIC LETTER THEH
    'th': ('thA', 'thB', 'thM', 'thE','ث'),
    # ARABIC LETTER JEEM
    'ja': ('jaA', 'jaB', 'jaM', 'jaE','ج'),
    # ARABIC LETTER HAH
    'ha': ('haA', 'haB', 'haM', 'haE','ح'),
    # ARABIC LETTER KHAH
    'kh': ('khA', 'khB', 'khM', 'khE','خ'),
    # ARABIC LETTER DAL
    'da': ('daA', '', '', 'daE','د'),
    # ARABIC LETTER THAL
    'dh': ('dhA', '', '', 'dhE','ذ'),
    # ARABIC LETTER REH
    'ra': ('raA', '', '', 'raE','ر'),
    # ARABIC LETTER ZAIN
    'za': ('zaA', '', '', 'zaE','ز'),
    # ARABIC LETTER SEEN
    'se': ('seA', 'seB', 'seM', 'seE','س'),
    # ARABIC LETTER SHEEN
    'sh': ('shA', 'shB', 'shM', 'shE','ش'),
    # ARABIC LETTER SAD
    'sa': ('saA', 'saB', 'saM', 'saE','ص'),
    # ARABIC LETTER DAD
    'de': ('deA', 'deB', 'deM', 'deE','ض'),
    # ARABIC LETTER TAH
    'to': ('toA', 'toB', 'toM', 'toE','ط'),
    # ARABIC LETTER ZAH
    'zha': ('zhaA', 'zhaB', 'zhaM', 'zhaE','ظ'),
    # ARABIC LETTER AIN
    'ay': ('ayA', 'ayB', 'ayM', 'ayE','ع'),
    # ARABIC LETTER GHAIN
    'gh': ('ghA', 'ghB', 'ghM', 'ghE','غ'),
    # ARABIC LETTER FEH
    'fa': ('faA', 'faB', 'faM', 'faE','ف'),
    # ARABIC LETTER QAF
    'ka': ('kaA', 'kaB', 'kaM', 'kaE','ق'),
    # ARABIC LETTER KAF
    'ke': ('keA', 'keB', 'keM', 'keE','ك'),
    # ARABIC LETTER LAM
    'la': ('laA', 'laB', 'laM', 'laE','ل'),
    # ARABIC LETTER MEEM
    'ma': ('maA', 'maB', 'maM', 'maE','م'),
    # ARABIC LETTER NOON
    'na': ('naA', 'naB', 'naM', 'naE','ن'),
    # ARABIC LETTER HEH
    'he': ('heA', 'heB', 'heM', 'heE','ه'),
    # ARABIC LETTER WAW
    'wa': ('waA', '', '', 'waE','و'),
    # ARABIC LETTER ALEF MAKSURA
    'al': ('alA', '', '', 'alE','ى'),
    # ARABIC LETTER YAA
    'ee': ('eeA', '', '', 'eeE','ي'),
    # ARABIC LETTER YEH
    'ya': ('yaA', 'yaB', 'yaM', 'yaE','ي'),
    'laaa': ('laBaaE', '', '', 'laMaaE','لا'),
    'laae': ('laBaeE', '', '', 'laMaeE','لا'),
    'laah': ('laBahE', '', '', 'laMahE','لا'),
    # ARABIC LETTER HAMZA
    'hhA': ('hh', '', '', 'hhE','ء'),
    # ARABIC LETTER ALEF WITH MADDA ABOVE
    'amA': ('am', '', '', 'amE','آ'),
    # ARABIC LETTER ALEF WITH HAMZA ABOVE
    'aeA': ('ae', '', '', 'aeE','أ'),
    # ARABIC LETTER WAW WITH HAMZA ABOVE
    'wlA': ('wl', '', '', 'WlE','ؤ'),
    # ARABIC LETTER ALEF WITH HAMZA BELOW
    'ahA': ('ah', '', '', 'ahE','إ'),
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'alA': ('al', 'alB', 'alM', 'alE','ئ'),
    # ARABIC LETTER ALEF
    'aaA': ('aa', '', '', 'aaE','ا'),
    # ARABIC LETTER BEH
    'baA': ('ba', 'baA', 'baM', 'baE','ب'),
    # ARABIC LETTER TEH MARBUTA
    'teeA': ('teE', '', '', 'teeE',''),
    'teeA': ('tee', '', '', 'teeE',''),
    # ARABIC LETTER TEH
    'taA': ('ta', 'taB', 'taM', 'taE','ت'),
    # ARABIC LETTER THEH
    'thA': ('th', 'thB', 'thM', 'thE','ث'),
    # ARABIC LETTER JEEM
    'jaA': ('ja', 'jaB', 'jaM', 'jaE','ج'),
    # ARABIC LETTER HAH
    'haA': ('ha', 'haB', 'haM', 'haE','ح'),
    # ARABIC LETTER KHAH
    'khA': ('kh', 'khB', 'khM', 'khE','خ'),
    # ARABIC LETTER DAL
    'daA': ('da', '', '', 'daE','د'),
    # ARABIC LETTER THAL
    'dhA': ('dh', '', '', 'dhE','ذ'),
    # ARABIC LETTER REH
    'raA': ('ra', '', '', 'raE','ر'),
    # ARABIC LETTER ZAIN
    'zaA': ('za', '', '', 'zaE','ز'),
    # ARABIC LETTER SEEN
    'seA': ('se', 'seB', 'seM', 'seE','س'),
    # ARABIC LETTER SHEEN
    'shA': ('sh', 'shB', 'shM', 'shE','ش'),
    # ARABIC LETTER SAD
    'saA': ('sa', 'saB', 'saM', 'saE','ص'),
    # ARABIC LETTER DAD
    'deA': ('de', 'deB', 'deM', 'deE','ض'),
    # ARABIC LETTER TAH
    'toA': ('to', 'toB', 'toM', 'toE','ط'),
    # ARABIC LETTER ZAH
    'zhaA': ('zha', 'zhaB', 'zhaM', 'zhaE','ظ'),
    # ARABIC LETTER AIN
    'ayA': ('ay', 'ayB', 'ayM', 'ayE','ع'),
    # ARABIC LETTER GHAIN
    'ghA': ('gh', 'ghB', 'ghM', 'ghE','غ'),
    # ARABIC LETTER FEH
    'faA': ('fa', 'faB', 'faM', 'faE','ف'),
    # ARABIC LETTER QAF
    'kaA': ('ka', 'kaB', 'kaM', 'kaE','ق'),
    # ARABIC LETTER KAF
    'keA': ('ke', 'keB', 'keM', 'keE','ك'),
    # ARABIC LETTER LAM
    'laA': ('la', 'laB', 'laM', 'laE','ل'),
    # ARABIC LETTER MEEM
    'maA': ('ma', 'maB', 'maM', 'maE','م'),
    # ARABIC LETTER NOON
    'naA': ('na', 'naB', 'naM', 'naE','ن'),
    # ARABIC LETTER HEH
    'heA': ('he', 'heB', 'heM', 'heE','ه'),
    # ARABIC LETTER WAW
    'waA': ('wa', '', '', 'waE','و'),
    # ARABIC LETTER ALEF MAKSURA
    'alA': ('al', '', '', 'alE','ى'),
    # ARABIC LETTER YAA
    'eeA': ('ee', '', '', 'eeE','ي'),
    # ARABIC LETTER YEH
    'yaA': ('ya', 'yaB', 'yaM', 'yaE','ي'),
    'laBaaE': ('laaa', '', '', 'laMaaE','لا'),
    'laBaeE': ('laae', '', '', 'laMaeE','لا'),
    'laBahE': ('laah', '', '', 'laMahE','لا'),
    # ARABIC LETTER HAMZA
    # ARABIC LETTER ALEF WITH HAMZA ABOVE
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'alB': ('alA', 'al', 'alM', 'alE','ئ'),
    # ARABIC LETTER BEH
    'baB': ('baA', 'ba', 'baM', 'baE','ب'),
    # ARABIC LETTER TEH
    'taB': ('taA', 'ta', 'taM', 'taE','ت'),
    # ARABIC LETTER THEH
    'thB': ('thA', 'th', 'thM', 'thE','ث'),
    # ARABIC LETTER JEEM
    'jaB': ('jaA', 'ja', 'jaM', 'jaE','ج'),
    # ARABIC LETTER HAH
    'haB': ('haA', 'ha', 'haM', 'haE','ح'),
    # ARABIC LETTER KHAH
    'khB': ('khA', 'kh', 'khM', 'khE','خ'),
    # ARABIC LETTER SEEN
    'seB': ('seA', 'se', 'seM', 'seE','س'),
    # ARABIC LETTER SHEEN
    'shB': ('shA', 'sh', 'shM', 'shE','ش'),
    # ARABIC LETTER SAD
    'saB': ('saA', 'sa', 'saM', 'saE','ص'),
    # ARABIC LETTER DAD
    'deB': ('deA', 'de', 'deM', 'deE','ض'),
    # ARABIC LETTER TAH
    'toB': ('toA', 'to', 'toM', 'toE','ط'),
    # ARABIC LETTER ZAH
    'zhaB': ('zhaA', 'zha', 'zhaM', 'zhaE','ظ'),
    # ARABIC LETTER AIN
    'ayB': ('ayA', 'ay', 'ayM', 'ayE','ع'),
    # ARABIC LETTER GHAIN
    'ghB': ('ghA', 'gh', 'ghM', 'ghE','غ'),
    # ARABIC LETTER FEH
    'faB': ('faA', 'fa', 'faM', 'faE','ف'),
    # ARABIC LETTER QAF
    'kaB': ('kaA', 'ka', 'kaM', 'kaE','ق'),
    # ARABIC LETTER KAF
    'keB': ('keA', 'ke', 'keM', 'keE','ك'),
    # ARABIC LETTER LAM
    'laB': ('laA', 'la', 'laM', 'laE','ل'),
    # ARABIC LETTER MEEM
    'maB': ('maA', 'ma', 'maM', 'maE','م'),
    # ARABIC LETTER NOON
    'naB': ('naA', 'na', 'naM', 'naE','ن'),
    # ARABIC LETTER HEH
    'heB': ('heA', 'he', 'heM', 'heE','ه'),
    # ARABIC LETTER YAA
    # ARABIC LETTER YEH
    'yaB': ('yaA', 'ya', 'yaM', 'yaE','ي'),
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'alM': ('alA', 'alB', 'al', 'alE','ئ'),
    # ARABIC LETTER BEH
    'baM': ('baA', 'baA', 'ba', 'baE','ب'),
    'taM': ('taA', 'taB', 'ta', 'taE','ت'),
    # ARABIC LETTER THEH
    'thM': ('thA', 'thB', 'th', 'thE','ث'),
    # ARABIC LETTER JEEM
    'jaM': ('jaA', 'jaB', 'ja', 'jaE','ج'),
    # ARABIC LETTER HAH
    'haM': ('haA', 'haB', 'ha', 'haE','ح'),
    # ARABIC LETTER KHAH
    'khM': ('khA', 'khB', 'kh', 'khE','خ'),
    # ARABIC LETTER SEEN
    'seM': ('seA', 'seB', 'se', 'seE','س'),
    # ARABIC LETTER SHEEN
    'shM': ('shA', 'shB', 'sh', 'shE','ش'),
    # ARABIC LETTER SAD
    'saM': ('saA', 'saB', 'sa', 'saE','ص'),
    # ARABIC LETTER DAD
    'deM': ('deA', 'deB', 'de', 'deE','ض'),
    # ARABIC LETTER TAH
    'toM': ('toA', 'toB', 'to', 'toE','ط'),
    # ARABIC LETTER ZAH
    'zhaM': ('zhaA', 'zhaB', 'zha', 'zhaE','ظ'),
    # ARABIC LETTER AIN
    'ayM': ('ayA', 'ayB', 'ay', 'ayE','ع'),
    # ARABIC LETTER GHAIN
    'ghM': ('ghA', 'ghB', 'gh', 'ghE','غ'),
    # ARABIC LETTER FEH
    'faM': ('faA', 'faB', 'fa', 'faE','ف'),
    # ARABIC LETTER QAF
    'kaM': ('kaA', 'kaB', 'ka', 'kaE','ق'),
    # ARABIC LETTER KAF
    'keM': ('keA', 'keB', 'ke', 'keE','ك'),
    # ARABIC LETTER LAM
    'laM': ('laA', 'laB', 'la', 'laE','ل'),
    # ARABIC LETTER MEEM
    'maM': ('maA', 'maB', 'ma', 'maE','م'),
    # ARABIC LETTER NOON
    'naM': ('naA', 'naB', 'na', 'naE','ن'),
    # ARABIC LETTER HEH
    'heM': ('heA', 'heB', 'he', 'heE','ه'),
    # ARABIC LETTER YEH
    'yaM': ('yaA', 'yaB', 'ya', 'yaE','ي'),
    # ARABIC LETTER HAMZA
    'hhE': ('hhA', '', '', 'hh','ء'),
    # ARABIC LETTER ALEF WITH MADDA ABOVE
    'amE': ('amA', '', '', 'am','آ'),
    # ARABIC LETTER ALEF WITH HAMZA ABOVE
    'aeE': ('aeA', '', '', 'ae','أ'),
    # ARABIC LETTER WAW WITH HAMZA ABOVE
    'wlE': ('wlA', '', '', 'Wl','ؤ'),
    # ARABIC LETTER ALEF WITH HAMZA BELOW
    'ahE': ('ahA', '', '', 'ah','إ'),
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'alE': ('alA', 'alB', 'alM', 'al','ئ'),
    # ARABIC LETTER ALEF
    'aaE': ('aaA', '', '', 'aa','ا'),
    # ARABIC LETTER BEH
    'baE': ('baA', 'baA', 'baM', 'ba','ب'),
    # ARABIC LETTER TEH MARBUTA
    'teeE': ('teeA', '', '', 'teE','ة'),
    'teeE': ('teeA', '', '', 'tee','ة'),
    # ARABIC LETTER TEH
    'taE': ('taA', 'taB', 'taM', 'ta','ت'),
    # ARABIC LETTER THEH
    'thE': ('thA', 'thB', 'thM', 'th','ث'),
    # ARABIC LETTER JEEM
    'jaE': ('jaA', 'jaB', 'jaM', 'ja','ج'),
    # ARABIC LETTER HAH
    'haE': ('haA', 'haB', 'haM', 'ha','ح'),
    # ARABIC LETTER KHAH
    'khE': ('khA', 'khB', 'khM', 'kh','خ'),
    # ARABIC LETTER DAL
    'daE': ('daA', '', '', 'da','د'),
    # ARABIC LETTER THAL
    'dhE': ('dhA', '', '', 'dh','ذ'),
    # ARABIC LETTER REH
    'raE': ('raA', '', '', 'ra','ر'),
    # ARABIC LETTER ZAIN
    'zaE': ('zaA', '', '', 'za','ز'),
    # ARABIC LETTER SEEN
    'seE': ('seA', 'seB', 'seM', 'se','س'),
    # ARABIC LETTER SHEEN
    'shE': ('shA', 'shB', 'shM', 'sh','ش'),
    # ARABIC LETTER SAD
    'saE': ('saA', 'saB', 'saM', 'sa','ص'),
    # ARABIC LETTER DAD
    'deE': ('deA', 'deB', 'deM', 'de','ض'),
    # ARABIC LETTER TAH
    'toE': ('toA', 'toB', 'toM', 'to','ط'),
    # ARABIC LETTER ZAH
    'zhaE': ('zhaA', 'zhaB', 'zhaM', 'zha','ظ'),
    # ARABIC LETTER AIN
    'ayE': ('ayA', 'ayB', 'ayM', 'ay','ع'),
    # ARABIC LETTER GHAIN
    'ghE': ('ghA', 'ghB', 'ghM', 'gh','غ'),
    # ARABIC LETTER FEH
    'faE': ('faA', 'faB', 'faM', 'fa','ف'),
    # ARABIC LETTER QAF
    'kaE': ('kaA', 'kaB', 'kaM', 'ka','ق'),
    # ARABIC LETTER KAF
    'keE': ('keA', 'keB', 'keM', 'ke','ك'),
    # ARABIC LETTER LAM
    'laE': ('laA', 'laB', 'laM', 'la','ل'),
    # ARABIC LETTER MEEM
    'maE': ('maA', 'maB', 'maM', 'ma','م'),
    # ARABIC LETTER NOON
    'naE': ('naA', 'naB', 'naM', 'na','ن'),
    # ARABIC LETTER HEH
    'heE': ('heA', 'heB', 'heM', 'he','ه'),
    # ARABIC LETTER WAW
    'waE': ('waA', '', '', 'wa','و'),
    # ARABIC LETTER ALEF MAKSURA
    'alE': ('alA', '', '', 'al','ى'),
    # ARABIC LETTER YAA
    'eeE': ('eeA', '', '', 'ee','ي'),
    # ARABIC LETTER YEH
    'yaE': ('yaA', 'yaB', 'yaM', 'ya','ي'),
    'laMaaE': ('laBaaE', '', '', 'laaa','لا'),
    'laMaeE': ('laBaeE', '', '', 'laae','لا'),
    'laMahE': ('laBahE', '', '', 'laah','لا'),
    
    'equ': ('...', '...', '...', '...','...'),
    'dot': ('.', '.', '.', '.','.'),
    'exc': ('!', '!', '!', '!','!'),
    'qts': ('?', '?', '?', '?','?'),
    'dbq': ('"', '"', '"', '"','"'),
    'com': ('،', '،', '،', '،','،'),
    'hyp': ('-', '-', '-', '-','-'),
    'col': (':', ':', ':', ':',':'),
    'brc': ('(', '(', '(', '(','('),
    'bro': (')', ')', ')', ')',')'),



    'ء': ('hhA', '', '', 'hhE','hh'),
    # ARABIC LETTER ALEF WITH MADDA ABOVE
    'آ': ('amA', '', '', 'amE','am'),
    # ARABIC LETTER ALEF WITH HAMZA ABOVE
    'أ': ('aeA', '', '', 'aeE','ae'),
    # ARABIC LETTER WAW WITH HAMZA ABOVE
    'ؤ': ('wlA', '', '', 'WlE','wl'),
    # ARABIC LETTER ALEF WITH HAMZA BELOW
    'إ': ('ahA', '', '', 'ahE','ah'),
    # ARABIC LETTER YEH WITH HAMZA ABOVE
    'ئ': ('alA', 'alB', 'alM', 'alE','al'),
    # ARABIC LETTER ALEF
    'ا': ('aaA', '', '', 'aaE','aa'),
    # ARABIC LETTER BEH
    'ب': ('baA', 'baB', 'baM', 'baE','ba'),
    # ARABIC LETTER TEH MARBUTA
    'ة': ('teeA', '', '', 'teeE','teE'),
    # ARABIC LETTER TEH
    'ت': ('taA', 'taB', 'taM', 'taE','ta'),
    # ARABIC LETTER THEH
    'ث': ('thA', 'thB', 'thM', 'thE','th'),
    # ARABIC LETTER JEEM
    'ج': ('jaA', 'jaB', 'jaM', 'jaE','ja'),
    # ARABIC LETTER HAH
    'ح': ('haA', 'haB', 'haM', 'haE','ha'),
    # ARABIC LETTER KHAH
    'خ': ('khA', 'khB', 'khM', 'khE','kh'),
    # ARABIC LETTER DAL
    'د': ('daA', '', '', 'daE','da'),
    # ARABIC LETTER THAL
    'ذ': ('dhA', '', '', 'dhE','dh'),
    # ARABIC LETTER REH
    'ر': ('raA', '', '', 'raE','ra'),
    # ARABIC LETTER ZAIN
    'ز': ('zaA', '', '', 'zaE','za'),
    # ARABIC LETTER SEEN
    'س': ('seA', 'seB', 'seM', 'seE','se'),
    # ARABIC LETTER SHEEN
    'ش': ('shA', 'shB', 'shM', 'shE','sh'),
    # ARABIC LETTER SAD
    'ص': ('saA', 'saB', 'saM', 'saE','sa'),
    # ARABIC LETTER DAD
    'ض': ('deA', 'deB', 'deM', 'deE','de'),
    # ARABIC LETTER TAH
    'ط': ('toA', 'toB', 'toM', 'toE','to'),
    # ARABIC LETTER ZAH
    'ظ': ('zhaA', 'zhaB', 'zhaM', 'zhaE','zha'),
    # ARABIC LETTER AIN
    'ع': ('ayA', 'ayB', 'ayM', 'ayE','ay'),
    # ARABIC LETTER GHAIN
    'غ': ('ghA', 'ghB', 'ghM', 'ghE','gh'),
    # ARABIC LETTER FEH
    'ف': ('faA', 'faB', 'faM', 'faE','fa'),
    # ARABIC LETTER QAF
    'ق': ('kaA', 'kaB', 'kaM', 'kaE','ka'),
    # ARABIC LETTER KAF
    'ك': ('keA', 'keB', 'keM', 'keE','ke'),
    # ARABIC LETTER LAM
    'ل': ('laA', 'laB', 'laM', 'laE','la'),
    # ARABIC LETTER MEEM
    'م': ('maA', 'maB', 'maM', 'maE','ma'),
    # ARABIC LETTER NOON
    'ن': ('naA', 'naB', 'naM', 'naE','na'),
    # ARABIC LETTER HEH
    'ه': ('heA', 'heB', 'heM', 'heE','he'),
    # ARABIC LETTER WAW
    'و': ('waA', '', '', 'waE','wa'),
    # ARABIC LETTER ALEF MAKSURA
    'ى': ('alA', '', '', 'alE','al'),
    # ARABIC LETTER YAA
    'ي': ('yaA', 'yaB', 'yaM', 'yaE','ya'),

    'لا': ('laBaaE', '', '', 'laMaaE','laaa'),

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
        print i
        if (i+1) > skip:
            letter = text[i]
            print letter
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

def arabizer(input_text,skip):
    output = []
    FORM = 1
    LETTER = 0
    NOT_SUPPORTED = -1
    text = input_text.split(' ')
    for i in range(len(text)):
        if (i+1) > skip:
            letter = text[i]
            if letter in LETTERS:
                output.append((letter, ARABIC))
            else: 
                output.append((letter, NOT_SUPPORTED))
            
        
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
    parser.add_argument('-a','--arabic', help='Write To Arabic', required=False)
    parser.add_argument('-s','--skip', help='Skip text entities for each line (For structured files)', required=False)
    args = vars(parser.parse_args())
    
    with open(args['file']) as f:
        content = f.readlines()
    f = open(args['file'] +".ctx", 'w')
    if args['skip']==None:
       skip=0
    else:
       skip=args['skip']
    if args['arabic']==None:
       arabic=False
    else:
       arabic=True
    for x in content:
        if arabic==False :
               f.write(reshape(x.replace("\n", " \n"),skip))
        else:
               f.write(arabizer(x.replace("\n", " \n"),skip).replace(" ", "").replace("sp", " "))
	
    f.close()
if __name__ == "__main__":
    main()
