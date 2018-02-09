from distutils.core import setup, Extension

module = Extension("waveform", sources=["waveform.c"], libraries=['groove'])

setup(name="wfPackage", version="1.0", description="This is a package for waveform", ext_modules=[module])