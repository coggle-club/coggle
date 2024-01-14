"""
coggle数据挖掘和人工智能项目最佳实践
"""
import nltk
nltk.download('punkt')

from . import dataset
from . import metrics
from . import utils
from . import text
from . import parser

__version__ = "0.1.0"

__all__ = [
    "dataset",
    "metrics",
    "utils",
    "text",
    "parser"
]
