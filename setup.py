"""
Setup configuration for audiopy_ai package
"""

from setuptools import setup, find_packages

# Read the long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="audiopy_ai",
    version="0.1.5",
    author="Adarsh Kotawar",
    author_email="adarshkotawar@gmail.com",
    description="A generalised Python library for audio editing and effects with AI-powered analysis, inspired by OpenCV.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AudioPy/AudioPy",
    project_urls={
        "Repository": "https://github.com/AudioPy/AudioPy.git",
        "Documentation": "https://github.com/AudioPy/AudioPy/blob/main/README.md",
        "Issues": "https://github.com/AudioPy/AudioPy/issues",
        "Changelog": "https://github.com/AudioPy/AudioPy/releases",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
    ],
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
        "advanced": ["librosa>=0.9.0"],
    },
    license="MIT",
    keywords=[
        "audio",
        "dsp",
        "signal-processing",
        "ai",
        "speech-recognition",
        "audio-editing",
        "audio-effects",
        "huggingface",
        "transformers",
        "whisper",
        "deep-learning",
        "reverb",
        "equalizer",
    ],
    include_package_data=True,
    zip_safe=False,
)
