from setuptools import setup, find_packages

setup(
    name="elpips",
    version="0.1.0",
    description="E-LPIPS metric for perceptual similarity evaluation.",
    author="Markus Kettunen",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "torch",
        "torchvision",
    ],
    include_package_data=True, 
)
