"""Setup configuration for axolotl."""

from setuptools import find_packages, setup


def read_requirements(filename):
    """Read requirements from a file, ignoring comments and blank lines."""
    with open(filename, encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="axolotl",
    version="0.4.1",
    description="Tool designed to streamline the fine-tuning of AI models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="axolotl-ai-cloud",
    url="https://github.com/axolotl-ai-cloud/axolotl",
    license="Apache License 2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.36.0",
        "datasets>=2.14.0",
        "accelerate>=0.25.0",
        "peft>=0.7.0",
        "bitsandbytes>=0.41.0",
        "sentencepiece",
        "tokenizers>=0.15.0",
        "tqdm",
        "pyyaml",
        "addict",
        "fire",
        "colorama",
        "rich",
        "requests",
        "huggingface_hub",
        "einops",
        "evaluate",
        "scikit-learn",
        "optimum",
        "wandb",  # added for personal experiment tracking
        "matplotlib",  # added for plotting training curves locally
    ],
    extras_require={
        "flash-attn": [
            "flash-attn>=2.3.0",
        ],
        "deepspeed": [
            "deepspeed>=0.12.0",
        ],
        "mamba": [
            "mamba-ssm",
            "causal-conv1d",
        ],
        "galore": [
            "galore-torch",
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov",
            "pytest-xdist",
            "black",
            "isort",
            "pylint",
            "bandit",
            "pre-commit",
        ],
    },
    entry_points={
        "console_scripts": [
            "axolotl=axolotl.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
    zip_safe=False,
)
