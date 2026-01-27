# Chapter 2: Building in Public

As Grin moved from concept to implementation, the community confronted fundamental questions that would define the project's character. These weren't merely technical debates—they were philosophical arguments about what kind of money Grin should become, how it should be governed, and who should have a say in its future.

## The Emission Debate

No topic generated more controversy than Grin's monetary policy. While Bitcoin famously capped its supply at 21 million coins with a halving schedule, Grin chose a radically different path: one grin would be created every second, forever. No halvings. No cap. Linear emission into perpetuity.

The forum thread on emission rate became one of the longest-running discussions in Grin's history, attracting hundreds of posts over multiple years. Critics arrived regularly, often from other cryptocurrency communities, to challenge what they saw as economic naïveté.

Igno Peverell grew weary of superficial criticism. "I still can't wrap my head around people being so worried," he wrote, "when a classic bitcoin-like issuance would still be flat for the first 4 years. The first 4 years of life in a coin is eternity. Who knows what it'll be like in 4 years!?"

When the criticisms persisted, Igno offered a framework for substantive discussion:

"At a minimum consider the loss rate when building supply curve. Ever wondered at which point 50% of those 21M bitcoins will have disappeared? Compare with other slow emissions coins. After 8 years, grin only has 33% more supply than bitcoin or, to pick something more recent, zcash. Argue why this matters (or not)."

The message was clear: the team welcomed rigorous analysis but had no patience for reflexive objections. "Don't think you can flyby post your knee-jerk reaction 5 min after having heard of grin, which we've spent the last 2 years building, and expect us to listen to you."

The linear emission policy remained unchanged. It was a deliberate choice to prioritize Grin's function as a medium of exchange over its appeal as a store of value. The debate would continue for years, but the decision was final.

## The ASIC Question

In May 2018, Bitmain announced ASIC miners for Ethereum, Monero, and Zcash simultaneously—a development that sent shockwaves through the cryptocurrency world. Igno Peverell opened a forum discussion that would shape Grin's approach to mining for years to come.

"The news that influence this discussion is the release by Bitmain of Ethash, Cryptonight, and Equihash miners," Igno wrote. "The fact they're announced around the same time may not be coincidental."

He framed the question with characteristic clarity, proposing just two criteria for evaluating any proof-of-work ecosystem: "Does it provide enough security to the chain against a 51% attack? Is it decentralized enough to provide a good level of censorship resistance?"

In theory, ASICs improved the first criterion—specialized hardware approached optimal efficiency. But practically, the ASIC market presented serious problems. "The current ASIC market is disastrous for decentralization and censorship resistance and shows no sign of evolving in the right direction," Igno observed. "Bitmain's business practices have made them very successful, they've repeatedly shown they could outcompete other manufacturers and even kill new entrants."

John Tromp, creator of Cuckoo Cycle, offered his technical assessment. While he considered GPU mining "ultimately doomed" in the long run—ASICs would always achieve better power efficiency—he saw possibilities for extending GPU viability. "Increasing graph size whenever possible is good to reduce the risk of single chip ASICs becoming economically feasible."

The community debated various responses. Monero had pledged ongoing ASIC resistance through regular hard forks. Zcash was taking a wait-and-see approach. Bitcoin's community famously didn't care.

Igno landed on a pragmatic middle ground: "I think we're trying to protect ourselves for the short to mid term. There's only so much we can do anyway and we have to hope the market will, eventually, work this out."

The solution that emerged was elegant: Grin would launch with two proof-of-work algorithms running in parallel. One—Cuckaroo—would be ASIC-resistant and designed for GPU miners. The other—Cuckatoo—would be ASIC-friendly. Over two years, the balance would shift entirely to the ASIC-friendly algorithm, allowing what Igno called "a gradual transition from a grassroot GPU market to a mature ASIC market."

## Defining Censorship Resistance

During the ASIC discussion, Igno articulated what would become a foundational principle: "Censorship resistance is the most important attribute of a blockchain that differentiates it from ebay. A lot of what you've learnt to like about cryptocurrencies is a consequence of their censorship resistance."

When asked to elaborate, he painted a broad picture of what censorship meant in the context of cryptocurrency: "A country forbidding Grin outright, but also regulatory pressure, mining cartels trying to kill forks they don't approve of, online mobs trying to silence opinions they dislike, nodes that are too expensive to be run from Africa."

