# Chapter 5: Growing Pains

*9 topics selected for this chapter*

---

## Yeastplume - Progress update thread - Mar 19 to Sep 19
*Date: 2019-03-01 | [Forum Link](https://forum.grin.mw/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303)*
*Importance Score: 89.4 | Core Participants: yeastplume, quentinlesceller*

### Post by @Yeastplume ⭐ (2019-03-01)
*Post #1*

Update Friday March 1st, 2019

Now working under the results of the last funding round, which I’m celebrating by starting a new thread.

I’ll start off by posting a pic of the latest Windows build running:

[ grin_win2.png1512×898 61.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/ea4d1a3fa210469d88c6ff4c671d81153be1b922.png "grin_win2.png")

Looks extremely similar to the picture I posted a few weeks ago. However, there are many many differences between this picture and that picture which represent most of the past couple of weeks worth of work.

Most importantly, preview windows binaries are now available here:

The server itself (built from a branch on my own repo):

[GitHub](https://github.com/yeastplume/grin/releases/tag/v1.1.0-win-preview-1)

### [yeastplume/grin](https://github.com/yeastplume/grin/releases/tag/v1.1.0-win-preview-1)

Minimal implementation of the MimbleWimble protocol. - yeastplume/grin

And the wallet:

[GitHub](https://github.com/mimblewimble/grin-wallet/releases/tag/v1.1.0-win-preview-2)

### [mimblewimble/grin-wallet](https://github.com/mimblewimble/grin-wallet/releases/tag/v1.1.0-win-preview-2)

Grin Wallet. Contribute to mimblewimble/grin-wallet development by creating an account on GitHub.

Grin Windows (Gwin?) now has most of the major issues worked out, and the resulting binaries are now being produced via travis CI. Getting the builds themselves working was an extraordinarily fiddly process, as were just about all of the other issues that needed to be addressed. There’s a pretty decent log of them in the [meta-issue](https://github.com/mimblewimble/grin/issues/2525), so I’ll leave thumbing through them as an exercise for the dedicated reader.

The largest single change was the [dynamic allocation of LMDB backend storage](https://github.com/mimblewimble/grin/pull/2605). DB management needed a bit of attention anyhow, and the improvements are completely cross-platform. The old code was just allocating a max db size of 500GB, which was okay on unixy systems where it’s just a max size and not the actual size on disk. Windows being windows needs to allocate the whole thing at once. So that’s been changed to resize the max db size in 128mb chunks as needed on all platforms.

I also more or less finished splitting off [grin-wallet](https://github.com/mimblewimble/grin-wallet), got all builds working on linux/macOS and windows, and removed all trace of wallet code from grin’s 1.1.0 branch. Again, a lot of small fiddly things (such as tests having to be moved/rewritten in some cases,) but nothing too remarkable.

So nothing earth shattering here. Lots of painful work resulting in some big wins for Grin. The wallet is split, windows is working and we can provide binaries. By all means give the windows binaries a try, but keep in mind they’re still pre-release and use at your own risk until we say otherwise. This should all become official for the upcoming 1.1.0 release, at which that point official 1.1.0 binaries will be released (also use at your own risk).

Very glad to have these two things mostly boxed off, and hopefully I should be able to get back to some actual enhancements from next week onwards. Enjoy the weekend.

---

### Post by @Yeastplume ⭐ (2019-03-08)
*Post #6*

Update Friday March 9th, 2019

With the windows work and wallet split mostly out of the way and waiting (expectantly for the release of 1.1.0), my focus is back onto improving and extending the wallet core functionality.

In case you’re new to Grin, our strategy with regards to the wallet is not to create the slickest, most polished and user friendly Grin wallet in existence (though we’ll certainly be improving it over time,). It is rather to create the slickest, most polished and developer-friendly Grin wallet toolkit in existence, that will allow community wallet developers to focus on creating the slickest, most polished and user-friendly Grin wallets in existence. `grin-wallet` is intended to be a set of tools and libraries with a reference CLI wallet wrapped around it.

I’ve started to put down all of the tasks and changes that need to happen to start moving the wallet towards ever-increasing developer friendliness in a [meta issue here](https://github.com/mimblewimble/grin-wallet/issues/11) (roadmap, even?). I won’t repeat the contents of that, but if you’re a wallet developer or at all interested in the direction of Grin’s core wallet functionality, I invite you to have a look and comment.

Most of this past week has been about reviewing all of the various changes, proposals and PRs out there and starting to think about them (I’ll be weighing in shortly in all of the appropriate threads and PRS). I’m also encouraging everyone to get everything prepared for the V2 wallet api tasks, as that’s the next big chunk of work I plan to get involved in.

Other major bits and pieces this week:

* [Fixes to LMDB paths on 1.1.0](https://github.com/mimblewimble/grin/pull/2656), turns out they’re a bit all over the place but 1.1.0 should remain consistent with 1.0.2
* [Changes to wallet info display and wallet check](https://github.com/mimblewimble/grin-wallet/pull/8) should allow wallet users to better differentiate between Unconfirmed coins and coins waiting for the other participant to post the transaction. It should also make `wallet check` less destructive by default, meaning it won’t wipe pending transactions. Details in issue

That’s it for now, and I look forward to jumping into V2API work next week!

---

### Post by @Yeastplume ⭐ (2019-03-15)
*Post #9*

Update Friday, March 15th 2019

It’s St. Patricks weekend coming up, so don’t expect much coherence from me over the long weekend. Here’s what went on last week in the continuing saga of grin-wallet.

A couple of major pieces of work are underway. First, I’ve done quite a bit of work on [slate version conversions](https://github.com/mimblewimble/grin-wallet/pull/13) to allow newer clients to communicate with older clients. This works by maintaining each slate version separately, and maintaining code that upgrades and downgrades versions, so if a slate v0 comes in and the wallet is on slate V2, it converts V0->V1->v2, operates on it, then (provided the incoming version is compatible,) converts back V2->V1->V0 to send it back. It’s quite a bit of code to maintain for each version and slightly inefficient, but at least it means that every new slate version just needs a single set of conversions (n-1 -> n, n -> n-1) to ensure backwards compatibility. That’s in place (but needs testing,) which means I can modify the v2 slate with impunity.

Second, I’ve turned my attentions to the V2 API. I have to give a shout out to Andrew Dirksen here, who’s put together an [elegant and as-concise-as-possible system](https://github.com/mimblewimble/grin-wallet/pull/2) for generating the API, which also generates documentation that also acts as integration tests. To support this, he also put together a simplified [json-rpc lib](https://github.com/layer1capital/easy-jsonrpc) that I think is badly needed in the rust world. Now that I’ve had a chance to go over his work in detail, I’m very excited about this and think we’re going to have a very robust, consistent, flexible and self-documenting API v2 that should support all sorts of clients and suit everyone’s needs.

I’ve done [some work towards completing the API](https://github.com/mimblewimble/grin-wallet/pull/20), but in doing this I started to realize that in order to best take advantage of all of the good things Andrew’s approach to generating API v2 will bring, quite a bit of the code needs to be refactored. I’ll go over the exact changes [I’m currently working on](https://github.com/mimblewimble/grin-wallet/pull/23) either in the issue or in a readme that explains the crate layout, but for now I’ll just say the current code that instantiates concrete wallet support structs and calls the api can definitely benefit from a better separation of concerns. Once this work is done, the code should be much cleaner, but also (very importantly) allow v2 api documentation tests that actually exercise the wallet code and act as complete integration tests as well.

So that’s where things are… naturally the code will need quite a bit of testing once this is done before 1.1.0 can be released, but the work is definitely worth it.

That’s it for now. Remember to enjoy Guinness responsibly.

---

### Post by @Yeastplume ⭐ (2019-03-22)
*Post #12*

Update Friday March 22, 2019

Tons of effort over the past week to get these working:

[ Screenshot from 2019-03-22 15-23-25.png1133×801 92.8 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b137a571c5dd75fccac5a664287d02f9aae0c6ed.png "Screenshot from 2019-03-22 15-23-25.png")

[ Screenshot from 2019-03-22 15-28-33.png1119×852 150 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/bf1005fdf74c4665a9e86762c789d8de5a5e3425.png "Screenshot from 2019-03-22 15-28-33.png")

Those are images of the rustdoc documentation I’ve been putting together for the v2 wallet API, and the self-testing documentation for the generated JSON-RPC stubs.

It looks like simple rustdoc documentation, but there’s a lot going on behind the scenes to produce this. That ‘json_rpc_example’ in the image isn’t just documentation, it’s the input to an entire integration test that runs against a sample chain in the wallet’s test framework, with the output carefully compared to the expected results in the documentation. By ensuring documentation and testing are integrated this way, we can pretty much guarantee that both the rust and generated JSON RPC APIs will stay consistent, current and documented going forward. Hugely important, and definitely worth the work.

And what work it is. It goes something like this:

* Sit down to create the json doc/test for a particular function
* Realize function args aren’t that json-friendly, fix them
* Come across obscure bug in serialization preventing example from working, spend hour tracking down and fixing
* Realise fix has to go into grin core, create that PR
* Realise function needs a statically-seeded test RNG to produce consistent output every time, implement that,
* Realise doctest helper functions need more work to support this particular function, implement and test that
* It’s 4 hours later and I’m still working on documenting the same function.
* etc, etc, etc.

It’s been like this for just about every single function, and it’s only just been since I got to the last few functions of the owner API that the testing started to go a bit smoother, as most of the bugs and changes required for testing have been ironed out. The upside is that this has been a great test of the V2 API generation, and this should be invaluable going forward to keep the V2 API clean, consistent and documented. The downside is it’s tedious as hell and I can’t stand looking at it anymore right now. Luckily, it’s [mostly there](https://github.com/mimblewimble/grin-wallet/pull/24), with most API functions and their doctesting complete. I’ll come back and complete when I’m more fresh, but luckily this big push to get the API documentation started should only have to happen once. Doc and test changes from here on out should be incremental and more focused, and hence easier to bear.

Right, I need to go do something that’s not aligning JSON brackets. Enjoy weekend!

---

### Post by @Yeastplume ⭐ (2019-03-29)
*Post #15*

Update Friday, March 29th, 2019

Had a good time at [Grin Amsterdam](https://www.meetup.com/Grin-Amsterdam/events/258141382/) during the early part of the week, all a bit of a blur but there’s plenty of video and other documentary evidence from the event. I can never watch videos that include myself, so I’ll leave the simple job of tracking them down to any interested readers.

As for the rest, I’m just in the process of merging a [final v2 PR](https://github.com/mimblewimble/grin-wallet/pull/32) finishing up the API documentation and making a few tweaks and changes to make it as friendly as possible. What’s there after this PR is merged should more or less be what the V2 API will look like for 1.1.0. It is by no means perfect, and minor version numbers (1.2.x, 1.3.x etc) with additions and changes will hopefully be coming on a more frequent basis than the main Grin executable. However, all of this work the past few weeks was vital to ensure changes will be (more or less) self-testing and as self-documenting as possible, which should greatly benefit all future work.

So short terms tasks are now:

* Wire the rpc-json API into the http listener (so there should be a v2 api listener on the endpoint as well as the previous)
* Merging grin’s master branch into the 1.1.0 branch, to prepare for 1.1.0 testing
* Much testing of the wallet 1.1.0 branch to ensure things aren’t completely broken (though hopefully the amount of code not covered by unit testing is significantly shrunk)
* … All other bits and pieces related to the release of 1.1.0

Looking very forward to getting all that done… see you next week!

---

### Post by @Yeastplume ⭐ (2019-05-03)
*Post #19*

Update Friday, May 3rd 2019

Just a quick update this week as I’m currently travelling over a long weekend

* Work on the [api support for invoice transactions](https://github.com/mimblewimble/grin-wallet/pull/90) is complete, documented, tested and merged. Complete details for those interested in trying it out via the
API can get all the documentation via rustdoc

* I’m currently working on the obvious follow up, [enabling invoice transactions in the command-line wallet](https://github.com/mimblewimble/grin-wallet/pull/96). Progressing steadily there and should have it ready for 1.1.0 (coming any week now!)

* As a skunkworks side project/learning experience, I’ve been putting together a rust implementation of [SLIP-39: Shamir Secret Sharing for mneumonic codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md), which I hope to integrate into the wallet as some point a nice feature-add. Basically, master key sharing where you can take your bip39 mneumonic and split it into a 3 of 5 (for example) threshold scheme to distrubute to family members. The underpinnings here also relate to future multisig wallet features. Much more on this later, but intend to get the implementation public as soon as I’ve got all the embarrassing bits out.

That’s all for now, enjoy long weekend (provided you have one).

---

### Post by @Yeastplume ⭐ (2019-05-10)
*Post #20*

Update Friday, May 10th 2019

Good week of steady progress, I think, with demonstrable results for everything mentioned in last week’s hasty post.

Firstly, [the command line support for invoice transactions](https://github.com/mimblewimble/grin-wallet/pull/96) is now completely in place in grin-wallet master. Instructions on how to use it are in the executable help, and writing this has just reminded me that I need to document the new commands on the wiki (unless someone else gets there first). Will get to that shortly.

In slightly bigger news, [@quentinlesceller](/u/quentinlesceller) has completed his work migrating CI from travis to Azure pipelines, which means we’re now able to produce builds for grin and grin-wallet for all 3 major platforms with a single tag. Since I’m pretty much done with feature adds for 1.1.0 wallet, I went ahead and did the [1.1.0-beta-2 build](https://github.com/mimblewimble/grin-wallet/releases/tag/v1.1.0-beta.2), which you can now download and start playing with. However, I don’t believe a 1.1.0-beta.2 build has been created for grin server, so you’ll either have to wait for that or compile grin from master. I’d imagine the grin 1.1.0-beta.2 should be out any day now (going to check on gitter right now)

Also, as mentioned last week, I’ve been working on an implementation of [SLIP-39: Shamir secret sharing for mnemonic codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md), which I’ve now made public on github at <https://github.com/yeastplume/rust-sssmc39>. I’ve been working on this as a bit of a side project in the background and hope to get it up a decent enough standard for inclusion in grin’s wallet. The process of doing this has given me a good education in secret sharing, which leads into future research on supporting multisig in the wallet since threshold signatures work using the exact same concepts. The wallet also gets a nice little feature add which I don’t think exists on any other wallet at present. Here’s a small example, from the lib’s test output:

My 12 Word wallet master key (BIP39 mnemonic) is run through the lib and split into a 3 of 5 scheme. The output is as follows:

Group 1 of 1 - 3 of 5 shares required:
pajamas walnut academic acne already upstairs perfect soldier stay trial always cradle midst dryer debut desktop snapshot kernel belong dramatic
pajamas walnut academic agree desktop lobe breathe avoid mule rapids injury task obesity briefing heat born level making medical painting
pajamas walnut academic amazing apart exhaust tenant away yelp mayor blessing prisoner plunge pants very calcium credit unfair rainbow negative
pajamas walnut academic arcade early disease fragment slow pulse software guilt flea paper lizard profile dynamic isolate calcium course agency
pajamas walnut academic axle deliver scene health afraid recall hormone lawsuit kernel cards holy fatigue cradle sympathy award much force

I can then take these split shares and distribute them to 5 family members. Each share is useless on its own, but when I get hit by a bus tomorrow (“he should have quit drinking vodka before noon”,) then any 3 of my 5 family members can get together, recreate my master key and enjoy my grins. There are multiple levels to the scheme, so it’s also possible to create splits that divide your key among multiple groups, like '2 of my personal shares can recreate the seed, or one of my shares plus 3 of 5 family members if I lose a share). There are literally infinite possibilities here, and I hope this implementation is a step toward making key management more… manageable.

So that’s it for now. I’m gonna split now (ROFLLMAOLOLLOLetc…). enjoy the weekend!

---

### Post by @Yeastplume ⭐ (2019-05-17)
*Post #24*

Update Friday, May 17th 2019

Got very sucked into completing tests and puttin finishing touches on the [Shamir Mnemonics](https://github.com/yeastplume/rust-sssmc39) code this week, and happy to say it’s fairly close to completion, with the major remaining tasks being completing some integration testing, CI and release work, and of course whatever reviews we can get on it.

That little segue mostly aside, [grin-wallet 1.1.0-beta.3](https://github.com/mimblewimble/grin-wallet/releases/tag/v1.1.0-beta.3) is released alongside Grin 1.1.0 beta 2., and I hope this is a short lived beta so we can move on to creating a 2.0.0 branch and get started on some major wallet work in advance of the scheduled hard fork.

No firm commits here as to what will get into what version, but as far as major near-term work I’m considering:

* [@jaspervdm](/u/jaspervdm)’s [updated recovery scheme](https://github.com/mimblewimble/grin-wallet/issues/105), which should allow for more flexibility with structing wallets (which I still need to review in detail (sorry [@jaspervdm](/u/jaspervdm)).

* [@mcdallas](/u/mcdallas) has been looking into encoding slates into minimized base-64, which many people think is worth including.

* Complete lifecycle management via the API, meaning that you should be able to create and manage multiple wallets via the owner api. Naturally there are a lot of other small little issues that need to be dealt with here, particularly around master key management. This will probably be a meta issue under which some discussion and refactoring work will fall in order to allow it

* Pulling the BIP-32 code out of grin and place it into a separate repository (as a) it really doesn’t belong in grin and b) and I’d like it split out to be included by the wallet API as part of lifecycle management work above to give greater flexibility in generating keys)

* Integrating sssmc39 as an option in the wallet api

That’s it for now. Enjoy weekend and hope we can get our final 1.1.0 releases early next week!

---



## Announcing the Grin++ Wallet! (finally!)
*Date: 2019-03-19 | [Forum Link](https://forum.grin.mw/t/announcing-the-grin-wallet-finally/4546)*
*Importance Score: 85.9 | Core Participants: david, jaspervdm*

### Post by @david ⭐ (2019-03-19)
*Post #1*

After getting delayed several weeks (sorry!), the Grin++ wallet is finally here! It took a lot of time to get everything to work well together, and there’s still plenty more to do, but I invite you all to try out the first beta release (floonet only): <https://github.com/GrinPlusPlus/GrinPlusPlus/releases/>

Although the official Grin client is obviously much more stable and well-tested, Grin++ offers several advantages. Here are just a few:

* Full Windows support
* Simple to use electron UI
* Multi-user support
* Lightning fast refreshes & wallet restores
* Full AES w/scrypt encryption to protect your coins and privacy
* Passwords never stored in memory

Planned Enhancements:

* HTTPS support
* Magic wormhole
* Multisig support
* Better error handling
* Mac Support
* and much, much more

Keep in mind that this is a beta release, and should NOT be used on mainnet. There are a few known issues and limitations with it, which I’m actively working to fix, but feel free to report bugs as you come across them.

Now, the part I don’t enjoy:
I’ve worked tirelessly on Grin++ over the last 6 months trying to get everything working, and have been fortunate enough to not have the need to ask for anything in return. That is, sadly, no longer the case. I’ve decided to leave my job so I can spend some time focusing on Grin++, and no longer have any source of income (YOLO, as the kids say). Naturally, I will be burning through my savings, and my wife probably won’t put up with that for long :). If anyone is in a position where they could help out, and allow me to continue to focus on building Grin & Grin++, I would be eternally grateful.

I’m accepting donations in Bitcoin, or if you want to send me some Grin, just message me.
BTC: 1EF6PmGJiQawozyGfZhyG1bsqbuJsGbmTv

As always, if you have any questions or would like to help out with the project, I can’t wait to hear from you! Come find me on Gitter, or email me at [davidburkett38@gmail.com](mailto:davidburkett38@gmail.com). Thanks!

---

### Post by @david ⭐ (2019-04-08)
*Post #25*

[@xiaojay](/u/xiaojay) Unfortunately, no. I started with the same APIs, but there were 2 issues:

1. v2 APIs were being developed faster than I could keep up with.
2. I didn’t like the idea of storing passwords in memory.

For these reasons, I modified the APIs to better suit my needs, including creating a login token system that all of my APIs use, and moving the foreign API to the front-end. Many of the APIs are very similar though (some identical aside from the additional token). If you’re still interested, I’d love to work with you to add Grin++ support to Niffler.

---

### Post by @david ⭐ (2019-04-19)
*Post #34*

Thanks for pointing that out. I have updated the readme.

---

### Post by @david ⭐ (2019-06-14)
*Post #41*

Transactions for Grin are interactive, requiring both parties to work together to build a transaction. There are several methods of performing this interaction. Grin++ supports 3 such methods: File(preferred), http(s), and grinbox. A typical transaction has 3 steps:

1. Init Send - In the initial step, the sender initiates the transaction and creates an in-process transaction. This in-process transaction is referred to as a “slate”.
2. Receive - The recipient adds his or her outputs and signature(s) to the “slate”, and returns this updated slate back to the sender.
3. Finalize - The sender adds their signature(s) and completes the transaction before sending it to the node to be included in a future block.

Sending by file, although currently the preferred way of sending grin, requires you to manually perform each step, whereas when sending by http(s) and/or grinbox, all of that happens without user-interaction as soon as the sender hits the “send” button. So in Grin++, the finalize button is only ever used when sending via file.

---

### Post by @david ⭐ (2019-12-31)
*Post #60*

There is an issue with receiving on mac. I’ll get a fix out today.

---

### Post by @david ⭐ (2019-12-31)
*Post #69*

I’m sorry you feel that way. Grin++ was developed as a windows-first node and wallet, but was highly reviewed and ended up being requested by dozens of Apple users. I reluctantly decided to create a mac version since, despite what you say, there are not “so many other working options”. Unfortunately, doing so has led to real headaches for myself (because mac doesn’t “just work”).

But the biggest problem is not necessarily Grin++, but the Grin protocol in general, which is very young and fragile. The sync process relies on downloading a massive zip file from a single peer, and to make matters worse, most of the peers on the network (running Grin, not Grin++) are actually serving bad zip files due to a bug in 2.1.0 and 2.1.1. This can cause syncing issues and data corruption, and I’m working hard to make this less frequent, but it’s a challenging problem to solve. fwiw, grin also corrupts data frequently.

The reason your “3 other Grin wallets” all work fine is that they are all sharing the same node data. Grin++ uses a different storage method, and it got corrupted. If Grin’s node data corrupted instead (which also happens frequently), then all 3 of those wallets would stop working instead.

Anyhow, thank you for your feedback. I encourage you to reach out if you continue to have problems. For quicker responses though, I recommend using the Grin++ telegram channel at [t.me/GrinPP](http://t.me/GrinPP)

---

### Post by @david ⭐ (2019-12-31)
*Post #71*

kelliblueeyes:

> I deleted the old version, I deleted the mainnet/node, and grin++ gives me the same error.

Have you run Niffler at all? It actually keeps the grin process running in the background on close, which conflicts with Grin++ (and all other nodes). In activity monitor, make sure there are no Grin related processes running.

Also, which Mac OS version are you running?

---

### Post by @david ⭐ (2019-12-31)
*Post #74*

kelliblueeyes:

> same error, don’t worry about it

I have to worry about it. Otherwise, how can Grin++ ever go from a “broken” app to a stable one?  It works perfectly fine on all of my macs.

---



## [POTENTIAL SCAM?] Grin Web Wallet - Confidentially Safely Conveniently
*Date: 2019-03-31 | [Forum Link](https://forum.grin.mw/t/potential-scam-grin-web-wallet-confidentially-safely-conveniently/4693)*
*Importance Score: 105.4 | Core Participants: david, lehnberg*

### Post by @Chief_Dementor (2019-03-31)
*Post #1*

We are glad to present Grin Web Wallet!
Grin Web Wallet - Confidentially Safely Conveniently
[Grin Web Wallet](https://mygrin.org/)
Grin Web Wallet allows you to safely hold, easily receive and send your Grin coins from any devices that has a browser and access to the Internet.

---

### Post by @david ⭐ (2019-09-30)
*Post #126*

24 hours is unacceptable. The address Grin++ generates, for example, is only valid for 8 hours. Any connection disruption along the way can cause you to lose that address as well. Exchanges should not take more than a few minutes to execute the withdrawal, and if they do take longer, they’re setting themselves up for an unnecessarily high number of support emails.

---

### Post by @david ⭐ (2019-09-30)
*Post #128*

Grin++ 0.6.4 is completely compatible with grin-wallet 2.0. Your exchange is just uninformed (most are). I would encourage restarting the Grin++ wallet before trying to withdraw again, since Bitforex clearly takes a long time.

---

### Post by @david ⭐ (2019-10-25)
*Post #142*

It’s much easier to modify grin-wallet to support multiple wallets than to make the kind of changes to support maintaining balances using a single wallet.

But let’s be honest with ourselves. This is a web wallet developed and maintained by a nym. There’s no way they’re going to let users control the keys. 11 years of bitcoin web wallets would suggest that the plan has always been to run away with everyone’s money. It’s not a matter of ‘if’, but ‘when’. I hope this turns out to be the one exception, but I’m not optimistic.

---

### Post by @lehnberg ⭐ (2019-11-25)
*Post #168*

[@Periurium](/u/periurium) this is now marked as `[SCAM]`

---

### Post by @david ⭐ (2019-12-11)
*Post #175*

It’s a scam. Hopefully they didn’t steal too much from you. In the future, avoid storing crypto in web wallets.

---

### Post by @david ⭐ (2019-12-11)
*Post #180*

Do they send via HTTP? You might have to forward port 3415, and withdraw using your public IP ([whatismyip.com](http://whatismyip.com)). Use the address: `http://<PUBLIC_IP>:3415`

---



## Niffler, An out-of-the-box open sourced Grin GUI Wallet
*Date: 2019-04-08 | [Forum Link](https://forum.grin.mw/t/niffler-an-out-of-the-box-open-sourced-grin-gui-wallet/4760)*
*Importance Score: 184.2 | Core Participants: david, davidtavarez, quentinlesceller, antioch*

### Post by @xiaojay (2019-04-08)
*Post #1*

Hello, I am glad to release an open sourced Grin GUI Wallet – Niffler.

The name ‘Niffler’ also comes from [“harry potter”](https://harrypotter.fandom.com/wiki/Niffler).

Github page: <https://github.com/grinfans/niffler>

Download link: <https://github.com/grinfans/niffler/releases/latest>

currently, only Mac beta version. Windows/Linux version will release soon.

## Features

* simple, straightforward user interface
* support multiple multiple languages(now is for English and 简体中文)

## Screenshot

#### Create new wallet

#### Send grin

#### Receive grin

## Help wanted

A logo from any designer in this community will be much appreciate

---

### Post by @xiaojay (2019-06-19)
*Post #42*

Yes, it’s wired.

ok, here the instructions to restore on mac with Niffler:
1、open Terminal. entry command:
mv ~/.grin ~/.grin2

2、start Niffler wallet. Chose “Restore wallet from seed phrase”

[ 屏幕快照 2019-06-19 20.16.19.jpg1206×250 59.1 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/718c7052fe6e6591e4385ebd406bd17eed24ba83.jpeg "屏幕快照 2019-06-19 20.16.19.jpg")

[ 屏幕快照 2019-06-19 20.18.51.jpg1286×1096 181 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/ea7f20928ac75eec580704366b99a00650fc85a4.jpeg "屏幕快照 2019-06-19 20.18.51.jpg")

---

### Post by @xiaojay (2019-07-04)
*Post #63*

Niffler wallet v0.4.0 is available.

[github.com](https://github.com/grinfans/Niffler/releases/tag/v0.4.0)

### [Release 0.4.0 · grinfans/Niffler](https://github.com/grinfans/Niffler/releases/tag/v0.4.0)

[s/tag/v0.4.0](https://github.com/grinfans/Niffler/releases/tag/v0.4.0)

Niffler v0.4.0 is an beta version, which support Grin's first hard fork in Mid-July. It's use the official grin-wallet v2.0.0 as backend. Niffler 钱包 v0.40 是一个支持Grin在7月中旬第一次的硬分叉的Beta版本， 使用官方的命令行钱包gr...

Niffler v0.4.0 is an beta version, which support Grin’s first hard fork in Mid-July.
It’s use the official [grin-wallet v2.0.0](https://github.com/mimblewimble/grin/releases/tag/v2.0.0) as backend.

Download it and reinstall before hard fork

---

### Post by @david ⭐ (2019-12-10)
*Post #122*

Via GUI:
Open Finder
Shift+Apple+G (or open Go from main menu and choose “Go to Folder…”)
Dialog will pop up - Type `~/.grin/main`
Hit GO

---

### Post by @quentinlesceller ⭐ (2020-01-16)
*Post #141*

very nice [@xiaojay](/u/xiaojay)! Does it uses the v3 wallet API?

---

### Post by @davidtavarez ⭐ (2020-05-27)
*Post #165*

for the infinite “`Waiting for peers`”, here’s a shortcut… close the wallet (Grin++), then go to `C:\Users\[USER]\.GrinPP\MAINNET`, rename the folder called `NODE` to `_NODE` (or whatever) and open Grin++… this will download the chain again, but you will have everything up and running again.

---

### Post by @xiaojay (2020-07-22)
*Post #186*

Mac version of Niffler v0.6.0-preview is available, which with slatepack support

[GitHub](https://github.com/grinfans/Niffler/releases/tag/v0.6.0-preview)

### [Release 0.6.0-preview · grinfans/Niffler](https://github.com/grinfans/Niffler/releases/tag/v0.6.0-preview)

Niffler wallet v0.6.0-preview support grin4, with slatepack supported 中国大陆下载地址: https://grin-fans.oss-cn-hangzhou.aliyuncs.com/Niffler-mac-0.6.0-preview.dmg

[截屏2020-07-22 下午9.43.221206×1222 185 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3890c8dc5eca1a1db14bcf3b0277d6315246d3c5.png "截屏2020-07-22 下午9.43.22")

---



## What is the intended market/use-case of Grin?
*Date: 2019-04-09 | [Forum Link](https://forum.grin.mw/t/what-is-the-intended-market-use-case-of-grin/4774)*
*Importance Score: 88.7 | Core Participants: tromp*

### Post by @SiriusB (2019-04-09)
*Post #1*

What is the purpose of Grin? What in your opinion is the use-case of Grin? Why would someone use Grin versus the other 1,000+ coins?

Merchants online won’t like the lack of transaction proof. There are other privacy coins with bigger networks already extant. And then there’s the issue of why people should use Grin instead of dollars, debit cards, PayPal, Venmo etc. People can hoard cash in their mattress and use dollars privately with no bank control now, so why Grin?

What, in your opinion, is the reason for Grin, specifically versus all the other coins and traditional payment methods that already exist? Who is Grin for? And how would you convey this idea in marketing?

---

### Post by @0xb100d (2019-04-10)
*Post #12*

Better logo than any competition.

Also the attempt to make running a node have lower overhead than competitors also is an attempt to make it “fairer.” Be your own bank works best if you can actually run the bank software yourself. And regarding the fairness of the distribution, it is objectively fairer by a bunch of metrics. The window to hoard all your bitcoin was very short before it started becoming too expensive to buy many of, this is hypothetically solved by grin. This means more people can “get bags” more easily. We don’t know yet if this is better game theory wise, but it is definitely going to give people more time to find out about grin and start messing with it before a grin is worth a bunch of money.

Regarding proving transactions: this is the same as cash. A merchant cannot prove you paid them in cash except by keeping the best records they can. This is in many ways a feature of grin and not a bug. It’s also trivially easy to use other methods (like a self-hosted [grinbox.io](http://grinbox.io) instance) if you are a business and want to incorporate some proof of tx. There is ongoing discussion on how to accomplish this with minimal tradeoffs: <https://github.com/mimblewimble/grin/issues/2652>

[TMGOX.com](http://TMGOX.com) just implemented grin payments. It would not work if it was not possible to wait to confirm that a transaction ocurred and blocks have been mined on top of the transaction block. (thanks to hashmap and cycle42).

Intended market/use case is the same as bitcoin/monero or cash, except that it is based on the lessons people have learned in the past years about how to launch a blockchain, and it does some super interesting new math to keep things private and lightweight. We are so early in the history of these non-sovreign currencies there’s no way to say who will win. Bitcoin could completely disappear in 50 years, and looking at the number of companies that were the first mover in their niche only to be replaced by better products, it seems likely bitcoin will be more historical than practical. There is no reason not to create diversity of experiments and see who fares best, for the sake of everyone. We can learn in these early days and someday maybe actually succeed in the goals of non-sovreign global electronic cash on a large scale.

Why are there more than one type of bird? Why do countries not all just use the Euro across the globe?

---

### Post by @SiriusB (2019-04-11)
*Post #29*

Because there are no addresses. The MimbleWimble protocol basically is just interacting private keys that sign transactions. The blockchain verification only checks that nothing has been created or destroyed, but fogs the actual amounts with a blinding factor composed of the always-hidden private keys. There are no public addresses. The blockchain doesn’t store amounts and there are no public addresses to store at all.

**Basically, MimbleWimble is like cash and the private keys are like hands that pass the cash. The banker-in-the-sky, the blockchain, only verifies that all cash passes were done in a way that no cash was passed that wasn’t held, and no cash received that wasn’t passed. It doesn’t track who passed what to who or how much. That’s how it’s private (because there is no record of amounts or identities stored on a public blockchain). And how it scales (because it doesn’t have to store all that information).**

An https listener can receive, but that’s just putting your hand on a server to be able to always receive passed cash, it doesn’t change the protocol or tell you anything about the sender, the purchaser of goods.

And you can arrange your purchase through email and your attached transaction file when processed proves you paid, but then why use a complicated, private currency if you’re going to do that anyway. Might as well use your credit card and get purchase protection.

Also, Monero is not as private as it seems. Both the mixins and the stealth addresses can be traced. There was an academic paper on this in 2016, and the code revisions in 2017 didn’t actually address the liabilities supposedly. MimbleWimble is truly private: you can’t trace or hack what simply isn’t there. However, there’s the rub, how does a merchant even know a Grin payment was made? The only way is key exchange, blah blah blah that defeats the point of a private coin. And again, use any top ten coin for merchant purchases only. There’s probably a cool mobile wallet for it already, and a payment portal.

---

### Post by @tromp ⭐ (2019-04-11)
*Post #34*

jasonzhouu:

> However MimbleWimble’s node doesn’t need to store all history transaction, even 100 years later, the full node only needs to store <200GB transaction data.

MW’s long term storage requirements are about 1/3 that of Bitcoin. Instead of storing a bitcoin tx of around 300 bytes, it needs to store a kernel of around 100 bytes. At 10 tx/s that amounts to nearly 30 GB per year.

---

### Post by @jasonzhouu (2019-04-11)
*Post #38*

Actually, inflation rate of Bitcoin and Grin don’t have big difference in the long run

[ IMG_3345.JPG1192×826 50.1 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3680b6d70c43659770b559b3de737deb644272f4.jpeg "IMG_3345.JPG")

image source: <https://plot.ly/~Bobby_Digital/1/#/>

---

### Post by @tromp ⭐ (2019-04-11)
*Post #42*

Grumpy:

> So early on bitcoin was being emitted 5x faster than grin.

1/12 BTC per second is 12x slower than Grin.
You seem to have seconds and minutes confused…

---

### Post by @tromp ⭐ (2019-04-14)
*Post #49*

kargakis:

> This is compared to Bitcoin w/o CT, right?

Yes; I do not expect to see CT on the bitcoin main-chain,
but if added, then a typical 2 output tx would increase in size to nearly 2KB due to rangeproofs. In that case MW offers more than an order of magnitude long term storage savings. And no bandwidth savings.

---

### Post by @jasonzhouu (2019-04-14)
*Post #53*

Grumpy:

> not many that are bullshit-free like grin.

Even if all Bitcoin are bought by government, people can fork a new Bitcoin which is also bullshit-free, with the same technology of the original Bitcoin. And don’t need to worry about backward compatibility, so many new technology can be applied, like schnorr signature, MAST, taproot, confidential transaction…

---



## mid-July PoW hardfork: Cuckaroo29 -> Cuckarood29
*Date: 2019-05-28 | [Forum Link](https://forum.grin.mw/t/mid-july-pow-hardfork-cuckaroo29-cuckarood29/5082)*
*Importance Score: 67.8 | Core Participants: tromp, jaspervdm*

### Post by @tromp ⭐ (2019-05-28)
*Post #1*

A major part of what makes our secondary PoW of Cuckaroo29 ASIC-resistant is frequent tweaking. The first such tweak is due 6 months after genesis, in mid July. Which is now only about 6 weeks away.

In the 133 days of Grin mining so far, there is no sign of any ASIC mining. We do know of several ASIC products planned to come out in Summer.
To the extent that any such ASICs have built in support for Cuckaroo29, we want our tweak to brick that support.

There are 3 separate aspects of Cuckaroo that could be tweaked:

1. the underlying hash function, currently siphash-2-4
2. the computation of endpoints of a whole block of edges
3. the type of cycle

I’ve chosen to leave 2) entirely alone and make tweaks in 1) and 3).

The tweaked siphash is defined by templating on one of the rotation amounts:

template <int rotE = 21>
class siphash_state {
...
void sip_round() {
v0 += v1; v2 += v3; v1 = rotl(v1,13);
v3 = rotl(v3,16); v1 ^= v0; v3 ^= v2;
v0 = rotl(v0,32); v2 += v1; v0 += v3;
v1 = rotl(v1,17);   v3 = rotl(v3,rotE);
v1 ^= v2; v3 ^= v0; v2 = rotl(v2,32);
}

and using siphash_state<25> in cuckarood rather than the default 21.

The new type of cycle is a directed one. Half the edges (those with even index) are directed from U to V and the other half (with odd index) is directed from V back to U. Alternatively, we can just say that the cycle must alternate between even-indexed and odd-indexed edges. At the same time the number of nodes in each of U and V is halved. So Cuckarood29 will have 2^28 U-nodes + 2^28 V-nodes, 2^28 U->V edges, and 2^28 V->U edges.

Curiously, this results in twice the expected number of cycles.
We will not be making any difficulty adjustments. That means that if half the current Cuckaroo29 miners fails to upgrade, then the secondary PoW solution rate will remain unchanged. If everyone upgrades in time, then average block time could drop to 36 seconds, but ar_scale will adjust downward to compensate and things will normalize in a few hours.

About the name: the appended ‘d’ mostly stands for directed, but as in SHA256d could also denote a doubling (of solutions).

Implementation wise, there is a new cuckarood directory at <https://github.com/tromp/cuckoo/tree/master/src/cuckarood>

In there you can find the new verifier in cuckarood.hpp and both a simple CPU miner and a CUDA mean miner.

A Grin PR is available at
[github.com/mimblewimble/grin](https://github.com/mimblewimble/grin/pull/2866) [ ](https://github.com/tromp)

####  [[WIP] PoW HardFork](https://github.com/mimblewimble/grin/pull/2866)

by [tromp](https://github.com/tromp) on [09:50AM - 30 May 19 UTC](https://github.com/mimblewimble/grin/pull/2866)

**3 commits** changed **8 files** with **255 additions** and **46 deletions**.

---

### Post by @0xb100d (2019-06-04)
*Post #2*

I just want to suggest we maybe call the AR variations something simpler like CUCKAROO29A/B/C instead of a whole new name. We already have a pretty clever (and a a little complicated) nomenclature and I don’t think we need any more variations on base naming conventions.

---

### Post by @tromp ⭐ (2019-06-04)
*Post #3*

0xb100d:

> instead of a whole new name

It’s not a whole new name. It’s Cuckaroo[a-z]29 where the extra letter somewhat describes the nature of the tweak.
Furthermore, since the tweaks are not size specific, I chose to put the size after the tweak indicator.
In other words, Cuckarood is a uniform familiy of PoWs ranging from Cuckarood6 through Cuckarood32, and you may want to refer to this family by name without referring to a specific size.

---

### Post by @0xb100d (2019-06-04)
*Post #4*

So in six months it will likely be CuckarooE29?

---

### Post by @FirsArgentum (2019-06-04)
*Post #5*

Maybe it could skip to Cuckaroof?

---

### Post by @tromp ⭐ (2019-06-04)
*Post #6*

Just a warning to all letters of the alphabet (except ‘d’):

any of you could be next!

---

### Post by @jaspervdm ⭐ (2019-06-05)
*Post #8*

The ASICs are for cuckatoo which remains unchanged.

---

### Post by @tromp ⭐ (2019-07-17)
*Post #12*

We hardforked to Cuckaroo29d as secondary PoW this morning… Cuckaroo29 is no more (although some miners are still submitting obsolete Cuckaroo29 shares).

---



## Proposal: Grin Governance Iteration
*Date: 2019-06-12 | [Forum Link](https://forum.grin.mw/t/proposal-grin-governance-iteration/5191)*
*Importance Score: 79.5 | Core Participants: yeastplume, joltz, lehnberg*

### Post by @lehnberg ⭐ (2019-06-12)
*Post #1*

# Grin Governance iteration

## Tl;dr

Evolve Grin’s governance:

* Introduce RFC (Request For Comment) process
* Introduce self-governing sub-teams that steward and guide work in each of their focus areas.
* Convert council into core team and define its responsibilities
* Recognize more contributors
* Achieve less centralization

## Motivation

### Background

Grin governance today consists of the Grin Technocratic Council, and the rest of the community. The council came to be as there was a need for some sub-set of community members to manage the multi-sig keys of the Grin General Fund, and it became a modest first pass at a governance structure. Over time, it has come to be that a lot of responsibilities and day to day tasks are handled by Grin council members. This puts a heavy workload on council members, but it also inhibits other members of the community from becoming more engaged, contributing more, and becoming recognized for it. Naturally this implies that either the council would have to grow large in order to be able to fit all the members of the community that deserve recognition for their contributions, or that we end up not rewarding active contributors properly.

As most decisions are taken in the bi-weekly meetings, it’s come to be that decisions take time to materialize: It can take up to 14 days just to have the initial conversation and sometimes multiples of that to reach an agreement. In these meetings the entire active community ends up participating in every discussion, in a synchronous fashion that often does not end up being productive.

We also struggle to answer more fundamental questions about Grin’s governance, as in how decisions are made, who has authority to make these, and what the path is for a community member who would like to take on greater responsibilities.

This is a proposal to evolve our governance process.

### Objectives

* **Reward and recognize contributions better.** Offer different ways to become more engaged and give better recognition for work
* **Empower more to contribute.** Encourage more community members to participate, facilitate more initiative.
* **Make Grin less centralized.** Rather than relying on a small group of people, share responsibilities and make the project more resilient against shocks.
* **Create a more transparent process.**

### Not objectives

* **Do not create fiefdoms.** Do not create emperors. Nobody is anybody else’s boss.
* **Do not create bureaucracy for the sake of bureaucracy.** Do not impose death by a thousand papercuts or let forms and administration get in the way of making progress.
* **Do not discourage contributions.** Nobody can prevent someone else from doing work. Anyone can contribute in which ever way they find meaningful. You do not need to ask for permission.

## Proposal

This proposal outlines a set of loose principles to guide the work we do. While some of these may already be in use, they might not have been articulated before. It converts the council into a core team, and outlines its responsibilities for the first time. In addition, it’s proposed that additional teams are introduced alongside it, as well as an RFC process. An initial teams breakdown is suggested, and the proposal concludes with a path to adoption.

### General principles

* **Lead by example.** “Cypherpunks write code.” We don’t tell others what to do. We do what we can, and if we need to we ask for help. We suggest, but never command. We act as we want others to act.
* **Not a democracy.** We are evaluated based on the work we do. It’s not a popularity contest, and the majority is not always right. Community members are here by their free will, participation is optional.
* **Influence is measured by recent and not historical work.** We are grateful for and respect historical contributions, but they do not lead to lifelong positions of authority. Influence is earned by making contributions consistently over time, allowing new contributors to join the ranks of the old.
* **Transparency.** Where possible, discussions and decisions are made in the open. We have nothing to hide, and we do not try to limit oversight unless there’s a defensible reason to do so.
* **Keep things lightweight.** We strive to only put in place the minimal structure and organization that’s needed, neither more nor less.
* **Groups organize themselves.** Structures do not need to be imposed tops down, and we recognise that what works for one group will not necessarily work for the other. Teams self-organize and define their own workflows and processes as they see fit.
* **Consensus-seeking decision making.** Voting creates winners and losers, and is polarizing. We recognize there are trade offs with everything and rarely any single right answer. This does not mean design by committee. We seek consensus through dialogue and discussion, but where there is a lack of consensus, we do not let it block us indefinitely. We’re ready to make judgment calls to the best of our abilities.
* **We speak for ourselves.** We can only speak in the name of ourselves, as contributors to the project. We do not write blog posts, articles, tweets, or give interviews speaking on behalf of the project as a whole. Grin itself has no single voice.
* **There’s no need to ask for permission.** We are not afraid to take decisions. We ask for feedback and opinions from others, but we do not need to ask for somebody’s permission. If we believe it’s in the best interest of Grin, we act, and are accountable for our actions.
* **Mistakes are tolerated.** As with any organization structure, mistakes happen. This is understood, and mistakes are accepted. We try to learn from them and improve. We assume we all act in good faith, until proven otherwise.

### Core team

The existing grin council is proposed to be renamed to core team. The core team leads the wider Grin project as a whole. In particular:

* **Sets overall direction and vision.** Core values and philosophies. Steering towards use cases and targets.
* **Sets priorities and plans releases.** Maintains high level planning, roadmaps, focus areas, decides on pace and the release schedule.
* **Work on broader, cross-sectional issues.** What falls in-between sub-teams, taking a global view.
* **Adds and removes sub-teams.** While proposals for new sub-teams can come from anywhere, the core team is responsible to ensure structures are productive and make sense.
* **Responsible for security.** Handles disclosures, vulnerabilities, audits, processes.
* **Handles multi-sig keys and takes high level spending decisions.** Spending proposals can be made by anyone, and sub-teams can have their own own budgets to deal with as they please.

The core-team is self-selecting, and _may include_ sub-team members. Over time, it’s intended to be a broad representation of the wider community with diverse stakeholders.

### RFC process

An RFC is a Request For Comments document, outlining a proposed improvement or design change to an area of Grin. The exact specifics for the template is TBD. They are kept in their own dedicated repo and need to be accepted before a pull request is merged. Their purpose is to outline a standardized way of making proposals and allow the community to discuss and evaluate whether something is worth doing. Having an RFC accepted means that there’s support “in theory” for the suggestion. It does not mean that a change becomes implemented automatically or in the exact way it is proposed, it is high-level design. The work still needs to be carried out. Accepted RFCs guide the broader planning work.

### Sub-teams

Sub teams are groups organized around specific areas or knowledge fields. They are responsible for these areas, but do not do all the work. Anyone can contribute anywhere, and do not need to hold a particular title to do so.

Rather, sub-teams work on policies, processes, and workflows for their specific areas, as required. They are in charge of the RFC process in their specific field: They determine what requires an RFC in their area, they assign RFC shepherds that guide an RFC through its various stages and ensures the right stakeholders become aware of it and solicit their feedback. Ultimately, sub-teams decide whether an RFC in their area should be accepted or rejected. They are responsible to ensure that each RFC in their area has a tracked status, and that they progress towards an outcome.

Sub-teams self-organize. They should have a leader, often this leader may be part of the core team. They determine how members get added to the team. They should include area experts, and stakeholders.

Sub-teams can be broken down into smaller working groups or sub-teams, permanent or temporary, as required and is seen necessary for them to be productive.

Each sub-team has a dedicated section on the forum, they should meet regularly, and keep some notes on what was covered and decided. Decisions do not need to happen in meetings, and could for example be handled asynchronously or in the RFC process.

### The teams

In addition to Core team, the following teams are proposed to be created initially.

* **Node development.** Core Grin technology, changes and optimizations to the node and anything consensus related, research and discussion of new technologies, proof of work.

* **Wallet development.** wallet technology, wallet API, wallet-related research.

* **Infrastructure.** Technical documentation, non-technical documentation, QA, testing, toolchain, developer productivity, guides, how-tos.

* **Ecosystem.** 3rd party developers interaction (wallets, pools, exchanges and others), integration and technical assistance, growing the grin ecosystem, stakeholder collaboration.

* **Community.** Onboarding of new community members, website, chat channels, conferences, events, meetups.

* **Fundraising.** Sponsorships, donations, activities to increase project funds.

* **Moderation.** Code of conduct, handles violations, across all areas of the project. To avoid biases and conflicts of interest, this sub-team _does not_ contain any member of the core team.

### Adoption path

1. Publish proposal on [grin-forum.org](http://grin-forum.org), refine as required
2. Discuss in governance meeting, refine as required
3. If approved;
* Sub-teams:
1. Appoint team leads from council/core where available
2. Let sub-teams without leaders self-form once there is someone ready to step up
* RFC process:
1. Propose template & process document
2. Create repo

## References

**Rust’s governance process**

* <https://rust-lang.github.io/rfcs/1068-rust-governance.html>
* <https://predictablynoisy.com/rust-governance>
* <http://mgattozzi.com/oss-governance-and-sustainablility-i/>

**Node.js governance**

* <https://medium.com/the-node-js-collection/healthy-open-source-967fa8be7951>

**Swarmwise, by Rick Falkvinge**

* <https://falkvinge.net/files/2013/04/Swarmwise-2013-by-Rick-Falkvinge-v1.1-2013Sep01.pdf>

---

### Post by @grin0 (2019-06-14)
*Post #2*

I propose a [Keybase](https://keybase.io/) team. If you haven’t heard of Keybase - definitely worth checking out. Their team/chat functionality rivals Slack, except it’s free. Keybase itself is rooted in cryptography.

I have a heavy background in Systems Infrastructure & Administration. I would love to be a part of the Infrastructure/Website/Ecosystem teams, or a mixture. I have many years experience in design & implementation of systems, as well as integration. Combined with a customer-service-focused mentality and strong inductive reasoning skills, I believe I could assist Grin. I’ve owned several businesses and am strong in building brand recognition as well. I can assist anywhere from hardware to software, networking to security, servers to desktops. Details gladly provided upon request.

Feel free to message me here or [via Keybase](https://keybase.io/asheroto) (encrypted).

[grin-forum.org](http://grin-forum.org) does not resolve… there is no DNS record for it.

---

### Post by @Yeastplume ⭐ (2019-06-14)
*Post #5*

Just for the record, personally I’m completely on board with this proposal, which is the result of a few weeks of internal discussions among the current council. I really very much urge everyone to read this carefully, reflect, and comment as this is arguably the most important change to Grin anyone has proposed to date.

---

### Post by @joltz ⭐ (2019-06-17)
*Post #7*

[@lehnberg](/u/lehnberg) your proposal looks great and seems to be a solid next step. I’m looking forward to hearing more community feedback. I initially wanted to generally ask if it makes sense to include security solely in the core team responsibilities. Instead I ended up with a proposal for a security subteam as an alternative option. I’d be grateful for any feedback and encourage any discussion for why they think a security subteam would be an asset or a liability.

_Grin Governance Iteration Modification Proposal: Add Security Subteam_
**tl;dr**

* Modify Grin Governance Iteration to include a Security subteam
* Reduce administrative overhead and centralization/liability risk for core team handling all aspects of security
* Empower core team to more efficiently address security with their direction and vision
* Improve transparency, accountability and reaction time for security practices and processes for Grin

**Motivation**
**Background**
Currently the governance iteration proposal puts the responsibility of handling disclosures, vulnerabilities, audits, processes solely on the core team.

The core team may not be now (or may not be in the future) sufficiently supported with the processes and experiences to proactively manage the mentioned security aspects while still maintaining focus on other duties.

Example: security review status indicated <https://github.com/mimblewimble/grin-pm/blob/master/notes/20190611-meeting-development.md>

The culture of security for a project like Grin is important for its long term survival and should be set up in a way that is not weakened with the comings and goings of core team members with varying security priorities and experiences.

A subteam can be suitable to support the technical and administrative overhead necessary for maintaining a long term and proactive security culture in the Grin ecosystem.

**Objectives**

* Cultivate community contributions in security by offering ways to recognize contributions with active engagement and feedback
* Empower the community to take their own security seriously with proactiveness and transparency
* Reduce centralization and other failure risks for handling vulnerabilities
* Improve overall transparency around security processes for the Grin project and ecosystem

**Not Objectives**

* Do not add friction or confusion to the existing vulnerability disclosure system
* Do not compromise the trust of the community

**Proposal**
This proposal outlines the general responsibilities and roles for a security subteam for Grin as well as the advantages and risks.

**Responsibilities**

* Formalize and facilitate responsible disclosure processes (incl. on-call management, disclosure key schemes etc)
* Curate and publish disclosed and fixed vulnerability reports according to the formalized disclosure process
* Design, deploy and maintain bug bounty program
* Manage RFC process for security related policies, processes and workflows
* Manage future audits with team and community feedback through RFC process
* Advocate for and engage in fundraising for future security audits
* Continually assess and address attack vectors on codebase, networks and overall ecosystem
* Coordinate and maintain emergency upgrade network to deploy fixes in cases of severe vulnerabilities
* Maintain coordinator channel for responsibly disclosing vulnerabilities and fixes to forks and other related implementations
* Assist other teams and ecosystem members with scheduled hardforks to encourage secure network upgrades
* Regularly update community with indications of progression in quantum ability
* Engage with community regularly about security related topics in the grin ecosystem (talks, articles etc)
* Provide representation for dev/community meetings
* Monthly reports: internally for core/subteams + publicly for community

**Roles**
At minimum a core representative and dedicated security lead would be required.

The security lead is there to support the direction, vision and priorities of the core team with protocols, procedures and advice.

Eventually a subteam PM could be added to free more time for the security lead to grow the subteam toward reducing reliance on the security lead (assuming the community feels the subteam is adding enough value to grow)

**Advantages**

* Frees up core developer time from tedious but necessarily timely administrative tasks
* Provides a holistic approach to security for the Grin ecosystem
* Better prepares the ecosystem to be proactive and reactive to security emergencies
* Encourages a long term culture of security for the project
* Reduces liability for core team

**Risks**

* More cooks in the security kitchen (in some circumstances it can be more efficient and secure for a small core team to be solely responsible)
* Increased overhead of dedicated team members
* More complex than directly mailing a core developer in case of vulnerability
* Offsets trust of vulnerability disclosure from core devs directly to a protocol and potentially differently trusted community members (I think this is what lehnberg’s proposal is going for in general and is good, but for something like vuln disclosure for ecosystems like this it is critical to get right)
* Potentially redirects focus from other important areas (“if it ain’t broke…”)

**Future Work**
Provide formalized proposals for community consideration for:

* vulnerability disclosure process and protocol
* bug bounty program structure
* evaluation of existing security process
* subteam budget
* subteam responsibilities and roles assignments

**About Me**
I got involved with BTC in 2012 and was motivated by exploring new tools to preserve and protect digital rights. My first work in the space was contributing to the world’s first scrypt asics in 2013-2014. After that I contributed to various privacy preserving and AI/ML projects until 2017 when I co-founded a blockchain security solutions company. There I helped build the world’s first quantum resistant signature scheme deployed to a public blockchain mainnet and facilitated security audits and engagements for many projects ranging from pure crypto to legacy dinosaurs. In Dec’18-Jan’19 I was able to help facilitate a very quick audit of Grin’s crypto library and gave a short talk on it at grinconus.

Currently I am exploring new models for providing sustainability, accessibility and capability to privacy preserving projects. I feel that this is an interesting opportunity to apply my experience and ultimately make progress toward the end of ensuring future generations have the choice of privacy. My intention with this proposal is to improve the security culture for Grin and by extension improve the sustainability, accessibility and capability for all decentralized privacy preserving projects.

**Next Steps**
If there is initial interest, we could add a discussion point to the Governance meeting agenda for June 18. If this proposal gains further support I would complete the items in the future work section and iterate on them until the community is satisfied to build out the subteam. I would assume responsibility for this following the adoption path in the original proposal for at least 3 months as a contribution to the Grin ecosystem.

If the community finds that it does not make sense to have a dedicated security subteam my hope is that through the discovery process the existing process ends up more robust and transparent.

Thanks for reading and participating in Grin’s governance. I’m looking forward to answering questions and discussing Grin’s security culture.

---

### Post by @AlexGSG (2019-06-17)
*Post #8*

Grin is an amazing project, and there are amazing people here, without understatement, especially the Core Developers and early github Contributors.

There are very few such people, so I formulated my sentences to increase the participants. Common people need more motivation and that’s my proposals:

1. People who are willing to be motivated only by pure interest, involvement in the project for a goodwill to all humanity, are so rare. Even more rare those who are ready to do it full time. Project need to be upgraded by the motivations of Grin owning. And the Core Team and General Fund need to be leaders in this movement.

2. The project grows, new branches appear, donations come to the project, they will be even much more, when the donors see, that the funds are being spent very efficiently. While I do not see this, I am saying it frankly. I had an experience with charity programs, Grin need much more transparency in this case. Transparency and efficiency are the 2 key indicators, that can improve donations much higher.

3. The Grin Technocratic Council or Core Team, as perfectly noted in the proposal, should form the tasks and the long-term agenda. The Core Team also needs :

* To form tasks and assign rewards for them from receiving funds (donations, payments, etc.).
* The participants of the teams (there may be a lot of them) see the tasks and the proposed reward, the whole reward is only nominated in Grins, all funds in other currencies are transformed into Grin. In an auction format, groups offer their conditions for the implementation of tasks and deadlines. They put offers down from initial reward.
* Grin General Fund accepts proposals from teams for the implementation of tasks, upon implementation the members of General Fund collectively accept the work and send an award.
-.In this payment format, it is possible both project tasks and periodic payments to the Core Developers and teams. Also i think ,that the members of the Core Team and the Grin General Fund also must be rewarded.
-. Since the reward will be in Grin, and the majority of participants are confident in the success of Grin the cost of work in FIAT or Bitcoin will be higher than in Grin.

4. It is important that the Grin General Fund has an optimal number of participants, ideally 5 people, to minimize bureaucracy and represent the community.

5. Fund reports must be no less than 1 time per month, and preferably at each Grin General Fund meeting ideally all movements are publicly available online (in the same Google Doc for a start) everything should be very transparent and so not needed to wait a long time for reports and results. Online fund movements is perfect.

About me:
my name is Alex, I am from Russia, my skills - sales and promotion , lawyer, crypto and blockchain enthusiast. Now I’m doing as much as I can to promote Grin in the Russian-speaking crypto community - website, groups, increasing the population of Grinners.

---

### Post by @Yeastplume ⭐ (2019-06-24)
*Post #12*

I’ve collected all of the docs and outstanding questions into the [fledgling Grin RFC repository](https://github.com/mimblewimble/grin-rfcs) with draft RFCs filled out for all of the above governance and RFC process topics. Would appreciate if we could all move the discussion there to help hammer them home!

---

### Post by @lehnberg ⭐ (2019-07-11)
*Post #18*

Thanks [@DoctorStrange](/u/doctorstrange)!

DoctorStrange:

> Is the Wikipedia entry still required? I could make a start on that over the summer.

Yes, it most certainly is, see here: [Add Grin wikipedia entry · Issue #92 · mimblewimble/grin-pm · GitHub](https://github.com/mimblewimble/grin-pm/issues/92)

Feel free to take a stab, happy to help wherever I can!

---



## Binance Listing
*Date: 2019-06-18 | [Forum Link](https://forum.grin.mw/t/binance-listing/5258)*
*Importance Score: 95.5 | Core Participants: tromp, lehnberg*

### Post by @grinn (2019-06-18)
*Post #1*

Grin on Binance would be huge

Price, trading volume, etc etc

Binance already backs Grin

[Binance](https://www.binance.com/en/blog/334214072237174784/Binance-Labs-Fellow-Ironbelly-an-OpenSource-GrinMimbleWimble-Mobile-Wallet)

### [Binance Labs Fellow: Ironbelly, an Open-Source Grin/MimbleWimble Mobile Wallet...](https://www.binance.com/en/blog/334214072237174784/Binance-Labs-Fellow-Ironbelly-an-OpenSource-GrinMimbleWimble-Mobile-Wallet)

Today, Binance Labs is excited to announce our first grantee for the Binance Labs Fellowship.

[Binance](https://www.binance.com/en/blog/345540707021938688/Binance-Labs-Fellow-Hashmap-a-Grin-Core-Dev-with-Knockturn-Allee-a-Payment-Processor)

### [Binance Labs Fellow: Hashmap, a Grin Core Dev, with Knockturn Allee, a...](https://www.binance.com/en/blog/345540707021938688/Binance-Labs-Fellow-Hashmap-a-Grin-Core-Dev-with-Knockturn-Allee-a-Payment-Processor)

Today, Binance Labs would like to introduce our next Binance Fellow, Alexey Miroshkin (a.k.a. hashmap), and his project Knockturn Allee.

In last 24h CZ acknowledged a tweet about Grin on Binance

[twitter.com](https://twitter.com/cz_binance/status/1140854675735842816)

####  [ CZ Binance (cz_binance) ](https://twitter.com/cz_binance/status/1140854675735842816)

@ngocnv84 @binance For @Binance listing, please see: https://t.co/usiISCtuSj For @Binance_DEX listing, please see: https://t.co/b1ZRm9lCC4

[8:00 PM - 17 Jun 2019](https://twitter.com/cz_binance/status/1140854675735842816) 4

In listing he posted one of his tips is:

“We require the project founder or CEO to fill out the form. Why? If there ever is a bug with your wallet, a fork or double-spend in your blockchain, we need to talk to a key person.”

Has a core dev / lead from Grin applied for Binance listing?

<https://www.binance.com/userCenter/coinApply.html>

Grin now has momentum this would be very helpful

Cheers

---

### Post by @Grumpy (2019-07-14)
*Post #6*

Done.

[ Screen Shot 2019-07-14 at 3.31.15 AM.jpg2056×1278 266 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a55cd0bb187c6642abfed7d5b6b20d878f0829cf.jpeg "Screen Shot 2019-07-14 at 3.31.15 AM.jpg")

---

### Post by @Neo (2019-07-16)
*Post #13*

What more can we do? We don’t need to shill too hard, when we’re already the cool kid…

Binance labs are funding 2x Grin projects( Knockturnallee & Ironbelly). Plus they’ve now received our _formal_ application. What more could they need?

Coinbase must be well aware as well, since people from there are showing off Grin stickers: <https://twitter.com/brian_armstrong/status/1144653330901159937>

Apparently even people from Google have been ordering Grin stickers: <https://twitter.com/TMGOX/status/1146309686431498240>

One of the Gemini core devs has also written medium articles about Grin: <https://twitter.com/arvanaghi/status/1103298939430858753>

---

### Post by @Swizz_beatz (2019-07-25)
*Post #31*

Following the advice from the Grin council to work on this ourselves. I think we collectively as a community work on multiple avenues towards increasing Grin awareness and adoption

* Started to create some videos aimed at explaining Grin, it’s history, etc but think this would be done best as a community. I’ve got a lot of ideas and and looking forward to even more bright ideas from this vibrant community. In the meantime, I’ll continue to work on it, but you can expect it to be shown here before anywhere else
* Although listing is important and does play a role at increasing awareness, I feel it might be a bit too early and maybe we should work on making sure that information about grin is readily available and presented in an easy and interesting manner prior. This is only my opinion and what matters even way more is what approach the community will like to take in regards to this
* It’s all a bit chaotic at the moment but lets work together to get a marketing subdivison and adding some structure to make sense of this process and tackle it more efficiently.
* Some members of the community have already started making ‘noise’ and spreading the word of Grin via Twitter/various social channels. Keep up the good work

P.S If anyone would like to take part in the video discussions/audio making for videos/posters/etc please don’t hesitate to let us know.

**I am Ignotus**

---

### Post by @lehnberg ⭐ (2019-07-26)
*Post #35*

[@grinn](/u/grinn) [@Yawser](/u/yawser) to propose a discussion item for a governance meeting, leave a comment on [the relevant GitHub issue](https://github.com/mimblewimble/grin-pm/issues/165).

---

### Post by @grinn (2019-08-01)
*Post #49*

thx for follow up! i actually just posted:

i would be interested in funding a grin ledger app - agree the difficulty seems in finding the right talent who isn’t already working on something else that’s more important

and i didn’t realize binance dex had encouraged us to list - has anyone applied, does anyone have an active application, etc

i am happy to pay the required BNB too

there are 42 questions here - <https://community.binance.org/topic/18/guidelines-on-how-to-list-your-token-on-binance-dex>

also there are questions on main binance app - can we work on these as a community in a public doc

does anyone have anything from other exchange apps? we should centralize all this biz dev / mkting info

---

### Post by @Swizz_beatz (2019-08-03)
*Post #69*

Thanks for admitting that you were simply speculating and lacked any objectivity to back up your claims.

They listed bitcoin because bitcoin is the first and biggest cryptocurrency. It would be crazy for any exchange to try to even consider starting an exchange without having bitcoin. Listing bitcoin works in their own interests. Without bitcoin, any exchange is automatically worthless and can’t even dream of competing. This does not apply to Grin at present. Should an exchange list or not list Grin does not affect it’s viability at all.

Also, don’t compare Grin to bitcoin. Bitcoin is on a different planet. It is proven, established and so known that it has always been the undisputed King of everything crypto-related and leads ****every** single alt coin (Grin included) in existence**. It also has a community and awareness to match.

Bitcoin vs Grin comparisons:

* Grin’s market share represents 1/3200th (0.03125%) of Bitcoin’s market share.
* Grin’s current hashrate is 6.60 Mgps vs Bitcoins 45,867,201,622 GH/s.

If you want Grin to look insignificant and worthless, keep comparing it to bitcoin. You’ll get a healthy dose of reality regardless of whichever metric you use.

---

### Post by @tromp ⭐ (2019-08-03)
*Post #70*

Swizz_beatz:

> Grin’s current hashrate is 6.60 Mgps vs Bitcoins 45,867,201,622 GH/s.

A graph is not comparable to a hash. At all…

---



## Yo Dawg, I heard you like CoinJoins
*Date: 2019-06-22 | [Forum Link](https://forum.grin.mw/t/yo-dawg-i-heard-you-like-coinjoins/5296)*
*Importance Score: 101.9 | Core Participants: david, jaspervdm, lehnberg*

### Post by @david ⭐ (2019-06-22)
*Post #1*

I will be releasing the code in a week or so for a service I will be hosting to help further obscure transaction graphs. The code will be available here once it’s ready: <https://github.com/DavidBurkett/GrinJoin>. In the meantime, I was hoping to get everyone’s thoughts on the idea, and see if anyone has any interest in helping out, or ideas for improvement. Thanks in advance!

# GrinJoin

A CoinJoin service for Grin

### Background

In 2013, Greg Maxwell proposed[1] the CoinJoin protocol as a way of anonymizing transactions. CoinJoin is a way of combining the inputs and outputs from multiple transactions into a single transaction. Doing such erased the original transaction boundaries, making it infeasible for blockchain analysts to determine which outputs spent which inputs.

Three years later, the original Mimblewimble protocol was outlined[2] by the pseudonymous Tom Elvis Jedusor. This combined CoinJoin with Confidential Transactions to make a non-interactive protocol for performing CoinJoins, which became the basis for the Grin cryptocurrency.

In Grin, every block is simply a CoinJoin of all of the other transactions in the block, resulting in one big transaction. This gives Grin an enormous privacy advantage over bitcoin, breaking transaction linkability! _In theory_ .

### Problem

There are a few problems though. Privacy is only gained if there are other transactions to join yours with. Since Grin is still new, there are only a few transactions per minute on average, meaning there aren’t very many other transactions to mix yours with. To make matters worse, anyone running a node that wants to monitor the transaction pool can see nearly all of the individual transactions before they’ve been combined in a block. So much for unlinkability!

### Proposed Soution

As usage grows, these issues become less of a problem. In the meantime, there are ways to make the situation significantly better for those who are willing to wait a few blocks before including their transactions. By introducing a _trust-minimized_ central server (or group of servers), transactions can be collected and combined for a period of time before ever being broadcast to the network and included in a block. Now only the central server knows which inputs and outputs belong to you!

But now this central service knows which node a transaction came from. How can we solve this problem? The same way we solve it for Grin transactions: Dandelion (and later, i2p). By introducing a new tx pool similar to Dandelion’s stempool, let’s call it the JoinPool, we can route our transactions through other nodes at random, obscuring their origin. Rather than “fluffing”/broadcasting a transaction after X hops (on average), the transactions in the JoinPool can instead be sent to the CoinJoin server to be joined with other transactions.

So now only the central server knows which outputs spend which inputs, but has no idea where that transaction came from. If we wanted, we could even setup a heirarchy of servers, so there’s not a single server that knows all of the original transactions. Each node could choose either a specific trusted server or a random one to send their transactions to. These secondary servers can aggregate transactions as they receive them, and after aggregating “enough” transactions, then send the final, joined transaction to the primary CoinJoin server to be joined with the aggregate transactions from the other secondary services.

### Roadmap

1. Finish implementing support for a primary “GrinJoin” server, and start hosting it. Interested parties can manually submit transactions to be included in the next GrinJoin transaction to test the service. I will initially log transaction info for debugging purposes, so at this stage, assume I could compromise your privacy if I wanted to.
2. Implement a JoinPool in Grin++ to obscure the origin of each transaction. Transactions that choose to use this new CoinJoin feature will eventually make their way to the GrinJoin server. I will remove all logging once everything is stable.
3. Add support to GrinJoin for running a ‘secondary’ server, and add the ability to Grin++ to choose which server to submit your transactions to.

[1] <https://bitcointalk.org/index.php?topic=279249>
[2] <https://download.wpsoftware.net/bitcoin/wizardry/mimblewimble.txt>

---

### Post by @david ⭐ (2019-07-23)
*Post #16*

[@rodarmor](/u/rodarmor) When I first read that proposal, I misread it terribly, and so quickly brushed it off as deeply flawed. Upon re-reading, I realized what you were saying, and it’s actually very similar to what I was planning on doing anyway, with a few key improvements. The only changes I would suggest is we

1. Use IP address instead of creating a new nodeId concept
2. use the receipt of a new block as the expiration of the patience timer. I apologize for brushing this off before.
3. Instead of just waiting for the tx to get to a fluff peer, which may never happen anyway due to cycles, just use probability as before, except instead of fluffing, make one additional hop to one of the fluff peers.

---

### Post by @david ⭐ (2019-12-01)
*Post #19*

I announced in a few other places already, but <https://grinscan.net/block/456188> contains the first ever “GrinJoined” transactions. 9 different transactions were sent via TOR to a GrinJoin server (grinjoin5pzzisnne3naxx4w2knwxsyamqmzfnzywnzdk7ra766u7vid.onion), and were joined together before ever being seen by the p2p network.

---

### Post by @david ⭐ (2019-12-01)
*Post #23*

The upcoming Grin++ release (was supposed to be this weekend, but I’m delaying again) will be as simple as:

For all other wallets, the API is super simple. Just make a JSON-RPC request via TOR to `grinjoin5pzzisnne3naxx4w2knwxsyamqmzfnzywnzdk7ra766u7vid.onion/v1` with a method of `submit_tx` and the `params` field simply needs to contain a field called `tx` which contains the JSON serialization of the transaction.

---

### Post by @lehnberg ⭐ (2019-12-03)
*Post #33*

shush:

> Step 4: Concurrent to step 3, the participant receives private keys from each other participant.

[@shush](/u/shush) thanks for sharing, I’ve been thinking along the same lines myself, but am not knowledgeable enough.  One of the problems I’ve encountered, is that by sharing private keys (or “ways to unblind”) with other participants, these participants would be able to also decrypt the original message (the unaggregated transaction), wouldn’t they?

In my thinking so far, I’ve seen a lot of similarities between this problem and the [Mental Poker](https://en.wikipedia.org/wiki/Mental_poker) problem, and the various decentralised shuffling protocols that’s come out of this, where an output/kernel would be the equivalent of a card to be shuffled. A big difference being that the exact deck of cards is not known to the participants in advance.

Virtue poker’s description of [how they do the shuffle at the poker table](https://virtue.poker/howitworks) seems relevant and interesting here.

Ignoring the DoS risk, tx validation, and other separate problems, if the main objective is to join inputs, outputs, and kernels in a way where the central party cannot trace the unjoined transaction back to a particular user, imagine a protocol where:

1. Each input, output, and kernel, are equivalent to cards in three distinct decks (blue, red, green cardbacks), and a “player” is a user, and the GrinJoin server is the “dealer”.

2. Each player first encrypts their own transaction(s) accordingly, hiding the true value of each card, and is equivalent of putting a “lock” on the cards.

3. There is a protocol where players share the encrypted cards with each other, each player put its own locks on all of the cards, and shuffle them. At the end of this, nobody will know the true order of the deck.

4. The GrinJoin server receives all the cards, does a shuffle, and puts their own lock on the cards.

5. Similar to 3, the cards are now shared sequentially amongst the players, but now the players _remove_ their own individual locks. Still, the last player receiving the cafrds cannot see their face value, as they still have the lock of the GrinJoin server.

6. Finally, the last player sends the cards to the GrinJoin server, who can remove its own final lock and now has a verifiably shuffled deck without knowing which input/ouput/kernel are associated.

I don’t know if any of this makes sense, and it’s probably needlessly complicated. But each player would only need to trust themselves to shuffle the deck correctly in order for the outputs to be mixed.

---

### Post by @david ⭐ (2019-12-03)
*Post #34*

This is definitely an approach we could take. This protocol, although rather complex, actually works as is. But as mentioned, there’s no DoS protection. Since we’re not able to validate until the end, and since we can’t identify the culprit if it does fail to verify, it’s really easy to DoS (intentionally and unintentionally), and there’s no obvious path forward if validation does fail.

I’ll see if I can work some DoS protection into this scheme, but I’m not actually confident that it’s a problem that can be solved.

---

### Post by @lehnberg ⭐ (2019-12-03)
*Post #35*

So I’m not sure _how_ to do this the proper way.  It’s not clear to me how Virtue poker does it. Iddo Bentov (their advisor) has published many mental poker papers, they make some reference to commutative encryption but I’m not sure what/how they do it, and whether it’s even [secure](https://crypto.stackexchange.com/questions/6573/are-there-any-secure-commutative-ciphers).

The idea has _many_ weaknesses as is right now:

* DoS (flooding of invalid transactions)
* Honest or dishonest disconnects / protocol abortions (which we at least can identify)
* Tx validation
* …and the protocol itself leaks info, as Player 2 knows the structure of Player 1’s transaction (how many inputs, how many outputs etc) by counting the cards. Even though I’m sure this can be mitigated/designed away.

Whilst it is tempting to try to fix these problems straight away, I’d be curious to understand if we’re even able possible to get this dumbed down version to work. As I’m not fully convinced we can. And then _if_ it works, we could then try to tackle the other problems. If we can’t get it to work naively, the others problems won’t matter.

Re the validation of transactions, I wonder if there’s some zk construction that would allow us to prove that:

1. a transaction’s equation is valid;
2. that the inputs are in the UTXO set;
3. that these particular commitments are the ones that are in the “deck of cards” that PlayerX encrypted and passed on;

… _without_ revealing anything about the actual commitments or kernels themselves. But again, don’t know enough about zero knowledge protocols.

---

### Post by @david ⭐ (2019-12-03)
*Post #37*

lehnberg:

> Whilst it is tempting to try to fix these problems straight away, I’d be curious to understand if we’re even able possible to get this dumbed down version to work.

So if we’re willing to look past DoS protection, I think I can dumb this down quite a bit (at least, in my mind it’s simpler to reason about), by removing all of these locks altogether.

1. Everyone connects to the tumbler, and uploads their kernel.
2. The tumbler gives each of them a next person to talk to, and identifies 1 of them as the first node in a ring.
3. The first node generates a random blinding factor _R_ , and adds it to that user’s transaction offset, and then passes the result to the next node.
4. Each node adds their transaction offset, and passes it to the next node until the last node, which adds their transaction offset, and passes it back to the first node.
5. The first node subtracts the blinding factor _R_ , and now has the sum of all transaction offsets, which is given to the tumbler.
6. Every node opens a new circuit to the tumbler for each input and each output in their transaction (using random timers to prevent linking) and then uploads their inputs/outputs to the CJ server.

I’m fairly certain this design provides all the same security/privacy guarantees as your protocol, while removing the need to use locks, and eliminates any leaking about tx structure. It also provides a little bit of resilience against unintentional disconnects, because if the next node in the ring isn’t reachable, their kernel can be thrown away without having to start over.

I didn’t base this off of any existing protocol, just a random thought I got a few minutes ago, so it very well could have a blatantly obvious fatal flaw

---


