# The Grin Story

### A Chronicle of Privacy, Community, and Decentralized Development

*Compiled from the Grin Forum (2018-2025)*

*Generated: January 2026*


---

# Introduction

*How a pseudonymous developer, a Harry Potter character name, and an obscure cryptographic whitepaper sparked a movement to build private, decentralized money.*

---

In July 2016, someone using the pseudonym "Tom Elvis Jedusor" - an anagram of Voldemort's French name - dropped a whitepaper onto a Bitcoin research IRC channel and vanished. The paper described MimbleWimble, a protocol that promised to dramatically improve blockchain privacy and scalability by eliminating the need to store full transaction history.

The cryptography community was intrigued. But the author was gone.

Within months, another pseudonymous developer picked up the torch. Calling themselves "Igno Peverell" - after the Harry Potter character who created the Invisibility Cloak - they began building Grin, the first implementation of MimbleWimble.

What followed was an experiment in open-source development, community governance, and technical innovation. Grin would launch without a pre-mine, without a foundation, without venture capital funding. Its contributors chose anonymity. Its monetary policy defied convention. Its governance evolved from a small group of developers into a decentralized community.

This book tells that story - through the words of the people who built it, the debates that shaped it, and the challenges that tested it. It's a story of technical innovation, but also of the human elements: the motivations, disagreements, and ideals that drove a community to build something designed to outlast any individual contributor.

The story begins, as many stories do, with a mysterious stranger and a radical idea.

---



---

## Table of Contents

**Chapter 1: MimbleWimble Origins**
*The MimbleWimble whitepaper appears, and Igno Peverell begins building.*

**Chapter 2: Building in Public**
*The community debates Grin's core design choices.*

**Chapter 3: Road to Launch**
*Final preparations for mainnet launch.*

**Chapter 4: Launch Day**
*Grin's mainnet launches on January 15, 2019.*

**Chapter 5: Growing Pains**
*Early challenges test the young network.*

**Chapter 6: First Hard Fork**
*The first network upgrade and ecosystem growth.*

**Chapter 7: The Hard Fork Years**
*Scheduled hard forks bring protocol maturity.*

**Chapter 8: Governance Evolution**
*Governance transforms from core team to community.*

**Chapter 9: Decentralized Development**
*Community-driven development continues.*

**Chapter 10: Legacy & Future**
*Reflections on Grin's journey and future.*


---

# Chapter 1: MimbleWimble Origins

In July 2016, someone using the pseudonym "Tom Elvis Jedusor"—an anagram of Voldemort's French name—dropped a whitepaper onto a Bitcoin research IRC channel and vanished. The paper described MimbleWimble, a protocol that promised to dramatically improve blockchain privacy and scalability. The cryptography community was intrigued, but the author was gone.

Within months, another pseudonymous figure emerged. Calling themselves "Igno Peverell"—after the Harry Potter character who created the Invisibility Cloak—they began building the first implementation of MimbleWimble. They called it Grin.

## The Forum Awakens

On January 16, 2018, the Grin forum came to life with a simple welcome message: "Grin is a blockchain and a cryptocurrency focused on privacy and scalability. Grin is also an implementation of the MimbleWimble transaction format with the extensions required for a complete blockchain."

The early days attracted a particular kind of person—technically curious, drawn to the project's combination of cryptographic innovation and Harry Potter references. Within a week, community members were already asking for spaces to discuss the project beyond pure technical matters.

"I am a non-technical person reading the resources available and very interested in this project," wrote one early member. "As far as I can see, MW GRIN is an evolved crypto that has the potential to eclipse/replace many others... I sense that the MW team is actively downplaying publicity during what is still early development stages."

Igno Peverell responded with characteristic pragmatism, explaining that a "Lounge" category existed but was hidden from new users—"the original intent was to avoid too much noise." As for market speculation and "when lambo" discussions, Igno hoped to keep those isolated in a dedicated Market category.

## Cuckoo Cycle: A New Kind of Mining

One of Grin's most distinctive features was its proof-of-work algorithm: Cuckoo Cycle, created by John Tromp. A core developer who co-architected several parts of Grin's consensus code—including the emission schedule, Merkle Mountain Range (MMR), difficulty adjustment, proof-of-work transitions, spent bitmap MMR, and fee system, as well as Cuckoo's CPU and GPU solvers—Tromp brought deep cryptographic expertise to the project. Unlike the hash-based mining that powered Bitcoin and most other cryptocurrencies, Cuckoo Cycle worked by searching through massive graphs for cycles—paths that loop back on themselves.

Yeastplume, who would become one of Grin's most prolific developers, created a comprehensive Mining FAQ that became essential reading for anyone wanting to understand the new system. "For most people's purposes," he wrote, "it's an algorithm that we hope turns out to be ASIC resistant."

The technical details were novel. Instead of measuring mining power in hashes per second, Grin miners measured their output in "Graphs per Second"—how many graph searches they could complete. Early GPU implementations on a 1080Ti achieved about 1.2 seconds per graph, though Yeastplume cautioned that these numbers represented "a very early and unoptimised version of the miner."

The mining guide that Yeastplume published in February 2018 became a landmark document in Grin's early history. Running to thousands of words, it walked miners through everything from basic CPU mining to advanced GPU configuration. The guide demonstrated the project's commitment to accessibility—anyone with modest hardware could participate.

"If everything is working correctly, you should see grin-miner connecting, accepting solutions, and mining in the TUI," Yeastplume wrote, before diving into the intricacies of plugin configuration, CUDA setup, and parameter tuning. The detail was exhaustive, covering everything from checking GPU stats with `nvidia-smi` to troubleshooting common errors.

## Building an Identity

As the technical foundations took shape, the community turned to questions of identity. The logo discussion that began in February 2018 would stretch for months, reflecting deeper questions about what kind of project Grin wanted to be.

Dozens of designs were proposed and debated. One design, created by community member 0xb100d—featuring a simple yellow circle with two dots and a curved line forming a face—caught the attention of Daniel Lehnberg, who would become central to Grin's governance.

"Simple, circular, has that cheeky feel to it, stands out from all other coins logos," Lehnberg wrote. "Very flexible. Very simple. I love it."

But Lehnberg also raised a more radical idea: what if Grin had no official logo at all? "It's a currency, we're not trying to sell anything. The USD or the GBP has a currency symbol, yes, but there's no logo." The suggestion captured something essential about Grin's ethos—a reluctance to centralize, even around something as seemingly harmless as branding.

The currency symbol debate proved equally spirited. Options ranged from the Paraguayan guaraní symbol (₲) to various stylized lowercase g's. The community eventually settled on an unexpected choice: ツ, the Japanese hiragana character "tsu," which resembled a smiling face. As Tromp later explained when someone asked how to pronounce it: "It's pronounced 'grin.'"

## The Wallet Challenge

While logos and symbols were matters of community preference, the wallet posed genuine technical challenges unique to MimbleWimble. Unlike Bitcoin, where you could simply post an address and receive funds, MimbleWimble transactions required interaction between sender and receiver.

"Grin payees currently provide IP addresses to payers so that their wallets can rendezvous and complete the payment," explained community member rodarmor in a February 2018 discussion. "We'll need to switch to a more robust address scheme eventually."

