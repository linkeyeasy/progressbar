# Progressbar
### A very simple python terminal progressbar

```Python
    import time

    from progressbar import ProgressBar

    # 初始化
    pb = ProgressBar()

    # 更新进度到80%
    pb.progress(percent=0.8)

    # 显示当前进度，并伴随消息
    pb.progress(percent=0.8, msg='blablabla...')

    # 一个从1 到 1000进度的显示过程，并伴有详细信息(为模拟进度过程用了0.01的sleep，实际使用中可以去掉time.sleep)
    for i in range(1, 1001):
        pb.progress(percent=float(i) / 1000, msg='app id -> %d' % i)
        time.sleep(0.01)
    time.sleep(2)
```
