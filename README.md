# ArabicTextContext

Python script to add position context to transcripted arabic text.

e.g. : 

No Context Text:  dh  he  ba  sp  na  wa  ha  sp  ma  zha  fa  ra  sp  de  ra  gh  aa  ma  sp  ba  sa  ha  ba  teE

With Context Text: dhA heA baA sp naA waA haA sp maA zhaA faA raA sp deA raA ghA aaA maA sp baA saA haA baA teeA 

Usage: run.py [-h] -f FILE [-s SKIP]
	-f : file containing n lines of arabic characters.
	-s : skip the x first character of each line in the file.

	
