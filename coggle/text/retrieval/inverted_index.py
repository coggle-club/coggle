"""
Package: coggle
Author: finlay
Date: 2024
"""
from collections import defaultdict
from typing import List, Any, Union


class InvertedIndex:
    """InvertedIndex"""
    def __init__(self,
        doc_ids : Union[List[str], None] = None,
        documents : Union[List[List[str]], None] = None
    ) -> None:
        '''
        倒排索引

        参数:
        - doc_ids: 文档名称
        - documents: 文档内容
        '''
        self.total_size : int = 0
        self.invert_index : dict = defaultdict(List[int])
        self._doc_id_set : dict = defaultdict(List[str])

        if doc_ids is not None:
            if len(doc_ids) != len(documents):
                raise RuntimeError("the count of doc_ids do not math documents!")

            for doc_id, document in zip(doc_ids, documents):
                self.add_document(doc_id, document)

    def update_document(self, doc_id: Any, document: List[str]) -> bool:
        """
        更新文档

        参数:
          - doc_id: 文档名称
          - document: 文档内容

        返回: 是否更新成功
        """
        if doc_id not in self._doc_id_set:
            return False

        for term, doc_ids in self.invert_index.items():
            if doc_id in doc_ids:
                doc_ids.remove(doc_id)

        for term in document:
            self.invert_index[term].append(doc_id)

        self._doc_id_set[doc_id] = document
        return True

    def add_document(self, doc_id: Any, document: List[str]) -> bool:
        """
        添加文档
        
        参数:
          - doc_id: 文档名称
          - document: 文档内容

        返回: 是否更新成功
        """
        if doc_id in self._doc_id_set:
            raise RuntimeError("doc_id can not duplicate!")

        for term in document:
            if term not in self.invert_index:
                self.invert_index[term] = []
            self.invert_index[term].append(doc_id)

        self.total_size +=1
        self._doc_id_set[doc_id] = document
        return True

    def delete_document(self, doc_id: int) -> bool:
        """
        删除文档

        参数:
          - doc_id: 文档名称

        返回: 是否删除成功
        """
        if doc_id not in self._doc_id_set:
            return False

        for _, doc_ids in self.invert_index.items():
            if doc_id in doc_ids:
                doc_ids.remove(doc_id)

        del self._doc_id_set[doc_id]
        self.total_size -= 1
        return True

    def delete_term(self, term: str) -> bool:
        """
        删除term

        参数:
          - term: term名称

        返回: 是否删除成功
        """
        if term not in self.invert_index:
            return False

        del self.invert_index[term]
        return True

    def query(self, query: List[str]) -> List[Any]:
        """
        查询函数

        参数:
          - query: 待查询文档
          - top_n: 返回结果topn限制

        返回结果: 排序后检索结果，格式如 [(doc_id, score)]
        """
        query = set(query)
        result = None
        for term in query:
            if term in self.invert_index:
                if result is None:
                    result = set(self.invert_index[term])
                else:
                    result = result.intersection(self.invert_index[term])
            else:
                return []

        if result is None:
            return []

        return [(doc_id, self._doc_id_set[doc_id]) for doc_id in result]
