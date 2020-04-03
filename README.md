# pdf2docx

- read PDF file with PyMuPDF
- parse text/image and format
- generate docx with python-docx


## Usage

### By range of pages
~~~
$ pdf2docx test.pdf test.docx --start=5 --end=10
~~~


### By page numbers
~~~
$ pdf2docx test.pdf test.docx --pages=5,7,9
~~~

~~~
NAME
    pdf2docx - Run the pdf2docx parser

SYNOPSIS
    pdf2docx INFILE OUTFILE <flags>

DESCRIPTION
    Run the pdf2docx parser

POSITIONAL ARGUMENTS
    INFILE
        PDF file to read
    OUTFILE
        Filename to write DOCX to

FLAGS
    --start=START
        First page to process, starting from zero
    --end=END
        Last page to process, starting from zero
    --pages=PAGES
        Range of pages

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
~~~


### To Markdown
~~~
$ DOC=test; pdf2docx $DOC.pdf $DOC.docx && pandoc -s $DOC.docx --wrap=none --reference-links -t markdown -o $DOC.md; cat $DOC.md
~~~


```python
import os
from pdf2docx.pdf2docx import Reader, Writer

pdf = Reader("file.pdf")
docx = Writer()

for page in pdf[0:5]:
	layout = pdf.parse(page)
	docx.make_page(layout)

docx.save("file.docx")
```
