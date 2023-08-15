from setuptools import setup, find_packages

setup(
    name="dspy-ai",
    version="2.0.0-alpha",
    description="DSPy",
    url="https://github.com/stanfordnlp/dsp",
    author="Omar Khattab",
    author_email="okhattab@stanford.edu",
    license="MIT License",
    packages=find_packages(include=['dsp', 'dspy']),
    python_requires='>=3.9',
    install_requires=[
        "backoff",
        "joblib",
        "jupyter",
        "openai",
        "pandas",
        "spacy",
        "regex",
        "ujson",
        "tqdm",
        "datasets",        
    ],
    classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
