# github-ci-python

通过`github actions`,自动将`python`代码, 打包`windows` 或 `macOS` 或 `linux`可执行文件

## pyinstaller注意事项
1. -w: macOS 和linux打包的时候, 不要加-w参数, windows加上此参数
2. --add-data: macOS和linux是`:`分隔, --add-data 'msyh.ttc:.', windows用`;`分隔,--add-data 'msyh.ttc;.'

## 常用命令

测试`github ci`的时候用

``` bash
git tag -d v1
git push origin :refs/tags/v1

git add .
git commit --amend --no-edit
git push origin main -f

git tag v1
git push origin v1


```