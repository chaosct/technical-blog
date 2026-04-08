---
title: The Age of Personal Software
date: 2026-01-25 00:00
status: published
description: Code agents have suddenly pushed us into a new era where software is so cheap that everyone can have it tailored to their needs.
summary: 'Code agents have changed the economics of software: creating ad-hoc tools, customizing open source projects, or automating tasks that previously were not worth it is now trivial. In this article I go over several practical examples of tools I have created or modified with agents, from onboarding automations to customizing Rust software in a language I barely know.'
tags: AI, agents, software
---

Over the last year, these tools have evolved at a remarkable pace. Early LangChain agents were exploring the same idea, but Claude Code was the first tool that really made it work: combining tools with LLMs in an action-and-test loop. In 2026, all of this is accelerating with Ralph loops and clawdbot.

Software is becoming dramatically cheaper to build and, despite its limitations, there are many use cases where the economics of programming have suddenly been turned upside down.

I don't have the time, or the skill, to write a full dissertation on where all of this is taking us, but I can at least share a few things I've been able to do with code agents that I could not have done before.

## Automating the long tail

The economics of automation were perfectly captured by the classic XKCD comic:

![XKCD 1205: is it worth the time?](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

The first time I saw that comic, it got burned into my brain. I've tried not to fall into the black hole of writing code to automate tasks that don't have a positive return on the time invested. That chart no longer really applies: software is now so cheap to create, in time terms, that almost anything can be automated.

### Onboarding and offboarding tools

I've built a couple of tools for onboarding and offboarding. Backing up Google Workspace data and then uploading it to a shared Drive folder? Done. Creating the new accounts across different platforms and assigning permissions? Done. Generating a report with the whole process? Done.

## Single-use tools

The same thing happens with tasks you only want to automate **once**.
I built a whole ad-hoc piece of software to transform **one** report from Markdown into PDF. With odd requirements, color-coded labels, a polished table of contents... It worked perfectly and after that single use, I will never use it again. But I would not have done it manually either. It would not have been worth it.

## Customizing existing software

This is one of the most interesting use cases. You can pull down a GitHub repo, ask an agent to adapt it, and just use the result. You don't even need to publish it.

### Tukai: learning touch typing

This year I realized that, with code agents, the bottleneck in development had shifted to my typing speed. In all my years in this profession, that had never happened to me before. Usually I spent more time thinking than typing.

So, at this point in my life, I decided to learn touch typing properly. I needed a practice program that also worked locally so I could use it during train trips. I found [Tukai](https://github.com/hlsxx/tukai) and liked it. The problem: it didn't even ship with a Catalan word list.

With Claude Code, or Codex, I don't remember which, we quickly added several Catalan dictionaries for different learning levels, based on the most frequent words in Wikipedia and with balanced coverage of all letters.

### Claude Code Sleep Preventer

One thing that really annoys me about the MacBook is how aggressive it is about going to sleep at the slightest opportunity. And when you're using a code agent, that becomes a problem.

Apparently [Claude Code Sleep Preventer](https://github.com/CharlonTank/claude-code-sleep-preventer) does exactly that, but: zero forks, zero stars. So I downloaded the code and had Claude Code audit it.

That already revealed a surprise: apparently the software also transcribes speech when you ask it to, and to do that it needs to download and run a local Whisper model weighing in at hundreds of megabytes. Aside from that, the software did not seem malicious.

So with five minutes of modifications in Claude Code, I had it installed, running, and without the speech transcription part.

And all of that in Rust, a language I barely know how to read, let alone write.

## Playing with clawdbot

The most extreme example I've personally tried is clawdbot. When I discovered what it was, a kind of universal Claude Code that you can use as a personal assistant, I installed it immediately. That immediately appealed to me, because I could genuinely use a personal assistant.

The thing is, if you ask it whether it can do this or that, it might answer something like: I can't do that, but I can program myself a plugin to do it. And then it does. The assistant can effectively build its own extensions. In my case, I wanted to process information from Notion, and a few minutes later it was already able to read and write articles there.

## Conclusions

We are entering a fascinating stage in software creation. I have no idea what the future will look like, but one thing I do know is that the era of fixed programs that do not evolve, of manual tasks completed in isolation, is over. We are entering the age of software that is cheap, abundant, and everywhere.
