# Chapter 3: Road to Launch

*17 topics selected for this chapter*

---

## Scheduled PoW upgrades proposal
*Date: 2018-09-17 | [Forum Link](https://forum.grin.mw/t/scheduled-pow-upgrades-proposal/820)*
*Importance Score: 81.1 | Core Participants: igno.peverell, tromp, jaspervdm, lehnberg*

### Post by @tromp ⭐ (2018-09-17)
*Post #1*

A major motivation for memory hard PoWs is to limit performance by the memory IO bottleneck.

If the memory requirements are set too low, as for instance in the case of Litecoin’s scrypt, then the resulting single-chip ASICs are not meaningfully different from pure computational ones like Bitcoin’s sha256. The same destiny befell Zcash’ Equihash, although they missed the opportunity to set much larger memory requirements at launch. Only ethash has so far succesfully resisted single chip ASICs.

Since the amount of memory that can economically be fit on a single chip grows over time, as one of many illustrations of Moore’s law, it behooves a memory hard PoW to also have increasing memory requirements.
Ethereum’s ethash PoW recognized this in having a linearly growing dataset (growing by 8 MB every 125 hours; see appendix J of <https://ethereum.github.io/yellowpaper/paper.pdf>).

I propose to have a similar linear increase in memory requirements for Grin’s long term PoW, Cuckatoo Cycle.

Specifically, after 2^k years, we will phase out the use of cuckatoo32+k. So cuckatoo32 will be phased out after 1 year, cuckatoo33 after 2 years, cuckatoo34 after 4 years, etc.

That means we’ll be mining cuckatoo42, using 1TB, in only 2^(41-32) = 512 years. Mark your calendars!

I additionally propose the following mechanism for phase out:

Each size cuckatooN has a natural scaling factor of 2^(N+1) * N.
Upon phaseout, the latter factor N will be reduced by 1 every week, until it reaches 0.
For instance, cuckatoo32 difficulty scaling will linearly decrease over 32 weeks, or between 7 and 8 months.

This fixed upgrade schedule relieves us of the need to try identify single chip miners and hardfork away from them. We would instead trust that any advantage of single chip designs is shortlived.

Furthermore, we will be able to tell after the fact, by seeing how much hashpower resides in a size that’s being phased out.

---

### Post by @tromp ⭐ (2018-09-18)
*Post #6*

epigramx:

> Fixing an assumption of an everlasting Moore’s Law

I’m not making that assumption.
That’s why I only let memory grow linearly, not exponentially.

---

### Post by @tromp ⭐ (2018-10-23)
*Post #15*

So that the miners more resemble general purpose computing hardware with separate memory chips, with the potential to accelerate advances in memory technology and adoption thereof. Obsolete mining hardware with lots of fast memory chips also offers more hope of recyclability.

---

### Post by @tromp ⭐ (2018-10-25)
*Post #26*

rodarmor:

> There are many possible layouts, architectures, and memory technologies to use in a high-memory ASIC.

True; Cuckatoo Cycle is as much about board level optimization as about chip level optimization.

rodarmor:

> exotic techniques […] to overcome inter-die communication latency and bandwidth issues.

rodarmor:

> an exotic optimization, perhaps not applicable to other chips

These are challenges that the general computing market is already focussing and competing on (unlike optimizing SHA256 circuitry), so we can expect wider applicability of any optimizations.

rodarmor:

> a manufacturer is likely to mine with their own hardware

As they already do with compute bound ASICs.

rodarmor:

> If smaller graph sizes are periodically made obsolete, in order to prevent single-die ASICs, and older generations of miners are rendered useless

We expect cuckatoo miners to be able to handle multiple graph sizes, to get comparable lifetimes to fixed size PoWs.

rodarmor:

> a new generation of Ethereum ASICs has been released that trounces GPUs and even old ASICs by a huge margin.

They have yet to be released, and if the delayed ETH hardfork switches PoW to ProgPoW we may never see then released. In any case, we saw such leap-frogging in earlier bitcoin days as well. It simply takes many years of ASIC development to significantly reduce the size of leaps.

Altogether I admit there are considerable risks to the experiment. At some point I suggested a long term dual pow model with 50% compute bound and 50% memory bound, but this was deemed too complicated.

---

### Post by @tromp ⭐ (2018-10-26)
*Post #28*

griffen:

> so cuckatoo32 and cuckatoo33 only get 1 year each?

Yes; recall that cuckatoo32+K gets phased out after 2^K years.

griffen:

> how much memory is needed to do mean mining for cuckatoo34?

Let’s say cuckatoo29 requires 3 GB. Then cuckatoo34 needs 2^(34-29) = 32 times more, or 96 GB DRAM, 33% more than what you find in an E3 ethash miner.

That’s why lean mining should be much preferrable, needing only 2 GB DRAM and 2 GB SRAM (or some fraction thereof, by trading off SRAM for extra passes). Note that an Z9 mini Equihas miner has almost 2 GB of SRAM spread over 12 separate ASICs.

---

### Post by @igno.peverell ⭐ (2018-11-07)
*Post #35*

I’ll provide some counterpoints in no particular order. I don’t think any one of them is a definitive win and you’ll likely have a “yes but” for multiple of them. But I do hope that overall they provide enough weight to move your personal balance away from SHA3 (for example) for Cuckoo Cycle.

1. Proof of work security does not exist in a vacuum. It’s useless if not enforced by a node. The validation of a Cuckoo Cycle is extremely simple and short. I can look at an implementation and see if it’s correct fairly quickly. Same for other implementations. SHA3 or other complex hash functions, not so much. I do acknowledge that SHA3 libraries could generally be more reviewed, but that’s not always true and not for all programming languages. So I choose simplicity for security.
2. Cuckoo Cycle is an actual proof of work. This may be more of a point of design or aesthetics, but generally hash functions are _not_. They become one when paired with a network target. But I like that Cuckoo has been designed with a PoW, provides several levels of difficulty and is extremely tweakable.
3. I can explain how Cuckoo Cycle works and why it does. Most hash functions are pretty much black magic at this point, where the right series of gates and logical operations gets stapled one after another to provide more entropy. They provide extreme levels of safety against extreme levels of opacity. Could you see where an XOR is missing and why it needs to be there? I think they’re a hammer and we don’t really have a nail.
4. Speaking of security, what are the goals of the proof of work? I’d personally list them as security, decentralization and distribution. Note that the 2 first are intimately related and I wouldn’t consider the first without the second. A pure hash-based PoW has mostly shown to lead to a winner-take-all situation for whoever can get the most silicon. Only clever chip design has been able to counterbalance that.
5. I see custom ASICs as a local optimum. Even this industry is starting to move toward paired programmable FPGA-like chips to be able to wire up ASIC functionalities differently if the upstream algo changes (see Ethereum miners for example). And this is a fast-changing industry as well. Designing or choosing algorithms just for what this industry can do right now could leave us very ill-prepared for the future.
6. There are multiple possible sources of optimization for Cuckoo Cycle. Is that good or bad? I don’t know, I’ve heard believable arguments on both sides. For what goal? I think this argument is a total wash.
7. On uncertainty of mining hardware improvement, I’m not sure I share your analysis. Uncertainty used to be pretty high for Litecoin for example, even though Scrypt is closer to SHA3 than Cuckoo. I think that uncertainty is inherent to the market and not the PoW design. And so again, picking the design based on the market is, ill-advised IMO.
8. I don’t worry that Cuckoo Cycle solvers are too complex. As mentioned people used to think the same of Litecoin. There’s lots of ingenuity in the hardware design space. And the lean solver is very simple to explain.

I’ll stop here. But overall I think it’s important to realize that currently this is a many-variables problem, with many unknowns. I don’t think there’s one true best answer and I don’t think there’s one best variable we should optimize on either. So in the presence of high uncertainty around the best solution to a problem, I tend to pick something simple but flexible. Cuckoo Cycle is that (and of course some other things too).

---

### Post by @tromp ⭐ (2019-01-10)
*Post #39*

timolson:

> What’s wrong with single-chip ASIC’s?

They’ve been done to death. They’re rather boring IMO.

Grin is taking an admittedly risky gamble on a novel and elegant PoW to find out what benefits competition for the most efficient memory IO can bring. I’m hoping, perhaps against all odds, but hoping still, that we will see some advances in memory technology in the long run (over decades), as such advances can be immediately monetized, whereas they may falter in the overly conservative commodity memory market.

Where every coin was happy with a fixed emission or small tail emission, Grin took the bold step of trying a pure linear emission.

ZCash clearly tried to avoid single-chip ASICs (stressing how Equihash would be “equitable”), but chose its parameters poorly.

timolson:

> But WHY?

To boldly go where no blockchain has gone before.

And because I love answering the question “what algo?” with

finding 42-cycles in random bipartite graphs with billions of nodes…

---

### Post by @tromp ⭐ (2019-01-10)
*Post #40*

timolson:

> IMO it’s easier to read and understand Keccak than Cuckoo. Is it more LOC? Technically yes, but it’s _simpler_ .

I strongly disagree Keccak is simpler. The cycle checking is conceptually trivial; it’s following the 42 edges around the cycle to verify the adjacencies. Any half decent programmer can code that from just the words “42-cycle”. So the real complexity is in the hash function. And Keccak is definitely way more complex than siphash.

timolson:

> CC’s solvers are crazy complex.

Some of them are. Others like the lean miner are quite simple, spending the vast majority of their time in essentially just these few loops

[github.com](https://github.com/tromp/cuckoo/blob/master/doc/simplesolve)

#### [tromp/cuckoo/blob/master/doc/simplesolve](https://github.com/tromp/cuckoo/blob/master/doc/simplesolve)

void count_node_deg(u32 uorv) {
for (edge_t nonce = 0; nonce < NEDGES; nonce++) {
if (alive(nonce)) {
nonleaf.set(sipnode(sip_keys, nonce, uorv));
}
}
}

void kill_leaf_edges(u32 uorv) {
for (edge_t nonce = 0; nonce < NEDGES; nonce++) {
if (alive(nonce)) {
if (!nonleaf.test(sipnode(sip_keys, nonce, uorv) ^ 1))
alive.reset(nonce);
}
}
}

for (u32 round=0; round < trims; round++) {
for (u32 uorv = 0; uorv < 2; uorv++) {
memset(nonleaf.bits, 0, nodeBytes));

This file has been truncated. [show original](https://github.com/tromp/cuckoo/blob/master/doc/simplesolve)

The complexity is due to the limitations of current-day memory technology, which Cuckoo Cycle aims to help lift.

---



## Yeastplume - Progress update thread - Oct 18 - Feb 19
*Date: 2018-10-05 | [Forum Link](https://forum.grin.mw/t/yeastplume-progress-update-thread-oct-18-feb-19/933)*
*Importance Score: 113.3 | Core Participants: igno.peverell, yeastplume, tromp, lehnberg*

### Post by @Yeastplume ⭐ (2018-10-05)
*Post #1*

October is when the results from the previous funding round kick in, so might as well start a new thread in honour of that fact.

It looks as if T4 is about a week or so away, and most of the work that needs to go in before we can give it a quick pre-deployment test is done. This week was all about getting support for Cuckatoo in place, which meant a lot of updates to grin, grin-miner and cuckoo-miner. More specifically:

* [cuckoo-miner](https://github.com/mimblewimble/cuckoo-miner), which is the library that builds cuck(at)oo plugins for inclusion in other projects, was updated with 2 new cuckatoo miners, courtesy of [@tromp](/u/tromp). There’s a cucakatoo-lean cpu miner, which takes between 25-35 seconds to find a graph on my machine depending on settings, and a likely much-more-useful cuckatoo-gpu miner, which is very comparable to the cuckoo gpu miner at around 4 GPS on a 1080ti. (A mean-cpu miner is forthcoming, which i’d estimate would do a single graph in a few seconds). In addition, the library was updated to allow for variable cuckoo sizes… it should now be possible to mine using whatever size cuckatoo plugin you want (above 29), and have any solutions passed back to Grin along with what size cuck(at)oo graph the solution is for.

*[grin-miner](https://github.com/mimblewimble/grin-miner) was updated to use the new cuckatoo plugins, as well as pass back cuckoo-size data to grin. Also a few enhancements to the TUI while I was there to display the plugin name and graph size for each plugin.

*And finally the [Grin PR that integrates all of the PoW work over the past couple of weeks](https://github.com/mimblewimble/grin/pull/1663) Mostly switching on flags that were already set up, but a few changes there as well to support multiple mining sizes.

Only 2 things left on my list for T4 now are to clean up some automated tests (results of the pow change) as well as integrate the final reviewed [Elements bullet-proof code](https://github.com/ElementsProject/secp256k1-zkp/pull/23) into our secp branch. (Some hard-forking changes went into there recently, and I want to be sure Grin T4 has the latest BP code before it deploys).

Besides that [@antioch](/u/antioch) and [@gary](/u/gary) have been looking at sync issues on T3, and it looks like they’re making good progress there. Once they’re happy with that, then we should be just about ready to merge this and all of the previous wallet, bulletproof, and aggsig work to create a (hopefully short-lived) T4 branch to test changes before we deploy what should hopefully be the final test network (though one can never say never).

That’s it for now, testnet deployments are always exciting times, and hopefully we’ll be mining T4 grins any day now.

---

### Post by @Yeastplume ⭐ (2018-10-13)
*Post #2*

Update Saturday Oct 13th, 2018

We don’t usually have a month going by where someone doesn’t ask this question ‘Why did you implement Grin in Rust instead of C’ in one of our various communication options. Sometimes this is accompanied by a little diatribe in which the poster implies that if only we had implemented Grin in a language that ‘everybody knows like C++’ they would have been able to lend their considerable skills to the project.

Alas, we must forge ahead without these people (I don’t think we’ve heard from any of these people twice). But my answer to anyone who asks either online or in real life is simply ‘When you write code in Rust, it does exactly what you think it’s going to do, every time.’

A lump of C/C++ code of any meaningful size rarely gets itself into a state where it does what’s intended without a considerable amount of time spent in front of a debugger tracing down odd threading issues, investigating segfaults, and dealing with general weirdness. Of course it’s possible to include tools or implement standards to lessen these issues, but it’s time consuming, and every team will implement all of this differently for every project. Then of course different compilers will produce different code and there are approximately 4000 different C++ standards.

Because Grin uses rust, we rarely have to deal with this sort of oddness, which frees up time to focus on the actual issues rather than spending weeks in LLDB. Now there are plenty of article about the merits of Rust on the Internet, and I’m not trying to create another one. This is just for context when I talk about this week’s work.

So Cuckoo-miner, which provides a Rust bridge to slightly-modified versions of [@tromp](/u/tromp)’s cuckoo/cuckatoo miners, is a Rust-C hybrid that I put together well over a year ago when I knew far less about Rust than I do now. The Rust-side is little more than an interface meant to be called by other rust projects, while the C side is an FFI shim to call the C code in the C solvers, however it also contains quite a bit of C code for queue management and to enable the multi threading needed to run multiple devices at once. When I was originally putting this together, I decided to do the queue management on the C side because I reckoned it had to work as fast as possible and doing it in C is the way to do this.

Nowadays, I realize that is entirely the wrong approach to take. When you’re using Rust, any decision to use C should be similar to when you’re primarily using C and are considering doing an algorithm in assembly. You might be able to make it faster, but an optimizing C compiler is generally going to produce far better assembly than you can hand-write, unless it’s something very specific and you really know what you’re doing. Similarly, you should never consider doing something in C when working primarily in Rust for ‘speed issues’ unless there’s some demonstrable need. The cuck(at)oo solvers themselves are good candidates for being written in C as they’re very hardware specific and need to interface into other C frameworks. The queue management portion of cuckoo-miner is not. It should have been kept in Rust as much as possible and the interface into the plugins themselves kept far thinner.

Reason I’m saying this is because over the last two weeks I integrated 3 solvers into cuckoo-miner, (mean CPU, lean CPU and cuda GPU) and each and every time I spent hours tracking down obscure issues that would either have been caught at compile time if those portions of the code had been using Rust, or simply not have been able to happen in the first place. The process of tracking down these issues are extremely frustrating and complicated exercises, usually hours spent hopelessly starting into a debugger with your branch of the code littered with print statements. This kind of session does not happen when working on Grin itself, and I don’t think I’d ever advocate C for a new project unless it’s absolutely required. Rust would simply a better choice in 99% of cases.

So with that little glorified tweet out of the way, here’s what I actually did this week:

* Integrated the Mean CPU miner into Grin-miner, which took a bit longer than expected as explained above. I’d love to re-do parts of cuckoo miner to move the queue management into Rust, but it works now, isn’t mission-critical and can be rewritten at any time. Probably more important things to focus on for the time being.

* Updated libsecp with the [very latest and hopefully final version of element’s bulletproofs](https://github.com/ElementsProject/secp256k1-zkp/pull/23) A few critical (but T3 consensus breaking) fixes in there, so glad to get it in before T4. Also a few upstream changes to how commits are represented meant a bit more headache integrating this than anticipated (seems to have been the theme of the week)

* Creation of the [testnet4 branch](https://github.com/mimblewimble/grin/tree/milestone/testnet4) and integration of all of the wallet, aggsig, bulletproof PRs, etc. I’ll go into far more detail on T4 next week (with an exact list of what’s changed), as there are still a few bits and pieces on it being done, suffice it to say this is where all the focus is now.

* Finally a bit of a breather between large coding efforts to catch up and better understand some recent concepts, particularly [Header MMRs, the newly proposed `prev_root` field and flyclient](https://github.com/mimblewimble/grin/pull/1716), our [dual PoW difficulty adjustments](https://github.com/mimblewimble/grin/pull/1709) and a couple of other things. I can get a bit of myopia sometimes when i’m deep in my own things, so find it helpful to come up for air once in a while and get back up to speed with everything else that’s going on (at the rate things are moving at the moment that could be a full-time job in itself).

That’s it for now, and the next week will most likely be about pre-release T4 testing and addressing whatever bits and pieces come up there. Everything is almost in place, and looking very forward to getting T4 out there.

---

### Post by @Yeastplume ⭐ (2018-10-26)
*Post #4*

Update Friday, October 26th 2018

As indicated last week shortly before the celebratory vodka-night, I had a good time this week bringing [grin-miner](https://github.com/mimblewimble/grin-miner), to a more refined standard. The original version was put together by someone who didn’t have a lot of experience with Rust (i.e. me, about a year and a half ago,) was overly complex and contained far more custom C than necessary. The new version has been pared down and moves all thread control Rust-side, eliminating the potential for 95% of the types of bugs I used to need to track down every time something went wrong in the old version. The new version is a much safer and stable experience, it’s eliminated several odd bugs already and has been very stable running multiple cuda devices on the yeastmonster. So a week spent here should save months down the line.

In detail, the work involved:

* Instead of keeping a custom fork of the solvers, with [@tromp](/u/tromp)’s assistance I made [quite a few changes to the main cuckoo/cuckatoo repository](https://github.com/tromp/cuckoo/pull/56) to enable linkage into other projects while retaining the ability to run them via command line. This means that going forward, there will be no extra layers added to the solvers when they’re run in grin-miner, and they should work exactly as they do from the command line. This means changes/updates to solvers can be instantly picked up in grin-miner, and, so long as future solvers are written to the same interface, they should be easy to integrate.

* Reducing the plugin interface to 4 functions (whereas it had about a dozen before, most of them adding no real value)

* Instead of the 3-repository layout that grew between our custom cuckoo fork, the separate cuckoo-miner library and grin-miner, all code is now in the grin-miner project which just pulls <https://github.com/tromp/cuckoo> as a sub module

* Chopping/simplifying much of the mining control, removing unnecessary function calls and eliminating threading in favour of rust mpsc message queues where it made sense. The main control portion of the cuckoo-miner lib itself is now just a few hundred lines of rust (as opposed to being split between rust and C): <https://github.com/mimblewimble/grin-miner/blob/master/cuckoo-miner/src/miner/miner.rs>

* Simplifying the configuration options in grin-miner.toml. It should be much easier and clearer how to set up plugins for multiple devices now.

* Many QOL bits and pieces in grin-miner, most noticeably more graceful error handling when solvers are misconfigured or throw errors.

Still one or two small things I’d like to do on grin-miner, but they can come over time. The biggest outstanding issue is that the solvers aren’t currently respecting a flag that asks them to stop solving and return immediately, which would be a bit of an issue on slower solvers meaning it still takes them several seconds to switch jobs once notified of a new block. This might lead to some rejected solutions, but those should be cleaned up once [@tromp](/u/tromp) has done a bit of work on getting solvers to exit on request.

So I’m happy with progress this week, and with this new version it’s probably a better time than ever to start test-mining Grin. Will need to go through a few old threads and update them, but for now the build instructions for grin-miner itself combined with the documentation in grin-miner.toml should be enough to get most people going.

Maybe another celebratory vodka-night is in order, who knows? Have a good weekend all!

---

### Post by @Yeastplume ⭐ (2018-11-02)
*Post #7*

Update Friday Nov 2nd, 2018

Bit all over the place this week, as it was shortened due to bank+school holidays (i.e. everyone else gets a holiday while I have to contain Yeastlings,) and also filled with an urgent need to get two coherent and non-embarrassing presentations together in advance of [grincon0](https://grincon.org/).

So on the presentation front, got the wallet one mostly done, and at least have an outline for the general Grin Intro. The latter is far more difficult given that it’s the first fully-human event that’ll happen at Grincon and there’s no real precedent here. I have images in my head of trying to whip up the crowd into a Grin-Euphoric frenzy, but I don’t trust my oration skills enough for that, so will probably go with something a bit more subdued. Whatever I end up coming with, it’s bloody time-consuming. Development work has suffered as a result, but given this is the first grincon and it’ll be live-streamed all over and recorded for posterity, I’ll take the liberty of wearing a marketing hat for a couple of days. This stuff is probably important too. I hope to get most of it out of the way over the weekend so the other speakers can review a bit, then have a clearer mind for deeper tech work next week.

Code wise, I did manage to get some fixes to wallet-restore in that I’d noticed a while ago but never got around to looking at while focused on the miner, and I’m also very aware of a few wallet issues that have popped up (I’ve discovered a few myself,) that I’ll attend to when next I sit down in front of vim/tmux. Also, the next major chunk of work I’m going to attend to will likely be to make a proper thing out of the [grin web wallet](https://github.com/mimblewimble/grin-web-wallet). I resurrected it locally to look at a few issues preventing it from working right this moment, but more importantly we had a few good conversations this week about how we’re going to approach it.

We’re going to spec it out some, get the user stories together until we have a proper brief, and then we’re going to go about getting it designed properly. This is a really, really good time for any designers in the community to get properly involved in turning the web-wallet into as good a user experience as possible, so if you’ve been thinking about adding your talents in that way, please do step forward. We have a plan to handle the design work if nobody does come forward, but we’re holding out hope for having the design community-driven.

If you have strong opinions about how the web wallet should work, the issue for user stories is here:

[github.com/mimblewimble/grin-web-wallet](https://github.com/mimblewimble/grin-web-wallet/issues/9) [ ](https://github.com/lehnberg)

#### [Issue: Define user stories for mainnet ](https://github.com/mimblewimble/grin-web-wallet/issues/9)

opened by [lehnberg](https://github.com/lehnberg) on [2018-11-01](https://github.com/mimblewimble/grin-web-wallet/issues/9)

Motivation
As we get ready for main net, there's a need to finalise a baseline flow and design for the wallet user...

We had a big talk about it, [@lehnberg](/u/lehnberg) graciously took the action of putting up the issue, and I’ve added nothing to it since. (I’m getting to that as well, just as soon as the grincon prep is under control.)

Right, back to google slides. I’m going to spend the weekend ignoring the family and gesticulating madly while pretending to address a crowd in my head.

---

### Post by @lehnberg ⭐ (2018-11-03)
*Post #12*

[@birdonawire](/u/birdonawire) [@darsmith](/u/darsmith) [@permaetheus](/u/permaetheus) that’s fantastic! We’d love to have your help. As Yeast mentioned below we’re trying to figure out user stories / use cases and we’ll have this drive a brief for a front end experience. Once there’s such a brief I’ll be sure to reach out to you all (pm me your emails if you prefer otherwise we’ll just post to here / GitHub).

In the meanwhile, a good way to help before the brief would be to work with us on the [user stories](https://github.com/mimblewimble/grin-web-wallet/issues/9).

---

### Post by @Yeastplume ⭐ (2018-12-21)
*Post #20*

Update Friday December 21st, 2018

Santa’s on his way, so we’ll all be getting together with our families to roast chestnuts on our new 9-GPU rigs, the kids unable to sleep with excitement for Grin’s mainnet.

I expect I probably won’t be getting around to an update next week (or have enough to report to make one worthwhile,) so I’ll leave the next update until consumer-stimulus season is over and the Year of the Grin rolls around. I might even spend a bit of time with the Yeastlings as well, mostly just to make sure they don’t wreck anything else.

The past week has been about [Floonet](https://forum.grin.mw/t/floonet-release-and-upcoming-mainnet/1493), which (a couple of hiccups aside), launched happily enough. For my own part, it was mostly bug fixes and knocking one or two things off the ‘must-have for mainnet’ list.

But I think I want to write about something slightly different today. After the launch of Floonet, I’m in as close to a sentimental mood as I ever get, meaning the empty space in my rib cage where my heart should be is a degree less cold than it should be.

So I’ve taken off the developer Santa hat for a few moments, cause when that’s on all I can do is focus on the massive list of things that either could be better or still need to be done. Instead, I’m just sitting back a bit and playing with all of the things we’ve all built over the past couple of years.

I recently set up a new rig (this one’s the Yeast Tsunami,) which I’ll be using to add my own paltry hashpower to the fray on mainnet, and today I went to install from scratch. I pulled and installed Grin (while carefully following the build guide, of course,) and it worked. I type `grin` at the command prompt, and up comes a fairly-informative TUI telling you what’s going on with your node and the chain. Sync kicks in (not enough blocks yet for fast sync), and I’m up to date and synced and in consensus with 18 other nodes. Stats on all of my peers and what’s going on mining-wise is all available right there if I need it. Although it’s early days for floonet, nobody’s reporting being out of sync, and the difficulty adjustment that has to account for AR and AT POWs appears to be behaving well

In another tmux pane, I type `grin wallet init -h` to create a new wallet. It gives me a BIP-39 recovery phrase which it tells me to write down (which of course I do, diligently,). I create a new account for mining, and start the wallet listening on that account.

So, let’s try mining. I take down the server, then turn on the stratum server in grin-server.toml and restart the server, which is configured by default to mine into the listening wallet on the default port. Because of the embedded stratum-server approach in Grin, now I can mine into my node and listening wallet from however many rigs I care to set up.

So then grin-miner… I check it out, change a config file to have it build the CUDA libs, and build. Grin-miner builds with all available plugins, and I have a range of CPU and GPU options to mine with right out of the box. I configure it to concurrently run cuckaroo29 on 2 2080s currently in the rig, and start grin-miner. Both cards hum into action and start mining away into my listening stratum server, confirmed by another TUI with useful stats about each mining device. Back on the server side, the ‘mining’ tab shows me the connected worker, and gives me more useful stats about how many shares each connected worker is contributing, and how many blocks have been found.

I find a few blocks and funds go into the wallet, which I can check with `grin wallet info`. Once they’ve matured, I should be able to exchange them with other users via files, http, or even directly via keybase.

Of course, Grin is larger than its github projects. Invariably, I’d want to check the status of the chain on a block explorer… I can go to [Grinscan](https://grinscan.net/) or [Grinmint’s explorer](https://grinmint.com/explorer/).
Speaking of Grinmint, I decided to point a yeastmonster at [Grinmint](http://grinmint) for a bit, everything works, and it looks excellent… very well designed and as easy to use as it possibly can be. I also try [Grinpool](https://www.grinpool.co/), which gives me a similarly successful mining experience.

And that’s just a small sampling of community projects. On the wallet side we have a few upcoming projects,such as [Grinbox](https://github.com/vault713/grinbox), as well as quite a few mobile wallets being built. Open CL miners are being worked on (which I hope will be integrated into Grin-miner) and I’m sure there are many other bits of infrastructure that have yet to be announced. If I’ve missed anyone I apologies, but think it’s safe to say that a completely open-source coin with this kind of quality community infrastructure in place is a rarity to behold.

Now, of course there are still things to do, the code isn’t perfect, and your particular machine might not be able to compile the Cuda plugins without some painful support issues. But we’ve come a long way since Voldy did his bitcoin-wizards drive-by thing and Igno decided to push a bit rust code to github (WTF is this rust thing?).

When I look at these things in front of me, I feel proud. And I mean for real, not like you’re at some corporate launch party with a few project managers pretending to give a shit. Everyone involved in Grin’s development should spend a few minutes sitting there bonding with this daftly-named Floonet, and feel some genuine pride, because there’s genuinely something here to be proud of. And that’s not something you get to feel much of in this life.

So, many congratulations to the entire Grin community. Take some time this holiday season to relish this moment, cause silly season is coming on Jan 15th, The Year of the Grin.

A very Yeasty holiday season from me and all Yeast-beings in this house. And don’t let Granny drink too much.

---

### Post by @igno.peverell ⭐ (2018-12-21)
*Post #23*

I’m proud of where we are and what we’ve accomplished as well. And thank you for all your work and contributions to Grin. Wishing all the best things to you and your family. Cheers!

---

### Post by @Yeastplume ⭐ (2019-01-11)
*Post #26*

Update Friday, Jan 11th 2019

A bit sick of writing things at the moment, so this is going to be a fairly short one. Here’s the reason why I’m sick of writing things:

* <https://github.com/mimblewimble/docs/wiki/How-to-run-a-Grin-node>

* <https://github.com/mimblewimble/docs/wiki/How-to-use-the-Grin-wallet>

* <https://github.com/mimblewimble/docs/wiki/How-to-mine-Grin>

* <https://github.com/mimblewimble/docs/wiki/Wallet-User-Guide>

Basically a lot of work getting the wiki filled with some Grin noob guides and a large pass over the wallet user documentation, which I’ve moved out of the source and into the wiki page (where it will be far more useful). Also a bit of work getting the [site](https://grin.mw/) into a state where it’s better leading newcomers to the information they need. I’m trying to get all eyes towards the [Getting Started wiki page](https://github.com/mimblewimble/docs/wiki/Getting-Started-With-Grin%3A-Links-and-Resource), which should contain all the relevant links people need to get up and running with Grin

Some dev work too, mostly quality-of-life things with one major fix:

* [Add the ability to init a wallet from a recovery phrase](https://github.com/mimblewimble/grin/pull/2330) added after a few users correctly pointed out the previous process was needlessly cumbersome and you should be able to recover a wallet in a single step. (though it’s two steps at the moment, `grin wallet init -r` followed by `grin wallet restore` which I believe should stay distinct steps, reasons why some other time)

* [Only update wallet outputs from the node if they’re involved in an outstanding transaction](https://github.com/mimblewimble/grin/pull/2322), this should give a large perf. improvement to the wallet under most conditions, as it was previously validating each and every Unspent output in the wallet each and every time to see if it had become spent. Makes sense that a wallet shouldn’t have to check outputs it hasn’t inserted into a transaction.

* [Automate wallet seed recovery process](https://github.com/mimblewimble/grin/pull/2319) automagically backs up/moves your existing wallet seed file if you’re trying to recover a seed into existing wallet data. Should be useful for those who forget their seed passwords

* [libSecp bug fix](https://github.com/mimblewimble/grin/pull/2304) Important fix, and very glad this was caught in floonet, as it would have made some outputs under certain conditions hard to recover and cause problems with wallet `check` and `restore`.

Oh and renamed `check_repair` to `check`, since `check_repair` sounds like the wallet broke, which is not the case. I very much think the `check` process should become part of usual wallet operations instead of having to run it manually, just the scanning process is potentially too cumbersome to perform all the time at present (I think we need an incremental scan approach).

And thanks again to everyone who attended the [Grin London Meetup](https://www.meetup.com/grinlondon/events/257028620/)! Was great seeing everyone and I hope to be coming out to a few more of these things once the mainnet launch dust settles down.

Speaking of that, Mainnet is launching in 4 days. Enjoy the weekend.

---



## Governance Agendas & Meeting notes
*Date: 2018-10-12 | [Forum Link](https://forum.grin.mw/t/governance-agendas-meeting-notes/970)*
*Importance Score: 111.2 | Core Participants: tromp, lehnberg*

### Post by @lehnberg ⭐ (2018-10-12)
*Post #1*

Links to future meeting agendas and past meeting notes will be posted in this thread as and when they are available.

---

### Post by @lehnberg ⭐ (2018-10-12)
*Post #2*

### [Meeting notes, October 09](https://github.com/mimblewimble/grin-pm/blob/master/notes/20181009-meeting-governance.md)

### [Agenda, October 23](https://github.com/mimblewimble/grin-pm/issues/1)

---

### Post by @lehnberg ⭐ (2018-10-24)
*Post #5*

### [Meeting notes, October 23 ](https://github.com/mimblewimble/grin-pm/blob/master/notes/20181023-meeting-governance.md)

### [Agenda, Nov 6 ](https://github.com/mimblewimble/grin-pm/issues/5)

---

### Post by @lehnberg ⭐ (2018-11-13)
*Post #6*

### [Meeting notes, Nov 6 ](https://github.com/mimblewimble/grin-pm/blob/master/notes/20181106-meeting-governance.md)

### [Agenda, Nov 20 ](https://github.com/mimblewimble/grin-pm/issues/17)

---

### Post by @lehnberg ⭐ (2018-11-21)
*Post #7*

### [Meeting notes, Nov 20](https://github.com/mimblewimble/grin-pm/blob/master/notes/20181120-meeting-governance.md)

### [Agenda, Dec 04 ](https://github.com/mimblewimble/grin-pm/issues/22)

---

### Post by @lehnberg ⭐ (2018-12-09)
*Post #9*

### [Meeting notes, Dec 04 ](https://github.com/mimblewimble/grin-pm/blob/master/notes/20181204-meeting-governance.md)

### [Agenda, Dec 18 ](https://github.com/mimblewimble/grin-pm/issues/26)

---

### Post by @lehnberg ⭐ (2018-12-23)
*Post #12*

### [Meeting notes, Dec 18 ](https://github.com/mimblewimble/grin-pm/blob/master/notes/20181218-meeting-governance.md)

### [Agenda, Jan 03 ](https://github.com/mimblewimble/grin-pm/issues/31)

NOTE: DIFFERENT DATE THAN USUAL

---

### Post by @lehnberg ⭐ (2019-01-01)
*Post #17*

It seems I’m not expressing myself clearly:

* A message that is encoded into the genesis block, will **never** change, unless the entire chain is re-organised. That message essentially exists there, unchanged, for as long as the chain exists.

* A mission statement, _may_ change and evolve over time. Ideally, you’d have a mission statement that remains consistent for as long as it makes sense, of course. But who knows for how long Grin will exist? And how can can we possibly claim to know today what will be Grin’s mission for the rest of its existence?

Given the above, it doesn’t seem wise to me to encode a mission statement or a tagline into the genesis block.

---



## Choice of ASIC Resistant PoW for GPU miners
*Date: 2018-10-22 | [Forum Link](https://forum.grin.mw/t/choice-of-asic-resistant-pow-for-gpu-miners/1017)*
*Importance Score: 111.5 | Core Participants: igno.peverell, tromp, antioch*

### Post by @tromp ⭐ (2018-10-22)
*Post #1*

As most of you know by now, Grin will feature two separate PoW in its first 2 years.

The “primary” one is Cuckatoo32+, a variant of Cuckoo Cycle designed to simplify ASIC design, as explained in <https://forum.grin.mw/t/cuckoo-cycle-weakness-and-possible-fix-cuckatoo-cycle>

This will start out getting only 10% of the reward at launch, linearly climbing up to 100% after 2 years. At that time there will hopefully be ASIC designs from multiple manufacturers engaged in a healthy competition. This PoW is ASIC Friendly (AF) in the sense of allowing huge efficiency improvements over a GPU by using hundreds of MB of SRAM, while remaining bottlenecked by memory IO.

Complementing this AF PoW will be an AR (ASIC Resistant) one, to be called Cuckaroo, aimed at GPU miners. That one will start out getting 90% of rewards at launch, dropping linearly over the course of 2 years down to nothing. ASIC resistance will mainly come from scheduled hard-forks every 6 months (Monero style), and to a lesser degree from also being bottlenecked by memory IO.

The mean solver for Cuckoo on 2^29 edges is quite suitable for GPUs, based on the sorting of multiple GBs of data (somewhat similar to Equihash 144,5). But allowing lean solving is a big risk as this size is small enough to be mined by a single-chip ASIC, which would avoid the memory IO bottleneck and enjoy a huge efficiency advantage. Previously we explored ways of penalizing lean mining in <https://forum.grin.mw/t/aes-based-hash-function-for-graph-generation-in-cuckoo-pow>

Thanks to a suggestion by Igno, we since found a much better approach to prevent lean mining. We still verify a 42-cycle on the Cuckoo graph, but we compute edge endpoints differently. Let HASH be a keyed hash function that transforms a suitably large state. We assume that the key commits to a header/nonce combination. Let K be some 2 power.

Then, to compute the endpoints of edges m*K+n, 0 <= n < K, we compute

State_0 = m
State_{i+1} = HASH(State_i) for i=0...K-1
EdgeState_n = State_{n+1} XOR ( n+1 == K ? 0 : State_K )
Edge_n = extract 2 endpoints from EdgeState_n

The idea is that a long sequential computation is required to compute the endpoints of a whole block of edges. The mean solver would do this only once and store all results, one 64-bit int per edge. Thereafter, remaining trimming rounds and cycle-finding would be exactly as in plain Cuckoo, but recovery of edge indices of any 42-cycle found would again use the blocked edge generation. Altogether this requires limited changes to our already reasonably optimized mean CUDA miner.

Meanwhile, the lean solver would be forced to repeat these computations for every phase of every trimming round, and thus end up with a large latency and energy penalty, leaving it inferior to mean mining.

Possible settings are for example K = 64, HASH = siphash24,
requiring a total of 64 * (2+4) = 384 siphash rounds per block.

Another option is HASH = 4-round-AES-128, which is a little slower for GPUs, but much faster for common CPUs. Compared to siphash24, this reduces the state size from 256 to 128 bits, which could weaken security.

So that’s our plans for the AR PoW, with some details yet to be decided.

Please let us know what you think…

---

### Post by @tromp ⭐ (2018-10-24)
*Post #8*

timolson:

> SRAM available to a single chip

We know from existing Equihash miners they have at least 144 MB available, in a 10nm process. So 256 MB looks within the realm of possibilities for 7nm.

timolson:

> A startup that can’t enter the Grin ASIC market because of the economics

So are you considering entering the SHA256 ASIC market?
Or the BEAM ASIC market, for which you can be the first ASIC on the scene?

---

### Post by @igno.peverell ⭐ (2018-10-24)
*Post #15*

_Sigh_. When we’re not releasing the AR PoW fast enough, you complain because you don’t have enough time to write an optimized GPU solver. When we start talking about it, you complain nothing is ASIC-friendly enough, the share is too small, and now you want to build an ASIC. And then you complain that while Cuckoo is good for you because you think you can optimize it better, no one else can be trusted.

Obviously you don’t care about grin, you only care about what _you_ can get out of it. All I read in your posts is bikeshedding, resentment and posturing. So why should we give you any further attention?

---

### Post by @tromp ⭐ (2018-10-24)
*Post #18*

timolson:

> For some reason I was thinking it required 512MB

You can make do with 1/2^k as much SRAM by doing 2^k times more passes over all edges. See the PART_BITS setting in the lean miner.

timolson:

> One bit for liveness + one bit for a counter

So that becomes 1 liveness bit + 2^-k node adjacency counter bits.

timolson:

> Lean miner takes wayyyy more power per hash than mean miner

Are you saying that 2^30 random 1-bit accesses to 64 MB of SRAM takes way more power than 2^31 mostly sequential 32-bit accesses to 7 GB of DRAM?

---

### Post by @tromp ⭐ (2018-10-25)
*Post #22*

timolson:

> If by 64MB you’re referring to the TMTO

No, 64 MB of SRAM is the full 2^29 bits node bitmap for cuckatoo29, i.e. PART_BITS = 0.

timolson:

> If I understand correctly, you are only considering the first pass, not the full trimming:

I consider the first round of trimming. A single trimming round has 2^PART_BITS passes. Line 155 of <https://github.com/tromp/cuckoo/blob/master/src/cuckatoo/lean.cu> loops over rounds, and line 156 over passes.

timolson:

> lean requires 20N siphashes

No, it wouldn’t, since number of remaining edges decreases geometrically. On average, an edge is hashed in less than 4 trimming rounds. And is hashed twice in a round, once in count_node_deg, and once in kill_leaf_edges. A siphash computation should cost much less energy than an SRAM lookup.

---

### Post by @tromp ⭐ (2018-10-25)
*Post #25*

timolson:

> Didn’t we start the conversation talking about a 7GB mean table?

We were talking about SRAM vs DRAM, but I used cuckatoo29 for my numbers because mean can still use 32 bit edges in the first round. For bigger sizes like cuckatoo32 it will need a less “round” number like 40 bits. I now see that causes unnecessary confusion. Sorry about that.
Btw, the mean CUDA miner for cuckatoo29 uses about 7GB, while the CPU miner gets away with 2.2GB, using lots of space saving tricks that would slow the GPU way down.

timolson:

> Are you saying that Cuckatoo-29 will be allowed on mainnet?

No, but the AR resistant Cuckaroo29 will be the secondary PoW.

timolson:

> assumed C-32

Yes, Cuckatoo32+ is the mainnet primary PoW. And its incompressible edge bitmap of at least 512 MB will not fit on chip, so any ASIC will require off-chip DRAM. SRAM can be either off-chip, or on-chip, but the latter only with tmto.

---

### Post by @igno.peverell ⭐ (2018-10-25)
*Post #26*

timolson:

> Please don’t be upset just because what I have to say about ASICs contradicts what you thought to be true

My previous reply was mostly caused by the tone, not really the content.

timolson:

> I’m offering insight from a position of knowledge and experience in the ASIC miner market.

And I appreciate that, your input _is_ valuable, especially so when you keep it on the constructive side of discourse.

---

### Post by @tromp ⭐ (2018-11-22)
*Post #37*

MoneroCrusher:

> I don’t see a big problem with FPGAs by the way, if they can implement it with 1GB they can also do it with 7GB

Existing FPGAs have limits on amount of memory supported. There will generally be many more FPGAs able to support 1 GB than ones able to support 8 GB.
ASICs, on second thought, should not be a problem as long as the DRAM required doesn’t fit on chip, which is certainly the case at >= 1GB.

There is another potentially large benefit to requiring more than 6GB. Many huge mining farms are dominated by <= 6GB GPUs. Excluding them makes it easier for hobby miners to compete.

MoneroCrusher:

> I believe getting as many people as possible into the project is the best way forward for Grin.

Lowering memory requirements allows more people to mine with their current equipment, but most won’t be able to do so profitably.

That said, we could in principle support a range of acceptable cuckaroo sizes rather than the single 2^29 size, if deemed beneficial to adoption.

---



## Help me design and add content to our site!
*Date: 2018-10-26 | [Forum Link](https://forum.grin.mw/t/help-me-design-and-add-content-to-our-site/1035)*
*Importance Score: 89.2 | Core Participants: igno.peverell, hashmap, lehnberg*

### Post by @igno.peverell ⭐ (2018-10-26)
*Post #1*

We need to start improving our current grin.mw site so it’s not outright scary. I’ve tried to do a first pass, with some graphics and some minor writing, but it’s definitely not my forte (I would personally say I suck at it):

<https://ignopeverell.github.io/site-test>

I do think we should try an incremental approach and build on this to get something more respectable instead of trying to boil the ocean. So to this end:

* Submit PRs to <https://github.com/ignopeverell/site-test>. It’s all based on Github pages and Jekyll using the [so-simple theme](https://github.com/mmistakes/so-simple-theme).
* Anyone can submit graphical, layout and writing improvements, as well as add content. I’ll merge everything that’s clearly better, and otherwise invite discussion.
* Nothing that’s in there right now is particularly good, so everything and anything can be improved upon.

Once we have enough improvements, the result should be published on [grin.mw](https://grin.mw). Unless the whole approach fails miserably. But I’m counting on you to not let that happen.

---

### Post by @igno.peverell ⭐ (2018-10-26)
*Post #4*

monkyyy:

> Hmmmm? Do you want to look like a shitcoin? I find fancy shit is inversely correlated with quality

I get the trauma created by ICOs and dubious projects’ websites, really I do. But step back a little. Grin’s mission is to enable good private money for everyone and open access to it as much as possible. That includes normal people, who don’t live and breath the trepidations of cryptocurrency. And no, not all normal people are hot heads clueless home traders.

Now I don’t think we can realistically reach “normal people” right now or in the next year, but there are quite a few early adopters that I hope we can convince to check Grin out. And it seems fairly reasonable for them to expect a welcoming website, with a mix of text and graphics that directs them appropriately and gently transitions to more detailed information if they’re interested.

None of that says shitcoin ICO to me.

---

### Post by @igno.peverell ⭐ (2018-10-28)
*Post #10*

[@grin.ninja](/u/grin.ninja) I quite like it! This is much nicer and keeps much more of the grin personality than I was able to.

---

### Post by @lehnberg ⭐ (2018-10-28)
*Post #11*

[@grin.ninja](/u/grin.ninja) wow great job!! I’ve been toying around at taking at stab at this myself at some point, but seeing as though you seem to clearly know what you’re doing (and I don’t), I’ll just give some general feedback here (which is my own and subjective). Do with it as you please.

# What I really like

* Its’ responsive and flexible!
* I love the iconography and how the icons are a play of the logo! Super nice!!
* Feels lightweight and simple, doesn’t have ICO-scam vibe.
* Call to actions on donation etc.
* Nice little status update at the bottom

# How I think it might be improved

* Going in a “less is more” / brutalist style to make it more in line with the hacker ethos. Lots of negative, white space.
* So less designed, maybe a black text on white background, let the logo (and iconography be what pops out) and the rest ultra minimal.
* One single font, fixed width like courier or Monaco.
* I don’t think the animated background is working and might just end up being distracting.
* Two grin logos at on the landing page is probably one logo too many. Perhaps “big round wobbly” logo could minimise into the smaller logo on the left as you scroll down? And then it could act as the navigation back to “home”?
* I would avoid the hamburger menu (three bars tap to drop down) in the mobile/tablet versions of the site, they are unintuitive and over designed. Something like a flat simple menu could just be easier.

# Questions

* How does Bulma work with Jekyll? Is it compatible? If not, is it still static-site generated?
* How easy will this be to maintain for the community?

* * *

In addition, here’s how far I got on what could be a site hierarchy that makes sense:

* HOME (GRIN LOGO)
* ABOUT
* mission
* team / council
* project history
* DOWNLOAD
* FUNDING
* Funding model etc
* Addresses
* Current and previous campaigns
* Friends of Grin
* RESOURCES
* Documentation links
* Github etc
* COMMUNITY
* Forum
* Gitter
* Community projects
* Socials

What do you think?

---

### Post by @igno.peverell ⭐ (2018-10-28)
*Post #18*

[@grin.ninja](/u/grin.ninja) as should be obvious at this point, my design literacy is just about as good as my Klingon (hint: I never watched Star Trek). But I’ll still venture a couple opinions.

1. You’ll likely find more brutalists in this community. But we should shy away from monocultures and it’s getting time to open up a little more, so my advice would be to hit a bit in the middle. I enjoy minimal+delight as well.
2. Please please please no fixed width even though [@lehnberg](/u/lehnberg) says so (sorry Daniel from Grin). I’ve spent my whole life staring at code, I don’t want to see some code-mimicking piece of text anymore. The atrophied sense of aesthetics in me still gets offended.

---

### Post by @igno.peverell ⭐ (2018-10-29)
*Post #28*

Note that the copy on the site wasn’t really thought through, I just added something that made sense and seemed to have to right length. We discuss the message and copy in parallel as that’s easy to update once we have it. Discovering the right message is likely to take a little bit…

---

### Post by @igno.peverell ⭐ (2018-10-31)
*Post #32*

Awesome, thanks! I think “Learn” and “What’s MimbleWimble” should also be their own pages with content a little more basic than the intro to start with.

---

### Post by @igno.peverell ⭐ (2018-11-20)
*Post #46*

How can we make walls of text less daunting? The funding page looks really hard for me to look at (and perhaps the typeface has something to do with it…).

---



## Benedikt Bünz's UTXO commitments / RSA Accumulators
*Date: 2018-10-27 | [Forum Link](https://forum.grin.mw/t/benedikt-bunzs-utxo-commitments-rsa-accumulators/1045)*
*Importance Score: 90.8 | Core Participants: david, igno.peverell, antioch, tromp, lehnberg*

### Post by @lehnberg ⭐ (2018-10-27)
*Post #1*

This was a talk from Scaling Bitcoin “Kaizen” a few weeks back.
Title “A Scalable Drop in Replacement for Merkle Trees” by Benedikt Bünz, Benjamin Fisch and Dan Boneh.

[Slides](https://tokyo2018.scalingbitcoin.org/files/Day1/scalable-drop-in-replacement-for-merkle-trees.pdf) | [Transcript](http://diyhpl.us/wiki/transcripts/scalingbitcoin/tokyo-2018/accumulators/) | [Video](https://youtu.be/IMzLa9B1_3E?t=3513)

The talk touches upon various methods of efficiently handling the UTXO set, specifically RSA accumulators as a superior alternative to Merkle paths. In the talk, using aggregate inclusion, Bünz is talking about reducing 160GB of UTXOs down to 1.5 kilobytes…

Thoughts? Something we should be paying attention to?

---

### Post by @igno.peverell ⭐ (2018-10-27)
*Post #2*

We should definitely pay attention. Keep in mind that at this point we only have a video to form an opinion on the described results, so take everything I’m writing with a grain of salt. But this could be very exciting.

First, assuming we can make the technique work, at a minimum this would allow us to replace our whole MMRs for one single piece of data of 1.5KB. This would simplify a lot of code, remove the need for somewhat complex storage and save a lot of space. But this is the boring part.

The less boring part is that we can break linkability between inputs and outputs. On lighter nodes, we could also get completely rid of the UTXO set as they wouldn’t be needed to validate transactions anymore (only for initial sync to validate supply). The idea can be broken down this way:

* Already now, we could replace the input commitment references to an output by a Merkle proof that the output exists, which would be built from our MMR. This would be a bad idea however as one can still link the output using the MMR and those proofs would be large, bloating transactions.
* RSA accumulators would allow us to do the same thing, but replacing the MMR with the accumulator and using its own much more compact version of a proof. This way an input can be validated without even having the output.
* Those accumulators are Zero-Knowledge, so no one knows _which_ output is being spent. You just know that the output has been added in the accumulator sometime and hasn’t been spent yet. This makes inputs and outputs unlinkable.
* Having the output itself with its range proof and commitment becomes unnecessary as long as you trust the output addition was valid, which you can either have checked yourself in the past (full node) or trust others to have done (light node). One could also imagine an hybrid mode where you get sync’d almost instantly like a light node (including FlyClient), and then do fuller validation in the background.

I have some worries about some attacks like replay or handling of duplicates and without the paper it’s not worth thinking about it too hard yet. But the good news are that we’d actually have fairly simple needs.

In summary, it’s very grinnesque: simpler and removes a bunch of data while improving privacy. We just need some more time to get the paper and analyze what the solution would look like.

---

### Post by @igno.peverell ⭐ (2018-10-27)
*Post #5*

[@0xb100d](/u/0xb100d) I already sent him a quick email, hopefully he can share. He has several papers in the pipeline I think (including FlyClient).

---

### Post by @lehnberg ⭐ (2018-12-11)
*Post #11*

My cliffnotes and what I managed to make sense out of the paper, please correct me where I understood things wrong.

## General

1. New type of universal accumulator is proposed, supporting batch adds and deletes, and also proof of membership and non-membership, which also can be aggregated into a single proof of constant size.
2. No trusted setup (in contrast to previous RSA accumulators) required, and no trapdoor is required.

## How the proposed blockchain would work

1. Each block contains a (constant sized) snapshot of the entire blockchain state, ie the UTXO set.
2. Everytime there is a new block mined, miners would batch-delete UTXOs being spent as inputs in txs, and batch-add coinbase + new UTXOs being created as outputs in txs.
3. Verification that this was done correctly can be done by other miners efficiently.
4. End users would only need to store the proof of inclusion for _their own_ UTXOs.
5. Nobody in the entire network would be required to store the entire state and history.

## My questions

1. What are the security assumptions, and how do they compare to Grin’s current assumption that the Discrete Logarithm Problem is hard?

2. The final paragraph of page 30 reads:

> Unfortunately, the design requires that user[s] update their witnesses for every addition or deletion to the set.

What is meant by this? That every user need to update the proof of inclusion they hold for each of their UTXOs after every new block is published on the chain? Or only when the user’s own UTXO set is updated?

3. What would be the role of the `bridge nodes` referred to in the subsequent sentences. How would they work in practice?

4. Is there anything in the approach that would break Grin as it works today?

5. What is missing from what is outlined in order to produce a working prototype?

---

### Post by @igno.peverell ⭐ (2018-12-12)
*Post #12*

Note: this is all based on a first read, I may have missed or misunderstood parts or all of it. First a minor correction:

> Verification that this was done correctly can be done by other miners efficiently.

Despite what the paper says, I think all full nodes would still need to validate to not compromise the trust model. So not only miners. Also, as far as we’re concerned there are at least 3 distinct benefits to accumulators:

1. More compact representations than full MMR trees.
2. Stronger privacy guarantees as inputs and outputs are unlinked.
3. The stateless chain model described in the paper, where a node can get rid of all UTXOs.

The paper goes straight for 3 as I guess they think it’s the stronger result, but we could have 1 and 2 without requiring 3 in most cases, as it does come with additional usability restrictions (which you mention). Don’t get me wrong, 3 is very interesting (and fun), but I don’t think we should consider that a “full node” still.

Regarding your questions:

1. It requires the [strong RSA assumption](https://en.wikipedia.org/wiki/Strong_RSA_assumption), which is over 20 years old now. While it’s a stronger assumption than the standard RSA assumption, there are no proofs or results I’m aware of showing that it’s any easier. It also requires the “adaptive root assumption” which is a little more slippery. It does seem that it’s closely related to the standard RSA assumption but to quote [Wes18]: " It is not known if this problem can easily be reduced to a standard assumption such as the difficulty of factoring N or the RSA problem". But keep in mind that most of these RSA-related are at least 20 years old. And while not being a security assumption, hashing to primes, which is used throughout the paper, doesn’t seem that it would be trivial to implement securely.
2. As I noted at the beginning of this message, this only applies to a stateless chain model. I’m not convinced that should be the chosen model for full nodes but could be very interesting for lighter nodes.
3. They would be able to produce the full proof that you’re able to spend a given output. In the stateless chain model, you wouldn’t be able to do that by yourself (although I’m not sure yet a hybrid model wouldn’t be possible).
4. Depends a lot on what you mean by break and how we’d implement this
5. From a paper-writing standpoint not much, from what I can tell the authors have done a really good job at covering a lot of ground. But the implementation would be a lot of work. Perhaps some crypto toolkits out there could be reused, but a lot of this is novel.

---

### Post by @lehnberg ⭐ (2018-12-12)
*Post #13*

Thanks Igno, this helps my understanding a lot.

On the distinct benefits you outline:

>   1. More compact representations than full MMR trees.
>

How would you describe this effort? Replacing the use of Merkle Mountain Range trees with universal accumulators basically? What are the implications? How much more compact would this be, and what other areas of Grin would be affected?

>   2. Stronger privacy guarantees as inputs and outputs are unlinked.
>

Scrolling up in this thread and reading [@antioch](/u/antioch)’s [previous post](https://forum.grin.mw/t/benedikt-bunzs-utxo-commitments-rsa-accumulators/1045/8), if I understand correctly, this would mean that we would go **from** today’s “full blockchain state” where every synced node tracks “a bunch of inputs that spend to a bunch of outputs + transaction kernels”, **to** every synced node keeping a snapshot of the current state of the UTXO set, which would be a single aggregated inclusion proof. Is that right?

Would we only need an inclusion proof of outputs? Or do we need input inclusion proofs as well? What about transaction kernels?

And what are the key differences between this and the stateless blockchain? That we would still require every node to fully sync and keep track of the entire UTXO set in comparison to every user only tracking their own outputs? Would the size of the blockchain be fairly constant here as well?

### Some more questions

1. I suppose the strong RSA assumption + Adaptive root assumption would still be required in the above approaches for MMR replacement and improving privacy? Or is that not the case? What about hashing to primes that you mention?

2. Going back to my previous question 2 + 3, this basically mean that you would be reliant on third party “validator nodes” to confirm that you are allowed to spend? It seems to me that this would introduce challenges in terms of censorship resistance and collusion prevention. Is that right?

3. > Depends a lot on what you mean by break and how we’d implement this

How do you see we best could explore the concepts above in prototypes, using Grin as a baseline?

---

### Post by @igno.peverell ⭐ (2018-12-15)
*Post #15*

> How would you describe this effort?

The bulk of the effort would be in the RSA accumulator implementation. On the grin side it wouldn’t that much and fairly localized. We could likely get rid of _a lot_ of code, making it a great @antiochp PR candidate. Our MMR roots would just get replaced with hashes of the RSA accumulator(s).

> Is that right?

In short, no  First we don’t track inputs right now. And in terms of tracking UTXOs and kernels data, it would be about the same. Except in the stateless chain model where we wouldn’t have any UTXO at all, but kernels would still have to be around. Until we figure out how to aggregate them, that is.

The “stronger privacy” comes from the fact that the RSA accumulator and associated proofs are zero-knowledge:

1. Your proof that says you can spend an output is only valid if the output is actually unspent. Once it’s spent, no valid proofs can be made anymore.
2. Said proof does not say _which_ output you’re spending. It just says your spend checks against the accumulator. So there’s no linking anymore, and the anonymity set of an input is the whole UTXO set.

As a finer point, one could think it’s a problem because we can’t validate coinbase maturity anymore. I think we’d just keep 2 accumulators for that: a regular output one and a coinbae one.

Regarding your additional questions:

1. All required.
2. That’s right. Which is why I think the stateless chain model belongs more in what we’d call light nodes or SPV-like nodes right now. Note however that the proofs are trustless, they can’t be faked. So the only weakness is liveness (which is still an issue for censorship resistance).
3. First, make a PoC RSA accumulator implementation. That shouldn’t be too expensive, perhaps a few months (but don’t quote me yet on that). Making it solid and fast is what would take more time. Once there’s a semi-functional accumulator, we could add it as an alternative to MMRs, and test it over a new testnet. Once all of this matures and assuming we’re happy with the result and don’t find deal-breakers on the way, add to Floonet and then mainnet.

I might try to do a ELI15 RSA accumulator post, the main idea is actually not that hard. Would that help?

---

### Post by @lehnberg ⭐ (2019-04-27)
*Post #26*

_Awesome discussion re accumulators in /dev the other night:_

* * *

Michalis Kargakis [@kargakis](/u/kargakis) 00:04

> with TXOs we just need to delete 32 bytes from the file next time we rewrite it

so you still track UTXOs in the MMR but with a tree that is pruned when an output is spent. it’s just that we cannot use that MMR to prove unspentness, does that sound right?
wondering now how this is going to look like with accumulators

goldenMetteyya @goldenMetteyya 00:20
MMR is append only so if you change something as said before the whole tree must be rehashed, if you build a MMR after each block for UTXO’s then you can prove unspentness for that block only next one its invalid

David Burkett @DavidBurkett 00:20
There’s a bitset that tells whether the output is unspent based on the MMR position

goldenMetteyya @goldenMetteyya 00:21
is this bitset updated after each block ?

David Burkett @DavidBurkett 00:21
As far as accumulators go, I spent the last couple weeks working with them, and right now, there’s a roadblock that could make them a non-starter.
@goldenMetteyya Yes

goldenMetteyya @goldenMetteyya 00:22
dynamic accumulators have fast verification but they have issues that each change results in all proofs to need to change
So your UTXO inclusion proof is valid for one block

David Burkett @DavidBurkett 00:22
That’s correct, and I was thinking we could get around that, but due to the way we prune, I don’t think we can without help from “Archive nodes"

goldenMetteyya @goldenMetteyya 00:24
with the latest accumulator research someone still needs to hold ALL the chain data

David Burkett @DavidBurkett 00:24
UTXO inclusion proofs can be updated by the miner really easily/efficiently. But the problem is restoring transactions makes it impossible to provide proofs

goldenMetteyya @goldenMetteyya 00:24
to generate the proos
@DavidBurkett depemds on the accumilator construction
if you are using RSA or Class group based then its not super fast
NlogN

David Burkett @DavidBurkett 00:25
Class group is still super fast, thanks to improvements realized by the Chia VDF competition
Not as fast as RSA, I agree, but still fast enough

goldenMetteyya @goldenMetteyya 00:27
depends on your chains block interval
its relative

Michalis Kargakis [@kargakis](/u/kargakis) 00:27

> if a malicious actor rewrites enough history then its possible nobody (if we prune obsolete UTXOs) has ever seen those outputs

does this mean that nobody gets to validate a malicious output for a year (assuming we obsolete utxos in a year)?

David Burkett @DavidBurkett 00:27
@goldenMetteyya With 1 minute blocks, it’s still fast enough. Just did some testing this morning.

goldenMetteyya @goldenMetteyya 00:28
Nice:)
but like 15 seconds its not that good

David Burkett @DavidBurkett 00:28
Possibly not

goldenMetteyya @goldenMetteyya 00:28
even then for 1 minute block time
you have a small window
where the miner who generated the block and then proofs get generated

David Burkett @DavidBurkett 00:29
If you’re looking at the cambrian implementation, just note that the code in master is really slow compared to the code in the class group improvement PR

goldenMetteyya @goldenMetteyya 00:29
by the time a wallet sees and tries to use it
@DavidBurkett can you share the link please

David Burkett @DavidBurkett 00:30
[cambrian/accumulator#35](https://github.com/cambrian/accumulator/pull/35)

goldenMetteyya @goldenMetteyya 00:37

[GitHub](https://github.com/stichtingorganism/classygroup)

### [GitHub - stichtingorganism/classygroup: Class Groups in Rust](https://github.com/stichtingorganism/classygroup)

Class Groups in Rust. Contribute to stichtingorganism/classygroup development by creating an account on GitHub.

this is a library i have used its based on chia entrant
I extracted into its own crate

[GitHub](https://github.com/dignifiedquire/rust-accumulators)

### [GitHub - dignifiedquire/rust-accumulators: Accumulators and Vector Commitments](https://github.com/dignifiedquire/rust-accumulators)

Accumulators and Vector Commitments. Contribute to dignifiedquire/rust-accumulators development by creating an account on GitHub.

this one is only RSA based for now
i have rough code that tested classgroups
i think that the vector commitments are more useful now as they have constant proofs to multiple openings
based on the accumulators

David Burkett @DavidBurkett 00:41
Nice, I’ll check it out

goldenMetteyya @goldenMetteyya 00:42
Recent propsal is Utreexo which is based on hashes, again the issue is proof updates in all of them, the windoe of use is not much
but stateless blockchain idea is cool, but i think MW is the closest that get to one on principles for a light chain

David Burkett @DavidBurkett 00:44
I was just going to ask if you knew anything about Uteexo. I was going to investigate it next. Sounds like it has the same problem though, so you saved me some time

goldenMetteyya @goldenMetteyya 00:46
its based on hashes which is the best assumption out of all them
it has logn proofs
like merkle trees
Its basically a variant, but the accumulators have constant proofs which is wat better
compared to the MMR you can delete items without having to rehash everything

David Burkett @DavidBurkett 00:48
Is the paper out yet? Or anything concrete?

goldenMetteyya @goldenMetteyya 00:49
no paper

[GitHub](https://github.com/mit-dci/utreexo)

### [GitHub - mit-dci/utreexo: accumulator for bitcoin utxo set](https://github.com/mit-dci/utreexo)

accumulator for bitcoin utxo set. Contribute to mit-dci/utreexo development by creating an account on GitHub.

[ ](https://www.youtube.com/watch?v=edRun-6ubCc)

David Burkett @DavidBurkett 00:49
O cool. Thanks

goldenMetteyya @goldenMetteyya 01:05
Essential one needs a dynamic set, that can proove inclusion ideally with constant size no matter the set size, and this proof of inclucion should remain valid even though elements are added and removed. There is no construction that gives this to us
UTXO case has the benefit that additions and deletion are done through autherizaion and there cant be duplicate items

---



## Help us write Grin's Mission statement!
*Date: 2018-11-01 | [Forum Link](https://forum.grin.mw/t/help-us-write-grins-mission-statement/1114)*
*Importance Score: 82.9 | Core Participants: tromp, lehnberg*

### Post by @lehnberg ⭐ (2018-11-01)
*Post #1*

# 1\. Introduction

What is Grin? What is it trying to achieve, and why is it even important? Why should anyone care? In order to better guide our work, are we able to come together as a community and agree on a set of common denominators that sets our direction and what defines us?

Ideally, we’d end up with something like the following:

* **Our mission:** a one sentence statement packed with power about _what_ it is we’re doing.
* **Our vision:** a couple of paragraphs about _why_ this matters, an ideal and aspirational end state we are trying to realise through our mission.

In the future, this could then help us determine:

* **Our strategy:** _How_ do we best go about achieving our mission?
* **Our values:** A set of principles we as a community stand behind that guide our work and how we interact with each other.

Some of these topics have been discussed in a [previous thread](https://forum.grin.mw/t/what-i-think-grin-needs-before-the-mainnet/676), and are also being raised as part of the [ongoing website redesign](https://forum.grin.mw/t/help-me-design-and-add-content-to-our-site/1035/26). (Ping [@Unit](/u/unit))

[@igno.peverell](/u/igno.peverell) and I have sparred a couple of times about this and while we have a couple of baseline ideas (below), they feel far from mature and could do with further scrutiny by all of you in the community.

Let’s try to brainstorm something together that we all feel we can stand behind!

* * *

# 2\. Mission draft

One version that has been raised:

> To create open electronic cash for all, without censorship or restrictions.

## Comments:

* ‘Cash’ implies fungibility, which implies Grin’s privacy preserving properties. It also suggests ‘simplicity’ because cash is minimal, simple, and easy to use. And it doesn’t include a lot of bells and whistles, because that would reduce the cash-like properties in the first place. It also goes well in line with our emission schedule.

* ‘Open’ and ‘for all’ points to being inclusive, and also not authoritative. We’re open, it’s not controlled.

* The last part “without censorship or restrictions” feels a bit… weak. Ideally we’d have something more powerful.

* Possible nice to haves:

* Can we hint better at privacy is it important?
* Can we touch upon that we’re minimal and simple?
* Is it a better way to articulate that we’re actively trying to prohibit censorship and authoritarian control of the system?
* Anarchic by design?

* * *

# 3\. Vision draft

_This is less of a draft, and more me just rambling a bit about what I think to some degree could explain why we exist today. So would be good to get some help here firming some of this up, reducing content, making it more impactful, and relevant._

* Physical cash is disappearing. The physical and digital worlds are merging, with the digital taking up an ever increasing amount of humanity’s time and attention. With the ascent of the digital world, transacting in physical cash has naturally given way to electronic means of transacting. Along the way, these electronic means have introduced surveillance, tracking, and gatekeeping abilities that are not present in physical cash. These reduce the authority that we as individuals have over our money and how we choose to spend it, and they undermine our privacy.
* Cash is important. It is certainty. It offers privacy. It’s inclusive, it does not pass judgement on its user, or on how it is being spent. It safeguards freedom and democratic values. We live in an era of ever increasing surveillance, data collecting, and targeting. We believe a payment form with true cash-like abilities is needed in the digital world, as it is needed in the physical.
* Crypto has the potential to deliver electronic cash but has not done that yet. There is still no true peer-to-peer-based electronic cash system. Previous efforts allow for surveillance and tracking, offer little privacy, have unnecessary complexity, work with unclear objectives, or are driven by questionable motives.

As the digital merges with the physical, we believe in a world where there are no barriers to transacting with one another. Where anyone can participate in the economy regardless of their personal background or ethnicity, regardless of their religious or political views. Where mass surveillance and tracking by governments and corporations alike is never enabled by our means of payment. Where the right to privacy remains a fundamental human right.

## Comments

Yes, this feels a bit bombastic and fluffy. But this is kinda what’s expected of visions. “End hunger.” “World peace”. That kind of thing. So we need to look far into the future and kinda think about the world we are trying to create. What’s the end state?

* * *

# 4\. Further Resources

URL | Comment
---|---
[Ted talk: Simon Sinek - Start with why](https://youtu.be/u4ZoJKF_VuA) | Good video to communicate the importance of why the vision needs to be closely tied to the mission, and why you should start with the vision, i.e. _why_ you exist, and not _what_ you’re trying achieve.
[Coinbase mission](https://www.coinbase.com/mission) | Example of a mission statement tied to a vision that’s defined as a set of “What ifs”. Accompanied by a [blog post](https://blog.coinbase.com/the-vision-mission-and-strategy-for-coinbase-944b79a64a7c) announcing it.
[Ubuntu mission](https://www.ubuntu.com/community/mission) | Another example, this time from open source.
_Got more resources and examples? comment and I’ll update!_ |

---

### Post by @lehnberg ⭐ (2018-12-11)
*Post #46*

Coming back to this thread now!

## Decision process

With this discussion having been open for ~6 weeks, and as a follow up from last week’s Governance meeting, I’d like to see if we can boil down proposals into a couple of concrete suggestions. With an emphasis on the **Mission statement**.

These could then be discussed at the [Dec 18 Governance meeting](https://github.com/mimblewimble/grin-pm/issues/26) and see if we could achieve some sort of rough consensus around one. If we don’t manage to conclude in that meeting, we take it back to the drawing board work a bit more on it, and float it at a future meeting. After the 18th, there are another 2-3 governance meetings before mainnet.

In terms of short-listing proposals, let’s see if we can keep discussion in this thread, and I can move proposals over to [this GitHub issue](https://github.com/mimblewimble/grin-pm/issues/27) where we can try to keep things a bit more tidy. Keep the long elaborations in this thread, and let’s do clean proposals in the issue.

* * *

## Personal comments / my own summary

Going in chronological order on what’s been raised.

### Key thing to keep in mind

We’re going to have to agree on the minimal common denominator here. We’re not all going to get exactly what we want from this statement. Rather it’s something most of us can agree is something we should strive towards. So let’s all keep our minds open.

### Important concepts

Call-outs that have been repeated by commenters:

* **Privacy.**

* **Minimalism.** In design, in security assumptions, in transactions left on the blockchain.

* **Scalability.**

* **Fairness.** In its launch. In its mining. In its reward schedule. In its organisation.

* **Neutrality.** Grin can be used for good, can be used for bad. Just like a hammer, or a kitchen knife. Grin is a tool, that comes to life in the hands of the user.

* **Freedom.**

### Sensitive words

Words that have loaded meaning, that we may want to stay away from as part of the statement:

* **“cash”** was used in my original suggestion because it’s easy to understand what cash is for the non-technical. It also implies fungibility and privacy, but not perfectly so, and has its own limitations. But cash is also outdated as others have pointed out. And are we really “only” trying to build an electronic form of cash? Or are we more ambitious than that?

* **“democratic”** implies certain political values and beliefs, which we probably will struggle to agree on.

* **“anarchic”** same as above.

* **“private”** can be easy to misinterpret. I.e. “we’re building private cash”. Is the cash privacy preserving, or is it private as in something made by the private sector?

* **“for all”** will it really be for all? Or is it just another of saying that it’s open for anyone to participate in?

* **”restrictions”** As been pointed out there are restrictions, in particular technical ones.

* **“create”** As others point out, it’s not in and of itself a mission.

### Questions

* Are we more than “just” a currency? Are we beyond transactions?

* Does it matter if we touch on the same things as other projects like bitcoin, Monero, etc?

* * *

## Proposals I would like to highlight

With my comments, and in no order of preference:

> Be the change you want to see in the world.

Wasn’t really a proposal, but should be, as ‘change’ is almost a pun here (!).
_“Grin is the change we want to receive when we’re at the store.”_ haha.

> Grin is net neutrality for money.

Short, concise, and **really** powerful. If only ‘net neutrality’ was a word that more people knew what it meant. Perhaps that doesn’t matter?

> Grin: private, trustless digital currency. Minimal by design, open to all.

Reads nice. Not really a mission perhaps, but more a statement. Maybe it can be rewritten so it becomes one?

> To empower financial self-sovereignty, through a private, simple and open medium of exchange.

**Very nice.** Is there a way to make “financial self-sovereignty” sound less “stiff” and less like it came out of my political science text book at uni? If so, it could become even more powerful I think. How could we simplify?

---

### Post by @lehnberg ⭐ (2018-12-11)
*Post #52*

[@AdamSC1](/u/adamsc1) some thoughts.

> To empower financial self-sovereignty, through a private, simple and open medium of exchange.

1. Is there a difference between self-sovereignty and just sovereignty? Either you are sovereign, or you are not. And doesn’t being sovereign, imply that you are self-sovereign?
2. There are other words that can replace sovereignty beyond autonomous. How about “independence” for example, or “freedom”?
3. I agree with [@midipoet](/u/midipoet), “minimal” or “minimalistic” might be better than simple.
4. Medium of exchange? Or transaction system. Or maybe just transactions?

Alternative take:

> Enable financial sovereignty through minimal and open transactions that protect your privacy.

---

### Post by @lehnberg ⭐ (2018-12-11)
*Post #57*

[@AdamSC1](/u/adamsc1) much better!

* Like “lightweight” as well.
* “Improve” good as well. “Strengthen”, or maybe even “Reclaim”, to hint that we once had this, but lost it as the economy transitioned into digital?
* Understand self-sovereignty, but feels still too difficult for my taste.
* The problem with medium of exchange is that nobody knows what that means. We can’t attach an investopedia link alongside our mission statement.

It needs to be so simple that I can say it to my mum and she gets it!

---

### Post by @lehnberg ⭐ (2018-12-11)
*Post #74*

If you can say something in a simple and easy to understand way, there’s no point in saying it in a complicated way. I thought the whole point was that we were supposed to be simple.

Being simple, to me, is not dumbing things down. That’s making the project more approachable and inclusive.

And while we could focus on talking to ourselves and our existing community, I would rather take the opportunity to draft a mission statement that more people can identify with and rally behind. Even if they don’t fully grasp the nuances of medium of exchange or the meaning of sovereignty.

---

### Post by @lehnberg ⭐ (2018-12-14)
*Post #83*

I didn’t mean for ‘my mother’ to be read literally here, poor use of words on my side.

I ever got caught in an elevator with some random person and they asked me what Grin’s purpose was, I think it would be nice to have a mission statement to fall back on that I can be confident they would understand. They wouldn’t need to believe in it, but it helps if they at least understand it, so that any follow-up questions are about the mission _itself_ , rather than what is meant by a particular phrase.

A complicated mission statement in a way defeats the purpose, it’s supposed to be inclusive. I welcome anyone to refer me to a well written and widely used statement that is not simple and easy to understand.

If instead, we prefer a position that’s more akin to “one does not simply _understand_ what Grin’s mission is about…”, we may as well remove any reference to being inclusive or open in the same go, in my opinion.

---

### Post by @lehnberg ⭐ (2018-12-14)
*Post #85*

So going back to my post here, let’s see if we can get some proposals onto the Github issue?

[@kargakis](/u/kargakis), [@midipoet](/u/midipoet), [@burrrata](/u/burrrata), [@0xb100d](/u/0xb100d) [@AdamSC1](/u/adamsc1) (and all the others in the thread who want), how about you share your single one favourite candidate and I can move it over? And they will then be discussed in Tuesday’s meeting.

---

### Post by @lehnberg ⭐ (2018-12-16)
*Post #103*

midipoet:

> To afford economic, social and political change through a private, open, and trustless monetary medium.

Added.

midipoet:

> > Grin records the private transfer of value in a lightweight and neutral manner.
>
> i actually really like this.

Added; I edited it to make it a mission, i.e. “to record…”

bondjamesbond:

> My take: “Grin helps you protect your economic sovereignty with privacy and fairness, empowering you with a dead simple medium of exchange.”

Added. I edited it to make it a mission, i.e. “to help…”

monkyyy:

> “Grin is an implementation of mimblewimble. Where other coins make compromises for speed, endless expansion or legality; the goal of grin is privacy first, let the consequences follow.”

[@monkyyy](/u/monkyyy) can you help me rewrite this more into a mission, and then I can add it?

Others can we remove some from the list? Can we drill down further into some favourites ahead of Tuesday?

[@AdamSC1](/u/adamsc1) on that note if you give me your top 3 (in total) I can include them.

---



## Confidential Assets
*Date: 2018-11-18 | [Forum Link](https://forum.grin.mw/t/confidential-assets/1217)*
*Importance Score: 76.4 | Core Participants: igno.peverell, tromp, antioch*

### Post by @rodarmor (2018-11-18)
*Post #1*

# Confidential Assets

Here’s my own understanding of confidential assets, as cobbled together from research papers, Blockstream press releases, and random posts. Please correct my mistakes, of which I am sure there are many. Also, big thanks to RJ Rybarczyk, who I’ve been discussing and researching CA with.

Confidential assets allow multiple assets to be traded on the same chain, alongside the chain’s native asset. Confidential assets use Pedersen commitments, which are also used in Mimblewimble, so they’re a natural fit for Grin.

Unlike, for example, ERC20 Tokens, confidential assets are no programmable, and function in exactly the same way as Grin’s native token.

## How do they work?

Confidential assets replace `H` in the output commitment formula `r*G + v*H` with a distinct NUMS point for every asset type. (I’ll use `A` for these, and reserve `H` for the asset tag of Grin’s native token.) So, the output commitment formula becomes `r*G + v*A`, with `A` representing the type of asset that the output represents.

So far so good. These new asset-bearing outputs can still be verified to sum to zero, just like Grin’s current outputs.

However, in order to verify the range proof for each of these outputs, the value of `A` must be known. The simplest way to make this work would be to include `A` in the clear with each output, but this would allow an observer to see which type of asset is in every output.

## Blinded Asset Tags

An asset tag `A` can be replaced by a blinded asset tag `A + s*G`, which hides the type of the asset. We can verify that these modified outputs sum to zero, and that the range proof is valid.

However, we have a problem! An attacker could choose the asset tag `-A + r*G`, which would essentially amount to a _negative_ amount of the token `A`. They could then create an output containing negative tokens, offset with an output containing positive tokens, allowing them to silently inflate the supply of tokens.

## Surjection Proofs

One way to prevent this malicious choice of blinded asset tag is to attach a _surjection proof_ to each output. A surjection proof proves that a given blinded asset tag is one of a set of known-good blinded asset tags. I’ll call this set of known-good blinded asset tags the _asset tag anonymity set_.

The size of each surjection proof scales with the size of the asset tag anonymity set. This is fine in a bitcoin-like chain, since each transaction has a small number of inputs, so the natural way to construct the asset-tag anonymity set is with the asset tags of all the inputs.

## Confidential Assets and Mimblewimble

This is where things get hazy!

In a mimblewimble chain, there is no discrete notion of a transaction, in the sense of a linked set of inputs and outputs. This complicates the choice of tags to include in each surjection proof’s asset-tag anonymity set.

One proposal is to construct surjection proof asset-tag anonymity sets using every asset tag in the system. Unfortunately, this means that the size of every output scales with the total number of assets in the system. This would preclude us from allowing users to issue new asset types willy nilly, likely requiring a soft fork to add new assets

I’m hoping that we can find some way to avoid this. If issuing new assets requires community coordination and a soft fork, then this process is likely to become highly politicized and contentious. Much better to allow users to issue new assets and let the market decide on which are useful or valuable, instead of requiring everyone to agree.

## Edit: Why user-issued assets?

I wanted to elaborate a little bit on the different reasons I think it’s desirable to allow users to issue their own assets, and additionally why it would be desirable to support a large number of assets.

* If Grin can only support a limited number of assets, say less than 10, then the pool of unallocated assets becomes a very precious and very scarce resource, and would require some allocation process. I imagine that there will be a lot of different ideas for potential assets, and it would fall to the devs and to the community to decide which are most worthwhile. This is definitely just speculation on my part, but I think this process would inevitably be contentious, and would divert time and energy from core protocol development. Governance is one of the most difficult things to do well, and all other things being equal, the less things that need to be governed the better!

* Also, if each new asset increases the size of all outputs, then people who don’t want to use that asset, and don’t think that it will add value to the system might reasonably object. I sort of pessimistically suspect that it will be very hard to build consensus on new assets.

* I can definitely see the argument that only a few assets will be useful, perhaps a Bitcoin peg, an Ethereum peg, and maybe a few others. I think people will certainly come up with some legitimately terrible ideas for assets, but I think they’ll also come up with a lot of neat ones, and I’m definitely curious to see what they are!

* Although it wouldn’t be a good fit for Grin, the codebase could serve a basis for systems which would require a large number of assets, I’m thinking in particular of a stock exchange or liquidity pool.

* I think that user-issuable assets make for an incredibly unique marketing point for Grin. I imagine that we’ll see a ton of attention and interest, and it would probably boost the value of the native token, since it would be the obvious currency of choice for trading between and buying into the various tokens on the chain.

## Vague and Underspecified Alternative Constructions

None of these are clear winners, but here are some ideas for alternative constructions that would allow for user-issued assets:

* **Public Assets** – Asset tags are included in the clear with each asset. This would be very simple, but with the downside that the asset types in each transaction would be clearly visible. This would be bad for privacy, but might be a good starting point, with the intention to add a blinding mechanism at a later date.

* **Confidential-enough assets** – Each surjection proof could include a small subset of all valid asset tags, perhaps 3 or 4. In such a system an observer might be determine the asset tag in each output by observing the transaction graph and using the process of elimination. We’d need a careful analysis of the privacy properties of such a system, and an algorithm for choosing asset tag anonymity sets that would maximize privacy.

* **Accumulator-based proofs** – Perhaps cryptographic accumulators could help. Each asset tag is added to a cryptographic accumulator on first issuance, and the surjection proof is replaced with a zero-knowledge proof that an output’s asset tag has already been added to the accumulator.

* **NUMS point derivation** – If the NUMS points used as asset tags can be derived in some special way, perhaps that method of derivation can be leveraged to prove that blinded asset tags contain a legitimate tag. Maybe, like, I dunno, bulletproofs, or something?

* **BLS-signatures** – BLS signatures have interesting aggregation properties, and support efficient threshold and ring signatures. Perhaps there’s some clever alternative construction of surjection proofs using BLS signatures.

## References

* [Original research paper](https://blockstream.com/bitcoin17-final41.pdf)
* [Blockstream press release on confidential assets](https://blockstream.com/2017/04/03/blockstream-releases-elements-confidential-assets/)
* [Description of surjection proofs as implemented in the elements project](https://github.com/ElementsProject/secp256k1-zkp/blob/secp256k1-zkp/src/modules/surjection/surjection.md)
* [Proposal by Andrew Poelstra to add confidential assets to Grin](https://lists.launchpad.net/mimblewimble/msg00103.html)
* [Reddit comment by Andrew Poelstra on confidential assets and Grin](https://www.reddit.com/r/Mimblewimble/comments/63co0u/blockstream_releases_confidential_assets/dft2hut/)
* [Post on Confidential Assets in the Chain Protocol by Oleg Andreev](https://web.archive.org/web/20181118054903/https://blog.chain.com/hidden-in-plain-sight-transacting-privately-on-a-blockchain-835ab75c01cb?gi=19795b400f2f)
* [Notes on Confidential Assets in the Chain Protocol](https://github.com/chain/chain/blob/4de676549645551d23a1b1604b21fda97f09559a/docs/protocol/specifications/confidential-assets.md)
* [Programmable Constraint Systems for Bulletproofs](https://medium.com/interstellar/programmable-constraint-systems-for-bulletproofs-365b9feb92f7)
* [Cloak protocol, confidential assets using bulletproofs](https://github.com/interstellar/spacesuit/blob/master/spec.md)

---

### Post by @igno.peverell ⭐ (2018-11-18)
*Post #3*

Caveat: this is just the first thing that comes to mind, I haven’t thought of the problem very much yet and it may be outdated. But Oleg Andreev has done some work around CAs as well and IIRC he was working this out as part of the range proof:

[Chain – 7 Feb 17](https://blog.chain.com/hidden-in-plain-sight-transacting-privately-on-a-blockchain-835ab75c01cb?gi=8392eda44df2 "10:10PM - 07 February 2017")

### [Hidden in Plain Sight: Transacting Privately on a Blockchain](https://blog.chain.com/hidden-in-plain-sight-transacting-privately-on-a-blockchain-835ab75c01cb?gi=8392eda44df2)

Introducing Confidential Assets in the Chain Protocol

Reading time: 16 min read

[github.com](https://github.com/chain/chain/blob/4de676549645551d23a1b1604b21fda97f09559a/docs/protocol/specifications/confidential-assets.md)

#### [chain/chain/blob/4de676549645551d23a1b1604b21fda97f09559a/docs/protocol/specifications/confidential-assets.md](https://github.com/chain/chain/blob/4de676549645551d23a1b1604b21fda97f09559a/docs/protocol/specifications/confidential-assets.md)

# Confidential Assets

* [Introduction](#introduction)
* [Usage](#usage)
* [Confidential issuance](#confidential-issuance)
* [Simple transfer](#simple-transfer)
* [Multi-party transaction](#multi-party-transaction)
* [Definitions](#definitions)
* [Elliptic Curve Parameters](#elliptic-curve-parameters)
* [Ring Signature](#ring-signature)
* [Borromean Ring Signature](#borromean-ring-signature)
* [Asset ID Commitment](#asset-id-commitment)
* [Encrypted Asset ID](#encrypted-asset-id)
* [Asset ID Descriptor](#asset-id-descriptor)
* [Asset Range Proof](#asset-range-proof)
* [Value Commitment](#value-commitment)
* [Encrypted Value](#encrypted-value)
* [Value Descriptor](#value-descriptor)
* [Excess Factor](#excess-factor)
* [Excess Commitment](#excess-commitment)

This file has been truncated. [show original](https://github.com/chain/chain/blob/4de676549645551d23a1b1604b21fda97f09559a/docs/protocol/specifications/confidential-assets.md)

Now I believe this was borromean-style range proofs back then, more research would be required to see if the same scheme would be applicable to bulletproofs.

P.S. Maybe download these, not sure how long it’ll stay online…

---

### Post by @igno.peverell ⭐ (2018-11-18)
*Post #5*

Good catch, the 2nd link was supposed to be those notes. Fixed, although discourse renders it as some ugly markdown.

---

### Post by @igno.peverell ⭐ (2018-11-19)
*Post #6*

Regarding my last question about applicability to bulletproofs, this seems to say it’s definitely possible using their constraint system. Sounds quite efficient as well.

[Medium – 19 Nov 18](https://medium.com/interstellar/programmable-constraint-systems-for-bulletproofs-365b9feb92f7 "09:13PM - 19 November 2018")

### [Programmable Constraint Systems for Bulletproofs – Interstellar – Medium](https://medium.com/interstellar/programmable-constraint-systems-for-bulletproofs-365b9feb92f7)

We are excited to share our progress on extending our Bulletproofs implementation with a constraint system API which enables…

Reading time: 7 min read

---

### Post by @kargakis (2018-12-01)
*Post #8*

rodarmor:

> I can definitely see the argument that only a few assets will be useful, perhaps a Bitcoin peg, an Ethereum peg, and maybe a few others

Genuine question: can you elaborate on why a Bitcoin or Ethereum peg would be useful?

---

### Post by @rodarmor (2018-12-01)
*Post #9*

kargakis:

> Genuine question: can you elaborate on why a Bitcoin or Ethereum peg would be useful?

Since Bitcoin and Ethereum don’t have much in the way of privacy, users might like to peg-in to Grin to transact, but might not want to buy and hold Grin.

---

### Post by @tromp ⭐ (2018-12-01)
*Post #12*

That implementation is specific to Ed25519, a different curve than our secp256k1.

---

### Post by @antioch ⭐ (2019-03-15)
*Post #21*

If we want to allow users to issue new assets such that the set of asset tags is unknown ahead of time, do we gain anything if we commit to the current set of assets in each block header? This set would grow over time as new assets were issued.

We could for example maintain asset tags themselves in an MMR and commit to the root of this MMR in each header.

Does this help in any way in terms of having a “global” set of asset tags that all nodes can and will agree on, even if they are not known ahead of time?

This way we could potentially leverage some “bulletproof type constraint thing” to verify the asset tag of a given output is an element in the set of known asset tags at that height.

* asset `Grin` is issued every block as coinbase reward (supply is known)
* asset `Grin'` issued at block height 2 (fixed issuance of 1.0 `Grin'` issued)
* at block height 1 we commit to the set of asset tags `[Grin]`
* at block height height 2 we commit to the set of asset tags `[Grin, Grin']`
* we can verify that `Grin` sums to 0 and that `Grin'` sums to 0 accounting for known supply of both (the sums of both will sum to 0)
* we can verify both asset tags `Grin` and `Grin'` are elements in the set of asset tags `[Grin, Grin']` committed to in the header at height 2
* any output with `Grin'` asset tag would _not_ be valid at height 1 as the asset tag is not valid at that height

---



## Questioning Core Assumptions on Our Emissions Model
*Date: 2018-12-13 | [Forum Link](https://forum.grin.mw/t/questioning-core-assumptions-on-our-emissions-model/1414)*
*Importance Score: 77.1 | Core Participants: tromp, lehnberg*

### Post by @AdamSC1 (2018-12-13)
*Post #1*

There are a few things that I think are important to address:

**A) Interest Rate Balancing:**

While I appreciate the philosophical nature of 1 G/s forever, and while in the first few decades it looks like a feasible model we actually run into two problems with a non-adjusted rate:

1. The rate of new Grin produced will eventually be so minuscule that it will be insignificant against our market capitalization and therefore not worth mining ruining the reward mechanism of securing a network.

2. In any monetary system, you need “reprints”. For paper money that is replacing bills that are old, damaged, torn or lost. For crypto that is replacing coins that leave the system through corrupt harddrives, lost keys, sent to wrong wallets etc. The goal would be to eventually have your inflation rate in perfect balance with this loss/reprint rate. While it is impossible to know the exact number, we can know that it is some estimated percent of currently existing circulation. If we have 1 G/s, then eventually you run into the issue where because of the sheer size of circulation, the loss rate is far larger than the interest rate and so the free float supply ends up going down. Eventually this makes the currency more valuable as an investment/store of value than a monetary unit.

**B) Spendability:**

One economic argument that I’ve not seen covered in this debate is in the spendability of a coin.

Far to often when we discuss emission rates, we look at the distribution equity and participation motivators for what gets a user included to adopt mining or acquiring a coin. This is in part why so many cryptocurrencies are viewed as get rich quick schemes, they are optimized towards the adoption of the individual.

Spendability is a balance between the incentives of merchants to accept the coin as payments, and users to use it as their payment method.

Why do people not use Bitcoin to buy things? Beyond being a bulky payment method and complicated interface, why would I buy a coffee for 0.0000X BTC today if I thought that same amout of BTC could buy me two coffees tomorrow?

To that same end, why would a merchant accept 0.0000X BTC if they thought there was a chance that tomorrow that BTC could be worth only half of a coffee.

So there actually become a series of criteria:

1. We want adopters to get onboard because the early rewards are lucrative enough.

2. We want the price of a Grin to not deflate too much, otherwise it becomes useless to accept it as payment because it declines too rapidly and is too high risk.

3. We want the price or value of Grin to not inflate too much, otherwise it becomes too strong of an investment and it doesn’t make sense to spend it today if it will be worth more tomorrow.

4. We don’t want the early rewards of adopting or mining Grin to be too lucrative, otherwise it seems unfair to later players.

For example, consider right now that in the first year of Grin there will be 100% inflation in the supply (and therefore 50% deflation in the value relative), it doesn’t make sense to collect Grin because of the value rate it will drop at and it certainly doesn’t make sense for merchants to accept Grin, because Grin is losing value at around 0.27397% per day.

We know that, anything about a 5% interest rate in value is interesting to large scale institutional investors for long-term hold, and is better than idle money interest.

At the same time in these markets it is not enough to create wild speculation.

That same 5% on the deflation side would be harder, but still probably manageable spread out across a year in terms of risk stability as now we are talking about 0.0137% value loss per day, which is an order of a magnitude and a half smaller than the previous rates. This is still on the high end for a business to consider accepting as they will need to be diligent in their sales back to fiat cash, and the higher the inflation rate the higher the volatility as well.

However, we currently won’t hit that rate until around 18-20 years out <https://i.imgur.com/Tkt1xr1.png>

This is far too long for us to develop the ecosystem. Quite simply, in the first 5 years of its existence, Grin will lose too much value to be worth merchants accepting.

**C) Positioning:**

As I mentioned I think the philosophical idea of a 1 G/s to always be fair is admirable, but I don’t think it is feasible given the points raised in A) and B).

Whatever the rate is, it should however be something that is line line with the mantra of Grin.

Those are core criteria that I think are important and not fully vetted in our current model.

I’d love to hear from others:

* Do you think these are important core criteria?
* Do you think our current model addresses them?
* Do you think there are other core criteria I’ve overlooked that we should consider?
* Do you have any alternative emissions models that may meet these criteria?

TL;DR: The 1 G/s creates some economic challenges that make it unlikely a good choice for businesses or people to accept Grin as a payment since it will so rapidly decline in value. This means, it is hard for people to spend and use Grin. It’s going to be almost 20 years before its at an acceptable deflation rate and that seems too far out to be feasible.

---

### Post by @AdamSC1 (2018-12-13)
*Post #2*

Adding this in as a second post to seperate it from the above questions.

One model I’ve been playing around with but is in its very early infancy is as follows:

**The Oscillating Variant Model:**

Within a variant model, the emission rate of grin would not only go down over time (like with Bitcoin) but would have reset periods where it spikes back up.

For example, within the first month Grin could be produced at 5 G/s, a high-rate to incentivize miners to join.

Then it would drop down to a low rate of 1 G/s for the next year.

After the first year, that rate could slowly climb over a 3 year period up to a high of 10 G/s. While this is 2x the previous peak output volume, the market should be more robust by then and so it should actually be less Grin per capita.

After reaching that peak and remaining their for a set time, the amount of Grin slowly declines until the annual emission of Grin is 3.33% of the total circulation.

This:

* Rewards early miners for participating in joining Grin and securing the network.
* It ensures that the value of Grin does not rapidly inflate, causing people to simply hold and invest.
* It ensures that the value of Grin does not rapidly deflate due to a rapidly doubling circulation. Thus, making it feasible for merchants to accept Grin in the first few years.
* The variance makes mining more profitable at certain ties, and less stable, so its less likely that ASIC miners would invest in robust operations within the network.
* It allows us to meet the needs of loss replacement.
* The timelines are long enough that people are not likely to mass buy or mass sell their Grin based on the changes.

It still needs a lot of work but it is an interesting concept.

---

### Post by @0xb100d (2018-12-14)
*Post #3*

Most miners sell their coins immediately to cover costs (source needed). So as long as it’s worth more than zero some equilibrium should be met to secure the network.

If network is worth a lot, then the 60 grins mined per minute will be worth a lot (doesn’t matter how small the mining reward is).

Disincentiving hoarding early on supports wide distribution (20 years to get your grins before it becomes a “SoV”).

All of the assumptions about high inflation have to do with national currencies where the inflation rate change is unknown, and so you cannot adequately prepare for fluctuations in the value of your money. With grin you will know exactly how long you should hold your money at a given day. If inflation is high you will exchange it to something else immediately, if it is not so bad you might keep it a week, if it is low you can hold on to it.

This transparency is the real innovation of bitcoin, and should allow equilibrium and price discovery to happen naturally, whatever the inflation rate.

Also, ASICs are good long term.

Also as adoption increases it will become more valuable and useful, with the possibility of actually utility outstripping supply inflation. 50% inflation doesn’t mean 50% price drop.

All hypothetically.

---

### Post by @lehnberg ⭐ (2018-12-14)
*Post #9*

A couple of comments:

>   1. We want adopters to get onboard because the early rewards are lucrative enough.
>

I have not noticed any importance being put on onboarding “adopters” seeking to make “lucrative rewards”. What do you base this on?

> For example, consider right now that in the first year of Grin there will be 100% inflation in the supply (and therefore 50% deflation in the value relative), it doesn’t make sense to collect Grin because of the value rate it will drop at and it certainly doesn’t make sense for merchants to accept Grin, because Grin is losing value at around 0.27397% per day.

Yes, exactly. It doesn’t make sense to collect Grin. It might still make sense for merchants to accept Grin though, depending on the needs they and their customers have. But more generally speaking, merchants should probably not rush to adopt Grin as a preferred method of payment any time soon. Not sure this is a problem.

The plan as it stands is for Grin to do a fair launch, using POW mining, 1 minute blocks, with 1 grin/s in coinbase reward. Do you have a concrete proposal for how this could be improved?

---

### Post by @lehnberg ⭐ (2018-12-14)
*Post #12*

> Those can be mission based, philosophical, financial, or in the pursuit of freedom. There needs to be some positive motivator to attract adopters of all categories, and those positives need to outweigh any friction points.

Right, so what does this have to with the emission model? Seems the point you’re trying to make is that if people find it useful, they will use it.

> From what I’ve read, one of the goals with Grin is to make it a practical currency to be used and spent. We want people to use it as a medium of exchange, correct?

Yes, but over the long term.

>   1. We know many miners sell right away to cover their costs. This puts downward sell pressure on a market.
>

And so the price goes down. Why does this matter?

>   2. Merchants shouldn’t adopt Grin because it doesn’t make financial sense due to the heavy downward on the pressure.
>

Again, you can trade in and out of the coin, you don’t have to hold it. So what has price got to do with it? Merchants shouldn’t adopt Grin (yet) because it’s a work in progress effort that could use a year or so to mature a bit more.

>   3. Grin has no utility purpose (it is not redeemable for something, nor a function tool like ETH).
>

Grin offers a high degree of privacy. This is utility, and serves a function to those who value it. It comes at a high cost of low adoption, friction, and lack of supporting services. For now. Those who are willing to pay this price will use it. This cost will go down over time.

---

### Post by @bondjamesbond (2018-12-15)
*Post #15*

I think the philosophy of “build it and they will come” can be done if it’s sustained of a solid economic model for—at least—some of the network participants. In Bitcoin, it worked with core users as they were incentivized to hodl based on a speculative bet on a limited supply—but what about Grin?

By design, Grin wants you to sell your coins as soon as possible as they become less valuable in the long term. In the short term, we have miners that need to cover their costs, in an industry where currently we can count with one hand GPU-mined coins that are profitable—and no one can point to a reason why would anyone want to buy and use Grin.

Sure, miners will speculatively mine as long as they can afford to do so, but what about if there is no organic demand for Grin in a multiyear long bear market? How strong would the security be, after most miners shut down their equipment because they can’t afford not to? And how would that erode Grin’s long term potential?

I do get the idea of just launching the network and see how it goes but as others, I’m a bit skeptical that the right incentives are set in place for a healthy growth in a diverse set of scenarios.

---

### Post by @Neo (2018-12-17)
*Post #22*

bondjamesbond:

> Agreed. But what happens if the demand doesn’t exceed the supply for years, driving miners out of the network, and reducing the security to risky levels?

The point here is that even if you adjusted the emission model to favor early adopters there’s no proof that it’s ultimately going to help increase the demand or improve the security of the network. There is also an argument that it could actually hurt adoption since newcomers have less incentive to get involved. What if Grin had a typical PoW block reward schedule( eg continuous or periodic reduction) and demand doesn’t exceed supply for years? You’re left with the same premise. There are so many examples of this already.

Grin will most likely be the leader in Cuckaroo & Cuckatoo hash. Being the leading coin of each hash function increases the security of the network and greatly reduces the chance of a malicious attack. There will be all sorts of shit coin forks coming up that use the same hash function- They will be ones most susception to an attack. A good example of this is Monero vs all the other Cryptonote/ Cryptonight shit coins.

bondjamesbond:

> I think a robust economic policy should particularly address worst-case scenarios, setting right incentives for network participants and not rely—excessively—neither on speculation nor creating demand out of thin air, especially when the consequences are security related. A good balance between both is ideal and, when one side is expected to be weak—for a period of time—the other one should be over incentivized to maintain that balance.
>
> I’m not saying that I do know which is the perfect monetary policy to implement, I just think the current monetary policy it’s being over-optimistic in the demand side and too aggressive on the speculation side, not setting the right course for a healthy, robust growth regardless of environment sentiment.

This sounds great in theory, but it’s not practical to implement. If you try to optimize a monetary policy to x conditions then you’re going to introduce all sorts of bias and end up with some kind of curve fitted model that is more susceptible to falling apart in a different market regime. You should leave it up to the free market. You can’t play god.

There is no such thing as a perfect monetary policy.

Consider this:

1. Early miners face a lower network difficulty created from the unknowingness & uncertainty of a new project, so they are naturally incentivized from a lower network hash rate( lower difficulty), which increases their share of the block reward. The net/ net effect of this could be no different from offering early miners a greater block reward.
2. Grin starts off as a 90/10 GPU minable coin that reduces to an ASIC PoW after 2 years. After those 2 years, ASICs should dominate the network, skyrocketing the difficulty. So this creates an additional incentive for early GPU miners to support the Network, knowing that after 2 years there could be an order of magnitude more hash required for the same portion of block reward. I think many have overlooked this nuance.
3. There is no premine/ ICO/ or treasury cut of the block reward, Grin is 100% community funded, no VCs or early investors have been able to get a slice of it when it could easily be the most interesting project of 2019(arguably the most organic launch since Bitcoin). So, there could easily be speculators willing to scoop up whatever they can get their hands on.

---

### Post by @tromp ⭐ (2018-12-22)
*Post #40*

I once estimated the number of high-memory mining GPUs at 1M, and expressed hope that Grin would capture a significant fraction of that.

---



## Floonet release and upcoming mainnet
*Date: 2018-12-21 | [Forum Link](https://forum.grin.mw/t/floonet-release-and-upcoming-mainnet/1493)*
*Importance Score: 78.6 | Core Participants: igno.peverell*

### Post by @igno.peverell ⭐ (2018-12-21)
*Post #1*

Grin’s last and long running testnet, the Floonet, has just been released. Please update your nodes and don’t forget to clean your `~/.grin` from any remaining Testnet4 data. The Floonet will continue being maintained for the foreseeable future, and used to test protocol updates before the hit mainnet.

In addition, as this marks a first important step toward mainnet, I thought I would outline a few important points.

* Grin is set to release on what should be January 15th 2019 in most populated timezones.
* We just released Floonet (our long-running testnet) today. It was also a good and successful practice of our mainnet release process.
* The grin mainnet genesis block will include a recent (as in last hour or two) bitcoin block hash, to prove the absence of pre-mine and a fair launch.
* The grin mainnet genesis block will also set a very high starting difficulty, for similar reasons. Don’t be surprised if the first few blocks take an hour or two. That being said, accurately estimating starting hashrate is nearly impossible so we may have surprises.
* Once created, the genesis block will be immediately pushed to our github repository and a normal Grin build will get you a mainnet node.
* No block will be valid for about 30 min after the genesis is published to leave everyone time to rebuild and restart. This is done by setting the timestamp of the genesis block in the future (grin enforces block time progression).

Our security review and audit(s) will keep happening in parallel and all issues fixed according to severity. We will have a planned hard fork after 6 months to address anything consensus critical (assuming it can wait). On that topic, I’d like to thank everyone who donated, with a special note to Aurel who closed the campaign with a very large donation, reaching the status of Grin Hero (it’s a thing).

After the release, celebration will be in order. The word on the street is that [@hashmap](/u/hashmap) is organizing a celebration party in Berlin on Jan 15th or 16th. There may be a few more parties in other parts of the world (feel free to organize one!), and of course on our Gitter channel where you’ll be able to find yours truly.

Finally, please join us at GrinconUS (<https://grincon.us>) January 28th. It should be extremely interesting and a lot of fun. Proceeds will also go back to the grin project fund, so get those sponsors and investor tickets.

---

### Post by @igno.peverell ⭐ (2019-01-10)
*Post #4*

Short and hopefully sweet update:

* We’re still on schedule for Jan 15th 2019.
* We’ll be starting around 15:00 (3pm) UTC time. The release procedure itself could take an hour or two, depending on how much caffeine I have in my system.

You’re all welcome to follow the fun on the [dev Gitter](https://gitter.im/grin_community/dev) but please don’t post so the development team can do its job. Various expressions of excitement can take place in the [lobby](https://gitter.im/grin_community/Lobby) or IRL if you’re into that sort of thing.

---

### Post by @Geyl (2019-01-11)
*Post #5*

Where can we see the mainnet parameter ? like which pow algorithm, ar_scale, difficulty

---

### Post by @igno.peverell ⭐ (2019-01-11)
*Post #7*

The release itself is pretty much composing the genesis block. This is what it looks like now:

[github.com](https://github.com/mimblewimble/grin/blob/master/core/src/genesis.rs#L168)

#### [mimblewimble/grin/blob/master/core/src/genesis.rs#L168](https://github.com/mimblewimble/grin/blob/master/core/src/genesis.rs#L168)

158. 				230, 217, 97, 105, 50, 208, 126, 180, 113, 81, 152, 238, 123, 157, 232, 19, 164,

159. 				159, 164, 89, 75, 33, 70, 140, 204, 158, 236, 10, 226, 102, 14, 88, 134, 82, 131,

160. 				36, 195, 127, 158, 81, 252, 223, 165, 11, 52, 105, 245, 245, 228, 235, 168, 175,

161. 				52, 175, 76, 157, 120, 208, 99, 135, 210, 81, 114, 230, 181,

162. 			],

163. 		},

164. 	};

165. 	gen.with_reward(output, kernel)

166. }

167.

168. /// Placeholder for mainnet genesis block, will definitely change before

169. /// release so no use trying to pre-mine it.

170. pub fn genesis_main() -> core::Block {

171. 	let gen = core::Block::with_header(core::BlockHeader {

172. 		height: 0,

173. 		timestamp: Utc.ymd(2019, 1, 15).and_hms(12, 0, 0), // REPLACE

174. 		prev_root: Hash::default(),                        // REPLACE

175. 		output_root: Hash::default(),                      // REPLACE

176. 		range_proof_root: Hash::default(),                 // REPLACE

177. 		kernel_root: Hash::default(),                      // REPLACE

178. 		total_kernel_offset: BlindingFactor::zero(),       // REPLACE

All those `// REPLACE` will be set to final values to launch the network.

---

### Post by @florent (2019-01-13)
*Post #9*

Same question as above, what would be the steps needed to mine from floonet to mainnet, will the pool autoswitch and we have nothing to do? do we have to update miners?

You seem keen to have a fair launch but if you don’t clarify those things only the insiders will be able to mine at launch.

Regards.

---

### Post by @kargakis (2019-01-13)
*Post #10*

This question is really a question you should be asking your pool operator.

---

### Post by @kargakis (2019-01-14)
*Post #14*

From Igno’s reply above:

igno.peverell:

> We’ll be starting around 15:00 (3pm) UTC time. The release procedure itself could take an hour or two, depending on how much caffeine I have in my system.

---

### Post by @igno.peverell ⭐ (2019-01-15)
*Post #17*

The Grin genesis block was pushed to Grin’s git repository with commit [8fc489a80868fcf12fcdbc0551528bb73fc891a0](https://github.com/mimblewimble/grin/commit/8fc489a80868fcf12fcdbc0551528bb73fc891a0). You can already build , binary releases forthcoming.

---



## PoW for Mainnet? cuckaroo29 vs cuckatoo31+
*Date: 2018-12-26 | [Forum Link](https://forum.grin.mw/t/pow-for-mainnet-cuckaroo29-vs-cuckatoo31/1557)*
*Importance Score: 68.5 | Core Participants: tromp*

### Post by @jason (2018-12-26)
*Post #1*

I see “Floonet and Mainnet will accept cuckaroo29 and cuckatoo31+”

What is the use case for cuckaroo29 vs cuckatoo31 on Mainnet? E.g. if I have a 1080ti, why would I want to run cuckatoo31+?

If I read other forum topics correctly, 29 is for GPU miners, 31+ is ASIC friendly and should be used by ASICs (and not GPUs)? Is this correct?

Thanks!

---

### Post by @tromp ⭐ (2018-12-27)
*Post #4*

Cuckaroo29 is ASIC resistant and will be tweaked every 6 months to remain the domain of GPUs. It will cease to be in 2 years.

Cuckatoo31+ is the long term PoW that is meant to attract ASICs. Every 2^k years, the smallest remaining graph size wil be phased out over some months. So sometime in 2020, the PoW will have become Cuckatoo32+ which will be out of reach of consumer GPUs.

---

### Post by @csga5000 (2019-01-13)
*Post #6*

As I understand no asics are known they’re anticipated to come later. Nobody knows for sure if they’ll be here within a year or never, or in a month.

---

### Post by @babaji (2019-01-14)
*Post #7*

So all the hashrate on GPS31 are from cards like the Nvidia rtx 2080 ti, and other cards with 11gb of memory?

How long have the details about this Cuckatoo31 algorithm been in the public domain?

---

### Post by @tromp ⭐ (2019-01-14)
*Post #8*

Since about 4 months: <https://forum.grin.mw/t/cuckoo-cycle-weakness-and-possible-fix-cuckatoo-cycle>

---

### Post by @schofieldn (2019-01-14)
*Post #9*

Is that the right link? I get ‘access denied’.

---

### Post by @babaji (2019-01-15)
*Post #11*

do you reckon anyone has built an asic in 4 months?

---

### Post by @timolson (2019-01-16)
*Post #12*

No, I doubt anyone made an ASIC yet, and we don’t see it in the hashrate, either.

The hashrate is roughly 50,000 GPU’s if they’re all 1080’s. Certainly under 100,000 GPU’s mining Grin currently, and if we price them at $200, that’s only $20m worth of hardware currently mining Grin. It will cost you minimum of $5m to even think about making an ASIC.

As it stands, Grin is actually just too small for an ASIC market to develop, even if ASIC’s got 100% of the block rewards.

That analysis can change quickly, of course! We just had Genesis and a bunch of GPU miners suddenly made public. Coin markets change fast in the first few months…

---



## Best GPU for mining Grin
*Date: 2019-01-02 | [Forum Link](https://forum.grin.mw/t/best-gpu-for-mining-grin/1654)*
*Importance Score: 104.3 | Core Participants: tromp*

### Post by @tromp ⭐ (2019-01-02)
*Post #1*

I can now say with some confidence that the best currently available GPU for mining Grin is the NVIDIA RTX 2080 Ti, with one caveat.

The main reason to prefer the 2080 Ti over the 2080 (and 1080) is the 11 GB memory which allows it to efficiently solve the ASIC targeted PoW, cuckAToo31+.

The reason to prefer the 2080 Ti over the 1080 Ti is the much higher efficiency at running cuckatoo31. Even without using its claimed 64 KB shared memory capability, it’s over twice as fast, and I don’t think its power use is close to twice as high.

The caveat I mention is that when ASICs show up, they may have enough efficiency advantage over the 2080 Ti to relegate it over to the GPU focussed, ASIC resistant PoW, cuckARoo29, where it has to compete with many other cards that only need 6 GB.

In the rare event that ASICs don’t show up in the first year, and cuckatoo31 gets phased out, then the RTX Titan 24 GB looks well positioned to solve cuckatoo32+ efficiently. But at $2499 it’s over twice as expensive as a 2080 Ti…

---

### Post by @tromp ⭐ (2019-01-03)
*Post #4*

Neither can mean mine cuckatoo32+ (would need about 22 GB).

---

### Post by @tromp ⭐ (2019-01-03)
*Post #10*

With cuckaroo29, siphashes are only computed once, and the superior computing efficiency of the 2080 is less pronounced there.

---

### Post by @tromp ⭐ (2019-01-03)
*Post #15*

keepwalking1234:

> what’s the GPS for 2080ti when you run cuckatoo31 ?

1.6-1.7

keepwalking1234:

> is it better when you also can buy the 1060 card A LOT with only 20% of price of 2080ti ?

depends on how crowded C31 mining segment will get, but could well be…

---

### Post by @tromp ⭐ (2019-01-04)
*Post #17*

A 1060 doesn’t have the 11 GB required to solve Cuckatoo31. A Tesla V100 doesn’t benefit from its extra memory, and is expected to score in between a 1080Ti and 2080Ti. It will however come into its own next year when Cuckatoo31 gets phased out and it will be one of the few cards with the 22 GB needed for Cuckatoo32.

---

### Post by @tromp ⭐ (2019-01-08)
*Post #26*

timolson:

> compute-bound on GPU

That is not what it looks like on cuckaroo_cuda_29;
a GPU typically spends 37 ms on computing and bucketing siphashes,
and then another 188 ms edge trimming and cycle chasing.
So even ignoring the initial bucketing, siphash computation is only about 16% of runtime.

timolson:

> A fully optimized Cuckoo Cycle miner

Are you suggesting that you optimized the 188 ms down to under 37 ms, for a 3x or more total speedup?

---

### Post by @tromp ⭐ (2019-01-09)
*Post #28*

g011um:

> what are the strongest arguments we have that edge trimming in its current implementation is close to optimal?

The observation that the lean miner only uses 2 bits of memory, 2 bit-writes, and 2 bit-reads, to verify that two connecting edges must be kept around. I cannot imagine using any less resources.

---

### Post by @tromp ⭐ (2019-01-24)
*Post #79*

1.7 sounds about right and it’s know to have fidelity around 0.7, so that has the same solution rate as 1.19 gps with fidelity 1…

---



## VOTE on Grin's Mission statement
*Date: 2019-01-04 | [Forum Link](https://forum.grin.mw/t/vote-on-grins-mission-statement/1724)*
*Importance Score: 74.7 | Core Participants: tromp, lehnberg*

### Post by @lehnberg ⭐ (2019-01-04)
*Post #1*

# NON-BINDING COMMUNITY VOTE

Read the FAQ **before** you vote.

## FAQ

Question | Answer
---|---
What am I voting on? | The [mission statement](https://forum.grin.mw/t/help-us-write-grins-mission-statement/1114) Grin should adopt. This will guide the project’s vision strategy.
Is the vote binding? |  **No, the vote is non-binding.** Whatever proposal wins the poll will not necessarily be the final adopted proposal.
If it’s not binding, what is the purpose? | To gauge community sentiment towards particular proposals, so that more informed decisions can be made.
How will the actual decision be made? | The vote results will guide a discussion as part of the [Jan 17 governance meeting](https://github.com/mimblewimble/grin-pm/issues/37), where a decision will hopefully also be made.
How many votes do I get? | You can cast **up to five (5)** votes on different proposals.
Why more than one vote? | To make it indicative of community sentiment only, and to get a better sense of general direction, rather than a specific proposal, and as mitigation against the [Condorcet paradox](https://en.wikipedia.org/wiki/Condorcet_paradox).
Do I have to use all votes | No. By using fewer votes, each vote gets a larger weight.
When are the results published? | Once the poll has closed.
Why are the results not visible until the poll has closed? | So that previous votes do not influence your vote.
When does the poll close? | Jan 16 @ 23:59:59 [UTC](http://www.timebie.com/std/utc.php).
Is my vote public? | Yes, once the results are published, members of the community will be able to see what proposal(s) you voted for.
Why is it not a secret ballot? | The vote is non-binding in any case and you need to join the governance meeting to argue in favour of your proposal, it makes trolls accountable, and it combats spamming and the use of fake accounts to influence vote outcome.
Where were the proposals sourced from? | From [this issue](https://github.com/mimblewimble/grin-pm/issues/27), which summarises the original forum thread. The list had to be truncated down to 20 proposals as this is the maximum allowed.
How can I vote on a different proposal? | Unfortunately the poll cannot be edited. If you think you have a better suggestion, please comment in the thread below and see who “hearts” it. The vote is non-binding. You can still join the Jan 17 governance meeting and argue for your proposal.
Who decided on all this? | The attendees of the last governance meeting. The details were left to me, [@lehnberg](/u/lehnberg), to work out as best as I could.
I have a different question, what should I do? | Ask it by posting in this thread.

## OTHER INFORMATION

* The [original forum post announcement](https://forum.grin.mw/t/help-us-write-grins-mission-statement/1114) offers an intro & reference about what this is about.
* **The mission statement is not a tagline for the project**.
* It needs to be aspirational and something to work towards, rather than something that describes what Grin is right now. So less `"Grin is..."` and more `"We're building Grin to be the..."`

* * *

## POLL

Grin’s mission is…

* To advance economic freedom, through a privacy-focused, simple, and fair medium of exchange.
* To advance financial sovereignty, through a private, simple, and accessible medium of exchange.
* To be a neutral, more efficient, money technology.
* To be a private, scalable, digital currency.
* To be a private, trustless medium of exchange; minimal in design and inclusive of all.
* To be an open community that makes sharing and exchanging value easy.
* To be https:// for money.
* To be the best digital cash.
* To be the soundest money possible.
* To build a private, scalable and open (community-initiated) currency.
* To create open electronic cash for all, without censorship or restrictions.
* To empower financial autonomy through a private, minimal, open medium of exchange.
* To empower financial self-sovereignty, through a private, simple and open medium of exchange.
* To empower freedom through an open, minimal, and private financial medium of exchange.
* To fight for the freedom of your money, through privacy-focused and light-weight transactions.
* To improve financial self-sovereignty through an open and lightweight medium of exchange, that protects your privacy.
* To make electronic transactions possible for everyone, without censorship or restrictions.
* To provide secure, private value transactions on a global scale.
* To raise the standards of freedom through a lightweight, private, and simple medium of exchange.
* To record the private transfer of value in a lightweight and neutral manner.

0 voters

---

### Post by @tromp ⭐ (2019-01-06)
*Post #8*

I think the mission statement might want to reflect Grin’s strengths compared to other crypto currencies.

Here’s how I compare Grin to several representative other designs:

Coin | Simplicity | Trustlessness | Scalability | Privacy | Fairness
---|---|---|---|---|---
Bitcoin | medium | high | medium | low | medium
Monero | medium | medium | low | medium | medium
Grin | high | medium | medium | medium | high
ZCash | Low | low | low | high | low
CODA | Low | low | high | high | low

The last column is about achieving a fair distribution of coins over time, an essential ingredient for long term viability. Coins with ICO/premine/mining tax score low here, while coins with fixed supply are penalized as well. Grin benefits from having not-far-from-optimal miners from day one combined with a big interest in mining it and of course the never-diminishing reward.

Perhaps the mission statement can reflect the balance of these properties, at none of which it fares poorly.

---

### Post by @tromp ⭐ (2019-01-06)
*Post #10*

kargakis:

> On scalability, why do you think Bitcoin and Grin are on the same level?

Because my levels are pretty coarse:-(
Grin definitely does scale better, but not by an order of magnitude.

kargakis:

> Also, what do you think it takes to achieve high privacy in Grin?

Well, it looks like it can be achieved by sacrificing some simplicity and trustlessness, for instance by implementing RSA accumulators. But we should not rush to make those sacrifices. Perhaps alternative approaches will be found to make tx aggregation much more effective. Approaches that do not require those sacrifices. Note that complexity is much easier to stomach when it stays outside of the consensus core of Grin. The above table is really about complexity in the core consensus layer.

---

### Post by @lehnberg ⭐ (2019-01-17)
*Post #16*

Polls have closed and the results are in! This will be discussed in today’s governance meeting.

---

### Post by @lehnberg ⭐ (2019-01-20)
*Post #22*

[last meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190117-meeting-governance.md#103-mission):

> #### 10.3 Mission
>
> Meeting favoured the following mission statements:
>
>   * A. `To be a private, scalable, digital currency.`
>   * B. `better money ツ`
>

>
> …without concluding on one of the two. General sentiment was that “private” in A needed to be reworked into something else, like “privacy-preserving” or similar.

---

### Post by @monkyyy (2019-01-21)
*Post #26*

“Better” is marketing bullshit.

Use words with meaning.

---

### Post by @tromp ⭐ (2019-01-21)
*Post #34*

kargakis:

> better money

another stab at it:

grin: fairly spread; well spent

---

### Post by @monkyyy (2019-01-22)
*Post #49*

> The people speculating on Grin are funds who see a black swan, and speculators following the hype. The funds will stay with us. The speculators will not

I’m a speculator first and foremost, while a fair bit of the economy is shitcoiners, thats not the full story.

I’m not going anywhere even if I’m moving my money wildly.

> People don’t have the time that I do to consider these things or the mental fortitude to understand. We need to fix that.

Thats done thru ease of use and price. The devs are working on ease of use, maybe a touch slowly, but wallet 713 has public addresses and messaging, presumably thats open source enough it will become a standard and guis and phone wallets will copy it.

As for price, just trust the market to reward good ideas.

> And it looks deranged if you can’t see it. It’s inside the emission model that’s stumping everyone, and it will invite a fork.

Tromps coin emission model was a mistake, but its ultimately a minor issue.

I however have quite a different philosophy from the standard industrialist and the never ending factions that it tends to make <https://twitter.com/fribergcs/status/635871278046445568?lang=en>

> We cannot have the ego-driven engineering culture that plagues tech at Grin.

Ego driven cultures aren’t plagues.

Arrogance is a virtue.

---



## What to mine? Choosing between Cuckatoo31+ and Cuckaroo29
*Date: 2019-01-04 | [Forum Link](https://forum.grin.mw/t/what-to-mine-choosing-between-cuckatoo31-and-cuckaroo29/1732)*
*Importance Score: 81.7 | Core Participants: tromp, jaspervdm*

### Post by @tromp ⭐ (2019-01-04)
*Post #1*

Grin’s dual PoW system present miners with a choice: should they mine the GPU oriented Cuckaroo29, or the ASIC oriented Cuckatoo31+?

First of all, let’s assume you want to mean mine with a GPU. CPUs kind of suck at the whole Cuckoo Cycle family, and lean mining is inherently very inefficient on all types of DRAM.

The two PoWs have rather different memory requirements.
The current cuckaroo_cuda_29 grin-miner plugin requires close to 5.5 GB, while both cuckatoo_mean_gtx_cuda_31 and cuckatoo_mean_rtx_cuda_31 require close to 11 GB.

So if your GPU has under 5.5 GB then your only choice is to wait
for a 3rd party miner that has even lower memory requirements. It appears possible to get under 4 GB by computing all siphashes twice, but I have no plans yet to implement that myself.

If you have at least 5.5 GB but less than 10.5 GB then the choice is simple: use cuckaroo_cuda_29, or C29 for short.

If you have at least or close to 11 GB, then you have a real choice.
First, your choice between cuckatoo_mean_gtx_cuda_31 and cuckatoo_mean_rtx_cuda_31 depends on whether you have a Pascal based GTX card like the 1080 Ti, or a Turing based RTX card like the 2080 Ti. Let’s call that the C31 miner. The + in Cuckatoo31+ signifies that you could also mine C32 or C33 or …, each of which doubles the memory requirement of the previous one. Those miners have yet to be implemented though, so we’ll ignore them for now.

Assuming you want to maximize your chances of an acceptable solution,
the choice between C31 and C29 depends on 3 factors:

1. your graph-rate on C31, denoted GPS31
1a) your fidelity on C31, denoted F31

2. your graph-rate on C29, denoted GPS29
2a) your fidelity on C29, denoted F29

3. the secondary scale, or as I like to call it, ar_scale (for asic resistant)

Fidelity of a miner is the probability of it finding 42-cycles in graphs that have them. Normally that should be over 0.999, so we can consider it equal to 1 for all intents and purposes. But when a (mean) miner is constrained by available memory, it has to spill a small fraction of edges that do not fit into the buckets and this reduces the fidelity. Notably, the cuckatoo_mean_cuda_rtx_31 miner has a reported fidelity of about 0.7

Your solution rate at mining C31 is going to be GPS31 * F31 / 42 solutions per second, since the probability of a random graph having a 42-cycle is 1/42. The probability of a C31 solution being accepted is
weight(31) / difficulty. To be precise, the cyclehash of the solution, viewed as a fraction in [0,1) has to be below weight(31) / difficulty. So your reward rate will be

(GPS31 * F31 / 42) * weight(31) / difficulty.

Similarly, your reward rate for mining C29 will be

(GPS29 * F29 / 42) * ar_scale / difficulty.

This is where the variable header field ar_scale comes in. Higher values make it easier to get C29 solutions accepted, while smaller values make it harder. It starts out at weight(29) in genesis, and is then adjusted every block to try move the balance between C29 and C31 rewards toward the goal balance at that height. E,g, 90%-10% at launch 45%-55% after 1 year, and 0%-100% after 2 years. If the total C29 hashpower is 9x that of the C31 hashpower, then we expect ar_scale to remain close to weight(29). But the C29 hashpower could easily be more than 10x the C31 hashpower, which would cause ar_scale to drop. That makes mining C31 more attractive. Eventually we expect C31 ASICs to show up and tip the balance in hashpower. Once they push ar_scale to values well above weight(29), all GPUs will be better off mining C29. But at least they only compete against other GPUs there. C31 ASICs won’t be able to take away any of the prescribed C29 rewards.

Putting everything together, we see that C31 mining is preferred when

(GPS31 * F31 / 42) * weight(31) > (GPS29 * F29 / 42) * ar_scale,

or in other words, when

ar_scale < weight(31) * (GPS31 * F31) / (GPS29 * F29).

Relevant weight values are weight(31) = 31 * 2^8 = 7936
and weight(29) = 29 * 2^6 = 1856.

The value weight(31) actually starts changing after one year, to force a migration to Cuckatoo32+. Over the course of 31 weeks it will linearly drop from 31 * 2^8 to 0 * 2^8. So remember that as you make the choice next year…

Happy choosing!

Also see the related post <https://forum.grin.mw/t/on-dual-pow-graph-rates-gps-and-difficulty>

---

### Post by @tromp ⭐ (2019-01-05)
*Post #3*

bearbearbowl:

> In practice, how would the ar_scale be determines? Do we look at past block type?

Like I said, ar_scale is adjusted every block to try move the balance between C29 and C31 rewards toward the goal balance.

If the past 60 blocks have more than 6 (initial goal of 10%) of type C31, then ar_scale tends to increase, and if fewer than 6, it will tend to decrease. The actual code is in function secondary_pow_scaling at line 316 of <https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs>

---

### Post by @jaspervdm ⭐ (2019-01-05)
*Post #7*

Yes, both GrinScan and GrinExplorer show the AR scale of the blocks. Just look at the latest block to get an idea what the scale currently is.

---

### Post by @tromp ⭐ (2019-01-06)
*Post #11*

Total difficulty is the sum of difficulties from genesis to current block.
You should instead use the target difficulty of 84,490 …

---

### Post by @tromp ⭐ (2019-01-13)
*Post #24*

Yes, all your conclusions are correct.

---

### Post by @tromp ⭐ (2019-01-13)
*Post #26*

That is correct too.

babaji:

> Or is there something else that needs to be considered

No; the reward splitting is already reflected in the value of AR Scale, which you used to arrive at your reward rate.

---

### Post by @tromp ⭐ (2019-01-13)
*Post #28*

Oops; you’re right. I failed to check your claim that

babaji:

> AR Scale: 1856

Indeed that should be 503.
And yes, the weights for Cuckatoo stay fixed until a graph size gets phased out.
Floonet and mainnet behave the same. You can find the weight function source code at <https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs#L164-L177>

---

### Post by @tromp ⭐ (2019-01-13)
*Post #30*

babaji:

> Can the figure for current weight(31) be looked up anywhere?

It’s in my very first message

tromp:

> weight(31) = 31 * 2^8 = 7936

---



## Grin on Ledger Hardware Wallet
*Date: 2019-01-08 | [Forum Link](https://forum.grin.mw/t/grin-on-ledger-hardware-wallet/1854)*
*Importance Score: 67.2 | Core Participants: davidtavarez, tromp, quentinlesceller*

### Post by @uruguaycrypto (2019-01-08)
*Post #1*

hi all

I’m new to Grin and very fascinated about it. so I just read that Grin has _no_ amounts and _no addresses_.
Please let me ask, does this imply that there will be no haradware wallet support, like Ledger Nano S, to store my Grin coins?

I’m used to keepin my coins safe on hardware wallets these days.

Thanks, keep up the good work

---

### Post by @tromp ⭐ (2019-01-08)
*Post #2*

We don’t see any technical barriers that would stop Ledger from supporting Grin on their hardware wallet. They just need time to study grin wallet behaviour and to port to their wallet.

---

### Post by @ear2ear (2019-07-23)
*Post #3*

Ledger tweeted this today!

[twitter.com](https://twitter.com/Ledger/status/1153605323581788160)

####  [ Ledger (Ledger) ](https://twitter.com/Ledger/status/1153605323581788160)

@iamcrowne Hello Jeff, neither $GRIN nor $BEAM are currently supported on our devices. The #grin and #beam communities are more than welcome to develop/submit their application, which we'd gladly review! You can find the guidelines on this process here: https://t.co/aydOi71HL0

[6:51 PM - 22 Jul 2019](https://twitter.com/Ledger/status/1153605323581788160)

---

### Post by @quentinlesceller ⭐ (2020-06-04)
*Post #7*

Now that Ledger Live is out it seems that the instructions above are outdated? It’s unclear whether there should be a PR on [GitHub - LedgerHQ/ledger-live-desktop: Ledger Live (Desktop)](https://github.com/LedgerHQ/ledger-live-desktop) and backend [GitHub - LedgerHQ/ledger-live-common: Common ground for the Ledger Wallet apps](https://github.com/LedgerHQ/ledger-live-common) additionally. It seems like most of their app are in different repo (e.g. Monero app [GitHub - LedgerHQ/app-monero: Monero wallet application for Ledger Nano S & X](https://github.com/LedgerHQ/app-monero)).

EDIT: And by the way, if anyone is up to the task, feel free to apply for funding

---

### Post by @davidtavarez ⭐ (2020-06-04)
*Post #9*

tempting… if someone could gather the information about how to do it would be nice.

---

### Post by @quentinlesceller ⭐ (2020-06-04)
*Post #10*

I think the first step would be to release the BOLOS app following the instructions here <https://ledger.readthedocs.io/en/latest/additional/publishing_an_app.html>
There are several app on the Github repo <https://github.com/LedgerHQ> which can be interesting too (also Monero app mentioned above).

---

### Post by @davidtavarez ⭐ (2020-06-04)
*Post #11*

Do you think is worth to work on that before the next hardfork? honestly?

These months I will be working on completing the Grin++ API documentation and, also, in a GUI for the mobile version of Grin++, but if someone in the community gently decides to donate a Ledger Nano I could probably take a look on how to do this, although I don’t think is worth to work on this before the next hardfork.

---

### Post by @quentinlesceller ⭐ (2020-06-04)
*Post #12*

Considering that the hard fork is in a month. I think this might be worth a try to start working now on the lower level logic (the BOLOS app) and take into account the Slatepacks RFC. Depends on how fast you are really  might take a while to digest the Ledger architecture.

PS: I PMed you

---



## Grin Miner Dev Donation Option
*Date: 2019-01-10 | [Forum Link](https://forum.grin.mw/t/grin-miner-dev-donation-option/1949)*
*Importance Score: 68.0 | Core Participants: igno.peverell, tromp, antioch*

### Post by @rodarmor (2019-01-10)
*Post #1*

I would very much like to see some amount of Grin’s supply go to the Grin General Fund, in order to fund development over the long term.

Since an ICO or founder’s reward is out of the question, I wanted to propose that an option be added to `grin-miner` that would mine some percentage of the time into a wallet that the core team controls.

I think that Grin will appreciate over the long term, so it may wind up being a substantial amount of money. Especially if people donate a lot (in Grin terms) early on, when the coin is less valuable and less established.

For the actual implementation, I would add a `dev-donation-share` option to the `grin-miner` configuration file that could be set between `0.0` to `1.0`, to mine to a dev wallet between 0% of the time and 100% of the time. Instead of making it opt in and opt out, it might be good to make the miner to refuse to mine unless the setting is manually set, with an explanation in the default configuration file, and a suggestion of, say, `0.05`, or whatever people think would be reasonable.

What do people think?

---

### Post by @tromp ⭐ (2019-01-10)
*Post #4*

We make the cucka(r/t)oo solvers available under the FAIR mining license

[github.com](https://github.com/tromp/cuckoo/blob/master/LICENSE.txt)

#### [tromp/cuckoo/blob/master/LICENSE.txt](https://github.com/tromp/cuckoo/blob/master/LICENSE.txt)

The FAIR MINING License

Copyright (c) 2013-2018 John Tromp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

FAIR MINING
Any derived miner that charges a developer fee for mining a fair coin
---one with no premine or other form of developer compensation---
shall offer to share half the fee revenue with the coin developers.

The above copyright notice, FAIR MINING condition, and this permission notice
shall be included in all copies or substantial portions of the Software.

This file has been truncated. [show original](https://github.com/tromp/cuckoo/blob/master/LICENSE.txt)

---

### Post by @tromp ⭐ (2019-01-10)
*Post #6*

rodarmor:

> the license above only applies to people using third party miners that charge a fee.

Correct. We do expect third party miners to appear before long, within a month or two, and fear that grin-miner may not be able to stay competitive for long.

rodarmor:

> seems like a missed potential source of donations.

Adding configurable donations to grin-miner is a non-trivial undertaking though, considering the need for interaction with the recipient wallet, and grin developer time is a scarce resource. The first step is to provide a Grin alternative to the current BTC/ETH donation addresses.

---

### Post by @tromp ⭐ (2019-01-11)
*Post #8*

rodarmor:

> with `grin-miner` there is no such incentive

I still have all my bounties on [GitHub - tromp/cuckoo: a memory-bound graph-theoretic proof-of-work system](https://github.com/tromp/cuckoo).
They’ve worked great in the past when there was no money to be made of Cuckoo Cycle directly. Now they probably need a big boost to entice programmers to publish their optimizations…

---

### Post by @tromp ⭐ (2019-01-29)
*Post #11*

sebseb7:

> what is a “derived miner” ?

Any miner that is based in substantial part on my reference solvers

sebseb7:

>   * is this license legally enforcable or is it considered “policial incorrect” to not follow that license?
>

The latter.

---

### Post by @antioch ⭐ (2019-01-30)
*Post #13*

“Political correctness” is the wrong way of thinking about this. This can be a very loaded term with implied negative connotations. I would think of this more in terms of an issue of ethics.

You are free to go build a clean-room implementation of a solver. You are also free to voluntarily donate to the dev fund. But if you leverage the existing reference implementation then there _is_ an ethical obligation to adhere to the license.

---

### Post by @igno.peverell ⭐ (2019-02-01)
*Post #19*

Answering for [@tromp](/u/tromp) but yes, at least GGM and bminer have.

---

### Post by @igno.peverell ⭐ (2019-02-01)
*Post #21*

Yeah, we don’t really have one of those yet but I think there’s a lot we need to do in that area, it’s a bit of a mess right now.

---



## Monkyyys market shitposting thread
*Date: 2019-01-14 | [Forum Link](https://forum.grin.mw/t/monkyyys-market-shitposting-thread/2163)*
*Importance Score: 479.2 | Core Participants: tromp, lehnberg*

### Post by @monkyyy (2019-01-14)
*Post #1*

None of the mods commented on my thread about making a thread like this… soooo saying sorry over asking permission

Post your wild unsubstantiated price predictions here; argue like children about a topic that no one knows what they are talking about and geneally make claims about the future with theories held together with spit and ducktape that are half gut feelings and the other half looking for data that supported your theory after you googled for it

Socialists and engineers digression is advised.

---

### Post by @Heffalump (2019-01-21)
*Post #69*

There are new found reasons to be optimistic. The rate of price decline has slowed and it will now take us until 27 January to reach zero.

[ E3603BFB-69BB-4677-92F6-A611F7B6AA37.png1119×579 40 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/5ba66f2c6c792330028ae83c8d342d20aa81c9c5.png "E3603BFB-69BB-4677-92F6-A611F7B6AA37.png")

---

### Post by @lehnberg ⭐ (2019-04-05)
*Post #376*

[@Grumpy](/u/grumpy) <https://forum.grin.mw/g/moderators>

---

### Post by @tromp ⭐ (2019-05-11)
*Post #440*

Chronos:

> equal chance of $0.50 or $8

That is by definition a $4.25 expected value, for a $2.25 expected return.

---

### Post by @tromp ⭐ (2019-05-28)
*Post #484*

timolson:

> The p2p network still sees all your transactions

But the network won’t know they are yours as they all look like uniformly random data, varying only in number of inputs and outputs.
Only some of the people you transacted with could recognize some inputs as yours, but that will be of limited use as better decoy and aggregation methods are developed in future,

---

### Post by @tromp ⭐ (2019-07-17)
*Post #715*

Neo:

> yet it’s ranked 98th based on current market cap

Grin seems appropriately ranked in a long term view at

<https://messari.io/onchainfx/view/B3EAFFCA>

(not replying on twitter as I have no twitter account)

---

### Post by @tromp ⭐ (2019-12-14)
*Post #995*

I’ll go with “I’m really into puzzles” …

---

### Post by @tromp ⭐ (2020-03-20)
*Post #1034*

What you call hopping is multiplying a secret key with the curve generator G to get a public key. This way you can hop from 0*G to 1*G to 2*G …
Except that private keys are big 256-bit numbers that no-one should be able to guess. They’re normally chosen by hashing some master seed with some additional information called a derivation path. The master seed corresponds to the 12 or 24 word list that you need to write down as a wallet backup. The master seed was randomly picked when you initialized your wallet, using entropy that your computer collects, such as disk latencies, mouse movements, etcetera.

---


