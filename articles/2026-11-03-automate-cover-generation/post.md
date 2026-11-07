# 做一顿午饭的工夫，助手 Jenny 替我把封面图跑完了

我做一顿午饭的工夫，文章的封面图做好了。

中间我一次都没回电脑前看。

## 以前怎么配图

我一周写两三篇文章，每篇要配一张封面。用的是本地的生图软件 ComfyUI，三个工作流：文生图、扩大画面、转换风格。

每一步都是一个套路：把 AI 写好的提示词粘进去，一次排满五个任务。我的 Mac mini 上生一张图大概 3 分钟，二十分钟后再回来挑一张，排下一步。

一套跑完要近五十分钟，还没算上选图、调图的时间。

每次文章还没写，配图已经让我头大了。

## 交给 Jenny

今天，我把这活交给 AI 了。

我和 Claude Code 说，你看，这三个工作流是我平时用的，你建个助手帮我干了吧。可以叫她 Jenny。

它三下五除二把 Jenny 建出来了。我把提示词存成文件，Jenny 自己跑那三个流程：自己选图、扩图、换样式。

拿一篇要配河狸修水坝的文章试手。Jenny 接过活开始忙，我起身去厨房炒菜。

等菜炒完了，锅也刷干净了，我才想起 Jenny。屏幕上静静地开着一幅尺寸正确、和以前封面风格相近的图：一只河狸蹲在泥巴堆起的小坡上，手里拿着一节树枝，直愣愣地瞪着镜头。

这顿午饭做得真踏实。

算下来用时和以前差不多，可中间那几趟来回全省了。

## 河狸站在了正中间

不过河狸在图的正中，看着堵心。Jenny 不知道主角应该放边上，画面才有透气感。

解法嘛，就是写进 Jenny 的说明书。我让 Claude Code 更新 Jenny，她每次生图前都会先读一遍说明书。现在讲构图的那段长这样：

```markdown
**Composition: rule of thirds, not centre.** The subject goes on the left third
(x = 480) or the right third (x = 960) of the 1440×720 frame; the open side shows
the scene the subject belongs to (the dam it is mending, the road it is walking).

- The subject faces or moves towards one side → put it on the opposite third,
  so it looks into the open space.
- The subject faces the camera → the right third by default.
```

吃过午饭，刷完碗，我回来再看，Jenny 已经重画好了。河狸站到了右边，眼神看向左边刚修好的水坝。

这样的要点再多几十条也不叫事儿。记在我脑子里的，多了肯定记不全；写进说明书里的，才稳当。

我当个监工挺好，细节让 Jenny 去跑。

不过那天切菠菜心的时候，我才想明白，真正该交给 Jenny 的是什么。

你手上有没有哪件重复的活，也想建个像 Jenny 这样的助手整个接过去？🤔

> 完整版在这里：[炒菜的功夫，AI 把封面做好了](https://ai-companion-newsletter.beehiiv.com/p/hand-cover-image-pipeline-to-ai-subagent)
