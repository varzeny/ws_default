from setuptools import setup

package_name = 'pkg_nodeModel'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='varzeny',
    maintainer_email='varzeny@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_publisher = pkg_nodeModel.node_publisher:main',
            'node_subscriber = pkg_nodeModel.node_subscriber:main'
        ],
    },
)
