from PyPDF2 import PdfMerger

merger = PdfMerger()

pdf_files = [
    "file1.pdf",
    "file2.pdf"
]

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

print("✅ PDFs merged successfully!")
print("Output File: merged.pdf")
