import subprocess
from os.path import dirname

# Getting taxa for query
params = snakemake.params

# Getting taxid lists
for k, v in params.items():
    taxlist = []
    for i in v:
        cmd = "get_species_taxids.sh -t {}".format(i)
        process = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        taxlist.append(process.stdout)
    with open(snakemake.output[k], "wt") as f:
        f.write("".join(taxlist))

