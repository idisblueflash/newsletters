# 你的Skill会被莫名其妙地召唤出来么？
skill-ch03-can-it-be-summoned-out-of-nowhere

你有没有碰到Skill会胡乱触发的情况？尤其是在你装了很多Skill之后。我装的Skill十个手指都能数得过来，所以我还没碰到，不过我们可以自己试着模拟一下。

任何Skill创建的时候都会采用「预设」触发方式。也就是说，你可以通过 /skill-name手动触发它，你的Claude也可以看聊天的意思，自动触发。

这就好比你去医院看病。如果你很清楚自己应该看哪科，你可以直接说「我要看牙科」（手动指定），但是有时候你不太明白要看哪一科，但是分诊台的护士能帮你决定。

「预设」触发的方式就是两个触发都开着，但是容易带来问题。

# 创建第一个skill：名词卡片

还是拿Anki建卡的例子来说。还记得我在做写作的作业嘛？每次要从一段文章里找出来名词，再从名词里找出来抽象名词，这是我的错题本：
```
今天练习里做错的两个词：
- 地方，具体名词，因为它指的是物理位置，能指向实体，只是没有给出名字。
- 夜，抽象名词，因为这是时间概念，看不到摸不到
```
| 考核名词 | 答案  | 理由                    |
| ---- | --- | --------------------- |
| 地方   | 具体  | 是物理位置，能指向实体，只是没有给出名字。 |
| 夜    | 抽象  | 是时间概念，看不到摸不到          |

```
请帮我设计一个叫做anki-abstract-noun的skill，它根据对话中的内容，找出练习的错误的抽象名词，并制作成Anki卡片。输出的格式可以参考：

| 考核名词 | 答案  | 理由                    |
| ---- | --- | --------------------- |
| 地方   | 具体  | 是物理位置，能指向实体，只是没有给出名字。 |
| 夜    | 抽象  | 是时间概念，看不到摸不到          |

保存成.csv文件
```

制作过程中，Claude Code会和你要「家目录」下的.claude/skills文件夹的访问权限。这是skill文件的默认存放位置。选择yes就可以。

> 你可能会注意到它不是在你的项目目录下的.claude/skills里创建的skill，而是这样的： /Users/husongtao/.claude/skills/anki-abstract-noun。在Mac OS下/Users/husongtao/是你的「家目录」。也就是你自己文件的存放路径，它下面可以有各种文件夹：Desktop、Downloads，你也可以创建一个Projects放你的多个Vibe coding项目。husongtao这是我登录自己Mac的用户名，你的会不一样，但是你肯定能认出来。
>
> Skill存放在这里，会对你在任何文件夹打开的Claude Code有作用。也就是说，每次你打开一个Claude Code这个skill就会被自动加载。

创建新skill的目录时，它还会找你要一次权限：
```
 Bash command

   mkdir -p ~/.claude/skills/anki-abstract-noun
   Run shell command

 Claude requested permissions to edit /Users/husongtao/.claude/skills/anki-abstract-noun which is a sensitive file.

 Do you want to proceed?
 ❯ 1. Yes
   2. Yes, and always allow access to skills/ from this project
   3. No

 Esc to cancel · Tab to amend · ctrl+e to explain
```
选1. Yes就行。下一个2. Yes，and always allow access to ... from this project是再说永远不要再问同样问题了。3. No是不要执行，通常你用不到。

> ~在Mac OS下是你的「家目录」的缩写，展开之后~/就代表着/Users/husongtao/。

这时候还有一个确认：
```
 Do you want to create SKILL.md?
 ❯ 1. Yes
   2. Yes, and allow Claude to edit its own settings for this session
   3. No

 Esc to cancel · Tab to amend
```
选1. Yes就行，因为要创建这个SKILL.md文件。第二个选择是允许Claude编辑它自己的settings。对于初学者我不推荐，因为Claude会替你做很多决定，而你却不知道。这样的话，后面碰到bug的时候，就很难排查。

现在Claude做好了新的Skill，你会看到类似这样的回复：
```
⏺ Skill 已经自动被识别到了（在 system-reminder 里能看到 anki-abstract-noun 已出现在列表中）。
  Skill 已创建完成，文件路径：~/.claude/skills/anki-abstract-noun/SKILL.md            **这个 skill 的工作方式：**

  触发词：说「生成 Anki 卡片」、「导出错题」、「保存复习卡片」或输入 /anki-abstract-noun
  
 执行逻辑：                                                                                                          
  1. 回溯对话，找出所有「抽象 vs 具体」判断练习 
  2. 筛选出用户答错的名词 
  3. 生成表格让你确认 

  考核名词,答案,理由                                                               
  地方,具体,"是物理位置，能指向实体，只是没有给出名字。"                                 
  夜,抽象,"是时间概念，看不到摸不到。"                                                

  4. 保存为 anki_abstract_noun_YYYYMMDD.csv（UTF-8 with BOM，Excel 直接打开不乱码）                                   
  **内置的判断标准也写进了 skill**
  里，包括几个常见混淆点（时间词、泛指地点、集合名词等），这样即使对话里没有明确标注对错，也能自动判断。            

✻ Cogitated for 1m 20s   
```

> .csv文件是Anki App接受的导入格式，你可以Anki的菜单File > Import里选中这个.csv文件，然后导入到你选中的deck里。

Skill创建完成后，我们用/exit命令退出Claude Code，再用claude命令进来。这样刚才新建的skill就激活了。