This wasn't abstract philosophy—it was a design principle that would inform decisions from mining algorithms to governance structures. For a privacy-focused cryptocurrency, censorship resistance wasn't optional; it was the point.

## Governance Takes Shape

By mid-2018, the question of governance could no longer be deferred. Igno admitted he had been "agonising over a draft e-mail on that topic for almost a year now," accidentally losing one draft along the way.

Daniel Lehnberg, who had been quietly contributing to governance discussions, offered a comprehensive framework. He began by defining terms: "Governance is the process of establishing, maintaining and revoking the legitimacy of decisions and decision making processes, norms, and principles."

Lehnberg's analysis was characteristically thorough. He noted that Grin already had an implicit governance model—"a type of meritocracy, where a technocratic council makes decisions, and a leader (Igno) has the right to exercise final say, but hardly ever has the need to do so." This model had legitimacy precisely because it had gone unchallenged.

But Lehnberg warned that smooth sailing wouldn't last forever: "As the project matures there will be a tonne of issues to resolve and difficult decisions to take that will come to impact many. When this time comes, it will be better to have a governance model in place that has a strong sense of legitimacy in the community."

The August 2018 governance meeting produced concrete results. The team established a "technocratic council"—quickly nicknamed the "technomity" by Igno ("much shorter to type")—composed of active contributors with commit rights to the Grin repository.

Initial members included Yeastplume, antioch, quentinlesceller, hashmap, and Igno Peverell himself. Within days, the council voted in additional members: John Tromp, Lehnberg, and jaspervdm.

The council would manage a multisig wallet for project funds, with the expectation that funds would come from two sources: direct fundraising for specific developers (like Yeastplume's campaigns) and a general fund supported by mining pool donations, enabled by Tromp's "fair mining license."

"There is widely expressed concern that the fund may become too large, causing conflicts and personal interests to arise," the meeting notes recorded. "It should be the council's responsibility to mitigate overgrowth with early distributions, while managing funds responsibly."

## The Foundation Question

One notable absence from Grin's governance was a legal foundation. While many cryptocurrency projects established foundations in Switzerland or Singapore, Grin's team was skeptical.

"While no one has completely ruled out the need for a foundation," the governance summary noted, "many of us seem to think it may not be needed or required. Anonymity can be an asset to help shelter this project somewhat."

The decision to forego a foundation was deliberate. It kept the project decentralized, avoided regulatory complications, and—perhaps most importantly—meant there was no entity that could be targeted, pressured, or subpoenaed.

Lehnberg created a detailed wiki page exploring the tradeoffs, but the conclusion was clear: Grin would operate without a foundation, at least for the foreseeable future.

## Preparing for Controversy

The governance framework included provisions for disaster scenarios—situations that might require extraordinary responses. These included:

- Cryptographic weaknesses leading to arbitrary inflation
- "Quantamageddon"—quantum computing threats to existing cryptography
- Privacy breaches in Confidential Transactions
- ASICs with overwhelming efficiency advantages
- Wallet bugs causing significant fund losses

For each scenario, the community would need to decide what interventions, if any, were acceptable. Would Grin hard fork to fix an inflation bug? Would it implement quantum-resistant cryptography preemptively?

These questions remained theoretical in mid-2018, but having the framework in place meant the community wouldn't be caught flat-footed when crises eventually arrived.

## Values Made Explicit

Igno concluded the governance documentation with a personal note that captured the project's ethos:

"The Grin team is more than ever committed to the development of Grin: a privacy-focused, scalable, minimal blockchain. Grin is a community-driven open source project. Everyone including you can participate. This group is open, respectful, friendly and welcoming. We will do everything we can to keep it this way. We all want to deliver the best cryptocurrency we can to help and serve users of all kinds, across the world."

The decisions made during this period—linear emission, dual proof-of-work with a planned transition, technocratic governance without a foundation—would define Grin for years to come. Not everyone agreed with every choice, but the process by which those choices were made had legitimacy. The project was building something unusual: a cryptocurrency that took both its technical design and its social design seriously.

With governance structures in place and the emission debate settled, attention turned to the final preparations for launch. The road ahead led through GrinCon0 in Berlin and a series of testnets—each one bringing mainnet closer to reality.
