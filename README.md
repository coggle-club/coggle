# coggle

## 项目介绍

## 模块与功能


## 开发流程

- 代码检查

```
pylint $(git ls-files '*.py')
```

- 单元测试

```
cd tests
pytest --cov ../
```

- 打包分发
```
$ python3 setup.py bdist_wheel sdist
$ twine upload dist/* --verbose
```

## 额外库

- SpaCy, https://spacy.io/models

```
https://mirror.coggle.club/pypi/zh_core_web_sm-3.7.0-py3-none-any.whl
https://mirror.coggle.club/pypi/zh_core_web_md-3.7.0-py3-none-any.whl

https://mirror.coggle.club/pypi/en_core_web_sm-3.7.1-py3-none-any.whl
https://mirror.coggle.club/pypi/en_core_web_md-3.7.1-py3-none-any.whl
```