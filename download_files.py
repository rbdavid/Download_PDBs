
from urllib import request
import sys

pdb_code = sys.argv[1].upper()
pdb_urls = 'https://files.rcsb.org/view/%s.pdb'
fasta_urls = 'https://www.rcsb.org/pdb/download/viewFastaFiles.do?structureIdList=%s&compressionType=uncompressed'

def download_url(url,extension):
    response = request.urlopen(url)
    response_str = str(response.read())
    response_list = response_str[2:-1].split('\\n')
    with open(pdb_code+'.'+extension,'w') as W:
        for line in response_list:
            W.write(line+'\n')

download_url(pdb_urls %(pdb_code),'pdb')
download_url(fasta_urls %(pdb_code),'fasta')

