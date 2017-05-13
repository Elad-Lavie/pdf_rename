from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
import sys
def main(path, new_name):
	inpfn = path
	fin = file(inpfn, 'rb')
	pdf_in = PdfFileReader(fin)
	writer = PdfFileWriter()
	for page in range(pdf_in.getNumPages()):
		writer.addPage(pdf_in.getPage(page))
	infoDict = writer._info.getObject()
	info = pdf_in.documentInfo
	for key in info:
		infoDict.update({NameObject(key): createStringObject(info[key])})
	# rename
	infoDict.update({NameObject('/Title'): createStringObject(unicode(new_name))})
	# It does not appear possible to alter in place.
	fout = open(inpfn+'out.pdf', 'wb')
	writer.write(fout)
	fin.close()
	fout.close()

	import os
	os.unlink(inpfn)
	os.rename(inpfn+'out.pdf', inpfn)
	#Finally, we can see we successfully modified the file.

if __name__ == "__main__":
	main(sys.argv[1],sys.argv[2])