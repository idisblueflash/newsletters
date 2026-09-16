---
slug: picture-the-word
title: 一张图看懂一个词
status: draft
mode: narrative
created: 2026-09-15
updated: 2026-09-15
tags: []
---

# 一张图看懂一个词

最近我在背单词。我看着单词的解释，其实没什么印象。就像是水从鸭子后背的羽毛上漫了过去，结果羽毛还是干的。

比如这个词：coordinate，在朗文字典里的解释是：

> to organize an activity so that the people involved in it work well together and achieve a good result.

我大概明白它说了啥，可脑子里还是模糊的。

但如果给出这张图就一目了然了吧：

[picture: coordinate]

这是用 Codex 生成的，每个例句都有配图。就算例句的文字你看不大懂，看到图之后，就能明白意思了。

我平时是这样用的：

get _cora on coordinate

Claude 会喊一个 agent 去做所有的流程，最后给我一个 3×3 的图片。

如果我有多个单词要做：

get multiple _cora on coordinate, critique, and bias.

它会并行地喊出三个 agent 同时去做。这样很省时，但是不能一次并行太多，它会很快吃掉我 Codex 5 小时的用量。
