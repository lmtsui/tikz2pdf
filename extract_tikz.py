'''
Usage:
    extract_tikz.py --in=<file> --out=<file>

Options:
    --in=<file>                       input tex file name
    --out=<file>                      output tex file name
'''
import re
from docopt import docopt

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return content

def write_file(file_name,content):
    with open(file_name,'w') as f:
        for line in content:
            f.write(line)

def chunk_search(content):
    """
    @param content (list[str]): input tex file contents
    output: chunks (dict): chunk[begin tikz line no] = (end tikz line no, label of figure )
    """
    chunks={}
    for i,line in enumerate(content):
        if '\\begin{tikzpicture}' in line:
            chunk_start = i
        if '\\end{tikzpicture}' in line:
            chunk_end = i
        if '\\label' in line:
            chunk_label = re.search('label{(.+?)}',line).group(1)
            chunks[chunk_start]=(chunk_end,chunk_label)
    return chunks

def write_tikz(content,chunks):
    """
    @param content (list[str]): input tex file contents
    @param chunks (dict): output dict from chunk_search
    writes a .tikz file for each chunk,
    outout: out (list[str]): output tex file contents
    """
    i=0
    out = []
    while i<len(content):
        if i in chunks.keys():
            chunk_start = i
            chunk_end, chunk_label = chunks[i]
            out.append('\\input{./figure/'+chunk_label+'.tikz}\n')
            write_file(chunk_label+'.tikz', content[chunk_start:chunk_end+1])
            i = chunk_end +1
        else:
            out.append(content[i])
            i+=1
    return out

def main():
    args = docopt(__doc__)
    in_file_name = args['--in']
    out_file_name = args['--out']
    # to_pdf = args['--compile_to_pdf']
    content = read_file(in_file_name)
    chunks = chunk_search(content)
    out = write_tikz(content,chunks)
    write_file(out_file_name,out)

if __name__=='__main__':
    main()
