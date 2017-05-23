from setuptools import setup

dependencies = ['pytest', 'pytest-cov']
extra_packages = {
    'testing': ['tox']
}

setup(
    name='Linked List',
    description="""Link List""",
    version='0.1',
    author='Sean Besseler, Carlos Cadena',
    author_email="seanwbesseler.gmail.com, cs.cadena@gmail.com",
    license="MIT",
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
      )
