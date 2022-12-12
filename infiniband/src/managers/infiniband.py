#
# managers/infiniband.py

from charms.operator_libs_linux.v0 import apt
from charms.operator_libs_linux.v1 import systemd


class Manager:

    packages = [
        "dapl2-utils",
        "ibacm",
        "ibsim-utils",
        "ibutils",
        "ibverbs-providers",
        "ibverbs-utils",
        "infiniband-diags",
        # "libdapl-dev",
        "libdapl2",
        # "libibdm-dev",
        "libibdm1",
        # "libibmad-dev",
        "libibmad5",
        # "libibnetdisc-dev",
        "libibnetdisc5",
        # "libibumad-dev",
        "libibumad3",
        # "libibverbs-dev",
        "libibverbs1",
        # "libopensm-dev",
        "libopensm9",
        "libosmcomp5",
        "libosmvendor5",
        "libpgm-5.3-0",
        # "libpgm-dev",
        # "librdmacm-dev",
        "librdmacm1",
        "libumad2sim0",
        "libvma",
        # "libvma-dev",
        "libvma-utils",
        "libvma9",
        "opensm",
        "opensm-doc",
        "pcp-pmda-infiniband",
        "perftest",
        "rdma-core",
        "rdmacm-utils",
        "srptools",
    ]

    def __init__(self):
        pass

    def configure(self):
        pass

    def install(self):
        if self.packages:
            apt.update()
            for name in self.packages:
                apt.add_package(name)

    def is_installed(self):
        if self.packages:
            for name in self.packages:
                try:
                    if not apt.DebianPackage.from_installed_package(name).present:
                        return False
                except:
                    return False
        return True
