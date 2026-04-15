# Copyright 2023 Axolotl contributors
# SPDX-License-Identifier: Apache-2.0

"""Axolotl - A tool for easily fine-tuning large language models.

This package provides utilities and tools for fine-tuning LLMs using
various techniques including LoRA, QLoRA, and full fine-tuning.

Personal fork notes:
- Using this fork for experimenting with custom LoRA configurations
- See configs/ directory for personal experiment configs
"""

import importlib.metadata
import logging

__version__ = importlib.metadata.version("axolotl")

# Set up a basic logger for the package; NullHandler avoids 'No handlers found' warnings
logging.getLogger(__name__).addHandler(logging.NullHandler())
