import os

idsf = 'protein_codes.txt'
fastas = 'allnts' # the dir with all nt genomes
out = 'el22_ntspy.fasta'

with open(idsf)as f:
    ids = set(line.strip() for line in f)

with open(out, 'w')as outf:
    for fasta in os.listdir(fastas):
        fastapath = os.path.join(fastas,fasta)
        with open(fastapath) as ff:
            lines = ff.readlines()
            i= 0
            while i<len(lines):
                line = lines[i].strip()
                if line.startswith('>'):
                    for prot_id in ids:
                        if prot_id in line:
                            outf.write('>' + prot_id + '\n')
                            for j in range(i+1,len(lines)):
                                if lines[j].startswith('>'):
                                    stop=j
                                    break

                            for k in range(i+1,stop):
                                outf.write(lines[k])
                            i = stop
                            break
                i+=1