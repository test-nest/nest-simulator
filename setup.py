from disutils.core import setup

setup(
    name='PyNEST',
    version='@NEST_VERSION_VERSION@',
    description='PyNEST provides Python bindings for NEST',
    author='The NEST Initiative',
    url='http://www.nest-simulator.org',
    license='GPLv2+',
    packages=['nest', 'nest.tests', 'nest.tests.test_sp', 'nest.lib'],
    package_dir={'nest': '@PROJECT_SOURCE_DIR@/pynest/nest'},
    package_data={
        'nest': ['pynest-init.sli'],
        'nest.tests': ['test_aeif_data_lsodar.dat'],
    },
)