The problems with IP-based communication were significant: vulnerability to man-in-the-middle attacks, the need for receivers to configure firewalls, exposure of network locations, and the impermanence of IP addresses. The discussion that followed explored solutions ranging from Tor hidden services to the emerging Wireguard VPN protocol.

Igno Peverell made one early clarification that would shape how the community talked about the problem: "I wouldn't talk about addresses or address format, that's going to confuse people. Whatever we come up with will have totally different characteristics... So how about wallet URL?"

This attention to terminology reflected a broader concern—ensuring that people understood MimbleWimble on its own terms rather than forcing it into Bitcoin-shaped mental models.

## Genesis Questions

Every blockchain begins with a genesis block, and the community debated what message, if any, Grin's should contain. Bitcoin's genesis block famously embedded a newspaper headline about bank bailouts—a political statement about why decentralized currency mattered.

One community member, posting under the handle harry.potter, suggested a quote from the Harry Potter series—the warning inscribed at Gringotts bank about the consequences of greed. It was perfectly on-brand for a project whose key developers all used Harry Potter pseudonyms.

But Igno Peverell delivered disappointing news: "It makes me a little sad but it doesn't seem that we'll be able to embed any text in our genesis block. Somewhat by design, all the data is obscured and there are no 'open fields.'"

Tromp, the creator of Cuckoo Cycle, offered a workaround: "We can put in a hash of any text we like as the prevhash (which would otherwise be 0). That's as good as putting the text itself in..."

The discussion revealed a deeper challenge. The genesis block needed to be pre-mined at a high difficulty to prevent the network from being overwhelmed at launch. Igno estimated that with 20 GTX 1080Ti cards working on the genesis block, it would take over 2.5 days to produce a valid solution. The team would ultimately need weeks to prepare.

## Yeastplume's Progress

Throughout the early months of 2018, Yeastplume posted weekly progress updates that became essential reading for anyone following Grin's development. His updates combined technical detail with candid assessments of what remained to be done.

"I tend to think that imposing a design on something like this up-front usually leads to unnecessary complexity," he wrote in May 2018, explaining his approach to wallet development. "I generally prefer to code to what you know now, and then refactor, refactor, refactor, letting the design take shape as more needs come to light."

The wallet work was painstaking—separating transaction building from key management, creating clean APIs, building infrastructure that would support multiple interfaces. Yeastplume introduced the term "Slate" to describe the data structure passed between parties during a transaction: "The idea here is the slate is passed around between all parties involved, each one filling in their information until there's enough info to finalise the transaction. How it's passed around doesn't matter (http or avian carrier)."

By June 2018, Yeastplume could show screenshots of an early web wallet interface—rough, but functional. "It's still very rough and doesn't necessarily do all of the error checking and user-friendly hand-holding that it should eventually do," he wrote, "but it works and can even be used to send at the moment."

The list of remaining work was daunting: LMDB backend for storage, new web server code to replace abandoned libraries, transaction logging, wallet restoration, security model definition—and that was before getting to advanced features like multi-signature transactions.

## A Community Forms

By mid-2018, patterns were emerging. The project attracted developers willing to work without guaranteed compensation, drawn by the technical elegance of MimbleWimble and the community's collaborative spirit. People arrived from other cryptocurrency projects, sometimes disillusioned with what those communities had become.

"Just moved from Zcash community to here for many reasons," wrote one newcomer. "Hope GRIN have better visions and future."

Another, a longtime Bitcoin holder, was more pointed: "Bitcoin has become a 'number go up' meme factory, and frankly its not what I got into crypto for. People here seem pretty knowledgeable, so I am here to absorb all the information I can."

The seeds planted in these early months—the technical foundations, the community norms, the philosophical commitments—would shape everything that followed. Grin was being built in the open, by pseudonymous developers who believed that privacy-preserving digital cash was worth the effort.

Testnet 2 was running. Testnet 3 was on the horizon. And somewhere in the distance, mainnet awaited.



---


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



---


# Chapter 3: Road to Launch

The second half of 2018 became a sprint toward mainnet. With governance structures in place and the major technical decisions made, the community turned to the hard work of implementation—refining the proof-of-work system, polishing the wallet, and testing everything that would need to work on day one.

## The Dual PoW Takes Shape

In September 2018, John Tromp laid out the final architecture for Grin's unique dual proof-of-work system. The design was elegant: two algorithms running in parallel, with the balance shifting over two years.

"The 'primary' one is Cuckatoo32+, a variant of Cuckoo Cycle designed to simplify ASIC design," Tromp explained. "This will start out getting only 10% of the reward at launch, linearly climbing up to 100% after 2 years. At that time there will hopefully be ASIC designs from multiple manufacturers engaged in a healthy competition."

The complementary algorithm, Cuckaroo, targeted GPU miners. It would begin with 90% of rewards, declining to zero over two years. ASIC resistance would come primarily from scheduled hard forks every six months—following Monero's example—with each fork slightly modifying the algorithm to invalidate any specialized hardware.

To prevent lean mining—a technique that could dramatically reduce memory requirements and enable single-chip ASICs—Tromp and Igno devised an ingenious solution. They would require a long sequential computation to generate blocks of edges, making it impractical to recalculate them on the fly. Mean solvers would compute this once and store the results; lean solvers would face a crippling latency penalty.

The memory requirements would also increase over time, following a predetermined schedule. "After 2^k years, we will phase out the use of cuckatoo32+k," Tromp wrote. "So cuckatoo32 will be phased out after 1 year, cuckatoo33 after 2 years, cuckatoo34 after 4 years... That means we'll be mining cuckatoo42, using 1TB, in only 512 years. Mark your calendars!"

When critics questioned the complexity and novelty of Cuckoo Cycle compared to proven algorithms like SHA-256, Igno offered a characteristically thoughtful defense:

"Proof of work security does not exist in a vacuum. It's useless if not enforced by a node. The validation of a Cuckoo Cycle is extremely simple and short. I can look at an implementation and see if it's correct fairly quickly. SHA3 or other complex hash functions, not so much."

He continued: "I can explain how Cuckoo Cycle works and why it does. Most hash functions are pretty much black magic at this point, where the right series of gates and logical operations gets stapled one after another to provide more entropy."

The rationale went beyond mere technical preference. As Tromp put it: "To boldly go where no blockchain has gone before."

## Yeastplume's Marathon

Throughout the fall of 2018, Yeastplume's weekly progress updates chronicled the relentless work required to ship a cryptocurrency. His October 5th update captured the pace: "It looks as if T4 is about a week or so away, and most of the work that needs to go in before we can give it a quick pre-deployment test is done."

The updates revealed not just technical progress but the philosophy underlying Grin's development. When explaining why Grin used Rust rather than C++, Yeastplume offered a perspective born from experience:

"When you write code in Rust, it does exactly what you think it's going to do, every time. A lump of C/C++ code of any meaningful size rarely gets itself into a state where it does what's intended without a considerable amount of time spent in front of a debugger tracing down odd threading issues, investigating segfaults, and dealing with general weirdness."

