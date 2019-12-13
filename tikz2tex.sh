for f in *.tikz; do 
    echo "\documentclass{standalone}"$'\n'"\usepackage{tikz}"$'\n'"\begin{document}"$'\n'$(cat $f) > ${f%.tikz}.tex ;
    echo $'\n'"\end{document}" >> ${f%.tikz}.tex;
    pdflatex.exe ${f%.tikz}.tex; done