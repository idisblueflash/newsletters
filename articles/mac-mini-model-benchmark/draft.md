# Mac Mini 生图模型测试

我把大概测试目的- 品质和速度，提了一下。

这次测试的本地生图模型是四个：Juggernaut SD1.5, Z-Image-Turbo, Flux Schnell 和 SD3.5 Medium。

我重点提醒 Claude 的是：模型第一次有加载时间(cold）所以要多生两次图片，才能记录没有加载模型的速度（warm）。

Claude 生成了一份仔细的计划，连多个模型之间的接力顺序都想好了，挺不错。我让他把这份计划存成 markdown 文件，然后清空对话框，开始测试。

其实我不知道他跑完所有测试用了多久。四个模型每个四张，有 16 张要生成。我后面去理发了，回来的时候它已经完成了，还有一份报告：

![机器人主题测试评分表](assets/robot-test-table.jpg)

![四模型机器人主题生图对比](assets/grid-robot.jpg)

Juggernaut 是 baseline，所以先不用看。 SD3.5 又慢又差，也排除掉。Z-Image-Turbo 首选，因为我对图片质量要求高。Flux Schnell 可以用来生成草稿。

这次生图的主题是机器人的，我平时的图是有人物和动作的。所以我又让 Claude 再跑了一次。这次换成了印第安纳·琼斯的动作图。报告是这样的：

![印第安纳·琼斯主题测试评分表](assets/indy-test-table.jpg)

![四模型印第安纳·琼斯主题生图对比](assets/grid-indy.jpg)

在机器人的图上，我只能看出精细程度，所以我完全信任 Claude 的评分了。这次有些不同，人物动作的图片看一眼就能分出好坏。

这两组测试下来，我已经知道 Z-Image-Turbo 是最后的选择了，哪怕会慢一点。