He wasn't just making a language choice—he was making a statement about software quality. "Because Grin uses rust, we rarely have to deal with this sort of oddness, which frees up time to focus on the actual issues rather than spending weeks in LLDB."

The miner integration work proved his point. "Over the last two weeks I integrated 3 solvers into cuckoo-miner, and each and every time I spent hours tracking down obscure issues that would either have been caught at compile time if those portions of the code had been using Rust, or simply not have been able to happen in the first place."

## GrinCon0

On November 9, 2018, the Grin community gathered in Berlin for GrinCon0—the project's first physical conference. For a project built by pseudonymous developers, meeting in person was both significant and slightly surreal.

Yeastplume's pre-conference update captured the tension between building and presenting: "Bit all over the place this week, as it was shortened due to bank+school holidays (i.e. everyone else gets a holiday while I have to contain Yeastlings,) and also filled with an urgent need to get two coherent and non-embarrassing presentations together."

The presentations themselves—covering wallet architecture, the general Grin introduction, and technical deep dives—were livestreamed and recorded. The event marked Grin's transition from a niche project followed by cryptocurrency insiders to something with broader visibility.

## Floonet: Dress Rehearsal

On December 21, 2018—just days before Christmas—Grin launched Floonet, its long-running testnet. Unlike previous testnets (numbered T2, T3, T4), Floonet was designed to persist, serving as a permanent staging environment for protocol updates.

Igno's announcement was characteristically direct: "Grin's last and long running testnet, the Floonet, has just been released. Please update your nodes and don't forget to clean your ~/.grin from any remaining Testnet4 data."

But he also laid out crucial details about the upcoming mainnet launch:

"The grin mainnet genesis block will include a recent (as in last hour or two) bitcoin block hash, to prove the absence of pre-mine and a fair launch. The grin mainnet genesis block will also set a very high starting difficulty, for similar reasons. Don't be surprised if the first few blocks take an hour or two."

The plan was deliberately conservative: "Once created, the genesis block will be immediately pushed to our github repository and a normal Grin build will get you a mainnet node. No block will be valid for about 30 min after the genesis is published to leave everyone time to rebuild and restart."

Yeastplume's post-Floonet reflection was uncharacteristically sentimental. After describing how he'd set up a new mining rig, installed Grin from scratch, and watched it sync and mine successfully, he stepped back:

"When I look at these things in front of me, I feel proud. And I mean for real, not like you're at some corporate launch party with a few project managers pretending to give a shit. Everyone involved in Grin's development should spend a few minutes sitting there bonding with this daftly-named Floonet, and feel some genuine pride, because there's genuinely something here to be proud of. And that's not something you get to feel much of in this life."

He acknowledged the community that had built up around the project: "And that's just a small sampling of community projects. On the wallet side we have a few upcoming projects, such as Grinbox, as well as quite a few mobile wallets being built. Open CL miners are being worked on... If I've missed anyone I apologize, but think it's safe to say that a completely open-source coin with this kind of quality community infrastructure in place is a rarity to behold."

## The Final Countdown

In the first week of January 2019, Yeastplume focused on documentation—creating guides for running nodes, using wallets, and mining. "Basically a lot of work getting the wiki filled with some Grin noob guides and a large pass over the wallet user documentation."

The technical polish continued: wallet recovery improvements, performance optimizations, and a critical libsecp bug fix. "Very glad this was caught in floonet," Yeastplume noted of the latter, "as it would have made some outputs under certain conditions hard to recover."

His January 11th update ended with words that captured the moment: "Speaking of that, Mainnet is launching in 4 days. Enjoy the weekend."

Two years of work—from Igno's first commit to testnet iterations to conference presentations to documentation—had led to this point. The genesis block awaited its bitcoin hash. The difficulty was set high. The community was ready.

January 15, 2019, was four days away.



---


# Chapter 4: Launch Day

At 6:48 PM UTC on January 15, 2019, the Grin genesis block was mined. The hash of Bitcoin block 558,994—mined just hours earlier—was embedded in the genesis data, proving to the world that no pre-mining had occurred. After two years of development, Grin was live.

## The Opening Hours

The first blocks came slowly, as planned. Igno had warned the community: "Don't be surprised if the first few blocks take an hour or two." The initial difficulty was deliberately set high to prevent anyone from stockpiling coins in the opening moments.

Within hours, the forum erupted with activity. Mining software developers raced to release optimized builds. Pools opened their stratum servers. GPU owners around the world pointed their cards at this new network with its unusual proof-of-work algorithms.

The numbers told the story of frantic adoption. By January 17th, just two days after launch, total network hashpower had grown from nothing to over 200,000 graphs per second. Within weeks, it would exceed 600,000.

Mining pools appeared seemingly overnight. Grinmint, which had supported Floonet testing, was ready for mainnet. F2Pool and Sparkpool—massive operations that mined multiple cryptocurrencies—added Grin support. Smaller pools like mwgrinpool served those who preferred decentralization over reliability.

The dual proof-of-work system created an unusual landscape. Cuckaroo29, the ASIC-resistant algorithm, dominated with 90% of rewards. GPU miners with 4GB, 6GB, and 8GB cards could all participate, though performance varied dramatically. A GTX 1080Ti achieved about 7 graphs per second on Cuckaroo29; a GTX 1060 managed only 3.2.

Cuckatoo31+, the ASIC-friendly algorithm, remained the domain of high-end hardware. Only cards with 8GB or more VRAM could attempt it, and even then, the memory requirements pushed hardware to its limits.

## John Tromp's License

Amid the launch excitement, John Tromp had a question for the commercial miner developers: "May I ask how you are complying with the license?"

Tromp's Cuckoo Cycle code carried what he called a "fair mining license"—a requirement that commercial software using his algorithms donate a percentage of mining proceeds to Grin's development fund. It was a clever mechanism: instead of taking a developer tax at the protocol level, Tromp had embedded the obligation in the software license.

Not everyone complied. When one miner developer promised to DM details about their compliance plan, Tromp waited. Days passed. "Nothing received," he wrote. "Please respond timely to compliance requests."

The exchange highlighted a tension that would persist: Grin had chosen to fund development through voluntary contributions rather than mandatory protocol fees. This required goodwill from miners, pools, and software developers—goodwill that wasn't always forthcoming.

## Early Disappointments

On January 21st, less than a week after launch, Igno Peverell posted a message titled "Early disappointments." It was unusually direct:

"Grin was started with as fair of a launch as possible for what's under our control. We did this for good reason: we believe in Grin's mission. I think I made pretty clear that to continue forward, the project would still need help. And yet Yeastplume's campaign is still very far from being even 10% funded."

The message wasn't aimed at the longtime community members who had supported Grin through its development phase. "This is directly addressed to some of the new funds, miners, mining pools and exchanges that have entered this ecosystem since the launch and benefited from it."

The numbers were stark. Professional mining operations were earning substantial revenue from the new network. Major pools were processing millions of dollars worth of transactions. Yet the developer funding campaigns remained largely empty.

