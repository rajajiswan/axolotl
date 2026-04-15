# Copyright 2023 Axolotl contributors
# SPDX-License-Identifier: Apache-2.0

"""Axolotl - A tool for easily fine-tuning large language models.

This package provides utilities and tools for fine-tuning LLMs using
various techniques including LoRA, QLoRA, and full fine-tuning.
"""

import importlib.metadata
import logging

__version__ = importlib.metadata.version("axolotl")

logging.getLogger(__name__).addHandler(logging.NullHandler())
