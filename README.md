# Underscore
Are you sick of HR sending you word documents with file names full of spaces.
If so, then this is the script for you! Replace spaces with underscores in
file names to your hearts content with one simple command!

## Options:
* Without arguments renames all applicable files in the current work directory
* Alternatively you can give a list of file names as arguments to be renamed

## Installation:
Clone the repository and set up a soft link to your ~/bin directory.
```bash
> ln -s underscore.py ~/bin/underscore
```

## Example:
```bash
cave@glados$ ls -1
'HR1 This was a triumph.docx'
'HR2 Im making a note here.txt'
'HR3 Huge success.pdf'

cave@glados$ underscore
HR1 This was a triumph.docx -> HR1_This_was_a_triumph.docx
HR2 Im making a note here.txt -> HR2_Im_making_a_note_here.txt
HR3 Huge success.pdf -> HR3_Huge_success.pdf

cave@glados$ ls -1
HR1_This_was_a_triumph.docx
HR2_Im_making_a_note_here.txt
HR3_Huge_success.pdf
```

