# 长文转社群文案的自动化流程
一步一步搭出最小化流程

昨天在社群里看到小艺在问「如何把长文章自动转成 FB、Threads 等社交平台的文案」。有人回复说：「这是个很适合问 AI 的问题」。我总觉得小艺可能还是没法下手。

> 贴长文给 AI，问：
>
> 「帮我转 Facebook 引流贴。」
>
> 多调几轮，满意后让它：
>
> 「存成提示词，用 Markdown 格式，方便我下载，以后直接用。」
>
> 下次有新文章，两个文件一起贴过去。
>
> PS：在 Claude.ai 上测试通过。

## 「自动化」被我漏掉了

第二天我打开帖子，还是没有看到新的回复。但我发现漏掉了正文最后一句，小艺想把这个流程做成自动化的。

上面的步骤已经能让新人把文章转换好了，我也贴了社群里别人分享的自动化帖子。

很多新人想到一个流程的时候，都会幻想着按下一个按钮，那套流程就跑完了。我们看别人 demo 的时候是这样的，但他们在 5 分钟之内没办法把每一个细节讲清楚。

## 一步一步搭出最小化自动流程

一个 skill（从 prompt 转过来的）、一个 CLAUDE.md（告诉 Claude 啥时候自动触发）、一组 input/output 文件夹。

你说「帮我转一下 @input/xxx.md」，Claude Code 读 CLAUDE.md，知道要用 fb-maker skill，转完自动存进 output。

prompt 不沉淀成 skill，每次都要重贴，一点也不自动；skill 不写进 CLAUDE.md，每次都要手动敲 /fb-maker；没有 input/output 约定，文件就会越堆越多，最后很难找。

---

上面说到了生成 prompt，接下来最好把它做成 skill。你可以和 Claude 说：「请帮我做成 skill，名叫 fb-maker」然后从 Claude.ai 下载回自己的电脑。

创建一个目录叫做`leadpost-maker`，用`cd leadpost-maker` 进入这个目录，再输入`claude` 打开你的 Claude Code。这时 Claude 就能看到这个文件夹下的所有文件了。

把刚才下载的 skill 拖到这个目录下，然后和 Claude 说：「请帮我安装 fb-maker Skill。」

在安装 skill 的过程中 ，你可以把你要转化的文章放在一个叫 input 的文件夹里。比如，我放进了一篇`when-extract-from-skill.md` 。

安装好之后输入`/fb-maker-skill @input/when-extract-from-skill.md`，他会和在 [Claude.ai](http://Claude.ai) 一样把文章转好。

转好以后，接着说：「请把转好的文件存成 MD 格式，放在 output 文件夹下。」

一套半自动的流程就有了。

接着你可以说：「请把转换过程记在你的 CLAUDE.md 里。」

等他写好了，输入`/clear` 回车，清空上下文。我们再模拟一次转化的流程。

然后说：「请帮我转一下 @input/when-extract-from-skill.md」

这时你可以观察 Claude Code 是怎么自己触发 skill、又如何自动地把结果存在 output 文件夹之下的。

如果发现它有做得不对的地方，你可以随时纠正，比如：

「你应该把文件自动存在 output 之下（请记住这一点）」

「请更新 fb-maker skill，让备选标题出现在最上面」

几个来回之后，你就有了一个最小化的自动流程。你也可以按照这个流程把 Threads 加进去，只是多一个 skill。然后你可以让 Claude 记住：下次我说要转化文章的时候，把两个版本同时转出来。

就好了。

---

我们把这个流程的文件夹开源了，你可以在下面的 GitHub 仓库里看到 CLAUDE.md 文件是怎么写的，fb-maker 的 skill 文件，还有转化出来的文件内容。

https://github.com/idisblueflash/leadpost-maker

完