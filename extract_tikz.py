'''
Usage:
    extract_tikz.py <in_file> <out_file> [--to_pdf=<bool>]

Options:
    --to_pdf=<bool>                   compile tikz files to pdf[default: False]
'''
import re
import os
from docopt import docopt

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return content

def write_file(file_name,content):
    with open(file_name,'w') as f:
        for line in content:
            f.write(line)

def tikz_block_search(content):
    """
    @param content (list[str]): input tex file contents
    identify tikz blocks and extracts figure names from label
    @returns blocks_dict (dict): blocks_dict[begin tikz line no] = (end tikz line no, label of figure )
    """
    blocks_dict={}
    in_block = False #flag for being within a tikz block
    for i,line in enumerate(content):
        if '\\begin{tikzpicture}' in line:
            assert not in_block
            block_start = i
            in_block = True
        if '\\end{tikzpicture}' in line:
            assert in_block
            block_end = i
            in_block = False
            assert '\\label' in content[i+1] #assumes \label{XXX} immediately follows \end{tikzpicture} in the next line.
            block_label = re.search('label{(.+?)}',content[i+1]).group(1) #extracts figure name from \label{XXX}
            blocks_dict[block_start]=(block_end,block_label)
    return blocks_dict

def write_tikz(content,blocks_dict,to_pdf):
    """
    @param content (list[str]): input tex file contents
    @param blocks (dict): output dict of the form {block_start:(block_end,block_label)} from tikz_block_search
    @param to_pdf (bool): whether to compile tikz figures into pdf
    writes a .tikz file for each block
    @returns out (list[str]): output tex file contents
    """
    i=0
    out = []
    while i<len(content):
        if i in blocks_dict.keys(): #start of tikz block
            block_start = i
            block_end, block_label = blocks_dict[i]
            out.append(to_pdf*'%'+'\\input{'+block_label+'.tikz}\n')
            out.append((not to_pdf)*'%'+'\\includegraphics{'+block_label+'}\n')
            write_file(block_label+'.tikz', content[block_start:block_end+1])
            i = block_end +1
        else:
            out.append(content[i])
            i+=1
    return out

def main():
    args = docopt(__doc__)
    in_file_name = args['<in_file>']
    out_file_name = args['<out_file>']
    to_pdf = bool(args['--to_pdf'])
    content = read_file(in_file_name)
    blocks_dict = tikz_block_search(content)
    out = write_tikz(content,blocks_dict,to_pdf)
    write_file(out_file_name,out)
    if to_pdf:
        os.system('cmd /k "bash tikz2tex.sh"')

if __name__=='__main__':
    main()