"So please, forward this to those you think this message concerns," Igno wrote. "Perhaps a Chinese translation would be a good thing. Make everyone aware of our needs. We have a long way to go, this can certainly be fixed. And keep in mind that Grin will profit infinitely more from the contributions of a great developer like Yeastplume than from any single additional miner, exchange or fund."

Community members expressed frustration. "I know so many normal individuals who were so excited about this coin for so long and literally none of them are happy with the way things went following launch," wrote one. The concern wasn't about the technology—it was about the ecosystem that had formed around it.

## The Community Responds

The appeal worked. Within days, donations began flowing to Yeastplume's funding campaign. Sparkpool, one of the largest mining pools, announced a contribution. Individual miners pitched in what they could.

Grinmint announced plans to implement a fee structure: 2% for pool operations, plus an additional 0.5% dedicated to Grin development. It wasn't perfect—some argued the development share should be larger—but it established a precedent.

"Looks like you all decided to prove me wrong, I like it!" Igno wrote in a follow-up. "Thanks a ton to keepwalking1234 and Sparkpool, as well as everyone who pitched in after this email. This is very much appreciated and it looks like Yeastplume is fully funded for this new period, which is awesome!"

The episode revealed both the challenge and the strength of Grin's model. Without a treasury or foundation drawing mandatory fees, development funding would always require active community support. But when that support materialized, it came from genuine belief in the project rather than coercion.

## The First ASICs

Even before launch, ASIC manufacturers had taken notice. In January 2019, Obelisk—a company known for its Sia mining hardware—announced the GRN1, a Cuckatoo31 miner.

"Obelisk is excited to announce the GRN1, a cuckatoo31 miner," the announcement read. "We are looking forward to work with the community and targeting its ASIC friendly family of algorithms."

The announcement sparked debate. Some community members welcomed the validation of Grin's design—the dual-PoW system was working as intended, with manufacturers willing to invest in ASIC development. Others urged caution.

"Anyone considering this is cautioned to look at Obelisk's history of shipping ASICs way late and way below spec," wrote one skeptic. Obelisk's previous products had faced delays and underperformed their specifications.

Tromp provided technical context: the GRN1 would be competitive until April, at which point the weight of Cuckatoo31 would decrease enough that Cuckatoo32 miners—requiring more memory—would become necessary. "Beyond April the weight of CC31 becomes low enough that CC32 miners will likely out compete them."

This was the dual-PoW system working as designed. Memory requirements would increase over time, preventing any single generation of ASICs from dominating indefinitely. Manufacturers would need to continue investing in new designs, or their hardware would become obsolete.

## A Network Takes Shape

By the end of January 2019, Grin had transformed from a development project into a living network. Blocks were being mined every minute. Transactions were flowing. Pools and miners had established an ecosystem, imperfect but functional.

The challenges were real: funding remained precarious, the user experience was rough, and the transaction model confused newcomers accustomed to Bitcoin's simpler address system. But the core promise—private, scalable, decentralized digital cash—was now running on real hardware, secured by real proof-of-work.

The community that had built Grin in the open was now maintaining it in the open. The first hard fork was six months away. The work continued.



---


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



---


# Chapter 6: First Hard Fork

On July 17, 2019, at block height 262,080, Grin executed its first scheduled hard fork. The upgrade had been planned since before mainnet launch—part of the project's commitment to iterating on the protocol during its early years. What happened on that day would set the tone for the network upgrades to follow.

## The v2.0.0 Release

Two weeks before the fork, Yeastplume announced the release of Grin v2.0.0 and grin-wallet v2.0.0. The changes were substantial but focused:

"Changes in these releases have been almost entirely focused on hard fork support and ensuring the entire ecosystem will be running the same version of the transaction-exchange format (the Slate) post-upgrade."

The node included support for Blockheader version 2, a tweaked secondary proof-of-work algorithm called "Cuckarood," and a new Bulletproof rewind scheme. The wallet dropped support for older slate versions and API versions—a clean break that would simplify maintenance going forward.

The compatibility table told the story: pre-2.0.0 nodes and wallets would simply stop working after block 262,080. Everyone needed to upgrade.

"Please be advised that a breaking upgrade will happen at block height 262,080 and pre-2.0.0 wallets and nodes will stop working at this point," the announcement warned. "All users will need to upgrade to version 2.0.0 in order to be able to continue using Grin."

## A Smooth Transition

The hard fork itself was anticlimactic—which was exactly the point. Nodes upgraded. Miners switched to the new algorithms. The network continued producing blocks.

Mining pools had a rougher transition. Some took days to update their payout systems to work with the new wallet format. "3-4 days of mining there with unpaid status," reported one miner about their pool experience. Hard forks are never easy, even when they're scheduled.

But the core protocol transition worked. The months of preparation, the careful versioning, the compatibility matrices—all of it paid off. Grin had demonstrated that it could upgrade itself without drama.

## Community Conversations

With the hard fork behind them, community members turned to bigger questions. A forum thread titled "Opinions regarding Grin" captured the mood six months after launch.

The thread began with praise: "Developers must be commended for their hardwork and effort during the past 4 years. It's almost completely unheard for a team to undertake a massive project such as this... with no reliance on corporations and institutions."

But concerns followed. Where was the security audit report? What exactly was the relationship between the dual proof-of-work algorithms and ASIC manufacturers? How would Grin compete with the forks and clones that were emerging?

Jasper van der Maarel, who had become increasingly central to the project, responded with characteristic directness: "Grin *is* the community. Or at least that is what it aims for. So if you think the project needs to do certain things or needs to start certain discussions, you are more than welcome to start on them."

## The Adoption Question

A dedicated thread on increasing Grin adoption drew passionate responses. One community member articulated what many felt:

"I have been following Grin now for a few months. It has astonished me how it towers above other cryptocurrencies. It is by far the new paradigm for privacy coins. The only videos and articles I have read have been pitched at an enthusiast crowd. I have wondered why this coin does not have a marketing team."

The suggestions were practical: an official GUI wallet (or at least one vetted by the council), Ledger hardware wallet support, more exchange listings, better liquidity.

The core team's response was consistent with their philosophy: they would build the tools, but community members needed to drive adoption efforts themselves. "If you think 'trying to get the masses to mine grin' is a worthwhile cause, feel free to devote your time to it," wrote jaspervdm.

This wasn't dismissiveness—it was a genuine belief that sustainable growth came from distributed effort rather than centralized marketing. Whether that belief was correct remained to be seen.

## Security Audit Progress

The security audit that had been commissioned with community funds was nearing completion. Joltz, who had taken point on security matters, provided transparency about the process:

"Regarding the last audit, my understanding is that the core team has had it for about two months. This still gives us an opportunity to publish around the 90 day mark."

He outlined the process: the team would review issues and fixes, auditors would verify the remediations, and then the public reports would be released jointly. It was methodical, responsible work that didn't make for exciting announcements but was essential for the project's credibility.

"I think it's pretty neat that a donation-based decentralized project was able to receive an audit of this quality, address the findings and ultimately share it with the community in a (somewhat) reasonable timeline," Joltz observed.

## Another Coinbase Donation

On November 11, 2019, Lehnberg announced the receipt of another anonymous coinbase donation to Grin's General Fund—a second gift of early-mined Bitcoin, echoing the May donation that had electrified the community months earlier.

