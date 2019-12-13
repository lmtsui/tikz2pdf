# tikz2pdf
usage: 
```
python extract_tikz.py input_file output_file [--to_pdf=<bool>]
```

Options:
```
--to_pdf=<bool>                   compile tikz files to pdf[default: False]
```

extracts .tikz figures from input .tex file and output separated .tikz files for each tikz figure, along with a modified .tex file with each figure replaced by an \input{figure_name.tikz} statement or \includegraphics{figure_name} statement, depending on whether the to_pdf boolean flag.

More precisely, replaces every block in input .tex
```
\begin{tikzpicture}...
...
\end{tikzpicture}...
\label{figure_name}
```
by (if to_pdf is False)
```
\input{./figure/figure_name.tikz}
%\includegraphics{figure_name}
\label{figure_name}
```
or (if to_pdf is True)
```
%\input{./figure/figure_name.tikz}
\includegraphics{figure_name}
\label{figure_name}
```
and creates a new figurename.tikz file with contents:
```
\begin{tikzpicture}...
...
\end{tikzpicture}...
```
if to_pdf is True, will also call tikz2tex.sh script which runs pdf2latex to convert every .tikz file into a .pdf file, assuming WSL in windows
