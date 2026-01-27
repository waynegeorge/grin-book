# Chapter 7: The Hard Fork Years

*25 topics selected for this chapter*

---

## Yeastplume - Progress update thread - Jan to March 2020
*Date: 2020-01-10 | [Forum Link](https://forum.grin.mw/t/yeastplume-progress-update-thread-jan-to-march-2020/6878)*
*Importance Score: 76.3 | Core Participants: yeastplume*

### Post by @Yeastplume ⭐ (2020-01-10)
*Post #1*

Update Jan 10th, 2020

And another new update thread… when this funding period is done I will have been working on Grin full-time for 2 years, and nearing 3 years total working on the project. Time is supposedly nice and linear like Grin emission, but there seems to be less of it every year… like Bitcoin’s emission… I’m sure there a clever tweet here somewhere that I can blast out all self-satisifed like once it’s properly composed.

But that’s not what I’m paid for… So I eased back into the swing of things with [our v3.0.0 launch](https://forum.grin.mw/t/grin-grin-wallet-3-0-0-released) which thus far appears to be going well. The real reckoning point is around the hardfork block, but the floonet swapover went well so fingers crossed that will be a simple repeat performance for Mainnet.

This past week has mostly been about tending to [<https://github.com/mimblewimble/grin-wallet/pull/289>](payment proof export and validation), something which needed a bit of time to do properly so I wasn’t quite able to get it in before the pre 3.0.0 code-freeze and holidays, so that’ll be a 3.1.0 feature.

We’ll be looking into our roadmap + features for upcoming releases over the next few weeks, but here’s what I have right now off the top of my head as what the next few weeks should look like

* Adding an interactive CLI mode to the wallet, which will help catching issues with the API as well as hopefully finally turn the reference wallet itself into something a bit more usable (for those command-line loving types). I hope it’s common knowledge that the focus has always been on enabling upstream developers via the API rather providing a shiny out-of-the-box experience, but it will be of great help for further API development and testing to have a command line mode where the wallet is ‘running in the background’ (like what the API expects) instead of executing a single command and exiting.

* Better documentation on how to use the API, and particularly sample (node) code on how to init and call the secure API in advance of removing the non-secure owner API in 4.0.0.

* Testing strategy for both the node and wallet… all of our automated integration testing badly needs restructuring and rework, so I think this should become a priority for the entire dev team for early 2020.

* Possible SQL wallet backend to support the needs of larger institutional users.

* And on a more ‘roadmappy’ note, I would very much hope that by the end of this year we have collectively decided on and performed some implementation toward a standard for how to send offline transactions, building on the TOR support discussed and implemented last year.

And that is by no means definitive… there are plenty of potential roadmap issues to discuss, and as-per usual plenty will come up as we go along.

Looking forward to the coming year’s work. Grin is markedly better than it was one year ago, and I fully intend to be saying something similar around this time next year.

---

### Post by @Yeastplume ⭐ (2020-01-17)
*Post #2*

Update Friday, Jan 17th, 2020

‘Boring and uneventful.’ Terrible review for your new Netflix series, but the highest praise you could possibly receive for your Hardfork, so well done all there!

I’ve been bashing away at smaller bugfixes and minor issues over the week, and it looks like we might be going for a small [3.0.1 wallet update](https://github.com/mimblewimble/grin-wallet/releases/tag/v3.0.1-beta.1) fairly soon… nothing major and you only need to update if you’re one of those affected by the issues in the listed bugs.

I’ve also got work underway on a larger piece [the cli-wallet mode](https://github.com/mimblewimble/grin-wallet/pull/295). A bit of refactoring needed there to make sure the interactive mode works identically to a 3rd party application, followed by a tiny bit of glue to call all of the existing commands in the context of a command-line, followed by tons and tons of small fiddly things to ensure absolutely all of the commands work correctly and return errors where and when they should.

This process is basically putting together a minimal sample client application for the wallet APIs. It will be a bit of a slow process going through all the commands one-by-one and ensuring they all behave correctly in the command-line, but the payoff here is that each little fix to an error message here and the expected API flow there is another small improvement for all upstream 3rd party wallets.

Thinking a little bit about 3.1.0 features, I think the payment proof export and round 1 of the CLI mode should be more or less it… there was one other thing that came up but it’s not coming to mind, will fill it in later when I remember. However, there’s no longer a real need to keep the node and wallet release schedules in perfect sync, so I hope we’ll be able to achieve slightly shorter release cycles, particularly for non-breaking quality of life additions.

That’s all for now, enjoy V3 Grinning!

---

### Post by @Yeastplume ⭐ (2020-01-24)
*Post #3*

Update Friday, January 25th, 2020

Lots of background work this week, a bit of refactoring, some triaging and organizing outstanding issues, and a few interesting discussions in node dev that always require me to stop and burn out some brain cells thinking about them. Plenty done, but nothing hugely exciting from an outside perspective. Highlights are:

* I’ve put together the [list of new features and fixes](https://github.com/mimblewimble/grin-wallet/milestone/7) for the 3.1.0 release of the wallet, aiming for the end of March as a release. TLDR: CLI Mode, Payment proof export/verification, V3 Node API and various other fixes and QOL Changes. If you think something else should be included as a matter of priority, please drop into the wallet dev channel.
* And dev work this week was mostly focused on one or more of these issues. In particlular, [finished, tested and merged the payment proof functionality](https://github.com/mimblewimble/grin-wallet/pull/289), then some [refactoring and cleanup](https://github.com/mimblewimble/grin-wallet/pull/309) in another PR, also ensuring that onion v3 addresses are used consistently throughout. Also a bit of progress on [CLI Mode](https://github.com/mimblewimble/grin-wallet/pull/295)

And that’s all, expecting the next couple of weeks to look more or less like this one to get 3.1.0 together, then most likely thinking about some more serious work with larger roadmap items.

Keep enjoying the general post-holiday absence of distractions. I know I do!

---

### Post by @Yeastplume ⭐ (2020-01-31)
*Post #4*

Update Friday, January 31st 2020,

As expected, this week looked much like the last, mostly working through the list of bugs and issues for the 3.1.0 release. In no particular order:

* [Reworking directory setups at launch](https://github.com/mimblewimble/grin-wallet/pull/318) quite a bit of rework and testing here to sort out directories at wallet startup. Should resolve several issues with paths and log files appearing where they shouldn’t.
* [Several](https://github.com/mimblewimble/grin-wallet/pull/319) other [bugfixes](https://github.com/mimblewimble/grin-wallet/pull/319) on the list
* More work on the CLI mode, particularly trying to get status messages to appear via the prompt and fixing a few commands

Also preparing a new Governance RFC which should be ready for initial PR next week, as well as starting to turn my attention to some documentation, particularly updating the wallet guide and a long-awaited primer on how to invoke the wallet’s V3 API! More to come next week.

---

### Post by @Yeastplume ⭐ (2020-02-07)
*Post #5*

Update Friday, Feb 07th, 2020:

And once again, relatively quiet on the front but loads of things done in the background. Some quick highlights:

* Biggest wallet news of the week is that the the long talked-about [cli mode](https://github.com/mimblewimble/grin-wallet/pull/295) has finally been merged into master, ready for testing and community feedback. Note that cli mode is still very much experimental, still a bit jankesque and not 100% ready for prime time (whatever that means,). However, it doesn’t affect any existing functionality as is very much a standalone feature-add, so there’s no harm getting it in early, letting people play with it, and refining over time. If you feel like building from master go ahead and play with it, otherwise there should be a beta 3.1.0 release in a week or so.

* Several other feature adds and bug fixes knocked off the [3.1.0 milestone list](https://github.com/mimblewimble/grin-wallet/milestone/7), I won’t go into each one in detail, feel free to browse.

* Also spent a good amount of time updating the wiki’s [Wallet User Guide](https://github.com/mimblewimble/docs/wiki/Wallet-User-Guide) to reflect 3.1.0 (with a bit of advance 3.1.0 thrown in). It had fallen badly out of date and several users had pointed out that it needed an overhaul.

* And finally, a new WIP [RFC on General Fund Spending Guidelines](https://github.com/mimblewimble/grin-rfcs/pull/41). I thought it might be a good idea to get an RFC together that clarifies how the general fund is spent. I’m sure this will spark plenty of discussion (please don’t make anyone tell anyone to keep it civil,) so will reserve further thoughts to that RFC and thread.

So that’s it for now, next week I’m going to get [the last large item for 3.1.0](https://github.com/mimblewimble/grin-wallet/issues/305) out of the way, address the other two outstanding issues one way or another, then hopefully have a 3.1.0 beta ready by the end of it. Hope it keeps the excitement going during this inter-fork period.

Have a weekend.

---

### Post by @Yeastplume ⭐ (2020-03-06)
*Post #8*

Update Friday, March 6, 2020

Onwards and upwards to 4.0.0 changes and features! Or perhaps sideways, around in circles and off in a random direction. Time will tell.

Particularly eventful and productive [development meeting earlier in the week](https://github.com/mimblewimble/grin-pm/issues/256) where we started to identify some v4.0.0 features. [We’ll be filling the list in any day now](https://github.com/mimblewimble/grin-pm/issues/248) … ahem. Much discussion on our post 5.0.0 forking strategy/consensus mechanisms and other interesting topics with as many opinions are the are people in the discussion. Good to see such a thriving level of involvement, and exciting times ahead.

So in my own personal sphere, The theme was very much 4.0.0, and a lot of mechanical work to support some of the features we’ve been discussing. In particular, a ‘slate-lite’ mode kicked off by [this issue](https://github.com/mimblewimble/grin-wallet/issues/317), that will enable the first leg of the any transaction to be significantly reduced in size and the data it presents to the other party. This is a decent privacy enhancement, and leads to some interesting possibilities like the ability to insert QR codes in the transaction workflow or serve up the initial slate as a relatively small string for cutting and pasting somewhere. (whether you’d want to is another story, and if you have an opinion I’d encourage you to join the chat in the wallet-dev channel)

And a bit more specifically in terms of PRs to support all this:

* [Removing the V2 Owner API](https://github.com/mimblewimble/grin-wallet/pull/351) bye bye insecure API. If you’re a wallet developer please pay attention to this, as you will now need to use the secure owner API exclusively. I’ve added a small [sample node project](https://github.com/mimblewimble/grin-wallet/tree/master/doc/samples/v3_api_node) in the repository that demonstrates how to do this.

* [Adding a V4 Slate](https://github.com/mimblewimble/grin-wallet/pull/354), that looks exactly like the V3 Slate so far, but at least we all of the versioning and upgrade code to support a seamless transition around HF time is in place.

* And as the first part of the work to Lite Slates (Slatelets?) [Make the transaction element in a Slate optional](https://github.com/mimblewimble/grin-wallet/pull/356) which turned out a bit rabbit-holey but I think it’s there and doing its job without changing anything from an external perspective. Once this is in place the next step is to start experimenting with sending excess sums instead of a list of inputs and outputs.

And quite a lot of reviews and thinking about outstanding PRs, RFCs and concepts that have been making the rounds, trying to get myself at least somewhat informed about all of the ideas and development threads that are going on (which can hurt my limited brain sometimes, bear with me).

Right, that’s all for now. Remain calm and have a decent weekend.

---

### Post by @Yeastplume ⭐ (2020-03-20)
*Post #9*

Update Friday, March 20th 2020

World has gone slightly mad since my last update, and with a Yeastlair full of 7 people with varying degrees of neediness, some challenges have been thrown into my usual routines. However, these issues are hardly unique to me at present so I won’t dwell on them.

[4.0.0](https://github.com/mimblewimble/grin-pm/issues/248) Release planning is firming up, and most of my time right now is taken up with still-experimental work of [‘compacting’ the Slate](https://github.com/mimblewimble/grin-wallet/pull/366), the idea being that we keep the first leg of a slate journey very minimal to allow for a greater wealth of transaction initiation options. There will be an RFC introduced shortly to go alongside this PR, and the hope is that the V4 Slate will be as compact as possibly, ready for the rigors of a possible post scheduled Hardfork world.

With the existing work that’s already gone into the 4.0.0, and the potential changes to [allow duplicate outputs](https://github.com/mimblewimble/grin/issues/3271), there should be plenty to do and test for 4.0.0. Needless to say there’s plenty to keep me out of trouble in the interim.

Going to keep it short for now. You most probably have greater worries at the moment than the state of a particular crypto-currency, but rest assured myself and everyone on the Grin team plan to keep plugging away as best we can.

Remain strong and sensible, get your news from reliable sources, stay safe.

---

### Post by @Yeastplume ⭐ (2020-03-30)
*Post #10*

Update Monday, March 30th, 2020

The [hybrid tx building RFC](https://github.com/mimblewimble/grin-rfcs/pull/46) is a hotbed of activity, and while I haven’t yet fully formed opinions on what transaction flows we should be advocating, I do know that ensuring the slate is as minimal as possible will enable options that we may not currently have. My focus continues to be on the [experimental slate reduction PR](https://github.com/mimblewimble/grin-wallet/pull/366).

Last week was very rabbit-holey in service of this PR, and involved a trip back to our secp-256k1 fork to implement [a Pubkey to Commit function](https://github.com/mimblewimble/secp256k1-zkp/pull/54), the absence of which was making a particular piece of code that calculates and stores the excess for either part very awkward. It’s been a good while since anyone made any changes to that repo, so also took a bit of time there to perform some maintenance, cleaning up warnings, the build (thanks [@quentinlesceller](/u/quentinlesceller),) etc…

Then a [similar round on rust-secp256k1](https://github.com/mimblewimble/rust-secp256k1-zkp/pull/64), and the rest of the week was spent integrating changes into the slate-reduction PR and continuing to reduce, and I’m happy with progress there so far. The current state of the minimised slate is even more reduced than what’s currently in the comments, and I’ll be updating the PR with details of changes and progress later in the week. There are still a few more obvious reductions that can be done, and I’d like to get them all in first so as the tx-building PR can be fully informed.

So that’s it for my work update. These are very harrowing times, people’s nerves are likely to be frayed for reasons far more important than Grin. People aren’t at their best, and that’s okay and perfectly understandable. Though my actions are far from perfect, I’d still like to make a little appeal to everyone to at least try to make an extra effort to apply a little bit more civility and understanding then they otherwise might. Everyone’s sanity depends on it.

---



## Let's talk about the elephant in the room
*Date: 2020-03-23 | [Forum Link](https://forum.grin.mw/t/lets-talk-about-the-elephant-in-the-room/7169)*
*Importance Score: 127.1 | Core Participants: david, tromp, davidtavarez, lehnberg*

### Post by @TheNewGrin (2020-03-23)
*Post #1*

Let’s talk about the elephant in the room.

Bottomline is: Grin is an exciting project with fascinating tech that might fail to gain traction and become one of many dead ends in the cryptocurrencies world. What can be done about this?

Some of the stuff below might sound harsh, but I guess that is not the time for sugercoating.

I think we all might be biased here. This might soud harsh, but the project is going nowhere in terms of wider interest (not to mention the price). Yeah, the concept was fun and many people were passionate to deliver something really good, but even the best intentions might not allign with what market prefers. It is still profitable enough to mine but with lack of interest the future is not bright. Big exchanges do not want to list it (and those who listed us seem to no longer care about it, look at Bittrex, where the wallets are off), new people are not coming to the community, ASIC producers scrapped their ASIC plans, people are still mining, because it is still profitable and devs are still developing, because they are getting like 10k USD per month (or whatever the money is now), so it makes sense for them to sit on this for as long as possible, but there is nothing that could bring people to Grin. When they are looking for anonimity they are picking Monero, when they want simple coin they go with BTC, and when they want smart contracrs they pick ETH. When they want experiment they pick the flavour of the month - and yeah Grin was flavour of the month last year in February, when prices were rallying and everyone were listing us, but it seems like dead end now. We all might be biased in believing otherwise since our bags might be heavy or we might be passionate about the tech, but all the positive and negative biases aside, anyone could think of 3 reasons why things could change in the near future? I mean, why suddenly people should get interested in Grin in the timeframe of following months?

I don’t think that’s something one person or small group of people could change. Perhaps this is question of finding the answer to the question WHY people should chose Grin. Yeah, scalability and anonimity are cool, but the first one is not that visible yet and second is achieved on smiliar level with projects like Monero or Zcash. Yeah, we can discuss that Grin has fairer distribution etc., so long term this is advantage, but when people do not care about the project advantages like this are irrelevant. Perhaps something that boosts adoption would make people realise, that we are not much worse than Monero, Zcash and on some levels can be even better.

If I had answer or even remotely valuable ideas I would bring them to the table.  Well, of course listings on mayor exchanges are something that always boosts interests, even if some people jump in only because of the listing, not caring if it is a shitcoin or valuable project, it always brings visibility and that would make all kinds of people involved in the community.

Second thing is easier onramping. Yeah, things that are done with projects like Grin++ are impressive, we understand that, but for new people it is much easier to onboard on Beam than on Grin (for the reasons that we know), so perhaps making onboarding easier would be second step, but listing, listings and listings are the most important thing right now. But we won’t have the listings without easy tools for people to handle their coins, so I guess both those things should happen.

Some of those plenty of BTCs that are being held by the council should be used for listings, because it brings visitibility to the project. Easiest way to bring visisbility. It is not a shame to ask for paid listing. Yeah, we might have gotten spoiled by free listings by Poloniex, Bittrex etc. in the early days of the project, but it is because back the Grin was flavour of the month.

Also, finding and enforcing standarized tx methos would be a milestone here. To summarise, we need listings (even if they cost us money) and easy GUI wallets with standarized tx methods. Perhaps you have other ideas, feel free to share them, but one thing seems almost sure - despite many technical improvements happening all the time, the project as a whole is heading downhill and we need smart person to figure out what can be done about it and implement that idea.

---

### Post by @tromp ⭐ (2020-03-23)
*Post #2*

TheNewGrin:

> Also, finding and enforcing standarized tx methos would be a milestone here.

Come join us in grincoin.teams.wallet_dev on keybase where this is being actively discussed.

---

### Post by @david ⭐ (2020-03-24)
*Post #15*

Markss:

> so grin plus plus is giving me error connecting to tor on my windows 10 and i can not get any address to send coins from poloniex. so i am stuck with my coins on poloniex like most people are.

Sorry you’re having this experience. Indeed, Grin can be quite a challenge to use, but it’s slowly getting better. If you ever want to figure out why you’re getting those connection issues, I’m always around to help at [Telegram: Contact @grinpp](https://t.me/grinpp)

---

### Post by @david ⭐ (2020-03-24)
*Post #17*

Markss:

> maybe you could share some link in the wallet itself if people need to download something additionally?

You shouldn’t need to download anything, but if you’ve used the tor browser before, you may have to delete `%userprofile%/tor/` before opening the wallet, since a user recently found that it can conflict with the tor version used in Grin++.

---

### Post by @lehnberg ⭐ (2020-03-27)
*Post #50*

Interesting discussion, I like elephants . Wanted to add a couple of things, opinions are my own, my filters are turned off, here we go:

### 1

In case you missed it, I referenced this thread in Tuesday’s governance meeting: [grin-pm/notes/20200324-meeting-governance.md at master · mimblewimble/grin-pm · GitHub](https://github.com/mimblewimble/grin-pm/blob/master/notes/20200324-meeting-governance.md#66-teams:)

> I just wanted to point out that suggestions and ideas like these are welcomed. There’s a dormant @grincoin.teams.community. If people have ideas for a fund or ambassador program, put it in an RFC, write a budget and a funding request, and let’s discuss in detail. Your chances for funding being approved will improve if you are not completely new around here and if you have some kind of positive track record of contributions to the project.
>
> If you’re new and still want to propose something, you might also want to start making contributions and get to know others here. That’s how it worked for all of us.

### 2

Generally speaking, any proposal that’s well argued, shows reason, follows logic, is full circled and is argued in good faith, seeking to discover some constructive improvement rather than trying to be right for the sake of being right or for the sake of inflating your own ego, I think will be at least **considered**. Even if people may not agree or draw the same conclusions as you. So if you have something to propose, nobody is stopping you. And there’s no shame in trying and failing!

### 3

The general fund being detached from Grin price fluctuation I think is a feature, not a bug. Especially given the emission rate the first years of mainnet, it would have been very difficult to fight the tide of the percentual increases to the supply.  Look around at other projects, living and dying with the price of their coin. You end up being very short sighted, doing what you can right now to move the price, rather than focusing on stuff that makes sense in the longer term.

### 4

If you think devs are being “insanely” overpaid, get involved when they ask for money. Make a convincing case for why they are asking for too much. Deduct operating costs, taxes, health insurance, pension contributions, etc and present your case for what a fair rate is instead. Keep in mind that each individual submits their own request. In fact, there was one funding request that launched today, so here’s your chance! [Request for funding / Antioch / Apr-Jun 2020](https://forum.grin.mw/t/request-for-funding-antioch-apr-jun-2020/7183)

### 5

So far, people who’ve been funded are Ignotus, Yeastplume, Jasper, and myself. They were all contributing without compensation for a long time (years) before asking for money (not sure about yeastplume). Antioch who’s now asking for money (see previous point) submitted their first PR to Grin in 2017. And me, I’m not sure but I think I was contributing 9-10 months before making my initial request. I’m sorry to disappoint but - none of us joined the project in order to get rich quick.

### 6

In fact, we never expected to receive such a windfall in the fund in the first place. We set up a mu-sig wallet, and we received very generous donations to it. It was unexpected, but it was most certainly welcomed. The large donor(s) understood who had control of the funds. “Keep doing what you’re doing” was the message. I for one intend to do just that, advocating for spending in the way I think best helps the protocol over the long term.

### 7

At some point though, the funding will run out, and donations will dry up. It’s okay. The project was literally broke and launched one of the most anticipated blockchains with $0 spent on protocol development. (Aside from three or so yeast funding rounds that he managed himself.) Unlike other projects, I think Grin will do just fine without any funding, we never even expected to have funding in the first place. This makes us resilient. I can think of many reasons why I would decide to leave the project, but running out of money is not one of those.

### 8

Even if you’re not a dev, and don’t have a brilliant idea you want to ask for money for, we can still use your help. We’re looking for community managers / moderators, testers, technical writers, wiki wizards, and individuals with good vibes in general that are excited about the tech and the promise of Grin. Hit me up if you want to toss ideas, my DMs are open.

### 9

If you’re not a dev, don’t have idea for how to spend money, don’t want to contribute, and don’t have any good vibes to offer either… Bummer. Make sure you stick around in any case, you might get inspired at some point in the future!

### 10

But! If you find that this is all _quite_ the bullshit, that the “true spirit of grin” has been hijacked by some centralized, virtue-signalling assholes that are buying themselves golden slippers and diamond rings (it’s all about that bling bling baby ) and you feel something ought to be done about this… then please do so! What is the core team anyways?

It’s some people with:

* commit rights to the github repo
* mu-sig access to a bitcoin wallet
* admin rights on a discourse forum
* admin rights on a keybase group
* (We don’t own the domain grin.mw, it’s been kindly lent to us from 0xb100d)

Really, how hard is that to replicate? Grab a few likeminded buddies, fork the repo, setup your own forum and keybase group, and there you go! Throw in a donation btc/grin wallet for good measure and you’re off to the races. Call yourselves Grin PRO, Grin X or whatever you like. If you follow the consensus rules, your node will be treated just like any node on the network. And we’d be happy to have you. The more the merrier. You’ll be running your own show, king of your castle, master of your domain, and can do whatever you like.

Note that this is NOT me telling you to “fork off”, on the contrary I’d like you to stay. This is me telling you that you DO NOT have to accept our governance model if you don’t want to. Participation is voluntary.

### 11

Finally, I just want to close with saying that we never expected to find ourselves a few months after mainnet having launched without Igno. Core team members were all looking to Igno for leadership, and he disappeared way too early. We’re definitely not perfect, and none of us are close to having the leadership qualities that Igno had. We’re doing our best, trying to learn from mistakes, and are hoping to improve over time.

* * *

Thanks for reading all the way, keep on keeping on in these times!

---

### Post by @david ⭐ (2020-03-28)
*Post #53*

lehnberg:

> If you follow the consensus rules, your node will be treated just like any node on the network. And we’d be happy to have you. The more the merrier.

This is disingenuous. You yourself told me the act of creating Grin++ was adversarial in its nature, and claimed that I was wrong to do so. This is just more virtue signaling.

---

### Post by @lehnberg ⭐ (2020-03-28)
*Post #64*

> > If you follow the consensus rules, your node will be treated just like any node on the network. And we’d be happy to have you. The more the merrier.
>
> This is disingenuous. You yourself told me the act of creating Grin++ was adversarial in its nature, and claimed that I was wrong to do so. This is just more virtue signaling.

It seems I wasn’t very clear, so let me expand. Whether you were being adversarial or not at the point of creation [@david](/u/david) is subjective and completely beside the point.

I actually would have thought you of all people would get the point I was trying to make:
You created your own implementation with Grin++ and have since secured your own funding. You have quite a lot of autonomy. You have your own governance for how you accept contributions to your codebase, and manage your release schedule. You can focus and prioritise matters that you consider most important to your users. And Grin++ nodes are being treated just like any other node on the network. As long as consensus rules are followed, why would that not be the case?

You’re clearly talented, and very passionate about Grin. Of course I would have wanted to see you improve the Rust implementation. But who am I to tell you what you should be doing? (: You wanted to take Grin in directions that you were not able to build consensus for in the months leading up to mainnet launch. So I get your logic for choosing to go at it on your own, allowing you to iterate, learn, and explore much faster. Grin++ seems to be doing well as a result, it is an alternative standalone implementation that allows for different approaches to be tried, and something Grin (Rust) can draw learnings from. If something bad would happen to the Rust project, there’s a chance the C++ project would be unaffected, and vice versa.

So now that Grin++ exists, having her around adds to the network, and creates resilience and reduces centralization. The whole network is greater than the sum of its two individual implementations. And so similarly to this, if there’s anyone else that thinks the approach we’re taking with the Rust implementation is so wrong that they cannot stand by watching this happen, or simply that they want to experiment with Grin in ways that the Rust implementation cannot support for whatever reason, they are welcome to build out their own alternative. Regardless of whether that’s a fork or a separate implementation (Grin Go anyone?). I would prefer you contributing to Grin (Rust) as we could use the help, but I’d rather you do your own thing than leave altogether.

Peace out

---

### Post by @lehnberg ⭐ (2020-03-28)
*Post #67*

I repeat that opinions are my own, and shouldn’t be attributed to members of the core team.

> You were kind enough to take the time to explain to me that the biggest reason I was disliked by several in the core team, and the reason why they were avoiding working with me, was because I created Grin++, rather than contributing to the Rust implementation.

You’re not quoting me verbatim, instead it feels like you are putting a negative spin on what I told you in that call. I’d appreciate if you stopped putting words in my mouth. The point of the call was to mend fences with you, but it looks like it had the opposite effect. That feels like a fail on my end, and unfortunate. In any case, you’re right - it doesn’t matter anymore.

My original post above was not directed towards you, Grin++, or whatever misgivings you have with the core team. You already have your own implementation, and I’ve already expanded in depth on the degree of autonomy you have. Is there anything more to say here?

> The claim was “we’d be happy to have you”. That was the outright lie I was pointing out.

Rather than agreeing or disagreeing with any of the points I raise, or making any kind of serious contribution, you’re highlighting one specific wording that you find provoking. This doesn’t feel like a discussion in good faith, more like nitpicking.

_“If you choose to fork the codebase or build your own implementation, we will find a way to carry on with the project despite of this.”_

Is that better?

> It’s clear that the community recognizes that the core team, despite containing a few really great people, no longer represents it. That’s positive news, and will hopefully lead to a brighter future someday.

You are already well aware of this, but for the benefit of other readers: Our governance model is not democratic, nor is it based on representation. To this date, we’ve never been governed by “the will of the people”, and there’s a reason for that (but let’s save it for some other thread).

That said, the _legitimacy_ of the governance model can always be put into question, and it is probably healthy to do so from time to time. I’m not so sure about our governance either to be honest, but I haven’t come across a better way to do it yet. I’m happy to consider constructive proposals.

In the meanwhile, those who feel this structure is illegitimate and want to do something about that can start new structures - the network will accept any alternatives that pop up, as long as clients can agree on consensus. This was the point I was trying to make.

The future is indeed bright.

---



## The 'Official' Grin GUI Wallet
*Date: 2020-04-01 | [Forum Link](https://forum.grin.mw/t/the-official-grin-gui-wallet/7209)*
*Importance Score: 93.4 | Core Participants: david, yeastplume, davidtavarez, tromp, joltz*

### Post by @Yeastplume ⭐ (2020-04-01)
*Post #1*

I just wanted to say a few things about our missing ‘official’ GUI wallet, and propose an idea that could help us find it.

I know that the approach members of the core team have taken toward GUI wallets is a bit of a sore point, and I completely understand this. Grin currently has usability problems, and having a nicely packaged ‘official’ GUI wallet that works on all platforms seems like a glaring omission that would go a long way toward addressing them.

GUI wallets are something that that I personally have been of two-minds about for just about the entire duration of this project. I’ve often thought that we should just bite the bullet and put one together. [I even started an experimental one at one point](https://github.com/mimblewimble/grin-web-wallet) just before launch, only to abandon it in favor of lower-level foundation work that seemed a bit more important at the time (and that I have more experience doing). But every time I’ve thought about it or floated the idea to other core members, I’ve always come back to the conclusion that this would be the wrong approach to take. This is even more true now than it has been in the past.

I like to think that the team is correct in taking a long-term view when it comes to proritising very limited resources, and the fact of the matter is that none of the core developers believe that creating an ‘official GUI’ wallet is the best use of their time or strengths at present. With the last of our two hard forks coming up fast, most of the developers would prefer to focus on important long-term architecture and protocol work.

So why not employ some of the fund to outsource it? I don’t personally believe it’s that simple. GUI projects (or indeed any project with a heavy design element) require a lot of ongoing feedback and management, and the design requires just as much ongoing maintenance work as any code. The effort and skills required to maintain an official GUI wallet are just as large a consideration as creating one in the first place, (if not larger).

This is not to say that I don’t think it’s important for the community to have easy-to-use, reliable wallets. As a matter of fact, I think that usability is currently Grin’s biggest problem. If you’ve followed the work I’ve been doing since launch, a lot of my time has been taken up with [creating a set of APIs](https://docs.rs/grin_wallet_api/3.1.0/grin_wallet_api/index.html) that enable downstream developers to create their own wallets and experiment with their own solutions to transaction-exchange challenges. There is also [plenty of effort underway](https://github.com/mimblewimble/grin-pm/issues/248) to standardize on formats and protocols before our last scheduled hard forks. Though I know it can seem frustratingly slow, the current approach is that the core team would prefer to continue to focus on what it can do best while also providing and supporting APIs and Infrastructure to make it easier for other developers to do the stuff we’re not great at.

And thus far, this strategy appears to be at least partially working, with the existence of several solid GUI wallets testifying to that. Niffler pretty much embodies the vision of a cross-platform GUI wallet that makes full use of the wallet APIs we’ve provided. Ironbelly has done all sorts of work to make the Grin wallet libraries usable on mobile. Grin++ has provided an all-in-one solution that uses its own architecture but is no less valid as a wallet that should be acceptable for use by the community.

However, I can completely understand that having no ‘official’ Grin GUI wallet is frustrating and confusing. Despite the presence of several very good wallets, the team thus far been very reluctant to fully endorse any of these community efforts. There are many reasons for this; a desire to remain impartial and fair, not wanting to discourage new approaches, and particularly issues around security and liability.

But however we got here, the end result is that we’re in a catch-22 situation whereby GUI wallets exist but it’s unclear to many, (particularly to newcomers) whether they’re endorsed or considered safe to use because they’re not ‘official’.

So I’d like to float an idea to address this:

If we had a process via which a particular wallet implementation could become “Approved by the Grin Community” (as is done with certain Monero wallets,) they could then be prominently listed alongside all of the other materials as fully endorsed by the community for use. In order to reach this status, the wallet would need to meet a set of criteria meant to strike a balance between security and inclusiveness. We’d need to sit down and think about what the exact criteria are, but they might be something like:

* Must be 100% open source and use open source libs
* Must adhere to all Grin RFCs and standards
* Must be kept up to date with the latest Grin releases (within reasonable timeframes)
* Must have a mutual disclosure agreement with the Grin project
* Any non-standard features or custom protocols must be clearly labelled as such and ‘use at your own risk’
* Somewhat community audited… and I’m not talking about exhaustive expensive audits, just that there have been enough community eyeballs on the code to determine nothing obviously malicious is going on (this one will be hard to get exactly right)

This list is not meant to be exhaustive or final, but the main point is that the criteria should not be onerous, be relatively easy-to-follow and should aim to not exclude any good-faith projects from meeting them. There is still quite a bit of thinking (for [@joltz](/u/joltz) in particular) as to a set of criteria that can strike the best balance, but I’m fairly sure it’s doable.

This would hopefully get us where we need to be with GUI wallet availability without duplicating efforts. Good GUI wallets exist that are already better than what an ‘official’ effort would come up with and can continue to be improved and refined, hopefully with the renewed focus that would come from them being as ‘official’ as they can be.

I’d also hope that this would encourage more people to apply their skills to these projects. Contributing to these wallets is just as worthy and helpful to the community as contributing to the main Grin project, and this would preserve the perception of this fact. For instance, someone with a bit of design skills could be directed to improve a particular Niffler screen (for instance,) as opposed to getting hit with the daunting task of “build us a GUI wallet”.

Interesting in hearing thoughts on this approach, particularly from the authors of such wallets and whether such a scheme would work for them.

---

### Post by @david ⭐ (2020-04-01)
*Post #2*

This is a fantastic idea. Let me know how I can help.

---

### Post by @tromp ⭐ (2020-04-02)
*Post #5*

I think they’re the ones getting listed at

[getmonero.org, The Monero Project](https://web.getmonero.org/downloads/)

### [Downloads](https://web.getmonero.org/downloads/)

Monero, a digital currency that is secure, private, and untraceable

---

### Post by @Yeastplume ⭐ (2020-04-02)
*Post #7*

So for an overall approach, I suggest we proceed something like:

* Collect feedback (in this thread and the wallet-dev channel) as to what the criteria should be
* [@joltz](/u/joltz) and I will collate and present a draft set for review
* Create a short, sharp RFC so the criteria is properly recorded
* We start working with interested wallet authors to get their efforts approved and ready for endorsement

Just a caveat that this is isn’t all going to be done at once and will take some elapsed time to roll out (particularly given the amount of other work going on,) but hopefully this initiative becomes a long-running thread that will continually improve the state of our community wallets.

---

### Post by @david ⭐ (2020-04-02)
*Post #8*

I know we’ve discussed this before, but bitcoin also takes this approach. <https://bitcoin.org/en/choose-your-wallet?step=5>

---

### Post by @david ⭐ (2020-04-02)
*Post #10*

True, but it’s still the unofficial “official” bitcoin website, in the same way that grin.mw is Grin’s.

---

### Post by @joltz ⭐ (2020-05-18)
*Post #16*

# Wallet Listing on grin.mw

It can be beneficial to list available wallets for users on the primary website for Grin, especially considering that there is not a GUI wallet in the mimblewimble github organization and that most users will want to use a GUI wallet.

There are two primary possible identified paths to support this, each with their own tradeoffs for the community.

## Option 1: Approval curated by core and security teams

The core and security teams can review and curate each wallet listed on grin.mw by manually reviewing to ensure they adhere to all RFCs and building confidence in the wallet developers ability to responsibly handle vulnerability disclosures.

Pros:

* Low chance of a malicious wallet being listed
* Guarantee that all listed wallets are compatible
* Ability to more seamlessly deploy security fixes across wallets

Cons:

* Approval is subjective without an exact checklist of steps that can be followed to ensure the core and security teams have a high degree of confidence (which may not be possible to produce in a comprehensive way)
* “Gatekeepers” become responsible for determining whether a wallet will be listed (and by extension used) in the Grin ecosystem
* There is still no guarantee of eliminating the possibility of malicious wallet activity

## Option 2: (Almost) any wallet can be submitted and ranked before listing

Any wallet developer can submit their app to be rated by the core and security teams according to the same metrics used by [bitcoin.org](http://bitcoin.org). Once rated the wallet will be listed. Wallets are removed by verifiable cases of (willful or not) malicious wallet activity. Wallets that do not verifiably follow accepted RFCs are not rated or considered for listing.

Pros:

* Less centralized, more open listing method
* Helps users find the right wallet for the right use
* No “gatekeepers” subjectively determining which wallets can be listed
* Though there are still “gatekeepers” doing the ratings

Cons:

* With a low barrier of entry some users could lose funds to a malicious wallet before it is detected and removed from the list
* Users may not be able to trust any of the wallets listed if there is a mix of “trustworthy” wallets with those that aren’t

Option 2 seems like a decent compromise of openness and quality. However there is a much higher chance of fund loss due to a malicious wallet being listed in option 2. Option 1 doesn’t guarantee a wallet won’t be malicious in the future either so we do want to avoid giving a false sense of trust or security. Maybe there is a mix of these that will produce the best result. It is important that whichever direction is chosen, users are aware of the risk of malicious wallet activity.

Just wanted to share these thoughts ahead of the next governance meeting <https://github.com/mimblewimble/grin-pm/issues/290>

---

### Post by @davidtavarez ⭐ (2020-05-21)
*Post #21*

There is a Telegram Group for Grin++ Support: <https://t.me/GrinPP>

---



## Network Upgrades / Hard forks on Grin v5.0.0 and beyond
*Date: 2020-04-06 | [Forum Link](https://forum.grin.mw/t/network-upgrades-hard-forks-on-grin-v5-0-0-and-beyond/7231)*
*Importance Score: 89.7 | Core Participants: david, tromp, antioch, lehnberg*

### Post by @lehnberg ⭐ (2020-04-06)
*Post #1*

In a dev meeting on Mar 3 there was a [discussion about how to handle hard forks / network upgrades after v5.0.0](https://github.com/mimblewimble/grin-pm/blob/master/notes/20200303-meeting-development.md#5-how-to-handle-upgrades-after-500), i.e. once the last of the [four currently scheduled hard forks](https://forum.grin.mw/t/proof-of-work-update/713) has occurred.

I’m making an attempt here to summarize some of the ideas discussed in the meeting. Please correct anything that is in need of it, and feel free to make other suggestions for improving this or make proposals of your own in tread and I will update.

The objective is to evaluate possible options and attempt to converge on a path forward well in advance of the deployment of v5.0.0 (Jan 15 2021), even if the agreement is to `do nothing`.

A continuation of this discussion is on the agenda for the April 14 development meeting, those interested are encouraged to participate.

* * *

### PLEASE NOTE

There are **NO PLANNED CHANGES** to Grin’s proof-of-work, and is something unrelated to this discussion.

* * *

# Alternatives discussed

# | Proposal | Hard forks | Motivation | Considerations
---|---|---|---|---
1 | Do nothing | By “community agreement”. | Sticks to the plan, and true to what was said before launch. Limits the degree of centralization. “Immutable by default.” | The path to a hard fork in practice is undefined. If there’s a consensus-breaking critical vulnerability that needs fixing, it may not be possible to upgrade the majority of the network successfully. Without a scheduled HF, the fear is that there will not be _any_ HF. Our stance towards soft-forks will significantly impact the ability to conduct upgrades without hard forks.
2 | Yearly evaluation | 1 scheduled HF, 1 year ahead, re-evaluated yearly. | Provides a controlled path for network upgrades, with the intention to be removed once network stabilizes. | Centralizes around those who control releases, i.e. core team at the moment. When is the network considered “stable enough” to remove hard forks? Will there ever be enough incentive to give up this control of the network?
3 | x years more | x scheduled HFs, once a year. | Gets the contentious decision out of the way once and for all so that work can focus on development, rather than a debate each year. | Would be a clear statement that Grin is years away from being stable and will remain under heavy development on the consensus layer for the foreseeable future. What happens after x years, and why would the situation be different then?
4 | Hard fork olympics | Every 4 years, counting from genesis (indefinitely) | Like the bitcoin halving, and Olympic Games |
5 | Hard fork phaseout | Every `2^i * YEAR_HEIGHT`, for `i = 2,3, ...` | Inspired by the original PoW phaseout schedule, this would appeal more to those who’d like to see Grin become increasingly consensus-immutable than proposals 2 and 3. Note the large 2-year gap after the final pre-planned HF4. | Our stance towards soft-forks will significantly impact the ability to conduct upgrades between hard forks.

* * *

### Changelog

_April 07: Tweak wording in #1-considerations._
_April 07: Adding #4 and #5_
_April 08: Adding soft-fork considerations to #1 & #5_

---

### Post by @david ⭐ (2020-04-07)
*Post #2*

I’d like to add one more option: Make Grin more softfork-ready. This isn’t foolproof, since it’s difficult to predict exactly what changes may be desired in the future. But there’s a few things we can do that will provide a decent bit of flexibility.

---

### Post by @tromp ⭐ (2020-04-07)
*Post #5*

lehnberg:

> If there’s a consensus-breaking critical vulnerability that needs fixing, it may not be possible to upgrade.

A critical vulnerability needs to be fixed one way or another, and if breaking consensus is the only way, then that clearly warrants a HF. In what way would it “not be possible to upgrade”?

---

### Post by @lehnberg ⭐ (2020-04-07)
*Post #6*

> I’d like to add one more option: Make Grin more softfork-ready. This isn’t foolproof, since it’s difficult to predict exactly what changes may be desired in the future. But there’s a few things we can do that will provide a decent bit of flexibility.

Making Grin mode softfork-ready is something that can be researched and proposed in parallel to this discussion. I think it would be important to understand what changes we would like to see there, regardless of the options above. Would you agree?

---

### Post by @tromp ⭐ (2020-04-07)
*Post #10*

I would like to throw out option 4, inspired by the original PoW phaseout schedule.

4. Plan increasingly rare successive future hardforks at heights 2^i * YEAR_HEIGHT, for i = 2,3, …

Not saying that I’m in favor of this, but this schedule should appeal more to those who’d like to see Grin become increasingly consensus-immutable than proposals 2 and 3. Note the large 2-year gap after the final pre-planned HF4.

---

### Post by @lehnberg ⭐ (2020-04-08)
*Post #17*

So our stance on soft forks may instruct our stance on scheduled hard forks. Thanks for clarifying, that now makes sense to me.

I’ve added a “soft fork” discussion point to [Tuesday’s dev meeting](https://github.com/mimblewimble/grin-pm/issues/273) to see if we can get some clarity / action points from that. Please join if you can!

In the meanwhile, how could the matter of soft-forks best be reflected in the table above? Should it be its own option? If so what would the contents of each cell be? Should it be a column? It’s own section? Something else?

---

### Post by @antioch ⭐ (2020-04-09)
*Post #21*

tromp:

> Plan increasingly rare successive future hardforks at heights 2^i * YEAR_HEIGHT, for i = 2,3, …

Is it accurate to call this “increasingly immutable”? The space between HFs increases but its not really any less mutable. I’m not sure that a stable period of 8 years followed by a HF is really any more immutable than a HF every 12 months?

Edit: Not trying to pick holes in this - just trying to wrap my head around what “immutable” looks like, short of zero HFs.

---

### Post by @lehnberg ⭐ (2020-04-10)
*Post #24*

Paouky:

> Anyway, why does the stance towards softforks lean negative currently?

How did you arrive to that conclusion?

---



## Pep Talk for one sided transactions
*Date: 2020-05-25 | [Forum Link](https://forum.grin.mw/t/pep-talk-for-one-sided-transactions/7361)*
*Importance Score: 108.2 | Core Participants: david, tromp, davidtavarez, lehnberg*

### Post by @system (2020-05-25)
*Post #1*

Earlier today i followed a discussion between [@lehnberg](/u/lehnberg) and [@david](/u/david) on telegram ([t.me/grincoin](http://t.me/grincoin)) regarding one-sided-transactions.
lehnberg wrote:

Thanks David.
There has been “some honest technical discussion” though. The reduced security model issue was identified by antiochp / jaspervdm / tromp after a review on keybase. The rogue key attack, a critical exploit that would allow funds to be stolen, was discovered by tromp and another researcher independently. These were two previously unidentified issues that were picked up by other people reviewing your proposal.

If there ought to be more review, it would be encouraging to keep an accurate, up to date version of the proposal somewhere. Leaving a critical exploit unpatched more than a month is discouraging, and makes it look like the entire effort was abandoned, even if the fix is trivial as you say. Having a place where grin-specific reviewer feedback can be shared helps to bring everyone on the same page, where a comment from one reviewer might inspire another. Doesn’t need to be an RFC, even if that seems like an obvious option.

Comparing this with the armored slates / slatepack proposal does not do your idea justice. Slatepack has a much smaller impact and is also less complex, so was much easier for me to engage with. It obviously helps that it doesn’t raise any contentious, over arching questions of the project like “Should Grin be less secure than Bitcoin?”, or come with any other comparable trade-off. It’s an approach that feels simple and contained in comparison, with fewer “unknown unknowns” and risks for potentially catastrophic protocol failures.

It may well be that the worsened security model only leads to an attack that’s impractical, I would guess that depends on the motivation and resources of the attacker. Introducing the risk for such an attack weakens Grin’s security model nevertheless, and makes it strictly worse than that of Bitcoin, I don’t think this can be disputed. To “simply self-spend coins when you receive large amounts”, as you write in the LIP, seems like something that might be a bigger issue than having interactive transactions.

Davids Response:

The changes to the security model were fleshed out on day 1, and the attack was even mentioned by tromp as having no practical difference than any 1-week reorg of the blockchain. The rogue key attacks were identified after I had to go dark with my proposal, since discussion of it was no longer permitted on keybase, which shows more honest technical discussion is needed. Just as relative kernels changed in form numerous times due to various technical challenges, so too has the one-sided proposal, but unfortunately all of these changes had to occur outside of keybase discussions.

I kept an up to date version of the proposal for quite some time, but as discussion of it was discouraged on grin channels, I stopped maintaining it. Litecoin won’t be ready for one-sided transactions for quite some time, so I have not prioritized maintaining their version.

And yes, it is impractical. It requires a _one-week reorg_. If that occurs to _any_ PoW chain, that coin is already dead, and the opportunity for an attacker to steal coins would’ve already been enormous. I can’t tell if you don’t understand the attack, or you’re just intentionally trying to oversell the risks.

Anyhow, those are my last words on the subject. You may continue to suggest that it’s an insecure scheme, or that it’s my own fault that the technical discussion never took place. I’m done playing these political games.

If the receiver is concerned that the sender could reorg the blockchain an entire week some point in the future, then yes, a self-spend would prevent that, and therefore give you the same security as bitcoin.

[@david](/u/david) has always been concerned about making Grin as easy to use as possible. At the end of the day, this is what this project is about: Usable Electronic transactions for all without censorship or restrictions (grin.mw). His Grin+±Wallet is just that: It makes Grin easy to use for folks who happens to not be computer scientists surfing on a CLI on Gentoo Linux.
Being usable is were Grin needs to go (where else should it head to?).

[@lehnberg](/u/lehnberg) has always been concerned about making sure the Grin Fundamentals are as robust and secure as possible. This is crucial. Without robust systems that are resiliant towards attacks you can not have usable Electronic transactions for all without censorship or restrictions (grin.mw).

So i really don’t get what the aforementioned discussion on telegram was all about. You have the same goals. Grin needs to be more usable (which it is currently not) and it needs to be robust at the same time.

Usually electronic payment is for participiants a no-brainer or as you would say “fire and forget”: You click on “ok/send/confirm” and it is done - the recepient gets the payment delivered by the underlying payment system. Grin is unintuitive to this. You need the recipient to do stuff, send something back or have his wallet online at the same time (what if his deskop-pc is offline because he is at sleep?). One-Sided Transactions need to happen and this is why [@david](/u/david) stresses this so much for very good reasons.
Obviously it is not trivial to get there with MW.

Back in the day Bjarne Stroustrup was super unhappy with C. So he created C with Classes (C++). There was one problem: The first C with Classes Implementation was a little slower than C. It was 3 % slower in direct comparison. But who cares, it got classes, right? The speed penalty coming with the concept of classes could have be seen as an acceptable trade-off for the new feature. Turned out Stroustup deemed the speed penalty totally unacceptable and so they started working on it and were able to remove the overhead (<https://www.youtube.com/watch?v=69edOm889V4> 26:10). In fact they got the classes and the speed.

I really hope for Grin and its mission that the devs think about how get Grin usable and resiliant towards attacks at the same time. It will not be enough to just point out to the security-flaws one suggestion towards a better usability might bring ([Status of Litecoin Improvement Proposal LIP-0004 for one-sided transactions](https://forum.grin.mw/t/status-of-litecoin-improvement-proposal-lip-0004-for-one-sided-transactions/7259)).

When nobody uses Grin it does not matter that it is robust under the hood.

---

### Post by @lehnberg ⭐ (2020-05-26)
*Post #4*

Good idea to create a thread here [@Grundkurs](/u/grundkurs).

The conversation started here:

[Telegram](https://t.me/GrinCoin/113708)

### [Grin Hub](https://t.me/GrinCoin/113708)

Grin ( ツ) is a lightweight MimbleWimble protocol implementation.

And ended here:

[Telegram](https://t.me/GrinCoin/113947)

### [Grin Hub](https://t.me/GrinCoin/113947)

Grin ( ツ) is a lightweight MimbleWimble protocol implementation.

---

### Post by @davidtavarez ⭐ (2020-05-26)
*Post #5*

The idea of interactive transactions might be good in terms of privacy but in practice isn’t working pretty well. From the Developer perspective, I can tell people faces the same issue over and over again: “making their wallet reachable”; I ended up hosting [a Service](https://forum.grin.mw/t/is-this-grin-wallet-url-reachable/7349) just for that and integrating this to [Grin++ GUI](https://github.com/GrinPlusPlus/GrinPlusPlusUI/pull/39). This is adding more and more unnecessary complexity making harder to bring all Grin features to a Wallet. Also, just thinking about a Mobile Wallet is a huge headache, the only feasible approach is to connect the wallet to a remote Node, making Grin less private, anonymous and, more important, less secure, **which is not an option**.

I’m not saying that non-interactive transactions are something easy to achieve, for sure it’s hard; I agree there is no a final proposal, but for God’s sake, this is something that will make life easier to everyone, users, developers and Exchanges. I’m trying really hard to not sounds biased on this topic, but it’s a headache, a bad one. The gains of non-interactive transactions are so much that is it really hard to argument against it.

I can’t understand why this is not a #1 priority.

---

### Post by @tromp ⭐ (2020-05-26)
*Post #8*

I love MW for its conceptual simplicity and elegance.

Its outputs are Pedersen commitments r*G+v*H which combine value and blinding factor into a single curve point. The blinding factor serves both to hide the value and to control ownership. Correspondingly, a single (multi-)signature serves both to prove value balance (non-inflation) and to authorize transfer of ownership. That’s kind of magic.

This allows MW to completely do away with bitcoin script, which is a language for specifying the conditions under which individual outputs can be spent, usually signatures with public keys that hash to a given value.
It’s also a huge source of complexity within Bitcoin.

MW instead requires interaction between sender and receiver to construct the signature. This incidentally removes the possibility of certain errors where funds are sent to the wrong place. (and makes it very ransom unfriendly). Note that such interaction is also required in 2nd layer networks like Bitcoin Lightning that is seeing growing adoption, and is bound to be the common form of transacting if Bitcoin is ever to see mainstream adoption. Having a similar experience between on-chain and off-chain tx building will ease the transition for Grin users.

In the one-sided tx proposal there would be two very different kinds of output. The simple MW ones that we have now, and complex ones that have several (at least four) additional fields of data attached to it.
For these complex outputs, the blinding factor no longer suffices to control ownership, as it will be known by both sender and receiver.
Rather, as in bitcoin, the spender must also prove knowledge of a specific public key. The full extent of additional data and rules is not clear, as the proposal is incomplete. It’s also not clear how transactions should deal with a mix of simple and complex inputs/outputs.

I find these complications to be detrimental to the simplicity of MW. Grin in particular aims to be a minimal and lightweight implementation of MW and this is neither.

The security problem may not be relevant in practice due to absence of week-long reorgs, but is still an ugly wart.

The main reason for the current usability problems is that exchanges don’t offer a backup mechanism for wallet connection failures, something that the deprecation of http and compact slates should improve.

---

### Post by @david ⭐ (2020-05-29)
*Post #33*

oryhp:

> Try downloading Bitcoin from 2010 and using it

I have. It was simple to use. This narrative does not work in Grin’s favor. I’ve done as much or more than anyone to try to make Grin more usable, and I still can only dream of it being as usable as 2010 bitcoin.

oryhp:

> If interactivity turns out to be a problem that can’t be solved, then Bitcoin has a much bigger problem than Grin

Here’s a well known LN enthusiast from Blockstream just a few days ago: <https://twitter.com/notgrubles/status/1265872951246753792>

The truth is, requiring private keys to remain online in order to receive is just terrible for security. You can’t just brush that off. It’s bad for real, practical security - not just imaginary scenarios about senders performing unheard of week long reorgs to take back the money they sent you.

---

### Post by @lehnberg ⭐ (2020-06-03)
*Post #55*

If you build grinbox into the p2p layer, it becomes a DoS / spam vector. Just flood the network with messages. They’re end-to-end encrypted, so it’s not easy to tell whether they are legit or not. Using proof-of-work as a rate limit etc is easier said than done effectively (i.e. to actually stop a motivated attacker, rather than being a nuisance for legitimate users), and if we want clients to broadcast using Tor, then sybil attacks can be tricky to prevent.

If you do not build it into the network, these concerns still apply, but they won’t affect the p2p network if they occur. Still, it becomes difficult to have this as a default (i.e. see any meaningful adoption) unless you explicitly enforce ONLY grinbox as the accepted method, that’s then run through a federated network of relay servers that are operating at loss. Kind of like how SMTP works today for email.

You’d have `gd6p24toTTDj7sxCCM4WGpBVcegVjGi9q5jquq6VWZA1BJroX514@grinbox.io` or some other `@relay.com` address depending on which server you used. If you connect to the relay over Tor, there’s no leakage of IP data.

These relays become critical point of failures for transaction building. So it would be a systemic risk if a lot of users are on [grinbox.io](http://grinbox.io) for example and the server goes down.

As one of the people working on grinbox, I really wanted this to work. It’s extremely simple compared to other solutions, it can be made to be fairly privacy-preserving, it’s reliable, fast, and performant. But for this to be viable for grin as a default, I think we’d need to see A LOT of people, companies, organisations running their own federated relays, and users being fairly well distributed between these relays. Then it’s decentralised and resilient to shocks. Otherwise it’s centralised and sensitive.

Unless the p2p network nodes act as the relays, but then you’re making it more resource intensive to run nodes (which may go against other objectives), and even if we wanted to do that, it’s still not clear to me how you’d execute that in a simple, reliable, and scaleable way.

---

### Post by @lehnberg ⭐ (2020-06-04)
*Post #57*

I appreciate your opinion about how to go about this. We’re all trying our best to come up with something that works. If there’s a slam dunk approach on how to go about this that ticks all our boxes, it seems it’s yet to be discovered[1]. Until then, I believe it’s a matter of figuring out what trade-offs we’re comfortable making.

> Beam solely relies on SBBS and would be screwed if DoS’d and they havent been.

“Project X has a DoS vector and they have not been DoS’ed yet” is not a strong security guarantee, in my opinion. Still, there’s a real opportunity for us to study and learn from the approach Beam took with SBBS.

> Tari is also relaying messages in p2p layers built into the tari protocol.

Tari is not in production yet. Their solution may work well in testnet, but that alone does not directly translate to a production grade solution that’s simple, reliable, and scaleable. But perhaps it will be! Tari’s approach is also something we should study and learn from. It seems that their objectives and priorities are different from ours and that they are making different trade-offs as a result.

> Fall back on slatepacks if attacked.

If relays are integrated into the grin nodes, it is the p2p network itself that is being disrupted if the relays come under attack. How does falling back on slatepacks help in that scenario?

* * *

[1] I believe this comparison table illustrates this quite well [Compare transaction-building alternatives · Issue #283 · mimblewimble/grin-pm · GitHub](https://github.com/mimblewimble/grin-pm/issues/283)

---

### Post by @lehnberg ⭐ (2020-06-04)
*Post #59*

> If it could DoS the whole network then it seems like that attack is possible with current comms too but we already either accept that or have sufficient mitigation measures in place.

P2P relays for encrypted transaction slates act as message stores. They have to store arbitrary amounts of data that anyone can send to them, that is difficult to validate to be legit while still preserving privacy, and that can be produced cheaply. An attacker could flood these relays with half built transactions until the hard drives fill up or some limit hits and legit slates stored on the p2p network get crowded out.

I don’t think you can do something similar in the current grin p2p network. You could try to flood the blockchain with finalised transactions, but that will require you to build valid transactions and pay transaction fees.

---



## Came Across 1st Grin ASIC of the World
*Date: 2020-05-31 | [Forum Link](https://forum.grin.mw/t/came-across-1st-grin-asic-of-the-world/7383)*
*Importance Score: 103.6 | Core Participants: tromp*

### Post by @gary (2020-05-31)
*Post #1*

**Finally saw this Grin ASIC hope to see the miner soon  **

(Came across Thomas from MicroComputer, took a few pictures together with this first Grin ASIC in the world ) Thomas said this chip was produced at 2020 week 18, as labeled on the chip.

[ WechatIMG1633024×4032 1.88 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f9369d0f5a04120586c5f7896fa5ff10d673831e.jpeg "WechatIMG163")

!

[ Screenshot 2020-06-01 at 6.42.27 AM915×327 385 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/bc2011d389ae66a9e92ed36fa2ba55e7e5a2bf28.png "Screenshot 2020-06-01 at 6.42.27 AM")

* News (in Chinese) from MicroComputer: <https://mp.weixin.qq.com/s/xqn-O7M9XX8FvmW3YBI9Ew>

---

### Post by @tromp ⭐ (2020-06-01)
*Post #5*

Thanks for the info , Gary!
Could you possibly ask them if the ASICs uses lean or mean (or the hybrid slean) mining?
Note that lean C32 would require 512/k MB SRAM + 512 MB DRAM for a k-pass solver, while a mean C32 would require about 16GB, and slean could use anything in between.

---

### Post by @tromp ⭐ (2020-06-02)
*Post #14*

It would also be nice to know how much SRAM is on the chip, and how much HBM2 DRAM is in those HBM2 stacks on top.

---

### Post by @tromp ⭐ (2020-06-02)
*Post #16*

Thanks, gary! So they use an 8x tmto (time-memory trade-off). For each trimming round they would need to read the 512MB edge bitmap 8*2=16 times. That’s a lot of memory bandwidth!

---

### Post by @gary (2020-08-10)
*Post #24*

Finally, I borrowed one G1 miner a few days ago and tried it by myself, so I can share some updated info here  (Thanks Thomas to borrow this miner to me for a test!)

Took two shots on this G1 miner ~

[ WechatIMG522976×3968 2.93 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/26e09d938c0e736e7fcde3fcb84660763d855f8b.jpeg "WechatIMG52")

[ WechatIMG512976×3968 2.38 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4ca7c9acdaa2a19f7f00f0c759427ccb6d91a095.jpeg "WechatIMG51")

The box dimension is about **44cm x 20cm x 35cm** , it looks like a desktop computer. The box weight is about **20kg** , including that attached power adapter. 4 big strong fans, 2 on each sides. The box is quite solid.

I connected this miner to a grin node to try mining, after less 24 hours, I got 3 blocks ([819660](https://grinscan.net/block/819660), [820461](https://grinscan.net/block/820461), [820801](https://grinscan.net/block/820801)) mined

20200809 13:24:27.998 DEBUG grin_servers::mining::stratumserver - (Server ID: 0) sending block 819493 with id 1 to single worker
20200809 13:24:27.998 DEBUG grin_servers::mining::stratumserver - (Server ID: 0) sending block 819493 with id 1 to stratum clients
20200809 13:24:30.856 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash b13185fb5af2, edge_bits 32, nonce 2822347394407211024, job_id 1, difficulty 23670/346750698, submitted by garyyu/001
20200809 13:24:33.213 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash cc8efaa0f499, edge_bits 32, nonce 11267890822336005302, job_id 1, difficulty 20504/346750698, submitted by garyyu/001
20200809 13:24:34.088 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash 28597ef96965, edge_bits 32, nonce 2822347394407211104, job_id 1, difficulty 103949/346750698, submitted by garyyu/001
20200809 13:24:34.395 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash 9d09f77d5d90, edge_bits 32, nonce 11267890822336005304, job_id 1, difficulty 26708/346750698, submitted by garyyu/001
20200809 13:24:34.732 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash 0fac411569d7, edge_bits 32, nonce 5322658827254272993, job_id 1, difficulty 267615/346750698, submitted by garyyu/001
20200809 13:24:35.832 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash 1cdae8850f53, edge_bits 32, nonce 11267890822336005336, job_id 1, difficulty 145357/346750698, submitted by garyyu/001
20200809 13:24:35.946 INFO grin_servers::mining::stratumserver - (Server ID: 0) Got share at height 819493, hash 442412a003f1, edge_bits 32, nonce 5322658827254272937, job_id 1, difficulty 61553/346750698, submitted by garyyu/001
... ...
20200809 15:59:12.039 WARN grin_servers::mining::stratumserver - (Server ID: 0) Solution Found for block 819660, hash 000114ea9675 - Yay!!! Worker ID: 1, blocks found: 1, shares: 7306
20200810 05:21:13.935 WARN grin_servers::mining::stratumserver - (Server ID: 0) Solution Found for block 820461, hash 00018450ea14 - Yay!!! Worker ID: 4, blocks found: 1, shares: 10569
20200810 11:07:57.219 WARN grin_servers::mining::stratumserver - (Server ID: 0) Solution Found for block 820801, hash 00014082e010 - Yay!!! Worker ID: 0, blocks found: 1, shares: 1468

The related wallet display is as follows:

$ ~/release/grin-wallet/grin-wallet outputs

Wallet Outputs - Account 'default' - Block Height: 820835
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Output Commitment                                                   MMR Index  Block Height  Locked Until  Status   Coinbase?  # Confirms  Value         Tx
=============================================================================================================================================================
08f40b48224b889e5d8c193ee968259ffd473c207560c909b54695e4288b6a2060  None       819660        821100        Unspent  true       1176        60.000000000  0
-------------------------------------------------------------------------------------------------------------------------------------------------------------
0876d0816a2e10bc21b632ccc82afbcd102f54f95d72bb90f8b208dbcbd5c05946  None       820461        821901        Unspent  true       375         60.000000000  1
-------------------------------------------------------------------------------------------------------------------------------------------------------------
08406fd920a38f59bcdd4d5cc8f764d3deb9af22f0ba5214143fcee926056637a0  8024312    820801        822241        Unspent  true       35          60.001000000  2
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Command 'outputs' completed successfully

BTW, I tested it at my home, the big noise of the fan is a little bit annoying for the family, I have to **limit the maximum fan speed to 30% for this test**. I suppose the miner performance will be much better if let its fan work at maximum 100%.

For thanks and fun to read this post, I would like to **share above mined 3 blocks award** to people who request to be shared here  Please just leave here your wallet receiving address, I will send 10 GRINs for each request, until the total 180 GRINs has been completely sent out. (only one request per one forum user of course.)

( **Tip** : About the detail info of this G1 miner, if interested, you can ask the manufacturer directly on next Grin governance meeting on Tuesday Aug 11 @ 15:00 [UTC](http://www.timebie.com/std/utc.php) in [Keybase main lobby](http://keybase.io/team/grincoin), Thomas from Vidtoo & MicroComputer will join that meeting for some Q&A. Refer to the [news here](https://forum.grin.mw/t/there-will-be-an-asic-ama-in-next-governance-meeting/7626)).

---

### Post by @tromp ⭐ (2020-08-10)
*Post #64*

This thread is turning into a slatefest!

---

### Post by @tromp ⭐ (2020-08-13)
*Post #139*

Without this ASIC on the horizon, I would be really looking forward to the 3080Ti which is now rumored to feature 20GB of GDDR6(X) memory, pretty much ideal for C32…

[Wccftech – 12 Aug 20](https://wccftech.com/nvidia-geforce-rtx-30-ampere-gaming-graphics-card-rtx-3080-ti-rtx-3080-launching-in-24-gb-20-gb-10-gb-variants/ "03:00PM - 12 August 2020")

### [NVIDIA GeForce RTX 30 Ampere Gaming Graphics Card Launching in 24 GB, 20 GB,...](https://wccftech.com/nvidia-geforce-rtx-30-ampere-gaming-graphics-card-rtx-3080-ti-rtx-3080-launching-in-24-gb-20-gb-10-gb-variants/)

NVIDIA's GeForce RTX 30 Ampere gaming graphics cards including the RTX 3080 Ti & RTX 3080 will launch in 24 GB, 20 GB & 10 GB flavors.

---

### Post by @tromp ⭐ (2020-08-17)
*Post #162*

I really don’t know. Could be as little as 10% or as much as 50%…

---



## Replay Attacks and possible mitigations
*Date: 2020-06-10 | [Forum Link](https://forum.grin.mw/t/replay-attacks-and-possible-mitigations/7415)*
*Importance Score: 100.0 | Core Participants: david, yeastplume, tromp, antioch*

### Post by @tromp ⭐ (2020-06-10)
*Post #1*

In a recent thread [1], Kurt outlined some possible replay attacks, and suggested consensus changes to avoid them.
Since then there has been some more keybase discussion of the seriousness of these attacks, as well as alternative ways to deal with them.
In this post I’d like to provide a summary of our current understanding of replay attacks and the options for mitigation.

Let’s consider the simplest possible form of a replay: that of a transaction tx with single input A, single output B, and single kernel K. In practice, replayed transactions would probably feature a change output as well, but they don’t fundamentally change the nature of the problem, so in the interest of clarity we’ll leave them out. A replay of tx happens when

tx: A --> B (K)

appears for the 2nd time on chain, say at height h2, after an earlier occurence at height h1. This is only possible under certain circumstances:

i) The same output can appear multiple times in the output MMR.
This is actually always possible in MimbleWimble with cut-through, since the consensus model doesn’t include the set of all spent outputs. Duplicate unspent outputs are not allowed simultaneously though: an output can appear at most once in the UTXO set. So B must have been spent in between h1 and h2, let’s say by some tx2.

ii) The same kernel can appear multiple times in the kernel MMR.
Since the Mimblewimble consensus model does include the set of all kernels, it’s up to each MW implementation whether to allow reoccurence of kernels, or to enforce unique kernels. The latter comes at a nontrivial cost though; necessitating a lookup of every new kernel in the set of existing ones. For the sake of efficiency, and simplicity of the consensus model, Grin chose not to do that.

iii) Output A must be re-created. This is not possible with publicly available wallet implementations. An attacker would need to make some minor changes to the source code to achieve this.

With all 3 circumstances holding, tx can then be replayed. At first glance this appears to be just giving free money to Bob, the original owner of B. But the following scenario shows how this could be an attempt to defraud Bob.

Let’s say that in the past, Alice paid Bob with tx to buy 1 trinket, and that Bob
ends up spending output B in tx2 to pay Charlie: A -> B -> C. Bob doesn’t realize that Charlie is colluding with Alice (or simply is an alter ego for Alice).

Now Alice proposes to buy another trinket from Bob, and they construct a transaction tx3 to pay for it. But instead of publishing tx3, Alice replays tx.
Bob’s wallet will notice output B as one it has generated.

If the wallet simply shows B as part of Bob’s spendable balance, and fails to show the pending status of tx3, then Bob may easily be fooled into accepting the replay as payment for another trinket. In which case Alice plans to replay tx2 as well after receiving the trinket. and thereby recover some or all of her payment, defrauding Bob.

This is what we must prevent from happening.

As mentioned before, one way is to change the consensus model, and enforce unique kernels, at some loss in efficiency.
The other way is to make wallets aware of previously spent utxos.

If the wallet still remembers that output B was spent earlier (in tx2), then it should consider new appearances of B as invalid, and either ignore them completely, or mark them as replayed so that Bob may realize the defrauding attempt.
This appears to be suffice for mitigating replay attacks, but we cannot guarantee that wallets remember all earlier spends, since they may become corrupted or inaccessible. In that case Bob would perform a wallet restore from his backed-up seed phrase.

Recall that we said above that “Bob’s wallet will notice output B as one it has generated.”
We can now see that this should be strengthened to “Bob’s wallet will notice output B as one it has generated _after_ its last restore” if the wallet was in fact restored.

If the wallet should find an output that was generated before the last restore, then it cannot know whether it was spent before. Such outputs should be marked as suspect, and would not contribute to the spendable balance.
Instead, the user should be given the option to either spend them back to oneself, or mark them as safe, with the user accepting any possible risk of replay.

This leaves the wallet restore process itself, that also finds lots of previously generated unspent outputs. This presents the greatest burden on the user (but there are other reasons why a restore cannot generally be expected to be a seamless experience).
They could again be given the above options for each output, or to sets of outputs that they group together. Perhaps they would respend all those above a certain value and accept the risk of replay on smaller ones.

Together, these suggested wallet behaviours should make replay attacks mostly pointless.
They do come at the cost of some UX complications in the presence of attacks or in the case of a wallet restore, hopefully both rare events.

[1] <https://forum.grin.mw/t/enforcing-that-all-kernels-are-different-at-consensus-level/>

---

### Post by @antioch ⭐ (2020-06-13)
*Post #7*

oryhp:

>   * Build wallet protection - no consensus changes
>

Is there some additional data we could add to a “payment proof” that would give recipients sufficient context in this situation? Payment timestamp for example.

My understanding of the “replay attack” is roughly as follows -
I am Bob.
Alice sent me funds previously.
I subsequently sent those funds to Charlie.
If Alice were to replay the A->B tx, this would open up possibility of replay of the B->C tx.
I do a full restore.
Alice replays A->B tx and (re)introduces an output into my wallet.
I now have a “raw” wallet with unspent outputs but no context, no tx history etc.
Alice is attempting to convince me that she paid me (a 2nd time) and that I should ship a widget out to her.
Alice is hoping I agree, so she can then “replay” the B->C tx to send those funds to Charlie.

I have no payment proofs as my wallet if restored and I have no tx history.
I effectively have no way of knowing the “state” of outputs in my wallet (w.r.t. replay risk).

So I ask Alice to produce the payment proof that we built together.
Alice reluctantly obliges and produces _a_ payment proof. But this is from the 1st original tx (we never built a 2nd one, it was only replayed). Alice is hoping I don’t look too closely.

According to the payment proof the tx was from several months ago.
But looking at the output it was added on-chain recently.
The discrepancy here is enough to make me question Alice’ motives.

So before I ship the widget out I sweep this output into a new output and wait for enough confirmations to be comfortable. These funds are no longer at risk of replay.

tl;dr Maybe we don’t need to sweep _all_ old outputs during a wallet restore. We can potentially be smarter with identifying “risky” transactions.

---

### Post by @david ⭐ (2020-06-13)
*Post #10*

oryhp:

> I think that putting any rules on the UTXOs means that the new nodes won’t be able to validate these rules.

Sure it can. Nodes only need to care about the UTXO set. By having a max height on the UTXO, it’s not possible to replay the transaction after that height.

oryhp:

> Regarding the kernel max_height I mentioned, I’m actually not sure the idea is good.

I have no opinion on whether or not it should be implemented. I was just offering an efficiency improvement.

---

### Post by @tromp ⭐ (2020-07-09)
*Post #53*

Suppose all wallets observe the following rules:

1. The wallet keeps track of what outputs it created, and which ones it spent.

2. When a previously-spent output re-appears anywhere, it is burned as fees.

3. When an output not known to have been created appears, it is in limbo, and the user is given the choice to accept it (e.g. when known to be created by a child wallet), or refresh it (e.g. sweep).

[EDIT] 3.5) When the wallet signs for some outputs to be spent (i.e. used as inputs), they are also considered in limbo (currently shown as "Awaiting finalization), until spent on-chain.

4. The wallet reports clean status if no coins are being burned or in limbo.

5. Upon restore, the user is asked for the last known date with clean status. All prior identified utxo are considered created and never-spent. All later ones are considered in limbo.

What would then be a realistic attack scenario?

---

### Post by @tromp ⭐ (2020-07-09)
*Post #63*

oryhp:

> A failure to publish a tx could expose a kernel which is the secret to a replay.

Good point. So an output that you signed for to be spent should also be considered in limbo. Post adjusted to reflect this.

---

### Post by @tromp ⭐ (2020-07-09)
*Post #72*

johndavies24:

> not at all similar to a spent output that is already on chain

It is quite similar. In both cases the wallet recognizes a utxo as its own, but without any further action from the wallet, this utxo can become spent on-chain.

The only distinction is that one is a play, and the other a re-play.

In neither case can the output be included in the wallet balance.

In both cases, the wallet may need to sweep the output to get it back into its balance.

---

### Post by @tromp ⭐ (2020-07-09)
*Post #75*

johndavies24:

> tromp:
>
>> It is quite similar. In both cases the wallet recognizes a utxo as its own, but without any further action from the wallet, this utxo can become spent on-chain.
>
> In one case the balance is considered “awaiting to be finalized” and in grin-wallet is not reflected in the bottom line (total balance) and cannot be used or spent in any way. The wallet simply marks as spent (or awaiting finalization on receiver end) to make sure it doesnt accidentally try to use them in a subsequent transaction.

That is in complete agreement with what I said above.

> In the other case, it is on chain and can be used and spent.

The other case being a re-created utxo that the wallet spent in the past. Which cannot be safely used, as it is subject to replay of the former spend.

---

### Post by @tromp ⭐ (2020-07-13)
*Post #102*

johndavies24:

>   1. Current UTXOs are possibly susceptible to replay attack
>

>   * This can be addressed with a full wallet history.
>  ** One solution is to sweep (or self spend) at risk UTXOs. This is a privacy concern by linking your UTXOs and opens the door for an attack that encourages users to link their UTXOs
>

Wrong; they would be swept individually, separated in time.

> ** Another solution is to ignore these at risk UTXOs. This is effectively burning coins and preventing users from access to value that they otherwise have the potential to control
>  ** A third solution is to spend as fees, which seems to discourage the attack, but still has users lose access to value they would otherwise have the potential to control.

One should design for simplicity, not for profit from situations that are unlikely to ever happen. The burning helps makes to make it even more unlikely.

>   * One issue is how to identify these upon wallet restore or in the situation of multiple wallet instances running on the same seed
>  ** Tromp suggested sweeping all outputs created since last restore.
>

No; not since last restore. Since the last time the wallet reported clean status (no outputs in limbo).

> It also doesnt take into account that some users will have multiple instances running simultaneously, so D.O.A.

It does take those into account. Outputs created by e.g. child wallets appear in limbo, until the user declares them safe.

> There have been at least two consensus solutions provided. One by Kurt and one that is live on the beam blockchain that solve all of the issues trivially.

It still allows play attacks in a limited time window.

> payment channels require constant monitoring anyway,
>  so your wallet would have to be online to protect you from funds being stolen.
>  If necessary, some kind of renegotiation powers could be provided to watch towers.

Watch towers don’t have the necessary keys, so this would be slightly awkward.

> **To date, there has been no solution provided that successfully provides security against replay attacks besides a consensus change as no solution addresses all previously spent outputs.**

Sure; if you disqualify valid solutions for having worse UX, and ignore limited window attacks on expiring txs.

---



## BEAM price higher than GRIN today
*Date: 2020-06-13 | [Forum Link](https://forum.grin.mw/t/beam-price-higher-than-grin-today/7424)*
*Importance Score: 140.8 | Core Participants: david, davidtavarez*

### Post by @ken19983 (2020-06-13)
*Post #1*

It’s happened. Beamppening

GRIN is officially worth LESS than BEAM today. First time it ever happened (that I’m aware of).

I remember the big splash when GRIN first launched in early 2019. It was several times more valuable (per coin) than BEAM. I recall Jan 2019, GRIN started out at about $10 per coin. I was one of the earliest GRIN miners with several hundred GTX 1070ti’s mining GRIN running GMiner. BEAM started out a couple weeks before at about $0.60 per coin. I had no interest in mining BEAM. GRIN was the star, not BEAM.

If you had told me 18 months later this is where we’d be today, I’d think you’d be nuts. GRIN, with an estimated $100M in venture capital invested in all sorts of mining infrastructure and all this goodwill and media attention – worth less than BEAM 18 months later? If you had told me that BEAM, not GRIN, would be the coin listed on Binance, I’d tell you to keep dreaming.

But yet, here we are.

---

### Post by @david ⭐ (2020-06-15)
*Post #125*

Pirat:

> That’s why I wrote that developers need to check these unofficial wallets, because they are bug

Most issues are related to tor, or are problems on the exchange side, which use the official wallet. An official GUI wouldn’t change anything. I really don’t understand why people think that would solve anything.

The difficulty with grin is due to interactivity requirements, not due to any specific GUI or lack thereof. Interactive transactions in their current form are fragile and complicated to support.

---

### Post by @david ⭐ (2020-06-17)
*Post #151*

markov:

> For Niffler and Grin++, the user experience is even less friendly than the Bitcoin wallet back to 2010!

What doesn’t work for you? Any suggestions for how we can improve?

There is nothing about an “Official wallet” that suggests it will be any easier to use.

---

### Post by @davidtavarez ⭐ (2020-06-18)
*Post #154*

you first said this

markov:

> the user experience is even less friendly than the Bitcoin wallet back to 2010

and now

markov:

> Grin++: I never start it successfully.

These are two different things… anyways feel free to Join the Telegram channel and ask for help: [Telegram: Contact @GrinPP](https://t.me/GrinPP)

---

### Post by @david ⭐ (2020-06-18)
*Post #155*

Grin++ uses a permanent address. It probably won’t start because Niffler leaves the node running in the background, which conflicts with the grin++ node. Kill the Grin process and try opening Grin++.

---

### Post by @davidtavarez ⭐ (2020-06-18)
*Post #159*

markov:

> The wallet should start and solve this problem

I don’t think you want a third party application killing and starting process… but, if you’re using Windows, I am pretty sure that your Antivirus will put this third party application in Quarantine.

markov:

> Grin++ and Niffler can solve it by communication with each other

Again…

If someone wants to say: “this app is not user friendly”, that person should run the app first, I guess…

---

### Post by @david ⭐ (2020-06-18)
*Post #164*

markov:

> And to be honest, I am an experienced developer working in developing scientific computing software.

Great, so it should be easy for me to explain what’s going on. Imagine running bitcoin core, and also trying to run libbitcoin on the same machine at the same time. That’s 2 different nodes trying to use the same ports, same peers, etc. so only one of them will succeed.

Niffler has chosen to leave the grin process (ie their node) running in the background. Because of this, Grin++ is not able to start its node on the same ports, using the same peers, etc. Now, we could automatically kill any process that’s using those ports, but that feels like the wrong decision to make. It runs the risk of corrupting the data of another program. So we decide to fail gracefully instead. For sure, we should improve that error message to indicate to the user what the issue is. I take full responsibility for the poor choice of wording, and will think of better ways to inform the user of the problem. Suggestions welcome.

markov:

> And where can I find the permanent address? In which wallet or the official command line tool? Can I provide it to any Exchange to withdraw my Grin there?

Grin++ always uses a tor address generated from your wallet seed. It’s the same address every single time. It also provides an http address based on that tor address that also never changes. You may use that http address on any exchange that supports http(s), which is the majority of them. For the few that don’t, they support send by file instead. Grin++ supports that as well.

markov:

> No interest to try it again.

Sorry to hear this. I do hope you’ll change your mind. If you do, we’re always happy to help with any Grin++ issues at [Telegram: Contact @GrinPP](https://t.me/GrinPP)

Thanks for the feedback, and don’t hesitate to reach out to me directly if you have any other advice for how we can further improve.

---

### Post by @david ⭐ (2020-06-18)
*Post #166*

markov:

> I do think the Grin community should work out one and only one Official Wallet

Do you think bitcoin should do the same? There are currently dozens of bitcoin wallets out there, and bitcoin core is actually one of the least user friendly btc wallets. Part of the reason bitcoin wallets are more stable in general is because they’re much more mature. Bitcoin is 11 years old. Grin is 18 months old. But their protocol also doesn’t require users to work together in order to build a transaction, which is a whole additional layer of complexity that grin wallet devs have to struggle with. Building a grin wallet is difficult.

Making the situation even more difficult, grin is being developed largely by volunteers with no expectation of profit. Some of us spend a lot of time working on this stuff, but it’s hard to compete with the thousands of VC-funded alts out there who exist to profit off of you. It understandably takes us longer. But I agree, that’s incredibly frustrating from a user’s perspective. It’s the unfortunate price we have to pay for a fair launch. There is no dev fee or premine to fund development.

But because of the lack of funding, there’s no reason to think having one “official” wallet will be any better. In fact, I’m willing to bet it would be much worse, because there’s nobody to actually build this official wallet. The core team has protocol developers, not GUI app developers. And we can’t exactly hire a team of UX designers and front-end developers to build it. The council would be broke within a year, and the protocol development - the thing that actually separates us from other coins - would suffer as a result.

In short, I hear you. It’s frustrating, indeed. But we’re doing the best we can given the limitations, and we appreciate all of the feedback you and many others have been providing.

---



## Efficient solution to verify kernel uniqueness + better absolute timelocks
*Date: 2020-07-09 | [Forum Link](https://forum.grin.mw/t/efficient-solution-to-verify-kernel-uniqueness-better-absolute-timelocks/7526)*
*Importance Score: 90.8 | Core Participants: david, tromp, antioch, quentinlesceller*

### Post by @Kurt (2020-07-09)
*Post #1*

If this is the retained choice with respect to the replay attacks (who knows! maybe we will respect users) here is a proposed solution.

PROTOCOL:

1. Two users want to make a transaction.
2. They look at the current block height of the Grin blockchain, represented by the integer `signature_block_height`.
3. They sign the transaction with `signature_block_height` in the signature’s message of the kernel excess.
4. Similarly to kernel offset, they join `signature_block_height` with their transaction (of course, unlike kernel offset, `signature_block_height` is not to be aggregated).
5. Transaction enjoys some time in the mempool up to `inclusion_block_height`, where `inclusion_block_height` is the block at which the miner includes the kernel in the blockchain (precisely, he includes it in the kernel MMR).

* * *

Instead of having its leaves on `(kernel)`, the kernel MMR has its leaves on `(kernel, relative_height)`. Kernels are still comprised of excess and signature only. `signature_block_height` is _not_ included in Kernel and is _not_ onchain data (but just mempool data).

* * *

6. Miner includes the kernel into the kernel MMR through the leaf `(Kernel, relative_height)` where `relative_height = inclusion_block_height - signature_block_height`.
7. Finished.

Protocol rules:
(i) Grin protocol rules has to set a maximum value allowed for `relative_height`, for example call it `relative_max`.
(ii) kernel verification rule: Each couple `(kernel, relative_height)` corresponds to a unique `inclusion_block_height` (visible by verifiers) and is valid (protocol rule) if and only if the signature for the kernel excess is correct for the message `inclusion_block_height - relative_height`.

This protocol allows:
(a) Verifiers to verify signatures easily since they directly derive the message of the signature in the leaf of Kernel MMR:
`message = signature_block_height = inclusion_block_height - relative_height`.
(b) Verifiers to verify efficiently kernel uniqueness on the whole blockchain without the need to keep all the history in memory but a very short history instead; all the kernels belonging to blocks older than `current_block_height - relative_max` can be forever removed of uniqueness check, where `current_block_height` is the current block height (most recent block on the blockchain).

The method doesn’t change the current composition of a kernel, and stores relative heights rather than absolute heights. Scalability and protocol elegance blows are essentially negligible.

_More on scalability of the construction, absolute time locks as side effect, and security are discussed in posts below._

---

### Post by @antioch ⭐ (2020-07-14)
*Post #10*

Nobody said it was an absurd concept. But it is undesirable. We aim to maintain the rule that a “transaction (with spendable outputs) once valid will not become invalid”.

It is not the size of the window that is undesirable here, but the existence of the window itself.

I understand your disagreement here and I understand your desire to solve the “replay attack” at the consensus level like this with kernel uniqueness.
But my feeling here is the downsides outweigh the benefits and this is not the solution.

---

### Post by @david ⭐ (2020-07-14)
*Post #14*

antioch:

> We aim to maintain the rule that a “transaction (with spendable outputs) once valid will not become invalid”.

If a transaction doesn’t confirm in a week or so, I think most of us would rather it expire. Otherwise it’s like writing a check and not knowing when it will be cashed. Having inputs stuck in limbo for months is strange.

---

### Post by @antioch ⭐ (2020-07-16)
*Post #19*

[@tromp](/u/tromp) has a good explanation of one approach (NRD kernel based) for payment channel revocation here - [Fwd: Relative Locktimes in Grin : Mailing list archive : mimblewimble team in Launchpad](https://lists.launchpad.net/mimblewimble/msg00636.html)

Andrew is talking about how they approach it today in Bitcoin/LN with penalty txs. The approach in Grin is a little different as we can cannot put locktimes on outputs themselves, only on the kernels.

The window between two NRD kernels provides the relative locktime necessary for this to work.
Within the window the _other_ tx can be used to revoke the channel close. Once the lock expires outside this window the tx containing the NRD kernel can be broadcast to complete the channel close.

* * *

Kurt:

> It honestly seems like pure trolling to me and it is time consuming.

We can disagree on approaches. Maybe take a step back if debate around your proposal feels like trolling.

Kurt:

> Time to go back to Earth at some point for grin.

That comment adds nothing to the conversation.

---

### Post by @david ⭐ (2020-07-16)
*Post #23*

mably:

> I personally think we are not in a hurry of anything and we should take all the time needed to reach a global consensus on that particular subject.

We absolutely are in a hurry to fix an attack that could allow theft of funds, especially considering that the last fork is approaching quickly, so if consensus changes are necessary, now is the time to do that.

---

### Post by @antioch ⭐ (2020-07-16)
*Post #34*

johndavies24:

> When you live in a glass house, dont throw stones. “Core gets veto rights” and “cool” sound familiar to you? You epiptomize what many have complained about the core. Your attitude is horrible and you have no interest in “team”, “community” or fairness.

Just to clarify - I apologized to you directly on keybase regarding my “core gets veto rights” comment, which was in bad taste. You then accepted my apology in keybase. And _then_ you come over into the forum and bring it up again, implying I am still at fault over this?

---

### Post by @antioch ⭐ (2020-07-16)
*Post #37*

Anynomous:

> So again, please give some more concrete examples so we can understand better the weight given to monoticity by you and others in this discussion and why it trumps giving scalability priority?

I don’t believe tx monotonicity and scalability are mutually exclusive. I’m definitely not trying to prioritize anything over scalability here.

I would like to retain our current behavior in terms of storing kernels - i.e. _not_ to add any additional requirements around storing kernels or indexing kernels. All nodes must validate all kernels during IBD but beyond that, some nodes could in theory discard historical kernels. Nodes only keep historical kernels to provide them to other nodes during IBD.

It sounds like maybe you think I am pushing for additional requirements around kernels? It’s the opposite - I don’t want to store or index them beyond what is absolutely necessary.

Tx monotonicity is around simplifying the mempool logic and avoiding spam, specifically transactions that may never actually be accepted on-chain. We can achieve this with the current kernel requirements.

I don’t think we need to verify kernel uniqueness. I think there are alternative approaches that we can take. And if we do not need to verify uniqueness we can avoid needing to index them.

---

### Post by @tromp ⭐ (2020-07-16)
*Post #39*

antioch:

> It sounds like maybe you think I am pushing for additional requirements around kernels? It’s the opposite - I don’t want to store or index them beyond what is absolutely necessary.

And for good reason!

In the future, we may augment (not replace) a long history of kernels with a concise zero knowledge proof of their validity, which would make Grin even more scalable for people who trust that technology.

---



## Play Attacks and possible mitigations
*Date: 2020-07-10 | [Forum Link](https://forum.grin.mw/t/play-attacks-and-possible-mitigations/7527)*
*Importance Score: 82.1 | Core Participants: david, antioch, davidtavarez, tromp, lehnberg*

### Post by @tromp ⭐ (2020-07-10)
*Post #1*

In the other thread on “Replay Attacks and possible mitigations”, I introduced the following attack scenario:

Bob requests a payment from Alice, using the invoice workflow.
This means that Alice is the first to sign for the tx. She sends her signature to Bob, but Bob doesn’t complete the tx, and either becomes unresponsive or gives some excuse for why his wallet couldn’t complete the tx.

Alice cancels the tx, and the amount re-appears in her balance.

Then some years later, after Alice had to restore her wallet, one day she suddenly see her balance decrease. She has no memory of the canceled tx to Bob. But Bob did remember…

Th cause of the above attack is that currently, the wallet cancels a tx by merely forgetting about it and returning the amount to the balance.
It fails to prevent a future replay of the tx. Which is not even a replay because the original tx never hit the chain.
This problem cannot be solved by any kind of kernel uniqueness.

We can mitigate this scenario by having the wallet put an output that it signed for to be spent in a “limbo” state, to indicate that it no longer has exclusive control over its spending. Limbo outputs do not contribute to a wallet’s balance. It would normally remain in this limbo state until the tx confirms on-chain.

Now when Alice cancels the tx, the wallet should take the input(s) out of limbo state by spending them back to herself, i.e. “sweeping” them.
Only once the sweep confirms, can the amount be included in her balance again.

[1] "[Replay Attacks and possible mitigations](https://forum.grin.mw/t/replay-attacks-and-possible-mitigations/7415)

---

### Post by @tromp ⭐ (2020-07-14)
*Post #16*

Kurt:

> We have everything to make grin nice with clean and simple and elegant solutions. instead this mental jerking with wallet tweaks has been going on for quite long time now. Its an attack on grin basically.
>  How can we tolerate to make this coin with one of the worst security and user exp in the industry? Do it if you want. I would be sad that this is the final choice, and doubtful about your intentions on Grin.

Not only are you completely mischaracterizing the pros and cons of the mitigations, but you have to use insulting language as well.

---

### Post by @antioch ⭐ (2020-07-14)
*Post #21*

davidtavarez:

> it feels like your solution transfers the responsibility to users and relies on wallet tweaks, and it’s really hard to engage with that.

I’m not sure its entirely fair to categorize healthy output/transaction management at the wallet level as “wallet tweaks”.

Grin/MW transaction building is inherently interactive. We should embrace this and take advantage of this where we can. The concept of “locking” outputs (aka outputs in “limbo”) once they are known to have participated in an interactive transaction building protocol is potentially a very clean solution to this “play” problem.

With a good wallet UX this does not shift responsibility onto the user. It does put additional responsibility on the wallet implementation but interactive transaction building effectively requires this responsibility regardless.

Once an output is in “limbo” it can be spent by the associated transaction, now or in the future (unless spent by another transaction). The _only_ way to mitigate this would be to spend by another transaction.

This is true for Bitcoin also. But in bitcoin the number of participants in possession of the (unbroadcast) transaction is reduced because transaction building is not interactive.

---

### Post by @antioch ⭐ (2020-07-14)
*Post #25*

Consider Bitcoin.

I create a simple transaction that spends a single output and creates a single output.
Rather than broadcasting this transaction I give the transaction to another party.
What can I do to prevent a future “play” attack from occurring on this, as yet, unspent output?

As far as I understand, this is the simplest demonstration of a “play attack”.
It is not specific to Grin. What is specific in the Grin case is the likelihood of the other party having possession of the un-broadcast transaction.

The _only_ way to mitigate this is to spend the at risk output with another transaction.

---

### Post by @antioch ⭐ (2020-07-14)
*Post #29*

Ok yes that makes sense.

So without tx expiry you would be at risk indefinitely and would want to mitigate by spending.
With tx expiry you are at risk for a limited period of time after which the tx would expire. But during this window you would may still want to mitigate by spending, rather than risk waiting for expiration.

So tx expiration limits the time you are at risk, but you are still at risk during this window.

---

### Post by @antioch ⭐ (2020-07-14)
*Post #38*

I’m not sure what you are arguing here. The “risk” is that an output gets spent at some time in the future.

1. Tx built “spending” output A.
2. Tx broadcast to network.
3. Tx included in a block and confirmed on-chain.

Between (1) and (2) the output A is effectively an unknown state.
The blockchain cannot resolve any dispute until (3) occurs, possibly preceded by (2).

Between (1) and (2) you cannot know with any certainty what will happen to A.
I am using the term “at risk” here, specifically in the scenario where the recipient says they will not broadcast the tx (they claim they lost it, but maybe they lied).

To mitigate this risk and reclaim output A you can spend it, assuming the new tx is broadcast and accepted in a block before the original tx.
If A is spent to produce a new output B and no transaction is known to exist that can spend B then B is in a known state.

---

### Post by @antioch ⭐ (2020-07-14)
*Post #44*

Kurt:

>   1. Receiver never learns partial offset of sender during tx process.
>

Kurt:

> Please give concrete example of such case when 1 2 and 3 are implemented. Like precise.

Rather than a concrete example of how this is still broken if 1, 2 and 3 are implemented let me try and illustrate why (1) above is not possible in the general case (only possible if there is a single “sender”).

* Let us define a “sender” as a participant in the transaction who contributes one or more inputs to the transaction.
* The transaction involves `s` participants who contribute inputs (senders).
* At the end of the interactive transaction building process, one single participant will have possession of the finalized transaction. This participant can choose to withhold the transaction, refusing to broadcast it to the network.
* If `s > 1` then by definition we have at least 1 “sender” who contributed inputs to the transaction but with no ability to broadcast the transaction. Their output is “spent” in the context of their wallet but they do not know when (or if ever) it will be accepted and confirmed on-chain.

Given this, it is impossible to guarantee (1) “Receiver never learns partial offset of sender during tx process.” replacing “Receiver” with “participant in possession of final transaction” in the general case.

Kurt:

> I explained to you in the post above why your autority argument for several senders is totally wrong. Please stop using autority argument it becomes super annoying and alienating.

Kurt:

> Nobody learned the partial offsets of any other parties, making the transaction at NO risk of replay.
>
> Again, please, for the love of God, Jesus and Mary, or TEJ, please back your claims with precise technical content. It would be super helpful.

The partial offsets are not the issue here. The problem is related to who is in possession of the finalized transaction (and has sole discretion over broadcasting it or withholding it).

Kurt:

> Computer dying in the middle of tx is not a risk if 1. and 2., very simple rules, are followed. You are literally imagining stuff rather than using reasoning.
>
> To be clear, what you said above is totally false.

Do you disagree that possession (and withholding) of the finalized transaction is the problem here?
It is irrelevant whether participants see the partial offsets of other participants, possession of the finalized transaction is sufficient.

---

### Post by @david ⭐ (2020-07-15)
*Post #47*

Here’s my proposal for preventing “Play attacks” in the invoice workflow:

Stop supporting a special workflow for invoices. Instead, an invoice should just simply be a file/blob/json/whatever (like a BIP70 PaymentRequest) that indicates the receiver address, amount owed, and potentially a message of some sort. Then, accepting (ie. paying) the invoice should just follow the normal send workflow. Then, the sender is always the one who sees the final transaction, and is responsible for broadcasting it. Failure to broadcast means the invoice is unpaid.

---



## Unique kernels without transaction expiry
*Date: 2020-07-24 | [Forum Link](https://forum.grin.mw/t/unique-kernels-without-transaction-expiry/7576)*
*Importance Score: 89.2 | Core Participants: david, tromp, antioch, lehnberg*

### Post by @Kurt (2020-07-24)
*Post #1*

Following the hot discussions on play and replay attacks, I did a small paper which summarizes my technical investigation and understanding of the concept of unique kernels. I hope that the document can help people in the community interested and open to the different solutions that we have in hand, to comprehend more the properties of unique kernels and their usefulness to fix the vulnerabilities. I have in particular introduced in the doc, as the title suggests, a quite scalable and simple proposal that allows to check uniqueness of the kernels without the need to enforce expiry on them.

The paper contains:

* Link of kernel uniqueness with the available fixes for play attacks

* Description of the kernel expiry proposal

* Security study of the kernel expiry proposal, including the DOS attack vectors that may be introduced by it

* Presentation of the proposal without kernel expiry, whose main ideas are based upon the kernel expiry construction

* Pseudo code of an algorithm checking kernel uniqueness in the non expiring proposal

* Pros and cons of the proposals

The document might be considered a bit long to read, in particular for community members that have not yet studied Mimblewimble closely, but I thought it was important to give the most details as possible. And I hope the content is mostly clear at least. Feedbacks or questions are welcomed.

pdf available at keybase://public/kurt3/kerun.pdf

---

### Post by @antioch ⭐ (2020-07-24)
*Post #2*

[@Kurt](/u/kurt) Thanks for writing this up. This looks to be a very comprehensive overview of what would be required to support unique kernels.

Am I right in thinking that the idea here is to effectively “cache” and index recent history, allowing fast uniqueness checks against a window of recent kernels?
And then if no duplicate was found, only then fall back to looking through the full history?

Recent history allows you to verify the _existence_ of a duplicate (similar to what we do for NRD) but cannot verify _non-existence_ of a duplicate kernel. So for every lookup in the recent history that did not find a duplicate you still need to go back a look over the full kernel history?

---

### Post by @lehnberg ⭐ (2020-07-24)
*Post #7*

bluimes:

> With the disclaimer of me not knowing all the specific technical specs I can tell this is without a doubt a seriously well written proposal. One that stands above and beyond the rest. Much respect for this work and commitment Kurt .

Yes to all of the above, this is a great addition to the discussion, kudos to [@Kurt](/u/kurt) for taking the time to put it together.

bluimes:

> Now can we live stream the emergency consultation of the council?

Fortunately, there doesn’t seem to be an emergency. It’s a shame we didn’t have this doc when [when the topic was discussed in Tuesday’s dev meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20200721-meeting-development.md#55--expiring-kernels-ek), would have been really useful.

But since we have it now, let’s add to the agenda for next meeting. By then there might have been more feedback to the proposal, and we could have a more informed discussion than what we had Tuesday. Hopefully [@Kurt](/u/kurt) will be able to join as well.

All in all, a positive development!

---

### Post by @lehnberg ⭐ (2020-07-24)
*Post #12*

For what it’s worth, I just read through the document in detail, and it reads _much_ clearer than these long winded forum posts debates that we’ve been seeing.*

Thank you again for writing it, and I personally now understand your proposal much better. The structure and format was really helpful. For example, it wasn’t clear to me until now that you had two proposals for replay attacks, one with kernel expiry and one without.

From the paper, I draw the conclusion that you prefer the non-expiring proposal, as it doesn’t have the DOS vector. Is that right?

Is the requirement around allowing Duplicate Outputs (DO) only to counter Play attacks, or is it needed for replay attacks as well? What are the downsides with allowing duplicate outputs in the mempool and elsewhere?

* * *

[*] that I wouldn’t want this thread to end up in either, so let’s try to stay on topic!

---

### Post by @lehnberg ⭐ (2020-07-24)
*Post #16*

Kurt:

> It is someone who I spoke to in dm two days ago about my proposal that told me about the second DOS vulnerability in case using kernek expiry. so kudos to him. Not sure if it was known by other people?

Yes, we brought it up in the dev meeting. Meeting notes: <https://github.com/mimblewimble/grin-pm/blob/master/notes/20200721-meeting-development.md#55--expiring-kernels-ek>

---

### Post by @antioch ⭐ (2020-07-24)
*Post #18*

> Scalability: Around 99% of the time, it is useful to note that inclusion block height = signature block height

This is unlikely to be true given inherent latency in transaction relay, specifically the stem phase during Dandelion. Transactions tend to be included several blocks later than their creation time.

* * *

One important thing to add here is this would impact transaction verification in some important ways.

We can currently validate the kernel signature in isolation.
i.e. Signatures can be validated without reference to any on-chain data. The message being signed is included fully in the kernel itself.

The approach here introduces a dependency on external data.
Verifiers must derive signature height based on inclusion height which in turn relies on both the block header and the kernel MMR. For historical kernels we need to determine which block the headers correspond to based on kernel_mmr_size of the header.

This can be done, but it does affect the simplicity (and performance) of the current kernel signature validation, where we simply batch validate signatures based on the associated kernel data.

---

### Post by @antioch ⭐ (2020-07-24)
*Post #20*

Kurt:

> Did you read the document ?

Don’t forget about historical validators though. Not everyone sees the transactions themselves.

---

### Post by @david ⭐ (2020-07-24)
*Post #28*

Kurt:

> I dont know yet if the second DOS vulnerability for kernel expiry proposal is fixable

Here’s the second DoS vulnerability:

The described “attack” ignores the fact that there will be a dynamic fee market when blocks are full. Transactions don’t just pour in at a steady rate with a constant fee. Instead, the ebb and flow of demand will result in the following 2 possibilities:

1. Demand for blockspace increases, driving fees higher, and pushing the “attacker’s” transactions out of the mempool (we prioritize by fee, among other things).
2. Demand for blockspace decreases, driving fees lower, and resulting in the confirmation of the “attacker’s” transactions, costing them the transaction fees.

The risk here of financial loss is simply too high, with no financial benefit for the attacker. However, if you’re still concerned, there’s always additional criteria we could add to the mempool. A well designed mempool should only ever accept txs that it reasonably expects to include in a block, anyway.

---



## Eliminating finalize step
*Date: 2020-08-02 | [Forum Link](https://forum.grin.mw/t/eliminating-finalize-step/7621)*
*Importance Score: 142.7 | Core Participants: david, antioch, davidtavarez, tromp, lehnberg*

### Post by @david ⭐ (2020-08-02)
*Post #1*

Currently, grin transactions are created using the following 3 (simplified) steps:

1. Send - Sender commits to amount, fee, and a public nonce, public excess. It could also commit to tx offset, inputs, change output, and probably others.
2. Receive - The receiver adds their output & rangeproof, and commits to their public nonce and excess. It then updates the total kernel commitment, and signs for their half of the kernel.
3. Finalize - The sender adds their half of the signature, aggregates the 2 partial signatures, and builds the final transaction.

The sender can’t just include their part of the signature as part of the send step, because it doesn’t yet know the receiver’s public nonce and public excess. _But what if it did?_

Grin now has slatepack addresses, which are just encoded ed25519 public keys. If we extended these to include a secp256k1 public key, then we could treat those addresses as BIP32 parent public keys, and the sender could generate the public nonce and public excess for the receiver, and just inform them of which keychain path they used to generate the public keys.

In fact, the sender could generate everything about the transaction except the bulletproof and the receiver’s half of the signature. Then they could just pass that to the receiver, who just adds their half of the signature, and appends a bulletproof to their output. The transaction is complete - no finalize step necessary!

This is a pretty radical change that would require rethinking nearly everything about the wallet: Play & replay attacks, payment proofs, invoices, etc. But I believe these are all solvable, and will propose solutions for these later, if there’s enough interest in this idea.

---

### Post by @david ⭐ (2020-08-02)
*Post #9*

[@Paouky](/u/paouky) The general idea is simple. For elliptic curves, private keys are scalars and pubkey are points generated by multiplying the private key by a common generator point (G).

If I have 2 private keys, s1 and s2, I can generate public key P1=s1 _G, and public key P2=s2_ G. It just so happens that if I add P1+P2=P3, that’s the same as if I add s1 and s2=s3 and multiply times the generator (s3*G=P3) . So:

(s1+s2) _G = (s1_ G) +(s2*G) = P1+P2 = P3

child keys are a bit more complex, but just to show you how I can generate a pubkey from your pubkey `P`=`s*G`, I can just generate a random secret key `s'`, and add `s'*G` to your pubkey `P` to get `P'`. Then give you `s'`, which you can add to your original secret key `s`. The result is the private key for `P'`, and only you know that private key.

(Typed on mobile while holding kid - sorry for mistakes)

---

### Post by @david ⭐ (2020-08-03)
*Post #14*

tromp:

> In the case where the sender needs no change output, this doesn’t seem too different from just sharing the blinding factor with the receiver

How so? The receiver never learns the blinding factor.

---

### Post by @lehnberg ⭐ (2020-08-09)
*Post #55*

Macker:

> Any news on this? Sounds like it may be possible. As far as user experience goes, it would make a huge difference!

Agreed, seems promising! I’m having a hard time understanding what the latest and greatest of this proposal is, there’s already ~50 replies in thread.

Would be great we could have a summary / overview of the most up to date proposal, for example:

1. List of currently known use cases. If we do this, how will tx-building become better? What additional things could be possible, how will UX become simpler, etc.
2. One paragraph overview of what changes are being proposed.
3. List of technical changes:
* New tx-building flow
* How is invoice flow handled
* How are payment proofs handled
* Any consensus related change?
* Any pre-requisites?
* any other related spec topic
4. Known issues / open questions. What’s still left to figure out?
5. Trade-offs. Any reasons **not** to do this? What are the costs?

I’m happy to assist and try to keep the list up to date, but don’t think I’m knowledgeable enough to take the lead on it. [@david](/u/david) would you be willing to help me?

---

### Post by @david ⭐ (2020-08-10)
*Post #64*

lehnberg:

> I got a bit bummed out by the one-time address requirement however,

Me too! It feels unavoidable, but I’m still looking for a clever solution.

---

### Post by @antioch ⭐ (2020-08-25)
*Post #76*

Cross-posting a comment I posted earlier on the github RFC here for reference -

[github.com/mimblewimble/grin-rfcs](https://github.com/mimblewimble/grin-rfcs/pull/59#issuecomment-679970246)

####  Comment by [ antiochp ](https://github.com/antiochp) to [WIP: Creating 'Eliminating finalize' RFC](https://github.com/mimblewimble/grin-rfcs/pull/59#issuecomment-679970246)

`mimblewimble:master` ← `DavidBurkett:eliminate_finalize`

The other thing that bugs me here is this proposal effectively pre-shares the pu[…](https://github.com/mimblewimble/grin-rfcs/pull/59)blic nonce prior to the message being committed to. There is not a lot of freedom in the message as we only include the features, the fee and potentially lock height, but there is _some_ freedom. So if the recipient publishes their public nonce, is the sender now able to potentially bias the message by choosing different fee and lock_height values? And in turn bias the hash function? See "Pre-shared nonces in MuSig" here - https://medium.com/blockstream/insecure-shortcuts-in-musig-2ad0d38a97da I honestly don't know if this is an issue with this approach - but something we should understand.

Edit: Not sure why its not linking directly to the comment.

> The other thing that bugs me here is this proposal effectively pre-shares the public nonce prior to the message being committed to. There is not a lot of freedom in the message as we only include the features, the fee and potentially lock height, but there is _some_ freedom.
>  So if the recipient publishes their public nonce, is the sender now able to potentially bias the message by choosing different fee and lock_height values? And in turn bias the hash function?

See “Pre-shared nonces in MuSig” here -

[Medium – 19 Nov 19](https://medium.com/blockstream/insecure-shortcuts-in-musig-2ad0d38a97da "09:21PM - 19 November 2019")

### [Insecure Shortcuts in MuSig](https://medium.com/blockstream/insecure-shortcuts-in-musig-2ad0d38a97da)

How (not) to reduce the communication complexity in BIP-schnorr-based multisignatures

Reading time: 7 min read

**tl;dr** Sharing the public nonce prior to committing to the message to be signed may be a bad idea.

I honestly don’t know if this is an issue with this approach - but something we should understand.

---

### Post by @david ⭐ (2020-09-09)
*Post #91*

antioch:

> **tl;dr** Sharing the public nonce prior to committing to the message to be signed may be a bad idea.

So, sharing the nonce is not a problem, but it turns out, the scheme where we no longer commit to pub excess in the challenge string actually _is_ vulnerable to Wagner’s attack after all. A huge thanks to Beam’s Vlad Gelfer for working this out. I’ll describe the attack now.

The proposed (insecure) signature scheme:
`k` = nonce, `k*G` = pub nonce
`r` = excess, `r*G` = pub excess
`M` = message
`e` = `Hash(M | k*G)`
`s` = `k + e*r`
Signature = (`k*G`, `s`)

The attack:
Rather than using `k*G` as the pubnonce, the attacker generates another random number, `x`, and uses `k*G + x*H` as the pub nonce. Then, he can calculate a pub excess after performing the challenge as:
pub excess = `r*G - x*(e^-1)*H`. He now just built a valid signature which, in addition to the excess (`r`), also has a value `x*(e^-1)`.

This is still not trivial to perform in mimblewimble, since in order to build outputs with the value of `x*(e^-1)`, the value has to fit in 64-ish bits to build a bulletproof (actually, closer to 70, because you could build say 1,000 outputs). But as it turns out, you can sum multiple kernels together so that the sum of their `x*(e^-1)` only has to total 70-ish bits, which Wagner’s attack tells us is much easier. Performing this attack results in undetected inflation

Solution:
Left as an exercise for the reader.

---

### Post by @tromp ⭐ (2020-09-10)
*Post #95*

I think the references assume a known public key X that can sign different messages, not an ephemeral X that is dependent on the nonce in a single signature.

The problem is that Grin public excesses are rather ephemeral…

Wikipedia is also a little sloppy in not explaining what exactly should be included in the hash of the Fiat-Shamir transform. It should be the history of all messages exchanged up to that point in the protocol. Which for Schnorr signatures ought to include the public key X.

---



## Wallet receiving clarification
*Date: 2020-09-02 | [Forum Link](https://forum.grin.mw/t/wallet-receiving-clarification/7785)*
*Importance Score: 73.4 | Core Participants: david, tromp, davidtavarez, lehnberg*

### Post by @aehyao (2020-09-02)
*Post #1*

So is it necessary that my wallet be listening to a specific port to capture any transaction? Like if my wallet isn’t “on” I cannot receive grin? This is confusing to me.

---

### Post by @tromp ⭐ (2020-09-04)
*Post #16*

I like the idea of embracing the unique properties of Mimblewimble, and not adding baggage to try to make it into something it’s not. If we apply the same idea to the question of how to obfuscate the transaction graph, then we might come up with some aggregation services, as an alternative to Dandelion.

You would send your non-urgent transaction (by TOR) to an aggregation service that you trust (e.g. run by the core devs, or by David Burkett), and they would await sufficient aggregation (I think any number significantly larger than 11 would do:-) before being published.

Yes, there is a small risk that the aggregation service is compromised, and your original tx is visible to someone, but this is no worse than the current situation, and the there’s a good chance that the situation will be much better…

---

### Post by @lehnberg ⭐ (2020-09-04)
*Post #17*

I agree. This sounds very similar to [GrinJoin](https://forum.grin.mw/t/yo-dawg-i-heard-you-like-coinjoins/5296/) \- [@David](/u/david) what’s the status of that? Is it in operation currently? Over Tor? Is it opt-in? Do you have any usage stats?

---

### Post by @davidtavarez ⭐ (2020-09-04)
*Post #18*

tromp:

> I like the idea of embracing the unique properties of Mimblewimble, and not adding baggage to try to make it into something it’s not

tromp:

> You would send your non-urgent transaction (by TOR) to an aggregation service that you trust

I don’t disagree on this… but… at the same time, I can’t count how many hours we have invested giving support to Grin++ users from countries like China, because their addresses are not green (= available)… but the Censorship isn’t just in China, also Venezuela, Iran and other countries. Relying on third-party project (Tor) may not be ideal, we don’t know how many 0days are out there or which bridges are compromised by bad actors, also, bypassing censorship is getting harder and harder… but maybe that’s the only option we have right now. I’m pretty sure things are going to be better after the next HF, but also because of the effort [@Paouky](/u/paouky) is doing documenting Grin, I’m expecting more people to get involved in grin soon.

oryhp:

> I’d prefer to actually own a wallet in every meaning of the word.

Me too and I think is really important.

---

### Post by @tromp ⭐ (2020-09-04)
*Post #19*

davidtavarez:

> Relying on third-party project (Tor) may not be ideal

When Tor is not available, some other medium (like Dandelion stem phase) can perhaps be used to send a tx to an aggregation service.

---

### Post by @david ⭐ (2020-09-04)
*Post #22*

lehnberg:

> Is it in operation currently? Over Tor? Is it opt-in? Do you have any usage stats?

I killed the server. People are still struggling with basic transacting, so I didn’t like the idea of adding another obstacle to getting transactions confirmed.

When it was operational, it was opt-in and over tor. Usage wasn’t enough to make it worthwhile yet. There is less than 1 transaction per minute in Grin, so even if every transaction used GrinJoin, the server would have to wait 15-30 minutes to have any kind of meaningful aggregation.

---

### Post by @tromp ⭐ (2020-09-04)
*Post #24*

tromp:

> await sufficient aggregation (I think any number significantly larger than 11 would do:-) before being published.

The downside of fixed-size aggregation is that it could be effectively (although at some cost) undone by broadcasting lots of dummy transactions around the same time.

Paouky:

> [@david](/u/david) I think the only viable way to do aggregation with current usage is to make aggregation windows of 12 hours, even up to a week

A fixed time window doesn’t suffer that downside. Perhaps it would make sense to have separate hourly, daily, and weekly aggregation servers, to accomodate different tradeoffs between speed and traceability.

---

### Post by @david ⭐ (2020-09-04)
*Post #25*

Yea, only time-based aggregation windows should be used. Fixed-size aggregation requires much higher fees to prevent dummies.

At this point though, running a coinjoin server is little more than an academic exercise. We know coinjoins are possible (in fact, trivial in mimblewimble). And nobody using Grin at these usage levels should expect any level of privacy. The best way to improve privacy right now is through increasing adoption or someone coming up with a clever crypto solution.

Starting up my GrinJoin server just creates more work for me with no practical gain. When we see more adoption, I’ll fire it up again.

---



## Non-interactive txs and usability
*Date: 2020-09-11 | [Forum Link](https://forum.grin.mw/t/non-interactive-txs-and-usability/7818)*
*Importance Score: 91.5 | Core Participants: david, davidtavarez, tromp, antioch*

### Post by @tromp ⭐ (2020-09-11)
*Post #1*

Mimblewimble has the nice property that funds can only be received after proving the ability to spend them. Or as I’ve seen someone say “You can’t lose Grin”.

Bitcoin lacks this property, but users often jump through loops with additional transactions of tiny amounts to try emulate this property and reduce their fear of funds ending up lost.

Non-interactive transactions are a departure from Mimblewimble in giving up this property.

I think the main culprit of current poor usability is the failure of exchanges to support TOR and slatepacks.

With regards to a finalize step being non-intuitive, I would prefer that the we see more use of the invoice workflow, where the three rounds can be called Request, Send, and Receive.
The initial slate sent in request can be accompanied by the wallet address, giving the sender a choice whether to complete the tx over TOR or by sending back a slate over whatever medium was used for the request.

One problem we have with invoice workflow is lack of payment proof, but that can be solved using the techniques of Integrated Payment Proofs.

---

### Post by @antioch ⭐ (2020-09-11)
*Post #4*

MerlinsBeard:

> Suggest, Request, Send, Receive

Note the `Suggest` step does not need to be part of the protocol, it can be “out of band”.
One example might be checking out on an online store. The process of checking out with a given cart would `Suggest` the amount to be paid.
Another example might be a simple “I’d like to donate 100 grin” web form etc.

`Suggest` is simply some mechanism that provides the recipient with an expected amount.

---

### Post by @tromp ⭐ (2020-09-11)
*Post #7*

antioch:

> Another example might be a simple “I’d like to donate 100 grin” web form etc.

The most used example will be entering on an exchange website how much you want to deposit.

---

### Post by @tromp ⭐ (2020-09-11)
*Post #8*

Paouky:

> Not practical for all scenarios. Imagine a medium article with a donation address at the bottom. Or a twitter account with a receiving address. The author can’t use a web form to automatically suggest an amount.

For those situations, where payment proofs are not needed, the non-interactive transactions described in <https://github.com/mimblewimble/grin-rfcs/blob/a2d9f25cdccf29904ef241df5b608ca3fd16ed61/text/0000-onesided.md> should suffice.

---

### Post by @tromp ⭐ (2020-09-11)
*Post #10*

I’m not sure that our current payment proofs are acceptable for the IRS. You probably need some statement from the charity for tax purposes.

---

### Post by @david ⭐ (2020-09-12)
*Post #16*

johndavies24:

> it’s just an expensive way to use the blockchain to store the slate instead of a message relay system.

It’s also insecure (no payment proofs) and requires a fork in order to store the diffie-hellman secret as part of the output.

---

### Post by @tromp ⭐ (2020-09-14)
*Post #22*

david:

> That only gets you up to 1 grin.

Of course not. You’d mostly have milligrin multiples. I bet that covers well over 90% if not 99% of current output values.

---

### Post by @davidtavarez ⭐ (2020-09-25)
*Post #36*

Grundkurs:

> GRIN currently relies on that the participants are online at the same time

My question is: are we not online all the time currently? I think we are and we will be more connected in the future; from that perspective we should simplify Grin as much as possible to have more and more implementations.

Grundkurs:

> Examples:
>
>   1. The Blog-Writer opens up his PC and GRIN-Wallet next morning. He sees a List of 5 transaction-requests that have been made in the night. He just clicks on “approve” and receives the funds.
>   2. The Student arrives finally at collage, opens up his Laptop and GRIN-Wallet and clicks on “accept” and receives the payment of his mom.
>   3. and so forth…
>

I like those examples because we can solve these cases in many different ways.

markov:

> Other coins are all easy to support. Why Grin is so special? What will make exchanges be willing to put more efforts to implement Grin if it is not profitable?

Right now, I’m not buying the idea of “ _Grin**must** do X or Y because **Exchanges** …_” anymore. Exchanges are not our friends, they don’t care if Grin succeed, and they don’t have to care… if they just care about profit then, why should Grin be adapted to them? I think we should make things easier for users by providing Exchanges with tools, we should write a kind of “plug & play” plugin for anyone who wants to integrate Grin, we should have better documentation, we should put more effort on reducing Grin TXs to just 2 steps, and so forth… but **we should never bend the knee to Exchanges**.

---



## Transaction Round Naming Challenge
*Date: 2020-10-10 | [Forum Link](https://forum.grin.mw/t/transaction-round-naming-challenge/7886)*
*Importance Score: 93.6 | Core Participants: david, tromp, antioch, lehnberg*

### Post by @tromp ⭐ (2020-10-10)
*Post #1*

The current wallet uses these round names

send
receive
finalize

for regular (sender-signs-last) flow, and

invoice
pay
finalize

for invoice (receiver-signs-last) flow.
These names are somewhat arbitrary, and finalize has been criticized for not being an obvious necessity.

For invoice flow, the following names are more descriptive:

request-payment
offer-payment
accept-payment

Is is possible to replace “payment” by another word that would be appropriate for regular flow?

I thought “invoice” might work, but hesitate to use that word in the non-invoice flow:-(

How about expense?

Btw, I hope that invoice flow becomes the standard, and reserve regular flow for cases where a high-volume transactor, such as an exchange, insists on being last-to-sign to minimize output locking.

---

### Post by @tromp ⭐ (2020-10-10)
*Post #3*

Grumpy:

> How about the word ‘grin’ instead of payment?

And grinloss (or loss for short) for regular flow?
When senders finalize, they are accepting their loss of grin…

---

### Post by @tromp ⭐ (2020-10-12)
*Post #21*

Yes, I think that would be my favorite too. So this gives

request-pay
offer-pay
accept-pay

for invoice flow, and

request-bill
offer-bill
accept-bill

for “regular” flow (he quotes reflect my hope that invoice flow will actually become the one in regular use:-)
We could allow pay-bill as a synonym for accept-bill.

Btw, although it requires more typing,

request-payment
offer-payment
accept-payment

sound slightly better to me.

---

### Post by @tromp ⭐ (2020-10-12)
*Post #23*

> If I want to send money to somebody, the last thing I’m thinking about is requesting and accepting a bill.

That’s what I do all the time when I eat in a restaurant. I ask for the bill. The waiter offers it to me. And then I accept (pay) it.

antioch:

> Edit: Is “transfer” a possible alternative to “bill” here?

Seems worse, as it doesn’t suggest an outgoing direction of pay.

---

### Post by @tromp ⭐ (2020-10-12)
*Post #25*

antioch:

> If cash is a rough analogy then there is no bill most of the time.

I still ask for the bill if I pay with cash in a resaurant:-)
And I’d be fine if they don’t hand me a piece of paper, but just say “that’ll be 7$ for the pita and icetea”.

Just think of asking for the bill as asking what you should pay them.

Would you be happier with

request-amount-owed

?

---

### Post by @tromp ⭐ (2020-10-12)
*Post #34*

antioch:

> It is confusing to have this based on a **payment** object in the “invoice” flow, yet an **invoice** (or bill) object in the “regular” (aka non-invoice) flow.

Yes, which I alluded to in my original post, saying “I thought “invoice” might work, but hesitate to use that word in the non-invoice flow:-(”

Once we get used to calling them payment-flow and bill-flow, that confusion will hopefully disappear.

---

### Post by @tromp ⭐ (2020-10-12)
*Post #40*

tromp:

> Once we get used to calling them payment-flow and bill-flow, that confusion will hopefully disappear.

Alternatively, we can end all confusion by calling them
receiver-sender-receiver (RSR) flow and
sender-receiver-sender (SRS) flow.

---

### Post by @antioch ⭐ (2020-12-22)
*Post #52*

I wonder how far we can push this?
The difference in the two flows is simply _who_ initiates and what direction funds flow. And I suspect these become even more similar once payjoin is considered.

Once a partial slate is created then it simply becomes a matter of both parties signing in the correct order.

Does the wallet (and user) even need to care about naming of these three steps?
Is this potentially just -

* send (0/2)
* sign (1/2)
* sign (2/2)

* invoice (0/2)
* sign (1/2)
* sign (2/2)

I’m just thinking about how bitcoin multisig is implemented in electrum etc.
You have an unsigned tx (0/2), then partially signed (1/2), then fully signed (2/2) and it can be broadcast (in the case of 2-of-3 multisig for example).

Our wallet knows what state the tx slate is in and knows what needs to be performed (2nd signing step etc.) Maybe these don’t even need names? And the wallet command(s) are more generic?

---



## Grin v5.0.0 network upgrade (Hard Fork 4: January 2021)
*Date: 2020-10-14 | [Forum Link](https://forum.grin.mw/t/grin-v5-0-0-network-upgrade-hard-fork-4-january-2021/7895)*
*Importance Score: 77.5 | Core Participants: tromp, lehnberg*

### Post by @lehnberg ⭐ (2020-10-14)
*Post #1*

_This post will be updated as there is progress, with an announcement in the comments section each time there’s a significant change._

Version 0.3
Dec 11 2020

# Important Block Heights and Dates

Event | Date or Block
---|---
Testnet Hard Fork Block Height | **642_240**
Testnet Hard Fork Date (expected) | 2020-12-08
**Hard Fork Block Height** | **1,048,320**
Hard Fork Date (expected) | 2021-01-15 (est.)

# Summary

As [previously announced](https://forum.grin.mw/t/proof-of-work-update/713), Grin is making network wide upgrades through four scheduled hard forks in the first two years after launch. These are set in the code to occur in rough intervals of 6 months, at every 60*24*7*26 = 262,080 blocks:

* ~~Hard Fork 1: 262,080~~ _Completed successfully_
* ~~Hard Fork 2: 524,160~~ _Completed successfully_
* ~~Hard Fork 3: 786,240~~ _Completed successfully_
* Hard Fork 4: 1,048,320.

**The fourth network upgrade is expected to happen in mid-January 2021**. Compatible versions of grin node and grin-wallet will be versioned **5.0.0** or greater. grin-miner will be unaffected. The first releases of these are scheduled for December.

This post describes breaking changes, timeline and communications that will take place, with the intention that the upgrade goes as smoothly as possible and that ecosystem participants can make the necessary preparations. It will be updated as necessary with additional information once available, so ensure to come back to it regularly.

## Important Information:

* **Grin v5.0.0 is a network wide upgrade**. Apart from updating their binaries in order to use Grin after the upgrade, users are not required to do anything. Stored grins will not be affected. **Beware of scams telling you to move your coins elsewhere.**
* Unlike the previous three network upgrades, **there will be no new secondary PoW algorithm** announced, or new solver provided. The network is now converging to mine the primary Cuckatoo PoW algorithm indefinitely.
* Staying true to the initial commitment before launch, **there are no further hard forks or network upgrades scheduled**. Any future network-wide upgrades will be done ad-hoc through co-ordination in the Grin community.

# Changes

The following is a list of targeted changes. This section will be updated as required.

## Node:

* **Improve transaction fee calculation** , as outlined in [this RFC proposal](https://github.com/tromp/grin-rfcs/blob/fixfees/text/0000-fix-fees.md), still open for comments and improvement suggestions.
* **Improve difficulty adjustment algorithm** , as outlined in [this RFC proposal](https://github.com/tromp/grin-rfcs/blob/fixDAA/text/0000-fix-daa.md), still open for comments and improvement suggestions.
* **(Partial) Parallel IBD:** Preparation for support of an improved process for initial sync and download of blockchain data.

## Wallet:

* **Late locking of outputs:** Removing the need for outputs to be locked during transaction building before the final stage.
* **Remove http listener for external addresses:** As per the deprecation announcement with v4.0.0, remove support for unsecured http listeners in favour of the [slatepack](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0015-slatepack.md) standard.

# Detailed contents & Status

* **For up to date overview:**
* [v5.0.0 planning issue](https://github.com/mimblewimble/grin-pm/issues/287)
* [v5.0.0 project board](https://github.com/orgs/mimblewimble/projects/1)
* **Node milestone:** [5.0.0 Milestone · GitHub](https://github.com/mimblewimble/grin/milestone/19)
* **Wallet milestone:** [5.0.0 Milestone · GitHub](https://github.com/mimblewimble/grin-wallet/milestone/9)

# Timeline

Date | Milestone | Description
---|---|---
2020-10-13 | Scope freeze | New functionality, improvements, and fixes targeted for the upgrade are defined, and prioritised.
2020-11-24 | Beta Binaries Release | Release of grin, grin-wallet, grin-miner beta binaries.
2020-12-08 | Testnet upgrade | Launch of testnet hard fork and public testing.
2020-12-15 | Release candidate binaries | Release of grin and grin-wallet RC binaries.
2021-01-05 | Final release | Release of grin and grin-wallet binaries.
2021-01-17 (est) | Mainnet upgrade | Grin is forking to v5.0.0.

NB: Actual dates (but not the hard fork block height) may vary slightly based on the current circumstances.

# Communication

Prior to the hard fork, the Grin community will communicate with the following medium:

Date | Milestone | Description
---|---|---
2020-10-30 | Communication to exchanges and mining pools | Communicate with exchanges and mining pools to make sure everyone is aware and are getting ready for the upgrade, offering assistance as required.
2020-12-01 | 1st Banner | First banner on the website with a link to a summary of what will happen.
2021-01-03 | 2nd Banner | Update banner on the website with binaries and urge ecosystem to upgrade.
2021-01-08 | Final banner | Update banner to urge mining pool and exchanges to upgrade.
Immediately following upgrade | v5.0.0 banner | Add a banner on the website informing about the hard fork, the changes introduced, and links to the latest binaries.

## Contact

For any feedback, questions, concerns, or problems, please contact Daniel Lehnberg:

* Email: [daniel.lehnberg@protonmail.com](mailto:daniel.lehnberg@protonmail.com)
* Keybase: [@lehnberg](http://keybase.io/lehnberg/chat)

## Changelog

* v0.1, Oct 14: Initial draft
* v0.2, Nov 03: Correct date typo
* v0.3, Dec 11: Added testnet fork height

---

### Post by @tromp ⭐ (2020-12-11)
*Post #5*

You can fill in the testnet fork height now: 642_240

---

### Post by @tromp ⭐ (2021-01-07)
*Post #7*

From HF4, the PoW is Cuckatoo32+, which is a miner’s choice of
Cuckatoo32 or Cuckatoo33 or Cuckatoo34 or … or Cuckatoo63.
In practice, I expect we won’t be seeing any Cuckatoo33 (let alone others) for a long time, considering it has double the memory requirements, as well as the awkward word size.

---

### Post by @tromp ⭐ (2021-01-08)
*Post #9*

No more change.
Your friend is misinformed.

---

### Post by @tromp ⭐ (2021-01-16)
*Post #19*

Every wallet has a TOR address. Some have yet to show it though.

---

### Post by @tromp ⭐ (2021-01-18)
*Post #24*

The 4th hard fork (that was really a network upgrade) was successful.

---



## Grin++ for Android v0.0.1
*Date: 2020-12-14 | [Forum Link](https://forum.grin.mw/t/grin-for-android-v0-0-1/8070)*
*Importance Score: 76.5 | Core Participants: david, davidtavarez, quentinlesceller*

### Post by @davidtavarez ⭐ (2020-12-14)
*Post #1*

Release: **Android 0.0.1**

This release is the first release of Grin++ for Android. Grin++ is an easy to use Grin Wallet, which does not store any personal identifiable information, there is no analytics; the little information that is stored like the session token is stored encrypted. Also, the node information like the wallets cannot be copied.

**Features**

* Create multiple grin wallets.
* Backup/Restore wallets via seed phrase.
* Send and Receive $grin via Tor and Slatepack Messages.
* Address availability checker.
* Transactions history.
* See the details of each transaction.
* Control Grin node using notification bar.
* Share the grin wallet address.

**Minimum Requirements**

* Minimum Android version required: **Android 9.0 (API Level 28)** .
* Architecture supported: **64bit** .
* ARM: **AArch64** or **ARM64** .
* Minimum RAM: **4GB** .
* Minimum Disk Space: **2GB**.

**Direct Link** : <https://keybase.pub/dtavarez/grin%2B%2B/apk/0.0.1/com.grinplusplus.mobile.apk>
**Google Play** : <https://play.google.com/store/apps/details?id=com.grinplusplus.mobile>

Please, make sure that your device meets the minimum requirements.

**Support**

Since neither analytics or crash reports were added, the best way to ask for support is using the Grin++ Support Channel: <https://t.me/GrinPP>

**Translations**

If you want to see Grin++ translated into another language, please, feel free to contribute.

[0011242×2208 154 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/611de75b9056259b35750e4a7593d4bfb873a05c.jpeg "001")

[0021242×2208 172 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/df0bb6b142ec1194bb729d0d1e113ddd7b3e85ce.jpeg "002")

[0031242×2208 173 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/28a9b05646523a29ebe65b3eadde88fe8eaee4cd.jpeg "003")

[0041242×2208 149 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e7f25072bdf17a5f5eaaba101aa183f085fa27f6.jpeg "004")

[0051242×2208 190 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/02085b16ccf1f671d674114d9178c68a7088a7a1.jpeg "005")

[0061242×2208 173 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/eb786a4d73605a495df49037831e2da3f9660df8.jpeg "006")

[0071242×2208 208 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c25dff0ac2a65a61ff44f271b2021a94bcfe0d23.jpeg "007")

---

### Post by @david ⭐ (2020-12-14)
*Post #4*

Samurai:

> Minimum RAM: **4GB** ?

It’s a full node. It won’t use that much ram all the time, but during IBD it could use quite a bit for brief periods.

---

### Post by @davidtavarez ⭐ (2020-12-14)
*Post #12*

Roelsmajor:

> 89 minutes for fully sync

89 minutes?! mmmm… are you using a VPN? could you share the devices specifications? Android version? I see only 6 connected peers, it is always like that? 6 to 8 peers?

Thanks.

---

### Post by @david ⭐ (2020-12-14)
*Post #14*

89 minutes seems reasonable tbh. It’s largely dependent on peers and connection speed, and there’s of course a ton of processing required when validating the state. I have fast internet and a relatively powerful device and it still took me quite a while.

---

### Post by @quentinlesceller ⭐ (2020-12-15)
*Post #15*

This is some impressive work [@davidtavarez](/u/davidtavarez) !! Congratulations! Having a full node running on a mobile device is amazing.

---

### Post by @davidtavarez ⭐ (2020-12-15)
*Post #17*

grin001:

> connection failure 127.0.0.1:3421

means that the node, which is running in background, stopped and the app is not able to communicate with the node; I recommend this:

Close the app like this: [How to close apps on Android: All you need to know](http://www.digitalcitizen.life/close-apps-android)

Stop the Service following the next steps:

Swipe from up to bottom your notification bar to display these actions:

[photo53665940724012606561078×691 35.8 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e7b08db1e1369db1883e8baf1e5423eb8518ff26.jpeg "photo5366594072401260656")

Now, tap on **STOP** :

[photo53665940724012606551080×406 19.2 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/d52bd9705319552bc5ca99ed4da921f7a764d89c.jpeg "photo5366594072401260655")

Make sure that Grin++ can be run in Background avoiding Android to kill the Node because this can cause the chain to get corrupted:

[Screenshot_20201215_1051101080×1107 38.1 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/54fa99ed476546fcd0f5a44c1c9b33bdc3ffc443.jpeg "Screenshot_20201215_105110")

_The process of doing this will vary depending on the device._

Open the Grin++ again and try yo create a wallet again.

---

### Post by @davidtavarez ⭐ (2020-12-17)
*Post #20*

Google finally approved Grin++ <https://play.google.com/store/apps/details?id=com.grinplusplus.mobile>

---

### Post by @davidtavarez ⭐ (2020-12-18)
*Post #23*

not a 100% ready yet; this is v0.0.1, currently beta; a new version will be released for the next HF. As long as you keep your wallet seed save, it won’t be a problem.

---



## [ENDED] Sales in Forum for iPOLLO G1-Mini Miner with Exclusive Discount and 20% Donation Promise
*Date: 2020-12-18 | [Forum Link](https://forum.grin.mw/t/ended-sales-in-forum-for-ipollo-g1-mini-miner-with-exclusive-discount-and-20-donation-promise/8089)*
*Importance Score: 95.1 | Core Participants: david, tromp*

### Post by @gary (2020-12-18)
*Post #1*

I see iPOLLO [G1-Mini](https://forum.grin.mw/t/ipollo-grin-g1-mini-miner-prototype/8030) start accepting orders since their [official new product launch event on Dec. 15](https://ipolloglobal.medium.com/ipollo-g1-mini-launch-appreciate-john-tromps-spirit-of-minimalism-b11a01aedee2), and I see the complains in community for the difficulty of making an order, especially for people from western world. I forward the words to iPOLLO’s top management team, they answer that there are too many scalpers there in Telegram channel and they’re hesitating on those queries/sales, they say iPOLLO want to launch a fair sales but it’s quite difficult to identify who comes from the GRIN community and who is a long term supporter of GRIN so as to give a priority. But I think this forum maybe can help on that, even not perfect.

During the communication, iPOLLO gave a proposal which I think quite feasible and I revised a little, that they can reserve 50 G1-Mini miners (or maybe a little more if needed) for this GRIN forum, but with following **restrictions** :

* These 50 G1-Mini miners are only for the old users in this forum, all new registered forum users after this post is not qualified to make order for this time.
* Each forum user can make an order for <= 2 miners.
* The delivery address must not be the China mainland. (Sorry about that but I suppose the Chinese users are convenient to buy it with WeChat.)
* The delivery address can not be India. (b/c problem of export there)
* This forum sales is available for about 2 weeks, i.e., **sales will be closed at 2020.12.31 UTC 23:59:59**.

Thanks for iPOLLO, we can get a discount plus a donation promise for this Forum Sales, and this discount is ONLY available here, not at any other sales channel.

* The official quotation of one G1-Mini is $520 (USD).
* 5% discount with GRIN payment, i.e., $494 for each G1-Mini.
* 20% donation for the total sales revenue in this forum sales, i.e., $100 donation to [Grin Dev Fund](https://grin.mw/fund) for each G1-Mini sales here. Donation will be given when this sales close.

**Payment and Shipment** :

* Please choose your suitable payment method presented in <https://www.ipollo.com/ipollo_en/interhashMikecrm.html>.
* The shipment would suppose to be the mid of Jan. 2021, if the logistics impact during the epidemic is not considered.
* This price only covers the cost of the miner itself. The transport logistics will have to be taken care of by buyer, and iPOLLO will check this with buyer before delivery.

iPOLLO will assign one salesman  ([@ipollosales](/u/ipollosales)) to join this forum so as to handle this forum sales. A **valid** order must be made by _**replying this post with the required number of G1-Mini**_ , _**plus sending an email to[interhash@ipollo.com](mailto:interhash@ipollo.com)**_, remember to _**note in email about your username in this forum, plus the delivery address.**_

Disclaimer:

1. I’m not part of iPOLLO, also I have no any financial interest related to iPOLLO. I’m a little bit active at this time to help iPOLLO (to connect better with GRIN community) just because GRIN indeed need ASIC miner and vice versa IMO, the investing for an ASIC (from R&D to manufacturing) is very expensive considering the current [GRIN market cap](https://coinmarketcap.com/currencies/grin/), and iPOLLO is the first available one with a promising performance. Higher network hashpower in GRIN always means better security and brighter future. I like/want GRIN better, that’s all.
2. Mining on your own risk. There’s no guarantee to be profitable mining GRIN with this machine. The crytocurrency market has big risks and any investment needs to be cautious!
3. iPOLLO is a company registered in China Zhejiang province, I take a screenshot (sorry only Chinese available) from China goverment website [http://zj.gsxt.gov.cn](http://zj.gsxt.gov.cn/) . Any issue concerning to the iPOLLO product, please consult with iPOLLO service or its legal entity.

[ 3181080×2340 151 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/47fcf3110f7ea5aa82fe27e1119d2c44202826ad.jpeg "318")

[ 3191080×2340 316 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/574d5242236a4f1a0d022f33b2463889ba332433.jpeg "319")

Frequent Links:

* Website: <https://www.ipollo.com/ipollo_en/>
* Contacts: [@ipollosales](/u/ipollosales) or email: [interhash@ipollo.com](mailto:interhash@ipollo.com)

---

### Post by @Shobji (2020-12-19)
*Post #9*

Sent E-Mail to confirm my order received this reply.

[image750×661 81.8 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2288d6db2b23490098a593b5c1f3372dc784aced.jpeg "image")

---

### Post by @ipollosales (2020-12-20)
*Post #16*

G1-Mini miners for Mainland China have been sold out, this was why we set this auto-reply info. As for overseas, we firstly reserve the 50 miners for this forum sales and then sell to others if there is any miner left. In addition, our official website is <https://ipollo.com/>, thanks.

---

### Post by @tromp ⭐ (2020-12-20)
*Post #19*

Could you please publish the total production numbers (existing and planned) of both the G1 and G1-mini? Thanks!

---

### Post by @tromp ⭐ (2020-12-21)
*Post #22*

ipollosales:

> Moreover, the total production numbers of G1-mini in this batch is less than 1,000.

Thanks for the info!
That seems like a rather small number. The total of 1400 gps of this batch will have only a minor impact on the network graphrate. Do you have any plans for future batches yet?

---

### Post by @tromp ⭐ (2020-12-21)
*Post #24*

> production of G1 which were reserved by customers last year,

These customer reservations imply planned or existing production of G1,
which I included in my original question.

---

### Post by @david ⭐ (2020-12-22)
*Post #25*

I’ll take one G1-mini please.
I will follow up via email.

---

### Post by @trevyn (2021-03-24)
*Post #94*

What temperature are people seeing who are getting full hash rate and minimal rejects? That should be the target. You may not ever see 60C with full, valid hashrate unless you put it in a freezer.

What is your ambient temperature? Have you tried putting it in a cooler place? I assume you’re not willing to crack it open and make some cooling mods?

I suspect what is happening is that there is a hard limit of ~100C in the chip, as there should be, and it is throttling to keep the temperature just below that. It’s a little weird that it seems to surface as rejects instead of just a reduced hashrate, but not entirely surprising given the circumstances.

Edit: [this post](https://forum.grin.mw/t/ipollo-grin-g1-mini-miner-prototype/8030/4) says there is a configuration setting for changing the fan speed, do you have this option?

---



## Images on the togetherness of Grin and Tor
*Date: 2021-01-14 | [Forum Link](https://forum.grin.mw/t/images-on-the-togetherness-of-grin-and-tor/8238)*
*Importance Score: 89.3 | Core Participants: davidtavarez*

### Post by @minexpert (2021-01-14)
*Post #1*

With the Slatepack standard, we can share creative images that symbolize our Tor connection under this topic. I’m adding two images I created myself.

[grintor1280×720 72.5 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/bf9c87bfa9dc224e63a3d6521afe031c83742be8.jpeg "grintor")

[grintor21280×720 65.9 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/70a9d685cfad70049ade541d6a2a54a5872402ed.jpeg "grintor2")

---

### Post by @nirg (2021-01-16)
*Post #3*

[ wlp1920×1080 260 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a52f9eebc35981b54e5569d91f33d045bbeb849a.jpeg "wlp")

combined force

---

### Post by @nirg (2021-01-17)
*Post #6*

Grin and Tor alliance ascii art style

[ ASCII-Art-11920×1080 150 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/23a92b47507235e0b8bf06762737a33d7493ad2a.png "ASCII-Art-1")

---

### Post by @nirg (2021-02-13)
*Post #12*

[ trust1920×1080 162 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/042d08777b9cba0ab9eb07923f29b9f6ad8f1aab.jpeg "trust")

In Grin We T(o)rust. Would it be better?

---

### Post by @nirg (2021-02-18)
*Post #15*

A map is always a good idea [@grn](/u/grn) So I design a grin++ via tor wallpaper.

[grin++1920×1080 623 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/10013667f041051485b7c5c24b926230d23cd2dc.jpeg "grin++")

---

### Post by @davidtavarez ⭐ (2021-02-22)
*Post #19*

pretty accurate, grin++ has been translated into 14 languages already

---

### Post by @nirg (2021-05-27)
*Post #31*

We are an image from the future

[ future1920×1080 522 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/9cbf645b47dbf0b984e675587aa8be82ba02c2c9.jpeg "future")

---



## Beam is more successful than Grin?
*Date: 2021-01-21 | [Forum Link](https://forum.grin.mw/t/beam-is-more-successful-than-grin/8276)*
*Importance Score: 75.8 | Core Participants: tromp, davidtavarez*

### Post by @markov (2021-01-21)
*Post #1*

Its price (0.37…) now surpass Grin (0.36…).

---

### Post by @markov (2021-01-21)
*Post #3*

Don’t put your hands over your ears to pretend that you can’t hear anything that is bad to you. Just admit it. If price is not important, why everyone rush to BTC?

---

### Post by @Paouky (2021-01-21)
*Post #18*

Literally 80% of the top 100 coins by market cap are complete junk and remain alive purely as a cash grab with no real future. Does their mcap make them successful? Sure, if you measure success by the acquired wealth of founders and investors.

This is a futile discussion.

---

### Post by @insider (2021-01-21)
*Post #22*

Spartakus:

> if you stay small, exchanges,users ignore you. Adoption is lagged becuz of tx problem. With slatepacks this problem is solved mostly.
>
> But users,community,Grinners are very lazy,they stay silent at social media,bitcointalk forum,reddit. i just saw Tromp and a few making comments and defending Grin Mimblewimble.
>
> How many of people here talked,twitted,mnetioned or argued with other crypto communities?
>
> How many of us forced exchanges ,submit tickets for slatepacks? just complaining here and bragging doesnt help.Devs doing job. Rest is just complaining.
>
> Grin community is small and lazy.

The Grin community is the best in the entire crypto space. It practically doesn’t talk about money. The community talks about ideas. And what is most interesting, you will not find so much art anywhere else. This speaks of interest. Look how much has already been done and how much will be done … You are very disrespectful. You take everything for granted and demand more.

Grin is currently at the earliest stage of adoption in the entire history of the universe. You must remember this and take into account the inflation schedule.

---

### Post by @tromp ⭐ (2021-01-21)
*Post #30*

markov:

> Its price (0.37…) now surpass Grin (0.36…).

By your reasoning, Grin is more successful than Ripple (0.28).

---

### Post by @vegycslol (2021-01-21)
*Post #33*

Whoever is disappointed by grin’s price knows nothing about the inflation. Currently inflation is just too high for anyone to invest in it and hold without a significant risk of losing a lot of the value. Instead of complaining about the price try to figure out how to improve privacy, 2-step etc

---

### Post by @tromp ⭐ (2021-01-21)
*Post #35*

Inflation is not higher than most non-premined coins in their initial years.

Rather, Grin’s emission is way SLOWER than others. Grin has only emitted about 2% of its soft total supply [1], whereas those others would have emitted over 20% after 2 years.

[1] <https://john-tromp.medium.com/a-case-for-using-soft-total-supply-1169a188d153>

---

### Post by @davidtavarez ⭐ (2021-01-22)
*Post #57*

please, update to v1.2.3  <https://grinplusplus.github.io/>

---



## Mimblewimble CoinSwap proposal
*Date: 2021-01-28 | [Forum Link](https://forum.grin.mw/t/mimblewimble-coinswap-proposal/8322)*
*Importance Score: 121.9 | Core Participants: tromp, joltz*

### Post by @tromp ⭐ (2021-01-28)
*Post #1*

# Abstract

We present a coin shuffling proposal with the following properties:

* Users submit self-spends throughout the day. No interaction needed for shuffling.
* Shuffling is performed at the end of the day by a set of mixnodes that cannot steal any coins.
* Invalid self-spends are automatically filtered out. No need to abort or restart the shuffling.
* As long as at least one mixnode is honest, then no one learns the input output links.
* The size of the shuffle is limited only by blocksize and could easily be over a thousand.
* Each shuffle only grows the chainsize by a small constant (~100 byte), thanks to MW cut-through.

Widespread use of the protocol would leave the transaction graph mostly obscured.

# Introduction

This document proposes a possible design for a ``trustless’’ Mimblewimble CoinSwap service to which users submit self spend data throughout the day (or hour or any desired period) which are validated, aggregated, and published at the end of the day.

Coins swaps are useful for obfuscating the Mimblewimble transaction graph. They can be applied to self spending outputs that were recently received, or to self-spends resulting from canceled/aborted transactions. The lack of urgency of such self spends lends itself well to the slow nature (and possible failure) of coinswaps.

Whereas self spends normally reveal their input-output link publicly in every mempool on the network, use of a CoinSwap service obscures this link from public view. If one further trusts at least one service node to be honest, then the link is obscured from the nodes’ view as well. In this sense little trust is needed to benefit from the service. If all nodes collude, they not only learn the input output links, but could also choose to revert the entire coinswap after it confirms on-chain. Which is still a manageable problem for wallets, even if very unlikly.

This document is not concerned with aggregation of regular transactions, or what could be called a CoinJoin service. Consistent use of coinswaps on outputs received in regular transactions should make coinjoins mostly redundant, although it does come at a roughly doubling of fees.

This design follows the Grin forum discussion at [Daily Aggregator (Partial Transactions) - #3 by antioch](https://forum.grin.mw/t/daily-aggregator-partial-transactions/8260/3) and combines ideas of users antioch, oryhp, vegycslol, and myself.

We first present the general design, and then discuss several refinements dealing with practical issues such as timing attacks, spam attacks and ownership proofs.

# The CoinSwap protocol

## MWixnet Architecture

The protocol is similar to that of mixnets, but instead of mixing messages from senders to receivers, we mix self spends from coin owners to themselves. Whereas the messages in a mixnet do not change, our mixnodes transform commitments into new ones, and then achieve mixing by sorting the results.

Let there be m self spends spend 1 .. spend m, and n mixnodes node 1 .. node n. We let subscript i range over spends, and subscript j range over nodes.

Let xi,j be the randomly generated excess by which node j should additively transform the commitment in spend i: Ci,j = Ci,j-1 \+ xi,j * G.

Conceptually Ci,0 and Ci,n are the input and output of spend i, except for a necessary fee adjustment:

* Ci,0 = Ciin \- fee * H
* Ci,n = Ci,0 \+ (Σj xi,j) * G = Ciout

The excesses form a matrix such as this one for 4 self spends and 3 servers:

x1,1 x1,2 x1,3

x2,1 x2,2 x2,3

x3,1 x3,2 x3,3

x4,1 x4,2 x4,3

which correspond to the linkages in this matrix C of commitments:

C1,0 ↔ C1,1 ↔ C1,2 ↔ C1,3

C2,0 ↔ C2,1 ↔ C2,2 ↔ C2,3

C3,0 ↔ C3,1 ↔ C3,2 ↔ C3,3

C4,0 ↔ C4,1 ↔ C4,2 ↔ C4,3

Each node receives a sorted column, not knowing the i indices shown, transforms each commitment by some excess specified for that commitment, sorts the results, and passes on the new column to the next node.

## Data provision

Node 1 is provided, for each i, with with a tuple datai,1 containing:

* commitment Ciin
* a proof of ownership of Ciin
* excess xi,1

Node n is provided, for each i, with with a tuple datai,n containing:

* commitment Ci,n-1
* corresponding range proof BPi
* excess share xi,n

Each other node j is provided, for each i, with a tuple datai,j containing:

* commitment Ci,j-1
* excess share xi,j

## Input validation

Validation starts with node 1 computing, for each i, Ci,0 = Ciin \- fee * H. It also verifies that each input commitment is unique, present in the UTXO set, and has a valid proof of ownership. All invalid data is removed (resulting in a smaller m).

## Output derivation

Then for each j from 1 to n in turn, node j computes, for each i, Ci,j = Ci,j-1 \+ xi,j * G, and if j<n, sends the ordered set of m commitments Ci,j to its neighbour node j+1.
Any commitments received by a node that are not among its tuples are invalid and get removed.
Also, any non-unique Ci,j are similarly invalid and removed. This will allow correct determination of validity in the later kernel derivation stage.

## Output validation

Node n removes all received commitments that don’t have valid range proofs.
Let Out be the set of remaining commitments.

## Kernel derivation

Then for each j from n to 1 in turn, node j computes kernel Kj for a public excess of G * Σvalid xi,j, and if j>1, sends Out, the set of n+1-j kernels, and the set of valid commitments Ci,j-1 to its neighbour node j-1.
This maintains an invariant that ΣC ∈ Out C - Σvalid Ci,j = Σk>j Kk.
[Mimblewimble CoinSwap proposal - #57 by oryhp](https://forum.grin.mw/t/mimblewimble-coinswap-proposal/8322/57) explains how to optimize this to a single kernel.

## Aggregation

Finally, node 1 ends up with a set of valid C0,j that by invariance differs from the Out sum by all n kernels.
It constructs the final coinswap transaction CS from the set of valid outputs Ciout in Out, the set of valid inputs Ciin, the n kernels Kj, and an extra input and/or output to collect the leftover fees (or pay missing fees) as appropriate.

Once confirmed, the coinswap is irreversible unless all n nodes collude.

# Practical Issues

## Data provision

The data provision step above suggests that users send data directly to n different nodes. While possible, this is not the most practical.
The following improvement is inspired by TOR, The Onion Router.
Let’s assume that each node j has a known public key PKj, and denote by ENC(PK, D) the pair <DHPK, E> where DHPK is a temporary public key generated by Diffie-Hellman for PK, and E is the symmetric key encryption of data D with the shared secret as key.
Then for each i we can recursively define an onion bundle OBi,j for nodes j..n as follows:

* OBi,n = ENC(PKn, datai,n)
* OBi,j = ENC(PKj, <datai,j, OBi,j+1>)

Now a user only needs to send OBi,1 to node 1, which can decrypt to obtain both <datai,1 and OBi,2. In the output derivation stage, each node j decrypts each OBi,j, checks that the received Ci,j-1 matches the one in datai,j (removing mismatches), computes Ci,j, sorts all OBi,j+1 by Ci,j, and passes those on to its neighbor node j+1.

This onion bundling not only prevents timing attacks on users whose spend data submisions to different nodes are correlated in time, but also allows them to send their data to a single node, possibly as soon as they receive the output they want to self spend.

## Fee handling (Grin)

In a more realistic setting, each node pays itself a mixfee with a 1-input 1-output transaction replacing $K_j$, where Σvalid xi,j can instead by added to the transaction offset.
The contributed fees should then match the coinswap relay fee plus n mixfees. In Grin this gives the identity (with FB being the fee base of half a millicent):

|Out| * fee = (|Out| + n) * (1 + 21) * FB + n * 3 * FB + n * mixfee, or
mixfee = |Out| * (fee - 22 * FB) / n - 25 * FB.

For simplicity, we could require a fee of (22 + n) * FB, resulting in a mixfee of (|Out| - 25) * FB. In that case, for a mixnode to earn 10 grin-cents a day requires 225 daily self spends.

## Spam attacks

A deluge of bogus onion bundles could fill up node 1’s memory buffers long before the day is done. This is mostly remedied by doing immediate input validation on every new bundle received by node 1. At the end of the day, we’d still redo the UTXO membership checks since self spend inputs could be spent during the day.

Thanks to the proofs of ownership, the number of self spends of any one attacker, surviving input validation, is limited by the number of outputs they own.
Having enough buffers to cover the entire UTXO set is one solution.

If after input validation at the end of the day, more spends remain than fit in a block (about 40000/22 = 1818) then two options are available:

* run a modified version of the above protocol that merely filters out all invalid data. Any invalidly spent input can be banned from future coinswapping.
* randomly partition them into equal sized (under 1818) subsets, and run coinswap on each in turn.

A proof of ownership of commitment C can take the form of a proof of a length-1 vector commitment as described in <https://forum.grin.mw/t/vector-set-commitments-generalize-schnorr-and-utxo-proof-of-ownership/>
which takes only 32 bytes more than a Schnorr signature.

## Bandwidth Optimization for n=2

In the case of only 2 non-colluding nodes, we can do away with the (relatively large) proofs of ownership, and reverse the flow of data. That is, the onions are constructed with the (much smaller) node 1 data inside the bundle for node 2. Node 2 starts with output validation and sends transformed valid commitments back to node 1, which then does input validation on its transformed commitments. Kernel derivation then proceeds back to node 2. In this case it’s possible to handle spam with intermediate filtering rounds. Even though both nodes determine valid sets of inputs and outputs, they would require collusion to link them together. One downside is that node 2 can try to correlate submission order with the order that final coinswap inputs appeared on-chain.

## Other Bandwidth Optimization

Node n could send the large Out set directly to node 1, reducing bandwidth through intermediate nodes on the backward pass by about half, but at the cost of those intermediate nodes no longer being able to check the invariant.

## Reorg protection

A deep reorg is likely to invalidate a big coinswap transaction. In order to be able to still redo most of the contained self spends, node 1 could remember all valid input onion bundles for the past few days, and reprocess any that were undone in a reorg.

---

### Post by @tromp ⭐ (2021-02-03)
*Post #12*

When you send your output from tx1 through a coinswap service before spending it in tx2, nobody can link these two tx together except with a small 1/N probability where N is the number of other coinswappers that day.

So it’s like getting a size N anonimity set, where N is limited to the max number of self spends in a block (1818).

Suffice to say, this is pretty awesome!

---

### Post by @tromp ⭐ (2021-03-30)
*Post #28*

gene:

> the swap nodes contributing random excess to the tx?

You mean the mixnodes? And what random excess are you referring to?

gene:

> how are non-signing swap nodes able to malleate txs with extra randomness?

By txs, do you mean the user’s self-spend data? Mixnodes can’t change the input, excesses, or output of anyone.

gene:

>   *     * does the original sender need to sign after the swap is “complete”?
>

No; as the proposal makes clear, the users just submit data. “No interaction needed for shuffling.”

gene:

> something like: “X tx marked for coinswap, keep in coinswap pool for M blocks, then aggregate”

That defeats the entire purpose of the coinswap protocol, since all i/o links are publicly visible in the coinswap pool.

---

### Post by @tromp ⭐ (2021-03-31)
*Post #30*

I thought by contribute you meant provide. Now I see you meant add.
The adding of user-provided random excessses is the mechanism by which to randomly permute the self-spends at each stage, to obfuscate the i/o links to anything less than a full mixnode collusion.

gene:

> All i/o links are still observable by mixnode 1, or am I wrong?

Yes, you’re wrong. Mixnode 1 doesn’t know what input corresponds to what output.

gene:

> is there a one or two sentence explanation for how the mixnodes obfuscate the transaction graph?

Each mixnode randomly permutes the i/o links using data only available to them.

---

### Post by @tromp ⭐ (2021-07-22)
*Post #35*

1. Requires finding reputable parties. enjoying widespread trust in Grin community, willing to run the mixnodes. Perhaps even multiple sets that users can select from through wallet configuration.

2. If implemented and enabled by default in most wallets, and having at least a few dozen genuine tx mixed per day, then the privacy is comparable to Monero.

3. It’s too good not to get implemented. But with current lack of developers, it will take time.

---

### Post by @joltz ⭐ (2021-11-19)
*Post #47*

Thanks for this work [@tromp](/u/tromp) [@scilio](/u/scilio) [@phyro](/u/phyro) and others. Apologies it has taken me this long to give it a review.

I’m going to attempt to restate my understanding of the protocol as it relates to a possible implementation to help my small brain before I get into the code.

Please correct me if I have anything critical incorrect or missing. I’ll do my best to not ask any questions already answered but no promises.

At some point soon I would like us to get a completed ‘specification.txt’ or ‘protocol.txt’ included in the mwixnet github repo in /docs/ or something to make all of this easier to assess, iterate on etc. (though [@tromp](/u/tromp) may want to keep two docs- one for the pure high-level protocol and one for the specification against which the implementation should be assessed). It might be nice to have a @grincoin#mwixnet channel for dedicated discussion in keybase too.

Steps below assume a 3-node route and focus on 1 spend with some generalization (with an attempt to use simple language):

1. For each transaction, the owner of the spend provides and generates the following:

* 1 valid UTXO present onchain
* 1 random excess for each mixnode used (if 3 mixnodes, 3 random excesses)
* 1 proof of ownership of the UTXO to be used as the input (exact strategy not explicitly stated yet in the spec?)
* 1 range proof on UTXO/input commitment + sum of all random excess commitments generated for each node (i.e. final output)
2. From a fixed set of known mixnodes, the owner determines an onion routing path through the nodes (see question(s) at the end about dynamic vs fixed routing)

3. Once the nodes and path are selected by the owner (if dynamic), owner constructs and encrypts payloads to be routed

* Note detailed key derivation etc is ignored here for simplicity

* For each encrypted payload, a plain text commitment is included

* The first commitment is provided by owner, subsequent commitments are provided by the previous node in the path
* The first payload is built and encrypted to a key of the first node

* commitment = UTXO/input commitment
* p1 = enc1(excess1, proof of ownership of UTXO/input commitment)
* The second payload is encrypted to a key of the second node, then encrypted again to a key of the first node

* p2 = enc1(enc2(excess2))
* The final payload is encrypted to a key of the final node, then encrypted again with previous keys of all previous nodes in reverse order

* p3 = enc1(enc2(enc3(excess3, range proof)))
* The range proof should be valid on original UTXO commitment + sum of all random excess commitments (i.e. final output)
4. The owner submits data1 to the first node they selected, node1

* data1:
* UTXO/input
* p1, p2, p3
* node1 decrypts all payloads, removing enc1 encryption layer
* node1 verifies that UTXO is unique, present onchain and that proof of ownership is valid
* node1 includes the modified commitment to create necessary data to send to node2
* data2:
* sum of UTXO/input commitment and excess1
* enc2(excess2)
* enc2(enc3(excess3, range proof))
* The first node submits the above data2 to node2
5. node2 decrypts all payloads, removing enc2 encryption layer

* node2 derives new commitment by adding excess2 to the provided commitment by previous node
* node2 includes the modified commitment to create necessary data to send to the final node, node3
* data3:
* sum of previous commitment and excess2
* enc3(excess3, range proof)
* The second node submits the above data3 to node3
6. node3 decrypts the remaining payload, removing enc3 encryption layer

* node3 builds the final output for the spend by summing the previous commitment with provided excess3
* node3 verifies that the range proof is valid for the updated final output commitment
7. node3 computes the first kernel with valid output(s) and commitment(s) with an excess of the sum of random excess(es)…

I’m still trying to fully wrap my head around the kernel aggregation section.

Does the protocol require that for a given mix, all spends must use the same routing order for j nodes, such that node n is always last node for each spend as well as node 1 always the first node for each spend?

It seems that if each node is supposed to produce one kernel per coinswap, the final commitments (outputs) need to all arrive at the same node for the first kernel to be built?

Though it seems simple enough and the invariant is straightforward, I’m still trying to work out the exact steps for how exactly the kernels would be derived based on the notation. Do we assume that routes for all spends are the same and fixed per coinswap and that all nodes j are participating and have all relevant data?

Thank you

---

### Post by @joltz ⭐ (2021-11-20)
*Post #51*

[@phyro](/u/phyro) thank you for the reply and clarification.

I was making a bad assumption re: routing. My concern would be without a dynamic routing, it only takes one node to be unavailable and all mixing would stop? The risk would be the mixing could be completely disrupted by dos’ing only one server? I know this adds a ton of complexity to address though so I’m not sure how much (if at all) it is worth talking about now.

[@scilio](/u/scilio) thank you very much for the explanation, it is clear now. I’ll leave a proper review in your PR in the next few days but on first pass it looks like you accomplished everything set out in your first milestone, nicely done, glad to have you here.

---

### Post by @tromp ⭐ (2022-01-15)
*Post #58*

oryhp:

> Mixnodes add their partial excess when going forward and they sign the total excess and adjust the offset when going backwards.

This is a good idea. I don’t think it will stop the coinswap from standing out, but it does save a few kernels, which is always good.

To make this work, each mixnode should generate both a random private excess and a random private nonce, and add the corresponding public excess and nonce to the cumulative versions that are passed forward. The final mixnode can then use the cumulated totals as public key and nonce for the single kernel. On the way back, each mixnode adds its input and output for fee collection, and adjusts the coinswap offset to compensate for its private excess, the valid x_i,j it added to commitments, and this added fee input/output.

---



## An open discussion on Non-interactive transactions
*Date: 2021-03-03 | [Forum Link](https://forum.grin.mw/t/an-open-discussion-on-non-interactive-transactions/8510)*
*Importance Score: 102.5 | Core Participants: david, tromp, davidtavarez*

### Post by @satoshocrat (2021-03-03)
*Post #1*

Hi all, long time lurker, first time poster hah.

I want to start by saying that I enjoy, and I am passionate about blockchains for what they fundamentally allow: “freedom of transaction.” That is to say, an “Open, Neutral, Decentralized, Borderless, censorship-resistant” conveyance of value from one party to another.

I fell in love with grin when I understood this value proposition, and what Grin offers the ecosystem by virtue of scalability. On top of that, add transactional privacy on base layer with amounts. Objectively, this is a “break-through,” and we should be excited about it. Admittedly, I feel a bit “late to the party,” as everyone has contributed so much, but my passion speaks.

I have over the months become dismayed about the fact there is so much contention over the vision of this opportunity.

What I aim to do is extend the dialogue regarding a feature many in this community desire, and one that would add conventional usability: Non-interactive transactions. This of course would not dismiss the opportunity for interactive (and all the future possibility it could entail); as I understand, interactive as “opt-in” maintains many of these benefits of interactive if implemented correctly.

I’m not asking for a rash judgment, or a mutiny of code/fork or anything of the sort.

I am asking that the voices of the many who feel disenfranchised in the process to be heard.

Let us as a community, of which each of us is a member, allow for a fair and robust analyses of the Non-interactive proposals’ merits. There are a few proposals which many feel have not been given the proper diligence in discussion, or “air time.”

Let’s do it.

With the community funding paradigm shifting, my desire would be we have all options on the table, fund a 3rd-party team of cryptographers (who may even improve it on simplicity, let a lone on security.)

I could be way off base, so please let your voice be heard. I want to stress that this is not to take away from any of the efforts of the “core” team, or any contributions yet-to-come that may deviate in vision. I do, however, believe it’s a valuable, necessary option for a blockchain that scales as a more-private, decentralized cryptocurrency. We are the community, and we owe it to the future to try.

---

### Post by @tromp ⭐ (2021-03-03)
*Post #3*

satoshocrat:

> please let your voice be heard

I let my voice be heard previously [1] [2] [3]. In summary, I’m strongly opposed to departing from the beautiful simplicity of Mimblewimble and turn it into some ugly hybrid in order to save 1 or 2 cut&pastes.

As the original MW implementation, Grin should embrace its unique properties rather than subvert them for the sake of conformance. Interaction allows us to

* transact with the assurance that the funds end up with the recipient able to spend them [4]
* agree to a payment proof stating the purpose of payment
* use payjoins for obfuscating direction of payment
* have a seamless migration to use of payment channels and a 2nd layer that will be critical to improving scalability by orders of magnitude.

We have yet to fully realized the advantages that interaction offers, and should not be disincentivizing progress on that path by getting most people to revert to non-interactive transacting. Especially not when that comes with big downsides of hugely complicating the consensus model, adding bloat to the chain, changing the security model, and having to support two different forms of transacting.

[1] [Pep Talk for one sided transactions - #8 by tromp](https://forum.grin.mw/t/pep-talk-for-one-sided-transactions/7361/8)
[2] <https://forum.grin.mw/t/non-interactive-txs-and-usability>
[3] [Minglejingle: Scalable blockchain with non-interactive transactions - #13 by tromp](https://forum.grin.mw/t/minglejingle-scalable-blockchain-with-non-interactive-transactions/8288/13)
[4] [[bitcoin-dev] BIP70 is dead. What now?](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2021-March/018560.html)

---

### Post by @davidtavarez ⭐ (2021-03-15)
*Post #29*

I totally agree with this:

tromp:

> As the original MW implementation, Grin should embrace its unique properties rather than subvert them for the sake of conformance

I’m completely opposed to this:

tromp:

> turn it into some ugly hybrid in order to save 1 or 2 cut&pastes.

Let me be clear, I think that Grin should embrace its unique properties. **I believe this will pay off at the long term**. That being said…

We must, not only should, **we must** improve Grin’s usability. Removing “1 or 2 cut & paste” is a huge improvement, a big win, and a statement saying: **we do care about simplicity**. Of course, we should no push for an ugly hybrid, but even at least one cut & paste that we remove would be a big difference, a **truly piece or art**.

Let’s imagine a scenario where a user could pay using Grins. The user makes click on “Checkout”, the site generates an Invoice that can be scanned or copied by the user, and after this, the user clicks on “Send”, and done: purchase made.

Another scenario. We’re at the Späti, you paid a beer for me because I only use Grin, no other currency. You open your Android wallet, I open mine, “take the amount of grins out of my wallet” (by setting the amount) and sent the transaction to you. You’re connected to the internet so you can confirm the transaction.

This is like sending literally cash by digital means.

Please, let’s do not undermine the UX because… What will Grin be without users, or miners?

---

### Post by @tromp ⭐ (2021-03-15)
*Post #30*

You seem to have misunderstood me, David.

I’m totally in favor of trying to save 1 or 2 cut&pastes.
We must strive to make transacting as smooth as possible.

But not at ANY price. I’m totally opposed to the current hybrid MW proposals to support non-interactive transactions. For me, the costs of departing from MW, hugely complicating the consensus model, bloating the chain, and compromising the security model, are just too high.

Any less draconian methods of improving usability, I wholeheartedly support.

---

### Post by @david ⭐ (2021-03-15)
*Post #31*

tromp:

> hugely complicating the consensus model

We just need to make sure we get it right. We can spend a year or two iterating on the design and hiring auditors. Complexity just means more upfront work to ensure it’s secure. Once we’re confident the design and implementation are secure, and the code is sufficiently modular (which both node implementations are), then the existence of the complexity has very little lasting effect outside of its impact on throughput (which in this case is relatively minimal).

tromp:

> bloating the chain

There is no permanent chain bloat with the LTC proposal. Outputs grow by 15-20%, but are pruned when spent.

tromp:

> compromising the security model,

As you’ve admitted before, it’s only an “ugly wart” of theoretical interest. It has no practical effect on security.

---

### Post by @tromp ⭐ (2021-03-16)
*Post #51*

david:

> No, I’m proposing to work together with those who oppose the current NITX proposals so we can find the cleanest and safest design that meets the usability needs of our users without sacrificing the prunability and privacy that makes Grin great.

While deviating from Mimblewimble and sacrificing Grin’s simplicity,
one of its main assets.

> those who are hopelessly obsessed

That kind of language does not belong in a civilized discussion.

david:

> at the _extremely high cost_ of practical usability.

Bitcoin lightning shows how interactive transactions can be made quite usable.

david:

> Then why were you so adamantly opposed to implementing a clean solution for preventing replay attacks?

I am adamantly opposed to needlessly complicating the consensus model.

david:

> sometimes using SRS, rather than going with a uniform standard that’s easier to learn.

Because there are advantages to exchanges using RSR for withdrawals. And always being the middle party in both withdrawals and deposits makes for a uniform exchange user experience,

david:

> But refusing to budge even a little to try to find middle ground has led to a painful stalemate whereby nothing ever gets done.

Plenty got done in Grin in its first two years, especially considering the limited manpower. Consensus model changes with significant downsides, which you are pushing for, are exactly the type of change Grin should resist.

Grin should make the UX as easy as possible, but within the confines of staying true to its nature as a clean Mimblewimble implementation.
The extreme simplicity of MW’s transaction model gives it a huge potential for future possibilities beyond just party A sending an on-chain payment to party B. I do not want to diminish that potential by the short-sighted action of making the uncommon act of A paying an offline B slightly more convenient.
I want to optimize Grin for the coming decades, not for the coming years.

david:

> It seems likely we’ll never accomplish anything

You might as well say that the Bitcoin lightning network, which has to operate within the same interactivity confines, will never accomplish anything.

---

### Post by @david ⭐ (2021-03-17)
*Post #53*

tromp:

> While deviating from Mimblewimble and sacrificing Grin’s simplicity,
>  one of its main assets.

It’s main assets are privacy and scalability. Most people don’t care about minimalism: <https://twitter.com/DavidBurkett38/status/1303106005056851971>

tromp:

> Bitcoin lightning shows how interactive transactions can be made quite usable.

I can certainly say this is the first time I’ve ever seen lightning network touted as an example of good usability.

tromp:

> I am adamantly opposed to needlessly complicating the consensus model.

So I guess a clean security model is not such an integral part of Grin’s appeal?

tromp:

> And always being the middle party in both withdrawals and deposits makes for a uniform exchange user experience,

How much time have you spent supporting grin users? I’ve personally spent hundreds, maybe even thousands of hours helping people try to use grin. I know a thing or two about how new users think about transacting. To most users, there is nothing “uniform” about this approach.

How are we supposed to explain to users that receiving from another grin user is different than receiving from an exchange? What happens when some exchanges support RSR, but some support SRS? What about stores - should they use RSR and SRS? How are service providers supposed to decide whether they qualify for exchange-style RSR, or normal style SRS?

Also, why have we given up on trying to support sending via tor? I thought the beauty of slatepacks was the ability to support synchronous in most cases, but fall back to asynch if the receiver is unreachable? Why are we no longer recommending that? Why is it that we continue to make recommendations that make things harder for our users?

tromp:

> Plenty got done in Grin in its first two years

True. Just look how many API and slate versions we’ve implemented!

tromp:

> especially considering the limited manpower.

There’s limited manpower because we launched with possibly the least usable cryptocurrency ever, so the hype died almost immediately and everyone bailed.

tromp:

> I do not want to diminish that potential by the short-sighted action of making the uncommon act of A paying an offline B slightly more convenient.

You can support both itx and nitx. We can do everything in our power to discourage people from using nitx unless absolutely necessary, including trying first to contact the receiver via tor to build transactions interactively, limiting the number of nitx per block, charging additional fees, showing big warnings, etc. There are plenty of ways we could compromise to get what we both want. But compromise never appears to be an option.

tromp:

> I want to optimize Grin for the coming decades, not for the coming years.

So do I, by making sure we actually stay relevant enough to survive decades.

tromp:

> You might as well say that the Bitcoin lightning network, which has to operate within the same interactivity confines, will never accomplish anything.

I didn’t say we will never accomplish anything because we have interactive transactions. I said we will never accomplish anything when one side refuses to search for reasonable compromises. It’s always `minimalism or death`, and sadly it’s starting to seem like Grin might end up with the latter.

* * *

I’m not going to continue these discussions. This coin was once the pinnacle of innovation, and you could just feel everyone’s enthusiasm when discussing new, cutting-edge ways to push mimblewimble to its limits. We used to discuss using BLS to possibly support aggregating kernels or one-sided txs (a much more complex consensus change), and Igno himself was very interested in it as well. We discussed finding alternative accumulators for a constant-sized replacement of MMRs. We were always on the lookout for ways to improve Grin’s privacy or scalability even further. Not all of the ideas were good, but we were at least trying to push the technology forward so we can remain relevant.

But then we launched, hype died, Igno left, and history was rewritten by a small group of minimalists whose one desire seemed to be creating the most simplistic consensus model out there, regardless of its impact on practical usage. Now, it’s not even worth the effort to propose new ideas, because it would be too exhausting and fruitless to try to fight the inevitable political battle that will result. We’ve become so good at minimalism that even our dev community is minimal, with near-silent dev channels outside of our weekly meetings. The dwindling dev community and shrinking userbase should’ve been enough for most people to stop and consider that maybe, just maybe, we aren’t on the right path.

---

### Post by @davidtavarez ⭐ (2021-03-17)
*Post #56*

tromp:

> You seem to have misunderstood me, David.

I was happy to read that I misunderstood you. But what I see is that you’re not willing to compromise anything, it feels like Grin is only about the minimalist MW implementation or nothing. I’ve been repeating this over and over again, and I will say it again: I’m sure this minimalist implementation will payoff in the long term. But, it seems you’re completely ignoring reality.

This is reality:

david:

> The dwindling dev community and shrinking userbase should’ve been enough for most people to stop and consider that maybe, just maybe, we aren’t on the right path.

Also this:

david:

> There’s limited manpower because we launched with possibly the least usable cryptocurrency ever, so the hype died almost immediately and everyone bailed

I noticed a long time ago that, and I hope I’m wrong, the Council isn’t spending a second giving support to users. There is a clear detachment here, between how users are using Grin (the few that are) and this idea of not putting attention to usability. And this is bad, really bad, and leads me to ask myself whether Grin is meant to be used or not.

Every attempt of NITX or 2 round transactions are being discouraged, the Council seems to be against that for the merely fact of being against. When a proposal, uncompleted or not, is made public there is no: “we think this is good, let’s explore this idea and try to make it possible”. There is always the counter-arguments of being insecure, incomplete and/or my favorite: it increases the block size.

tromp:

> I want to respect those limits rather than break them.

And this is great, my question is: is usability in your list at least? are you thinking about the end users?

Sometimes it looks like users are been treaded as some kind of peons that need to be sacrificed in order to achieve… what? This is hurting Grin; we could, of course, condemn all Exchanges for not having in place the “right implementation”, but how will they? if we can not even agree on usability.

---



## [LOCKED] Support Ledger Wallet
*Date: 2021-03-03 | [Forum Link](https://forum.grin.mw/t/locked-support-ledger-wallet/8517)*
*Importance Score: 142.9 | Core Participants: david, tromp, quentinlesceller, lehnberg*

### Post by @quentinlesceller ⭐ (2021-03-03)
*Post #1*

## Description

Hardware wallet support is a feature requested multiple times (e.g. [Grin on Ledger Hardware Wallet - #9 by davidtavarez](https://forum.grin.mw/t/grin-on-ledger-hardware-wallet/1854/9) and [Hardware Wallet Support](https://forum.grin.mw/t/hardware-wallet-support/6999)). Ledger is one of the most popular hardware wallet provider with their Ledger Nano S and Ledger Nano X.

This bounty is for delivering support for Grin on Ledger Wallet.

## Deliverables

**All code must be available on GitHub. Upon completion, the code will be transferred to the[mimblewimble org](https://github.com/mimblewimble) and be licensed under Apache 2.0 License (or similar).**

1. A BOLOS application, written in C, running on a Ledger device. Approved by Ledger Wallet security team and available in the list of applications from the Ledger Live client.
2. Grin Interface on Ledger Live. Support for transactions through Tor and copy pasting of slatepacks following the [Slatepack RFC](https://docs.grin.mw/grin-rfcs/text/0015-slatepack/)

## Requirements

* Knowledge in C (BOLOS App).
* Knowledge in Javascript (integration in Ledger Live).

## Resources

* [Publishing an Application — Ledger Documentation Hub 3 documentation](https://ledger.readthedocs.io/en/latest/additional/publishing_an_app.html)
* Monero BOLOS App [GitHub - LedgerHQ/app-monero: Monero wallet application for Ledger Nano S & X](https://github.com/LedgerHQ/app-monero)
* From Ledger website, you’ll need “A transaction explorer that interfaces between the front-end and the cryptocurrency daemon, running either locally (in the case of a full node) or remotely (light wallet).” Basically, either a full node or a way to check transaction status and interact with the network (push tx). [@mcm-mike](/u/mcm-mike) high availability API can be something worth considering.

# Amount Available

50k USD.
_If you feel that this amount should be higher please provide a new amount alongside reasonable arguments in your proposal._

---

### Post by @tromp ⭐ (2021-03-06)
*Post #3*

Thanks for providing your extensive design considerations!

Vlad:

> We actually implemented it, and have our custom firmware for Trezor and Ledger. However they didn’t include our code in their official firmware so far.

Are they still conducting tests? Does Ledger provide any timelines on how long it takes to to go from code submission to firmware release?

---

### Post by @quentinlesceller ⭐ (2021-03-06)
*Post #6*

Hi [@vlad](/u/vlad), thank you for your input ! Do you have a link for the Beam Ledger firmware code?

---

### Post by @quentinlesceller ⭐ (2021-03-09)
*Post #10*

In the first place, connecting the ledger app to grin-wallet would probably be an excellent start.

---

### Post by @tromp ⭐ (2021-03-10)
*Post #13*

markhollis:

>   * Implement Receive transaction. I would start with this transaction type.
>   * Sign kernel and payment proof.
>   * Implement Send transaction. As this transaction type is more complex, I would implement this in a later phase.
>   * Verify payment proof was signed by receiver.
>   * Implement Split transaction.
>

Note that Grin uses different signature schemes for signing kernels (secp256k) and signing payment proofs (ed22519). I hope that the Ledge Nano S can support the use of both under a single coin type.

Although it hasn’t been finalized yet, I hope you can make provisions to support the more general payment proofs in this RFC: <https://github.com/tromp/grin-rfcs/blob/early-payment-proofs/text/0000-early-payment-proofs.md>
It might make sense to allow the memo to be as long as the maximum that can be shown on the Ledger device.

What is a Split transaction?

---

### Post by @lehnberg ⭐ (2021-03-14)
*Post #17*

[@markhollis](/u/markhollis) thanks for this thorough application!

The meeting Quentin refers to above is [Agenda: Governance Mar 16 2021 · Issue #403 · mimblewimble/grin-pm · GitHub](https://github.com/mimblewimble/grin-pm/issues/403), if you can make it, it would be great to have you present answering any questions.

---

### Post by @tromp ⭐ (2023-07-07)
*Post #28*

NicolasFlamel:

> Here’s all the tasks and subtasks required to complete this bounty

Out of curiosity, did you receive any funding for developing Ledger support for the MWC wallet?

---

### Post by @tromp ⭐ (2024-03-23)
*Post #37*

NicolasFlamel:

>   1. Remove the requirement of needing Ledger to officially release the app and integrate the Ledger Live changes.
>   2. Remove the requirement for a grin-wallet CLI integration.
>   3. Increasing the bounty’s reward from 50k USD to 100k USD.
>

Our sincere apologies for the late response.

The Grin Council has decides to partially agree with 1, fully agree with 2, and to disagree with 3.

75% of the original bounty can be paid out immediately, and the remaining 25% can be paid out once the Ledger app has been reviewed and approved by Ledger.

Please contact any OC member to arrange payment.

EDIT: Nicolas has been paid on Mar 24.

---



## Grin testnet exchange example
*Date: 2021-03-11 | [Forum Link](https://forum.grin.mw/t/grin-testnet-exchange-example/8570)*
*Importance Score: 77.6 | Core Participants: david, tromp, davidtavarez*

### Post by @vegycslol (2021-03-11)
*Post #1*

I’ve created a simple grin testnet exchange example so that we can play with it, analyze the flow and try to improve its UX and security. I would call it some kind of a beta version since it probably has some bugs and security issues, so sorry in advance for that, will try to fix them asap (i know i still need to check some stuff but i’ve decided to let you play with it to not delay this any longer). I might reset the database when doing upgrades if I won’t feel like bothering with the updates so you might lose your coins on the exchange because of it. But you should not be keeping the coins on this test exchange anyway.
Current grin-wallet rust implementation has some wallet-api bugs, so i’ve forked it and the testnet exchange is currently using [this branch](https://github.com/pkariz/grin-wallet/tree/fix/invoice-issues) \- i could create a PR but since i’m not that familiar with rust and grin-wallet i’m not sure if my fixes are appropriate and don’t break some other stuff.

# Implementation

For those who like to dive into the code, [here](https://github.com/pkariz/grin-testnet-exchange) it is. The most important files are `backend.api.views.py` and `backend.api.tasks.py`. Thanks to [@bladedoyle](/u/bladedoyle) and [@xiaojay](/u/xiaojay) for their python wallet and node api implementation (i’ve partially done it myself, then blade showed me their implementation so i’ve reused the rest). Also thanks to [@david](/u/david) for helping me understand some grin-wallet basics which helped me fix the grin-wallet api issues that were needed for this exchange to work.

## Deposit and Withdrawal

I used django and vue (both are very readable and i know them, so yeah good reasons :D).
Deposits are done through invoice flow (RSR), Withdrawals are done through payment flow (SRS). This seems the best to me because it makes the flow practically the same for the user to do both and at the same time exchange is the one responsible for finalizing stuff (well i would hope they know more about how to do that than the users). In withdrawal we require a payment proof, in deposits we don’t since payment proofs for invoice flows are not yet implemented. In both cases the user gets an encrypted slatepack for his wallet and after he performs “pay” (deposit) or “receive” (withdrawal) the generated slatepack is also encrypted for the exchange’s wallet.

## Confirmations update

I wasn’t sure how to check for confirmations so what i do is i store the kernel of deposit/withdrawal and then each minute i have a task which gets the current height and checks the height of all “active” deposits/withdrawals and updates number of confirmations. Until there are 10 confirmations the funds are locked, after that they’re unlocked (in the case of deposit that means they become useful, in the case of withdrawal they disappear). User can only have 1 active deposit (eg. waiting for user’s signature), if he creates another one, the old one gets canceled (tx is also canceled, but as we know grin-wallet currently doesn’t have a proper cancel implemented yet so that might not be the best).

## Automatic transaction rebroadcast

I’ve wanted to do that through the “repost”, but wallet-api doesn’t have it implemented yet and i wasn’t sure if i can just pass everything to the owner api or not, so i didn’t implement that. The idea was to automatically try to rebroadcast the transaction if it didn’t land on chain for 30 minutes or so (should reduce the number of tickets an exchange gets).

For more detailed explanation on how to deposit and withdraw you can click on **Instructions** at the top-left corner on the website.

# Important

This is a testnet exchange example, security is probably not the best, so no, it was not built to be anything more than a testnet exchange and there is no plan for it to be anything more than that.

# Getting testnet coins

One way to get testnet coins is through faucet. The faucet communication works through TOR so you need to have it installed on your system and then run `grin-wallet --testnet listen` to listen for TOR communication (when you run this command it will output that you don’t have TOR if you don’t have it installed). Then run `curl -d '{"address": "<your wallet address>"}' http://faucet.testnet.grin.lesceller.com` \- that’s basically “please send me 1 grin”. You get 1 grin for each call, can do this up to 5 times i think - probably per day or smth - thanks to [@quentinlesceller](/u/quentinlesceller) for the faucet

# Website

<https://exchange.learngrin.com/>

# Bug reporting

Either write it here or open an issue on [github repo](https://github.com/pkariz/grin-testnet-exchange)

---

### Post by @davidtavarez ⭐ (2021-03-11)
*Post #2*

This is great! Thanks for the effort! Maybe you mentioned before, but why you called “contract” to the slatepack?

I think we should have an **Airdrop** of testnet grins to play with this

---

### Post by @david ⭐ (2021-03-11)
*Post #5*

This is really cool, but why exclude the majority of users? None of the GUI or mobile wallets support invoices AFAIK. So they can’t even test this. And since invoices don’t have payment proofs, they aren’t even secure yet.

And reinventing the terminology just means we’re now suggesting non-standard terminology for exchanges who want to use this as a model.

I’d be happy to help fix these critical issues so we have something we can point to for other exchanges to adopt.

---

### Post by @tromp ⭐ (2021-03-11)
*Post #6*

david:

> None of the GUI or mobile wallets support invoices AFAIK.
>  …
>  I’d be happy to help fix these critical issues

So you’ll add testnet invoice support to Grin++ :-?

---

### Post by @david ⭐ (2021-03-11)
*Post #9*

vegycslol:

> this implementation would be the one i would suggest to the exchanges

But it’s not even one that’s secure today, nor is it one that the overwhelming majority of developers agree with. The fact that no GUIs support invoices should be an obvious indicator that your opinion is not shared by everyone. Why make controversial choices when this is supposed to be something we can point to as an example for exchanges to follow? I can no longer do that with the way you’ve designed it.

---

### Post by @david ⭐ (2021-03-11)
*Post #11*

vegycslol:

> I feel like RSR/SRS is my answer and SRS/SRS is yours

I think SRS/SRS is the easiest, most obvious answer. Besides, we’ve had issues in the past with exchanges not broadcasting right away. We want to make sure we aren’t making it even easier for transactions to get delayed due to poor exchange implementations of RSR (just because you show exchanges a good example of doesn’t mean they’ll follow it exactly).

vegycslol:

> My opinion is that every gui wallet should support the invoice flow

My opinion is that bad UX choices should not keep getting forced on every GUI wallet. The big advantage of having competing 3rd party wallets is we have freedom to experiment with what does and doesn’t work. I’ve personally experimented and concluded invoices don’t work well.

---

### Post by @david ⭐ (2021-03-11)
*Post #13*

vegycslol:

> users will be unhappy, they will be getting many more support tickets and users will move to other exchanges.

That’s not really how it has worked in practice. TO has done the best job of implementing it, but they don’t get used much because of liquidity issues. People use the exchange they’re most familiar with, not the one that does the best job at supporting Grin.

vegycslol:

> i found it quite pleasant to work with

What is so pleasant about it? It’s not like it simplifies the UX at all, and it actually makes it a bit worse in some cases, since you have to add deposit amount.

Say you want to send your max balance, you have to go to your wallet and do an estimate send for max balance, copy that amount and go back to the exchange to enter the amount and the address. Then back to your wallet, then back to the exchange. It’s an extra step.

---

### Post by @davidtavarez ⭐ (2021-03-12)
*Post #24*

The code is in Python, I think this is a good opportunity for people to get involved and learn more about Grin. What do you think about instead of adding support for both within the same source code, maybe just clone it and run it in different subdomains as [@oryhp](/u/oryhp) expressed?

I think if you over complicate the code it would be hard to follow, but also I think that by separating the code anyone could go and help you (potentially). Both flows are different, so the challenges too, but having both implementations will definitely help us educating users, and also we will have a better picture of what is simpler. I understand that current implemented flow (RSR) seems to be better from the exchange perspective, but without having payment proofs for invoices, it feels incomplete. I’m happy to see Grin++ users playing with this testnet exchanges, and, again, this can be used to educate.

I honestly feel lost using the CLI after using Grin++

---



## Grin ledger hardware wallet progress thread by @markhollis
*Date: 2021-03-30 | [Forum Link](https://forum.grin.mw/t/grin-ledger-hardware-wallet-progress-thread-by-markhollis/8670)*
*Importance Score: 265.8 | Core Participants: tromp*

### Post by @markhollis (2021-03-30)
*Post #1*

Hello,

Here I will post my updates about the work I’m doing for implementing Ledger hardware support. See this thread: [[LOCKED] Support Ledger Wallet](https://forum.grin.mw/t/locked-support-ledger-wallet/8517)

The past two weeks I started working on the connection between Grin++ and Ledger.

There are two projects I am now working on: the Grin++ hardware wallet support and the Ledger device app.

Now I’m working on the USB communication code on the Grin++ side.

After this goes well, here are some tasks I can already anticipate:

I plan to look at how to implement other setup functions like key derivation, setting PIN and passphrase.

I will also look at integrating some of the C embedded code that Vlad posted previously. Notably the cryptographic primitives, such as rangeproofs. These are things that will be reused.

After this, I will start working on the transactions: defining the UI screens, the different commands that must happen during the different types of transactions.

---

### Post by @markhollis (2021-04-27)
*Post #6*

Update for the weeks 13/04 to 27/04:

* I have been looking about how to open an existing hardware wallet on the desktop side. I have looked at how the Monero project approached this issue. The way they do this, is that when the wallet is created, an view key is generated on the device, sent to the host and serialized in a file.
* I have learned more about the MW/Grin cryptography in depth, as I felt I was lacking in this area. I started looking in detail at the Beam
* I started integrating code in the grin-wallet and created a pull-request for some files.
* Added the secp256k1-zkp library to the app firmware.

Next will be further integration, and looking more into cryptography specific components.

---

### Post by @tromp ⭐ (2021-04-28)
*Post #8*

Yes, Grin does have view keys, just like Monero; see

[github.com](https://github.com/mimblewimble/grin/blob/master/keychain/src/view_key.rs)

#### [mimblewimble/grin/blob/master/keychain/src/view_key.rs](https://github.com/mimblewimble/grin/blob/master/keychain/src/view_key.rs)

// Copyright 2021 The Grin Developers
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use crate::blake2::blake2b::blake2b;
use byteorder::{BigEndian, ByteOrder};
//use crate::sha2::{Digest, Sha256};
use super::extkey_bip32::{
BIP32Hasher, ChainCode, ChildNumber, Error as BIP32Error, ExtendedPrivKey, ExtendedPubKey,
Fingerprint,

This file has been truncated. [show original](https://github.com/mimblewimble/grin/blob/master/keychain/src/view_key.rs)

---

### Post by @markhollis (2021-05-25)
*Post #13*

Update for weeks 11/05 to 25/05.

* Researched initialization and sender/receiver wallet functions further + implementation.
* Made an interface that encapsulates the logic for dealing with the device and keys, similar to how Beam uses a KeyKeeper interface.
* I researched rangeproofs somewhat these weeks, but it isn’t yet clear to me how I should approach this further. I’ve been reading through [GitHub - AdamISZ/from0k2bp: From Zero (Knowledge) to Bulletproofs - writeup](https://github.com/AdamISZ/from0k2bp) and through how BP’s are used in grin. Here ([grin/proof.rs at 1b8acee72e7a4236cdf8561a7af5f894bfe11985 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/1b8acee72e7a4236cdf8561a7af5f894bfe11985/core/src/libtx/proof.rs#L28)) it seems like BP’s should be created at the device. Creating BP’s is however computationally expensive for the HW. Maybe the HW should do only the part before the call to secp.bullet_proof()?
*One thing I’m thinking of as I write this, in grin-wallet, an input is a Vec<(Identifier, Option, u64). The Option<64> is an mmr_index. See: [grin-wallet/types.rs at bdc5bd748a4e399e6febc5e3c4974e569ee39638 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/blob/bdc5bd748a4e399e6febc5e3c4974e569ee39638/libwallet/src/types.rs#L553). I should look into how this MMR index is generated.
* I did some work again on the Grin++ side. I found a C++ library to work with Ledger, which I can communicate with the device. The plan here is to implement the same ideas as I already did in the grin-wallet. Furthermore, it is informing to see two implementations of the protocol; it makes somehow the protocol more clear to me at certains points.
* I made a document for grin-wallet and Grin++, for listing parts in the source code that should be delegated to the HW wallet. (The documents cointain permalinks and some comments about the code structure.) However, these are not ready to share yet.

---

### Post by @tromp ⭐ (2021-09-01)
*Post #28*

markhollis:

> ed25517 curve

That curve is new to me:-)

---

### Post by @markhollis (2021-09-15)
*Post #33*

Implementing the rangeproof part is challenging. Here are some notes about the use of rangeproofs in grin-wallet. It can contain faults or inconsistencies and it is certainly incomplete.

## Related work

There is some previous work done on rangeproofs in Monero

[github.com](https://github.com/LedgerHQ/app-monero)

### [GitHub - LedgerHQ/app-monero: Monero wallet application for Ledger Nano S & X](https://github.com/LedgerHQ/app-monero)

Monero wallet application for Ledger Nano S & X

There is a publication on a Monero Trezor implementation
See:

* <https://eprint.iacr.org/2020/281.pdf>
* [GitHub - ph4r05/monero-tx-paper: Repository related to the paper "Privacy-friendly Monero transaction signing on a hardware wallet"](https://github.com/ph4r05/monero-tx-paper)

Monero has switched to BP++.

There is also the Beam HW wallet implementation.
I haven’t studied these implementation in depth yet.

If someone knows related work regarding implementations of Bulletproofs on Ledger/Trezor, let me know.

In the following, I will give some comments on the rangeproof code, as it is used in Grin.

## Rangeproof

* Rangeproof signing is calculated by the HW. Note that Rangeproof validation will happen by the host.

* “A rangeproof is therefore attached to every output and proves that its value isn’t negative and that its size is restricted so it doesn’t overflow”. [Mimblewimble - Grin Documentation](https://docs.grin.mw/wiki/introduction/mimblewimble/mimblewimble/#rangeproofs) Rangeproof creating is done in the receiver action.

* The Rangeproof field in the struct Output is here defined: [grin/core/src/core/transaction.rs at f51b6e13761ac4c3c8e57904618ef431c14c6227 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/f51b6e13761ac4c3c8e57904618ef431c14c6227/core/src/core/transaction.rs#L2014)

* (Here the proof is verified. pub fn verify_proof(&self) → Result<(), Error>: [grin/core/src/core/transaction.rs at f51b6e13761ac4c3c8e57904618ef431c14c6227 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/f51b6e13761ac4c3c8e57904618ef431c14c6227/core/src/core/transaction.rs#L2121) )

* The build::output() method fn output<K, B>(value: u64, key_id: Identifier) is defined here. It calls the proof::create function. [grin/core/src/libtx/build.rs at 1b8acee72e7a4236cdf8561a7af5f894bfe11985 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/1b8acee72e7a4236cdf8561a7af5f894bfe11985/core/src/libtx/build.rs#L112)

* This creates the rangeproof/bulletproof itself: [grin/core/src/libtx/proof.rs at 1b8acee72e7a4236cdf8561a7af5f894bfe11985 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/1b8acee72e7a4236cdf8561a7af5f894bfe11985/core/src/libtx/proof.rs#L28)

* An output with a given rangeproof (created in the previous method) is created here: [grin/core/src/core/transaction.rs at f51b6e13761ac4c3c8e57904618ef431c14c6227 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/f51b6e13761ac4c3c8e57904618ef431c14c6227/core/src/core/transaction.rs#L2078) This method is used in the output function above: tx.with_output(Output::new(OutputFeatures::Plain, commit, proof)),

* The previous is then used in the receive action., using tx::add_output_to_slate() ([grin-wallet/libwallet/src/internal/tx.rs at 8547f4a162b466a1dacef63df2282b34c3964e78 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/blob/8547f4a162b466a1dacef63df2282b34c3964e78/libwallet/src/internal/tx.rs#L206)), which then calls build::output [grin/core/src/libtx/build.rs at f51b6e13761ac4c3c8e57904618ef431c14c6227 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/f51b6e13761ac4c3c8e57904618ef431c14c6227/core/src/libtx/build.rs#L112)

Other interesting parts in the Wallet layer:

* test_rewind_range_proof(): [grin-wallet/libwallet/tests/libwallet.rs at bdc5bd748a4e399e6febc5e3c4974e569ee39638 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/blob/bdc5bd748a4e399e6febc5e3c4974e569ee39638/libwallet/tests/libwallet.rs#L458)

Now for the bulletproof algorithm itself:

* It derives a secret key, using the secp256k1 curve. ([grin/core/src/libtx/proof.rs at 1b8acee72e7a4236cdf8561a7af5f894bfe11985 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/1b8acee72e7a4236cdf8561a7af5f894bfe11985/core/src/libtx/proof.rs#L46)) This should happen on the HW.

* Private nonce is created using this method: [grin/core/src/libtx/proof.rs at 1b8acee72e7a4236cdf8561a7af5f894bfe11985 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/1b8acee72e7a4236cdf8561a7af5f894bfe11985/core/src/libtx/proof.rs#L277) Likely this must happen on the HW (I’m not sure).

* It then call the secp.bullet_proof(), using the FFI and the secp256k1 library. [GitHub - mimblewimble/rust-secp256k1-zkp: ZKP fork for rust-secp256k1, adds wrappers for range proofs, pedersen commitments, etc](https://github.com/mimblewimble/rust-secp256k1-zkp)

* pub fn range_proof() [rust-secp256k1-zkp/src/pedersen.rs at 4128f64505143859c48fab04158c25127a2a9858 · mimblewimble/rust-secp256k1-zkp · GitHub](https://github.com/mimblewimble/rust-secp256k1-zkp/blob/4128f64505143859c48fab04158c25127a2a9858/src/pedersen.rs#L576)

* ffi::secp256k1_rangeproof_sign() called: [rust-secp256k1-zkp/src/pedersen.rs at 4128f64505143859c48fab04158c25127a2a9858 · mimblewimble/rust-secp256k1-zkp · GitHub](https://github.com/mimblewimble/rust-secp256k1-zkp/blob/4128f64505143859c48fab04158c25127a2a9858/src/pedersen.rs#L605)

* int secp256k1_rangeproof_sign() ([secp256k1-zkp/src/modules/rangeproof/main_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/rangeproof/main_impl.h#L73)) acts mainly as a checker for the arguments, to call secp256k1_rangeproof_prove(). blind is here the secret key. The normal case, with tau_x, t_one, t_two and commits equal to NULL, seems to be the simplest case.

* secp256k1_rangeproof_prove() is here: [secp256k1-zkp/src/modules/bulletproofs/main_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/main_impl.h#L184)

* Beginning, lots of checks that the arguments are correct

* Commitment is calculated from Blindingfactor, must happen on the device I think.

* Main functions called seem to be these two:

* secp256k1_pedersen_commitment_load: [secp256k1-zkp/src/modules/bulletproofs/main_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/main_impl.h#L251) But this is in the multi party case.
* secp256k1_bulletproof_rangeproof_prove_impl call: [secp256k1-zkp/src/modules/bulletproofs/main_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/main_impl.h#L280)
* Parameters: blind: 32-byte blinding factor used by commit. nonce: 32-byte secret nonce used to initialize the proof (value can be reverse-engineered out of the proof if this secret is known.)

* This is part of the BP normal case. Code in this block should be done on the HW, as it uses the blinding factor. [secp256k1-zkp/src/modules/bulletproofs/main_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/main_impl.h#L243) This requires EC multiplication, for which I’ve seen example code, not using secp256k1, but the Ledger SDK.

* secp256k1_bulletproof_rangeproof_prove_impl implementation: [secp256k1-zkp/src/modules/bulletproofs/rangeproof_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/rangeproof_impl.h#L431)

* This secp256k1_lr_generator_init methods needs to be done on the HW, as it uses the secret nonce: [secp256k1-zkp/src/modules/bulletproofs/rangeproof_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/rangeproof_impl.h#L589)

* I don’t understand the usage of gen and blinding gen at the moment

* This needs to be done on the HW, uses blind: [secp256k1-zkp/src/modules/bulletproofs/rangeproof_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/rangeproof_impl.h#L667)

* This method (inner product proof secp256k1_bulletproof_inner_product_prove_impl) doesn’t use nonce or blind, so it doesn’t need in principle the HW?: [secp256k1-zkp/src/modules/bulletproofs/rangeproof_impl.h at 8d1f5bb152580446a3438cd705caebacc2a5d850 · mimblewimble/secp256k1-zkp · GitHub](https://github.com/mimblewimble/secp256k1-zkp/blob/8d1f5bb152580446a3438cd705caebacc2a5d850/src/modules/bulletproofs/rangeproof_impl.h#L716)

This note is certainly incomplete, especially the analysis of the Bulletproof algorithm itself.
The question I have is how to offload the part which uses the secret nonce and blinding factor to the HW. Perhaps studying related work will help here. If there are suggestions, they are very welcome.

---

### Post by @vek (2021-09-22)
*Post #34*

markhollis:

> ted work will help here. If there are suggest

If you wish, you could work in collaboration with Nicolas Flamel. He made some good advancement on his own MWC ledger integration.

[GitHub](https://github.com/NicolasFlamel1/ledger-mimblewimble-coin)

### [GitHub - NicolasFlamel1/Ledger-MimbleWimble-Coin: MimbleWimble Coin (MWC),...](https://github.com/NicolasFlamel1/ledger-mimblewimble-coin)

MimbleWimble Coin (MWC), Grin (GRIN), and Epic Cash (EPIC) Ledger hardware wallet apps. - GitHub - NicolasFlamel1/Ledger-MimbleWimble-Coin: MimbleWimble Coin (MWC), Grin (GRIN), and Epic Cash (EPIC...

---

### Post by @MegaSega (2022-12-16)
*Post #76*

Doesn’t Grin already work with ledger hardware wallets??

[twitter.com](https://twitter.com/grin_privacy/status/1595951830571155456?s=20&t=E8tDDRG85i8sYwkFkAaUSQ)

#### [Grinツ](https://twitter.com/grin_privacy/status/1595951830571155456?s=20&t=E8tDDRG85i8sYwkFkAaUSQ)

[@grin_privacy](https://twitter.com/grin_privacy/status/1595951830571155456?s=20&t=E8tDDRG85i8sYwkFkAaUSQ)

Q: wen $grin ledger A: right here ser! [reddit.com/r/grincoin/com…](https://www.reddit.com/r/grincoin/comments/z39ebv/grin_ledger_hardware_wallet_support/?utm_source=share&utm_medium=web2x&context=3) <https://t.co/kpkMFrJTrd>

[1:25 AM - 25 Nov 2022](https://twitter.com/grin_privacy/status/1595951830571155456?s=20&t=E8tDDRG85i8sYwkFkAaUSQ) 69  17

---


