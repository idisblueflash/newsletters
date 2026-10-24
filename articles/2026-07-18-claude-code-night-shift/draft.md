---
slug: claude-code-night-shift
title: 凌晨三点，那行红字
status: ready         # draft → in-review → ready
mode: narrative
created: 2026-07-17
updated: 2026-07-20
tags: [claude-code, automation, personal-essay]
---

# 凌晨三点，那行红字

**你还在半夜指挥 AI 继续干活吗？**

上次 Meetup 里 R 说她经常半夜爬起来，看看 Claude 是不是卡住了。卡住了，就推它一把，让它接着跑。

我那时候心想：这怎么行啊！睡眠质量得下降多少啊！我才不会这么干呢。

几天后我又开了一个 Claude Pro 账户。

「多花的这 20 美金，总得充分利用。」我想。

别人贴了每天烧掉一个亿的 Token 截图，我看完也觉得有道理，就开始让 Claude Code 每次都跑满限额才停下。

有天凌晨三点，我起夜去洗手间。回来经过书桌，我想起有个任务卡在了限额上。我坐下来，在笔记本的 touch pad 上滑了一下，屏幕从锁屏里醒来，一句红色的英文停在下面：

*You've hit your session limit · resets 2:20pm (Asia/Shanghai)*

我又扫了一眼时间，抬起手，在键盘上敲出 continue，按下回车。

屏幕上开始一行行地冒英文。我呼出一口气，起身爬回床上。

---

这样的晚上不止一次。

更多时候我是在等。等那个还剩几十分钟的解禁点，手上干点这个，干点那个，时间一到，我就赶紧让它继续。

有时我在半夜里还要进入工作状态，弄明白 AI 的问题，替它拍板，让它能多跑一段。躺回床上，我的脑子里还会转着刚才的问题。一周下来，我的脑袋是懵的。

又有个晚上，我坐在电脑前，台灯还没开，荧幕特别亮。我看着表，等着那行红字消失。

「这怎么行啊！... 我才不会这么干呢。」

我突然想起了这句话。

---

等我把这件事想清楚，反倒是在真正闲下来之后了。

这五个小时的额度，本来就不是从午夜或者哪个整点开始算的，是从我发出第一条消息那一刻起算的[^1]。2:20pm、1:20pm、11:20pm，没有一次重样。它压根不是一个我能提前记住的钟点。

我盯着的其实不是这行红字什么时候变。是它还亮着的时候，我在不在电脑前。

我半夜不去守在电脑前，那 20 美金就像白花了一样。

我跑去问 Claude Code ：「怎么办？」

答案竟意外地简单：写一个脚本，隔几分钟去敲一次门。限额还没解开，敲一下就回来等着，几秒钟的事；解开了，它就真正开始干活，干完它自己会停，还会留下每一次敲门的日志。

这功能 Claude Code 还没有。GitHub 上有人提过好几次，到现在还晾着[^2]。

当然这脚本不能帮我拿主意，所以我尽可能把长任务提前准备好，晚上直接可以跑。

那晚我九点多离开电脑。第二天醒来，打开日志，最后一行是 `ALL_TASKS_DONE`。那一整夜，我睡我的，它忙它的。

---

这个脚本怎么写、怎么跑起来，我新写了一篇教程：《[别再半夜爬起来点「继续」：让 Claude Code 撞到限额后自己接着干](https://ai-companion-newsletter.beehiiv.com/p/claude-code-overnight-resume)》。一步一步照着做，做完它就能自己过夜：撞到限额自己等，解开了自己接着干，你睡你的。

[^1]: Claude 官方帮助中心的文章确认了「五小时会话额度」这件事本身，写明每五小时重置一次；「从发出第一条消息起算、不是固定钟点」这半句，现行官方页面没有逐字写出，由 Anthropic 2025 年公告的措辞、多篇独立整理文章，以及我自己几次实跑观测到的漂移重置时间（`6am`/`1:20pm`/`6:20pm`/`11:20pm`）共同佐证。<https://support.claude.com/en/articles/9797557-usage-limit-best-practices> · [存档](http://web.archive.org/web/20260715074201/https://support.claude.com/en/articles/9797557-usage-limit-best-practices)

[^2]: 「限额解开后自动继续」目前不是 Claude Code 自带的功能。在 anthropics/claude-code 的 GitHub 仓库里，「[FEATURE] Auto-continue after subscription rate limit resets」（#35744）截至写作时仍是 open 状态；另一条类似请求 #36320 被标记为重复并关闭。<https://github.com/anthropics/claude-code/issues/35744>

