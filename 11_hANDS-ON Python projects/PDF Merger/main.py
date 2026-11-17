from PyPDF2 import PdfWriter

merger = PdfWriter()
PDFS=[]
try:
    n=int(input("How many pdfs do you want to merge?\n"))
    for i in range(n): # Collect the all pdf
        name=input(f"Enter the name of pdf {i+1} :")
        PDFS.append(name)

    for pdf in PDFS:#merge the all pdf
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()
except Exception as e:
    print("Some error Occers",e)