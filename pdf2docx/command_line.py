#!/usr/bin/python3
# -*- coding: utf-8 -*-

from docx import Document
from pdf2docx.pdf2docx import Writer, Reader

def parse(infile, outfile, start=0, end=None, pages=[]):
    pdf = Reader(infile)
    docx = Writer()
    pdf_len = sum(1 for x in pdf)
    if pages: 
        pdf_pages = [pdf[int(x)] for x in pages]
    else:
        end = end or pdf_len
        pdf_pages = pdf[int(start):int(end)]

    for page in pdf_pages:
        print(f"Processing {page}/{pdf_len-1}")
        layout = pdf.parse(page, debug=False)
        docx.make_page(layout)
    docx.save(outfile)

def main():
    import fire
    fire.Fire(parse)


if __name__ == '__main__':
    main()
