import os

ncbicodesfile='hits_seqs.txt'
with open(ncbicodesfile,'r')as f:
    ncbicodes=[line.strip() for line in f]

fastadir='allaas'
outdir='aa_hit_seqs'

for filename in os.listdir(fastadir):
    if filename.endswith('.faa'):
        fastafile=os.path.join(fastadir,filename)
        outfile=os.path.join(outdir,filename)

        with open(fastafile,'r')as f:
            seqs=f.read().split('>')
        
        selected=[]
        for seq in seqs[1:]:
            header,seq=seq.split('\n',1)
            header_parts=header.split()
            ncbicode=header_parts[0]

            if ncbicode in ncbicodes:
                selected.append('>'+header+'\n'+seq)
        if selected:
            with open(outfile,'w')as f:
                f.write('\n'.join(selected))