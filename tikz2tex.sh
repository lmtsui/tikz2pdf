for f in *.tikz; do 
    echo "\documentclass{standalone}"$'\n'"\usepackage{tikz}"$'\n'"\begin{document}"$'\n'$(cat $f) > $f.tex ;
    echo $'\n'"\end{document}" >> $f.tex;
    pdflatex.exe $f.tex; done

for f in *.tikz.pdf; do
    mv -- "$f" "${f%.tikz.pdf}.pdf"; done