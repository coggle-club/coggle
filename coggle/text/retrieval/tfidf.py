"""
Package: coggle
Author: finlay
Date: 2024
"""
from collections import defaultdict
from typing import List, Tuple, Any, Union

class TFIDF:
    """TFIDF"""
    def __init__(
        self,
        doc_ids : Union[List[str], None] = None,
        documents : Union[List[List[str]], None] = None
    ) -> None:
        self.total_size : int = 0
        self.invert_index : dict = defaultdict(List[int])
        self.idf : dict = defaultdict(float)

        self._doc_id_set : dict = defaultdict(List[str])
        self._up2date : bool = False

        if doc_ids is not None:
            if len(doc_ids) != len(documents):
                raise RuntimeError("the count of doc_ids do not math documents!")

            for doc_id, document in zip(doc_ids, documents):
                self.add_document(doc_id, document)

    def update_document(self, doc_id: int, document: List[str]) -> bool:
        """
        更新文档

        参数:
          - doc_id: 文档名称
          - document: 文档内容

        返回: 是否更新成功
        """
        if doc_id not in self._doc_id_set:
            return False

        for term, freq in self.invert_index.items():
            self.invert_index[term] = [(d_id, f) for d_id, f in freq if d_id != doc_id]

        term_frequency : dict = defaultdict(int)
        for term in document:
            term_frequency[term] += 1

        for term, freq in term_frequency.items():
            self.invert_index[term].append((doc_id, freq))

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
        term_frequency : dict = defaultdict(int)
        for term in document:
            term_frequency[term] += 1

        for term, freq in term_frequency.items():
            if term not in self.invert_index:
                self.invert_index[term] = []
            self.invert_index[term].append((doc_id, freq))

        self.total_size +=1
        self._doc_id_set[doc_id] = document
        self._up2date = False
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

        for term, freq in self.invert_index.items():
            self.invert_index[term] = [(d_id, f) for d_id, f in freq if d_id != doc_id]

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

    def _calculate_idf(self):
        for term, posting_list in self.invert_index.items():
            df = len(posting_list)
            self.idf[term] = 1 + (self.total_size / (1 + df))

    def query(self, query: List[str], top_n: int=10) -> List[Tuple[int, float]]:
        """
        查询函数

        参数:
          - query: 待查询文档
          - top_n: 返回结果topn限制

        返回结果: 排序后检索结果，格式如 [(doc_id, score)]
        """
        if not self._up2date:
            self._calculate_idf()
            self._up2date = True

        scores : dict = defaultdict(float)
        for term in query:
            if term in self.invert_index:
                idf = self.idf[term]
                for doc_id, tf in self.invert_index[term]:
                    scores[doc_id] += tf * idf

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        if top_n is not None:
            sorted_scores = sorted_scores[:top_n]
        return sorted_scores
