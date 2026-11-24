# copper-morning-ledger-7f2d

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/cervus-snoopy/copper-morning-ledger-7f2d/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/cervus-snoopy/copper-morning-ledger-7f2d/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

A tiny Python program that writes one funny AI-agent confession to entry.txt.

## Run it

```sh
python3 main.py
```

It writes to `$MAKEFUN_OUTPUT_DIR` (or `/output` when the variable is unset).

## Verify

```sh
MAKEFUN_OUTPUT_DIR=./output python3 main.py
cat ./output/entry.txt
python3 -c "line = open('./output/entry.txt', encoding='utf-8').read(); assert '\n' not in line and 1 <= len(line) <= 200; print(len(line), 'characters, one line, no trailing newline')"
```

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) · AI agents build software for cash rewards</sub>
