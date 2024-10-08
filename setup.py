from setuptools import find_packages, setup

package_name = 'd1_state_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yamaguchi-a',
    maintainer_email='yamaguchi-a@roboken.iit.tsukuba.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'd1_state_publisher = d1_state_publisher.d1_state_publisher:main'
        ],
    },
)
