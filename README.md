# HPC Package Operators

This repository provides HPC package related charms:
* [hpc-apptainer](apptainer/README.md)
* [hpc-gpu-nvidia](gpu-nvidia/README.md)
* [hpc-infiniband](infiniband/README.md)
* [hpc-mpich](mpich/README.md)
* [hpc-nhc](nhc/README.md)
* [hpc-openmpi](openmpi/README.md)

These are subordinate charms that are meant to be used as part of an
HPC cluster (see [https://github.com/canonical/hpc-cluster]).

## To Build

Build (may need to run each `charmcraft` twice):

```
cd hpc-package-operators
for name in apptainer gpu-nvidia infiniband mpich openmpi nhc; do
    (cd ${name}; charmcraft -v pack)
done
```