Lehnberg shared excerpts from a brief exchange with the donor, who wished to remain anonymous: "I know how you treated the last donation, this is why I am contacting you." The donor's message struck a tone that resonated deeply with the community's values: "It feels like 2009/2010 again... It's wonderful that we have GRIN now, our motives are not economical! It's about the technology and the protocol."

The donor addressed the development team directly: "We saw your work and your ethics towards the project and your interest free work. This is what we are honouring right now with these donations so that you can work freely on GRIN. Without economic dependencies."

The message concluded: "Hopefully we judged it right, time will tell."

The back-to-back coinbase donations—both from early Bitcoin miners who had chosen to support Grin with coins worth hundreds of thousands of dollars—sent a signal that went beyond funding. Someone who had been present at the dawn of Bitcoin saw something in Grin worth backing.

## GrinCon1 and the Cuckaroom Unveiling

In November 2019, the Grin community gathered for GrinCon1, the project's second major conference. Among the presentations, Tromp unveiled Cuckaroom—the next evolution in the Cuckaroo family of ASIC-resistant algorithms.

The announcement marked the latest step in Grin's planned proof-of-work transitions. Just as Cuckaroo had been active for only six months (January through July 2019), Cuckarood would reach the end of its life at the second hard fork in January 2020. Its successor would be Cuckaroom.

"Its successor, and latest member of the Cuckoo Family, 'Cuckaroom', was unveiled last Friday at GrinCon1," Tromp wrote to the forum. The name revealed the algorithm's key innovation: the 'M' stood for "Monopartite." Unlike the bipartite graphs used in Cuckaroo and Cuckarood, Cuckaroom's graph structure allowed cycles of all possible lengths—including odd ones, and even single-node "unicycles."

The technical changes were deliberate. Where Cuckarood had tweaked the underlying hash function and cycle type, Cuckaroom instead modified the edge block computation while reverting to standard siphash. The new approach meant that miners would need to perform twice as many rounds to trim edges, and the expected solution rate would drop from 1/21 to 1/42.

"So we can expect a large drop in C29 solution rate come hardfork time," Tromp warned, "from slower solvers, halved solution rate, and the seemingly unavoidable unprepared miners. However, difficulty should adjust within a matter of hours."

The progression was now clear: Cuckarood, then Cuckaroom, and eventually Cuckarooz. Each iteration represented another round in the ongoing arms race to keep GPU mining viable while ASICs were being developed for the ASIC-friendly Cuckatoo algorithm.

## Looking Ahead

The first hard fork marked a transition point. The frantic energy of launch had settled into the steadier rhythm of ongoing development. The next hard fork was scheduled for January 2020—six months away. Then another in July 2020, and a final one in January 2021.

After that, the scheduled forks would end. The protocol would stabilize. The secondary proof-of-work would phase out entirely, leaving only the ASIC-friendly Cuckatoo algorithm. Grin would become what it was always meant to be: a stable, privacy-preserving currency that could run for decades without requiring users to constantly upgrade.

But that was still eighteen months away. For now, there was work to do: wallets to improve, features to add, a community to nurture. The first hard fork had proven that Grin could evolve. The question was what it would evolve into.



---


# Chapter 7: The Hard Fork Years

Between January 2020 and January 2021, Grin executed three scheduled hard forks—the final three in its planned series. Each upgrade brought protocol improvements and tested the community's ability to coordinate. But the period was also marked by broader challenges: a global pandemic, difficult conversations about Grin's direction, and the beginning of a transition away from the founding team.

## v3.0.0: The Second Fork

On January 20, 2020, Grin completed its second hard fork at block height 524,160. Yeastplume's assessment captured the mood: "'Boring and uneventful.' Terrible review for your new Netflix series, but the highest praise you could possibly receive for your Hardfork."

The upgrade introduced Cuckaroom, the third member of the Cuckaroo family of ASIC-resistant algorithms. Following Cuckarood from the first hard fork, Cuckaroom represented another iteration in the ongoing effort to keep GPU mining viable. As Tromp had unveiled at GrinCon1, Cuckaroom made further tweaks to edge block computation and moved to a monopartite graph structure, allowing cycles of all possible lengths. This was the middle step in the Cuckaroo progression—Cuckarood, then Cuckaroom, and eventually Cuckarooz.

The upgrade had gone smoothly—Floonet testing had worked, and mainnet followed without incident. But Yeastplume was already looking ahead, outlining priorities for the coming year: an interactive CLI mode for the wallet, better API documentation, improved testing infrastructure, and progress toward standardized offline transactions.

"Grin is markedly better than it was one year ago," he wrote, "and I fully intend to be saying something similar around this time next year."

## A World Gone Mad

By March 2020, the COVID-19 pandemic had disrupted life worldwide. Yeastplume's updates reflected the new reality: "World has gone slightly mad since my last update, and with a Yeastlair full of 7 people with varying degrees of neediness, some challenges have been thrown into my usual routines."

Development continued despite the disruption. The team focused on "compact slates"—reducing the data required for the first round of transaction building to enable new interaction methods like QR codes. It was the kind of careful, methodical work that improved the protocol incrementally but didn't make headlines.

"You most probably have greater worries at the moment than the state of a particular cryptocurrency," Yeastplume acknowledged, "but rest assured myself and everyone on the Grin team plan to keep plugging away as best we can."

## The Elephant in the Room

In late March 2020, a forum post titled "Let's talk about the elephant in the room" crystallized concerns that had been building for months:

"Bottomline is: Grin is an exciting project with fascinating tech that might fail to gain traction and become one of many dead ends in the cryptocurrencies world. What can be done about this?"

The post acknowledged the developers' hard work but raised uncomfortable questions. Big exchanges weren't listing Grin. New users weren't joining. The price had collapsed from launch highs. What made Grin different from countless other projects that had faded into obscurity?

Daniel Lehnberg's response, numbered and comprehensive, addressed the concerns head-on:

"Generally speaking, any proposal that's well argued, shows reason, follows logic, is full circled and is argued in good faith, seeking to discover some constructive improvement rather than trying to be right for the sake of being right or for the sake of inflating your own ego, I think will be at least *considered*."

On the general fund being held in Bitcoin rather than Grin: "The general fund being detached from Grin price fluctuation I think is a feature, not a bug... Look around at other projects, living and dying with the price of their coin. You end up being very short sighted, doing what you can right now to move the price, rather than focusing on stuff that makes sense in the longer term."

On sustainability: "At some point though, the funding will run out, and donations will dry up. It's okay. The project was literally broke and launched one of the most anticipated blockchains with $0 spent on protocol development... Unlike other projects, I think Grin will do just fine without any funding, we never even expected to have funding in the first place."

And for those who disagreed fundamentally with the project's direction, Lehnberg offered a sincere invitation: "Grab a few likeminded buddies, fork the repo, setup your own forum and keybase group, and there you go! Call yourselves Grin PRO, Grin X or whatever you like. If you follow the consensus rules, your node will be treated just like any node on the network."

## v4.0.0: The Third Fork

