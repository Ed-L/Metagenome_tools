#This script is from Dr. Adina Howe from Iowa State University.

#usage python count-up.py <blast output from metagenomes>

#!/usr/bin/python 

import sys

d_gene = {}

for f in sys.argv[1:]:
    for line in open(f):
        mg_id = f.split('.')[0]
        dat = line.rstrip().split('\t')
        gene = dat[1]
        if d_gene.has_key(gene):
            d_gene[gene][mg_id] = d_gene[gene].get(mg_id,0) + 1
        else:
            d_gene[gene] = {}
            d_gene[gene][mg_id] = 1

fp = open('summary-count.tsv', 'w')

sorted_samples = sys.argv[1:]

