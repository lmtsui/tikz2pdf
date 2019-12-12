# tikz2pdf
usage: python extract_tikz.py --in=<file> --out=<file>
  
extracts .tikz figures from input .tex file and output separated .tikz files for each tikz figure, along with a modified .tex file with each figure replaced by an \input statement

More precisely, replaces every block in input .tex
'''
\begin{tikzpicture}...
...
\end{tikzpicture}...
\label{figure_name}
'''
by
'''
\input{./figure/figure_name.tikz}
\label{figure_name}
'''
and creates a new figurename.tikz file with contents:
'''
\begin{tikzpicture}...
...
\end{tikzpicture}...
'''
usage: ./ tikz2tex.sh

runs pdf2latex to convert every .tikz file into a .pdf file, assuming WSL in windows