On July 16, 2020, Grin's third hard fork arrived at block height 786,240. The release introduced important technical improvements: compact slates that reduced transaction size, better Tor integration, and the deprecation of insecure API versions.

The secondary proof-of-work algorithm changed to Cuckarooz—another iteration in the ongoing effort to keep GPU mining viable against ASIC development. It would be the last such change; after the fourth hard fork, the ASIC-resistant algorithm would phase out entirely.

## v5.0.0: The Final Scheduled Fork

On January 21, 2021, at block height 1,048,320, Grin completed its fourth and final scheduled hard fork. The moment marked an important milestone: the end of the planned upgrade cycle that had been announced before mainnet launch.

The secondary proof-of-work—the ASIC-resistant Cuckaroo family—began its final phase-out. Over the following months, its share of block rewards would decline to zero, leaving only the ASIC-friendly Cuckatoo algorithm. The dual-PoW experiment was drawing to its planned conclusion.

The hard fork also brought relative kernel locks—a feature that enabled time-locked transactions relative to their inclusion in a block. This laid groundwork for future features like payment channels, though implementing those features would require additional wallet work.

## The Inflation Bug

Just two months after the final scheduled hard fork, Grin faced one of the disaster scenarios the governance framework had anticipated: an inflation bug that allowed arbitrary creation of coins.

On March 18, 2021, something strange happened. The Grin++ node—David Burkett's independent C++ implementation—refused to accept block 1,136,081. The official Rust node accepted it without complaint. When two implementations of the same protocol disagree about validity, something is deeply wrong.

David Burkett's warning was immediate and stark: "Do not use Grin right now at all while we investigate."

Within hours, the team identified the problem. John Tromp explained the technical flaw: "The former code accepted a rangeproof BP for output commitment O, if BP appeared in the verifier cache as having been verified before. This logic was faulty since the earlier verification was not necessarily against the same output commitment. The earlier verification could be against a different output, while the new one commits to a negative value."

In other words, an attacker could reuse a valid range proof from a legitimate output to validate a completely different output—one that created coins from nothing. It was an elegant exploit of a subtle caching optimization, and it had been executed deliberately. As one community member observed: "This was an attack by someone with good understanding of Grin and the rust implementation."

Antioch released v5.0.3 within hours. The fix mitigated the cache issue, rewound the invalid block, and improved peer banning. All miners were urged to upgrade immediately to build work on a valid chain. Exchanges and users were told to halt transactions until sufficient work had been built beyond the invalid block.

The community response was mixed. Some users complained bitterly about the "rollback" affecting their transactions. "I think this fork is very stupid, never think about the ones who received grins after block 1136081," wrote one frustrated user. Others demanded compensation for lost coins.

But the broader community understood what had happened—and what hadn't. The attack had been detected and stopped before significant damage was done. No one had successfully inflated Grin's supply. The network had proven resilient.

The lesson was clear: having multiple independent implementations wasn't just a nice-to-have—it was essential infrastructure. Grin++ had caught what the Rust node missed precisely because it didn't share the same caching logic. Diversity of implementation had saved the day.

"Nice example of the benefits of having two independent node implementations," observed Anynomous, the community member who had helped coordinate the response.

The inflation bug validated the governance framework's foresight in planning for "cryptographic weaknesses leading to arbitrary inflation." It also demonstrated that the community could execute a coordinated emergency response without the original core team. Grin had survived its most serious crisis through the same decentralized cooperation that had built it.

## Stability at Last

With the final scheduled fork complete, Grin entered a new phase. The protocol was stable. Users and miners could expect that the consensus rules they learned today would remain valid indefinitely. ASIC manufacturers could invest in hardware confident that their designs wouldn't be invalidated by the next fork.

The frantic pace of scheduled upgrades was over. The question now was what Grin would become without that forcing function—whether the community could maintain momentum and continue improving the project without the pressure of deadline after deadline.

The hard fork years had proven that Grin could evolve deliberately, executing complex coordinated upgrades without the drama that plagued other projects. They had also surfaced deeper questions about adoption, sustainability, and purpose that the next phase of Grin's development would need to address.



---


# Chapter 8: Governance Evolution

As the scheduled hard forks concluded, Grin's governance was transforming. The informal "technomity" that had guided the project through launch and early development was giving way to something more distributed. Key contributors were stepping back. New voices were emerging. The project was becoming what it had always claimed to be: a truly community-driven endeavor.

## The Core Team Transition

The departure had been gradual rather than sudden. Igno Peverell, Grin's founding developer, had faded from the project in 2019—his last forum posts appearing that August. There had been no dramatic announcement, no explanation. One day he was there; over time, he wasn't.

Lehnberg acknowledged the loss openly: "We never expected to find ourselves a few months after mainnet having launched without Igno. Core team members were all looking to Igno for leadership, and he disappeared way too early. We're definitely not perfect, and none of us are close to having the leadership qualities that Igno had."

The remaining core team—Yeastplume, Lehnberg, jaspervdm, antioch, and others—had to fill the gap. There was no playbook for this. Grin had been designed to survive the loss of any individual contributor, but theory was different from practice.

## Research and Funding

One sign of maturation was the emergence of funded research proposals. In April 2020, a researcher using the pseudonym DrazenV submitted a request for €5,000 to investigate BLS signatures—specifically whether they could enable kernel aggregation in Grin.

The proposal sparked debate about standards and transparency. How should the community evaluate anonymous researchers? What credentials were required? How much should specialized work cost?

"My formal education is at the level of a PhD, which is in mathematics and specifically the mathematics of public key cryptography," DrazenV wrote. Some community members questioned the phrasing. Others questioned whether a month of research was worth €5,000.

Antioch offered a constructive path forward, suggesting the work be split into prerequisites and subsequent research: "Maybe one way to approach this would be a 'literature review' to summarize where we stand today... This would give us a solid baseline and starting point for evaluating further possible research."

The discussion illustrated both the promise and challenge of decentralized research funding. Without a foundation or academic institution to vet proposals, the community had to develop its own standards.

## The Yeastunit

Developer compensation had coalesced around what the community informally called a "yeastunit"—€10,000 per month, the rate established by Yeastplume's original funding campaigns. It became the standard against which other proposals were measured.

Antioch's funding requests showed how the process worked in practice. Each quarter, developers would submit proposals detailing their planned work, past contributions, and funding needs. The community would discuss, question, and ultimately decide whether to approve.

"I would like to request a further 3 months of funding to cover July through to September," Antioch wrote in one such request. "This would be for the standard yeastunit of €10k/month."

The transparency was notable. Every proposal was public. Every discussion was recorded. Anyone could participate—and anyone could object.

## New Directions

As the scheduled forks concluded, developers' attention shifted toward features that could improve Grin's usability without requiring consensus changes. Antioch outlined several possibilities:

"Mostly lock-free transactions"—reducing the time users needed to wait for transactions to complete. PayJoin—a technique for improving privacy by having recipients contribute inputs to transactions. Multi-party outputs for atomic swaps. Payment channels leveraging the newly-enabled relative kernel locks.

"These all share some commonality," Antioch observed, "specifically around the interactive transaction building process, fine-grained control over output selection and kernel offset adjustments."

