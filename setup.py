from distutils.core import setup
setup(
    name='boundary',
    version='0.3.0',
    url="http://boundary.github.io/boundary-api-cli/",
    author='David Gwartney',
    author_email='davidg@boundary.com',
    packages=['boundary', ],
    scripts=[
      'bin/alarm-create',
      'bin/alarm-delete',
      'bin/alarm-get',
      'bin/alarm-list',
      'bin/alarm-update',
      'bin/action-installed',
      'bin/action-types',
      'bin/event-list',
      'bin/hostgroup-create',
      'bin/hostgroup-delete',
      'bin/hostgroup-get',
      'bin/hostgroup-list',
      'bin/hostgroup-search',
      'bin/hostgroup-update',
      'bin/measurement-create',
      'bin/measurement-get',
      'bin/metric-create',
      'bin/metric-create-batch',
      'bin/metric-delete',
      'bin/metric-export',
      'bin/metric-get',
      'bin/metric-import',
      'bin/metric-list',
      'bin/metric-markdown',
      'bin/metric-update',
      'bin/plugin-add',
      'bin/plugin-get',
      'bin/plugin-get-components',
      'bin/plugin-list',
      'bin/plugin-install',
      'bin/plugin-installed',
      'bin/plugin-readme',
      'bin/plugin-remove',
      'bin/plugin-uninstall',
      'bin/relay-list',
      'bin/relay-get-config',
      'bin/source-delete',
      'bin/source-list',
      'bin/user-get',
      'bin/user-get',
    ],
    package_data={'boundary': ['templates/*']},
    license='LICENSE.txt',
    description='Command line tools for using the Boundary REST APIs',
    long_description=open('README.txt').read(),
    install_requires=[
        "Pygments >=2.0.2",
        "python-dateutil >= 2.4.1",
        "requests >= 2.3.0",
        "jinja2 >= 2.7.3",
        "six >= 1.9.0",
    ],
)

