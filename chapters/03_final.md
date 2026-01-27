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
