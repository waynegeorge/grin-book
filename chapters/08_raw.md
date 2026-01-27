# Chapter 8: Governance Evolution

*25 topics selected for this chapter*

---

## Request for Funding: BLS sigs research
*Date: 2020-04-13 | [Forum Link](https://forum.grin.mw/t/request-for-funding-bls-sigs-research/7257)*
*Importance Score: 90.0 | Core Participants: antioch, yeastplume, quentinlesceller, tromp, lehnberg*

### Post by @DrazenV (2020-04-13)
*Post #1*

This is a request for funding for a research project in compliance with Grin’s open research problems (<https://grin.mw/open-research-problems>).

As this is my first funding request, the project is kept narrow and focused. It is my intention, however, to contribute to Grin’s research in the long term.

The project is to address the first problem on the list, which is to further investigate BLS signatures and their suitability to Grin (see also <https://github.com/mimblewimble/grin/issues/2504>).

The funding sought are for €5000 and the project time frame is a single month.

After discussing with several community members, it is my understanding that the main interest in BLS signatures is for kernel aggregation (due to the (non-interactive) signature aggregation ability), while the worries are mainly about the security guarantees.

After reviewing the materials on Grin’s different platforms and talking with community members, it seems to me that the disadvantages of BLS are fairly articulated, while the potential benefits are to be further investigated.

The main objectives of the project are the following:

* Put simple the security assumptions and explain the known vulnerabilities due to state-of-the-art attacks.

* **Initial** research on how BLS could be used for kernel aggregation.

* Get myself exposed to other features and research problems, like scriptless scripts and non-interactive transactions.

The last two objectives are an initial preparation for future contribution.

In more detail, my plan is the following:

* Review the security of BLS and pairing-based cryptography – I have very good knowledge in the area, yet there are new assessments (due to recent attacks) about the size of the curve’s base field needed in order to obtain a desired bit security.

* Review how BLS may enable kernel aggregation and hopefully proposing an initial construction – the advantage of BLS is straightforward due to the signature and public key aggregation ability; it remains to understand how such construction should look for the purposes of Grin, I had some discussion about it on keybase.

* Study GandalfThePink’s “BLS signatures in Mimblewimble” proposal (<https://github.com/mimblewimble/grin/issues/2504#issuecomment-467446197>), which includes kernel aggregation and some sort of non-interactive transaction process – I have already started studying this proposal, yet the full construction remains unclear.

* Understand the implications on scriptless scripts – I have no prior knowledge.

* [optional] Addressing related issues, if raised (e.g. efficiency: since the arithmetic involved in BLS is more complicated than simple elliptic curve operations, verification is significantly less efficient than other (elliptic curve based) signature schemes).

My plan is to finalise the project in one month time.

**About me**

My formal education is at the level of a PhD, which is in mathematics and specifically the mathematics of public key cryptography; this also includes post-quantum cryptography. I worked as a post doctoral researcher for a year and a half, and for over a year, until recently, I have been working as a researcher for a funded blockchain project (still in development, currently running testnet) - I am not involved with this project anymore.

I got exposed to mimblewimble about a year ago. My interest in this novel approach was immediate, but I was too busy to carefully study it. I would like to change this now.

The funding would allow me to put a focus on researching mimblewimble.

---

### Post by @lehnberg ⭐ (2020-04-13)
*Post #2*

Thanks for this, I’m glad to see a request coming in for our Open Research Problems!

Funding request added as a point in the agenda for the next governance meeting on [April 21 @ 3PM UTC](https://github.com/mimblewimble/grin-pm/issues/276).

---

### Post by @tromp ⭐ (2020-04-14)
*Post #4*

DrazenV:

> My formal education is at the level of a PhD, which is in mathematics and specifically the mathematics of public key cryptography; this also includes post-quantum cryptography.

Do you have any of your research papers publicly available?

---

### Post by @quentinlesceller ⭐ (2020-04-14)
*Post #5*

Hi [@DrazenV](/u/drazenv). Welcome  :).

I’m very happy to finally see a funding request!

There is a lot to discuss in your request but it’s a good start!

First and foremost do you want to stay anonymous? We would need something like previous work, publications or anything that can validate the education/skills mentioned above. Thank you!

---

### Post by @antioch ⭐ (2020-04-15)
*Post #7*

Hi [@DrazenV](/u/drazenv). This sounds really interesting. Thank you for putting a proposal together.
I’m wondering if maybe it makes sense to split this proposal out into pre-requisite work followed by a proposal for subsequent research.

DrazenV:

> Review how BLS may enable kernel aggregation and hopefully proposing an initial construction – the advantage of BLS is straightforward due to the signature and public key aggregation ability; it remains to understand how such construction should look for the purposes of Grin, I had some discussion about it on keybase.

This is likely a pre-requisite, with a solid understanding of this necessarily in place before we can really start thinking about the tradeoffs inviolved with a BLS solution.

DrazenV:

> Study GandalfThePink’s “BLS signatures in Mimblewimble” proposal ([https://github.com/mimblewimble/grin/issues/2504#issuecomment-467446197 ](https://github.com/mimblewimble/grin/issues/2504#issuecomment-467446197)), which includes kernel aggregation and some sort of non-interactive transaction process – I have already started studying this proposal, yet the full construction remains unclear.

This is very likely a pre-requisite. It would be really valuable for the wider community if somebody could take time to review this in detail with a thorough understanding of how this relates to various earlier BLS discussions.
Is this technically possible? Is the proposal solid?

DrazenV:

>   * Understand the implications on scriptless scripts – I have no prior knowledge.
>

This is a pre-requisite. Any further research, at least directionally, should consider the implications here.

So maybe one way to approach this would be a “literature review” to summarize where we stand today, taking the above into account.

* Schnorr signatures and lack of signature aggregation
* BLS signature aggregation and how this relates to Grin transaction kernels today
* GandalfThePink proposal for non-interactive transactions (summary of what is being proposed and why it does or does not work)

This would give us a solid baseline and starting point for evaluating further possible research and investigation.

With this summary of our current “state of play” I suspect a funded 1 month research project would naturally emerge.

---

### Post by @DrazenV (2020-04-15)
*Post #8*

Thanks for looking at the proposal.

If applicable, I would like to stay anonymous, though I wouldn’t like to make a big deal of it. It is mainly my will to keep myself private (or rather unlinkable) online as much as possible.

If it matters, since I value my privacy I priced my proposal to take that into account (to be clear: I won’t change the funding request in any case, but I hope it is something that will be taken into account). I understand the concern and will take a couple of days to consider the right approach for me. I am happy to hear from the community for suggestions.

Again, I don’t want this to become an issue.

antioch:

> I’m wondering if maybe it makes sense to split this proposal out into pre-requisite work followed by a proposal for subsequent research.

First I’d like to say that I am happy to revise my proposal with feedback from the community about Grin’s needs, as long as it fits my expertise. That is why I took the time to discuss on keybase and understand what are the main community interests before submitting this proposal.

Secondly, I basically agree with the view in [@antioch](/u/antioch)’s post. Besides of the first task, which is to review the current attacks on elliptic curve pairings (actually DLP in extention fields) and the subsequent implications (I already know of several claims that the popular curve called “BLS381-12” does not provide the standard 128 bit security), the other tasks are indeed a preparation/ pre-requisites for further research. I hope that it is already clear in my proposal.

I tried to explain in my proposal that I am asking for the funding in order to be able to dedicate more time into researching Grin.
For example, I know that there’s a lot of interest in the “BLS signatures in Mimblewimble” document. I looked at this proposal several times, and I actually don’t believe that the aggregation proposed there works. But in order to formally convince myself that this is the case, I need to study it more thoroughly. Another example is some recent discussions about non-interactive txs, that should be carefully studied.

I am more than happy to hear what the community thinks. In particular, if we break the tasks, what should be the top priority.

---

### Post by @Kurt (2020-04-15)
*Post #10*

“I priced my proposal to take that into account”

Are you kidding ?

Full time professors earn about this amount of money per month in France (5,000euros). Associates half of this. And it often is for ten years after they have finished their phD.

You have proven nothing to the community, you are new, and probably lying about your credentials, and you want to ask for a salary that junior lawyers don’t even win per month (in France), while sitting on your desk and working on introductionary problems that you could be doing by yourself and provided no proof that you can do them.

If I am rude, it is because I take the very fact that you stay anonymous in this context as something very alarming and disrespectful to the persons that take the time to give attention to your proposal. at least to me.

It doesnt take a phD to understand that, given you are totally unknown by everyone here, you have to provide proof (and it would not even be sufficient) that you did what you claimed you did. not doing that does not demonstrate a lot of maturity and a lot of effort from your side.

For my personal opinion, even if you have done a phD and a post doc, it is not sufficient to give 5,000 euros for someone that just proposes to introduce himself to problems that don’t even take a phD or a Master degrees to learn and understand.

5,000 euros. Any junior phD that may have more knowledge than you (we still do not know if your phD or post doc are something you really did) would dream about.

And I am not saying all that so that you lower your request.
I am saying that because I find it disrespectful for our times that you pretend you have to think about giving your identity or not for a few days.

You could have thought of that before I think.
The question and the concern about your identity has been raised since one week on keybase, and you just ignored and responded nothing

For how much more time do you want to make us lose our time ?

---

### Post by @Yeastplume ⭐ (2020-04-16)
*Post #13*

DrazenV:

> My formal education is at the level of a PhD, which is in mathematics and specifically the mathematics of public key cryptography; this also includes post-quantum cryptography. I worked as a post doctoral researcher for a year and a half, and for over a yea

In addition to some of the concerns listed above, I have to say I find the way this is worded very ambiguous. Do you have a PhD in mathematics or not?

---



## Request for funding / Antioch / Jul-Sep 2020
*Date: 2020-06-20 | [Forum Link](https://forum.grin.mw/t/request-for-funding-antioch-jul-sep-2020/7458)*
*Importance Score: 87.0 | Core Participants: davidtavarez, antioch, lehnberg*

### Post by @antioch ⭐ (2020-06-20)
*Post #1*

I am currently funded through until the end of June ([previous funding request](https://forum.grin.mw/t/request-for-funding-antioch-apr-jun-2020/7183)).
I would like to request a further **3 months** of funding to cover July through to September.
This would be for the standard yeastunit of **€10k/month**.

I have been almost exclusively focused on Grin node over the past few months, specifically NRD kernel support and ongoing work on node stability and performance etc.
I am looking to shift my focus a little over the next few months and spend at least a portion of my time with Grin wallet.
There are a few wallet features under discussion that I would like to get involved with and put some time toward.

1. [“mostly” lock free transactions](https://forum.grin.mw/t/mostly-lock-free-transactions/7313)
2. [PayJoin aka Pay-To-EndPoint (P2EP)](https://blockstream.com/2018/08/08/en-improving-privacy-using-pay-to-endpoint/)
3. multi-party outputs for [Succint Atomic Swaps](https://www.reddit.com/r/BitcoinDiscussion/comments/gi6led/sas_succinct_atomic_swaps_half_the_number_of/)
4. Payment channel implementation (leveraging NRD relative locks and multi-party outputs)

These all share some commonality, specifically around the interactive transaction building process, fine-grained control over output selection and kernel offset adjustments.

We currently support a relatively limited and “simplified” single-round transaction building protocol, supporting a single sender and a single receiver. (1) and (2) require more flexible output selection and flexibility of kernel offset adjustments. (3) and (4) actually require a different and more complex transaction building protocol. We need support for “three-round” [musig](https://blockstream.com/2019/02/18/en-musig-a-new-multisignature-standard/) with secure communication of random nonce values etc.

We will likely not implement all of these in the next few months but I would like us to be thinking about them collectively and to ensure we do not implement one at the expense of making subsequent changes harder.

So while I was focused on activating NRD kernel support at the node p2p protocol layer (on floonet for testing) for HF3 I suspect my HF4 focus will shift to wallet related support for musig and improved transaction building flexibility.

It will be interesting to see what we can do with the Grin wallet to support this additional complexity while keeping the UI/UX as simple and robust as possible.

Alongside this shift in focus toward wallet I’m also aiming to continue spending time on node itself.
We have one final scheduled hardfork at the end of the year. We want to ensure we are ready for this, both taking advantage of this final hardfork to make any necessary protocol changes and to prepare Grin for what happens beyond HF4.

I am aiming to stay involved in the ongoing “Parallel IBD” work that will add significant improvements to the initial Grin experience, in terms of both stability and performance.

Edit: This post makes the assumption that we _require_ musig support to be able to support multi-party outputs securely. This is not necessarily true and we need to spend time investigating this further. [@tromp](/u/tromp) suggested in keybase that we _may_ be able to continue using “naive Schnorr” and we need to convince ourselves of this. So please treat any reference to musig above as a loose term for Schnorr signatures in general.
We may be able to avoid the additional complexity of musig if we are careful.

---

### Post by @antioch ⭐ (2020-06-20)
*Post #5*

[@kurt](/u/kurt) Hmm yeah maybe I’ve been using the term _musig_ incorrectly when thinking about this.
What we _want_ is a way for multiple parties to produce a signature that is immune from key cancellation and rogue key attacks.

My (somewhat limited) current understanding is that right now our simple tx structure prevents this as _all_ keys involved in the signature map directly to individual outputs (with corresponding rangeproofs), so neither party has an opportunity to introduce a rogue key. The rangeproofs effectively act as proof that all involved keys are legit.

This no longer holds if both parties contribute keys to a _single_ multi-party output (say during an atomic swap) and what we need is a robust way of doing this securely.

I have been referring to this (I guess in loose terms) as musig - but as you say, this may not necessarily be what we want here.

---

### Post by @lehnberg ⭐ (2020-06-22)
*Post #13*

Good write-up [@antioch](/u/antioch), I had some questions:

1. There were [questions in the GrinHub Telegram](https://t.me/GrinCoin/116022) about whether you intended to be working on atomic swaps as part of your funding request. I do not read your request as such, but it would be helpful if you could confirm?

2. While I think the points above are all important and interesting, and I understand the logic for why it makes sense to investigate them together, I’m also aware of the fact that you’re one of our key node contributors at the moment. How would node progress be affected by this shift in focus to the wallet? As we head into preparations for our last scheduled hard fork, what consensus breaking changes (or changes that makes sense to introduce as part of a fork) have we yet to tackle?

3. Conversely - the topics you list above that are related to transaction building are not consensus breaking, correct? What’s the rationale for taking them on sooner, rather than later?

---

### Post by @davidtavarez ⭐ (2020-06-22)
*Post #17*

It is hard for me to visualize the output after these 3 months. Could you clarify what do you want to achieve at the end September 2020, please?

Thanks.

---

### Post by @antioch ⭐ (2020-06-22)
*Post #28*

davidtavarez:

> It is hard for me to visualize the output after these 3 months. Could you clarify what do you want to achieve at the end September 2020, please?

One option that I am proposing here is to make concrete progress toward enabling additional flexibility in transaction construction in the wallet -

* multi-party output (and rangeproof) support
* fine-grained control over kernel offset and kernel excess

I know others have discussed interest in implementing payjoin and “mostly” lock free transactions. My interest here is making sure we are not “over fitting” any of these implementations and that whatever foundation we build around this can be reused easily for similar needs around payment channels.

If I can help others to implement one of these (payjoin or lock free transactions) in such a way that it indirectly makes progress toward a subsequent payment channel implementation then that will personally feel like an achievement.
Alternatively if we can get to the point of being able to robustly build multi-party outputs via the wallet (and we have convinced ourselves we can do this securely with the current signature scheme) then that will be an achievement.

[@lehnberg](/u/lehnberg) raises a good point though about maybe needing to focus more time on node and less on wallet given the balance of current contributors. So I may end up not shifting maybe as much as I’d like. In this case I would probably be focused on helping get parallel IBD implemented and deployed.

---

### Post by @antioch ⭐ (2020-06-22)
*Post #29*

lehnberg:

> Good write-up [@antioch](/u/antioch), I had some questions:
>
>   1. There were [questions in the GrinHub Telegram ](https://t.me/GrinCoin/116022) about whether you intended to be working on atomic swaps as part of your funding request. I do not read your request as such, but it would be helpful if you could confirm?
>   2. While I think the points above are all important and interesting, and I understand the logic for why it makes sense to investigate them together, I’m also aware of the fact that you’re one of our key node contributors at the moment. How would node progress be affected by this shift in focus to the wallet? As we head into preparations for our last scheduled hard fork, what consensus breaking changes (or changes that makes sense to introduce as part of a fork) have we yet to tackle?
>   3. Conversely - the topics you list above that are related to transaction building are not consensus breaking, correct? What’s the rationale for taking them on sooner, rather than later?
>

1. No. This was simply an example use case to illustrate why we need more flexible transaction building support in the wallet. My interest here is more in the foundational work required to get closer to this.

2. All good points. We definitely need to discuss the runup to the final scheduled HF. And this may result in continued focus on node over the next few months. My understanding is “duplicate UTXOs” is one area of consensus breaking work that we _may_ decide to tackle prior to HF4. I’m not sure if there are others being discussed currently.

3. tl;dr Prerequisite for payment channels is robust multi-party output support in the wallet. So this would fall under work required prior to activating NRD on mainnet (itself a consensus breaking change). That said there is a _lot_ of work to get to full payment channels (with nice associated wallet UX) so this needs to be weighed against other work that can potentially be done for HF4.

---

### Post by @lehnberg ⭐ (2020-06-23)
*Post #31*

Thanks, that’s clear to me, and I’m generally supportive of this.

I definitely see the value in thinking more thoroughly about (advanced) wallet use cases. There’s not been a lot to work in that area so far, and as a result you might uncover needed consensus changes, simplification opportunities, or things we just haven’t thought about yet. Also agree it makes a lot of sense to look at a lot of these things together to avoid “over fitting” as you say, and that we’re keeping things as minimal as possible.

I’m worried about us being spread out too thin, perhaps missing needed work on node as a result. But as you point out, we would first need to identify what that node work would be and we’re not quite there yet I think.

---

### Post by @antioch ⭐ (2020-06-23)
*Post #32*

It may be that we end up focusing on one of these wallet related features. I suspect “almost” lock free transactions would provide the most impact and immediate benefit. And would push us down the path of starting to think about more flexible wallet interactions.

If we can do this then we can take in progress transactions and “translate” them to use alternative inputs and potentially outputs. We will also be able to adjust the kernel offset per participant as necessary.

I know several people are already thinking about this so I can definitely make some of my time available to help here.

There is also potentially node related changes here in terms of identifying a “locked” transaction during initial push to the node, to allow the wallet to adjust a tx and re-push if necessary. I have not thought this through so this may not actually be the case, maybe all this should be isolated in the wallet itself.

Avoiding taking on too much at the wallet layer would free time up to continue to focus on node as you say.

---



## Request for funding @paouky
*Date: 2020-07-21 | [Forum Link](https://forum.grin.mw/t/request-for-funding-paouky/7560)*
*Importance Score: 88.6 | Core Participants: david, davidtavarez, quentinlesceller, tromp, lehnberg*

### Post by @Paouky (2020-07-21)
*Post #1*

## Overview

I’d like to request a 3-month funding period to create a comprehensive introduction and documentation for Grin. That would make me the first non-Core member to receive funding for their work.

Grin’s on-boarding process is really bad; I believe I speak for all of us when I say that.
To understand even the most fundamental things about the project, one has to sift through old forums threads, scattered medium articles and outdated & unorganized GitHub docs.

The inevitable result is that potential users are deterred from even taking the time to learn about the project and the unique propositions it has to offer.
One might claim, rightfully so, that in our very early stage we’re better off without attracting too many actual users. However that claim holds no water when you recognize that every avid supporter, every contributor, begins as a simple user with a mild interest.

It is no secret that even long-term community members often have minimal understanding of the project, because the learning process is so demanding. I was one of those myself. It’s essential, in my opinion, that those who are dedicated to grin are actually capable of explaining it well to others.

#### Objectives

* **Create a marketable, one-stop introduction resource for Grin.**
Make the first step into the project as clean as possible and reduce friction for potential future users and contributors.

Examples
* Story & history
* Core design choices
* Friendly explanations of technical aspects
* CLI-wallet (and TUI node) beginner introduction
* Archive of significant articles and forum posts
* Overview of 3rd party software and exchanges
* Media package
* edit: [@Mokhtar](/u/mokhtar)’s [list](https://forum.grin.mw/t/request-for-funding-paouky/7560/11).
* **Official documentation/wiki work**.
Building upon [@quentinlesceller](/u/quentinlesceller)’s [great start.](https://quentinlesceller.github.io/grin-docs/)
As I’ve experienced myself lately, even the advanced users who dare to venture into github, often run into old and dusty documentation.

This list is open to community suggestions.

## Funding request

**€1.5k/month**
For a single period of 3 months, not to be extended.
(fund; amounts to ~0.15%/month).

#### Role

* Full-time
* Writing & Documentation
* Improve Introduction to Grin

## About me

I very recently finished a military service in a field of work I can’t disclose. I begin my BSc CS studies in 3 months. I’ve been following Grin closely and occasionally participating in community discussions since early '18. But now that I’ve regained my status of citizenship, I have also reclaimed my time, and I’d like to dedicate all of it to Grin.

I also absolutely do not plan on leaving after said funding period. I’ll remain an active community member and help maintain the written material.

[GitHub](https://github.com/Paouky), [Twitter](https://twitter.com/MWgrin), [Keybase](https://keybase.io/paouky)

## Next Steps

The intention is to ask for community support and approval in the upcoming Governance meeting on the 28th of July.

Update: The request has been approved on a month-to-month basis. See you in the [progress update thread](https://forum.grin.mw/t/paouky-progress-update-thread-aug-2020/7637/8).

---

### Post by @bluimes (2020-07-21)
*Post #2*

Hi Paouky,

Great that you keep committing yourself to this project. I just wonder… do you have any experience in such a task which should convince us you can pull this off? There is a lot going around in the documentation and branding of a product. And for now it appears to me that no one really is clear about what Grin is going to be. So how are you going to document that? Not that I want to be skeptical, but I think it should be done by someone who has some decent experience in that field of work and also has some extensive knowledge of what Grin is. With that being said is today not a little bit early for that?

---

### Post by @davidtavarez ⭐ (2020-07-21)
*Post #5*

I like this, this the boring but very important work nobody is motivated enough to do, myself included

bluimes:

> it should be done by someone who has some decent experience in that field of work

I disagree, in fact, I think a fresh-mind is better because any core developer is already biased.

[@Paouky](/u/paouky) do you really think that a 3 months period is enough time? I’m not sure to be honest, it could take maybe 4 or 5, also, there is an upcoming HF in 6 months, I would suggest to considered that.

---

### Post by @tromp ⭐ (2020-07-22)
*Post #19*

grin-wallet
Password:
Wallet command failed: Unknown wallet command, use ‘grin-wallet help’ for details

This is annoying though.
Seems it should have the help behaviour without any arguments?!
Or, for more concise output, just respond with

Missing wallet command, such as grin-wallet help

---

### Post by @quentinlesceller ⭐ (2020-07-22)
*Post #20*

FWIW I 100% agree that we need an intuitive GUI Wallet with one click install and super simple to use.

However, I disagree that it is as simple as hiring someone on Gitcoin or on some freelancers website. We will pay likely a lot for a wallet that will break at the next HF.

But that’s not at all the subject here and I don’t think we should halt everything until we have a GUI wallet.

[@paouky](/u/paouky) very nice. Two questions:

* **Create a marketable, one-stop introduction resource for Grin.** Can you details what is it in term of concrete deliverables?
* Second part would be great. Do you have any idea how deep/technical you’d go. I can totally see that part as a month project or 4 months project based on how deep you go.

Thank you

---

### Post by @david ⭐ (2020-07-23)
*Post #23*

This is an outstanding idea. You get all 0 of my votes.

If all goes well, I highly recommend applying again to document our protocol. I could help point you to the areas it’s most needed. I sincerely believe that if we had solid documentation, our exchange issues would go away.

Btw, a solid technical writer is easily worth 3-4x what you’re asking, so kudos for the modest request.

---

### Post by @lehnberg ⭐ (2020-08-03)
*Post #25*

This request was approved in the latest governance meeting, with the adjustment of payments being done on a monthly basis: <https://github.com/mimblewimble/grin-pm/blob/master/notes/20200728-meeting-governance.md#decision-approve-paouky-funding-request>

Payment for the first month has gone out, spending logs have been updated.

---

### Post by @lehnberg ⭐ (2020-08-03)
*Post #27*

Nice! did not know of this, adding to the newsletter that is just going out.

---



## A Message from Nervos
*Date: 2020-07-23 | [Forum Link](https://forum.grin.mw/t/a-message-from-nervos/7568)*
*Importance Score: 85.7 | Core Participants: joltz, quentinlesceller, lehnberg*

### Post by @jm9k (2020-07-23)
*Post #1*

Hi everyone, my name is Jordan, and I’m from the Developer Relations team at Nervos. I’m here today to represent the Nervos Foundation and deliver a message.

Grin has made profound technical contributions to the industry and remains one of the most successful efforts to build a community around privacy technology. Nervos believes strongly in the importance of community surrounding decentralized technology and has a deep respect for the principles and accomplishments that Grin has achieved.

The Nervos Foundation would like to announce a donation of 10 BTC to the Grin General Fund. This donation is being made to help continue the advancement of the Grin platform and Mimblewimble protocol.

Nervos would also like to make it known of our intent to incorporate support for the Mimblewimble protocol into our platform in the form of a privacy layer. Nervos is a UTXO based proof-of-work blockchain with Turing complete smart contracts, and this similarity with Grin’s technical architecture will simplify the process of integrating Mimblewimble protocol.

Over the next few months Nervos will begin a three-phase effort:

* Phase 1: Schema Design (~2 months) - A general schema will be prepared for the operation model.
* Phase 2: Technical Specification (~2 months) - A detailed technical specification will be produced.
* Phase 3: Implementation (3+ months) - Construction of the codebase.

Nervos recognizes Grin as the authority on the Mimblewimble protocol and welcomes any contributions by the Grin community during any of the three phases.

We believe that pursuing this additional Mimblewimble implementation will:

* Demonstrate the importance of Mimblewimble as a flexible and extensible privacy protocol.
* Increase brand awareness of Grin and Mimblewimble in China and other Asian markets.
* Pave the way for new offerings based on Mimblewimble, such as privacy-based cross-chain swaps and asset exchange between Grin and Nervos.

The Nervos Foundation is also setting aside a grant fund specifically for infrastructure and interoperability solutions between Grin and Nervos. Any Grin community members with interest are encouraged to apply!

We, the members of the Nervos Foundation and community, are excited about the advancement of Mimblewimble technology. We invite everyone to take in voicing their opinions and ideas for what can be achieved in the future!

We look forward to your comments and I’d be happy to answer any questions or help to connect you with the team at Nervos.

---

### Post by @Anynomous (2020-07-23)
*Post #3*

Looks like Grin funding is going well. If I read it correctly these 10 BTC come with no strings attached [@jm9k](/u/jm9k)?

Time to read up on Nervos, it is new to me .

---

### Post by @quentinlesceller ⭐ (2020-07-23)
*Post #7*

Nice! That’s a very generous donation :). Many thanks to the Nervos Foundation for supporting Grin.

---

### Post by @joltz ⭐ (2020-07-23)
*Post #8*

This is great, Nervos reached out a few weeks ago asking for help using MW in an implementation for their network and we suggested a donation and description of their plans would be a good approach to get feedback and raise awareness. It is nice to see them follow through.

---

### Post by @jm9k (2020-07-23)
*Post #9*

Yes, that’s right. This donation was made with no strings attached to help with the continued advancement of technology that we believe is a strong benefit to the world.

However, I should reiterate that any form of contribution is very much appreciated. The efforts of the community are the heartbeat of a decentralized project, and that importance cannot be understated.

This includes non-technical contributions! Showing support, voicing your opinions, and helping to share that enthusiasm with others is greatly important to the long-term vision.

---

### Post by @lehnberg ⭐ (2020-07-24)
*Post #11*

It’s great to see an increased interest in Mimblewimble, thank you for the generous donation and good will gesture! We’ll try to put it to good use. Looking forward to knowledge sharing between the communities.

---

### Post by @minexpert (2020-07-24)
*Post #12*

Good things collect good things around. Welcome!

---

### Post by @mcm-mike (2020-07-25)
*Post #13*

Thank you [Profile - jm9k - Grin](https://forum.grin.mw/u/jm9k) for the contribution.

From what I did read you entering different phases, we ([Grinnode.live](https://grinnode.live/)) are providing a lot of [free & open GRIN API](https://github.com/MCM-Mike/grinnode.live) and [GRIN infrastructure](https://github.com/MCM-Mike/grinnode.live#infrastructure-grinnodelive) you could use for testing purposes for your pre-live / testing and implementation phases.

We are happy to [help](https://github.com/MCM-Mike/grinnode.live/blob/master/contact.md) if we can.

---



## Unique Kernel Thread #73
*Date: 2020-08-12 | [Forum Link](https://forum.grin.mw/t/unique-kernel-thread-73/7688)*
*Importance Score: 83.1 | Core Participants: david, tromp, antioch, lehnberg*

### Post by @david ⭐ (2020-08-12)
*Post #1*

This thread will serve as an attempt to come to agreement on the best way to prevent replay attacks via unique kernels in order to facilitate the writing of a future RFC. This is not a place to discuss the pros and cons of a consensus vs wallet based approach. Please avoid discussing wallet-based alternatives, dogmatic arguments against consensus changes, personal attacks, mentioning “the core team”, bad-faith discussions, or general off-topic comments.

The simplest way of supporting unique kernels, without having a large impact on scalability, is to introduce a new type of kernel (`expiring_kernel`) which simply contains an 8 byte field indicating the maximum block height that the transaction can be included in. These kernels cannot be included in any blocks more than 7 days (ie. 10,080 blocks) before that max block height.

Nodes must enforce kernel uniqueness for all `expiring_kernel`s, which means they will need to keep all `expiring_kernel`s included in the last 10,080 blocks, preferably indexed in memory.

While it can be assumed that most transactions will use `expiring_kernel`s, it’s not necessary to disable plain kernels, or any other existing kernel types. It seems likely we’ll also have to have a new kernel type which supports minimum and maximum block height in order to complement the existing `LOCK_HEIGHT` kernels.

Though it is up to node developers to decide exactly which rules to apply to mempool logic, to avoid potential DoS attacks, at minimum the mempool should not accept transactions that are about to expire (in the next few hours, perhaps).

What are the cons of this proposed change, and most importantly _How can it be improved?_

---

### Post by @tromp ⭐ (2020-08-12)
*Post #2*

Just for reference, I’ll repeat my con:

Bitcoin experts like Andrew Poelstra stress the importance of “tx monotonicity”, which is the property that once a tx passes initial mempool entry checks, it remains valid while its inputs are unspent.
I agree this is a nice property that simplifies thinking about tx processing. It makes it easier to manage the mempool.

It also prevents having to deal with certain unwanted complexities. Currently the tx fees protect against spamming of the network. For a tx to be broadcast worldwide, it cannot escape paying tx fees. But if you could publish txs that are about to expire, then the spammer reduces the odds of having to pay any fees (to nearly zero if they are a miner that just found a new block). This problem would be magnified once blocks fill up.

It’s also not clear what impact expiry height has on tx aggregation. Could a tx with a distant expiry get aggregated with another that has an imminent expiry and then get rejected, negating the issuers expectation? Or will we have to limit aggregation, harming privacy?

When in the distant future blocks fill up, tx expiry would be increasingly common, and it’s less clear how broadcasting resources will be covered by fees.

Then there’s the issue of what bitcoiners call “reorg-safety”.
In case of a medium size reorg, expiry risks losing transactions that just barely made it in the old branch. Particularly if the reorg mined empty blocks. Losing already confirmed transactions due an accidental reorg and not being able to replay them without having to reconstruct them from scratch could be a serious problem.

---

### Post by @lehnberg ⭐ (2020-08-13)
*Post #8*

Question: If the motivation behind unique kernels is to prevent replay attacks, wouldn’t it require all kernels to be `expiring_kernels` in order for it to be effective? I.e. if some x% of kernels are not, wouldn’t they need to take other measures?

* * *

Also: As I was digging a bit on this subject, I found [this discussion on /bitcoin](https://github.com/bitcoin/bitcoin/issues/3722) where gmaxwell outlines a double spend attack that relies on an “expiration replacement race”.

**Please take the following with a grain of salt.** I don’t know how applicable that is to Grin, but I personally think it illustrates well some of the complexities that can arise when it comes to actually implementing mempool logic like “not accepting transactions that are about to expire in the next few hours” and expect synchronised, consistent behaviours across the entire network. It might be easy enough to specify it, but I wonder how straight forward it is to actually implement in a way that does not create unexpected attack vectors.

---

### Post by @david ⭐ (2020-08-13)
*Post #9*

Yes, transactions that don’t use unique kernels would need to take additional measures, but the recommendation for most transactions should be to use unique kernels. I just prefer not to remove kernel types since there may be uses for them.

One example is self-sending to a cold wallet, maybe you want to send with low fee and no expiration, so it gets included whenever there is free block space. A plain kernel is perfect for that. Since you control both sender and receiver, replay attacks aren’t a problem.

The attack outlined by gmax isn’t really a valid attack these days anyway, since greedy mining make 0conf untrustworthy. But it doesn’t apply here anyway, since we are talking about actual consensus expiration instead of just mempool policy.

---

### Post by @david ⭐ (2020-09-13)
*Post #12*

There hasn’t been any more feedback, so I’ll go ahead and respond to every remaining point to see if we can come up with an agreeable solution. I believe only [@tromp](/u/tromp) has issues that remain unaddressed, so I’ll go ahead and take a stab at those now.

tromp:

> Bitcoin experts like Andrew Poelstra stress the importance of “tx monotonicity”, which is the property that once a tx passes initial mempool entry checks, it remains valid while its inputs are unspent.
>  I agree this is a nice property that simplifies thinking about tx processing. It makes it easier to manage the mempool.

While I appreciate that Poelstra is brilliant and has a deep understanding of crypto & blockchains, I don’t see any technical arguments in this paragraph, so there’s nothing for me to refute.

tromp:

> But if you could publish txs that are about to expire, then the spammer reduces the odds of having to pay any fees (to nearly zero if they are a miner that just found a new block).

Why do you think this is the case? Is it just because you think miners will include it since they don’t want to miss out on fees? Because game theory would suggest that’s not true.

With empty blocks:
None of this matters at all since miners will include any non-zero-fee tx they receive.

With full blocks:
If there are txs with higher fees, they will include those instead. Otherwise, competing miners will end up with the higher fee txs. If the concern is that people will use short expiration to get included quicker, miners would easily recognize that and realize that once the tx expires, the tx originator will just create another tx. There’s no financial advantage to accepting lower fee txs when there is not a mining monopoly.

tromp:

> Could a tx with a distant expiry get aggregated with another that has an imminent expiry and then get rejected, negating the issuers expectation? Or will we have to limit aggregation, harming privacy?

The only aggregation we do that is useful for privacy is stem-phase aggregation. Stem-phase agg already has the problem where someone could try to take advantage of someone overpaying, so we already need rules about aggregation. It’s trivial to add an additional rule that only aggregates when transactions do not expire in something like less than 90% of whatever we choose for the default expiry. So, if we decide the default tx expiry should be 1 day, we won’t aggregate anything that expires in less than 22 hours. And of course, the tx originator can always resend if it’s unhappy with the results of aggregation.

In other words, this is just a special case of users aggregating low-fee transactions, and in practice, does not make the situation any worse.

tromp:

> In case of a medium size reorg, expiry risks losing transactions that just barely made it in the old branch. Particularly if the reorg mined empty blocks. Losing already confirmed transactions due an accidental reorg and not being able to replay them without having to reconstruct them from scratch could be a serious problem.

This is a very rare scenario, but something worth discussing. This is just another form of a double-spend attack. In large reorgs, the few transactions performed by the attacker already cause havoc on transaction graphs. This just provides one more situation where that can occur. The solution to the problem is the same as we already have today: adjust confirmations required according to your desired security needs.

TL;DR: All of the attacks in here are just variations of things that already exist. This includes various attempts at aggregating low-fee txs with txs that overpay (which isn’t even necessarily a bad thing), or already-problematic double-spend attacks. Even with no additional rules added to stemphase aggregation or mempool acceptance (aside from making sure txs are valid ie. not expired), then the situation is not much worse than today. And with minor tweaks or simple rules that can be added to the mempool, I see no reason we should expect anymore problems than we already have.

---

### Post by @tromp ⭐ (2020-09-14)
*Post #16*

david:

> I don’t see any technical arguments in this paragraph, so there’s nothing for me to refute.

Yet making it easier to reason about tx processing is a large benefit.

david:

> Why do you think this is the case?

Because if a tx expires after height H, then broadcasting it when block H is just found but not yet relayed will waste resources.

david:

> None of this matters at all since miners will include any non-zero-fee tx they receive.

It makes sense for miners to use the same mempool acceptance criteria as any other nodes, and reject txs with fees below the required minimum. It’s in their long term interest to have everyone know that minimum fees are enforced, else many people will try to sidestep fees (paying just one nanogrin) by sending them directly to mining pools, and there will be less miner income in future.

david:

> It’s trivial to add an additional rule that only aggregates when transactions do not expire in something like less than 90% of whatever we choose for the default expiry. So, if we decide the default tx expiry should be 1 day, we won’t aggregate anything that expires in less than 22 hours. And of course, the tx originator can always resend if it’s unhappy with the results of aggregation.

Having to make trade-offs (i.e compromises) between different objectives is not ideal, and not trivial.

david:

> The solution to the problem is the same as we already have today: adjust confirmations required according to your desired security needs.

Doesn’t solve the problem that expiring transactions sometimes can’t be replayed in a reorg.

david:

> simple rules that can be added to the mempool

I much prefer adding simple rules in the wallet, requiring no additional censensus model complexity.

---

### Post by @david ⭐ (2020-09-14)
*Post #17*

tromp:

> Yet making it easier to reason about tx processing is a large benefit.

This still isn’t much of a technical argument, since it’s not falsifiable or something I can attempt to “solve.”

tromp:

> Because if a tx expires after height H, then broadcasting it when block H is just found but not yet relayed will waste resources.

Mempools shouldn’t accept transactions about to expire. It’s a one-line change.

tromp:

> It makes sense for miners to use the same mempool acceptance criteria as any other nodes, and reject txs with fees below the required minimum. It’s in their long term interest to have everyone know that minimum fees are enforced, else many people will try to sidestep fees (paying just one nanogrin) by sending them directly to mining pools, and there will be less miner income in future.

If they don’t pick up on those fees, even if low, another miner will. It’s simple price competition.

tromp:

> Having to make trade-offs (i.e compromises) between different objectives is not ideal, and not trivial.

It’s not clear which trade-offs and which objectives you’re referring to. Nearly all transactions will be broadcast shortly after creation, meaning it will have most of the default expiry. Those will be aggregated together with no issue (assuming similar fees). I think we’ll see that full blocks and dynamic fees already ruins our chances of ever having any significant stem-phase aggregation. I hope I’m wrong, but I don’t see how it could ever work well.

tromp:

> Doesn’t solve the problem that expiring transactions sometimes can’t be replayed in a reorg.

Correct, it’s unsolved in the same way that any large reorg can always lead to transactions that can’t be replayed.

tromp:

> I much prefer adding simple rules in the wallet, requiring no additional censensus model complexity.

Yes, this has been made abundantly clear, but I’d like to focus on solutions that don’t sacrifice privacy, and don’t require bloating the blockchain with outputs that are never spent.

---

### Post by @tromp ⭐ (2020-09-27)
*Post #18*

On tx-monotonicity, Andrew Poelstra remarked:

"As you say, the benefits to monotonicity include

1. You can’t get out of paying fees by broadcasting near-expiring transactions (assume additional network rules like RBF prevent you doing the same thing by double-spending)
2. Harms to aggregation, both noninteractive and coinjoin-style
3. Reorg safety
4. Harms to second-layer protocols (though I assume these would work if you just required participants to disable non-monotonic features).

The only thing I can think of that you didn’t mention is:

5. Caching: if transactions expire at a fixed time this is not too bad, but
if the expiry conditions are more complicated then you have to constantly re-validate transactions in your mempool to check if they’ve expired
"

On your reply, he remarked:

"But he seems not to understand the concern about fees (he says “miners will include higher-fee transactions instead” as though that were a solution, rather than the problem).

He suggests solving problems with aggregation by adding epicycles, which I don’t care to analyze in detail, but he says “this is just a special case of users aggregating low-fee transactions” which is definitely untrue, both because the aggregation function is different (weighted average for feerate, minimum for expiry times), and more importantly, because reasoning about fees is a 1D problem (efficiently optimizable) while fees + expiry is a 2D problem (knapsack problem, NP complete).

Then he suggests that the reorg safety issues around transactions which automatically become invalid regardless of user/miner choice are commensurate with reorg safety issues in the presence of active double-spend attackers.
It is not. In the case of expiring transactions the result is an unreliable
network. In the case of a double-spend attacker the result is unreliable
transactions when dealing with unreliable people."

He clarified that “It is a term from history of science to refer to addition of orbits upon orbits upon orbits, to try to make a broken solar system model match observation. I’m using it by analogy, see
<https://en.wikipedia.org/wiki/Deferent_and_epicycle#Bad_science>”

---



## Request for funding @davidtavarez (Grin++ mobile wallet)
*Date: 2020-08-29 | [Forum Link](https://forum.grin.mw/t/request-for-funding-davidtavarez-grin-mobile-wallet/7774)*
*Importance Score: 123.5 | Core Participants: david, antioch, yeastplume, davidtavarez, lehnberg*

### Post by @davidtavarez ⭐ (2020-08-29)
*Post #1*

### TL;DR

I’m planning to release a mobile version of Grin++ for the next, and maybe the latest, hardfork (around Jan 15 2021), therefore I would like to spend more time and energy on this task, that’s why I’m opening a request for a 3 months funding period. I want to have a fully featured mobile wallet.

### Intro

I met Grin at the begining of 2019 and got attached to the idea of a cryptocurrency built to be used as a means of payments. I ended up contributing to Grin++ by completely rewriting the UI codebase at that moment to bring a clean, truly easy to use and multilanguage Desktop Wallet. Now I want to do the same but for Mobile.

I’m a believer of " `dogfooding` " or " `eating your own food` " and maybe that’s the main reason why Grin++ is widely accepted since even though I’m a developer, I try to think and see things as a real world user. I want to do the same with the mobile version of Grin++.

### What do I want to achieve?

These are some cool features I will try to bring to the mobile app:

* All current Grin++ functionalities: Multiple accounts, Multi-language (12 different idioms) and Coin Control.
* Address availability checker (as the Desktop version has).
* Sending and Receiving Grin via Tor, Slatepack and NFC (based on Slatepacks)
* QR scanning.
* Backup/Restore seed wallet.
* and many more…

Also, we’re going to have an ARMv7 binary of the backend that could be used in any other project.

### Some FAQs

* Will the wallet be compatible with `grin-wallet` ?
* No, but it could be if someone wants to create a wrapper for `grin-wallet` and fork the project.
* Will users be able to use a remote node/wallet?
* In theory and with some work, yes, but I would not recommend this at least the user knows exactly what they are doing.
* Will this just cover the effort needed for an UI?
* No.
* What tool am I using?
* Xamarin (C#).
* Did I already started?
* Yes, but I would like to dedicate more effort to finish this before January 2021.
* Why should this mobile version be funded?
* Having more choices is healthy for the community, more options = more decentralization.

### Funding request

**€4k/month** .

### About me

I’m a Senior Software Engineer, focused on being a (Security oriented) Full Stack Developer. I define myself as a Cryptoanarchist, in my free time I write [Open Source](https://github.com/davidtavarez) and I’m currently the Lead UI Developer for Grin++.

---

### Post by @david ⭐ (2020-08-29)
*Post #4*

I’m biased, but imho, there are few people more deserving. David has done an incredible job of making Grin++ more accessible to everyday users. He writes professional quality code, is always happy to support it, and has an obvious passion for the technology, the community, and the mission of Grin.

If the core team decides that they’re ready to start funding community projects, this is an obvious place to start.

---

### Post by @Yeastplume ⭐ (2020-08-31)
*Post #18*

All fine in principle, [@davidtavarez](/u/davidtavarez) has been an upstanding community member.

Obviously think that if this is approved, it’s understood that anyone should be able to fork the Grin++ GUI for use with Grin-wallet.

Is there any reason using the Grin++ GUI with grin-wallet would require a fork as opposed to a refactor to allow an ‘adapter’ type approach? Grin-wallet has a very comprehensive API and from what I can tell the Grin++ GUI is calling out to a similar looking API.

---

### Post by @david ⭐ (2020-08-31)
*Post #19*

grin-wallet lacks APIs for coin control (solvable), and multi-user support (also solvable, but would require significant rework).

---

### Post by @antioch ⭐ (2020-09-01)
*Post #21*

I think this would be a very positive project to fund.

My understanding is this proposal is for a “full” mobile node with the Grin++ node running entirely on the mobile device.
Is there “prior art” and other projects we can point to that have done this successfully for other cryptocurrencies?

Would it potentially make more sense to do this in a “trusted node” model? With the mobile UI interacting with a configurable server based node.

---

### Post by @davidtavarez ⭐ (2020-09-01)
*Post #22*

Yeastplume:

> Is there any reason using the Grin++ GUI with grin-wallet would require a fork as opposed to a refactor to allow an ‘adapter’ type approach? Grin-wallet has a very comprehensive API and from what I can tell the Grin++ GUI is calling out to a similar looking API.

I will try my best to make the codebase as **flexible as possible**. I’m considering to create a `nuget package` for the Grin++ API but anyone could do the same for `grin-wallet`; in the timespan of 3 months I won’t be able to write an adapter for `grin-wallet`, but I’m more than happy to support other community members.

Neo:

> Could Grin++ mobile support the option to run a full node? With settings so the node only downloads and validates when the user tells it to/ so it’s not always serving data to other nodes in the background.

Yes; that’s one of the goals although there are some challenges here. I would like to see more progress on “light nodes” but in the meantime I’m a bit _optimistic_ since nowadays cellphones and tablets are really powerful overall. I will keep the community posted.

natsu:

> This is an awesome idea, especially considering Ironbelly’s tenuous rate of development. If Grin++ could bring mobile transactions via QR codes it would be an amazing development for Grin’s usability!

Totally! another option is to use NFC, at the beginning it will only be available between 2 Grin++ mobile wallets. To be able to send/receive coins just with proximity makes me really excited, maybe we will be able to pay for a pizza with our mobile wallets very soon… I don’t know, I don’t mind opening a PR for **IronBelly** with this feature later on 2021 when the feature becomes more stable.

In general, the option of running a mobile wallet using a remote backend will be there, but I won’t encourage users to do it, at least not for now. Also, in the current version of Grin++ Desktop the user must enter their password in order to authorize Sending grins, for the mobile version it will be the same control (probably replacing it with TouchID when it’s possible).

---

### Post by @davidtavarez ⭐ (2020-12-13)
*Post #23*

After being funded I was able to bring Grin++ to [Android 9+](https://forum.grin.mw/t/building-and-running-a-full-grin-node-grin-on-android/7917) and the [Raspberry Pi](https://forum.grin.mw/t/building-grin-for-raspberry-pi4/7916). The full node runs on a **Linux ARM64** bit and Android, also **aarch64**.

I also built an [Android mobile app](https://forum.grin.mw/t/grin-mobile-progress-update-thread-by-davidtavarez/7894) and a [nuget package for the Grin++ API](https://www.nuget.org/packages/GrinPlusPlus.Service/). The APK (**beta version**) was already submitted to the Google Play and it’s under review right now.

**What next?**

I will keep contributing to the Grin community. After collecting feedback from users a non-beta version of the apk will be released, this apk will be a 100% compatible with the next hardfork. Most of my contributions are focused on Grin++ but I’m planning to migrate some cool features to [IronBelly](https://github.com/i1skn/ironbelly) too, so no grin user will be left out.

I still have a bunch of stuff to do, specially, to write a bunch of documentation. For 2021 my main goal is to create an unique experience between the Desktop UI and the Mobile application and add more cool features. This will keep me busy for several months, I’m sure. Improving the base code, writing more tests and decoupling it as much as I can is on my radar too, this will help anyone to easily reuse both UIs.

What about iOS? Well, iOS not only requires a huge amount of effort, but even if I could get a binary running for iOs, it is very unlikely that they will accept it on the App Store and playing a cat-mouse game with Apple is not on my plans. Users could either **use IronBelly** or wait for a solution.

**Final thoughts**

Backing up and restoring wallets using a plaintext seed makes me nervous. I wish I could have more time to write a RFC with some new ideas, I think we can take advantage of what [this RFC](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0015-slatepack.md) brings to Grin to create a more secure method to improve this.

The Slatepack Message flow is a huge improvement, I personally think the Exchanges should forget about Tor and implement only the new flow. If we could prioritize [Eliminating the third step](https://forum.grin.mw/t/eliminating-finalize-step-reloaded/7817) we could be more closed to achieve a (cuasi) cash feeling like while sending/receiving transactions; this will help developers simplify the user’s life. Right now, we could say that transitioning over Tor works fine, but users from countries with high levels of censorship usually face issues trying to receive coins, this is a headache for everyone, most of the support is related on this, but more important we’re not fulfilling the “ _To be used by anyone, anywhere_.” statement. I remain optimistic, I’m pretty sure we’re going to figure it out.

I must confess, **this is becoming a huge time consuming for me**. After reaching a certain point with the mobile application and the Desktop UI, I would like to build more projects, a payment gateway is bouncing in my head right now, but it will depend on what other community developers will build at that moment.

Looking forward to see what 2021 will bring to Grin

---

### Post by @lehnberg ⭐ (2020-12-14)
*Post #26*

Awesome work [@davidtavarez](/u/davidtavarez)! Looking forward contributing to Grin with you in 2021

---



## Dismantling the core team and governance structure
*Date: 2020-09-05 | [Forum Link](https://forum.grin.mw/t/dismantling-the-core-team-and-governance-structure/7801)*
*Importance Score: 161.4 | Core Participants: david, antioch, davidtavarez, tromp, lehnberg*

### Post by @lehnberg ⭐ (2020-09-05)
*Post #1*

## Tl;dr

Solicit ideas and approaches on how best to break down the current governance structure and replace it with something new. I pledge to help write an RFC and/or shepherd it if I can be convinced it will be an improvement over the existing structure.

## Motivation

Rather than making empty threats to “destroy the core team”, let’s instead embrace the thought and work together in the open to see if we can come up with a better governance structure to replace it with. It’s very possible that what’s worked well in the past may not be suitable for the future of the project[1]. The main reason we’ve evolved into today’s structure is because we didn’t see a better approach at the time, and I have no reason to believe it’s perfected or that improvements cannot be made.

* * *

## Quick overview

(write below fixes and suggestions and I’ll add / update accordingly)

### Some of the current responsibilities

* Managing keys to general fund
* Taking fund spending decisions, approving/rejecting funding requests
* Administering & moderating the `/mimblewimble` GitHub org
* Administering & moderating the forum and keybase
* Managing non-public discussions like exchange listings
* Adding/removing sub-teams, like security, wallet, node
* Approving/rejecting project-wide RFCs, like governance

### Some pros

* Clear process to make decisions
* Resistant to attacks
* Focal point for project communication

### Some cons

* Point of centralization / single point of failure:
* For consensus changes
* For releases
* For spending decisions
* For RFC approvals
* For project leadership
* Negative feedback loop:
* Creates “us” and “them” in the community, those on the inside, and those on the outside
* This leads to the assumption that core team is “responsible” for the project’s direction and success, fosters complacency by non-core members.
* This leads to more work for core team, makes it more tolling to be part of the core team, which reinforces the first point.

### Flaws in the design

* Core team members have the right to stay for an indefinite time, there are no terms.
* Only core members can add new core members / remove existing ones.
* There are no checks and balances. Community can protest and object in case of conflict, but nothing technically prevents the core team to going against the will of the community.
* The system sucks up contributors. Either there are no new core team members added (which is bad optics). Or you add contributors that work hard in the community and are worthy of membership (which leads to only core members being the strong contributors, which reinforces the “us” and “them” which leads to bad optics and another slew of problems).
* Because of the general lack of non-core engagement, it ends up being core team members that fill most the spots in sub-teams, defeating their purpose.

### Some challenges / limitations with any approach

* There’s a general lack of engagement and contributions
* On top of that, there’s a lack of technical / developer expertise
* Ignotus left abruptly, and took with him a lot of the legitimacy and authority of the project’s leadership. There is undeniably a power vacuum in Igno’s absence where there’s no clear leader to rally around.
* We received clear show of support from the anonymous donor to “keep doing what you’re doing”, which means that I personally at least have a sense of obligation and duty to this donor to do what I think is right. I can obviously be overruled by others, but I’m not going to be bullied into doing something I don’t believe is in the best interest of the project.

### My conclusion

* It’s… messy.
* For any replacement structure I think the two most crucial questions are:
* How to handle the funds in the General fund (and its keys)
* How to handle the GitHub org.

Money is what created most of the contention in the community, and is hardest to manage appropriately for a project like Grin. The rest can probably be figured out more easily.

## Possible approaches

(come with your suggestions and I’ll update)

* Return the funds to the anonymous donor
* Burn the funds
* Split funds to core team members and break up the band
* Split funds between implementations
* Open application process:
* For funds with the purpose of having spent all of it before a certain point in time; or
* For new “teams” to be formed, i.e. groups or individuals, each get an equal chunk of the funds and have to work in the best interest of Grin according to their best abilities.
* Temp core teams, existing core team keeps the mu-sig keys but are not the core team any more. We have temporary core teams (say a new team every 6 or 12 months), that people somehow appoint, and they get a pre-determined amount to spend according to their best discretion, perhaps via filing a budget for it.

… what else?

## My pledge

I’ll work with whoever wants to be involved in this thread, in good faith. If a proposal arises that I believe in and think will be an improvement over the status quo, I offer either to write or to shepherd a future RFC that introduces this and lobby for it.

I also pledge to heavily moderate this thread, so please stay on-topic and stay constructive, no bad faith rants or trolling will be tolerated.

* * *

## Notes

[1] See for instance this article on the subject: <https://a16z.com/2020/01/09/progressive-decentralization-crypto-product-management/>

## Changelog

* _Sep 05: First draft_

---

### Post by @david ⭐ (2020-09-06)
*Post #2*

Thanks for getting this discussion started [@lehnberg](/u/lehnberg)!

This overview is top notch. An excellent breakdown of the current situation, the pros and cons of it, and a thorough explanation of _why_ things are the way they are. A few quick questions and comments about the overview:

lehnberg:

> Resistant to attacks

I’m not sure I follow. What kind of attacks are you referring to?

lehnberg:

>   * There’s a general lack of engagement and contributions
>   * On top of that, there’s a lack of technical / developer expertise
>

Though we risk derailing a bit, it might be important to understand why there’s such limited participation, and whether this is something we can improve upon as a result of any governance changes that may take place. I’m sure there are a great variety of reasons why people are leaving the project, or why we fail to attract new contributors. I’m sure plenty of those reasons are beyond our control, but I’m also sure there must be things we can do to improve the status quo. Here’s some things we might have some influence over that could be a contributing factor (some only tangentially related to governance):

1. Lack of visibility
I’ve heard from numerous people who’ve said that Grin feels like a dying project, and I totally understand that feeling. There was once a bit of clout (even if exaggerated or altogether imaginary) that came from working on Grin. It was an exciting project with lots of attention. Now, the very very little publicity we get is never positive [1].

2. Lack of adoption
The price continues to tumble, more exchanges and services are delisting Grin than are adding it, and the community is shrinking, not growing. While some of the early contributors we lost are gone because of the lack of attention, most of them left when they found it was unprofitable. There were once a number of projects & businesses started around Grin that hoped to make a profit but are now dead or dying (vault713, cycle42, GrinGoldMiner, Galleon, superlinear, countless mining operations, etc). The potential for profit drives innovative ideas, but aside from a few exchanges and mining pools, there’s almost no chance of profiting off of Grin with its current usage and interest levels.

3. Old guard discouraging new ideas
It sometimes feels as if the earliest grin developers are stuck in the ways of the past, and refusing to adjust to a changing climate. The Grin community looks much different than it did in 2017/18 when Grin was being planned and developed by those with the optimistic belief that this was going to be a better bitcoin. There was a widespread belief that launching in the most fair way possible a beautiful & minimalistic protocol that improves scalability and privacy was all it would take to guarantee Grin’s place in the future. There are still a few key players who hold onto this belief, and at least seem to be actively combating new ideas they see as impure or never part of the original plan, despite the market very clearly indicating that purity is not nearly as valuable as believed. I’ve even seen claims like “the grin protocol is largely complete”. Many devs who hear statements like that, or believe new ideas will be written off because they’re not part of The Original Plan ™, will be naturally less inclined to work on the protocol.

4. Paying devs discourages volunteers
Having a few paid developers can be discouraging for outside contributors. Back when everybody was volunteering, and there was no central fund to pay for developers, there was little reason to be envious of others. It has been shown[2] that people don’t care as much about their income (or in our case, whether they’re being paid at all) as they do their income in relation to their peers.

5. Not paying enough devs
On the flipside, maybe we aren’t doing enough to make it known that funding is available to outside devs. Coins that have fancy quarterly budgets for community initiatives and clear guidelines for applying (eg. Zcash) seem to have no shortage of devs looking to contribute.

lehnberg:

> It’s… messy.

lehnberg:

> Money is what created most of the contention in the community

What makes you say this? I’m one of the largest critics of our current governance structure, and money has only ever been a secondary concern for me (unless by “money”, you’re just talking about Grin - A better money ツ). Funding has no doubt been a source of contention, but a much larger problem (and harder to solve imho) is centralized decision making. I personally got involved with Grin because I wanted a decentralized money with no kings, rulers, or federal reserve board members making all the decisions. What we have now feels a lot like a rebranding of the status quo. This is supposed to be a trustless & decentralized cryptocurrency, but having a centralized team with ultimate decision making power seems antithetical to what we (at least I) hoped to achieve.

Gotta get some sleep now. I’ll weigh in tomorrow on the “possible approaches” to dealing with funding and also start discussing ways to overcome the flaws and challenges you outlined, and the causes of poor participation that I mentioned. Hopefully we’ll also have suggestions from others by then.

[1] [18 Months In, Few People Use, Mine or Buy Privacy Coin Grin - CoinDesk](https://www.coindesk.com/18-months-few-people-use-mine-buy-privacy-coin-cryptocurrency-grin)
[2] <https://www.researchgate.net/publication/43348242_Money_and_Happiness_Rank_of_Income_Not_Income_Affects_Life_Satisfaction>

---

### Post by @david ⭐ (2020-09-06)
*Post #4*

Your comment adds very little value to this discussion.

mably:

> Some people seem to be forgetting that Grin is just an highly experimental project with absolutely no guarantee of success.

Are you saying that because there’s no guarantee of success, we shouldn’t strive to make it successful? What a strange attitude to have.

mably:

> I don’t see the point to try to change it so some kind of get rich quick business.

Who said anything about making it a get rich quick business?

mably:

> I can see a lot of wishful thinking and day dreaming going on around. Let’s get back to earth and only invest what you can afford to lose.

I’m not even an investor in Grin, so what are you talking about?

mably:

> Governance of the “core” implementation should be kept technical and development related only.

So they shouldn’t have a fund with 100+ BTC in it? What should we do with those funds then?

---

### Post by @tromp ⭐ (2020-09-06)
*Post #5*

david:

> despite the market very clearly indicating that purity is not nearly as valuable as believed

The market indicates no such thing. That’s just wishful thinking on your part.

---

### Post by @lehnberg ⭐ (2020-09-07)
*Post #20*

david:

> I’m not sure I follow. What kind of attacks are you referring to?

Attacks on Grin’s governance. Governance is a massive security risk for any blockchain project. Example of possible attacks:

* Sibyl, bribing, or collusion attacks on any kind of voting or signalling by community.
* Attempts to gain control of mu-sig wallet.
* Subversion of decision making process in order to gain unduly influence for personal gain, for example through changing emission, pow, and so forth.

> it might be important to understand why there’s such limited participation, and whether this is something we can improve upon as a result of any governance changes that may take place.

To explain my intention a bit better, I listed the lack of participation as something that should be taken as a given, to avoid proposals for some new system that would rely on a large and active community of contributors, as this is unfortunately not realistic today.

It would be great to see proposals that can lead to improved engagement and contributions, perhaps this could be motivated as part of the actual proposal itself.

> What makes you say this? I’m one of the largest critics of our current governance structure, and money has only ever been a secondary concern for me

Because to me, “what do we do with the mu-sig?” is the hardest question to answer, and I can see how it can become infected.

Adding to this, there’s been a lot of back and forths about

* [“Why didn’t you fund the grin++ audit?”](https://forum.grin.mw/t/question-about-the-grin-audit/7558)
* [“Why are you not funding GUI wallet development?”](https://forum.grin.mw/t/question-about-funding-gui-wallets-like-ironbelly-or-grin/7559)
* [“Why don’t you hire a cryptographer?”](https://grin.mw/open-research-problems)
* “Why are you not doing any of the above, while paying yourselves?”

All of the above, relates to money, and the fact that the core team has control of some, which means we need to make (sometimes tough, sometimes easy) spending decisions. If we had no money, there would be no decisions to make, and less contention as a result.

The question “who decides what gets merged in `/grin` and `/grin-wallet`” seems to be way less contentious, and has easy solutions if it’s not working as it should: Developers can fork the repos or write their own implementation from scratch.

The question “who decides what Grin’s consensus rules should be?” is more complicated, but still much easier to reason about (at least right now) than Bitcoin - there is a process in which to propose and introduce consensus changes. And given that there’s been some clear design decisions and directives set out very early in the project’s life cycle (like emission, minimalism, scalability), there is definitely some kind of “checklist” for how we can reach agreement amongst ourselves for that.

Furthermore, regardless of the outcome of this thread, there are larger questions that we will need to figure out at some point. Right now there are two Grin implementations. What happens when there’s three, or four, or five? How do we reach agreement amongst implementations about the right rules, when to make changes, and how to do so? The current governance model doesn’t really account for this, there is no governance process between implementations.

---

### Post by @david ⭐ (2020-09-09)
*Post #37*

Off-topic about what to build + a picture of a house

No worries, I’m over it.

I’m also totally in favor of building a strong, minimal foundation. But it has been taken to an absolute extreme to where we are willing to add all kinds of hacks on top of the base layer, rather than simple tweaks to strengthen the base (see: play/replay attack debate - wallet solutions vs expiring txs). We consider our tiny foundation complete, despite wanting to grow our use-cases, resulting in something that looks like this:

* * *

_mod: off-topic, hiding_

---

### Post by @lehnberg ⭐ (2020-09-10)
*Post #78*

lehnberg:

> Furthermore, regardless of the outcome of this thread, there are larger questions that we will need to figure out at some point. Right now there are two Grin implementations. What happens when there’s three, or four, or five? How do we reach agreement amongst implementations about the right rules, when to make changes, and how to do so? The current governance model doesn’t really account for this, there is no governance process between implementations.

The more I think about this matter, the more I see the resemblances with supra-national governance. Bottom line: There is no well functioning governing body today that can govern above nations. We have the United Nations and other multi-national organisations like Nato, IMF, and WTO, but these are not sovereign _above_ nations, it’s based on agreement _amongst_ nations.

An implementation is like a sovereign state. Other states cannot decide what other states should exist or what rules they should have.

The Rust and C++ implementations cannot agree on a framework for Grin governance and expect it to be stable. Because at any point in time a Go implementation can come to existence out of nowhere that decides not to play by these rules.

Instead implementations work the same way like nations do with each other, using diplomacy and influence. In international trade negotiations, every country is treated with mutual respect and courtesy, and the rules are the same for each nation. But some nations command different authority and wield different influence in the outcome of negotiations than other nations.

What am I trying to say with this?

That this _cannot_ be about general Grin goverance (the wider project across all implementations). It must be (I think) about the Rust implementation, the repos under `/mimblewimble`.

And maybe website, keybase, forum, etc ought to be clearly marked either as **rust-implementation-only** , or alternatively become **implementation agnostic** , i.e. **completely neutral territory**. So for example the website cannot have a governance and code of conduct section at the same time as claiming to be speaking for wider Grin. Either the website is for anything Grin, or it’s only for Rust Grin.

Right now, it’s a bit of both, and this is confusing, and I can imagine also annoying (for Grin++, who hasn’t signed up on any of this).

---

### Post by @lehnberg ⭐ (2020-09-11)
*Post #85*

Without dwelling too much on the past and whether your representations above are fair, I do think you have some right to be frustrated. And I do think that we need to resolve this in order to make progress.

I try to define a form of “natural law” below, i.e. not some rules that I propose or think ought to exist, but rules that simply exist by the nature of how things are.

The way I see it, any contributor to Grin can have influence by making one (or more) of the following three types of contributions:

1. Contribute to an existing implementation and work themselves into a position of influence (i.e being part of an existing nation state). For example, the Rust implementation.

2. Break out by forking / writing a new implementation and work this implementation into a position of influence (i.e. forming a new nation state). For example the Grin++ implementation.

3. Work across implementations and influence the directions of those projects without actually having any authority over them (i.e. the way NGOs like the Red Cross work across nations). For example, this could be some individual or movement campaigning for a capped emission or for the implementation of BLS signatures.

Of course, there’s also the nuclear option always:

4. Break the consensus model and hard fork, essentially exiting Planet Grin and going to some other place in the crypto universe bringing with them whoever wants to join them.

There’s no right or wrong way to contribute, and it’s always up to the individual to choose what they want to do. Depending on their preferences, they will have a different degree of influence based on their actions.

If what they care about the most is autonomy and freedom to work on a Grin node or wallet in the language they prefer, or using a specific architecture design, or with custom features and functionality, then it makes sense to create a stand alone implementation they have full control over.

If what they care about the most is consensus and protocol rules, then working on the canonical implementation makes sense, i.e. the one that defines consensus. They will have more influence over the rules by making changes to this implementation that become accepted. Of course it’s possible to still have influence over consensus in other ways, and by working on other implementations, but the canonical implementation will have the most influence over the direction of the protocol. For as long as it remains the canonical implementation.

Or they can be soft power diplomats, working across implementations as lobbyists, perhaps writing blog posts and producing research, arguing for one thing over the other. While at the same time acknowledging that each implementation at the end of the day will be making their own decisions, and if they are not part of that process, they won’t have much direct influence over the outcome.

david:

> any solution that results in an explicit structure should either have ways of ensuring the community and other impls have some authority, or it should make absolutely clear that it is representative only of the rust implementation, and not the greater grin.

If what I wrote above holds, then any organisation between implementations will always be voluntary. I don’t see a way we can devise a structure that ensures authority and consent from future implementations.

To me, logically, it must then be that the governance we are talking about in this thread is only representative of the Rust implementation, and that nobody can really speak on behalf of the greater grin today, the same way that nobody can speak on behalf of Bitcoin, or of Planet Earth for that matter.

So that the next time someone would ask for the “official website” for Grin, the answer should be that there is no such thing. And that, I think, is as it should be.

---



## Ironbelly - Progress update thread (Sep - Dec 2020)
*Date: 2020-09-28 | [Forum Link](https://forum.grin.mw/t/ironbelly-progress-update-thread-sep-dec-2020/7865)*
*Importance Score: 102.4 | Core Participants: davidtavarez, lehnberg*

### Post by @i1skn (2020-09-28)
*Post #1*

Hi everyone !

As some of you might know [my funding request](https://forum.grin.mw/t/request-for-funding-i1skn-ironbelly-wallet/7733) for Ironbelly got approved and I will posting here bi-weekly updates about progress I’ve done on Ironbelly.

So, here is the first update:

* Ironbelly was migrated to the latest version of `grin-wallet` on both iOS and Android. Because APIs and some libraries in `grin-wallet` were updated (like `croaring`) it took some time to get it up and running on both platforms again. This means Slatepack is unlocked for Ironbelly .
* Completely new flow for creating transactions is in-progress. I hope it will be more straight forward for new users. Users also would be able to copy/paste Slatepack messages instead of only sending/receiving files. Because there is no “the approach” in Grin on how to build async/sync transactions in UI it takes some time to experiment with different approaches to get it right.

Regarding the release date I would like to finish the new flow for creating transactions and then cut v4 release.

If you have any questions/suggestions please join [Ironbelly Telegram channel](https://t.me/ironbelly).

Here is a sneak peek of the new flow (still is subject to change though)

[ Simulator Screen Shot - iPhone 11 Pro - 2020-09-28 at 01.54.571125×2436 341 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/fb2d2a306cb438178b79d4557757200cfb70cb37.png "Simulator Screen Shot - iPhone 11 Pro - 2020-09-28 at 01.54.57")

---

### Post by @Paouky (2020-09-28)
*Post #2*

i1skn:

> Because there is no “the approach” in Grin it takes some time to experiment with different approaches to get it right.

What do you mean? Slatepack (RFC0015) flow is the approach now.

---

### Post by @i1skn (2020-10-12)
*Post #7*

Hi everyone! It’s time for the update!

Last couple of weeks I did some experiments on how best to structure transacting process using Slatepack and I hope you will like it.

## The flow explained

1. **Initiate Send**. On the initial screen Alice enters an amount and choose fee she would like to pay. Then when she presses “Send” it would navigate her to the next screen.
2. **Sending Screen**. On this screen Alice would see a little guide on what to do next and her part of the transaction in the form of _Slatepack_. She now needs to share it as a text or as a file with Bob.
3. **Initiate Receive**. Button “Receive” in the bottom left was only used for information purposes, but not anymore! Now it would navigate Bob to “Receiving screen”.
4. *_Receiving Screen_. Here Bob sees a little guide and the text area which he can fill manually, paste from clipboard or open a file (depend on how Alice has shared her slatepack). When Bob enters the slatepack from Alice he press “Generates response” and shares it back with Alice as a text or as a file.
5. **Finalizing**. Alice receives Bob’s slatepack and enters it on the “Sending screen”. Then she presses “Finish transaction”.
6. **Posting**. After finalization app would automatically show a confirmation dialog after which transaction would be send to the node.

Also, if a user opens a slatepack from another app (as it is the only way right now) in Ironbelly it would automatically navigate to the needed screen!

## Little Demo

I’m doing final tests at the moment and hope this or next week this functionality will be in App/Play stores!

## What’s next?

My next big goal is implementing Grin addresses in Ironbelly!

Besides here is a couple of things I’ve been doing as well or will be doing:

* New website
* Bringing back to life end-to-end tests, so I can do less manual testing and iterate faster.
* Researching solutions for app translation.
* Small redesign and ideas for dark mode.

If you have any question - join Ironbelly Telegram channel <https://t.me/ironbelly>

---

### Post by @shush (2020-11-03)
*Post #11*

I think the primary innovation here for grin is to be able to send slatepacks over animated QR codes (<https://github.com/divan/txqr>). Almost every phone has a front-facing camera, so the transport medium is there. This could be easier than juggling files on phones.

As a user, I’d expect that if I point my front-facing camera at another phone, the two phones would able to communicate by reading each-others animated QA codes. The phones will vibrate to give feedback once the interaction is complete.

---

### Post by @davidtavarez ⭐ (2020-11-03)
*Post #12*

shush:

> a user, I’d expect that if I point my front-facing camera at another phone, the two phones would able to communicate by reading each-others animated QA codes. The phones will vibrate to give feedback once the interaction is complete.

Why not NFC as Apple Pay and Google Pay?

---

### Post by @lehnberg ⭐ (2020-11-16)
*Post #16*

Nice job, looks great [@i1skn](/u/i1skn)!

---

### Post by @davidtavarez ⭐ (2020-12-18)
*Post #23*

How cool is this?!

> Sending [$Grin](https://twitter.com/search?q=%24Grin&src=ctag&ref_src=twsrc%5Etfw) from [@ironbellywallet](https://twitter.com/ironbellywallet?ref_src=twsrc%5Etfw) (iOS) to Grin++ mobile( Android) using only QR codes! Grin/MW is so hard to use 😉 [pic.twitter.com/MamoDWx4av](https://t.co/MamoDWx4av)
>
> — G R I N ツ (@grin_privacy) [December 18, 2020](https://twitter.com/grin_privacy/status/1339804565030334466?ref_src=twsrc%5Etfw)

---

### Post by @i1skn (2021-01-14)
*Post #28*

Hi everyone!

Regarding the upcoming hardfork - Ironbelly 5.0.0 is in review on both App and Play stores, so you all should be able to get it very soon! No actions from users, who use the default Ironbelly node are required. For ones, who use their own nodes, please update them to v5.x to be able to continue use Ironbelly.

More info here: [Network Upgrade 4! | Ironbelly | Grin mobile wallet](https://ironbelly.app/2021/01/14/hard-fork-4.html).

P.S.: I’ve been trying to ship Dark mode within this update, but decided to do so as a part of the next update. But here is a sneak peek

[ Simulator Screen Shot - iPhone 12 - 2021-01-12 at 20.36.421170×2532 171 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e63c5c5f6c7147aed99558e501c832af9326213b.jpeg "Simulator Screen Shot - iPhone 12 - 2021-01-12 at 20.36.42")

[ Simulator Screen Shot - iPhone 12 - 2021-01-12 at 20.36.441170×2532 176 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/daa02be3f801d6f4f5579589d506808f7a6d584d.png "Simulator Screen Shot - iPhone 12 - 2021-01-12 at 20.36.44")

---



## Request for funding @jaspervdm, Nov-Jan 2020/21
*Date: 2020-10-13 | [Forum Link](https://forum.grin.mw/t/request-for-funding-jaspervdm-nov-jan-2020-21/7892)*
*Importance Score: 92.0 | Core Participants: david, davidtavarez, jaspervdm, lehnberg*

### Post by @jaspervdm ⭐ (2020-10-13)
*Post #1*

Hello everyone,

My current funding period is set to expire at the end of October. During this period my main focus has been to work on the parallel initial sync. I think we have made some decent progress on this front with a bunch of preparation work done on the node, specification of the data to be sent over the p2p network (the ‘MMR segments’) and the implementation of them.

However there is still a lot of work to do. The next step would be to build up the new sync process that downloads these different segments in parallel from the available peers and reconstructs the full chainstate from them. For now this new sync method will exist side-by-side with the older method, until we are convinced that the new method has been implemented correctly.
There are some open questions regarding the initial activation timeline of this new feature, that we will be able to answer soon. It is very unlikely that the feature is full finished by the next Hard Fork, but a partial activation might be possible. Activation during a Hard Fork is not strictly necessary but it does simplify some things. So we would like to make use of the final HF wherever possible, without rushing anything in.

As I think this feature is one of the most important ones currently still missing from the Grin node, I would like to continue to work on it in a fulltime capacity. Therefore I would like to request funding for the 3 month period of November 2020 until January 2021 for a the standard yeast-unit compensation of €10K/month, for a total of €30K, to be paid in BTC.

This funding proposal will be discussed at the next Governance meeting on the 20th of October. Any comments or suggestions can either be placed here or be voiced during that meeting.

Regards,
Jasper

---

### Post by @david ⭐ (2020-10-14)
*Post #8*

oryhp:

> I don’t think we should restructure the payments because someone had to take care of life things for half a year.

Imagine you decided to not show up to work for 5 months without any kind of communication. Why would you act like this is not a big deal? Of course it’s okay if he has personal things to take care of, but it takes just a few minutes to communicate that with the community that is funding you. Jasper is a brilliant guy and great developer, but the fact that he cbf to take 5 minutes from his day just to inform the community what’s going on reflects poorly on him, and we shouldn’t act like it’s not a big deal.

I had written a long list of reasons why accepting this funding request seems like a bad idea, but I don’t want to tarnish his reputation in pursuit of protecting the council’s funds. The bottom line though, is that choosing to fund Jasper means we’ve lowered our standards from “Let’s fund people who are passionate about Grin and already contributing so they have _more time_ to work on Grin” to “Let’s fund developers who probably wouldn’t be here otherwise, and may or may not hang around once we pay them.” _Have things really gotten that bad?_

Regardless of whether or not the council chooses to fund Jasper, it should go without saying that he should be paid month to month, not 3 months in advance.

---

### Post by @david ⭐ (2020-10-14)
*Post #10*

oryhp:

> But this isn’t a good enough reason for a switch to post-pay.

It certainly is enough reason, but to be clear, I was not actually suggesting post-pay. I meant something more along the lines of what was done for [@Paouky](/u/paouky).

oryhp:

> I can’t speak whether he would or would not contribute if he wasn’t paid

None of us can say for sure, but his contributions dropped drastically once Binance funding stopped and it became clear 713 wouldn’t be profitable, and he had no contributions at all from mid-November until just 2 weeks before requesting funding the first time.

FWIW, I don’t personally think it’s a necessity for funding that someone would be a contributor even without that funding. I was okay with Ivan’s one-time request, even though it was not clear he would hang around if his request was not approved. But what we’re talking about here is a _recurring, full-time position, working on the core project_. To me, it seems obvious that you would want to have someone in that position who is passionate about the success of Grin. I’m not convinced Jasper fits the description.

Anyhow, I’m not going to keep defending my arguments here, since it involves speaking negatively. I have nothing against Jasper personally, and love the work that he’s done with Grin. He’s easily one of the brightest and most talented people we’ve got, and has a better understanding of bulletproofs, signatures, swaps, etc. than most of us ever will. I just feel this request is poorly-timed, and would rather see him take some time to rebuild some trust first.

---

### Post by @lehnberg ⭐ (2020-10-14)
*Post #12*

Having worked with Jasper on projects quite a lot in the past years, it troubles me to see a mixed response to his funding request. We should be welcoming him back with open arms in my opinion.

That said, I can understand why there are concerns, but I think they are misplaced. I want to share some of my personal thoughts on what’s been said in this thread:

1. There’s been no crime commited here. I was in contact with Jasper early on, and he [made clear he would do good on his commitment one way or another](https://github.com/mimblewimble/grin-pm/blob/master/notes/20200602-meeting-governance.md#3-jaspervdm-update). It took some time, but he came back, and did exactly just that, as promised. What else is there really to discuss?

2. This is not employment. Making the analogy of “what would happen if you did XYZ at a job” doesn’t make sense to me. There’s no sick leave. There’s no support or health care. You don’t have a manager, and you don’t have any obligations or answer to anyone. You make a request for funding to go work on certain things, and then it’s up to you to deliver against that. That’s it.

3. There are comments above about how Jasper “should have communicated”, how “reasonable” of a request that would have been, and stating he was “clearly capable” of doing so. Based on him forking a github repo? As a community, I’d like to see us speculating less about people’s abilities and personal situations, do less “detective work” when there’s no crime committed, and instead spend more time constructively trying to improve Grin and grow our community. To me personally, it feels incredibly off-putting to see a bunch of random people here make claims about other people’s personal states during periods where they’ve explicitly taken a leave of absence. It’s not something I would like to see happen if I ever had to make the same request. I urge you to stop with this, give people space, and try to be a positive force instead.

4. The timings of Jasper’s re-appearance for sure can appear suspicious, but the fact of the matter is that Jasper had been talking about coming back a long time before that vote ever took place. Others can attest to that. His return was already in the works, and I personally urged him to come back before he was voted off, as I thought that him staying on the council would be a net positive for the project. And so he did.

5. If we want to meet the scope we’ve set out for v5, there’s a lot of work that needs to be done. I don’t see how we could do it without Jasper. Why would it be better for the project to not have him work these next few months?

6. Regarding being paid 3 months in advance or month-by-month, this is a complete red herring to me. I’m sure Jasper would agree to either. But I for one trust him and am happy he’s back, and I don’t see a need to trust him any less than before, or anyone else. Again, we seem to forget that he actually came through on his previous funding request. I’m sure he’ll come through now too. There might be reasons for why we should pay _everyone_ on a monthly basis, but I see no reason to make Jasper the exception here. The concern with Paouky was that he had not made a single contribution of note prior to his request being approved.

If you need anyone vouching for Jasper, I wholeheartedly do so, for whatever that is worth. When he took a break, I asked him early on what was up, he gave me an answer, he promised to come back and do right by him, and he did just that. We were in touch throughout this period.

He has my full support, and I hope he has yours as well.

---

### Post by @johndavies24 (2020-10-14)
*Post #15*

I am not against this funding request for two reasons: I stand by my original defense of his absence and do not think a single event (unless egregious, which this does not appear to be) should hold a lot of weight. The other reason articulated by [@lehnberg](/u/lehnberg) #5, we have no choice. I also think his contributions to grin have been indispensable and all the devs deserve their share of the funds.

That being said, the situation and the optics of the situation are not ideal and certainly merit a discussion. It would seem wrong to be entirely silent about the situation. Which leads to [@lehnberg](/u/lehnberg) #2 scenario:

lehnberg:

> you don’t have any obligations or answer to anyone. You make a request for funding to go work on certain things, and then it’s up to you to deliver against that. That’s it.

This seems very flawed and as if you are suggesting there is no mechanism for enforcing accountability (and no need for it). Clearly, if you do not deliver the community will require answers, certainly if communications and funding requests continue. Accountability comes here, but it is complicated with core/council members as they have voting rights on each others funding which creates an unavoidable conflict of interest. I think trusthworthy individuals with high integrity would feel obliged to uphold their word to the best of their abilities and take responsibility for any failures. This is referring to the odd stance that there is no one to answer to and no mechanism for accountability and not to suggest that Jasper doesn’t fit the description of a trusthworthy individual.

lehnberg:

> they’ve explicitly taken a leave of absence

This seems off because there was no request to take a leave of absence. Maybe if Daniel is the boss of all funded individuals and their progress reports are sent directly to Daniel this would make sense. But I think no one wants that, which means communication to the community would be the only logical mechanism for communicating the leave of absence.

lehnberg:

> Jasper had been talking about coming back a long time before that vote ever took place. Others can attest to that. His return was already in the works

This also doesnt add up because the request to remove him was made by a core/council member and it remained on the agenda as such. If I recall, Jasper’s reappearance was at that very meeting. Not so sure why so many backdoor conversations have to occur and who is privy to what (this concern extends beyond this specific topic).

oryhp:

> your progress updates were good, not sure why people complain about them.

The progress reports are smaller and less informative than those from everyone else. Maybe they are sufficient, I was more concerned with public discussions in total. Similar to the topic above, it appears that he has had a lot of technical conversations about what he is doing with Antioch. Maybe they are referring to their comments on the github PR, but it is just unclear how many core/council conversations occur in private that are not private in material (strictly referring to topics that would be appropriate for the grin community).

My concern remains and I will pose it as a question:
What are reasonable metrics for rebuilding trust and were they met? Is it sufficient to reappear the day you are being removed from council, do what you were paid to do 5 months ago, and request your new funding before finishing the time remaining on the prior funding?

I honestly do not know the answer to those questions but the latter feels like “no” even though it seems unfair to say “no” if I cannot answer the first question.

---

### Post by @davidtavarez ⭐ (2020-10-16)
*Post #22*

The Community agrees that [@jaspervdm](/u/jaspervdm) is a valuable asset, he’s committed on bringing the hardest and coolest stuff that we all want to see in Grin, it is fully understandable the fact that he had to take some time, nobody is condemning him, we all humans. [@jaspervdm](/u/jaspervdm) doesn’t have to give any explanation regarding his personal life and he’s back… now, this decision should nonetheless remain rational, and should not constitute in any way a precedent for the future; I think we should not ignore that the Community is hurt and needs to heal, a decision regarding this, at least now, could be misinterpreted by the Community members.

In my opinion, the amount is fine, the committed work is fine too, I would like to have [@jaspervdm](/u/jaspervdm) back again for a long time period, honestly I do, but please, take your time, maybe one or two months could help regain the Community trust.

---

### Post by @lehnberg ⭐ (2020-10-20)
*Post #30*

[@johndavies24](/u/johndavies24)

> Where you stated very concerning things like suggesting there is no accountability or need to enforce accountability for individuals receiving funds

You have my post above. Please quote me directly where I suggest this. I’ve lost track of how many times I’ve asked you before, but here goes again, stop [strawmanning](https://en.wikipedia.org/wiki/Straw_man), it’s not constructive.

> You have chosen to not clarify these alarming statements, among others. Maybe you just meant no accountability for those who get a vote on your funds? Maybe you meant no accountability for those in your private chats? No idea what you meant…

If you don’t understand my ‘alarming’ statements, try asking me politely to clarify, instead of spreading FUD and taking your usual [concern trolling](https://www.wisegeek.com/what-is-concern-trolling.htm) approach to engaging on the forums.

---

### Post by @jaspervdm ⭐ (2020-10-21)
*Post #35*

johndavies24:

> But it would have gone a long way retaining trust if he communicated with us when he disappeared

You are absolutely right. I apologise to everyone in the community for not doing so. At this point the best I can do is pledge to communicate such issues in public instead of relying on a proxy, should they ever arise again (which I hope they don’t in the first place, of course). I understand that due to my actions I have damaged the trust some of the community members have put in me in the past. I don’t think anything I say right now will fix this, it is just something I hope to rebuild over time.

johndavies24:

> […] and then he reappeared the day (maybe a few days) before the council was going to vote to remove him from the council.

I understand this timing may seem suspicious, however my comeback was in progress for a while before this happened. It is not something I can prove but daniel already confirmed it above.

siNix:

> Stop paying people upfront, but pay each month.

This was raised during the meeting yesterday as well, and I have agreed to a monthly payment. I hope this will alleviate some of the concerns.

---



## Grin++ (mobile) - Progress update thread by @davidtavarez
*Date: 2020-10-14 | [Forum Link](https://forum.grin.mw/t/grin-mobile-progress-update-thread-by-davidtavarez/7894)*
*Importance Score: 118.6 | Core Participants: david, davidtavarez, lehnberg, quentinlesceller*

### Post by @davidtavarez ⭐ (2020-10-14)
*Post #1*

Hello, this is my [progress update](https://forum.grin.mw/t/request-for-funding-davidtavarez-grin-mobile-wallet/7774)… fasten your seatbelts.

**Grin++ Mobile Application UI/UX.**

After pivoting several UI concepts I came up to the one I would like to use. This one makes use of swipe gestures, tries to simplify actions and keep alive that punk look that we like… let’s see how.

**001 - Initial screen:** this is the first screen that we see

[ 0011080×2244 93.5 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/0cdbeb3f5f387b47677f230eb5a05401c3f29d48.jpeg "001")

**002 - Login screen:** after booting up, we can login into any of our wallets (in this case Personal, Donations and Test…), create a new wallet and restore it. This behavior is also present in the Desktop application.

[ 0021080×2244 116 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7895c1f96232bc14041e2de5131b60a02585f71e.jpeg "002")

Also, we can use our fingerprint to login after selecting a wallet.

[ 0031080×2244 177 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/66ecf4ef5d0f45d0bb86cf667241b47ace5b4961.jpeg "003")

Create a Wallet: Username, Password, Seed length and you’re good to go.

[ 0041080×2244 92.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c94d87c32829da293e2932574c5884be817991a4.jpeg "004")

Restore Wallet: we also can restore a wallet.

[ 0051080×2244 80.8 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/36f9fea16980e52d713f084279a0fa15026b5815.jpeg "005")

PS: I would like to, **later** , use an encrypted wallet seed to restore it, I don’t like that much the idea of sharing the seed in plain text.

**003 - Wallet screen:** after the login we see this screen, here we can appreciate our spendable and the “in progress” transactions: Receiving and Sending. If we want to see the complete history we swipe right and for receiving, we swipe left. To see the details of a transaction we just need to make click on the transaction row.

[ 0061080×2244 183 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/500478c8d5949a42b2f7dfcf4e825f051c0aec7f.jpeg "006")

Transaction details: important information regarding the transaction.

[ 0071080×2244 266 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4a56ed275352677498ce3f870e7999af79baf5e6.jpeg "007")

Transactions History: Completed transactions: Received and Sent, Cancelled and Coinbase.

[ 0081080×2244 136 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4984ab1da065e74c9cfe6ef89883f5bb1df157e3.jpeg "008")

Receive/Finalized: We can get this screen by swiping left from the Wallet Screen. Here we could Receive and Finalize a transaction using Slatepack. Also we can Enable and Disable the NFC, the feature here is that we could use proximity to make a transaction, for now this will be only available for Grin++, after making this stable enough I could migrate this to Ironbelly.

[ 0091080×2244 180 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/81c718b1aa313784d12aa2f78d684cd98a3d2514.jpeg "009")

We see here a big button with our address, if the wallet is available we will see this button in Green if not, the button will be in Orange. To share your address, you just need to make click like this:

[ 0101080×2244 320 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/9688b7fefaf78e372b1bd3ac8a97cf420fb39772.jpeg "010")

Now, if we want to send Grins, we could swipe up from the Wallet Screen.

**004 - Sending screen:** from here we can scan the Address using a QR Code, set the amount and choose a Sending method.

[ 0111080×2244 110 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/bbf4a0d27d62b8e42343410ed1a3e3c82ed2f445.jpeg "011")

**Without Interactivity:** Offline sending, this is the classical grin method using slatepack.
**Using Interactivity:** This means that the app will attempt to complete the transaction using Tor, if it fails the slatepack string will be shown. If the user wallet isn’t available (sender or receiver) the button will be disabled like it is in the screenshot.
**Through Proximity:** In the end this should be like an offline transaction but everything happens wireless (NFC), both sender and receiver should be close to each other.

If everything goes well, we should see this screen:

[ 0121080×2244 69.4 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3cdffbd88debc438e91399924fe21cfd874748f2.jpeg "012")

**Grin++ backend running on Android.**

[ 0002244×1080 142 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b792fc62752d86754dcb9af59ad38786dd871457.jpeg "000")

Grin++ has been compiled for Android and it’s able to sync after a while, but right now it isn’t stable enough because some device memory issues. Also Tor is properly running on Android.

There is a (_unstable_) branch for [Raspberry Pi](https://github.com/GrinPlusPlus/GrinPlusPlus/tree/linux-arm64) too in Grin++ github repository which uses Docker to compile an **ARM64** binary. If you know what you’re doing feel free to play a bit with it.

**Final thoughts.**

First, thanks to [@Mokhtar](/u/mokhtar) for helping me out to come up with the swiping gestures based wallet screen, I’m sorry for making you and [@david](/u/david) suffer with the earliest ugly UIs . Now, I will be open to any feedback for the UX/UI (not new features, please) while I’m working on mitigating the memory issues. The code will be released in the next progress update hopefully. At this pace we could have an **APK** for December. Stay tuned!

---

### Post by @quentinlesceller ⭐ (2020-10-14)
*Post #10*

Regarding the overall design. I think you should look at what BRD wallet and Tari Aurora are doing.
I find both app UX really great in term of setup and global usage.
I’m not fond of the multiple page where it’s not extra clear there is something else on the left and right.
Also I don’t think you need a Coinbase tab.
BRD login:

[ IMG_71481125×2436 111 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/9e8c4da8cb53697faa1c8691641c8030ff94995b.jpeg "IMG_7148")

BRD main screen (unnecessary in your case IMO since there is only Grin):

[ IMG_71491125×2436 342 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/52679ec5ccd15974e2e45d0c034e11613661a472.png "IMG_7149")

And Bitcoin main screen:

[ 6A93A190-0F6C-4529-B480-DB1D3AA27FDA_1_105_c602×1304 82.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/808fc18cffb63d769a920fde46495d2e7dbf7318.jpeg "6A93A190-0F6C-4529-B480-DB1D3AA27FDA_1_105_c")

And here is Tari first setup:

[ IMG_71521125×2436 46.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/26352784002a15878daaadd86db17302e80cbebc.jpeg "IMG_7152")

[ IMG_71531125×2436 25.8 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/04821fe75bb1b7e1a06d36c7aa0760ecac974725.jpeg "IMG_7153")

[ IMG_71511125×2436 268 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/df5d2aba45d8a6d2a918135529494f13937bb30e.jpeg "IMG_7151")

[ IMG_71541125×2436 144 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/0cdd0cd84fa2c3987e642c06cfcc6369128b919c.jpeg "IMG_7154")

[ IMG_71551125×2436 140 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/02f6066d7d38354fdb8394a54d8b7b077fcfa1b5.jpeg "IMG_7155")

[ IMG_71571125×2436 142 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/67457b835dbccbce256ef5b45e12ba374712907f.jpeg "IMG_7157")

[ IMG_71561125×2436 139 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/9d592a16a426be2b8842dbfa2eba707f575a70ef.jpeg "IMG_7156")

[ IMG_71581125×2436 124 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/8ef44eeeca70306e09cc6cd80651d4c3235e1558.jpeg "IMG_7158")

[ IMG_71591125×2436 145 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/242211433358de4b58d752bf49236c2a435f2752.jpeg "IMG_7159")

[ IMG_71601125×2436 230 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/81b1722b76da65cd3ece2df282c426762792da17.jpeg "IMG_7160")

You might also want to look at [Argent](https://www.argent.xyz) which I think looks great.
This is just my 2 cents , design is a very personal thing and it’s your app.

---

### Post by @davidtavarez ⭐ (2020-10-21)
*Post #14*

Now there is two more post to follow the process:

[Building and Running a full Grin Node (Grin++) on Android](https://forum.grin.mw/t/building-and-running-a-full-grin-node-grin-on-android/7917) [Development and Technical Discussion](/c/techtalk/9)

> BIG NOTES: the node is still unstable. I will keep this thread up to date. Do not waste your time trying to do this on Windows. The target for now is Android 10. The first thing that we need is the Android NDK. The Android NDK is a toolset that lets you embed components that make use of native code in your Android applications. Grin++ is written in the almighty C++ therefore we could use the Android NDK to build this little baby. At this moment we will need to download the NDK from the Canary (…

And…

[Building Grin++ for Raspberry Pi4](https://forum.grin.mw/t/building-grin-for-raspberry-pi4/7916) [Development and Technical Discussion](/c/techtalk/9)

> One of the biggest challenges is to be able to cross-compile dependencies, that’s why Grin++ uses [vcpkg](https://github.com/microsoft/vcpkg), which is a cross-platform open source package manager. In order to simplify the building process I decided to use [dockcross](https://github.com/dockcross/dockcross). The branch is public for everyone and can be found here: <https://github.com/GrinPlusPlus/GrinPlusPlus/tree/linux-arm64> and inside there is a Dockerfile. Te process is really straight forward: Make use of linux-arm64 docker image (based on debian:stretch-20190326-slim…

I will keep this thread exclusively for the updates and the app itself.

---

### Post by @davidtavarez ⭐ (2020-11-06)
*Post #16*

Some updates.

* The code of the mobile app is now public here: <https://github.com/GrinPlusPlus/GrinPlusPlusMobile>
* An apk can be downloaded from here: keybase://public/dtavarez/com.grinplusplus.mobile.apk (or <https://keybase.pub/dtavarez/>). Note: **the apk is using mocked data**.
* I will start connecting the UI with the API now.
* I will update the builds more often in case anybody wants to test.

In short words: now, I will be **focused on bringing the mobile app into life**! even if I’m not able to deliver all the features that I want for the first release, I’m still very confident we will have a fully functional Grin++ mobile app for December.

---

### Post by @davidtavarez ⭐ (2020-11-06)
*Post #17*

Some screenshots now.

[0011080×2244 125 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a6ad4eace95e013be964de03eb8fc06a6e31a2e2.jpeg "001")

[0021080×2244 87.5 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b16a39283eb699aaa9798ae86344806423c9c8f8.jpeg "002")

[0031080×2244 102 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/593c6169ef22aa0700bbad57857d4e8bd4ad497a.jpeg "003")

[0041080×2244 98.6 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/da954c0185b820fac60e912946c44c47f768e7d8.jpeg "004")

[0051080×2244 169 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7ab7105794d03b578d370c83234681eab6d222ba.jpeg "005")

[0061080×2244 184 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/58510df25e39e617af2035b89ba8fea90c4e54e9.jpeg "006")

[0071080×2244 176 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c8289f995b13b684fb750d72d5e900c8feb3dcf3.jpeg "007")

[0081080×2244 148 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f3f9407ebe155ec5dfe8779a3accf1a95d97d0c6.jpeg "008")

[0091080×2244 172 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/ff19469fe4a1fb359731e4b44ad2208f46c427f0.jpeg "009")

[0101080×2244 155 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/578b62a87afb3ca073391c7952eca7d8e586998b.jpeg "010")

[0111080×2244 95.3 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/106266fa67538c7b674cc79ccbd20ea6bba4c761.jpeg "011")

[0121080×2244 126 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/1d58bd6c19c324097a65a66b6bbedecebdc74af3.jpeg "012")

[0131080×2244 103 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/1de27243baeba57109d03d8762d429b033b098fb.jpeg "013")

[0141080×2244 147 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6d95524a19196245bbec88e5043bd16fbfe294fa.jpeg "014")

[0151080×2244 116 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b6261ac27aba572a5ba2ed6dbb311160e96408c3.jpeg "015")

[0161080×2244 63.2 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/54714294fb41518bf5d951e505a5859add649d99.jpeg "016")

---

### Post by @davidtavarez ⭐ (2020-11-26)
*Post #30*

grab a  and take a  'cause this may take a while

welcome to my latest progress update, this time I want to present not just the UI but also I want to explain the user flow to give a better look on where the mobile application is right now.

**booting up:** after opening the application, the node is also opened in the background, it shows the progress until the node is fully synced, then the user is redirected to the login screen after syncing the node.

[ 0001080×2244 75.2 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/1a70a3b6d7f0149733dd523fe8045e4283debb1d.jpeg "000")

[ 0011080×2244 160 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e18ffd3badd07e7332070f8da0fd5db0d928eed9.jpeg "001")

[ 0021080×2244 157 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/481a26f682847d652576df5098c7576973285953.jpeg "002")

[ 0031080×2244 170 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/70680072a2d5a6243fca3eaf2c248bff0dd65936.jpeg "003")

the first time the application runs, it could take a while… like, honestly, a lot… maybe… between **25** to **40** minutes depending on the device, but for a full node on a mobile phone I personally don’t think that is too much.

**open, create or restore wallet** : with grin++ users can manage multiple accounts (or wallets), this is possible also in the mobile version; from this screen users could either, open an existing wallet, create a new one or restore a wallet using a wallet seed.

if the fingerprint is available, the user should use their fingerprint to fully open the wallet after writing the password.

[ 0041080×2244 110 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/94ef31b2fb235fc7682175ff3a0f941e760fb564.jpeg "004")

[ 0051080×2244 94.9 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a5f6234cc08bc9cb964b09c35b65f91ab1a32be1.jpeg "005")

[ 0061080×2244 113 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7966a2822668a118bfdb7554815cf7bbf834dd82.jpeg "006")

[ 0071080×2244 95.1 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b250d467cb872cc0509fb307f720554e8d4cfd43.jpeg "007")

[ 0081080×2244 96.8 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6b77d85ff838fc267f9ceb0001267b748d16eb2d.jpeg "008")

[ 0091080×2244 86.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/d06d8cd5d432e858054d9c71f500ef323dba5a89.jpeg "009")

**wallet:** now, the user wallet is opened; the first tab shows the basic information of the wallet’s balance: spendable coins, immature, unconfirmed and locked, and below that table, the **in progress** transactions are listed.

[ 0101080×2244 148 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/0bd081b647f4e15a597e8cb9fa5ca5d9d01cd515.jpeg "010")

from the second tab, users can, first, see and share their **slatepack address** , but more important, the user can **check the availability** of the wallet through tor, where green means that the wallet is reachable, of course, orange means that the wallet is not reachable at that moment and white means: I don’t know yet ; this check is performed every 10 seconds.

to check the wallet availability I’m utilizing the hidden [grinaddresschecker](https://github.com/davidtavarez/grinaddresschecker) tor service and using tor as a socks5 proxy; the hidden service is hosted on a provider with 0 logs policy, therefore no ip, no request and no address is registered… also this service is paid in advanced for at least a year thanks to the donations of our beloved and wonderful grin++ users.

[ 0111080×2244 130 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7de5f2b6e7ddf5a0326c5b119a89304c4672dd44.jpeg "011")

[ 0121080×2244 124 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/036ab309313291e61eb37f28074aefc1879d7849.jpeg "012")

[ 0131080×2244 133 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6af4678d7ba9f81a34dbc60eab25f0dc9520b53c.jpeg "013")

**history:** maybe the most boring screen, from here the user can see the transaction history grouped by date, click on a transaction and see the details:

[ 0141080×2244 187 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a3b3d100e46f9bf8d698ca7919fb581db1b75b9b.jpeg "014")

[ screenshot-16064218905421080×2244 133 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/558b488f49870bccfcce0a49874f93bb6690d2f5.jpeg "screenshot-1606421890542")

**status:** I regret, this is the most boring one… as you can see, some basic information is displayed, including the connected peers; this information is also periodically updated.

[ 0151080×2244 144 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a3ca147177b57aebedcfc896c3025636bee31fb6.jpeg "015")

you see? it is just another screen

now… let’s go to the main dish: **sending** , **receiving** and **finalizing** … grab another … and a  or maybe … salud!

**sending:** after clicking on **send** from the first tab, a screen is displayed where the user sets the amount to send (also the **max** button can be used to send the maximum spendable available)

the next step is to enter the address by typing in the box or scanning a qr code.

[ 0171080×2244 126 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7d505a41d215f68602359d6fd625197f778d2f10.jpeg "017")

[ 0181080×2244 116 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e0cd9586890c7531610c516df06db81d53c6d3e2.jpeg "018")

[ 0191080×2244 147 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2c4563ef8ddd3fb286f1af8d96bc9cc85f0ca4ae.jpeg "019")

[ 0201080×2244 157 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f6fe33569f2ca2baeea9f376fda98e40653b2442.jpeg "020")

after setting the amount, the receiver’s address and an optional message, the user confirms the transaction details and can **send the transaction** or **cancel it** , not starting the transaction.

after confirming the details, the wallet attempts to send the transaction through tor:

[ 0211080×2244 66.1 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/1b7b63068d7eca642e22a37e6f8f5609dd2400a9.jpeg "021")

if it succeeds, the screen is closed, otherwise, a slatepack message is returned:

[ 0221080×2244 336 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c8c66f26420c6b960ecf7050bf485bb564fbe685.jpeg "022")

as you can see in the image above, the slatepack message can be copied to the phone clipboard or share it directly through another application… most people will say that the receiver could also read the generated qr code, but, **no** , the receiver won’t be able to read it correctly because that qr code isn’t properly rendered on a small screen since the slatepack message isn’t short at all (and technical details that are not worth mentioning).

scanning the qr from a desktop works perfectly, and this leads us to the next step: **finalizing the transaction** , which can be done from screen above.

before the sender can finalize the transaction, the receiver needs to actually receive the transaction… because the receiver’s wallet was not reachable while the sender tried to send the first time(or because of another reason), the receiver can also use grin++ to receive the transaction using the slatepack message:

[ 0161080×2244 118 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/af22297335e8546512523b487ba5b31236877f2d.jpeg "016")

from here, the receiver can paste the slatepack message from the clipboard, scan a qr code with the encoded message or type it manually (_yeah, good luck with that!_).

after receiving the slatepack message, the application will show the slatepack message that should be shared with the sender:

[ screenshot-16064253618131080×2244 336 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/353c6d6530e6caa8ad479a52fc5829a2bd1a763f.jpeg "screenshot-1606425361813")

the receiver can, from here, copy the slatepack message and share it with the sender.

the sender can finalize the transaction from their screen where the first slatepack message can be shared or, by swiping to the left on the box displaying the transaction like this:

[ 0251080×2244 180 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f55fb8d4f6306d77fa52766f93b5cff0ef96a790.jpeg "025")

[ 0231080×2244 121 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2223c9fac705cdf79cb46c23f9893b069e8cf3ce.jpeg "023")

the sender could also cancel the started transaction by swiping to the right on the same box:

[ 0261080×2244 111 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/492f0f9056893333b61b80b1b3ed7f1bc2d82872.jpeg "026")

[ 0271080×2244 174 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/d51b5498d1b0065dfadb96b1fabfba46ebca778f.jpeg "027")

[ 0281080×2244 148 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/0e1fd6180bb7101a9c012db7b1a5a3fc42d8c2e2.jpeg "028")

the transaction is then sent to the transaction history.

the end

.
.
.

now… the credits:

* Minimum version required: **Android 9.0 (API Level 28)**.
* Architecture supported: **64bit**.
* ARM: **AArch64** or **ARM64**.
* Minimum RAM recommended: **4GB**.
* Programming Language: **C#**.
* Framework: **Xamarin.Forms**.
* Source Code: [GitHub - GrinPlusPlus/GrinPlusPlusMobile](https://github.com/GrinPlusPlus/GrinPlusPlusMobile)

known bugs: there is a bug while trying the restore a wallet from the apk, the embedded node closes itself due (probably) to memory consumption… this bug is currently being tracked.

release date: **december 2020** after fixing the bug above and some other minor details.

---

### Post by @davidtavarez ⭐ (2020-11-26)
*Post #31*

second part… in this part I would like to answer some probable questions and offer a personal opinion…

but before even thinking about it, no! it won’t be backwards compatibility, this application fully embraces the changes made for the next hard fork… having said that… thank you, let’s continue.

what next? well, after releasing a first version there are three big features that I would love to add:

* coin control
* sending/receiving using nfc…
* a tool to overcome censorship helping users to set tor bridges.

also the desktop ui will be updated for the next hard fork and I will try to create an unified user experience… I want to take this opportunity to thank **Sasha Abramovich** for the feedback received and for [this amazing medium post](https://medium.com/beam-mw/360-roundabout-on-beam-ux-part-1-past-d4eb34d835cb)… (yes, yellow fellows, I asked some Beam friends for feedback, they have done a wonderful job).

as you all can see 2021 will be a busy year and I’m looking forward to it… I also plan to contribute to [IronBelly](https://forum.grin.mw/t/request-for-funding-i1skn-ironbelly-wallet/7733) on bringing some cool stuff available in grin++ (cough! nfc… cough! address availability…).

there are a few things that I’m kind of proud of… first, we’re a running a whole node in a mobile phone! and on a raspberry pi! I’m not sure if users would appreciate some interesting facts of the mobile app, but… I’m not storing any personally identifiable information, there is no analytics, the little information that is stored like the session token is stored encrypted, I’m adding rules to avoid that the node information like the wallets can be copied, and some others benefits of having the node running locally.

big kudos to [@david](/u/david) for his amazing job on the grin++ node/wallet backend… when are we going declare this guy out of this world?

to wrap up, I personally believe we’ve made some really cool progress, and when I say “we” I’m referring to grin… the slatepack is a huge improvement, I think that the flow described in my previous post could be a lot better when we get rid off the (infamous) third step, maybe, at that moment I would be fully convinced that the interactivity is a feature and not a flaw .

I love the idea of having full control of what it comes in and goes out of my wallet, but honestly, I think we can achieve way more without the third step.

---

### Post by @davidtavarez ⭐ (2020-12-08)
*Post #41*

Ready for another update??? grab a  or a  because this one isn’t that exciting as my previous one

* The Restore Wallet issue was fixed, now users can properly Create and/or Restore wallets.
* A button to Delete a wallet was added _[having too many testing wallets was driving me crazy]_.
* Users can now Backup their wallets _[I believe that we should export an encrypted binary, I will probably dig about it]_.
* A big bug with the Fingerprint on Android 9 was fixed _[thanks[@Mokhtar](/u/mokhtar) for the help testing the buggy apk]_ .
* A bunch of small bugs were fixed _[thanks again to[@Mokhtar](/u/mokhtar) for the help testing the buggy apk]_ .
* Before sending, the user should (if the Fingerprint is available) use the Fingerprint to confirm the Sending request.
* The Node starts faster now since Tor is controlled by the Service.
* The Node Agent was changed to: Grin++ (Android).

Now, there are **2 major** new improvements:

* The node is now running as a Service, this means that the allocated resources for the app are used to improve the UI interaction with the user. The app should feel light and smooth while the Operative System does the management of the Node and Tor processes.

* 3 Actions were added to the Notification Bar:

1. **Restart** : the user could restart the node manually in case that is needed.
2. **(Re)synchronize** : pretty explicit, right? but if someone does not get it: this will synchronize the chain again.
3. **STOP** : Isn’t it obvious? this will close the node and also, stop the Service.

[ photo53665940724012606561078×691 35.8 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e7b08db1e1369db1883e8baf1e5423eb8518ff26.jpeg "photo5366594072401260656")

[ photo53665940724012606551080×406 19.2 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/d52bd9705319552bc5ca99ed4da921f7a764d89c.jpeg "photo5366594072401260655")

Stay tuned! **Grin++ for Android** will be available this week!

---



## Request for funding @jaspervdm, Feb-Apr 2021
*Date: 2021-01-27 | [Forum Link](https://forum.grin.mw/t/request-for-funding-jaspervdm-feb-apr-2021/8313)*
*Importance Score: 98.4 | Core Participants: david, jaspervdm, davidtavarez, tromp, lehnberg*

### Post by @david ⭐ (2021-01-28)
*Post #4*

I’m glad to see you’re still wanting to contribute to Grin, but I have concerns with another full-time funding request. As a full-time contributor to Grin, I would expect to see you active on keybase and the forum, making steady progress on the code, providing regular progress updates, and just generally trying to push Grin forward daily.

Instead, lackluster coding efforts have resulted in PIBD dragging on for 6 months already with no clear end in sight. You’ve gone weeks on end without any meaningful contributions on github[1]. You’re only particularly active on keybase during meetings, and you don’t participate in any discussions about ways to improve Grin. Your forum activity consists only of a request for funding every 3 months, and a brief progress update every 2 to 4 weeks[2].

While you were once a passionate contributor to Grin, it’s clear that flame has gone out long ago. I’m concerned this fund is now being seen as a reward for past effort that you and a few others can continue to draw from at will with minimal effort. That is not the purpose of the fund. If it was, then I would be owed some serious cash right now

My recommendation is to withdraw your funding request, re-evaluate how much time you’re actually able to contribute, and then come back with a more acceptable _part-time_ funding request for one month at a time that contains a clear list of deliverables for the community to evaluate at the end of that month. Considering how hit or miss you’ve been with the past 2 funding periods, I don’t think I’m making an unreasonable request.

I don’t take any joy in being the guy who speaks up against these funding requests, but it’s necessary that someone does in order to preserve Grin’s image and to protect the fund so it’s available when we really need it. And while I may be the only one who speaks up publicly about the request, these thoughts are not just my own. I’ve spoken with others before writing this who have all echoed similar sentiments.

[1] [jaspervdm · GitHub](https://github.com/jaspervdm/)
[2] [Profile - jaspervdm - Grin](https://forum.grin.mw/u/jaspervdm/activity)

---

### Post by @david ⭐ (2021-01-28)
*Post #9*

Anynomous:

> Lol, when I saw you typing your comment I was already expecting a comment exactly like this as well as expecting [@johndavies24](/u/johndavies24) to like it . Often a ‘negative voice’, but that also has its function in this group.

Ha, this may come as a surprise, but I don’t actually enjoy being the negative voice at all. I’m not heartless - it really does bother me to have to say these things. I started writing that post as soon as I saw his request, but had to take a break for a day or 2 before finishing it. When nobody else seems willing to speak up against abuses of the fund though, I feel obligated to be the bad guy.

---

### Post by @davidtavarez ⭐ (2021-01-28)
*Post #12*

johndavies24:

> I saw this zcash ledger app funding the other day and thought it was a smart way to break a longterm project into bite size funding, but we could do even better and reward efforts so it’s not all feast or famine

I totally agree with this. The project was divided on payed milestone which is great in many ways: the community is able to see progress, there is an estimated time and there is more transparency with the funds, it is a win-win situation.

Anynomous:

> Also I know it is important to have enough ‘Full time developers’ on pay roll

I think that is also true, but we should have a clear goal and some estimations to avoid any kind of misinterpretation.

david:

> Instead, lackluster coding efforts have resulted in PIBD dragging on for 6 months already with no clear end in sight. You’ve gone weeks on end without any meaningful contributions on github[1]. You’re only particularly active on keybase during meetings, and you don’t participate in any discussions about ways to improve Grin. Your forum activity consists only of a request for funding every 3 months, and a brief progress update every 2 to 4 weeks[2].

Maybe it is just perception since there is no transparency on the amount of work required to finish the PIBD implementation. It is hard to estimate, but with regular communication we could avoid confusions.

jaspervdm:

> Plan and implement the parallel sync method. A fundamental part of the work is done, now that all the v5.0+ Grin nodes support serving of data segments. The remaining work can be roughly described as follows:

Sounds like a plan to me… but I have some questions [@jaspervdm](/u/jaspervdm)… 3 months are enough to do that and also this: `Improve the stability of both the node and the wallet`? Maybe this estimation is too optimistic, would you mind to detail a bit? From your last [progress update](https://forum.grin.mw/t/jaspervdm-progress-update-thread-nov-to-jan-2021/7960/6) you were working on a RFC, is this the same RFC? During these 3 months, are you going to write the RFC and the implementation? or how far you think you could go? does this includes the node and the wallet?

Having a way of tracking the progress on each item from the [wish list](https://github.com/mimblewimble/grin-pm/issues/385) maybe it helps to keep the community posted…

I would say that this should be expected from any funded dev

david:

> I would expect to see you active on keybase and the forum, making steady progress on the code, providing regular progress updates, and just generally trying to push Grin forward daily.

---

### Post by @jaspervdm ⭐ (2021-01-29)
*Post #20*

Anynomous:

> How about late locking, is that already (fully) implemented or is that on [@antioch](/u/antioch) to do list?

The late locking feature is enabled on the wallet and can be used with the `-l` flag. There is a known limitation currently in that the transaction cant be finalized if the required number of inputs changes. This could be solved by adding a second kenrel that pays for the difference.

* * *

[@david](/u/david)
The way I see it, there’s 2 concerns here:

* I have not been engaging with the community much outside of the meetings – this is definitely true. There are some reasons for it, but not something I am going to discuss here. Going forward what could help me is if we add an explicit expectation here, something like “funded devs should spend roughly X% of their time participating in discussions”.
* My output is not considered high enough – I work at the speed I do, I can’t change much about that. I do acknowledge I have the tendency to put my head down in certain periods which may make it seem like there is not much progress. However, if my output is not high enough to warrant funding and there is a candidate capable and willing to do the (pibd) work for a lower cost, I urge them to apply to the fund instead. It would be for the good of the project.

* * *

[@johndavies24](/u/johndavies24)
While I am not opposed to bounties on principle, I didn’t think that discussion was far along yet for me to consider it an option for now. If we were to flesh the idea more out it is a possibility, yes.

* * *

davidtavarez:

> From your last progress update you were working on a RFC, is this the same RFC? During these 3 months, are you going to write the RFC and the implementation?

Yes, it is the same RFC. And yes, during these proposed 3 months I would work on both writing the RFC and the implementation.

* * *

With all that being said, I am retracting this funding request for now. I am going to reconsider whether or not it is worth it for me to continue down this path.

---

### Post by @tromp ⭐ (2021-01-29)
*Post #23*

To sidestep the full time vs part time issue, would you be willing to request funding for completing certain tasks, such as finishing the PIBD design and implementation, which you can then work on at whatever pace best suits you?

---

### Post by @lehnberg ⭐ (2021-01-29)
*Post #25*

I’ve added a point to Tuesday’s Governance agenda about our view on funding requests, in lieu of the above.

I think there’s some valid feedback brought up, but I also think it’s being raised in a needlessly antagonistic and zero-sum way, and that’s a real shame.

Let’s think about how we can improve for the future, how can we set clearer expectations from both fellow community members and and the person raising the funding request, without throwing the baby out with the bathwater.

I don’t think Jasper pulling his funding request, is a win for Grin. Who’s doing PIBD now? Did we really need fewer hands working on Grin at this stage? How is it a win for Grin if Jasper works part time now? Does this mean work will progress faster? What’s to say this will give us better value for money?

If someone thinks that Jasper being funded is unfair, that they themselves or someone else deserves to be funded instead, then why not just submit your own funding request and do a better job contributing while you’re at it? Lead by example. Be the positive change you want to see in the world.

I don’t have a strong opinion about how best to proceed.

But I do think that “just doing a bounty program like monero or zcash” is not as easy as it sounds. Zcash has been having quite a lot of trouble it seems with their grants process lately, and Monero’s funding system has yet to be replicated successfully (to my knowledge) by any other project, and we certainly don’t have a large swath of bag holders that can donate to projects for the greater good.

Similarly, from the point of the funding requestor, asking for project-based funding for doing things that have not been done before, that are heavily R&D dependent, possibly also having other people and areas on the critical path to completion, would be akin to shooting themselves in the foot. You make an open ended commitment to work indefinitely on something for the same amount of pay. No professional in their right mind would ever commit to that unless they were dead certain they could deliver within their own estimations.

My position is and remains that beggars can’t be choosers when it comes to having people contribute to Grin’s codebase. We should have demands. We should be as precise as possible with those in order to ensure we get good value for money. If we’re not getting good value, we should pause and reflect and figure out how to improve (like we’re doing now). At the same time, we should be realistic and practical. Some progress is better than no progress. At the current size of the fund, contributing is not zero sum; If Jasper gets funded, that doesn’t mean someone else will not. More is more.

Let’s not deter people from asking for funding or ask them to retract their funding requests. Let’s not call them names. Let’s not ask them to work **less** for Grin. Let’s welcome them and help them do a better job instead.

---

### Post by @lehnberg ⭐ (2021-01-29)
*Post #28*

Yes agree, let’s not do that. Instead why don’t you come and participate in Tuesday’s governance meeting instead.

> Do you, [@lehnberg](/u/lehnberg), personally believe Jasper’s contributions this past 2 funding periods have been adequate enough to justify further funding?

I can say that I think out of all of Jasper’s funding periods, the last one probably wasn’t his strongest.

The one before (I _think_) is the one he took a leave of absence from and came back to do good on and really I have no cycles to spend dissecting that one beyond what we’ve already done in the past. I hope we’re ready to move on by now.

Whether these are “adequate enough to justify further funding”, feels like the wrong question to ask, I suspect the point I was trying to make above is not coming across, so let me try again to explain where I’m coming from:

We have a long list of work we want to get done for Grin. We know what this is. It would do the project good to have someone work on those.

If we’re concerned about whether Jasper will give us good value for money or not, asking him to withdraw his funding request and possibly apply for part-time in the future looks like a lose-lose* outcome to me: Grin has work it wants done, and now it either will not be done at all, or done slower. Jasper wants to work on Grin full time, and now he either should look elsewhere for a full time job or a part time job.

Instead, I’d be more keen on constructively working with Jasper, and concerned members of the community such as yourself, to find a win-win scenario, one where:
a) Grin as a project gets the work it needs done;
b) Jasper gets some sort of semblance of confidence he’ll get paid fairly for the work he puts in; and
c) Community members can feel some assurance that the general fund is spent wisely.

I don’t think this forum thread is the right place to brainstorm this (let’s discuss on Tuesday instead), but on top of my head a couple of things we could be doing:

* Insist on regular interval updates containing specific content that gives people better insight on progress.
* Ask for specific portions of his time to be allocated on engaging in forum and keybase discussions (if we think that’s worth while).
* Introduce check-points and reviews mid-way or at each month before deciding whether to continue or not with the current scope of work, or shift priorities to do something else, or stop the funding request altogether.

The possibilities are endless for figuring out win-win solutions, but it requires us to take a constructive approach in the way we go about things. In a regular jobby-job, we have people mentoring and coaching us, constructively helping us to get better and improve. I don’t see why we can’t have this here as well.

* * *

_*) If Grin had a list of other candidates ready to step up and fill Jasper’s shoes, it wouldn’t necessarily be the case. But me knowingly, we don’t, so it’s a lose-lose._

---



## Grin community projects - brainstorm & kickstart - funding available
*Date: 2021-02-23 | [Forum Link](https://forum.grin.mw/t/grin-community-projects-brainstorm-kickstart-funding-available/8466)*
*Importance Score: 93.7 | Core Participants: david, davidtavarez, tromp, quentinlesceller*

### Post by @Anynomous (2021-02-23)
*Post #1*

Dear all, I started this topic to:

* COLLECT, BRAINSTORM and DISCUSS COMMUNITY PROJECTS
(yes I love to capitalize)

During the last governance meeting it was decided that funding will be made available of which the spending will be mostly community governed. This funding is seperate from the funding for core development of Grin and will be used to fund interesting and fun Grin related projects.

Everyone is free to:

* submit ideas
* brainstorm
* discuss
* upvote
* downvote

Or in any other way contribute to the process of kickstarting non-core related Grin community projects. To give some examples, here are some of my crazy brain-farts/community ideas of which some are rather unfeasible.

1. Starting a test(net) Grin exchange
2. Building a web plugin to allow webstores to accept payments in grin
-was worked on long ago, not sure about the status
3. Building a name system on top of addresses to make Grin more human friendly
4. Implementing atomic swap for Grin
-was worked on long ago, not sure about the status
5. Build a private chat system that use the Grin network, litening network like [WhatSat](https://www.publish0x.com/blockchain-space/whatsat-the-whatsapp-of-bitcoin-xezwpx) or memory-pool for messages or for example for public key exchange
-credits of the idea go to [@Mokhtar](/u/mokhtar)
6. Build a Signal or Telegram (Telegrin [@FirsArgentum](/u/firsargentum)) plugin to automatically send, accept slate packs in messages from contacts for seamless integration with Ironbelly and Grin++ mobile wallet

### Community ideas

7. Educational material in a form of short (Doodel) videos exlaining Grin’s origin, higher level working and technicals
-credits of this idea go to @oryph
8. Improved cold storage, e.g. a seperate sign key for accepting Grin payments (hot privatekey) and sending Grin (cold privatekey).
-credits of this idea go to [@grn](/u/grn)
9. Build a Grin faucet to allow new users to play around with nano-grin/gots (10^-9 Grin) and learn how transactions work.
-credits of this idea go to [@EucliwoodHellscythe](/u/eucliwoodhellscythe)
10. Write the first, well seccond if you count the Grinoire, Grin book
-credits of the idea go to [@minexpert](/u/minexpert)
11. Creating a one click installer for grin + grin-wallet for all platform as a bounty
12. Creating an Aidrop workflow, pregenerated seed phrases
-used in a temporary account to accept e.g. 1 Grin
-with a special marker to make it so they can only be used to import and move funds to a wallet and not in ‘recover wallet from seed phrase’ since this would create a comromised wallet/
-for the future, possibly implement more complex and fun airdrops by e.g. using custom salts such as GEO location to attract cryptographers

…In other words, what would you like to see added to the grin ecosystem? Let us know which of the above projects you l(dis-)ike, or which community project ideas should be added to the list. Think crazy, be realistic and even better, get your hands and mouth dirty by getting involved in discussions, or even better, in the building process of these community projects.
Funding is waiting to be spend on any cool and feasible community projects .

---

### Post by @insider (2021-02-23)
*Post #3*

Examples 2 and 6 seem very promising to me.

In particular, everything related to the use of Telegram, I see it as a serious movement towards adoption. As Pavel Durov once wanted to do for his cryptocurrency under the ticker TON.

Once the creator of Telegram, Pavel Durov, intended to launch his own cryptocurrency. But the SEC did not allow him to do this because of participation in ICO of American investors. His vision of a messenger is related to cryptocurrency. And the fact that, say, bitcoin is not integrated into it, leaves the situation unsaid… Or it will happen soon. Or there are reasons why this will not happen.

I have no idea how to convey information about Grin to Pavel.

Everyone who uses telegram, in this case, can open their own store and create their own economy. I think this symbiosis (Telegram+Grin) is key for the future.

---

### Post by @Chronos (2021-02-23)
*Post #8*

I have experience in producing educational crypto videos. Here’s a similar playlist I produced for Peercoin: <https://youtube.com/playlist?list=PLvd1OhApu6fULYdoGIDBxlNl9qglo2vJG>

Is something like this what you have in mind?

---

### Post by @nirg (2021-02-24)
*Post #15*

Anynomous:

> Starting a test Grin exchange

If this becomes a reality on different terms than the rest of the exchanges operate, it will be amazing! Since most exchanges have established KYC, the Grin exchange for example could establish AYC (Anonymize Your Client).  A principle that allows the exchange of cryptocurrencies between users while respecting their anonymity and privacy.

I AM NOT A DEVELOPER(be forgiving  ) and what I will describe I do not know if it is realizable. User registration will only require email. Automatically a .txt file will be created to be stored in a secure place, so that every time you log in you need to add a lexarithm for security reasons. In the first login the first word number will be used, in the second login the second etc. When it reaches its end the user will be able to create a new one.

1.4qd56A 2.nNR91f 3.Tu5VMh 4.Xww14z ... 50.U09fkK

The user will then be able to deposit the cryptocurrency of his choice. I do not know if this can be done with slatepack method. The idea is this though. Slatepack message to be used in exactly the same way but to have the role of guarantor for the release of cryptocurrencies between users. For example we have user1 and user2 . User1 wants to buy 100 Grin from user2 for 1 btc. User2 accepts user1. This will be followed by the process of freezing the corresponding amounts of each user and automatically a slatepack message will be generated to user2. User2 sends slatepack message to user1 and user1 sends back the message generated to user2. If messages are compatible with this procedure, then the coins will be released to the respective addresses of the users. This will not only apply to Grin but to any cryptocurrency exchange.

What I am describing may be entirely impracticable, but as an idea I am thinking of something corresponding. That with exchangeable encrypted messages that will act as guarantors, the release of cryptocurrencies will be allowed between users.

---

### Post by @david ⭐ (2021-02-25)
*Post #23*

This is definitely a worthy project to fund in my opinion.

---

### Post by @tromp ⭐ (2021-02-25)
*Post #34*

Coinbase is waiting on certified legal opinions on where Grin is tradeable throughout the world…

---

### Post by @quentinlesceller ⭐ (2021-03-17)
*Post #42*

I was actually thinking about creating a one click installer for all platform as a bounty. I think that’d be great.

---

### Post by @davidtavarez ⭐ (2021-03-17)
*Post #45*

mmm maybe a installation using docker compose will also useful.

---



## Call for Grin Community Candidates for additional fund granting control
*Date: 2021-03-04 | [Forum Link](https://forum.grin.mw/t/call-for-grin-community-candidates-for-additional-fund-granting-control/8521)*
*Importance Score: 89.0 | Core Participants: david, tromp*

### Post by @tromp ⭐ (2021-03-04)
*Post #1*

Grin is a cryptocurrency that launched with no premine or dev tax of any kind, after a multi-year development effort by volunteers led by founder Ignotus Peverell.
The only source of funding for continued development comes from donations to the Grin General Fund [1].
Thanks to many generous contributions including two early bitcoin coinbase donations in 2019, and to the recent Bitcoin price surge, Grin now finds itself very well funded, to the tune of several million dollars.
The Bitcoin funds are held in a multisig wallet controlled by members of the Grin Council.

RFC 0014 [2] specifies the guidelines for spending the Grin Development Fund.
Funding requests are made in the Grin Forum, and 1-3 weeks later decided upon in a public government meeting.

Some community members have expressed concern that the current funding model leaves the direction of Grin development too much under the control of the 7 members of the Council and their vision of what Grin should be. A related concern is that a majority of funds is applied for and granted to several members of the Council.

In response, the Council has expressed a willingness to share funding control with people from the wider Grin community.
Following public discussions on what forms this could take, there are now 3 proposals in place [3][4][5], that call for a selection of community members to either add control of the single existing fund, or be in full control of 1 or 2 separate funds to be split off from the existing fund.

In order to streamline the challenges of selecting the best proposal and selecting candidates for that proposal,
we invite community mmembers with a keen interest in helping to fund Grin projects to put forth their candidacy and indicate which of the 3 proposals they prefer to operate under. All applications made before the end of Mar 2021 will then be considered in April to select the most prefered proposal and who will serve it.

Each candidacy should use its own thread (“New Topic”) under the “Governance” category on the Grin Forum [6].

[1] [Grin](https://grin.mw/fund)
[2] [grin-rfcs/0014-general-fund-guidelines.md at master · mimblewimble/grin-rfcs · GitHub](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0014-general-fund-guidelines.md)
[3] <https://forum.grin.mw/t/fund-alternative-a-grants-model-proposal>
[4] <https://forum.grin.mw/t/fund-alternative-a-split-fund-proposal>
[5] <https://forum.grin.mw/t/fund-alternative-another-split-fund-proposal>
[6] <https://forum.grin.mw/>

---

### Post by @tromp ⭐ (2021-04-15)
*Post #3*

For those who missed Tuesday’s governance meeting, I’d like to restate the outcome of the council’s deliberations on the candidacies.

Of the 3 proposals, the simple split fund looks the most viable in terms of filling the required number of seats with candidates in support, and has the council’s preference.

Four of the candidates in support of this proposal (davidtavarez, hendi, mcm-mike, and paouky) are on the council’s shortlist for acceptance, as long standing community members with recognized contributions.

We’d like to ask candidates

* who previously didn’t express support for the split fund proposal, to change their mind
* who did, to possibly restate/strengthen their case
* who missed the previous deadline, to come forward now

The new deadline is the end of Tue, Apr 20.

Then we’ll have a forum community vote (excluding newly made accounts) to decide on the remaining two seats (subject to council approval).

---

### Post by @tromp ⭐ (2021-04-24)
*Post #4*

As far as I can tell, the eligible candidates for the final two seats are, in no particular order (apologies if I overlooked anyone) :

<https://forum.grin.mw/t/grin-community-candidate-for-fund-granting-control-alex-promoteam>

<https://forum.grin.mw/t/grin-community-candidates-for-fund-granting-control-anynomous>

<https://forum.grin.mw/t/grin-community-candidate-for-fund-granting-control-cekickafa>

<https://forum.grin.mw/t/grin-community-candidate-john-davies>

<https://forum.grin.mw/t/grin-community-candidate-m-a-c>

Note that candidate hardman has withdrawn.

Other replies in this thread will be deleted.

We’ll do approval voting by “Like”-ing the candidates you prefer over the others, who you refrain from “Like”-ing,
Note that liking all of them has the same effect as liking none of them.
Likes from accounts created after the original call for candidates will be discarded, as will a Like from the candidate themselves.

I propose we look at the Like counts on May 24, noontime in UTC, approximately one month from now. The two most Liked candidates meeting with council approval will join davidtavarez, hendi, mcm-mike, and paouky to be in charge of the alternate fund.

---

### Post by @david ⭐ (2021-04-27)
*Post #8*

Responding on behalf of John Davies.
<https://forum.grin.mw/t/grin-community-candidate-john-davies>

---

### Post by @tromp ⭐ (2021-05-21)
*Post #12*

Reminder: the vote closes in about 3 days.
If you voted 10 days ago or more, you may have missed the last candidate to register for voting.

---

### Post by @tromp ⭐ (2021-05-24)
*Post #13*

The vote is closed and the top 3 liked are

1. Mac, with 19 eligible likes out of 21
2. Anonymous, with 16 eligible likes out of 18
3. John-Davies, with 14 eligible likes out of 16

Pending council approval, Mac and Anoymous will join davidtavarez, hendi, mcm-mike, and paouky to head the alternate fund.

Thanks to all candidates that applied, and to all users that participated in the vote!

---

### Post by @tromp ⭐ (2021-05-24)
*Post #15*

No, but I hope it can happen by next month.

---



## Resolved: D̶o̶ ̶n̶o̶t̶ ̶u̶s̶e̶ ̶G̶r̶i̶n̶ ̶(̶g̶r̶i̶n̶-̶w̶a̶l̶l̶e̶t̶,̶ ̶G̶r̶i̶n̶+̶+̶,̶ ̶I̶r̶o̶n̶b̶e̶l̶l̶y̶)̶ ̶u̶n̶t̶i̶l̶ ̶f̶u̶r̶t̶h̶e̶r̶ ̶n̶o̶t̶i̶c̶e̶!̶
*Date: 2021-03-18 | [Forum Link](https://forum.grin.mw/t/resolved-d-o-n-o-t-u-s-e-g-r-i-n-g-r-i-n-w-a-l-l-e-t-g-r-i-n-i-r-o-n-b-e-l-l-y-u-n-t-i-l-f-u-r-t-h-e-r-n-o-t-i-c-e/8620)*
*Importance Score: 117.2 | Core Participants: david, antioch, davidtavarez, joltz, tromp*

### Post by @Anynomous (2021-03-18)
*Post #1*

MCM-Mike (grinnode.live) — Today at 12:41
[@everyone](/groups/everyone)
There is some ongoing investigation about a possible problem with GRIN-Network at the moment.
This is just for your information as I currently do not have more details.

* Grin++ Telegram group was set to read only - David will update you there as well.
* Message from David: <https://twitter.com/DavidBurkett38/status/1372496601604820996>
* GRIN council is also investigating it

We will keep you updated in #announcements

@davidburkett@bitcoinhackers.org (@DavidBurkett38)
@MWgrin_fr This does not just apply to Grin++. Do not use Grin right now at all while we investigate.

Twitter•Today at 11:34

---

### Post by @davidtavarez ⭐ (2021-03-18)
*Post #5*

**EDIT: Let’s wait until v5.0.3**

---

### Post by @tromp ⭐ (2021-03-18)
*Post #11*

The former code accepted a rangeproof BP for output commitment O,
if BP appeared in the verifier cache as having been verified before.
This logic was faulty since the earlier verification was not necessarily against the same output commitment. The earlier verification could be against a different output, while the new one commits to a negative value.

---

### Post by @tromp ⭐ (2021-03-19)
*Post #45*

yunf:

> let btc do a rollback, how many people will agree?

Bitcoin _did_ do a rollback after a similar arbitrary inflation bug [1]
(which, curiously, also related to not checking for negative values).
They fixed the bug and made miners switch to a new bug-free branch which then quickly overtook the old chain so that even non-upgraded nodes would switch to the correct chain.

Needless to say, everybody agreed.

[1] [Strange block 74638](https://bitcointalk.org/index.php?topic=822.msg9503#msg9503)

---

### Post by @joltz ⭐ (2021-03-20)
*Post #53*

Just wanted to share a general summary as there still seems to be some confusion in this thread.

A potentially catastrophic attack was carried out against the Grin network with block `1136081`, hash `0002897182d8cf7631e86d56ad546b7cf0893bda811592aa9312ae633ce04813` by exploiting insufficient rangeproof cache verification logic.

This was a worst-case scenario attempted attack for any privacy coin: potentially undetectable inflation.

Fortunately, the attack was detected and mitigated by our community before any significant damage was caused.

The Grin ecosystem is diverse and robust with multiple implementations, notably Grin++, where logic was able to detect this attack and the creators were able to help mitigate the attack network-wide. With multiple implementations, critical flaws in one implementation may be caught in another, at a risk of potentially diverging on a single valid block etc due to differences across implementations.

Grin requires rangeproofs to ensure that negative commitment values do not create inflation scenarios. Without rangeproofs, it would be possible to create transaction outputs that artificially inflate the supply by using negative values. **Without a valid rangeproof to verify that an output is not negative, it is possible for a malicious actor to create transactions containing negative-value outputs along with high-value outputs that appear to balance out to zero new coins being created.**

In this case, insufficient validation in an optimization for caching verification for rangeproofs was used to attempt an exploit.

This attempt was discovered by a grin++ user due to their verification process and was relayed to the rest of Grin team by David Burkett as well as a fix to mitigate the faulty rangeproof caching logic.

In addition to fixing the underlying caching validation issue, network nodes needed to perform the following to recover:

* Rewind block 1136081 that contains invalid rangeproof
* Rewind headers with bad blocks built on invalid rangeproof block
* Improve peer banning around serving invalid blocks/headers

As a result, the Grin team released a series of hotfixes addressing the above issues as quickly as possible to minimize downtime for the ecosystem. Initially v5.0.3 was released to address the block rewinds, which was followed by v5.0.4 to address the header sync to properly filter “good” and “bad” blocks for all nodes.

With any coordinated, critical security fix like this we reveal the strengths and weaknesses of our ecosystems. These necessary upgrades were successfully deployed to one of the most decentralized networks in the blockchain ecosystem and are a testimony to the level of talent we have invested in Grin.

We are working to publish a CVE report with all of the technical details in `grin-security`.

---

### Post by @tromp ⭐ (2021-03-22)
*Post #67*

With the reorg well behind us, it’s nice to see it captured in these grinscan charts:

[ Screen Shot 2021-03-22 at 11.32.02 AM629×864 46.4 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/22c792eee58a7b05c4d5c3ab7a33d5ef1b591e0c.png "Screen Shot 2021-03-22 at 11.32.02 AM")

If I checked correctly, then [GrinScan - Block 1,136,317](https://grinscan.net/block/1136317) at 2021-03-18 23:59:11 UTC (the first of 4 blocks in the final minute of Mar 18) is the lowest difficulty ever block at Network difficulty 15,833,792.
Also, the drop from 174,816,158 at height 1136081 to 37,336,151 at height 1136082, is a record 4.68x reduction, due to (the fixed) [GrinScan - Block 1,136,081](https://grinscan.net/block/1136081) taking 14h 44m 44s to mine.

Kudos to our Difficulty Adjustment Algorithm for handling this gracefully.

The reorged branch went as far as height 1137458, 1378 blocks beyond the common ancestor at 1136080, as tracked by [GrinExplorer - The first Open-Source Grin Blockchain Explorer](https://grinexplorer.net/block/1137458)

---

### Post by @tromp ⭐ (2021-04-22)
*Post #72*

Doogevol:

> I think it was a soft-fork.

Correct. The bug-fixed code accepts a strict subset of the previously accepted histories. Non updated clients work fine as long as majority graph power runs fixed code.

---

### Post by @tromp ⭐ (2021-04-22)
*Post #74*

Anynomous:

> This difference in consensus that separates old and new nodes makes it a hard-fork technically.

That does not make it a hard-fork. To qualify as a hard-fork, new code must accept some history that the old code rejects. I.e. make new things possible.

If the difference is new code accepting a strict subset of old code, then that by definition is a soft-fork.

---



## Request for funding @gene (Adaptor signature atomic swaps GRN-BTC)
*Date: 2021-03-20 | [Forum Link](https://forum.grin.mw/t/request-for-funding-gene-adaptor-signature-atomic-swaps-grn-btc/8632)*
*Importance Score: 96.7 | Core Participants: tromp, davidtavarez, lehnberg*

### Post by @gene (2021-03-20)
*Post #1*

# Who am I

My name is Gene Ferneau, and I’m a developer and cryptographic engineer. My focus is on privacy-enhancing technologies and cryptocurrencies.

I have been following Grin for a while, and want to become more involved with the project’s development.

# What is the project

This project aims to create a `no_std` library for performing adaptor signature atomic swaps between Grin and Bitcoin.

Atomic swaps are a great way for the decentralized exchange of cryptocurrencies. They remove the need for arbitrage and custodial exchanges.

Recently, Aumayr et al. authored the paper [“Generalized Bitcoin-Compatible Channels”](https://eprint.iacr.org/2020/476.pdf) which formalizes earlier work on adaptor signatures, introduced by Poelstra for use in [scriptless scripts](https://download.wpsoftware.net/bitcoin/wizardry/mw-slides/2017-05-milan-meetup/slides.pdf). The main focus of Aumayr’s paper is on generalized payment channels with application to Payment Channel Networks, like Bitcoin’s Lightning Network. Essentially, instead of Hash Time Lock Contracts, adaptor signatures are used to construct the contracts neccesary for payment channels.

Partial signatures are made on channel creation, revoke/punishment, state update, and closure contracts. If either party “adapts” the partial signatures into full signatures, the “witness” (private key) for the full signature is revealed to the other party. By revealing the secret, if either party breaks the contracts,
the other party is able to punish, or force close the contracts. The witnesses are also used by both parties in the update and “peaceful” closure of payment channels.

Codifying the rules with adaptor signatures allows for secure and private construction of payment channels. Removing the need for HTLCs also enhances privacy of on-chain transactions, since adaptor signatures are indistinguishable from normal signatures to outside observers.

Atomic swaps using adaptor signatures can be seen as a special case of payment channels, and can be performed between cryptocurrencies using Schnorr or ECDSA signatures.

The theoretical basis for ECDSA-Schnorr adaptor signatures comes from Hybrid Anonymous Multi-Hop Locks from Malavolta’s et al. work [“Anonymous Multi-Hop Locks for Blockchain Scalability and Interoperability”](https://eprint.iacr.org/2018/472.pdf).

In addition to adaptor signature contracts, online watchtowers are needed to constantly monitor the Grin and Bitcoin blockchains for on-chain transactions.

If either party attempts to break the contract of the Funding and/or Commit transaction(s), e.g. the transaction does not appear within a certain time threshold, the watchtower must notify the other party to cancel the swap.

On the Grin side of the swap, Schnorr signatures will be used, with ECDSA on the Bitcoin side. Schnorr signatures are currently being considered for activation on Bitcoin, so Schnorr-Schnorr adaptor signatures will also be possible in the future. For some time, ECDSA will still provide a larger anonymity set for Bitcoin transactions.

Providing a secure option to users for choosing Schnorr or ECDSA on the Bitcoin side is a future goal for the project, after implementing ECDSA-based atomic swaps.

The library should be able to be integrated into the main grin-wallet implementation, and other Rust wallets like Ironbelly.

With some work, C interfaces can also be exposed to enable integration with C/C++ wallets like Grin++ and Bitcoin Core.

# Project milestones

* Implement cryptographic primitives needed for adaptor signatures

* use [secp256k1](https://github.com/rust-bitcoin/rust-secp256k1) and/or [secp256k1-zkp](https://github.com/mimblewimble/secp256k1-zkp) as much as possible
* use [bitcoin-hashes](https://github.com/rust-bitcoin/bitcoin_hashes) as much as possible
* Pedersen commitments
* SHA256
* [Fischlin transformation](https://crypto.ethz.ch/publications/files/Fischl05b.pdf)
* NIZK proof of exponent using Fischlin transformation
* NIZK proof of exponent for partial ECDSA signatures
* Schnorr signatures
* Partial Schnorr signatures
* ECDSA signatures
* Partial ECDSA signatures
* Bulletproofs
* Implement on-chain Grin transactions for atomic swap contracts

* use [secp256k1-zkp](https://github.com/mimblewimble/secp256k1-zkp) and [grin-wallet/libwallet](https://github.com/mimblewimble/grin-wallet/tree/master/libwallet) as much as possible
* Funding transaction
* Commit transaction
* Implement on-chain Bitcoin transactions for atomic swap contracts

* use [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) as much as possible
* Funding transaction
* Commit transaction
* Implement adaptor signatures for Grin-Bitcoin side of the swap

* Schnorr-ECDSA adaptor signature multisigs
* Implement adaptor signatures for Bitcoin-Grin side of the swap

* ECDSA-Schnorr adaptor signature multisigs
* Implement watchtowers for monitoring on-chain transactions

* may or may not be `no_std` depending on need to interact with the OS
* Ensure Funding transaction appears on chain within a certain blockheight delta threshold
* Watch for Commit transactions being signed to claim funds on the opposing blockchain
* If timeout occurs, reclaim own funds from the Commit transaction
* Expose C interfaces for C/C++ Grin and Bitcoin wallets

* Any wallet able to consume a C API should also be able to use these interfaces
* Full documentation of the public API and details of the project

* Documentation efforts will be ongoing throughout the life of the project
* Test suite including unit and fuzz tests

* Integration and functional tests using Grin and Bitcoin testnets

* Testing efforts will be ongoing throughout the life of the project

# Outline of atomic swap transaction flow

GRN fnd -> <- rcv BTC fnd -> <- rcv GRN

2-of-2 multisig on funding and commit transactions

Gary is the Grin funder

Blair is the Bitcoin funder

* Gary sends Blair their proof of ownership for outputs used in the swap
* Gary’s proof also includes a bulletproof proving the output is at least as large as the agreed swap amount + fees
* Blair sends Gary their proof of ownership for outputs used in the swap
* Each party verifies the other party’s proof of ownership
* Gary creates a (unsigned) funding transaction with the outputs in the proof
* Blair completes their half of the interactive transaction, and sends to Gary
* Blair creates a (unsigned) funding transaction with the outputs in the proof
* Blair sends the transaction to Gary
* Each party verifies the other’s unsigned funding transaction
* Each party creates their half of the multisig on the other party’s funding transaction
* Each party verifies the other’s multisig on the funding transaction
* Each party creates a commit transaction sending coin to the other party
* Gary creates a partial signature on their half of the BTC-GRN commit transaction
* Blair creates a partial signature on their half of the GRN-BTC commit transaction
* Each party verifies the other party’s partial signature
* Gary signs their half of the multisig on the GRN-BTC commit transaction
* Blair signs their half of the multisig on the BTC-GRN commit transaction
* Each party verifies the other’s signature on the commit transactions
* Each party completes their half of the multisig on their own funding transaction, and posts to the respective blockchain
* After the height lock expires on the commit transaction, each party adapts their partial signatures
* Adapted signatures reveal the spending secret for the other party to claim their funds

Commit transactions will use a lock height to ensure sufficient time for funding transactions to appear on their respective blockchains. Aumayr et al. use a value of 3 blocks. Since Grin’s block schedule is shorter than Bitcoin’s, a lock height equal to 3 Bitcoin blocks should be used on the Grin side (i.e. 30 blocks).

The funding transaction needs a conditional lock height on the Grin side to ensure Gary can retrieve their coins after a certain time (e.g. Blair fails to post their funding transaction). Similarly, the Bitcoin funding transaction should have a conditional lock height. The lock height should be higher than the time expected for an honest completion of the swap protocol.

If, at any stage, verification of signatures and/or proofs fail, the protocol must be stopped. Any timelocked funds should allow the lock to expire, and reclaim the funds.

Bitcoin multisignatures may either be implemented using multisig contracts, or 2P-ECDSA threshold signatures.

* [Grin multisig - multiparty outputs](https://docs.grin.mw/wiki/transactions/contracts/#multiparty-outputs-multisig)
* [Grin multiparty timelocks](https://docs.grin.mw/wiki/transactions/contracts/#multiparty-timelocks)
* [Bitcoin multisig](https://en.bitcoin.it/wiki/Multisignature)
* [Bitcoin timelocks](https://en.bitcoin.it/wiki/Timelock)
* [2P-ECDSA](https://eprint.iacr.org/2020/540.pdf)

# Potential issues

Further research is needed to fully implement the atomic swap protocol, and the protocol outlined above may change during implementation.

I have done my best to perform due dilligence in my research so far, but some details only come up during implementation.

The future is uncertain, and for any number of reasons, I may be unable to finish the project.

My plan is to provide in-depth documentation, and clearly understandable code.

Good documentation will be beneficial by making it easier:

* for review / feedback
* for other projects to integrate the library
* in case I need to hand off work to another person / team.

# Project timeline

Timelines are difficult for research-intensive projects. The best estimate I can give for an optimistic timeline is ~3-4 months for a minimum-viable-product.

There could also be unknown problems that come up, that may mildly or drastically extend the timeline.

# Funds requested

I am requesting 40.000 EUR equivalent in BTC, based on the 60-day [rolling average](https://en.wikipedia.org/wiki/Moving_average) at the time of payout.

I would prefer payouts based on milestones achieved to prevent an all-or-nothing situation.

I am open to suggestions on funding amount, and payout schedule.

Being new to the Grin community, I would understand hesitance over my competence to complete a long-term project. So, I am very open to discussion about possibilities for increasing funders’ confidence in my abilities.

---

### Post by @tromp ⭐ (2021-03-21)
*Post #6*

Funding request are discussed and decided on in the next governance meeting after the request has been up for a week.

---

### Post by @lehnberg ⭐ (2021-03-22)
*Post #12*

Added to the agenda: [Agenda: Governance Mar 30 2021 · Issue #410 · mimblewimble/grin-pm · GitHub](https://github.com/mimblewimble/grin-pm/issues/410)

---

### Post by @davidtavarez ⭐ (2021-06-01)
*Post #15*

I’m glad to see progress on Atomic Swaps, I think this is something that a lot of people are asking for a long time. The work done and the commitment to delivery Atomic Swaps is undeniable.

I do remember that the funding request was discussed and approved during the past March 30th meeting, but the request changed a bit during the meeting, would you mind to clarify how was approved, please? it was approved as 10k monthly month by month?

Thanks.

---

### Post by @davidtavarez ⭐ (2021-10-12)
*Post #18*

Definitely! I thought this was solved.

[@stakerV](/u/stakerv) would you mind to add this to today’s meeting? We need to find a resolution to this ASAP.

---

### Post by @tromp ⭐ (2021-10-12)
*Post #21*

gene:

> Over the few months working on atomic swaps, I did my best to go above and beyond for Grin. Please pay me for the work I have completed, and the Grin council agreed to fund.

I agree payment is overdue.

Regarding the deliverables, I was under the impression that funding was for an implementation of Succinct Atomic Swap, with the distinct advantage of needing only 1 tx on the bitcoin side. You abandoned that approach and went with the inferior non-succinct atomic swap.

I didn’t have time to review the new RFC until recently, but found its protocol description rather unclear. Could you address my comment on [Atomic Swaps by GeneFerneau · Pull Request #83 · mimblewimble/grin-rfcs · GitHub](https://github.com/mimblewimble/grin-rfcs/pull/83) ?

---

### Post by @tromp ⭐ (2021-10-20)
*Post #25*

gene:

> The fact that one failure path leaves one party with the traded funds, and the other funds burned doesn’t sit right with me.

I have that exact worry about your form of atomic swap, while I convinced myself that S.A.S. is safe as long as parties don’t get close to the time-out.

gene:

> Either way, I need to take a deeper read of the spec.

Likewise I need a closer look at your protocol, but the current write-up makes that hard, as it doesn’t show in what order txs are constructed, pre-signed, and broadcast.

---

### Post by @tromp ⭐ (2021-11-03)
*Post #26*

gene:

> I can go over your comments, doing a partial rewrite to clarify the issues you brought up.

You have yet to provide a clear and correct description of the protocol steps, which is crucial for reviewing your work…

---



## Grin-Bitcoin Adaptor Signature Atomic Swap update thread
*Date: 2021-04-02 | [Forum Link](https://forum.grin.mw/t/grin-bitcoin-adaptor-signature-atomic-swap-update-thread/8689)*
*Importance Score: 103.2 | Core Participants: tromp*

### Post by @gene (2021-04-02)
*Post #1*

Hi everyone, I’m starting this thread for weekly progress updates on atomic swaps using adaptor signatures.

Over the past week, I’ve made decent progress implementing the cryptographic primitives needed for ECDSA adaptor signatures.

* Fischlin proofs: <https://github.com/geneferneau/fischlin>
* Dual Schnorr consistency proofs: <https://github.com/GeneFerneau/adaptor/blob/main/src/schnorr.rs>
* ECDSA pre-signatures + verification: <https://github.com/GeneFerneau/adaptor/blob/main/src/lib.rs>
* Exposed some necessary functions in rust-secp256k1: [https://github.com/rust-bitcoin/rust-secp256k1/compare/master…GeneFerneau:adaptor](https://github.com/rust-bitcoin/rust-secp256k1/compare/master...GeneFerneau:adaptor)

Not sure if the changes would be welcome upstream for `rust-secp256k1`, so will open discussion through an issue/PR. Depending on how the discussion goes, I may end up re-implementing ECDSA adaptor signatures as a libsecp256k1 module. Then expose interfaces in rust-secp256k1. TBD

Some problems came up when trying to implement Positive ECDSA pre-signatures. Because pre-signatures are not verified normally, I’m having a problem with the dual Schnorr proofs when `s` is negated (to ensure `|s| <= (q-1) / 2`).

The concrete NIZK proof isn’t specified in the paper, and I designed the dual Schnorr proof based on the scheme specified in <https://tools.ietf.org/html/rfc8235>. It works when `s` is not negated, but fails when `s` is. Still working on how to modify the proof to make it work, and still retain all its security properties.

When verifying the pre-signature in a way closer to how the original ECDSA schemes are verified:

r == f({H(m) * s^-1}*g + {r * s^-1}*X)
when r = k*g during signing

the signature verifies even when `s` is negated (as expected). So, the problem is definitely in the Schnorr proof I’m working on.

Will keep working on the problem, since it is fundamental for the security of the adaptor signature scheme.

After I solve the issue with the dual Schnorr proofs, I’ll continue with implementing the witness extraction and adaption algorithms.

When those are finished most of the cryptographic primitives will be finished™ (still need more testing and refactoring). Then I can start working on integrating the signatures into `mimblewimble/grin-wallet` and a PoC wallet using `rust-bitcoin/rust-wallet`.

Please feel free to ask questions, and give feedback in this thread.

Thanks for reading

---

### Post by @tromp ⭐ (2021-04-23)
*Post #7*

gene:

> I’ll implement the 3 transaction version of SAS, at least to start. This won’t require any watchtowers.

I agree that the 3 tx version is a lot more practical. It also doesn’t need relative timelocks, which is good in that NRD kernels are not activated on mainnet.

gene:

> After getting the 3 transaction version complete, I may work on the 1 transaction version.

You mean the 2 tx version?! I would not bother with that one; I consider the online/watchtower requirement too onerous for only a 1 tx savings. It’s a different story for payment channels, where the requirement appears unavoidable.

---

### Post by @tromp ⭐ (2021-05-15)
*Post #11*

gene:

> or on the RFC

Is there a high level overview of your succinct atomic swap protocol yet that you can share, that shows the role of this “atomic nonce” ?

Would it be reasonable to extend it to 64 bits and not bother with any filter since the odds of reuse would be too small?

---

### Post by @tromp ⭐ (2021-06-02)
*Post #18*

RubenSomsen:

> Is it the case that in Grin one can indefinitely delay transactions from confirming?

Not easily. Once broadcast, and present in mempools, a tx is bound to be included in a subsequent block. The attacker would have to fill up the mempool with days worth of txs to prevent new ones from fitting.

RubenSomsen:

> In Bitcoin Alice can use CPFP to guarantee that both the `Revoke tx` and `Refund tx #2` to go through in a timely manner, even if the initial fees are too low.

Once Grin blocks start filling up, we can revisit the mempool logic to
achieve the same functionality in Grin. One suggestion I made is a RBF where the replacement has a higher fee_shift (essentially a tx priority level).

RubenSomsen:

> You would only need the `success tx` (T0, revealing Bob’s nonce), one `refund tx` (T1, revealing Alice’s nonce) and the `timeout tx` (T2, optionally revealing Bob’s nonce), all spending directly from the `on-chain tx` .

In fact the Grin protocol already kinda behaves like that. Since Grin has no relative timelocks yet, we replaced the ones on Refund #1 and Timeout by absolute timelocks. Now when Alice wants to do Refund #1, she just waits for its timelock and then performs the aggregation of Revoke and Refund #1. Similarly, Bob can perform the aggregation of Revoke and Timeout when the time is right. So we might as well remove the separate Revoke.

So we end up with something like

+----------+             +-------------+  1 day        +----------+
| 87k Grin |  --Fund-->  | 87k Grin    |  --Refund-->  | 87k Grin |
| Alice    |             | Alice + Bob |  reveals      | Alice    |
+----------+             +-------------+  secretA      +----------+

|    |
|    +--Timeout-------+
|      2 days         v
|
|                +----------+
+--Success---->  | 87k Grin |
reveals         | Bob      |
secretB         +----------+

+-------+         +-------------------+
| 1 BTC |  ---->  | 1 BTC             |
| Bob   |         | secretA + secretB |
+-------+         +-------------------+

---

### Post by @tromp ⭐ (2021-06-02)
*Post #20*

RubenSomsen:

> So then Alice runs the risk of Bob simultaneously sending `Succes` and both secrets becoming known. Alice can avoid this by sending `Revoke` first, instead of aggregating. Again, you could certainly choose to simply accept this risk, but to me it seems wise to prevent this from occurring.

Ah, yes; I overlooked that the purpose of the separate revoke is to take away Bob’s option to execute the Success transaction before Alice reveals her secret. I agree we shouldn’t take the risk.

---

### Post by @tromp ⭐ (2021-06-12)
*Post #27*

RubenSomsen:

> Well, I’ve been arguing that this isn’t secure. I’m not sure what more I can say to make the need for `Revoke` more clear.

Beyond that, Refund #1 cannot be a single Grin tx since it has two separate spending conditions.

---

### Post by @tromp ⭐ (2021-06-15)
*Post #30*

gene:

> So, is the atomic swap described in [grin docs ](https://docs.grin.mw/wiki/transactions/contracts/#atomic-swap) also insecure? If so, why?

That one looks secure to me, but is much less attractive in that it requires two bitcoin transactions, and requires the bitcoin holder to start. Also, the hashlock reveals the nature of the transaction.

---

### Post by @tromp ⭐ (2021-06-15)
*Post #32*

gene:

> For the hashlock, I would replace with a normal transaction signature under the aggregate secrets used in the atomic swap, so it would look like a normal transaction.

On a closer reading, it is not a hashlock, but a regular secret public key x*G. It is still abnormal in having a alternate timelocked spending condition.

gene:

> Could also wrap the Bitcoin transaction in a timelock

I don’t know what you mean by wrapping here.

gene:

> Why would there need to be two Bitcoin transactions?

Because that’s how atomic swaps worked before S.A.S. Bob locks up bitcoin that either gets refunded or spent by Alice learning a secret.
S.A.S.manages to avoid the refund by first setting up a more complicated revoke mechanism on the other side.

gene:

> Why would the Bitcoin user have to start?

That’s how that particular protocol is setup. You could make a variant where the Grin user starts though.

---



## [Withdrewed] Request for Funding @davidtavarez: One-time use Slatepack addresses for Wallet (RFC and Grin++ Implementation)
*Date: 2021-04-06 | [Forum Link](https://forum.grin.mw/t/withdrewed-request-for-funding-davidtavarez-one-time-use-slatepack-addresses-for-wallet-rfc-and-grin-implementation/8707)*
*Importance Score: 156.8 | Core Participants: david, joltz, davidtavarez*

### Post by @davidtavarez ⭐ (2021-04-06)
*Post #1*

## tl;dr

On April 1st my previous [funding request expired](https://forum.grin.mw/t/davidtavarez-progress-update-thread-q1-jan-mar-2021/8320/4). In order to advance the [Post 5.0.0 wish list](https://github.com/mimblewimble/grin-pm/issues/385) I would like to tackle the **One-time use Slatepack addresses for Wallet and implement this in Grin++**. This implementation requires a [RFC](https://github.com/davidtavarez/grin-rfcs/blob/master/text/0001-rfc-process.md).

### What do I want to achieve?

The **SlatepackAddress** is a shareable **bech32** encoded **ed25519 public key** that can be used both to route synchronous transactions and to encrypt asynchronous transactions. We can use Grin HD wallets to generate deterministic ed25519 public keys and therefore Grin addresses. Addresses are being generated using keychain paths.

I will bring the possibility for the users to be able to use one-time Slatepack addresses.

### Why I want to do that?

One-time addresses is a tool to **protect users privacy** and are very common in a large variety of cryptocurrencies. Grin should definitely give this option to the users. One-time addresses are not the same as addresses from different accounts, this One-time addresses are tied to an specific account. Users can use one-time address [for each account](https://github.com/mimblewimble/grin-rfcs/blob/86d8d7d648760441d3ecea304774f82db00da470/text/0010-online-transacting-via-tor.md#addressing).

### Time Estimations/Plan

In this situation it would be hard to estimate time. I will considered this as **finished** when the **RFC gets approved**. This process could take x amount of time that I am not aware of. **The plan is to have a working implementation on Grin++ of the RFC**. This will help us to see this working and polish the UX. The implementation of this RFC on `grin-wallet` will depend on the Rust team priorities.

Anyways, if one wants to be pessimistic I would say that in 2 months this should be merged into the Grin++ master branch. But since Grin have this 2-weeks cycle for the Developers meetings, I might be shooting myself in a foot by giving an estimation because I can’t say when the RFC will be approved and I can’t predict the potential suggestions .

### Funds requested

I am requesting **10.000 EUR** equivalent in **BTC**. I will place a PR for the RFC and also, I will have this feature released on Grin++ Desktop.

### Logs

[github.com/GrinPlusPlus/GrinPlusPlus](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/168)

####  [Address generation after receiving transaction and on demand, new Tor Bridges endpoint and more](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/168)

`master` ← `feature/multiaddresses`

opened 06:28PM - 06 Apr 21 UTC

[ davidtavarez ](https://github.com/davidtavarez)

[ +805008 -215 ](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/168/files)

Taken from the [Post 5.0.0 wish list](https://github.com/mimblewimble/grin-pm/is[…](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/168)sues/385) this PR attempts to implements One-time use slatepack addresses for Wallet. This is still Work in Progress since we need a RFC to introduce this change. The plan is to explorer the implementation, see the challenges and address them. I will edit this comment to give more details.

[Request for Funding, @davidtavarez: Q1 (Jan-Mar) 2021](https://forum.grin.mw/t/request-for-funding-davidtavarez-q1-jan-mar-2021/8073) [Governance](/c/governance/10)

> tl;dr On December 14th my funding from [the previous campaign](https://forum.grin.mw/t/request-for-funding-davidtavarez-grin-mobile-wallet/7774) expired. This is a request for a 3 months period (Jan - Mar 2021). Rate: €6,000/month . Working time: 28 hrs/week. What do I want to achieve in these next 3 months? My main focus will be to take [Grin++ mobile](https://forum.grin.mw/t/grin-for-android-v0-0-1/8070) to a stable version, this will require at least: to keep the arm64 branch of Grin++ up to date with master. improve the Tor interaction. fix the found bugs during the beta period. allow to Initialize a transaction without req…

[Request for funding @davidtavarez (Grin++ mobile wallet)](https://forum.grin.mw/t/request-for-funding-davidtavarez-grin-mobile-wallet/7774) [Governance](/c/governance/10)

> TL;DR I’m planning to release a mobile version of Grin++ for the next, and maybe the latest, hardfork (around Jan 15 2021), therefore I would like to spend more time and energy on this task, that’s why I’m opening a request for a 3 months funding period. I want to have a fully featured mobile wallet. Intro I met Grin at the begining of 2019 and got attached to the idea of a cryptocurrency built to be used as a means of payments. I ended up contributing to Grin++ by completely rewriting the UI c…

_**EDIT: This funding request was not approved.**_
_**EDIT 2: Added Withdrawed at the title to avoid misunderstanding.**_

---

### Post by @davidtavarez ⭐ (2021-04-22)
*Post #6*

I’ve been experimenting a bit. There are 3 potential flows for this.

**#1. Automatically generate a new address after receiving a transaction.** Many BTC wallets allow this, and people are familiar with this, but after shortly testing this flow, it is a bit confusing to be honest.

**#2. Generate a new address on-demand.** This case is less confusing than #1 and very straight forward. The user would just need to demand a new address. But there is a downside, especially for Miners, they will need to set their address every time they want to withdraw.

**#3. Generate a permanent address and temporary ones.** This seems to be more flexible. We could set the address generated from `m/0/a/0` as permanent and we could allow users to generate new ones on demand. Having a list of addressed that can be used and reused at any moment could complement this flow.

What do you think?

---

### Post by @david ⭐ (2021-04-23)
*Post #16*

There is no practical reason for #1. Bitcoin wallets do that because their addresses are stored on-chain, so therefore reusing is discouraged. For Grin, much like Monero’s stealth addresses, the only time you really need a new one is if you have 2 separate online identities that you don’t want to link together (e.g. say I have 2 forum.grin.mw accounts and want to share addresses on both - I obviously wouldn’t want to use the same address).

I think #3 is ideal of course. The best approach is to have some kind of address management page that allows you to create new addresses, mark them as one-time, permanent, or limited duration (maybe 1 day). You can manually expire addresses, or manually restore old addresses as needed. This would solve all use-cases, but would require the most amount of work from you, obviously.

---

### Post by @davidtavarez ⭐ (2021-04-26)
*Post #19*

I would like to summarize this including the feedback received.

I’m proposing a feature. Grin could offer the possibility of having **extra addresses** for each account.

### Reusable, Disposable (one-time) or Permanent.

Addresses can be: reusables, disposables or permanent. Reusable means that this address can be used more than once at any moment. Disposable or One-time Use Address, can’t be used again after receiving a transaction. A Permanent address is the default address. Currently by default we are using the address generated from `m/0/a/0` where `a` is the account, this could be the initial address. A permanent or default address is the address that is used to create the default listener by the wallet. This wallet does not change automatically, only can be alternate by the user manually.

### Listeners

Only one permanent address and one extra address can be enabled (listening) at the same time, to avoid confusion.

### Addresses Manager

Addresses should be managed by the wallet using the local database with the current state, the type and an alias. More about how this should work will be written in the RFC.

### Optional

This feature must be optional and could be enabled and/or disabled by using a configuration flag. The default value is: disabled.

### Miners

Miners could use a different address for each pool and enable the address using the alias, since transactions are interactive, this won’t represent any problem.

### What about in a context of User Level _interactivity_ or **UITX**?

I don’t see any incompatibility with the flow described [here](https://forum.grin.mw/t/transaction-interactivity-levels/8786).

---

### Post by @davidtavarez ⭐ (2021-04-27)
*Post #25*

vegycslol:

> what is the difference between a permanent and reusable address? Here I mean as an example of when a reusable address would be used

Since extra addresses can be an optional feature, users can opt-in and opt-out at any moment. I said above: Permanent or Default; it is permanent because this address does not change at least you manually pick another address to be your permanent one. Default, because this address is the one that it will be listening whether you have the feature enabled or not. Since you can disable the feature, the last permanent address will be your default address.

What is the difference between one-time address and reusable then?

[onetime_1701×386 7.56 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/bee4644ae9c2032deafcd3999e41c532fe9d579e.png "onetime_1")

Disposable means that I can not use that address after completing the receiving process because it is a one-time use address. Reusable means that I can use this address at any moment. For example, If I am mining in two different pools, I can create two address, one for one pool and one for another pool.

Let’s say I don’t want to share my default address and I’m not mining, in this case I can create disposable addresses for each transaction. Or maybe I’m currently receiving payments on my default address (`m/0/0/0`) but I want to start using disposable addresses, I just need to enable the feature and that’s all.

Also, I could change my default address without using extra addresses.

[disabled703×385 3.76 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/69e2f2def0c6e1f6584809261473d6730516978b.png "disabled")

vegycslol:

> If yes then I see a problem with using one-time addresses since if you’re not doing it synchronously (eg. manual confirmations) then when you will be doing multiple transactions your tor address will expire before the user manually confirms

I [asked](https://forum.grin.mw/t/transaction-interactivity-levels/8786/9) explicitly about the flow of a manual confirmation just to make sure I’m not missing any step. For a manual confirmation, the transaction is not “received” until you accept it. In this case, a disposable address won’t expire until you accept the transaction.

Now… if you want to go only with a manual confirmation flow, maybe you will need to be able of having multiple extra addresses listening at the same time in order to receive multiple transaction using different address which are not your default one. In other words: you may want to enable different addresses at the same time besides the default one.

Your screen may look like this then:

[multiple696×393 7.53 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/5b657b7f7e89ae5fcd41267662f6294b756f2c8f.png "multiple")

Let me know if I’m understanding your point of view please [@vegycslol](/u/vegycslol)

---

### Post by @davidtavarez ⭐ (2021-04-27)
*Post #30*

Emyn:

> I even remember [@davidtavarez](/u/davidtavarez) trying to reinvent the encrypted wallet.seed file several months ago… So I think that [@vegycslol](/u/vegycslol) is doing a good job vocalizing these possible issues as soon as possible.

I said it once, and I’ll say it again: I don’t like, no… **I hate** to be introducing word by word my Mnemonic Seed in a proper order to restore my wallet; specially at 2, 4, 5 am while I’m coding a GUI (Desktop/Mobile) to make things easier for users. I’m sorry if this bothers you, but after hours and hours testing over and over again, I realized that I hate that process and I found that it is so much easier if I could just “import” a file to restore my wallet. I’m not afraid of saying it

vegycslol:

> how would multiple disposable addresses work through tor

Multiple disposable addresses listening/enabled you mean? The basic process is very simple. We can add multiple [tor listeners](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/168/files#diff-d16845f1e2840e641b279d56e632b105d788e727e9120fabd361d59450216e40R245) for the same foreign server (RPC API). From an encrypted slatepack we can get the `SlatepackAddress` [of the recipients](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0015-slatepack.md#encrypted-metadata), and since the wallet is managing the addresses list locally we can then [remove the listener](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/168/files#diff-706fd393e285609ea2fdbe4b38781010bc3693a6095152179443b616c3cc0ae3R171) and update the local database to set some kind of flag to avoid using that address again. Sure, this is a raw idea, I would need to put this in practice, if someone has a better idea, please let me know.

vegycslol:

> Can you have no default address - example: i might use one-time addresses for regular txs, but i also mine so i use some permanent default one. Then i decide to stop mining and would not want to listen on the permanent default one. The solution in this case is to just change the permanent address right?

Yes, the solution in this case is just generate a new permanent address. I don’t think we should change the current behavior, therefore I think we should avoid impacting it. Removing the default listener could confuse the user imo. Even if we can it doesn’t mean that we must.

Now, what would it happen with the addresses list if I restore my wallet somewhere else? Well, the process starts over again; we could just determine the last address used and I don’t find a practical use to exporting and importing the addresses.

---

### Post by @davidtavarez ⭐ (2021-04-27)
*Post #36*

I want to clarify some things to avoid any kind of misunderstanding. First, let me create a common ground:

* It doesn’t makes sense to have a RFC without an implementation.
* There are two implementations of Grin, one written in Rust (`grin-wallet`) and another one written in C++ (`Grin++`).
* Grin++ can be considered as much as official as `grin-wallet`.

I can understand that it could be a bit risky for the Core to fund this request as it is, because there was not a commitment from me to write this feature in `grin-wallet`. Right now, I can’t properly estimate the effort of writing this feature for `grin-wallet` and it is not ethical for me to make a commitment without even be able of giving a potential deadline while I’m receiving funds.

I thought that with a RFC and the Grin++ implementation anyone else could write the Rust code. Am I capable of writing the Rust code for this feature? Well, yes, but first, with a RFC available, second, having implemented the RFC in Grin++, and, third, investing an undefined amount of time.

Because of this undefined amount of time in one hand, and, in the other hand, a bunch of stuff to do for the Grin++ UI, and for Grin Android, I need to rethink this funding request as it was written. Also, my initial idea changed after collecting feedback from different people.

I need to reconsider the scope of the request, but more important, I would like to evaluate the priority of me working on this feature for `grin-wallet` instead of delivering more value for the Grin++ users. Does this mean that I will never work on the implementation for `grin-wallet`? No, in fact I’m more than open to do it, so when then? I don’t know right now. Will I open another Funding Request related to this? I don’t know.

---

### Post by @david ⭐ (2021-06-11)
*Post #53*

Anynomous:

> some members thought it would be a better fit for the community fund.

Again, what do you mean “better fit”? How can something be a better fit for another council if they’re both meant to be covering the exact same areas?

Anynomous:

> (I do not think it was rejected)

It’s clear it would’ve been.

I understand you have a natural tendency to put a positive spin on everything, but the positive spin is just distorts reality, and makes excuses for poor behavior in this case. The council made a huge mistake, and should’ve funded David.

The way they argued we were pushing devs away for wanting better accountability from a council dev who lacked all transparency and made only the minimal effort during his funded period, yet chose not to fund davidtavarez, a dev who always over-delivered and always asked for minimal compensation for his work, was annoyingly hypocritical. It showed that the barrier for council funding was much lower than the barrier for getting others funded, when in fact the opposite should’ve been the case.

---



## First Grin Mask
*Date: 2021-06-08 | [Forum Link](https://forum.grin.mw/t/first-grin-mask/9023)*
*Importance Score: 85.1 | Core Participants: davidtavarez*

### Post by @minexpert (2021-06-08)
*Post #1*

The strongest area in human memory is the visual side. You can forget a person’s name after hearing it carefully, you can forget his last name after hearing it carefully, but once you look at his face carefully, you will remember that face wherever you see it. To understand this, look at a photo of your schoolmates. You may not remember the names and surnames of some of them, but when you look at their faces, you remember who they are and what traits they have. Another example is when you think a lot about the name of a famous person and you may not remember it. But when you see his face, you will know that person is that celebrity you know.
In summary, visual memory is much more powerful and memorable. It is so powerful that sometimes we don’t forget what we see once for the rest of our lives.

**Grin Face**

At this point, we need to learn the value of Grin’s logo. Because the Grin logo is inspired by the human face and a person who sees it may not forget it for a long time with the effect of our strong visual memory.
Let prove it.

**Masks**

You may not have watched some of the movies and TV shows where the masks you have seen above. But if you’ve seen one of these at least once on social media, you probably remember that mask.
Is not it? Here is the proof.

**Awareness**

We need to realize that we have a very valuable logo. Because Grin’s logo has the human face, which is the thing that a person sees most in our life, and therefore it has the potential to take a serious place in our visual memory. However, let’s realize that only Grin has the human face logo, out of nearly 10 thousand cryptocurrencies. In summary, we are different, special and we have the most memorable logo.
So what should we do with it?

**What we need to do?**

We need to make use of this beautiful logo in a way that is more beautiful and spreads everywhere. In this, the easiest and most beautiful thing we can do is to make Grin’s mask. It will be the world’s first cute yellow-faced mask to represent justice and secrecy. It will be unique. Many who see it will remember it for the rest of his life.

**Road map**

Simple. One of us will design a three-dimensional Grin mask, staying true to the original logo. I think [@nirg](/u/nirg), [@lovelygrin](/u/lovelygrin), [@grinsun](/u/grinsun) or someone else can do it. As a community, we will open the mask designs for voting. The mask with the most votes will be the one we will support on behalf of the community.

**Things that have been tried so far**

By this time, there have been many people trying to spread Grin. However, many failed. Because the main issue that ordinary people are interested in is price and money. When you tell them how valuable a $28-30 million project is, they will only look at its price and price rise performance. But only a small community like us can see the intrinsic value of this thing. Therefore, we can now change the our mission.

**Mission**

Let’s forget everything and everyone. Let’s put aside all attempts to spread Grin. Let’s just put a mask on our face. Wherever we defend privacy and justice, let’s just wear our masks instead of talking.

Let this be a quiet and flamboyant protest. It is also the most effective one. Let’s be sure that someone who sees our mask will start to wonder about Grin and will never forget him again. This is the mission of our mask.

**Who are we?**

We are fishermen. We have Grin on the end of our fishing rod. To the fish, hey! We’re not going to yell that there’s Grin here. Because no sound can be heard underwater. We’ll just put the Grin on the end of our fishing rod and wait for them to come on their own.

Let’s do this!

---

### Post by @minexpert (2021-06-09)
*Post #4*

Yes there are various smile-emoji masks.
What we need is something that totally showcases Grin.

For the eye part, this place can be see-through

or

the middle of the eyes can be pierced.

---

### Post by @unknownus3r (2021-06-12)
*Post #16*

[ anonygrin377×533 46.2 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a92aae26733f8a3866b49756104ccd69ddf471cf.png "anonygrin")

Needs a tidy up but a quick and dirty MW ANON

---

### Post by @acidmax (2021-06-16)
*Post #26*

I am not a graphic designer

[ grin-mask-3589×581 103 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/9e852a1678daed364d3c10668ee8d896d1e292cf.png "grin-mask-3")

[ grin-mask-1794×794 371 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2ae7bbe735012034ebbcc5bf2121aa42fb7400e1.png "grin-mask-1")

[ grin-mask-1a794×794 367 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2a09c9254351719d7513e128bd7f4965ef120d98.png "grin-mask-1a")

---

### Post by @minexpert (2021-07-06)
*Post #40*

I would like to present the first Grin Mask to Ignotus Peverell.
This work will be called Ignotus Peverell. The name of mask will be Grin Mask.
Speaking for myself, I learned a lot like being humble, minimalist and humane from Igno. On behalf of all of this, I want to thank him here.

[ 2021-07-06 15.28.203024×4032 1.88 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/8efa63f9cad3bd7beaccd385f97877bfdd95a05d.jpeg "2021-07-06 15.28.20")

Anyone who defends the Grin ideology will be able to wear this mask.
I will share all the details of the mask soon. After the design is finished, we will need a manufacturer.

---

### Post by @davidtavarez ⭐ (2021-07-06)
*Post #41*

Dios mio! I want that backround!

---

### Post by @minexpert (2021-09-25)
*Post #53*

[@Anynomous](/u/anynomous)
Yes. We have completed the design.
Firstly, I would like to present Ignotus Peverell.

[ WhatsApp Image 2021-07-01 at 20.57.271838×2048 147 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f0a5dd92d252673d5ba486d78d999cd33f185646.jpeg "WhatsApp Image 2021-07-01 at 20.57.27")

Completed in mask. However, there is currently need time for this mask.
I believe Grin will be successful, but I think he needs a little more time to make himself heard. Because, when we think about it in detail, most of the cryptocurrencies that have been popular until this time either started with ideal(ethereum) or low inflation , either had a limited supply or distributed half of their supply in the first few years (monero). Due to this, faster purchases were made in these cryptocurrencies. However, due to Grin’s fair structure, both its supply is unlimited and its inflation is high. 2 factors together. These may require a longer time than others for the Grin to be valued.
Let’s just put it this way, it started with high inflation in Bitcoin, but the supply was predictable. Even if it was bought 1 bitcoin with very high inflation, every 1 bitcoin we buy has a rate of 1/21.000.000. But Grin doesn’t have this. The rate of each Grin taken is 1/∞ Because supply is unlimited.
So, i think, if supply is unlimited, the only solution is to lower inflation.

Why did I tell you this?
Because there’s a great idea out here. This idea is called Grin.
For these reasons now, it’s a great idea, even if it’s still undervalued! I believe this with all my heart.

I think, also it’s great at making the mask of this great idea. But both of them need time.
Just as people are not interested in Grin for these reasons right now or at least let’s say they’re waiting, they also may not be interested in his mask for these reasons.
Therefore, it may make more sense to realize this idea over time. Then this idea will be unlocked. I will do this but even if I don’t do this, someone else will run this idea. I am 100% sure of that.

---

### Post by @davidtavarez ⭐ (2021-09-26)
*Post #55*

Can you imagine a [Displate](https://displate.com/) of this?! wow!

---



## Let's create the ultimate Grin Wallet experience! (Grin++ UX/UI)
*Date: 2021-07-04 | [Forum Link](https://forum.grin.mw/t/lets-create-the-ultimate-grin-wallet-experience-grin-ux-ui/9092)*
*Importance Score: 96.6 | Core Participants: david, tromp, davidtavarez*

### Post by @davidtavarez ⭐ (2021-07-04)
*Post #1*

Grin++ experience is good but not perfect, and I want it to be perfect. I’ve been thinking how we can improve the Grin experience in general.

First, I’m going to start with a bold statement to set the baseline: **Let’s stop trying to shape Grin to be like another coin, and let’s fully embrace our uniqueness**. Grin is not Bitcoin, Grin is not Ethereum, Grin is not Beam, Grin is Grin. This sounds obvious but from time to time it is good to say it as a reminder. My intent is not to start another long discussion but to brainstorm what would the perfect experience for Grin be.

I know, I know, we want to make Grin usable, we want to be able to buy a beer using Grin, at least that’s what I want, after that I’m out, I’ll close my account and no one will see me again around; meanwhile… let me offer two easy examples…

## Better wording (?).

### Example: Slatepack

We have a comprehensive transaction building flow: Slatepack, but what that heck does that even mean?! I can’t even pronoun Slatepack 10 times in a row without making a mistake; is Slatepack “a pack of slates”? I honestly don’t know, I was not invited to the party when the Community decided to use that word, but even “slate” does not make any sense. I’m not a native english speaker, but neither “pizarra” or “Schiefer” makes sense to describe the transaction process. In Grin, a basic transaction looks like this:

Maria provides the amount, fee and her signature. Juan joins by adding an output for the amount, adds his signature and shares this with Maria. Maria finishes the transaction (_signs and broadcast it to the chain_).

Reading the above I ask myself 2 questions: one, where are Alice and Bob? maybe on vacation; two, and more important, Why do we use the word “Slatepack” for this?! Some ideas could be:

* Agreement
* Deal

Why is this so important? Because we could say something like this then:

1. The Sender create an agreement/deal to start the transaction and sends it to the receiver.
2. The Receiver sends the signed agreement/deal by him/her to the sender.
3. The Sender sign the agreement/deal signed by the Receiver.
4. Transaction is broadcasted by Sender.

And this makes a lot more sense for everybody. My question is: what other words can we change?

Note: [We also have Contracts](https://docs.grin.mw/wiki/transactions/contracts/), therefor I’m not sure if we should use “contract”.

## Uniqueness

### Example: SlatepackAddress aka Address (?)

People tend to associate Bitcoin addresses with something like a “bank account number”, but in Grin addresses are not the same, an address is literally that: an address, more like a Url. By definition: `SlatepackAddress` is a shareable bech32 encoded ed25519 public key that can be used both to _route synchronous transactions_ and to _encrypt asynchronous transactions_.

We previously used Tor addresses along side HTTP and also Files, to transact, what a mess! But the truth is there is no such thing as address in Grin. Addresses in Grin are more like “listeners”. For me, having [one-time addresses](https://forum.grin.mw/t/withdrewed-request-for-funding-davidtavarez-one-time-use-slatepack-addresses-for-wallet-rfc-and-grin-implementation/8707) is really important, but also the ability of running multiple listeners at the same time, why? Because we can! I personally don’t want to reuse the same “address”, but also if you’re a miner you could use one address for each pool and one address for personal uses, and the uses case go on and on…

## Next

The reality is that there is not a mass adoption of any crypto yet, not even a mass adoption of Bitcoin, why should we try to look like Bitcoin then? I’m not saying we’re better or worse, we are just two different coins. Another thing is that, because the lack of mass adoption, there is no such thing as a “standard ux/ui”, and even if there was, this is constantly changing, look what Android is today compare to what it was some years ago, for example.

I could go with a longer post, but I won’t, what I am going to do is to start sharing in this post a bunch of mockups with my ideas. This will be something long term, I want to make a Community driven effort to create the Ultimate Grin Experience and I need your help!

_EDIT 1: Correction of the transaction’s steps._

---

### Post by @davidtavarez ⭐ (2021-07-05)
*Post #7*

oryhp:

> Maria doesn’t provide a signature at step1

Yes, the steps sequence was meant to be below (now labeled by 1,2,3 and 4). Thanks for the correction, stupid mistake from my side.

oryhp:

> I think it’s very important that users understand that there are 3 steps in transaction creation and that they are actually putting a signature on it because without this knowledge, you can’t understand what transaction cancellation means or which transactions you _should_ cancel. I’m talking about [safe-cancel ](https://github.com/mimblewimble/grin-rfcs/pull/71) that actually performs a transaction behind the scenes.

But what are we doing is a self-spend by sender before the transaction is broadcasted, right? I missed the purpose of that RFC draft.

renzokuken:

> We do use a lot of complicated terminology

Totally, and it get worse by “forcing” Grin to look like other coins.

unknownus3r:

> Is it possible in Grin++ to put a tutorial overlay on first use like some apps do, they guide you through basics of the application until you tick a box “don’t show in the future”

Definitely, but what about simplifying terms and flows too? for example…

If a “Receive” action from a Receiver perspective truly means _to accept (by signing) an agreement/deal sent by Sender_ , I think it would be better if we use “Accept” a transaction instead of “Receive”.

But now, we have an interesting scenario because when an user receives grins ツ via Tor, what is actually happening is that the receiver is automatically saying something like: “I’m accepting the transaction sent by Sender”. Maybe, the idea of manually accepting the transactions isn’t that crazy at all. It could be like cash, accepting the incoming transaction could be seen as putting the a bill into my pocket or wallet and letting you know that I certify the authenticity of the bill. To be fair, this could be confusing at the beginning, I think it is because we’re biased, we tend to think like “bitcoiners are doing this, then we should do the same”, but maybe _we should not_. Maybe the most natural flow is to manually accept the transaction.

Grin should be simple enough like _cash_ but at the same time, it could be robust enough to attract advanced users.

It would be nice to travel to El Salvador and see what people are doing [now](https://www.bbc.co.uk/news/world-latin-america-57398274). Which wallets are being used there? Are they using the LN? Are they using a commercial banking app? Will regular people care about privacy in a year of so when the mafia bosses aka the government, goes after them to collect the taxes? Could Grin be used by regular people of El Salvador in a year or so?

I don’t know, maybe I’m overthinking all these stuff

---

### Post by @davidtavarez ⭐ (2021-07-05)
*Post #9*

**What is Grin (ツ)?**

Grin is a privacy-preserving digital currency built openly by people distributed all over the world and launched in January 2019. Grin is community driven effort, which means that Grin is not controlled by any company, foundation or individual. Its purpose is to serve as digital cash.

Grin a light implementation of a protocol called Mimblewimble. Mimblewimble requires only about 10% as much data storage as the Bitcoin network. This makes Mimblewimble highly scalable for storing the blockchain, significantly faster and less centralized. Furthermore, the nature of the protocol allows for private transactions that are highly anonymous.

Grin is designed for the decades to come, not just for tomorrow. To be used by anyone, anywhere.

**What is not Grin (ツ)?**

Grin is not Bitcoin, nor Bitcoin 2.0, Grin is Grin.

**How does ツ differ from other coins?**

Grin requires interaction between parties involved in the process of building a transaction. Well, addresses in Grin are used for two things, one, to encrypt the transaction information and two, to determine the Tor Urls of the parties involved in a transaction; this Tor Url is used to establish a secure and anonymous communication.

Grin scales mostly with the number of users and minimally with the number of transactions. Past transactional data can be pruned, making grin drastically lightweight compared to other blockchains.

---

### Post by @davidtavarez ⭐ (2021-07-08)
*Post #26*

Let’s think about when we use cash to pay for a coffee… what do I do? first, I open my wallet to get a $5 bill to pay for the coffee, then I realize I’m poor so I have no money in my wallet, then in a desperate move I check my pockets and I find an old bill (thank God ), I take the bill from my pocket, the cashier double-checks the bill (with all reasons), accepts it, and keeps the bill.

What did we do? Interact with each other, and if we want to emulate that, wouldn’t it be nice if could “establish the communication” with the cashier in the safest way possible?

Interactivity… well, what can I say about interactivity that hasn’t been said before? I personally have a mixed feeling when it comes to the Interactivity discussion… but if we agree on that one of the Grin’s purposes is to serve as digital cash, interactivity is actually a core characteristic of all transactions based on cash. So, for the sake of this experiment I’m going to assume that Grin is like Cash and then I’m going to (re)imagine the flow from a Receiver perspective.

### How should receiving grin look like?

Grin uses Tor to establish a communication between Sender and Receiver, something like: Channel?Tunnel? Avenue? Route? Canal?

I will discard the word “Channel” since it can be confused with Payment Channels, which allow users to make multiple transactions without commiting all of the transactions to the blockchain. I personally like: Route, because we can say something like this then:

> Grin uses Addresses to encrypt the transaction information and to establish a _**secure route**_ via the Tor network, where Sender and Receiver can anonymously communicate with each other.

And let’s be honest, that’s a really cool feature! With that in mind I can make the next assumptions:

* Addresses could be disposable.
* Reusing an address should be the exception, not the rule.
* Sometimes I would like to be able to run several “listeners” or “encrypted routes” or addresses at the same time.

It doesn’t make sense not to generate a new address every time I receive some grin, but I get if you don’t want to. We could even generate a new one after every send, but it would be a big mess. **We want to provide users with flexibility without making things confusing**.

Now we can think in these terms: **Disposable addresses** and **Reusable addresses**.

**Disposable** means that I can not use that address anymore after completing the receiving process because it is a one-time use address. **Reusable** means that I can use this address at any moment. For example, If I’m mining in two different pools, I can create two addresses, one for one pool and another one for another pool and I could start an encrypted route for each address at the same time.

But, we also want, one, to keep the compatibility for current users, and second, we want to keep things simple for those who don’t care about these things. In this case we can have a **Default** address, this address is always listening by default, and then it can be replaced manually by a new one.

_“Ok, David, but what about the Dust?”_ you might ask; [Jameson Lopp](https://www.lopp.net/) recently wrote an [article explaining the Bitcoin Dust Attack](https://blog.keys.casa/bitcoin-dust-attack-myths-misconceptions/), I will cite him for the sake of giving context.

> **What Is Dust?**
>
> Bitcoin dust refers to UTXOs with tiny values that are so small that they are economically unspendable. That is, it costs more (in transaction fees) to spend than the value of the UTXOs. It’s possible to end up with dust in your wallet due to poor UTXO management. It’s also possible to receive dust deposits that you did not request. This is because you can’t stop someone from sending funds to a valid bitcoin address and every bitcoin address that has ever received funds is publicly viewable on the blockchain.

He also said that “ _while it’s technically possible**it’s incredibly unlikely**._”, I also believe that but anyways we can solve this in Grin by:

* Manually deactivating a listener and generating a new address.
* Disabling the “auto finalize” behavior.
* Rejecting transactions below an amount.

This can be also solved in a non-interactive scheme, but the point that I would like to make is that it can also be easily solved with the interactivity.

Do we want wallets to automatically generate a hierarchical tree-like structure of private/public key pairs? Probably, yes.

Do we need [on-chain bookkeeping](https://forum.grin.mw/t/grin-hd-wallet-one-time-use-addresses-rfc/9028#on-chain-bookkeeping-1)? I’m not sure what pains we are solving with that.

Do we want all enabled addresses to be listening automatically? I don’t think so.

Do we want any of our wallet to be automatically on? I’m not sure, maybe I just want to transact off-line.

I feel it worth experimenting with this. I think about this as an opt-in feature, people are not forced to make use of these capabilities but they could at any moment.

### Screens

Initially the screen could look like this

[addresses_001615×490 8.22 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/9a80af657b16193f90d4ad42d7ececa82cb1bfa4.png "addresses_001")

One could manage the have extra addresses like this.

[addresses_002614×485 12.3 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/ceae1985c07ebc50e999acb261a13f6e4508c6f7.png "addresses_002")

---

### Post by @tromp ⭐ (2021-07-08)
*Post #29*

davidtavarez:

> **Disposable** means that I can not use that address anymore after completing the receiving process because it is a one-time use address.

I can use a payment proof to prove that I made a payment to a particular address. This makes sense for reusable addresses, that a receiver can publicize and tie to thier identity.

If that address is disposable then how do I link it to a particular recipient?

---

### Post by @davidtavarez ⭐ (2021-07-08)
*Post #30*

tromp:

> If that address is disposable then how do I link it to a particular recipient?

After validating both signatures, we just want to check whether one of the addresses belongs to the open wallet, right? we could agree on generating disposable addresses from a specific keychain path for example `m/0/[account]/0/x`, I can think in few ways to do it, but none of them very efficient way tbh. I’m open to suggestions. I think this is a good question.

oryhp:

> before receiving the coins

Makes sense to me.

oryhp:

> Some people could be annoyed because they’d need to click on the “confirm” button at step2

That’s another reason why this feature should be optional I think.

Anynomous:

> I like it, except that I am favour of putting reusable adresses under an account.

I have not stop to think about the keychain paths and it is a very important part of all of this. Thanks for sharing.

vegycslol:

> not sure whether we will ever support manual confirmations but if we do, it might be that `Sending Unsigned Transaction Agreement` went through, but the response from receiver’s wallet is `Waiting for user's manual acceptance`

I see… well, the more I think about it, the more I’m convinced that maybe it is time to have manual confirmations. This can be included within the API response to give a better feedback to the user.

vegycslol:

> I would probably have RSR go through TOR and business would create a memo committing to the content of the payment (explained a bit more [here ](https://forum.grin.mw/t/an-open-discussion-on-non-interactive-transactions/8510/73))

To have some consistency maybe we want to have RSR go through Tor too I guess, but I don’t the details of the implementation, I could take a look though. Regarding a memo I would say that it could be out of the scope for now, at least, for me because it could turn out into an endless and completely discussion.

An use case for a store using multi addresses is that the store could generate an address by day or for each invoice (in a RSR flow) and link the address with the buyer. This is something that should be manage by a payment gateway implementation probably.

---

### Post by @davidtavarez ⭐ (2021-07-09)
*Post #33*

Let’s assume we have a “manual_confirmation” flag in our configuration that means we want to manually confirm a transaction when is done via Tor.

SRS
Manual Confirmation Flow

Alice=Sender
Bob=Receiver
Alice wants to send 5 grins to Bob.

Bob’s wallet has `manual_confirmation=false`

Scenario A: Alice set the amount that she wants to send but not Bob’s address; since Alice did not provide any address, the slatepack is shown in Alice’s screen. Alice manually shares the slatepack with Bob. Bob manually sign the transaction and send back the slatepack to Alice. Alice’s wallet finalizes the transaction. The transaction is broadcasted.

Scenario B: Alice set the amount that she wants to send and Bob’s address; Alice’s wallet can’t communicate with Bob’s wallet via Tor, so the partial slate is shown in Alice’s screen. Alice manually shares the slatepack with Bob. Bob manually signs the transaction and send back the Slatepack to Alice. Alice’s wallet finalizes the transaction. The transaction is broadcasted.

Scenario C: Alice set the amount that she wants to send and Bob’s address; Alice’s wallet is able to communicate with Bob’s wallet via Tor. Bob receives Alice’s partial slate and responds back to Alice’s wallet. Alice’s wallet finalizes the transaction. The transaction is broadcasted.

* * *

Bob’s wallet has `manual_confirmation=true`

Scenario A is the same as the Scenario A written above.

Scenario B is the same as the Scenario B written above.

Scenario C: Alice set the amount that she wants to send and Bob’s address; Alice’s wallet is able to communicate with Bob’s wallet via Tor. Bob receives Alice’s partial slate and responds back to Alice’s wallet. Alice’s wallet can’t finalize the transaction because she did not receive a slatepack from Bob. Bob now sees an incoming transaction, but rejects the incoming transaction.

> What happens then? The transaction can’t be just hang there until the end of the times, right?

Scenario D: Alice set the amount that she wants to send and Bob’s address; Alice’s wallet is able to communicate with Bob’s wallet via Tor. Bob receives Alice’s partial slate and responds back to Alice’s wallet. Alice’s wallet can’t finalize the transaction because she did not receive a slatepack from Bob. Bob now sees an incoming transaction, accepts the incoming transaction. Bob is able of communicate with Alice’s wallet via Tor. Alice’s wallet finalizes the transaction. The transaction is broadcasted.

Scenario E: Alice set the amount that she wants to send and Bob’s address; Alice’s wallet is able to communicate with Bob’s wallet via Tor. Bob receives Alice’s partial slate and responds back to Alice’s wallet. Alice’s wallet can’t finalize the transaction because she did not receive a slatepack from Bob. Bob now sees an incoming transaction, accepts the incoming transaction. Bob is not able of communicate with Alice’s wallet. Bob shares the slatepack with Alice. Alice cancels the transaction.

> What happens then?

> What happens if Alice and Bob both cancels the transaction?

---

### Post by @davidtavarez ⭐ (2021-07-09)
*Post #34*

More mockups! I’m assuming we add an optional “Manual Confirmation” feature, let’s se…

# Transactions

The list of transactions could look like this:

[transactions_0001290×448 15.5 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2a6912a71c722a3734a41f9c5c5960501d09b686.png "transactions_000")

### SRS Flow

Since we can now manually accept transactions, we can see a new button: “Accept”. “Complete” is the same as “Finalize”; “Reject” and “Cancel” means that we’re either rejecting the incoming transaction or canceling the unfinalized transaction.

When we click on “Complete” it is the same process of what we know now as “finalize”.

[transactions_001790×473 11.2 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/8dc968db5846740df333a4bf512431798ef3db8f.png "transactions_001")

[transactions_002766×474 6.93 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/873320b8aad5769a92acbcfaa340203585a4d68f.png "transactions_002")

The new thing is the manual confirmation. When we click on “Accept” we are able of confirming the amount and the receiver address.

[transactions_003730×379 7.82 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/dd35200893dc2df01ef1195f50ffee5cdaec2ac1.png "transactions_003")

After accepting the transaction, our wallet will try to communicate via Tor with the sender, if everything goes well, we see something like this:

[transactions_004783×384 9.03 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/185aa038740c956e50915061224c0bb49eb998a5.png "transactions_004")

Well, the reality is that things can go wrong, and probably we could not reach the sender. In this case, we will need to manually share the signed transaction agreement with the sender.

[transactions_005781×605 14 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/70ea2c977c0d435ff3cf588e716a223e0599f1b1.png "transactions_005")

### RSR Flow

We could have also `invoices`. From the wallet we can:

* Generate invoices
* Pay invoices

When we generate an invoice, we will have an transaction pending for payment (`Payment Requested`), we need to wait for the sender to pay the invoice; this invoice then can be manually completed when the sender shares the transaction agreement aka slatepack with us. Invoices can be also canceled.

In order to register the payment, we should accept the transaction agreement signed by the sender:

[transactions_006768×470 11 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c1eecb1991fb55d53e38ec6c2e7a5f0296439ef5.png "transactions_006")

[transactions_007770×476 6.96 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2ec4568bd3b7b3c1ec94eff87155329ad442822e.png "transactions_007")

If we receive an invoice, we have a transaction pending for payment (`Payment Pending`); we can decide to pay it, but also, we can just reject it.

[transactions_008746×381 7.79 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/8626398bb8ff21267a2b866206be5a31c664cdea.png "transactions_008")

After clicking on “Pay”, we try to communicate via Tor with the receiver, if something goes wrong, we then should share the transaction agreement manually.

[transactions_009756×377 8.71 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6d4fca5bd66b5c0513c26d99a8b4463fcd00ba5c.png "transactions_009")

[transactions_010781×649 14.1 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/14c461a38aa3659f049b6cc9607b2979b431c5cf.png "transactions_010")

## Conclusion

Having both flows together (Sender-Receiver-Sender and Receiver-Sender-Receiver), in addition with manual confirmation for SRS, looks pretty similar. I don’t think it will add any confusion at all, we just need to be less technical and pick better wording to describe the transaction building process. Maybe “Add Signature” is over simplifying, that’s why “Add participant data” sounds a bit more accurate. We can keep iterating until we find a better way to describe things for the regular user. Achieving this will require to define and pass some RFCs, but again, **I think it is worth it**.

---



## List of Grin problems and their solutions - Open Discussion + Cool Website to compare Grin inflation
*Date: 2021-07-10 | [Forum Link](https://forum.grin.mw/t/list-of-grin-problems-and-their-solutions-open-discussion-cool-website-to-compare-grin-inflation/9111)*
*Importance Score: 104.6 | Core Participants: tromp, davidtavarez*

### Post by @BlackSnow (2021-07-10)
*Post #1*

-a potential inflation bug (like with all privacy coins)
-the balance is locked for the next minutes after you made a tx (like with monero)
-no ledger nano support (we hope soon)
-the tx graph issue “Researcher Breaks Mimblewimble, Deanonymizing 96% of Grin Transactions” (soon fixed?)
-the interactive tx (but if the receiver is online , it’s not interactive anymore)

That being said Grin has a lot of advantages too not mentioned in this post

Feel free to comment with potential solutions that could arrive to fix those problems

one of the the biggest ones seems to be the tx graph issue
“Obscuring transaction outputs from being linked by monitoring nodes is not something that’s covered by Mimblewimble’s privacy model. The ambition is to get there, but we’re not there yet”

[Medium – 19 Nov 19](https://medium.com/grin-mimblewimble/factual-inaccuracies-of-breaking-mimblewimbles-privacy-model-8063371839b9 "03:31PM - 19 November 2019")

### [Factual inaccuracies of “Breaking Mimblewimble’s Privacy Model”](https://medium.com/grin-mimblewimble/factual-inaccuracies-of-breaking-mimblewimbles-privacy-model-8063371839b9)

A detailed critique to an inaccurate research attempt.

Reading time: 6 min read

This statement was published in November 2019
Is there any progress on this issue ? Anything we can expect ?

If there was plenty of transactions in each block (with more adoption) , would it make Grin much more private ? How would it compare with monero regarding privacy ?

What about the inflation bug threat ? Is it highly likely ? Could it be devastating for Monero/Grin ?

btw I also wanted to mention I found this website about monero , this page compares 4 privacy coins with respect to the emission curve (monero , dash , zcash , grin)
<https://moneroj.net/compinflation/> (being updated now it seems)

Also I’ll repost that comparison image I saw on twitter

thanks

[ E0U6ENfXEAQeimo773×2048 138 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3e6ab254683d431495118e4f1989c8161e77eb18.jpeg "E0U6ENfXEAQeimo")

[ E2CsUEQVUAAz0Tr903×286 10 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/42d823db80ceb36c19a87c465abe97c3cb61ad58.png "E2CsUEQVUAAz0Tr")

---

### Post by @tromp ⭐ (2021-07-15)
*Post #28*

MerlinsBeard:

> Clearly amounts were not necessary to deanonymize 96% of the transactions

Clearly what the guy did was not deanonymizizing transactions, he was merely identifying their inputs and outputs, having no idea what amount was transacated or what address was sending or receiving,
let alone any clue about who were transacting or for what reason.

---

### Post by @davidtavarez ⭐ (2021-07-15)
*Post #31*

Grundkurs:

> Against this background, it is not surprising that the German government is planning to introduce a law requiring crypto wallet providers (!!!) to also identify the names of users of self-hosted wallets. What sounds like insanity in this area is explained against the background presented. ([Kryptogeld-Dienstleister sollen Namen erfassen | heise online](https://www.heise.de/news/Kryptogeld-Dienstleister-sollen-Namen-erfassen-6121763.html))

Die Bundesregierung has God complex! They’re insane.

Neo:

> Until some of these people think Grin’s privacy is enough, the other 99.9% are probably never going to hear about it Grin, since it has no compelling use case.

I think most people don’t care about privacy, hoping that they care about it is an already lost fight for me. Governments are all-in with CBDC projects, like [the EU](https://www.ecb.europa.eu/press/pr/date/2021/html/ecb.pr210714~d99198ea23.en.html); it will be interesting to see how a digital euro will comply with the GDPR stuff. Nobody knows what it will be happening in the future, what I believe is that some people will be surprised when politicians starts deciding what people should eat, wear, where to live, and what people must do with their money. Only then some people, and probably few of them, will care about privacy, and Grin, Monero, MWEB, Beam, Zcash, etc. will see their compelling use cases. We are all betting, our money is on our implementation of the Mimblewimble protocol, we’ll see who wins, probably we all wins or maybe we all lose.

I think the idea of no amounts and no addresses is a good start; [coinswap](https://forum.grin.mw/t/mimblewimble-coinswap-proposal/8322), along with one-time use addresses and manual confirmation helps. To have the peer-to-peer communication over Tor could be interesting to say the least. All this plus payment channels, improved payment proofs, atomic swaps, [etc](https://github.com/mimblewimble/grin-pm/issues/385). does not sounds bad, in fact, sounds pretty good and better when we remember that we can have all this in the palms of our hands.

---

### Post by @davidtavarez ⭐ (2021-07-15)
*Post #34*

Anynomous:

> Grin is not a privacy coin (because that is not its main objective), Grin is trying to be sound money/sound cash. And yes, sound money/cash includes the need for some privacy.
>  Therefore, from a marketing perspective, I do not think Grin should be marketed as a privacy coin, bust just as sound money/cash.

Privacy is the ability to keep things to yourself, to be anonymous is to hide your identity and I think Grin is trying to do both by implementing Confidential Transactions, Dandelion, Cut-through and Slatepacks. CoinSwap will also help.

Also I read somewhere that _**Grin is a privacy-preserving digital currency**_

---

### Post by @davidtavarez ⭐ (2021-07-17)
*Post #49*

vegycslol:

> I’m not sure perfect privacy is desirable

Privacy is a **right** to which every person is **entitled**. Privacy rights protect the public from **unlawful and unnecessary** government surveillance and **bad actors**. We must never give up on making Grin as privacy-preserving as possible.

Doogevol:

> For me one problem in grin is the lack of a unique definition what grin is.

Grin has 99 problems but a lack of unique definition ain’t one. Grin is a privacy-preserving digital currency built openly by people distributed all over the world. Grin is not another commercial project. It is built by a community for the community. It has no CEO and no investors. Grin owes nothing to any government, state or company.

---

### Post by @davidtavarez ⭐ (2021-07-17)
*Post #53*

Doogevol:

> For me that definition is not satisfactory, because it doesn’t help out to Identify grin, which I need for my use case as sound money. If I still try to do something with that definition, I wonder what no ‘no investors’ mean. What If I find someone pretending to invest?

to be a privacy-preserving digital currency means that Grin is committed to protect users privacy.
“built by a community for the community” means that Grin is a community effort.
“no investors” means that Grin doesn’t have to respond for a particular pressure.

I invite you to take a look into [Zcash and their Regulation Compliance](https://z.cash/wp-content/uploads/2020/07/Zcash-Regulatory-Brief-062020.pdf). They are a private company with VC investors, VCs invest in companies because they want profit, so in this case profit is over all principles. Let me give you some cites:

> Zcash has re-used the Bitcoin protocol for its t-addresses and transparent transactions, making it simple and straightforward to add support for Zcash to existing transaction monitoring systems

> This allows the VASP to detect transaction patterns that do not match that customer’s expected behaviour, and investigate further to determine whether the unexpected behaviour is suspicious.

> On occasion, it may be necessary to share shielded transaction information with third parties. The Zcash protocol has been designed to support two features that enable the disclosure of shielded transaction information.

Imagine a situation where a government tries to impose an illegal and unnecessary action upon you, which governments do on a day-to-day basis just because… what do you think it will happen when Zcash (and many other companies) has to decide between you and them? let me tell you: they’ll sell your ass off in a fraction of a microsecond.

In Grin we’re free of living not for profits but by principles.

---

### Post by @davidtavarez ⭐ (2021-07-20)
*Post #56*

oryhp:

> I think living without any controls is not the society’s optimum, the sweet spot is likely somewhere in between, but I don’t know what that is.

For these people there is nothing in between. Let me share with you what these people think: <https://twitter.com/McGuinnessEU/status/1417494008037879819>

> Cryptocurrency is one of the newest ways to launder money. Our rules will now apply to the whole of the crypto sector. We will ban anonymous crypto wallets and make sure that crypto-asset transfers are traceable.
>  …
>  And equally the whole financial world is changing. Crypto-assets are now common currency, if you like, but they’re anonymous. And I would refer you perhaps to the Financial Action Task Force website for a very simple graphic of how criminals corrupt the crypto-asset marketplace, and we are tackling that, and I think that is just timely that we are doing that.

Mairead McGuinness is an Irish politician, who has served as the [European Commissioner for Financial Stability, Financial Services and the Capital Markets Union](https://ec.europa.eu/commission/commissioners/2019-2024/mcguinness_en) since October 2020. Two of her duties were:

* Preserving and improving **financial stability,** protecting savers and investors and ensuring the **flow of capital** to where it is needed.
* Ensuring a common approach with Member States on **cryptocurrencies** .

These people are no joking at all. I won’t be surprised if they declare Grin, Beam and Monero tools for criminals. They exists to protect investors, they don’t care about regular joe. Today they say that they want to protect us, they just want to chase “criminals”, but Governments are creating new criminals by writing new stupid laws and regulations everyday. Tomorrow who knows what it will be considered a criminal activity.

I don’t care if Grin attracts those who are trying to not be owned by those sociopaths.

---

### Post by @davidtavarez ⭐ (2021-07-20)
*Post #63*

Cekic:

> Becuz of this political mindset of trying to control every inch of this open source project. This drove away many contributers. Community driven so called,simply not true.

I would prefer to avoid the Core vs Community rhetoric, this will not add anything constructive at this point.

vegycslol:

> That sounds very dangerous, we should try to objectively analyze what such privacy might bring us (pros and cons)

It can be dangerous probably, but I think most of the time it depends on who defines what is dangerous. I will give you an example. In South Africa, private guns are prohibited by law. Lately law abiding citizens are trying to defend their businesses and neighborhoods using… wait for it… guns!  who would have expected it… those who passed the laws enjoy the private protection mostly, while the rest of the people are being victimized by those who ignore all kinds of laws and regulations.

Privacy is and will be the last frontier.

---



## Request for Funding @scilio (CoinSwap Implementation)
*Date: 2021-07-28 | [Forum Link](https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149)*
*Importance Score: 191.1 | Core Participants: tromp, davidtavarez, joltz*

### Post by @scilio (2021-07-28)
*Post #1*

Hi everyone, I’m a long-time lurker and experienced developer hoping to get more involved with GRIN.

[@tromp](/u/tromp)’s [CoinSwap Proposal](https://forum.grin.mw/t/mimblewimble-coinswap-proposal/8322) appears the most promising attempt to solve transaction linkability in MW. Sadly it seems GRIN is temporarily short on developers capable of implementing such a complex system. Luckily I’m in a position to dedicate time to this project throughout the remainder of the year.

# Project Plan

This is a large project, so in order to facilitate incremental incremental evaluation and funding payouts, I’ll be breaking the project into smaller deliverables.

### Milestone 1: Server & APIs

* Define & document all public APIs
* Using JSON-RPC
* Create server project
* There are GRIN libraries in [rust](https://github.com/mimblewimble/grin), [c++](https://github.com/grinplusplus/grinplusplus) and [golang](https://github.com/blockcypher/libgrin), so I will evaluate each and then decide on language to use
* Implement APIs
* APIs will return basic success responses when requests are valid and errors for invalid requests
* Test framework will be written to spin up a local server and query the APIs

### Milestone 2: Single Server (Trusted) CoinSwap

Support a single server that users can submit self-spends to which will be aggregated daily with all other submitted self-spends. This includes at minimum:

* Validation of all incoming data against a live node
* Daily aggregation and broadcasting of the finalized transaction
* Basic reorg protection
* Automated e2e testing

### Milestone 3: Multi-Server (Trustless) CoinSwap

Support a fixed set of CoinSwap servers for trustless swapping.

* Data provisioning using encrypted bundles
* Inter-server communication
* e2e tests that spin up local servers 1-n, demonstrating the workflow against a mock GRIN node

### Future Plans

* Add better protection against spam, reorgs and other attacks
* Add wallet support in grin-wallet or grin++

# Project Timeline

Estimating the time for a project of this size can be challenging, but I’ve chosen milestones that I believe can be implemented in about two months’ time. Thus, this project is expected to be delivered in 6 months.

# Funding Request

I am requesting to be funded £50,000 for the total completion of the project, with regular payouts. I have not yet established a reputation with the GRIN community, so I propose weighting the later milestones greater than the earlier ones in order to prove myself and to incentivize completion of the project. My request is to be funded for each milestone upon completion and acceptance by the funding council in the following amounts:

* £10,000 for Milestone 1
* £15,000 for Milestone 2
* £25,000 for Milestone 3

I am of course open to suggestions for changes to any of the above details. Regular updates will be provided on the forum.

---

### Post by @davidtavarez ⭐ (2021-08-03)
*Post #6*

I like this and I will say the next:

* Open sourced the project since day 0, maybe we could create a repository on grincc github account.
* Milestone 1 includes the definition and documentation of all public APIs, I would like to suggest to do only that in a Milestone 0, including a architecture design before starting. Why? to have a better idea of how a deliverable will looks like.
* I found 6 months too optimistic.

A CoinSwap Implementation is a ton of work, and I think we all agree on having this done; Now, I would like to see a more detailed planning; perhaps, maybe it is better for [@scilio](/u/scilio) to have an atomic plan and evaluate if you are ok with working on payments based on progress made. I think this is a better fit when it is hard to estimate due to the big amount of work.

I have no authority to say how much anyone’s time costs, I’m just trying to find a more fair way to bring [@scilio](/u/scilio) aboard.

---

### Post by @davidtavarez ⭐ (2021-08-10)
*Post #13*

You don’t have a github profile, we don’t know you, we don’t know who you are, we don’t know nothing about you, why should we trust you? there is not a single reason to do that, and you’re aware of that. I respect your choice to remain unknown, and I support it. I don’t know if you will be working alone on this or how many hours you are able to invest on it, you or your team in case you’re requesting funds in behalf of someone else. We’re breaking our own rules by funding unknowns. That was not supposed to be like that, but it seems that the Community likes to selectively ignore rules, but that’s another topic.

Now, since we don’t know nothing about you, and even if we do know, we’re not sure that you will deliver, but since this is a need that the Community seems to agree on, I think we are willing to take the risk. How can we mitigate the consequences of you disappearing in the middle to the process? simple: we need to make sure anyone could finish your work if you disappear.

I won’t put a price on your time, ask for £60,000 if you want, split it however you want, I don’t care, but if we’re going to take the risk, we need to make sure anyone could finish your work if you vanish, first, and second, if you do your job we must compensate you properly in a fair way for both sides.

---

### Post by @davidtavarez ⭐ (2021-08-11)
*Post #17*

Look at the PIBD work, we ended up without neither an implementation nor a RFC nor even a work-in-progress Pull Request. In advance or not, for me that is irrelevant if we can’t find a way to get this thing, or anything else, done. It is not hard to understand. Do we want to be in the same position again where we are left with nothing? I think we don’t.

I don’t want to be an obstacle here, I want to find a win-win situation for [@scilio](/u/scilio) and for the Community.

---

### Post by @davidtavarez ⭐ (2021-08-11)
*Post #20*

oryhp:

> people need money

Yes, but not only need, people want money and that is totally fine, and like I said:

davidtavarez:

> I won’t put a price on your time, ask for £60,000 if you want, split it however you want, I don’t care

oryhp:

> Shit happens, and someone will have to continue the implementation.

Exactly, that’s my point and I want anyone to be able to continue the implementation if something bad happens. For the PIBD work we spent donations on that, today we don’t have neither the funds or a single RFC, no one will be able to finish that work. I’m not sorry for not wanting to be in the position of not being able to complete the job.

oryhp:

> No person should have to do this, nor do I think we should encourage them to

I think this is something else, but we don’t want to encourage one-time contributors either. It is completely unhealthy for Grin to rely on sporadic contributions, but if we’re going to take that path, which I’m against of, because life is a joke, we must make sure the code can be maintained and upgraded, not just by the authors but by anyone at any moment in the Community.

Grin is a decentralized open-source project, what we do want is to compensate passionate contributors. I don’t mind if someone sees an one-time opportunity to make money contributing to Grin, that is totally fine. Now, donations spent on unfinished work, donations that are not going into people’s pockets who truly care about Grin. If we’re going to take the risk of having unfinished work, at least, we need to make sure that those donations are not wasted.

Let’s put it like this: let’s say we allocate £50k to this project, or £60k or £80k (again, I don’t care), and for whatever reason (legit or not it doesn’t matter) [@scilio](/u/scilio) has to stop working on this at the 3rd month, what I think we want is to compensate him/her for the work done, and at the same time, we can leave the offer open for anyone to finish the work with the budget left.

---

### Post by @davidtavarez ⭐ (2021-08-13)
*Post #27*

What I like about C++ is that you can easily compile the code to a bunch of platform, as we are doing with Grin++, you can run Grin++ on Android, Pi4, Linux, Windows and macOS; I don’t how to achieve that using Go or Rust, but I don’t think is that easy as it is with C++.

As long as [@scilio](/u/scilio) includes Tests, like he/she said which is perfect, we’re good. A tests coverage of 90% should be good. With a unit testing mindset at the moment of writing the code, the functions and methods can be audit independently and anyone could perform a [Fuzz testing](https://owasp.org/www-community/Fuzzing).

---

### Post by @tromp ⭐ (2021-08-31)
*Post #34*

> The [commitment signature](https://forum.grin.mw/t/comsig-signature-for-mimblewimble-non-interactive-transaction/6976) of the message "MWIXNET",

It may be wise to have the message additionally commit to the date of the coinswap (and for an hourly swap service, the hour of day as well).

>
>                "description": "The excess scalar encrypted using label \"excess\" ",
>

Why does this field need to be separately encrypted? And what does encryption using a label mean?

>
>                "description": "The range proof encrypted using label \"rangeproof\" (only required for the final round)",
>

Since the rangeproof is only required for the final node, I don’t think it belongs in the per-round data.

Does the json array type for rounds make sense when its elements will be at different nesting levels in the onion encryption?

---

### Post by @tromp ⭐ (2021-09-01)
*Post #38*

oryhp:

> Do we know if [ComSig Signature for Mimblewimble Non-Interactive Transaction ](https://forum.grin.mw/t/comsig-signature-for-mimblewimble-non-interactive-transaction/6976) is secure?

It is honest verifier zero knowledge in the same way that Schnorr sigs are. A simulator can pick e, u, v at random and produce a valid transcript with R = u*G+v*H-e*C.

Interestingly, a regular Schnorr signature is a Commitment signature with v=0.

oryhp:

> Not sure if it is simpler

Clearly, (generalized) Schnorr sigs are WAY simpler than bulletproofs. What you mean is “more commonly used” rather than “simpler”. BPs are also an order of magnitude larger, although that has a much smaller impact on the entire coinswap submission which already contains a BP along with many other data items.

I say we go with the simpler and more efficient commitment proof of knowledge and get someone like Andrew Poelstra to bless it.

---



## Funding request should be at least paid XX% in Grin, we need your opinion!
*Date: 2021-08-17 | [Forum Link](https://forum.grin.mw/t/funding-request-should-be-at-least-paid-xx-in-grin-we-need-your-opinion/9181)*
*Importance Score: 99.1 | Core Participants: davidtavarez*

### Post by @Anynomous (2021-08-17)
*Post #1*

Dear all, since we think Grin is a great project ready to grow its economy (grinconomy), we plan to at least pay Funding Request for XX percentage in Grin. We discussed this during the Grin Community council meeting of 17-08- 2021 and got a lot of positive feedback.

We should however also be realistic, not only think from what we as community members would like to see now but also from the developers perspective what developers would find ‘the sweet spot’ in earning Grin and as such getting stake in the project without being forced to exchange all their earnings for a living, which might result in losses if the liquidity is to low. The percentage we ask you to vote on is a start and will most likely increase over time as the liquidity of Grin grows together with its economy.

Whether you are a community member of developer, please think what you think would be a reasonable percentage for all involved parties. Below the voting you can elaborate and discuss why
Bounties are a separate topic and could for example be 100% in Grin.

Funding Requests should be paid at least XX% in Grin (please vote by liking the option(s) below):

---

### Post by @Anynomous (2021-08-18)
*Post #14*

oryhp:

> I think we should encourage, but not require. Grin is extremely volatile and will continue to be for years. There are also different laws/regulations around cryptocurrencies depending where you live. I’d prefer if we are inclusive of all options, but, I too would encourage people to pick a percentage of Grin if they were up for it.

I agree with your reasoning which I know is shared by many. I also do not like ‘forcing people’, I think many will chose to be paid a certain percentage in Grin anyway if encouraged.
At the same time, I do think a small percentage would increase the feeling of stake/ownership/belonging to the Grin project. What I learned from other communities like the Verus and Komodo community is that they thrive in activity and feeling of belonging by dispersing their coin throughout its ecosystem to both to developers and community members. We can learn from these projects.

Therefore I voted for 10% obligatory payment in Grin, since if a developer cannot accept such a small percentage of Grin, it simply means he/she has zero trust in the project and maybe is not the right developer for the project.

An alternative would be to set a default percentage to be paid in Grin but give developers the freedom to chose any other amount - so make it default, but not obligatory. In such as case I would prefer that the default percentage would not be to big, so developers can voluntarily chose a higher amount, which might be better to get their involvement than forcing it upon them .

---

### Post by @vegycslol (2021-08-18)
*Post #15*

Anynomous:

> Therefore I voted for 10% obligatory payment in Grin, since if a developer cannot accept such a small percentage of Grin, it simply means he/she has zero trust in the project and maybe is not the right developer for the project.

I don’t believe grin’s price will go up until inflation rate lowers vastly (sov is usually the first use case for cryptocurrencies, it might happen that grin will be different because inflation rate reduces more slowly). So if the paid dev thinks the same as me it makes sense to sell grin he gets to buy more of it later, even if he thinks grin is a great project. I would give devs an option, especially until we have liquidity so he can dump his grin without loss (which isn’t the case now afaik)

---

### Post by @oryhp (2021-08-18)
*Post #21*

Everyone is simplifying things by reasoning from their own situation. Contracting to be paid for Grin isn’t necessarily the same as fiat or Bitcoin. It depends on the country, laws etc. Forcing these things on people is basically reducing the pool of potential candidates that might believe in Grin, but don’t want to take legal or other risks. This doesn’t mean they don’t believe in the project, far from it.

Currently Grin has big liquidity issues. If you want to sell a lot of Grin, you might need to do it via multiple orders to avoid losing money, maybe even days apart because the order book is so shallow. This could bring a different tax to your crypto holdings because of random rules like `if orders_in_last_year > N or order_place_days > M` you become considered a trader. And based on this you could get taxed 25% or 0%. I’m not making this up, these rules exist in some countries and people want to minimize the two variables. In some cases it could probably bring legal issues to the table as well. Being paid in Bitcoin or Grin can be a completely different experience.

I’d like to add that we can’t solve the problems of liquidity by forcing _others_ to transact in Grin. It should come from the community without a force applied on the community members. It should be natural and by those that want and know why they want to transact.

---

### Post by @Anynomous (2021-08-18)
*Post #23*

Cekic:

> where the idea comes from that 1 or 2 Grin devs will be paid a couple thousands Grin and Grin liquidity will deepen?) Thats absurd man.
>  Point is , its a symbol and dedication to Grin project .
>  And legal ,tax issiues are for devs problems , it is funny if a devs paid with Grin and commit to crime, we will be responsible?

Yes and no.
For example, in the Netherlands you cannot (prohibited by law) to deposit Grin, you can only buy and sell at the exchange but not withdraw or deposit.
That is a real issue that we should take into consideration, we do not want to force a problem on devs.
At the same time, if it is a small %, it should not be a problem much to Devs, they can see it as investment and commitment like you said, but they will not need it for their daily living.
And indeed if you never start an economy, it will not appear out of thing air, changes should be coached gently by implementing incremental changes such as these (paying partly in Grin), followed by natural growth. Extremes should be avoided, like not using Grin at all, or paying 100% in Grin.

…As I said earlier, both points are really valid and should be taken into account. Multiple truths can exist at the same time.

---

### Post by @davidtavarez ⭐ (2021-08-18)
*Post #25*

I think we are missing the point here… the topic isn’t about discussing Grin’s inflation or liquidity. Since when it is our problem to solve Grin’s liquidity issue? I don’t get it. It is extremely hard to have a conversation when people seems to be more focused on being the smart one rather than solving anything.

First, **we don’t want to create a problem for contributors**. Second, 10% seems to be a good amount to start.

And yes, good luck selling a product you don’t think is worth buying .

---

### Post by @davidtavarez ⭐ (2021-08-18)
*Post #27*

oryhp:

> It’s easy to see this makes no sense because the value of 1 Grin clearly isn’t worth putting contractors in such a position. But at which point is it? The lower the value, the worse it is. The higher the value, the more we force an asset they might want to sell for whatever reason - and all other possible issues I mentioned above.

There is a simple solution for all the hypothetical cases mentioned here: **to talk**. I think Grin should be as neutral as Bitcoin (as [@Cobragrin](/u/cobragrin) said). At the end, if a potential contributor has an issue with receiving x% of grins, they just need to talk and that’s all, done, problem solved.

I think we are sending a wrong message by not inviting people to hold (not hodl) grins. We already have [Slatepacks.com](https://slatepacks.com/) to exchange grins for products/services, we probably want to support those kind of initiatives more.

I think it worth trying to give it a try, I don’t believe that someone will say: “I won’t contribute to Grin because they suggest to accept 10% of the donations in grin, I know I can decline the offer, but still I don’t want to decline, I will just not contribute”.

If we get at some point with no liquidity at all we already doomed anyways, but again, we can just suspend the policy at that moment.

---

### Post by @davidtavarez ⭐ (2021-08-18)
*Post #32*

Cekic:

> Why you are explaining your voting and trying to influence others [@oryhp](/u/oryhp)

This is totally OK, [@oryhp](/u/oryhp) (and everybody) has the freedom of expressing his mind. There is no need to silence anyone. It is fine to disagree.

vegycslol:

> Liquidity is important,

Who said it is not a problem?

It seems totally ridiculous to me that a cryptocurrency project does not support its own currency or its ecosystem.

---



## Grinpost, spreading the Grin ツ word
*Date: 2021-09-28 | [Forum Link](https://forum.grin.mw/t/grinpost-spreading-the-grin-word/9251)*
*Importance Score: 119.7 | Core Participants: tromp, davidtavarez*

### Post by @Cobragrin (2021-09-28)
*Post #1*

Hello ,i am trying to spread Grin and its features ,which you know fundamentals at social media twitter,reddit. But i am the only 1 person , Grin devs code ,but Grin community stalled so much lately,due to exchange problems , price decrease. But in my opinion we wont be able to cure it if we sit on our ass.This is an internet currency. We need user base and a wide ecosystem.

So Grin needs to be distributed not only with coin but with the words and get a user base. Lately there is many developments going on about Governance and Technicals. i wrote 3 rd post ,you can take the any part and write some idea,mention at twitter and other channels PLEASE.

Apologies if i didnt mention,forgotten some names or made a mistake ,feel free to reach me… for some reasons i didnt on purpose mention the NAMES ,who worked,contributed before build the most of Grin -as you can understood what i mean MimbleWimble spell

if any other ideas,about sharing meme,gifs,news spreading the word,please comment.
Please share the news. Thank you all. ツ

[twitter.com](https://twitter.com/MW_Grin/status/1442973865064370179)

#### [Grin 😶 POST ツ](https://twitter.com/MW_Grin/status/1442973865064370179)

[@MW_Grin](https://twitter.com/MW_Grin/status/1442973865064370179)

$Grin MimbleWimble a more DECENTRALİSED way..[#Grincoin](https://twitter.com/search?q=%23Grincoin) ツ [#cryptocurrency](https://twitter.com/search?q=%23cryptocurrency) [grinpost.medium.com/gri%CC%87n-a-m…](https://grinpost.medium.com/gri%CC%87n-a-more-decentrali%CC%87zed-way-next-chapter-9ee7049ebab9)

[10:05 PM - 28 Sep 2021](https://twitter.com/MW_Grin/status/1442973865064370179) 32  5

---

### Post by @Cobragrin (2021-12-05)
*Post #4*

[twitter.com](https://twitter.com/MW_Grin/status/1467505556080451590)

#### [Grin POST ツ](https://twitter.com/MW_Grin/status/1467505556080451590)

[@MW_Grin](https://twitter.com/MW_Grin/status/1467505556080451590)

$Grin a #MimbleWimble ⚙️ Machine https://t.co/gZt0U9SbAe @grin_privacy @iPolloGlobal @NHASH_mining

[6:46 AM - 5 Dec 2021](https://twitter.com/MW_Grin/status/1467505556080451590) 1

---

### Post by @Cobragrin (2022-04-02)
*Post #6*

GRINPost _Late March_ 2022

[grinpost.substack.com](https://grinpost.substack.com/p/grin-100-million-designed-for-the)

### [GRIN 100 Million-Designed for the Decades...](https://grinpost.substack.com/p/grin-100-million-designed-for-the)

GRINPOST #Late MARCH

---

### Post by @Cobragrin (2022-04-11)
*Post #7*

A more edited version of Igno Peverell interview, _highlights_ about GRIN ethos.

‘**'When Grin grows, we can all grow with it**.’’

IGNO

[Medium – 9 Apr 22](https://grinpost.medium.com/grin-recollections-f8aa9507dbc1 "01:08PM - 09 April 2022")

### [GRIN recollections.](https://grinpost.medium.com/grin-recollections-f8aa9507dbc1)

IGNOTUS PEVERELL interview Highlights after Grin Launch.

Reading time: 6 min read

---

### Post by @davidtavarez ⭐ (2022-11-18)
*Post #28*

oryhp:

> I think “PIBD Activated!” is a bit misleading because only the RFC transitioned to `Active` state. The nodes don’t sync with PIBD on the network and won’t for some time.

I second that

Also, I don’t think it is very accurate to say this: “shortens the amount of time required to bootstrap nodes”. PIBD definitely increases endurance, but the expectation of making things faster I’m not 100% sure because the same amount of data must be offloaded. If your node is stuck with slow and/or unresponsive nodes the syncing process will be slow. In the long term, when most nodes enable support for PIBD the synchronization will require less time, but in the meantime I think we should avoid creating a false expectation. IMO.

---

### Post by @tromp ⭐ (2022-11-18)
*Post #30*

davidtavarez:

> the same amount of data must be offloaded

But formerly it all had to be downloaded serially, whereas now at can be done in parallel from many peers.

---

### Post by @davidtavarez ⭐ (2022-11-18)
*Post #31*

tromp:

> But formerly it all had to be downloaded serially, whereas now at can be done in parallel from many peers.

Yes, but what I contend is that by rolling out v5.2.1 on June 1, 2023 things won’t be any faster the moment after. I think it’s important for the Community to know that it will take time before users start to notice a significant increase in speed.

What I want to avoid are unfounded complaints in the future based on false expectations. I think it’s important to set the right expectation, as we try to do with many other things. Just that.

---

### Post by @davidtavarez ⭐ (2022-11-18)
*Post #33*

Cekic:

> it is taken from [RFC ](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0020-pibd-messages.md).

Yes, but we have to be more critical and careful with what is written in the newsletter. It is important for Grin to prevent people from reading the newsletter and, based on what is written, starting to form wrong opinions.

---



## Grin Pool Centralization Over 80%
*Date: 2021-10-16 | [Forum Link](https://forum.grin.mw/t/grin-pool-centralization-over-80/9274)*
*Importance Score: 89.3 | Core Participants: davidtavarez*

### Post by @minexpert (2021-10-16)
*Post #1*

By this time, the largest Grin mining pool was GoblinPool.
The founder of the pool Xiao Jay is the creator of the Niffler wallet.
Since most of the miners are in China, over 80% hashrate was on the Goblin Pool so far.
It was a big problem but everyone ignored it. Xiao Jay tried to prevent this by increasing the pool commission to 2.5%, but was unsuccessful.
Now, Goblin Pool is closing due to legal regulations in China.
And we are moving towards centralization again.
Because, in the last 12 hours, miners started redirecting to the always.vip pool, which has another Chinese server.
No miners are switching to grinmint or 2miners.
Source: [Grin (GRIN) Cuckatoo32 | Mining Pools](https://miningpoolstats.stream/grin)

Miners should know that they are making this coin dangerous, which they earn money.
You should know that if grin has 51% attack, all your mining devices, all your dreams will be rubbish.
Even if the pool creator won’t do it, someone can do who hacking access to the pool server.

So now we have to resolve this issue.
Dividing miners as 33%-33%-33% into always.vip, grinmint and 2miners is currently the most useful solution.
This three pools have Asia server.
Always.vip and 2miners have 1% commission. Grinmint has %2.5 comission.
It would be fair for Grinmint to switch to 1% commission for decentralization.
I recommend that all pool founders hold a meeting and for this, the three pool founders can post a joint statement on the pool homepage.
[@mcm-mike](/u/mcm-mike) [@xiaojay](/u/xiaojay) [@tromp](/u/tromp) [@david](/u/david) [@davidtavarez](/u/davidtavarez)

---

### Post by @davidtavarez ⭐ (2021-10-16)
*Post #2*

minexpert:

> I recommend that all pool founders hold a meeting and for this, the three pool founders can post a joint statement on the pool homepage.

This sounds good. I also recommend a short compilation of the URLs and ports since all of them offer servers in Asia:

always.vip

[always.vip1186×112 5.01 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/ff41a3c951c18bdf14f35073bdb17f111beeb5f1.png "always.vip")

2miners

[2miners1276×284 18.6 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3eb78dee6ed6ded6c6ee1c7498944cda3ecd9547.png "2miners")

grinmint

[grinmint918×103 6.15 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7e51b749c4188bb7d297676dc59bf2a4f003e620.png "grinmint")

herominers

woolypooly

We could use the [CC github](https://github.com/grincc/docs) repo to post a short document about it. I will start writing this now.

minexpert:

> Always.vip and 2miners have 1% commission. Grinmint has %2.5 comission.
>  It would be fair for Grinmint to switch to 1% commission for decentralization.

I’m not sure about reducing the comission. I undertand the point, however this will depend on what is best for each pool, last time we checked, costs were a bit high.

These are the current mining fee % for grin (12.10.2021)

|**Pool url** |Pool fee|
| — | — | — |
|[goblinpool.com](https://goblinpool.com/)|2.5 %|
|[always.vip](http://pool.always.vip/)|1 %|
|[2miners](https://grin.2miners.com/)|1 %|
|[2miners-Solo](https://solo-grin.2miners.com/)|1.5 %|
|[grinmint.com](https://grinmint.com/)|2.5 %|
|[herominers.com](https://grin.herominers.com/)|0.9 %|
|[woolypooly.com](https://woolypooly.com/coin/grin)|0.9 %|

---

### Post by @davidtavarez ⭐ (2021-10-16)
*Post #5*

xiaojay:

> Because tor is forbidden in china, so it is hard for chinese user to deposit grin to [gate.io ](http://gate.io), which is the biggest grin exchange.

by this you mean, let the miner to set the “memo”? which is not possible by using grinmint for example, correct?

---

### Post by @mcm-mike (2021-10-16)
*Post #8*

**I am available for a short meeting with mining-pool owners / operators.**

* Can someone please send me some details about the process for `gate.io` to deposit/withdraw GRIN in order for us to understand what we should implement.

Still unsure why Chinese GRIN users not using [TradeOgre](https://tradeogre.com/exchange/BTC-GRIN) **GRIN/BTC** which is an Exchange who supports GRIN since I can remember being a part of GRIN.

Also if you start using TreadeOgre, you will notice there is no need for TOR , you can use Slatepacks which is not requiring a TOR connection. It’s like exchanging a text file with the Exchange in order to transfer GRIN.

**Deposit at TradeOgre:**

[ image1894×494 61.4 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c2f419b324ade32bbf2d137676cc344c5b0677bc.png "image")

---

### Post by @davidtavarez ⭐ (2021-10-16)
*Post #9*

DQF:

> Yes, now only always.vip and goblin support this.

The issues is that [Gate.io](http://Gate.io) is using an inconvenient implementation of Slatepack, far from what is defined in our RFCs. I wish we could help [Gate.io](http://Gate.io) somehow if they can reach us in Keybase I’m sure we can find a way to have a more stable implementation. To be honest, [Gate.io](http://Gate.io) is causing a lot of confusion.

mcm-mike:

> Can someone please send me some details about the process for `gate.io` to deposit/withdraw GRIN in order for us to understand what we should implement.

[@mcm-mike](/u/mcm-mike) taken from <https://www.gate.io/article/19663:>

Gate.io has completed the GRIN wallet upgrading and added support for Slatepack addresses. The obsoleted URL addresses will not be supported any longer. This upgrading brings some major changes:
1) Slatepack address will be used for depositing GRIN. The Memo displaying on your deposit page is exactly the decimal part of the amount you should deposit. For any amount you want to deposit, the decimal part must match the memo exactly, while the whole number part can be of any number. For example, if the Memo for your GRIN deposit page is 722413, then you can deposit 1.722413, 2.722413, 10.722413 , 100.722413, etc.
2. Slatepack address will be used for withdrawing GRIN. The URL address is not supported any longer.

xiaojay:

> Because tor is forbidden in china, so it is hard for chinese user to deposit grin to [gate.io ](http://gate.io), which is the biggest grin exchange.

Is there any special reason why miners from China are not using TradeOgre? The process seems to be clear and simple:

[ ](https://www.youtube.com/watch?v=G9TaVXFrqKI)

With grinmint miners can also use slatepack messages too. They don’t need Tor.

---

### Post by @davidtavarez ⭐ (2021-10-17)
*Post #12*

Let me know if I get the problem right.

Miners are using the pool that lets them send the rewards to [Gate.io](http://Gate.io) because they can set the memo. Interesting… but people can use [Tor Bridges](https://bridges.torproject.org/) to bypass censorship. If this is too much hustle, they can always use slatepack messages to transfer their rewards to their own wallets. Then send the Grins to [Gate.io](http://Gate.io) to their accounts. It seems that this is too much too (?).

minexpert:

> So my idea is to first make the pools available for [gate.io](http://gate.io) by setting memo.

Mmm… but… Is there any guarantee that they will switch pools if another pool lets them to do the same thing with the memo?

---

### Post by @davidtavarez ⭐ (2021-10-20)
*Post #22*

Next CC meeting is on October 26th 2021 we could try to invite them, or we could move the meeting one week to coordinate better.

---

### Post by @davidtavarez ⭐ (2021-11-30)
*Post #73*

DQF:

> 你们应该能弄清楚矿工们为什么来VIP矿池而不去其他矿池，这方面的原因中文社区已经阐明很多次了。
>  You guys should be able to see why miners come to VIP pool not others, the reasons for this have been stated many times By the Chinese community.

Because VIP pool makes thing easier for them to sell the rewards, correct? Am I missing something?

---



## Let's fork GRIN!
*Date: 2021-10-17 | [Forum Link](https://forum.grin.mw/t/lets-fork-grin/9277)*
*Importance Score: 94.0 | Core Participants: tromp, davidtavarez*

### Post by @gringott.one (2021-10-17)
*Post #1*

It will soon be 3 years since GRIN was born, for cryptocurrencies that is a long time to draw certain conclusions about what has been done well and what has probably gone wrong and needs to be fixed before it’s too late.

A lot of people have been inspired by the idea of a new honest and decentralized cryptocurrency. Very compact and scalable blockchain with great privacy features, no premine, no dev fee, no ico, etc. It would seem that what could stop the project from growing.

But something went wrong. If everything is so cool, why are there almost no developers left in the project? There aren’t the best folks left who believed and supported the idea from the beginning and put their soul into the project. They didn’t join in on all the scams that flooded the crypto space, and were always faithful to the idea of a free society with a free economy and money. GRIN was like a breath of fresh air to them. They undoubtedly deserved better treatment and respect. Instead, they were thrown into a bottomless abyss along with the price of GRIN which continues to fall by the day. Many of them have lost their life savings and, most importantly, their time.

In my view, saying that the GRIN is a cash and that it should not be a store of value is pretty stupid. Because cash does not mean that the value must always fall. To me cash is money which is convenient to use in everyday life. GRIN which is constantly losing its value is no better than usd, why bother with it at all, let’s use paper dollars, it has much more privacy than in any cryptocurrency. Any good money should at least retain its value, otherwise it doesn’t make any sense.

GRIN has a constant linear emission with decreasing inflation. The reason is to ensure that the distribution of coins is as decentralized as possible. Is this really the case? It’s no secret that GRIN is mostly traded on just two exchanges, GATE and TO, which makes the circulation of the coin very transparent. So, about 3 months ago one buyer appeared, who started to buy GRIN for about 1000 satoshi, gradually lowering the price level, currently he is buying at 600 satoshi. He brings 2 bitcoins and puts a limit buy order every time a previous order is filled. He also sees no problem with just taking all the liquidity by market price up to 850-1000 satoshi from time to time. By my calculations, he has accumulated at least 6.1 million coins and keeps buying. That’s, for a second, 7% of all supply. Even Satoshi with his 1 million (5.5%) coins and zec with its devs fees look more modest. What kind of decentralization can we talk about? Someone is purposefully monopolizing the coin, and we don’t know the real resources and intentions of this buyer, all capitalization of GRIN at the moment is only 524 BTC. Someone can afford to buy up all of GRIN without a problem. If there is a resource to buy that many coins then there is probably a resource to increase the price and continue manipulations in the future. Pump and Dump scheme is the future of GRIN. It doesn’t make sense for such a player to hold GRIN because of high inflation, but it does make sense to make sharp dumps when interest in the coin will be high. In the end, we never get what we expected initially. We are losing desired decentralization.

Bitcoin turned out to be a strong project because Satoshi was strong not only technically, but also in game theory. A system becomes stable if it reaches a Nash equilibrium [Nash equilibrium - Wikipedia](https://en.wikipedia.org/wiki/Nash_equilibrium). Simply, a Nash equilibrium is the result of a scenario in which everyone wins because everyone achieves the desired outcome.

Bitcoin is a system in which miners and investors get the desired outcome. Investors know that bitcoins are finite, so they are valuable and it makes sense to keep them, miners are interested in them as long as the mining continues and the price covers all costs and makes some profit. That way there is a balance, and the system continues to work quite well. Bitcoin will have problems when the mining stops.

GRIN provides interest for miners, but not enough value for buyers. Yes the emission is time-limited, privacy and scalability are all cool, but the fact that 84,000 new coins is born every day, there is no reason to hold them because tomorrow will be mined another 84000 coins, the plan that inflation will be low in 50 years is certainly beautiful, but let’s face it. There will be thousands of new projects created during that time to compete with GRIN and the chance of winning is negligible, but the chance of dying is increasing every day.

So before it’s too late, I propose to fork GRIN, keeping all the original principles, but changing the monetary policy to protect investors’ interests, add some value to Grin to be able reach Nash equilibrium. GRIN has already begun to lose its decentralization and accumulates in single hands. Yet I believe it’s not too late.

I propose to change emission from 60 coins per minute to 1(ONE) per minute.

Perhaps this transition can be done gradually to keep miners interested. Or just give a few months for the market to evaluate this change.

The second option would be to create another coin that would keep the existing distribution of GRIN, thereby fairly rewarding those who initially believed in the project. This also could be the experimental project for testing new features like coin join or atomic swap first. And who knows, maybe the second project will succeed.

We would get inflation about 2% with a good decentralized distribution of coins which exists at the moment. If this is not done, the coins will concentrate in a single hand, and it would be impossible to resist this.

Let’s add some value for GRIN.

P.S. If someone has other solutions on how to fix GRIN let’s discuss.

---

### Post by @tromp ⭐ (2021-10-17)
*Post #5*

gringott.one:

> By my calculations, he has accumulated at least 6.1 million coins and keeps buying. That’s, for a second, 7% of all supply.

No, that’s 7% of _current_ supply. Which, as you note, is being diluted fast _thanks to_ grin’s high inflation (or slow emission as I would call it).
That makes it only 0.19% of the supply in 100 years.
Now it doesn’t look like Satoshi does it?

gringott.one:

> I propose to change emission from 60 coins per minute to 1(ONE) per minute.

By drastically reducing inflation, you’re making your hypothetical whale own an orders of magnitude larger fraction of the supply in 100 years, and much more like Satoshi.

You’re arguing against yourself.

Btw, that was what Doge’s emission was like. A huge block reward in the first year, and then a 20x smaller block reward for all later years, turning many early adopters into whales.

gringott.one:

> P.S. If someone has other solutions on how to fix GRIN let’s discuss.

Get Elon to tweet about Grin:-)

---

### Post by @davidtavarez ⭐ (2021-10-17)
*Post #6*

gringott.one:

> But something went wrong. If everything is so cool, why are there almost no developers left in the project? There aren’t the best folks left who believed and supported the idea from the beginning and put their soul into the project.

Developers and contributors are real world people with real world problems, they have to pay bills, they probably also have families like everyone else, friends, hobbies, ambitions, etc. When a developer or contributor leaves a project it does not mean anything but that developer found something else to invest their time in, because they are, at the end of the day, **human beings**. This has very little to do with the monetary policy, and a lot to do with human beings trying to figure it out what is best for them.

gringott.one:

> So before it’s too late, I propose to fork GRIN

Cool, go ahead, here’s the repository, it is all open source: [mimblewimble · GitHub](https://github.com/mimblewimble/) it won’t be the first nor the last Grin’s fork anyways.

gringott.one:

> but changing the monetary policy to protect investors’ interests

That mindset is extremely dangerous for a project like Grin. What is in best interest of investors? Simple: profit. There are hundreds of projects where you can get your profit, pick one, like Shiba Inu Coin for example, the internet is full of posts of people making a ton amount of money, then when you make your profit move it to another one, and then to another one, and that’s all. (DISCLAIMER: I’m not a financial advisor).

I’m not saying: f*ck the investors. Are you driven by profit? are you a trader? good for you, that is fine, there is nothing bad about that. I wish I could learn more about trading so I can make profit with the next meme coin

gringott.one:

> P.S. If someone has other solutions on how to fix GRIN let’s discuss.

In summary:

* Improve the user experience by embracing Grin features.
* Build an Ecosystem. Let people build stuff on top of Grin, like POS, Payment Gateways, new forms of sending and receiving, etc.
* Build a strong community.
* Improve miners experiences.

But also, most important, ask Elon to tweet about Grin.

---

### Post by @gringott.one (2021-10-17)
*Post #10*

Guys, you are all right, and I share your thoughts, but we are repeating the same thing for the third year, in the end, besides the cool technology there is nothing left, the work on
the project has almost stopped, there are no buyers either, no one needs a cool coin that is constantly losing value, there are only miners who keep selling. GRIN is almost history, it’s not the present and has no chance for the future unless we change something. I’m just trying to find something that can save the situation.

We had everything, cool developers, everyone wrote about us, lots of articles, everyone supported us. After such a great start, we lost everything. So what led to this situation? Personally for me the answer is obvious: the imbalance of economic interests. And this imbalance is only getting worse. I have nothing against low inflation, but what is the point of waiting 50 years, killing the project with super-high inflation, it is not quite clear?

---

### Post by @davidtavarez ⭐ (2021-10-17)
*Post #14*

gringott.one:

> After such a great start, we lost everything. So what led to this situation?

We are all aware of this, but you are contradicting yourself and mixing too much stuff trying to find a one fix-for-all solution, sadly, that’s not possible. Grin is an open source project, we were able to compensate contributors for their work, and we are still able to do it, did they leave because money? of course not, look at the rates, there were pretty good competent rates. Also, we are still able to do that because of generous donations, what is the economic insentive for those who donated to Grin? Please, I want to know, because I don’t see any. Were those who donated stupid? You will say yes, they were stupid, probably, but I will never do it. They did it because they believe in what Grin is and is meant to be.

Is there a lack of articles about Grin? Yes, so what? Grin is not news worthy, what is the problem with that?

If your argument is that people are not investing in Grin because of the monetary policies, well, you are right, but that is nothing new. Why should we adapt Grin to fit investors’ needs?

I’m more worried about miners, we need to make things easier for them as well for users. They keep the network safe. Now, should I be worried about those who only chase profits wanting to destroy Grin just because they want to make some profits before pivoting onto the next coin? Grin does not need them at all, well… actually… we need them as far as possible.

I’m not arguing against profits, making profits is totally fine. I’m arguing against destroying the fairest, most descentralized, and simplest cryptocurrency project out there.

gringott.one:

> I don’t really understand such a sacrifice for the sake of future generations, they are unlikely to appreciate it, because except us, everyone has already forgotten about the GRIN, and there are no new people to be seen. Honest distribution is when everyone is good and not for those who may be able to live in 100 years. It’s just ridiculous sorry.

Just go to the webiste and you will see:

Electronic transactions for all.
Without censorship or restrictions.

Designed for the decades to come, not just for tomorrow.
To be used by anyone, anywhere.

At this point I’m starting to think that you are trolling here.

---

### Post by @tromp ⭐ (2021-10-18)
*Post #26*

Markozzz:

> and the GRIN will turn into a first-class shit coin.
>
> Something needs to change…
>  For example, reducing the block reward

Messing with the block reward and departing from 1 per second forever is what would make GRIN a shitcoin.

---

### Post by @davidtavarez ⭐ (2021-10-19)
*Post #41*

grn:

> Is there any other example of a crypto project where devs have left, only because of the tone in the community? I think it is much more the lack of near-term growth that gets people to look elsewhere, while an annoying discussion could be the last straw for some. Lack of growth is lack of reward and everyone wants to be rewarded in one way or the other. You’ll need extremely altruistic contributors if the only promise is fairness towards other people at some unspecified time in the future, but typically people ask “what’s in it for me besides of the regular pay?”.

I do not exactly disagree with you on this and I think you brought out good points, but I think you’re missing some details. The Open Source world is full of long/pointless/toxic/ego-centered discussions, this is in fact, very a common thing, toxic as hell but common. I think you are totally right here, people will eventually ask themselves: `what’s in it for me besides of the regular pay?` definitely no one likes to be insulted over and over again. You can receive the perfect salary but you will eventually quit if your work environment is toxic. This is the same everywhere. Now, combine that with a lack of project growth as you mention, the result is simple: total demoralization and loss of motivation. Grin, as a project, had both things in the recent past.

grn:

> Regarding pointless discussions: an issue that I see with the way the project is set up, is that there is no project manager. Contributors have to discuss every little detail with the entire community, which is more emotionally taxing than just having to report to a single entity (who then talks to the community), like in a regular job

The reason why every change should be detailed and openly discussed is because of Grin’s nature. Projects that are being developed by private entities backed by investors are driven by one thing always: make profits through technology. Grin is driven by the technology itself.

I think that there is lack of direction and probably that is what you’re trying to describe [@grn](/u/grn). We haven’t even finished embracing Mimblewimble capabilities. We want to be unique but at the same time we also want to make Grin look and feel like Bitcoin. Exchanges can easily see this and say: “fuck it! let me know when you make up your own mind” and then we put the blame on them but we can’t accept that indeed we are not focused on making things easier but more complicated. Most discussions are about being the one with the biggest brain and less about solving any issue. This is not helping to bring and keep contributors either. Why someone will code or write something to see it die in a Pull Request? I believe this is affecting us more than the monetary policy.

---

### Post by @davidtavarez ⭐ (2022-08-17)
*Post #51*

markov:

> except the most important one: end user experience.

I think it’s simple in terms of user experience as well. I’ve said it before and I’ll say it again, we should stop trying to fit Grin into the Bitcoin box.

---