> 如果你想回来的时候，接着上面的上下文，你要用--resume开关。这个完整的命令回在你每次退出Claude Code的时候提示给你。你可以复制粘贴到命令行，再回车，就能回去了。比如我的是这样的： claude --resume 498b3f8f-4a88-4bb4-aab0-cc41e6e17615
>
> 如果你是在创建新的Skil，我推荐你不要这么做。直接claude命令进入。这样做你是从一个空的上下文对话开始，适合排除历史干扰，安全测试新创建的Skill。

让我们试试看这个skill。
```
今天练习里做错的两个词：
- 地方，具体名词，因为它指的是物理位置，能指向实体，只是没有给出名字。
- 夜，抽象名词，因为这是时间概念，看不到摸不到
  
@anki-abstract-noun
```

如果你能看到下面这个消息，就证明Skill被触发了。
```
 Skill(anki-abstract-noun)                 
  ⎿  Successfully loaded skill
```

你接着能看到它的回复:
```
⏺ 根据对话记录，两个错误题目如下：                  
  ┌──────────┬──────┬────────────────────────────────────────────────────────────────────────────────┐                
  │ 考核名词 │ 答案 │                                      理由                                      │                
  ├──────────┼──────┼────────────────────────────────────────────────────────────────────────────────┤                
  │ 地方     │ 具体 │ 指向物理空间中的实际位置，虽未命名但仍是可指向的实体，不能因"模糊"而归为抽象。 │              
  ├──────────┼──────┼────────────────────────────────────────────────────────────────────────────────┤
  │ 夜       │ 抽象 │ 是时间段的概念，无法通过感官触摸或指向某个实体，与"桌子""猫"等不同。           │                
  └──────────┴──────┴────────────────────────────────────────────────────────────────────────────────┘                

  正在生成 CSV 文件。 
```

因为要创建新的csv文件，它会再次和你要授权，选1. Yes就可以。如果你是正式在自己的练习中用，你会创建多个文件，也就需要多次确认。这个时候，为了方便，可以选 2。

它创建出来的csv的文件内容长这样：
```csv
考核名词,答案,理由
地方,具体,"指向物理空间中的实际位置，虽未命名但仍是可指向的实体，不能因「模糊」而归为抽象。"
夜,抽象,"是时间段的概念，无法通过感官触摸或指向某个实体，与「桌子」「猫」等不同。"
```
> CSV文件是普通的文本文件，只是后缀不是常见的txt或者md，而是csv。里面第一行是标题栏。剩下的每一行都是一条数据，这和我们上面的表格没有什么不同，只是用了`,`来做了分割。如果文字里有逗号，它还会用“”把整个文字包上，免得在不该分隔的地方隔开。

刚才我们是用/anki-abstract-noun这个命令，主动触发的。你也可以通过输入对话，让Claude按照情景触发：
```
生成Anki卡片
```
# 动词卡片skill
让我们再设计一个Skill，用来把查找错误的动词做成卡片。

我们这次可以说：请你参考 /anki-abstract-noun 设计一个anki-verb 的skill用来制作学生练习里漏掉的动词. 

Claude可能会找你澄清一些说法，比如卡片应该是什么样子的？你可以回答它：正面放句子,背面放找到的动词 。

之后同样会有一些对文件的操作需要你确认。保守的确认就是1. Yes。

这个skill创建完成后，我们同样要/exit退出，再claude进来。

# 胡乱触发

这时候如果你输入：`制作Anki卡片`，你只会看到anki-abstract-noun被调用，而anki-verb没有调用的情况。

这是因为两个的Description有明显的不同，所以Claude会选那个意思最相近的。

你如果打开两个SKILL.md对比着看，就能发现区别。

```
---
name: anki-abstract-noun
description: 从对话中找出用户判断错误的抽象名词练习题，生成 Anki 复习卡片并保存为 CSV 文件。当用户说"生成 Anki 卡片"、"导出错题"、"保存复习卡片"或"/anki-abstract-noun"时激活。
---

---
name: anki-verb
description: 从对话中找出学生在动词识别练习里漏掉的动词，生成 Anki 复习卡片并保存为 CSV 文件。当用户说"生成动词卡片"、"导出漏掉的动词"、"保存动词复习卡片"或"/anki-verb"时激活。
---
```

`制作Anki卡片`这个触发短语在anki-abstract-noun里高度一致，也没有在anki-verb里出现。

那么如果我们也把这个触发短语加入anki-verb，是不是就能把胡乱触发的效果复刻出来呢？结果是不太会。
```
⏺ 请问你想生成哪类 Anki 卡片？

  1. 抽象名词错题 (anki-abstract-noun) — 从练习中提取判断错误的抽象名词                 
  2. 动词识别漏题 (anki-verb) — 从练习中提取漏掉的动词
```

它没有猜，而是直接问你。

# 触发率
更重要的是触发率。就像上面那个例子，Claude会问你到底想用哪个？这样肯定不行。最好是我们说了，它就自动找到正确的skill。

650次受控实验发现，description的格式对触发率的影响，比大家想象的大多了。

以下面的数据为例：

| 格式                                    | 触发率       |
| ------------------------------------- | --------- |
| 被动式：Use when 。。。                      | 37-87.5%  |
| 加上更多关键词                               | 81.5-100% |
| 指令式：ALWAYS invoke。。。Do not X directly | 94.4-100% |

你可以按照这个推荐的模板提高你的触发率：
```
description: <Domain> expert. ALWAYS invoke this skill when the user asks about 
<trigger topics>. Do not <alternative action> directly — use this skill first.
```


---

未完待续

下集预告：居然存在不用触发的Skill？
