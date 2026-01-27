# Chapter 5: Growing Pains

The months following launch were a period of rapid maturation. The core team worked through a backlog of improvements while the community began building the broader ecosystem that a cryptocurrency needs to thrive. Windows support, wallet improvements, and the emergence of alternative implementations marked Grin's transition from launch product to production system.

## Windows Arrives

For months, Grin had been a Linux and macOS affair. Windows users could participate through WSL or virtual machines, but native support remained elusive. In March 2019, Yeastplume finally delivered.

"Grin Windows (Gwin?) now has most of the major issues worked out," he wrote, alongside a screenshot of Grin running natively on Windows. "Getting the builds themselves working was an extraordinarily fiddly process, as were just about all of the other issues that needed to be addressed."

The work had been painstaking. Windows handled database allocation differently than Unix systems—it actually allocated the full requested size rather than treating it as a maximum. Yeastplume had to implement dynamic allocation of LMDB backend storage, growing the database in 128MB chunks as needed.

With the wallet now split into its own repository and Windows builds automated through CI, Grin could reach a much broader audience. The cryptocurrency was no longer just for Linux enthusiasts.

## The Wallet Strategy

Yeastplume articulated a philosophy that would guide wallet development: "Our strategy with regards to the wallet is not to create the slickest, most polished and user friendly Grin wallet in existence. It is rather to create the slickest, most polished and developer-friendly Grin wallet toolkit in existence, that will allow community wallet developers to focus on creating the slickest, most polished and user-friendly Grin wallets in existence."

This was deliberate decentralization of development. Rather than trying to be everything to everyone, the core team would provide robust building blocks. Third-party developers could create the interfaces that best served their users.

The V2 API became the embodiment of this philosophy. Working with Andrew Dirksen from Layer1 Capital, Yeastplume built a system that was self-documenting and self-testing. Documentation examples weren't just illustrations—they were actual integration tests that ran against the wallet's test framework.

"It looks like simple rustdoc documentation, but there's a lot going on behind the scenes," Yeastplume explained. "That 'json_rpc_example' in the image isn't just documentation, it's the input to an entire integration test... By ensuring documentation and testing are integrated this way, we can pretty much guarantee that both the rust and generated JSON RPC APIs will stay consistent, current and documented going forward."

## Grin++ Emerges

In March 2019, David Burkett announced Grin++, an alternative implementation written entirely in C++. After six months of quiet development, he was ready to share it with the world.

"Although the official Grin client is obviously much more stable and well-tested, Grin++ offers several advantages," Burkett wrote. "Full Windows support, simple to use electron UI, multi-user support, lightning fast refreshes & wallet restores, full AES w/scrypt encryption to protect your coins and privacy."

The announcement came with a personal note that captured something essential about open-source cryptocurrency development:

"I've worked tirelessly on Grin++ over the last 6 months trying to get everything working, and have been fortunate enough to not have the need to ask for anything in return. That is, sadly, no longer the case. I've decided to leave my job so I can spend some time focusing on Grin++, and no longer have any source of income (YOLO, as the kids say)."

Burkett's decision to quit his job and work on Grin full-time—funded only by donations—demonstrated the project's ability to attract serious contributors. Grin++ would become an important part of the ecosystem, offering users choice and contributing to the network's decentralization.

## Invoice Transactions

One of the more significant wallet features to land in this period was invoice transactions. Unlike typical cryptocurrency payments where the sender initiates, invoice transactions allowed recipients to create payment requests that senders could fulfill.

The feature required careful API design and extensive testing. Yeastplume documented every edge case, created integration tests, and ensured the command-line interface was intuitive. It was the kind of methodical work that rarely made headlines but gradually improved Grin's usability.

## Shamir's Secret Sharing

As a "skunkworks side project," Yeastplume began implementing SLIP-39—Shamir Secret Sharing for mnemonic codes. The concept was elegant: take a wallet's recovery phrase and split it into multiple shares, where any threshold of shares could reconstruct the original.

"My 12 Word wallet master key (BIP39 mnemonic) is run through the lib and split into a 3 of 5 scheme," Yeastplume demonstrated. "I can then take these split shares and distribute them to 5 family members. Each share is useless on its own, but when I get hit by a bus tomorrow... then any 3 of my 5 family members can get together, recreate my master key and enjoy my grins."

The work connected to broader goals around multisig support, which would use similar threshold cryptography concepts. It was typical of Grin's development approach: building foundational pieces that would enable future features.

## A Coinbase Donation

In May 2019, Grin's General Fund received a remarkable anonymous donation: 50 BTC, sent in a single public Bitcoin transaction. The coins came from a coinbase reward—the payout for mining an entire Bitcoin block solo back in 2010, when the reward was worth just $14. The anonymous miner had held those coins for over eight years, watching their value appreciate by more than two million percent, before giving them all away to support Grin development.

The donation, worth over $400,000 at the time, was a powerful vindication of Grin's funding model. A project that had launched with no ICO, no premine, and no developer tax had attracted the kind of supporter who had been in cryptocurrency since nearly the beginning—and who valued Grin's principles enough to part with a fortune.

As one community commentator put it: "Even though Grin depends entirely on donations, it's actually looking pretty healthy right now."

## The Ecosystem Grows

Beyond the core team's work, the broader ecosystem was taking shape. Grinmint and other pools refined their operations. Block explorers like Grinscan provided network visibility. Community wallets like wallet713 offered alternatives to the command-line interface.

Meetups happened in Amsterdam, London, and other cities. Developers who had only known each other through Gitter and GitHub met in person, strengthening the social bonds that held the project together.

The challenges remained significant. The interactive transaction model confused users accustomed to Bitcoin's simpler flow. Exchange listings were limited. The price volatility that plagued all cryptocurrencies affected Grin too.

But the project was maturing. The infrastructure was being built. And the first hard fork was approaching—a test of whether the community could execute a coordinated network upgrade without the drama that had plagued other projects.
