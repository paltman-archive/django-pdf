VERSION = (1, 0, 2)  # following PEP 386


def get_version():
    version = "%s.%s" % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    return version


__version__ = get_version()
