import os.path as osp
from distutils.extension import Extension

import numpy as np
from Cython.Build import cythonize
from setuptools import find_packages, setup


def readme():
    with open("README.rst") as f:
        content = f.read()
    return content


def find_version():
    version_file = "torchreid/__init__.py"
    with open(version_file, "r") as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]


def numpy_include():
    try:
        numpy_include = np.get_include()
    except AttributeError:
        numpy_include = np.get_numpy_include()
    return numpy_include


ext_modules = [
    Extension(
        "torchreid.metrics.rank_cylib.rank_cy",
        ["torchreid/metrics/rank_cylib/rank_cy.pyx"],
        include_dirs=[numpy_include()],
    )
]


def get_requirements(filename="requirements.txt"):
    here = osp.dirname(osp.realpath(__file__))
    with open(osp.join(here, filename), "r") as f:
        requires = [line.replace("\n", "") for line in f.readlines()]
    return requires


setup(
    name="torchreid",
    version="1.0.2",
    description="Pytorch framework for deep-learning person re-identification",
    author="Kaiyang Zhou",
    author_email="k.zhou.vision@gmail.com",
    license="MIT",
    long_description=readme(),
    url="https://github.com/KaiyangZhou/deep-person-reid",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.17.4,<1.18.0",
        "Cython>=0.29.12,<0.30.0",
        "h5py>=2.10.0,<2.11.0",
        "Pillow>=6.0.0,<6.1.0",
        "six>=1.12.0,<1.13.0",
        "scipy>=1.3.0,<1.4.0",
        "opencv-python>=4.1.2,<4.2.0",
        "matplotlib>=3.1.0,<3.2.0",
        "tensorboard>=1.14.0,<1.15.0",
        "future>=0.17.1,<0.18.0",
        "yacs>=0.1.6,<0.2.0",
        "gdown>=3.8.3,<4.0.0",
    ],
    keywords=["Person Re-Identification", "Deep Learning", "Computer Vision"],
    ext_modules=cythonize(ext_modules),
)
