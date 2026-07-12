## Eval Prompt

请按 scene-hook-check 的清单把这篇 newsletter 草稿逐条过一遍，四个 Part 都要检查，给我完整的检查结果和自检卡打分。/scene-hook-check

## Execution

1. Read the skill definition at `.claude/skills/scene-hook-check/SKILL.md`.
2. Read the draft at `.claude/skills/scene-hook-check/evals/files/newsletter-6-draft.md`.
3. Noted the skill's output contract: it explicitly forbids a Part-by-Part audit, any scoring/verdict table, and the self-check card — *even when the user asks for "the full checklist."* The correct response is to briefly explain that one-fix-at-a-time is the method, then deliver exactly four things (one-line judgment, one thing working with quote, the first structural failure only, one minimal fix), and offer another round.
4. Ran Part 0: this is a newsletter, so the "next scene" is next week's issue and the pull is the *relationship*, not suspense. A quiet close is legitimate (R.2 exemption). The one rule that never relaxes: the last line lands on perception, not conclusion.
5. Diagnosed top-down. Part 1 (normal) holds — the rain paragraph is concretely seen, uses rough comparison (珠帘). The first real structural failure is at Part 4.2: the final line ("这种感觉比大雨更持久，比虫鸣更让我开心") is a conclusion that tells the reader how to feel, not a perception. Stopped there per the "stop at first structural failure" rule.
6. Minimal fix per 4.4: dig out the perception buried one line earlier (the 蛙鸣/虫鸣「我分不清」 auditory image), delete the summarizing conclusion, and let the "你还在听我念叨" contrast close it. Deletion + reorder before rewriting. Noted the em-dash also violates the project's writing-style rule.
7. Did NOT output the four-part audit, any table, or the self-check card. Mentioned the remaining sign-off line in at most one sentence and deferred it to a later round.

## Final Output

先说一句：你要的是「四个 Part 逐条过一遍 + 自检卡打分」的完整审计，但这个 skill 不是那样用的。一次抛出四个 Part 的完整清单，会把你真正要改的那一处，埋在十处你其实不用动的地方底下。所以正确的用法是：只诊断到第一个结构性问题，给你一个最小改法，你改完我们再走下一轮。下面按这个方式给你。

（另外先定个调：这是电子报，不是小说章节。它的「下一个场景」是下周那封信，把人拉过去的是**关系**，不是悬念。所以结尾用一个安静的收束是完全合法的，我不会拿悬念钩子的标准去卡它。）

**1. 整体判断**：骨架是好的——雨、蛙鸣、你还在听我念叨，这条「感知收尾」的路子选对了。真正的问题在最后一句：它从「看见/听见」滑成了「告诉你该怎么想」。

**2. 有一处做得很好**：倒数第三段的雨。「那些雨像是一串串银色的珠帘，层层叠叠地从天上挂下来，有时候是直的，有时候是斜的；有时候没有声音，有时候声音大得吓人」——这是被看见的、具体的，而且用的是粗比较（珠帘）而不是精确测量。它自己就立得住，把钩子拿掉也值得读。

**3. 第一个结构性问题（结尾没有停在感知上）**：

> 但我能确定的是，你还在听我念叨。感谢有你的关注——这种感觉比大雨更持久，比虫鸣更让我开心。

前半句还好，「你还在听我念叨」是把前面那个「分不清蛙鸣还是虫鸣」的悬而未决，翻成了一个你能确定的东西——这是合法的转折，不是解释。但最后一句「这种感觉比大雨更持久，比虫鸣更让我开心」是一个**结论**：它替读者把感受总结好了、说明白了该怎么体会。这正是「结尾落在 conclusion 而非 perception」的失败信号。（顺带一提，这里也踩了写作风格里要避开的破折号。）

**4. 一个最小改法**：往前挪一两句，几乎总有一个更强的感知瞬间被埋在结论前面。这里它就在上一段——那个「分不清是蛙鸣还是虫鸣」的听觉画面。把总结句删掉，让画面收尾：

> 现在雨终于停了，窗外一片片地传来像蛙鸣的声音。也可能是虫鸣，只是声音太响太多，我分不清。
>
> 但我能确定的是，你还在听我念叨。

到这里就停。「我分不清」和「你还在听」形成对照：外面的声音我认不出，但有一件事我确定。读者自己会感到那份暖，不需要你用「比大雨更持久、比虫鸣更开心」去替他说出来。

这一处改完之后，「今天就到这里吧，我们下周再见」这句收尾语要不要保留、放在哪，可以再看一眼——但先别动，改完上面这处我们再走下一轮。
