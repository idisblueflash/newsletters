---
title: "The First Fix"
subtitle: "What my taste is good for when I build with a code agent"
date: 2026-10-15
tags: [claude-code, ai-collaboration, taste, plugin-design]
source_notes: notes/claim-taste-problem-finder.md
status: draft
---

# The First Fix

There's a common belief about working with a code agent: think the solution through,
write it down clearly, and let the agent build it. You're the architect; it's the
builder. I believed it too. When something looked wrong, I'd arrive with the fix
already in mind.

My answer now: my taste finds the problem, and the agent is often better at the fix.
By taste I mean the gut sense that something is off, which I get while using what we
built. The agent holds more of the project's context. In my experience, this holds at
least when the problem touches several parts of a plugin.

## One small sentence

I'm building a Claude Code plugin called *reading*. It helps me read papers. Each
concept I meet gets a card with a **Meaning** section, and a map page shows the cards
next to the text.

One morning I was reading this card:

> **C-031 Diagnostic test**
> **Meaning:** A procedure that tells whether a patient has a disease, when the patient
> is already suspected of having it. Examples are a laboratory measurement and a
> radiological image. The essay does not define the term; this is the standard meaning.

The last sentence bothered me. It isn't part of the meaning. It's a note about where
the meaning came from. My fix was quick: move it into its own paragraph, in a small
font.

The agent agreed with the problem and disagreed with the fix. It had looked at the map's
code. The sentence wasn't only on the card. It also showed up in the hover tooltip on
every link to the term, and in the concept list. So this wasn't a styling problem. It
suggested a data field instead, `defined: no`, and showing a small muted line on the
card only.

Then I asked a second question: should we mark these concepts at all, since almost
every concept uses the standard meaning?

That changed the answer. If nearly every card carries the mark, the mark tells you
nothing. So the agent turned it around: mark the *exception*. A concept the paper
really defines gets `defined: S01-03` and a small "defined in S01-03" link to the
section. Every other card says nothing about where its meaning came from. The sentence
was deleted from seven files.

The final fix contradicted my first idea. It also contradicted the agent's first idea.
And it was simpler than both.

## Was it a one-off?

I went back through my sessions on the same project, about a week of building two
plugins. The other one is called *backlog*. It works the same way, but for building
software: it keeps a list of things to build, shows them on a map, and writes down for
each task what "done" looks like, its *acceptance criteria*.

I found ten moments where my taste flagged something.

- **My taste was right about the problem every time.** The agent never said "that's
  not a problem."
- **My fix was replaced 3 times.**
- **My fix was kept but changed 3 times.**
- **My fix was kept as is 3 times.**
- **In the tenth, it went the other way:** I corrected the agent.

The concept card was the first replacement. Here's the second: in the backlog map, acceptance
criteria were written in code blocks, and the narrow side panel made me scroll sideways
to read even one line of a criterion. My fix: stop putting them in code blocks. The agent changed
only how the map *shows* them. The files kept their code blocks, because two other
parts of the plugin count those blocks to number the test scenarios. My fix would have
broken them.

And the third: I wanted a step that decides which user story to build next, and I asked
whether it belonged inside the `implement` command or in a new one. Neither. The plugin
already had a `/backlog:next` command that picks the next item. The judgment belonged
there.

## Why my fix got replaced

Two kinds of knowing were at work.

**I know the output from using it.** I'm the one who scrolls sideways, who reads a
meaning and trips over a note. The agent doesn't use the map. It can't feel that a
sentence is in the wrong place until someone says so.

**The agent knows the project.** It reads the repo. It knew the sentence showed up in
three places, that two tools counted the code blocks, and that a `next` command already
existed. I wrote all of that, but I couldn't keep it all in my head while looking at one
card.

My fix came from where I was standing. The agent's fix came from the whole project.

## When my fix was fine

Three times the agent did exactly what I asked: make the detail panel wider, use a
contrast color for the selected row, add a button that moves sections into the trail, a panel that collects the tasks and
concepts I'm focused on right now.
Each one changed a single spot in the page.

The replaced fixes were different. Each one touched several parts of the plugin. That's
the limit of my claim: when the problem stays in one place, your first fix may be fine.
When it spreads across the project, that's where the agent's view of the whole project
matters.

## Two things I didn't give up

**I still argue.** In one session, the agent said running tasks in parallel was risky:
"parallel worktrees are cheap to start but expensive to merge." A worktree is a separate
copy of the project, so several sessions can each work on their own task at once. The
expensive part used to be merging those copies back together, because a person had to
untangle every conflict by hand. I asked it to rethink that: in my workflow, an agent
does the merging, not a person. It agreed and revised its plan. In another session, I disagreed with when the plugin should recommend a review,
and it changed the rule my way. The agent holds the project's context. That doesn't
make its judgment right.

**I keep asking.** In the concept story, the reversal didn't come from the agent alone.
It came from my second question and the fact inside it: almost every concept uses the
standard meaning. Letting go of my first fix didn't mean going quiet.

So "co-designer" fits better than "builder". I bring the problem and what I see while
using the output. The agent brings the whole project. The fix comes out of the
back-and-forth.

## Two honest limits

**I'm not a typical beginner.** I was a backend developer. I know roughly how software
fits together, so my taste for "this is wrong" has some training behind it. I don't
know whether a newer developer's taste finds problems as reliably.

**This is about a code agent.** Claude Code read the repo before it answered. A chat
assistant that can't see your files doesn't have that context, and the agent's view of the whole
project falls away.

And it's ten moments from one person in one project. Small, but enough to change how I
work.

## So, what should you bring?

If you stick to your own fix, you can miss the agent's fix, which comes from the whole
project and might be the simpler one.

It's worth trying this: when your taste says something is wrong, say *what* feels
wrong and *why*, then offer your fix as a draft, not a spec. My first fix is a draft
that a code agent can improve. My taste is what tells it where to look.
