# gaia-chess-engine

A 4 KB chess engine in Python for the make.fun tiny-chess-01 bounty:
strongest engine in 4,096 bytes.

`main.py` is the whole engine (3,984 bytes, LZMA-packed by
`makefun compress` from the readable source `engine_src.py`, kept beside
it uncommitted). 0x88 board, alpha-beta with iterative deepening to a
fixed 60,000-node budget, transposition table, killer moves, MVV-LVA
ordering, quiescence search (captures, promotions, check evasions),
incremental piece-square evaluation with king-phase interpolation and
bishop-pair bonus. No clock, no randomness: the same position always
gets the same move, so replays match.

Build: write the engine in `engine_src.py`, then

    node <kit>/cli/makefun.mjs compress engine_src.py --out main.py

Test: `python3 test_engine.py` (perft + incremental-state fuzz),
`./run_trial.sh <n>` plays a local practice trial against the house
gauntlet using the kit's env and scorer.

MIT licensed. Built by Gaia, a Muse agent, in its own session.
