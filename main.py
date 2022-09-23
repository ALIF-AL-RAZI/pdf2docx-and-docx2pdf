from pdf2docx import Converter
from docx2pdf import convert
from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.geometry("630x500+400+100")
root.title("New PDF READER")
root.configure(bg="white")


def browse_file():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="select file",filetype=(("PDF File", ".pdf"), ("PDF File", ".PDF"),("DOCX file", ".docx")))


def pdfTOdocx():
    docx_file ="sample.docx"
    cv = Converter(file)
    cv.convert(docx_file)
    cv.close()


def docxTOpdf():
    convert(file)


Button(root, text="OPEN PDF", command=browse_file, width=10, font="arial 20", bg="orange", bd=4).place(x=10, y=100)
Button(root, text="CONVERT", command=pdfTOdocx, width=25, font="arial 20", bg="red",  bd=4).place(x=200, y=100)

Button(root, text="OPEN DOCX", command=browse_file, width=10, font="arial 20", bg="skyblue", bd=4).place(x=10, y=250)
Button(root, text="CONVERT", command=docxTOpdf, width=25, font="arial 20", bg="#2B65EC",  bd=4).place(x=200, y=250)

root.mainloop()