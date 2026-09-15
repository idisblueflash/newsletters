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

你已经知道我在背单词了，你是不是会看到一些单词的解释，但是对它没什么感觉呢，就像我一样？

比如这个词：coordinate，在朗文字典里是这样解释的：

> to organize an activity so that the people involved in it work well together and achieve a good result.

你能大概明白它说了啥，可脑子里还是模糊的。

但如果给你这张图片就一目了然了吧：

[picture: coordinate]

这是用 Codex 生成出来的图片，每个例句都有生动的配图。就算例句的文字你看不大懂，但是看到图之后，就能明白了。

我平时是这样用的：

get_cora on coordinate

它会下发一个 agent 去做所有的流程，最后给我一个 3×3 的图片。

如果我有多个单词要做：

get multiple _cora on coordinate, critique, and bias.

它会并行地下发三个 agent 同时去做。这样会很节省时间，但是不能一次并行太多，它会很快吃掉我 Codex 的 5 小时用量。