The work would be challenging—it required changes to how wallets built transactions without breaking compatibility or introducing security vulnerabilities. But it represented the kind of incremental improvement that could make Grin more practical for everyday use.

## Community Council

The governance structure continued to evolve. The original "technomity"—the technocratic council of core contributors—began transitioning toward a broader community council model. The change reflected both philosophical commitment and practical necessity: as original contributors stepped back, new participants needed paths to involvement.

The shift wasn't always smooth. Debates arose about decision-making processes, fund allocation, and the balance between technical purity and practical adoption. But the debates themselves were evidence of a healthy community—people cared enough to argue.

## The RFC Process

Technical decisions increasingly flowed through a formal RFC (Request for Comments) process. Proposals were submitted as pull requests, discussed publicly, and merged only after community review.

The process brought discipline to decision-making. Ideas that might once have been implemented on a developer's whim now required written justification, community feedback, and explicit approval. It slowed things down but improved quality and buy-in.

RFCs covered everything from spending guidelines for the general fund to technical standards for transaction building. They became the project's institutional memory—a record of not just what was decided but why.

## Looking Forward

By the end of 2021, Grin's governance had matured significantly from its early days. The informal coordination among a small group of developers had given way to documented processes, community councils, and formal funding mechanisms.

The transition wasn't complete—governance never is. But the foundation was solid. Grin had demonstrated that a cryptocurrency project could evolve its social structures as deliberately as its technical ones.

The question facing the community was no longer whether it could survive without its founders. It was what it would build now that it had proven it could.



---


# Chapter 9: Decentralized Development

With the scheduled hard forks complete and governance structures evolved, Grin entered a new phase of community-driven development. The project's survival no longer depended on any single contributor or organization. What emerged was a distributed effort—sometimes slow, sometimes inefficient, but remarkably resilient.

## The Community Council

The Grin Community Council (GrinCC) became the primary vehicle for coordinating development and managing funds. Unlike a traditional foundation with paid staff and formal hierarchy, the council operated as a loose coordination mechanism among volunteers.

The council maintained a wishlist of desired features, prioritized by community input:

**Critical priorities** included PIBD (Parallel Initial Block Download)—a faster and more robust syncing strategy that would dramatically improve the experience for new users—and multisig support, though the latter remained elusive due to unsolved cryptographic challenges around threshold range proofs.

**Important features** included Tor support for nodes, light node implementations, and PayJoin transactions for improved privacy.

The wishlist reflected the community's practical focus: make Grin easier to use, more robust, and more private. Grand visions took a back seat to incremental improvements that real users needed.

## Product Thinking

A forum thread titled "Grin product wishlist" captured a shift in how the community thought about development. Rather than starting with technical features, contributor trab proposed starting with user needs:

"What are some products that incorporate grin that you would like to see? My goal is for us to think from a product perspective so that maybe it will become more obvious what is *missing* from a *framework/foundation* perspective."

The suggestions were practical: a Venmo-style wallet for sending money to friends, a point-of-sale system for small businesses, a web wallet that could plug into applications with a simple library include.

Anynomous, a longtime community member, responded with context about what already existed and what remained to be built. View keys were in the code but lacked tooling. Payment proofs were on the wishlist but not high priority. PIBD and a GUI wallet came first.

The discussion revealed both the community's ambitions and its resource constraints. Without venture funding or a foundation treasury, development proceeded at whatever pace volunteers could sustain.

## The Contracts Branch

Yeastplume continued his work on what he called the "contracts" branch—an experimental version of the wallet with improved transaction flows and early payment proofs. The work aimed to make Grin transactions more robust and user-friendly without requiring consensus changes.

"Early payment proofs working and enabled by default in the contracts branch of the wallet," Yeastplume announced in 2025. The feature allowed parties to prove that payments had occurred—essential for commerce but surprisingly difficult to implement in a privacy-preserving way.

"Really, the best way to get payment proofs live would be to get the experimental contracts branch working within Grim and test, test, test to the point where we'd be comfortable merging all of the work in the contracts branch to master."

The mention of Grim—a GUI wallet built by community developer ardocrat—illustrated how the ecosystem had matured. Multiple wallet implementations existed, each with different strengths, all interoperable through Grin's transaction protocol.

## Decentralized Infrastructure

The messaging question—how to coordinate interactive transactions across the internet—sparked ongoing research. One thread explored various peer-to-peer protocols that might work for a "Venmo-style" Grin experience:

Reticulum, Waku, Gun, Nostr, XMPP, Matrix, Hypercore, libp2p, Yggdrasil—the community evaluated each against criteria like forward secrecy, centralization risk, and ease of integration.

"The problem with matrix is that the rooms, and room participants are known to the server admins," trab wrote. "This makes Matrix a non-starter for this use case."

The research didn't produce immediate results, but it demonstrated the community's technical sophistication and willingness to explore unconventional solutions.

## Sustainability

Without guaranteed funding, development operated on a different timescale than venture-backed projects. Features that other cryptocurrencies might ship in months took years in Grin. But features that shipped stayed shipped—there was no pressure to pivot, no investors demanding returns, no threat of the project being sold or shut down.

The community council funded work through donations, allocating resources carefully and transparently. Every spending decision was discussed publicly. Every funded contributor submitted regular progress reports.

It wasn't fast. It wasn't flashy. But it was sustainable.

## The Long Road

By the mid-2020s, Grin had outlasted many cryptocurrencies that had launched with larger teams and bigger budgets. The protocol worked. The community persisted. Development continued.

The questions that had seemed urgent in 2019—Would Grin gain mainstream adoption? Would it compete with better-funded privacy coins?—had resolved into something more modest but perhaps more meaningful. Grin existed. It served the users who needed it. It would keep serving them for as long as anyone cared to maintain it.

That was, perhaps, the best outcome a decentralized project could hope for: not explosive growth or world-changing adoption, but quiet resilience. Grin had become what its founders intended: a tool that would outlast any individual contributor, maintained by a community that believed in its mission.



---


# Chapter 10: Legacy & Future

In June 2019, the Grin community received news that everyone had been dreading but no one wanted to acknowledge. Igno Peverell, the project's founder, was stepping away.

## The Announcement

Yeastplume delivered the message on behalf of the council:

"As some have already noticed, Igno has not been very active over the past few weeks. He recently communicated to us in the council that he needs to be away from the project for a while for personal reasons. We do not have further details on his situation or a timeline for his return, but we anticipate he will be absent for at least a few months, possibly more."

The announcement was deliberately understated. No drama. No speculation about reasons. Just acknowledgment of the facts and a statement of continuity: "As Grin is open source and not reliant on any single person or group in order to progress, our work continues uninterrupted in his absence."

Yeastplume included a message from Igno himself: Grin was "in the best hands possible." This was directed not just to the council but to the community as a whole.

## Speculation and Reality

The community reacted with a mix of concern and curiosity. Some speculated that Igno had moved on to other projects. Others noted the timing with various cryptocurrency launches. The rumor mill churned.

