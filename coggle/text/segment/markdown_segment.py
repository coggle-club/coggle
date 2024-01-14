"""
Package: coggle
Author: finlay
Date: 2024
"""
from typing import Union, List


class MarkdownSegment:
    """MarkdownSegment"""
    def __init__(
        self,
        chunk_size: int = 30,
        chunk_overlap: int = 0,
        separator: Union[str, None] = None,
        language: Union[str, None] = None
    ):
        raise NotImplementedError("Unsupported in MarkdownSegment.")

    def segment(self, document: str) -> List[str]:
        """
        将文档切分成块，按照预定的块大小和重叠大小

        参数:
        - document: 输入的文档字符串

        返回:
        - 切分后的文档块列表
        """
        raise NotImplementedError

    def __call__(self, document: str) -> List[str]:
        return self.segment(document)
