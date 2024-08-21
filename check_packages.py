import pkg_resources

required_packages = [
    'sqlalchemy==2.0.0',
    'python-dotenv==1.0.0'
]

installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

for package in required_packages:
    pkg_name, pkg_version = package.split('==')
    if pkg_name in installed_packages:
        if installed_packages[pkg_name] == pkg_version:
            print(f"{pkg_name}=={pkg_version} is installed.")
        else:
            print(f"{pkg_name} is installed but the version is {installed_packages[pkg_name]}, expected {pkg_version}.")
    else:
        print(f"{pkg_name} is not installed.")