from setuptools import setup
from woniurobotv3 import app
# setup(
#     name='woniurobotv3',
#     packages=['woniurobotv3'],
#     include_package_data=True,
#     install_requires=[
#         'flask',
#     ],
# )
from woniurobotv3.indexview import index

if __name__ == '__main__':
    app.run(debug=True)