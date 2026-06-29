"""
Setup configuration for audiopy_ai package
"""

from setuptools import setup, find_packages

# Read the long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="audiopy_ai",
    version="0.1.6",

    author="Lalit Mohane, Adarsh Kotawar, Swaraj Nalawade, Kaiwalya Joshi",
    author_email="lalitmohane0275@gmail.com",

    description=(
        "A generalized Python library for audio editing and "
        "effects with AI-powered analysis, inspired by OpenCV."
    ),

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/AudioPy/audiopy_ai",

    project_urls={
        "Repository": "https://github.com/AudioPy/audiopy_ai",
        "Documentation": "https://github.com/AudioPy/audiopy_ai/blob/main/README.md",
        "Issues": "https://github.com/AudioPy/audiopy_ai/issues",
        "Source": "https://github.com/AudioPy/audiopy_ai",
    },

    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "examples",
            "examples.*",
        ]
    ),

    include_package_data=True,
    zip_safe=False,

    python_requires=">=3.9",

    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "soundfile>=0.10.0",
        "matplotlib>=3.4.0",
        "transformers>=4.20.0",
        "torch>=1.9.0",
        "torchaudio>=0.9.0",
    ],

    extras_require={
        "advanced": [
            "librosa>=0.9.0"
        ],
    },

    license="MIT",

    keywords=[
        "audio",
        "audio editing",
        "audio processing",
        "signal processing",
        "dsp",
        "ai",
        "speech recognition",
        "audio effects",
        "deep learning",
        "transformers",
        "whisper",
        "reverb",
        "equalizer",
    ],

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",

        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)