But for those who had worked closely with Igno, the personal nature of the departure seemed genuine. As one community member observed: "Life is complicated. Terrible events can occur and come seemingly out of nowhere, loved ones can get sick or, god forbid, pass away suddenly. Really, there are dozens of reasons why Igno might actually need to take time away from a project like this for personal reasons."

The months passed. Igno's August 2019 forum post would be his last.

## I Am Ignotus

A community member proposed a tribute: signing forum posts with "I am Ignotus"—a reference to the "I am Spartacus" scene, where characters claimed a shared identity to protect their leader.

The initiative sparked debate. Some found it moving. Others thought it performative or premature—Igno wasn't dead, after all. The moderators eventually clarified that their existing rule against signing posts applied regardless, though the rule had nothing to do with censorship.

The episode illustrated something important about the Grin community: even in tribute, it valued substance over spectacle. The best way to honor Igno wasn't through symbolic gestures but through continued work on the project he had started.

## What Igno Built

Igno Peverell's contributions to Grin and cryptocurrency more broadly were substantial:

**The implementation itself**: Igno took Tom Elvis Jedusor's whitepaper—a theoretical sketch—and turned it into working code. From his first commit in October 2016 to his departure in 2019, he built the foundation that everything else rested on.

**The culture**: Igno set the tone for how Grin would operate. Pseudonymous contributors. No ICO. No premine. Transparent governance. Technical rigor. These weren't just policies; they were values that Igno embodied and that the community absorbed.

**The team**: Igno recognized and encouraged talent. Yeastplume, who would become Grin's most prolific developer, was drawn in by Igno's work and vision. So were the other core contributors who would carry the project forward.

**The ethos**: "He never once looked down upon any member of this community," one community member wrote, "and always encouraged everyone regardless of skill-set or background to take part in the project without fear of repercussions or ridicule."

## The Project Continues

Grin's design had always assumed that contributors would come and go. The protocol didn't depend on any individual's continued involvement. The code was open source. The documentation was public. The community owned the project collectively.

This wasn't just rhetoric—it was tested by Igno's departure. And the project survived.

Yeastplume continued his wallet work. Jaspervdm and antioch maintained the node. Lehnberg coordinated governance. New contributors emerged. The hard forks happened on schedule. Development continued. When the inflation bug struck in 2021, the community coordinated an emergency response without missing a beat.

It wasn't the same without Igno. The community had lost something irreplaceable—not just technical skill but a particular kind of leadership, quiet and principled. But it had gained something too: proof that the decentralized ideal actually worked—not just in theory, but under pressure.

## Looking Forward

What will Grin become? The honest answer is: no one knows.

The protocol is stable. The community is resilient. Development continues at whatever pace volunteers can sustain. The scheduled hard forks are complete, and the consensus rules will remain unchanged unless the community decides otherwise through established processes.

Grin may achieve widespread adoption. It may remain a niche tool for privacy enthusiasts and cryptography researchers. It may be superseded by better technology. It may persist quietly for decades, maintained by a small but dedicated community.

All of these outcomes are possible. None of them diminish what has already been accomplished: a group of pseudonymous developers, inspired by a mysterious whitepaper, built a new kind of money from scratch. They did it in the open. They did it without corporate backing. They did it the way they believed software should be built.

The MimbleWimble whitepaper appeared in July 2016. The Grin genesis block was mined on January 15, 2019. The story continues.

---

*"In his message to the council members, Igno stated that Grin was 'in the best hands possible.' This was directed to the community as a whole."*

*—Yeastplume, June 2019*



---


# Appendices


## Timeline of Key Events

### 2016
- **July**: Tom Elvis Jedusor publishes the MimbleWimble whitepaper

### 2017
- **October**: Igno Peverell begins building Grin
- **November**: First public commit to Grin repository

### 2018
- **January**: Grin forum launched
- **March**: Testnet 2 released
- **July**: Testnet 3 released
- **August**: Governance structure ("technomity") established
- **October**: Testnet 4 released
- **November**: GrinCon0 in Berlin
- **December**: Floonet (long-running testnet) launched

### 2019
- **January 15**: Mainnet launch
- **January 28**: GrinConUS in San Mateo, CA
- **July 17**: Hard Fork 1 (v2.0.0)
- **August**: Igno Peverell's last forum post
- **November**: GrinCon1

### 2020
- **January 20**: Hard Fork 2 (v3.0.0)
- **July 16**: Hard Fork 3 (v4.0.0)
- **September**: 1,000,000th block mined
- **December**: Core team dissolution discussions begin

### 2021
- **January 21**: Hard Fork 4 (v5.0.0) - final scheduled hard fork
- **March 18**: Inflation bug detected and mitigated; v5.0.3 emergency release
- Community Council governance model established

### 2022-2025
- Continued community-driven development
- Wallet ecosystem expansion
- Ongoing protocol improvements



---


## Glossary

**ASIC (Application-Specific Integrated Circuit)**: Specialized hardware designed for a specific computational task, in this context, cryptocurrency mining.

**BLS Signatures**: A cryptographic signature scheme that allows for efficient aggregation of multiple signatures.

**Bulletproofs**: A type of zero-knowledge proof used to verify that a transaction amount is valid without revealing the actual amount.

**Confidential Transactions**: A cryptographic technique that hides transaction amounts while still allowing verification of their validity.

**Cuckoo Cycle**: The proof-of-work algorithm family used by Grin, designed by John Tromp. Variations include the Cuckaroo family (ASIC-resistant: Cuckarood, Cuckaroom, Cuckarooz) and Cuckatoo (ASIC-friendly).

**Cut-through**: A MimbleWimble feature that allows spent outputs to be removed from the blockchain, dramatically reducing its size.

**Dandelion**: A privacy-enhancing protocol for transaction propagation that obscures the origin of transactions.

**Hard Fork**: A network upgrade that requires all nodes to update their software to remain compatible.

**Kernel**: In MimbleWimble, the cryptographic proof that a transaction is valid, which cannot be pruned from the blockchain.

**MimbleWimble**: A blockchain protocol that combines Confidential Transactions and CoinJoin-like transaction aggregation to improve privacy and scalability.

**Pedersen Commitment**: A cryptographic commitment scheme used to hide transaction amounts while allowing mathematical verification.

**Range Proof**: A cryptographic proof that a hidden value lies within a certain range, preventing negative or overflow amounts.

**Schnorr Signatures**: A digital signature scheme known for its simplicity and efficiency, used extensively in Grin.

**Slate**: Grin's transaction building format, used to exchange transaction data between sender and receiver.

**Slatepack**: An improved transaction format introduced in later versions, making transactions easier to share.



---


## Key Contributors

This story was built by many hands. While preserving the privacy that Grin values, we acknowledge the pseudonymous and named contributors whose forum discussions form the basis of this narrative:

**Founding Developer**: Igno Peverell

**Core Developers**: Yeastplume, antioch, hashmap, jaspervdm, quentinlesceller, John Tromp (tromp)

**Project Management**: Daniel Lehnberg (lehnberg)

**Community & Governance**: davidtavarez, joltz, phyro, and many others

**And countless community members** who participated in discussions, testing, documentation, and building the ecosystem.

---

*This book was compiled from public forum discussions on forum.grin.mw. All quotes are attributed to their original authors.*

