# 长文转社群文案的自动化流程
一步一步搭出最小化流程

昨天在社群里看到小艺在问「如何把长文章自动转成 FB、Threads 等社交平台的文案」。有人回复说：「这是个很适合问 AI 的问题」。但我总觉得小艺看完还是没法下手。

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

## 我漏看了「自动化」三个字

第二天我打开帖子，没看到新回复。但我发现自己漏看了正文最后一句，小艺其实是想把这个流程做成自动化的。

上面的步骤已经够新人把文章转好了，社群里也有别人分享的自动化帖子我贴过去了。

很多新人一想到流程，脑子里就是一个按钮：点一下，文章进去，FB 贴出来。看别人演示 demo 时确实是这样，博主屏幕上几个文件夹、几行命令，三分钟跑完。但你自己打开终端，连 skill 装在哪个目录都不知道，那个按钮就消失了。

## 一步一步搭出最小化自动流程

这套流程要三样东西：一个 skill（从 prompt 转过来的）、一个 CLAUDE.md（告诉 Claude 啥时候自动触发）、一组 input/output 文件夹。

你说「帮我转一下 @input/xxx.md」，Claude Code 读 CLAUDE.md，知道要用 fb-maker skill，转完自动存进 output。

---

先把 prompt 做成 skill。你跟 Claude 说：「请帮我做成 skill，名叫 fb-maker」，然后从 Claude.ai 下载到自己电脑上。

创建一个目录叫做`leadpost-maker`，用`cd leadpost-maker` 进入这个目录，再输入`claude` 打开你的 Claude Code。

把刚才下载的 skill 拖到这个目录下，然后和 Claude 说：「请帮我安装 fb-maker Skill。」

装 skill 的同时，你可以把要转的文章放进一个叫 input 的文件夹里。

装好之后输入`/fb-maker-skill @input/when-extract-from-skill.md`，回车。屏幕上一条条往下吐：三个备选标题、正文、结尾 callback。

转好以后，接着说：「请把转好的内容存成 MD 格式，放在 output 文件夹下。」

打开 output 文件夹，里面多了一个 .md 文件。这就是半自动流程。

---

接着你可以说：「请把转换过程记在你的 CLAUDE.md 里。」

等它写好了，输入`/clear` 回车，清空上下文。我们再走一次流程。

说：「请帮我转一下 @input/when-extract-from-skill.md」

这时你可以看 Claude Code 自己怎么触发 skill，又怎么把结果自动存到 output 文件夹里。

这时你会发现一些不对劲的小地方。比如文件存到了根目录、备选标题被埋在文末。你就跟它说：

「你应该把文件自动存在 output 之下（请记住这一点）」

「请更新 fb-maker skill，让备选标题出现在最上面」

几个来回下来，你就有了一套最小化的自动流程。照这个套路也能把 Threads 加进去。然后跟 Claude 说：下次我让你转文章，把两个版本一起转出来。

就好了。

---

我把文件夹开源了，你可以在下面的 GitHub 仓库里看到 CLAUDE.md 是怎么写的、fb-maker 的 skill 文件，还有转出来的文件内容。

https://github.com/idisblueflash/leadpost-maker

完