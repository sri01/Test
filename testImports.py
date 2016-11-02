""" List the modules in a given package"""

def method_1():
    """ Module "imp" showing as depricated in 3.x using pycharm
    """
    import imp
    import os
    MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

    def package_contents(package_name):
       # file, pathname, description = imp.find_module(package_name)
       file, pathname, description = imp.find_module(package_name)
       if file:
           raise ImportError('Not a package: %r', package_name)
           # Use a set because some may be both source and compiled.
           return set([os.path.splitext(module)[0]
       for module in os.listdir(pathname)
           if module.endswith(MODULE_EXTENSIONS)])

    package_contents("paramiko")

def method_2():
    import paramiko
    from paramiko.sftp_client import SFTPClient
    print(dir(SFTPClient))
    print([module_name for module_name in dir(SFTPClient) if not module_name.startswith("__")])


def main():
    method_1()
    #method_2()

if __name__ == '__main__':
    main()