#
# managers/mpich.py

from charms.operator_libs_linux.v0 import apt


class Manager:

    packages = [
        # "libmpich-dev",
        "libmpich12",
        # "libscalapack-mpich-dev",
        # "libscalapack-mpich2.1",
        "mpich",
        "mpich-doc",
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
