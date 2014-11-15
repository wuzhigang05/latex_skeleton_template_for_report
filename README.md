#A Latex Skeleton template for producing professional report


##Requirements:
  * Latex engine. In Mac OS, I recommend [MacTex](https://tug.org/mactex/).

##How to use:
  
  ```bash
  make
  ```
  This will compile all the figures and references into one pdf called report.pdf.
Note that in order for above to work, in \*nix environment you need to replace 
'**open** $<' with '**xpdf** $<' because open behaves differently between Mac OS and 
\*nix environment. In Mac OS, when you type 'open report.pdf' it will open using 
Preview.app to open that pdf file. However, in \*nix environment, 'open' is a 
function to open a file.

Feel free to submit pull request to make this better.

##Contact:
  zhigang.wu@email.ucr.edu



