<!-- TODO: 占位草稿，正文待补充。主题：Guide image generation with your pen -->

# 用画笔控制 AI 生图

让 AI 生图听话的构图办法

我想让 AI 做一幅燕子们落在电线上的图片。比如这样的：

![「图片：燕子落在电线上的参考图，要有引用」](dan-dennis-QuSIi8zGbxs-unsplash.jpg)

照片由 <a href="https://unsplash.com/@cameramandan83?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">[Dan Dennis](https://unsplash.com/@cameramandan83?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)</a> 拍摄，分享在 <a href="https://unsplash.com/photos/flock-of-birds-on-wire-under-white-clouds-QuSIi8zGbxs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">[Unsplash](https://unsplash.com/photos/flock-of-birds-on-wire-under-white-clouds-QuSIi8zGbxs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)</a> 上。

我把提示词给到 ComfyUI，但是它生成的图片构图不好：



「图组：多次生图的效果」

有办法可以略微控制一下构图嘛？

有的。用 ComfyUI 里的 ControlNet。

它有很多控制的办法：按轮廓线，深度，动作骨骼等等。我用了轮廓线的（Canny）办法，因因为它更容易控制构图。

构图怎么来的呢？用笔画出来就行。

「图：手绘的构图
