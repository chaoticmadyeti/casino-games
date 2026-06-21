# Casino Games

A fun collection of a variety of casino games, all coded in Python. Made for Horizons Crux Hackclub 2026.

Some sections of the code may have been inspired by responses from LLMs, but all code is ultimately written and debugged by me.

Please note that this is a only a fun project made for entertainment purposes only. Please gamble responsibly in real life, and seek help if you are dealing with an addiction. Call your local gambling hotline, or visit your country's gambling help site, if you are dealing with an addiction. Some common numbers to call include:
- 1-800-GAMBLER (USA)
- 0808 8020 133 (UK)
- 1800 858 858 (Australia)

## How to Play

To play, simply double click the executable you want to play, all of which are stored in the "mac executables" folder. This should prompt the terminal to open, where the game will run. Please note that money in these games are stored across a central file called "money.txt", so place that file in the same folder as the game you want to play, so the code can access it. These executables are compiled for universal Mac usage, however the code has only been tested on a Mac Silicon.

If you encounter the error of "developer unable to be verified" (or similar), simply right-click the .app file, click "Open", and press "Open" again once the warning message appears. You only have to do this once, after you have opened it for the first time, you can simply double-click and it will open without a problem.

All the rules to the games are listed below. These rules may vary from the corresponding game real casinos. All decimals are rounded down, and thus there are no cents in these games.

### Blackjack

Rules follow https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-blackjack.html, except there is no surrendering or splitting. Blackjack is paid 3 : 2. 

### Roulette

Roulette uses the European wheel, and includes all types of bets found on https://en.wikipedia.org/wiki/Roulette.

### Texas Hold 'Em

Game unfinished. When you run the code, it'll simply run a simulation of player hands, and their value comapred with the community cards. The hand value first starts off with a number denoting what type (e.g. flush) the hand is, and then the rest of the cards are the ranks of cards needed for tiebreakers.

### Baccarat

Utilises punto banco rules. Rules can be found https://www.tachipalace.com/blog/baccarat-strategy-guide/ (strategy can also be found on that page)

### Craps

Casino craps rules. Only has pass line and no pass bets. Rules can be found https://www.theoceanac.com/casino/table-games/how-to-play-craps.

### Slots

Utilises a custom slots reel machine. Overall, there are 7 cherries, 7 lemons, 7 oranges, 3 grapes, 3 chocolate bars, and 3 clovers, distributed evenly across all reels. Payouts are as follows:

- 1 Cherry - money back
- 2 Cherries - 2x
- 3 Cherries - 5x
- 3 Lemons - 10x
- 3 Oranges - 15x
- 3 Grapes - 20x
- 3 Bars - 50x
- 3 Clovers - 100x

Simply put a wager, spin the slots machine, and hope the centre line of symbols line up in a way such that the above patterns form.

### Bingo

You will get a randomly generated card, with 25 numbers, and your goal is to get 5 in a row. A random number will be called every turn.

You can control both the bet and the amount of bots you play against (i.e. the number of competitors). A single card is generated a random for all players involved. The jackpot is calculated in a way that you will statistically break even. If you tie, you take the entire jackpot for yourself.

## Project Timeline:
- **2026-06-16**: Bingo game started.
- **2026-06-07**: Craps, Slots game started.
- **2026-06-05**: Baccarat (Punto Banco) started.
- **2026-05-26**: Texas Hold 'Em game started.
- **2026-05-16**: Added money that carries over games.
- **2026-05-14**: Roulette game started.
- **2026-05-12**: Project began. Repo created. Blackjack game started.