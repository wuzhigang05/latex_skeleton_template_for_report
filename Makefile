texFiles = $(wildcard *tex)
bibFiles = $(wildcard *bib)
figures = $(wildcard *pdf)

srcFiles = $(texFiles) $(bibFiles) $(figures)

fileName = "report"

open: $(fileName).pdf
	open $<


$(fileName).pdf: $(srcFiles)
	pdflatex $(fileName); bibtex $(fileName); pdflatex $(fileName); pdflatex $(fileName);


clean:
	rm -rf $(fileName) $(fileName).{aux,bbl,blg,lof,log,lot,pdfsync,wsp,toc,out}


# sloppy alias
c:
	rm -rf $(fileName) $(fileName).{aux,bbl,blg,lof,log,lot,pdfsync,wsp,toc,out}

o: $(fileName).pdf
	open $<



