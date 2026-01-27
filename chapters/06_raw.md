# Chapter 6: First Hard Fork

*14 topics selected for this chapter*

---

## Grin v2.0.0 Node + Wallet Released
*Date: 2019-07-01 | [Forum Link](https://forum.grin.mw/t/grin-v2-0-0-node-wallet-released/5398)*
*Importance Score: 79.1 | Core Participants: yeastplume, jaspervdm, lehnberg*

### Post by @Yeastplume ⭐ (2019-07-01)
*Post #1*

## Summary

Grin v2.0.0 and Grin-wallet v2.0.0, which include support for the upcoming hard fork, have been released. Changes in these releases have been almost entirely focused on hard fork support and ensuring the entire ecosystem will be running the same version of the transaction-exchange format (the Slate) post-upgrade.

These are required updates for all users, and we recommend everyone take the opportunity to update as soon as possible.

## Overview of Changes

### grin

* Support for Blockheader version 2 (post fork)
* Support for tweaked post-HF secondary proof of work, ‘Cuckarood’
* Support for new Bulletproof rewind scheme
* Version information function added to node API
* Modify stratum-> Wallet communication to use V2 wallet API

### grin-wallet

* Drop support for v0 and v1 Slates, and only use the V2 format.
* Drop support for V1 wallet API. The new V2 API will be maintained going forward, with full documentation [here](https://docs.rs/grin_wallet_api/2.0.0/grin_wallet_api/)
* Drop support for older versions of Grin’s Node API. The wallet must be run against a v2.0.0 or newer Grin node, and will halt activity if the configured node is v1.1.0 or earlier.
* Support for new Bulletproof rewind scheme, which will be applied to all outputs created by v2.0.0.

## Binary downloads and detailed release notes

* Node, `grin`: <https://github.com/mimblewimble/grin/releases/tag/v2.0.0>
* Wallet, `grin-wallet`: <https://github.com/mimblewimble/grin-wallet/releases/tag/v2.0.0>

## Final notice: July hard fork

Please be advised that a breaking upgrade will happen at block height 262,080 and pre-2.0.0 wallets and nodes will stop working at this point. All users will need to upgrade to version 2.0.0 in order to be able to continue using Grin.

## Comparison

Wallet | Compatible with node | Supports sending tx slates | Supports receiving tx slates
---|---|---|---
v1.0.x | v1.0.x or greater | v0/v1 | v0/v1
v1.1.0 | v1.1.0 | v0/v1 (default)
v2 (optional) | v0/v1/v2
v2.0.0 | v2.0.0 | v2 | v2

## Compatibility

Until the time of the hard fork, 2.0.0 wallets are fully compatible with 1.1.0 wallets to send and receive grin, as long as v2 slate version are used to send. These are used by default in v2.0.0. To send a v2 slate using wallet version v1.1.0, include the `-v 2` flag in the send command.

## Contact

For any feedback, questions, concerns, or problems, please contact Daniel Lehnberg:

* Email: [daniel.lehnberg@protonmail.com](mailto:daniel.lehnberg@protonmail.com)
* Keybase: [@lehnberg](http://keybase.io/lehnberg)
* Gitter: [@lehnberg](https://gitter.im/lehnberg)

---

### Post by @UncleWiggly (2019-07-01)
*Post #3*

Would this page be helpful for the above application? <https://wallet.713.mw/install/>. I am waiting for my tech guy to review all of this before I install. --Thanks

---

### Post by @lehnberg ⭐ (2019-07-01)
*Post #4*

[@UncleWiggly](/u/unclewiggly) it will be, we’re hard at work to make sure wallet713 is 2.0.0 compatible at the time of the hard fork

---

### Post by @kargakis (2019-07-01)
*Post #5*

Got my node upgraded, thanks for all the hard work to all!

---

### Post by @SiriusB (2019-07-02)
*Post #6*

Everything’s working great with 2.0. However, none of the miningpools are set (really I can only say this for Grinmint and Bepool - what I use) 3-4 days of mining there with unpaid status from and account accumulating, indicating they haven’t figured out how to send. Hard forks are never easy - hopefully the ecosystem will adapt. If the mining pools aren’t ready, transactions will stop until they can verify again?

---

### Post by @jaspervdm ⭐ (2019-07-02)
*Post #7*

No, the issue is with transaction building, not verification.

---

### Post by @Wiley12 (2019-07-24)
*Post #10*

Hello, how do I go about upgrading my node 1.0.2 to 2.0?

Thanks

---



## Opinions regarding Grin
*Date: 2019-07-22 | [Forum Link](https://forum.grin.mw/t/opinions-regarding-grin/5650)*
*Importance Score: 77.9 | Core Participants: tromp, jaspervdm, joltz*

### Post by @Swizz_beatz (2019-07-22)
*Post #1*

Hi everyone, I’m starting a new thread with the hope of getting community feedback on the issues and challenges facing Grin. Feel free to add your voice here. Keep in mind that this is not in any way just a solely ‘critique’ of Grin. Efforts must be taken to also mention what one feels is good about Grin.

To start things, The good things about Grin:

* Developers must be commended for their hardwork and effort during the past 4 years. It’s almost completely unheard for a team to undertake a massive project such as this. This is a monumental task within itself and what makes this even more amazing is that the team did this with no reliance on co-operations and institutions. This cannot be overstated, must thanks a bunch to the developers for this amazing work which could disrupt an already disruptive technology advancement.

* Recently, the council has begun measures to make the grin technocratic council more inclusive to the community.

Areas for improvement:
1\. Security audit report:
\+ Initial regular updates by Igno in April 2019
\+ Lehnberg on the 7th May 2019 stating that the final report has been received and ‘Conservative estimate for the publication of the audit reports is ~ 4 weeks’.
\+ Igno added a week later: ‘The more severe issues should be in 1.1.0. Then we should have about a month, perhaps 1.1.1 or so, to make sure we’re all good with respect to all those findings’.
\+ Since then, 1.1.0 was released on the 6th of June, and 2.0.0 was released on the 1st of July. During the last 3 (Three) months since, not much was added. Most meetings have simply been posted with ‘no update’ and the only documented action taken was that ‘j01tz’ is tracking the issues. This has raised suspicion that the Grin council is hiding something from the community. I am not saying something sinister is happening, but this has alarm bells ringing everywhere.

Lets just hope that J01tz stays true to his comment on the 16th July 2019 ‘I expect this to wrap up in the next week or so (assuming hardfork is calm) so that we can complete the verification process. My goal by the next meeting is to have all fixes verified by coinspect and have target dates set for blog post/pr stuff’

2. POW & ASIC changes: On the 26th June 2019, Tromp wrote the following: ‘Let’s start with our commitment to ASIC mfg: In our original commitment we committed to not make changes to primary pow “in the foreseeable future”. I want to make that more concrete now, specifically, that we commit to not making changes that take effect in less than 18 months. This gives ASIC mfg more confidence to invest in ASIC development.’ Since then, the grin team has given out conflicting information, stating a 6 monthly hardfork for the next 18 months specifically to keep ASICs at bay. Maybe I’m missing something here, but I’d appreciate it, if a member of the community can clarify this.

3. What exactly are Layer1 contributing to the field, because, as far as the community is aware, they have not contributed anything. Questions about external involvement where raised on the gitter chat, but this was immediately shut down by the Grin council.

4. What thought has Grin given towards grin being more adopted and used. With Grin forks coming out right, left and center (MWcoin/Bitgrin/EPIC), the community is concerned that at current pace, and lack of any discussion to satisfy adoption, these copy cats might one day surpass Grin. If there is one thing for sure, these copies lack any development skills but will aggressively market their project. Should they even get one major listing, they will easily surpass Grin and use those funds to hire more developers that could render Grin insignificant in the future.

Recommendations:

* Stay awesome
* Prior to undertaking additional tasks including the RFC, maybe focus on getting some of the issues that have been outstanding for months out of the way first
* Avoid complacency, competition is developing and make no mistake about it, they have clearly marked and are targeting Grin is an enemy. It would be foolish for Grin to remain in wonderland and dismiss these threats even now
* Aim towards increasing the community. Poloniex has offered 50% or so of their Grin transaction fees (approx 5 btc donated since Feb). Grin could take on more listings which would not only increase adoption but also potentially lead to hundreds of BTC that can be allocated towards Grin development (should exchanges contribute a percentage of their fee towards Grin development).

---

### Post by @jaspervdm ⭐ (2019-07-22)
*Post #2*

> Since then, the grin team has given out conflicting information, stating a 6 monthly hardfork for the next 18 months specifically to keep ASICs at bay.

To my knowledge, there is no conflicting information. If you think there is, please provide quotes/sources and we can resolve them. The 4 hard forks have been planned since before mainnet launch. Those forks will be used to introduce consensus-changing improvements, as well as changes in the secondary PoW

> What exactly are Layer1 contributing to the field, because, as far as the community is aware, they have not contributed anything.

I have never heard this concern before. Have you asked Layer1 directly what they are contributing?

> With Grin forks coming out right, left and center (MWcoin/Bitgrin/EPIC), the community is concerned that at current pace, and lack of any discussion to satisfy adoption, these copy cats might one day surpass Grin.

Grin _is_ the community. Or at least that is what it aims for. So if you think the project needs to do certain things or needs to start certain discussions, you are more than welcome to start on them.

---

### Post by @jaspervdm ⭐ (2019-07-22)
*Post #7*

Maybe I am misunderstanding you, but I don’t see any conflicting information here. The commitment relates to the primary PoW (ASIC friendly), the hard forks will introduce changes to the secondary PoW (ASIC resistant).

> I have just done so with starting this thread, obviously

Alright, but “how to increase Grin adoption” seems like a pretty big topic which might deserve its own thread, it might get snowed under here.

> I’d be very interested to hear your opinions about the security audit

I don’t have anything interesting to say about it. Most devs working on the project were focussed on the hard fork. Now that that is over, things are moving forward with the audit report but I don’t have an ETA or anything like that to announce

---

### Post by @joltz ⭐ (2019-07-22)
*Post #11*

Hi [@Swizz_beatz](/u/swizz_beatz), thanks for raising those concerns and encouraging the community to engage.

You are correct that the security audit reporting is an area for improvement.

Especially considering that:

* transparency is critical for a project like Grin
* community funds were used
* the results of a security audit can potentially impact users

I’m hoping to add some clarity around security processes for Grin in an RFC <https://github.com/mimblewimble/grin-rfcs/pull/13>

This sets a public disclosure time of a maximum of 90 days which is more reasonable for a project like Grin (note that is for disclosure of single vulnerabilities, not entire audit reports).

I’d also like to point out that well-funded centralized projects can take several months to properly address audit reports. I think it’s pretty neat that a donation-based decentralized project was able to receive an audit of this quality, address the findings and ultimately share it with the community in a (somewhat) reasonable timeline.

Regarding the last audit, my understanding is that the core team has had it for about two months. This still gives us an opportunity to publish around the 90 day mark (though it depends on time available from the already spread thin core developers and the auditors- if there is one thing I’ve learned in crypto it is to not set hard dates).

The current status of the audit is “pre-remediation verification”. The core team needs to do a final review of the issues and fixes to make sure we are ready for verification from the auditors. I’m sure this will happen soon™. Everyone has been focused on a successful hardfork as [@jaspervdm](/u/jaspervdm) said. This will be discussed again tomorrow at the developer meeting.

From there the status will be “remediation verification” where the auditors will make sure any issues they raised were properly addressed. If a fix wasn’t effective or created another issue, another cycle happens of issue->fix->verify and the public report will be slightly delayed futher. I’ll do my best to communicate this to the community in that case.

Once all raised issues have been verified to be adequately addressed by the auditing team, the public reports will be compiled and jointly released by the Grin community and the auditing team. I’m happy to answer more questions on this process.

Moving forward I hope we can make Grin’s security processes more transparent to address the concerns you raised about the lack of updates and complacency- I think we are on the right track but still have more work to do.

---

### Post by @jaspervdm ⭐ (2019-08-06)
*Post #29*

Could you elaborate, what is in your eyes the problem with the increased hash rate, and what kind of response did you expect to receive in the dev meeting?

---

### Post by @jaspervdm ⭐ (2019-08-06)
*Post #32*

> No one has explained, as far as I know, what happened here.

The hashrate increased, that’s all we know. Grin is permissionless so we don’t know who/what is responsible. I don’t know what more you expect of us.

> If there is a serious flaw / issue it should be communicated to the community.

If you have evidence of a flaw / issue, please provide it. Otherwise I think we should apply Occam’s razor

---

### Post by @jaspervdm ⭐ (2019-08-06)
*Post #34*

One of the recent things that come to mind is the creation of subteams

---

### Post by @jaspervdm ⭐ (2019-08-06)
*Post #49*

If you think “trying to get the masses to mine grin” is a worthwhile cause, feel free to devote your time to it

---



## How To Increase Grin Adoption
*Date: 2019-07-25 | [Forum Link](https://forum.grin.mw/t/how-to-increase-grin-adoption/5672)*
*Importance Score: 113.9 | Core Participants: david, tromp*

### Post by @Yawser (2019-07-25)
*Post #1*

[Opinions regarding Grin](https://forum.grin.mw/t/opinions-regarding-grin/5650/7)

> Alright, but “how to increase Grin adoption” seems like a pretty big topic which might deserve its own thread, it might get snowed under here.

I have been following Grin now for a few months. It has astonished me how it towers above other cryptocurrencies. It is by far the new paradigm for privacy coins. The only videos and articles I have read have been pitched at an enthusiast crowd. I have wondered why this coin does not have a marketing team / volunteers. When I asked about it in Gitter, I have been told to do it myself.

I am not trained in marketing but there may be people in the community who are.

What I can do is link any good sources I find to this topic. If anyone finds a way for marketing Grin or sites or users doing so, please post here.

Also post here if you need support for a social media post. We can an army of clicks for worthy posts.

---

### Post by @Yawser (2019-07-25)
*Post #3*

[Opinions regarding Grin](https://forum.grin.mw/t/opinions-regarding-grin/5650/15)

> A few quality of life improvement/suggestions from the non-techie user.
>
>   1. An “official” GUI wallet would be nice. Or at least a wallet recommended or vetted by the council that has some GUI interface on it. Most non-techies don’t really want/like to deal with CLI. BEAM has a pretty nice GUI wallet. I really enjoy using that one over the GRIN CLI wallet.
>   2. Ledger support of some kind would be nice. Lots of people have Ledgers and having some support on it might increase adoption. I know of at least a handful of people who would like to put GRIN on their Ledger devices but it isn’t supported. Might make people feel safer about where they stash their GRIN.
>   3. Some effort to increase liquidity would be nice. Only a handful of exchanges support GRIN.
>  Some day it would be nice where every merchant takes GRIN as payment but until that day comes, it would be nice to have some way to make moving/converting/buying/selling GRIN easier. I don’t know if the solution is more outreach to exchanges or working with more merchants to accept GRIN but it would be nice to have GRIN be more liquid. Liquidity would help get GRIN into the hands of more people and increase adoption/awareness.
>

>
> These are just one non-developer’s suggestions.

Thank you [@grinn](/u/grinn) will get on with this. Need people to post here. We need to get in the habit of liking and sharing social media posts that are positive towards grin. Also if there are any misleading posts we need to address them.

---

### Post by @ken19983 (2019-07-26)
*Post #5*

1A. I would actually add to #1 beyond just having GRIN vet or offer their own GUI wallet. It would be pretty nice to have 3rd party wallets that support other cryptocurrencies to also offer support for GRIN. For example, JAXX is a fairly popular wallet and offers support for a large number of cryptocurrencies. Many people use this wallet and feel comfortable or are familiar with it. Being able to put my GRIN in my [Jaxx.io](http://Jaxx.io) wallet would be pretty convenient rather than having to download/manage/install yet another wallet. There are a number of popular wallets out there that store various cryptocurrencies. Getting GRIN on some of the more popular ones would be helpful.

2A. Similar to 1A, Ledger is just one (popular) hardware wallet out there. Having hardware wallet support would help increase adoption of GRIN. Little things like “A safe, convenient way to store your GRIN” will go a long way to increase adoption.

---

### Post by @Neo (2019-07-26)
*Post #9*

Would be good if grin was supported on BTCpay server, it’s arguably the best open source payment processor.

[btcpayserver.org](https://btcpayserver.org/)

### [BTCPay Server](https://btcpayserver.org/)

BTCPay Server is a self-hosted, open-source cryptocurrency payment processor. It's secure, private, censorship-resistant and free.

However, this probably requires non-interactive txs

[github.com](https://github.com/btcpayserver/btcpayserver-doc/blob/master/Altcoins.md)

#### [btcpayserver/btcpayserver-doc/blob/master/Altcoins.md](https://github.com/btcpayserver/btcpayserver-doc/blob/master/Altcoins.md)

# Altcoins

Bitcoin is the only focus of the project and its core developers. However, opt-in integrations are available for several altcoins:

- BGold (BTG) (also known as Bitcoin Gold)
- BPlus (XBC) (also known as Bitcoin Plus)
- Bitcore (BTX)
- Dash (DASH)
- Dogecoin (DOGE)
- Feathercoin (FTC)
- Groestlcoin (GRS)
- Litecoin (LTC)
- Monacoin (MONA)
- Polis (POLIS)
- Viacoin (VIA)

Altcoins are maintained by their respective communities.

For more information, check the [Altcoin FAQ page](FAQ/FAQ-Altcoin.md).

This file has been truncated. [show original](https://github.com/btcpayserver/btcpayserver-doc/blob/master/Altcoins.md)

Would be good if Grin was supported on Coinpayments aswell( Beam is on here)
<https://www.coinpayments.net/coinhosting>

^There is a sizable integration fee listed, but apparently, this is not the case for all.

---

### Post by @Swizz_beatz (2019-08-03)
*Post #45*

That’s why we have this forum. To try and identify issues, raise them up and try to solve them. [@Grin.Fast](/u/grin.fast) did just that and raised a really cool idea. I’m with him 100%. Excited to see the awesome work he’s doing.

imegi:

> thats why i said we need to identify it first ,to reach other markets

Yea I agree, but there is barely any support or momentum on that front (God bless those who want to help [@grinn](/u/grinn), [@Chronos](/u/chronos), [@grindify](/u/grindify) to name a few). Hopefully a few months/year down the line someone will come across these threads and the community would be more willing then.

Seems like we may have another donation campaign coming up too. We are quiet a small community hence reaching the targets is particularly difficult. Haven’t seen any concrete action on trying to increase awareness to remedy this. Appreciate the team, love the idea but unfortunately can no longer donate to the campaign. Grin has cost me a lot of btc in loses and like some developers, I have Swizz_beatlings of my own to care for. I’ll start donating as soon as Grin nets me a +ve return. Out for now

---

### Post by @grindify (2019-08-05)
*Post #59*

Some polarization of opinions seems evident among the posters on this thread (and forum) _vis a vis_ the communications/PR about Grin. Grinners on both sides of that temporary bifurcation have strongly held views. In principle, this is not necessarily bad IMO as it demonstrates passion for the project. Generally, two heads are better than one, and three heads are obviously better than two heads and so by induction, _n_ heads approach optimum head. But this may require a head wrangler - or some level of organization/structure with respect to this topic. The council recently agreed to a scheme such that in essence, key areas of advancement would be compartmentalized and managed through a pretty structured process. So there is an acknowledgement of sorts that some structure is necessary to get things done, rather than being completely guided by natural selection where whoever shouts the loudest/devises the most acerbic insult moves the project forward. By extension, the trolling and discrediting each other’s opinions in a negative manner is probably unhelpful. Disagree, provoke and stimulate discussion but more progress will be made through reasoned, mature debate with a view to achieving consensus about step-wise decisions/issues as they arise.

The Grin project as it stands, doesn’t have some of the advantages of a (typical) investor-funded project – ready cash, generous guaranteed salaries, connections to potential ~~beneficiaries~~ ”committed financiers with a passion for innovation in the space” and an obscene marketing budget … But it has other advantages that those projects do not have – mostly freedom to pursue quality, equity (in the general sense ;), transparency etc. Speaking from 1st hand experience, it is an understatement to say that it can be an incredibly limiting burden to have investors to whom one must answer. Risk capital invested by people with “skin in the game” changes the dynamics utterly. The project you thought you were doing has a whole other set of parameters, metrics and expectations that determine its trajectory, unless you are a proven unicorn and it’s worth remembering, there is a reason for that epithet… So I say that the advantages of the Grin project approach need to be appreciated, embraced and “leveraged” – that just may take a little more time ツ

---

### Post by @tromp ⭐ (2019-08-08)
*Post #71*

PhamKy:

> All other coins except Grin and Bitcoin have a management company

Monero is not managed by a company…

---

### Post by @david ⭐ (2019-12-01)
*Post #118*

The 2,966 members of [t.me/GrinCoin](http://t.me/GrinCoin) would disagree with you.

---



## Grin Poster creation team
*Date: 2019-07-31 | [Forum Link](https://forum.grin.mw/t/grin-poster-creation-team/5727)*
*Importance Score: 66.2 | Core Participants: tromp*

### Post by @Swizz_beatz (2019-07-31)
*Post #1*

Hi everyone, in addition to the video content creation thread started, I thought it might be helpful if we have a poster content creation team that can produce posters which could subsequently be used to spread awareness of Grin.

The objective is to produce posters which:

* Describe Grin and all the fundamentals and innovations present
* A poster focusing on sticky points that are commonly mis-interpreted. E.g Grin’s emission rate
* A poster focusing on the shared history of bitcoin and Grin. E.g. How Grin aims to create an electronic peer to peer system
* A poster focusing on how to use Grin. This should include all of Grin’s ecosystem projects (Wallets & payment systems)

*** The posters need be simple, informative and help show the great properties of Grin (hats of to the Grin council and developers for giving us plenty of cool things we can talk about). They also need to use the appropriate styling - cyperpunk & cool

It’ll be great if members of this community are willing to help. Any action big or small would be great. One of the simple ways you can help is by:

* Recommendations/ideas for what you feel is crucial to be included in posters
* Creating simple messages which conveys Grins decentralization/privacy/scalability features.

This list is extensive, but if there’s anything you can help with (including those not mentioned above) please chip in.

We don’t expect this project to incur significant costs, but if significant expenses are required & justified we can look towards methods to make it possible.

Disclaimer: Some people are working on getting the news out there along social media channels (twitter/telegram/reddit/etc). Video content creation/propagation/sharing/etc is not within the limits of this thread/project. This thread/project is solely concerned with creating posters that the social media team/ community can use.

---

### Post by @tromp ⭐ (2019-07-31)
*Post #5*

Let’s not compare Grin with ICO coins that create a billion coins out of thin air and sell them for billions of dollars…

My post at <https://www.reddit.com/r/CryptoCurrency/comments/chl5hf/evaluating_launch_coin_distribution_fairness/>
has some ideas for comparing against non-premined coins.

---

### Post by @tromp ⭐ (2019-07-31)
*Post #11*

The number of coins is not that relevant. Grin emits a billion nanogrin every second. IOTA uses MIOTA as a unit, but that is also one million IOTA. Some people similarly propose replacing BTC by mBTC, a milliBTC. It’s all arbitrary scaling. What’s important for fair distribution if everyone had to put in a similar effort in getting a coin. With ICO that’s clearly not the case. The creators can assign themselves arbitrary amounts. Similarly, instamines and dev taxes detract from fair distribution.

---

### Post by @MerlinsBeard (2019-08-02)
*Post #15*

Inspired by [@Neo](/u/neo)’s poster:

[ grin_poster.png1920×1080 101 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/78eb1afb5ae5ae629cbc3a4b4254a9d239e27d21.png "grin_poster.png")

[ grin_poster_2.png1920×1080 219 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/eb1d94fe16789b20527bcb7d589ba027f5752314.png "grin_poster_2.png")

---

### Post by @Grumpy (2019-08-02)
*Post #19*

Here is my submission.

[ Screen Shot 2019-08-02 at 12.07.33 AM.jpg1426×1424 243 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3cb1ea0decdf2cb4e7f9b207c9c3e0dd5dfbd5cc.jpeg "Screen Shot 2019-08-02 at 12.07.33 AM.jpg")

---

### Post by @Swizz_beatz (2019-08-02)
*Post #25*

Dear Grinners, please do not pay heed to [@Grumpy](/u/grumpy). He enjoys getting a laugh and trolling any positive development by the Grin community. It may be related to his inability to contribute positively or some deeply hidden insecurity issues.

Continue your great work on this project and don’t pay any attention to this troll.

[@Ronaldo](/u/ronaldo), I appreciate your enthusiasm but it appears that your hoping that [@Grumpy](/u/grumpy) gets cancer which is not appropriate. I would just ignore him as opposed to wishing him ill

---

### Post by @MF_Grin (2019-08-04)
*Post #33*

I made this as an alternative Grin logo. The original logo is great, but I think we need a shorthand version which can be easily written down/drawn by anyone like the Bitcoin “B” with the dollar signs through it - used the Grin money symbol so nothing completely new. Not sure if this has been discussed.

[ meet-grin-yellow.png890×536 12.4 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f67d668cf21f8afafca12aee0577c90a9f2b36dd.png "meet-grin-yellow.png")

[ meet-grin-alt.png1000×536 23.2 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a79e0a86deaf2c09c0a339cf1d13f49594eedbd5.png "meet-grin-alt.png")

[ grin-logo-alt.png1000×1000 13.2 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/997a7848d7c01d4a30937790fa173a4689316db3.png "grin-logo-alt.png")

[ grin-white-alt.png1000×1000 12.4 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/bdb684638372f0a03d291e5253ca5e8c2fdbad4a.png "grin-white-alt.png")

---

### Post by @dinhhoangphong (2019-08-09)
*Post #39*

Tks
I designed the size like that as a twitter cover
Grin poster part 2 ^^

[ Grin poster-02.jpg5315×1772 1.65 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c84dc644b9e88429d4efd59a127874856117982e.jpeg "Grin poster-02.jpg")

---



## Grin Icon Branding
*Date: 2019-08-15 | [Forum Link](https://forum.grin.mw/t/grin-icon-branding/5846)*
*Importance Score: 76.2 | Core Participants: tromp, antioch*

### Post by @Tech (2019-08-15)
*Post #1*

Currently, there is a icon on [grin.mw](https://grin.mw) and that many exchanges are using,

i’d like to propose we use this one instead.

I think the one which the joker/amazon.com logo mix looks kind of weird.

---

### Post by @tromp ⭐ (2019-08-15)
*Post #2*

Your version removes the curl on the right of the mouth that makes it “G” shaped. With the eyes already forming letters, it’s only natural that the mouth resembles one too.

---

### Post by @MF_Grin (2019-08-15)
*Post #5*

I made this one

[ grin-man.png700×700 32.3 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6a1130a06383b4cec152e34bf23997633afae1cf.png "grin-man.png")

---

### Post by @tromp ⭐ (2019-08-15)
*Post #8*

Btw, the current logo stems from this Grin Logo thread:

[Grin Logos for Community Consideration](https://forum.grin.mw/t/grin-logos-for-community-consideration/155/91)

> [@Askepios](/u/askepios) [@0xb100d](/u/0xb100d) I made some logo comparisons, see below: [[logoVariations]](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/d3e43f10fe6606ad2764b33ddb68e02c7ba4b01d.png "logoVariations") In general, I think this logo works really well, across board and in many different sizes and variations. Gives us a lot of flexibility. Since we’re talking about merchandise (I’ve been thinking about it as well btw, would both be cool and a nice little source of income for the dev fund!), it might make sense to ensure the yellow is [print friendly](https://www.printninja.com/printing-resource-center/file-setup/offset-printing-guidelines/offset-color-requirements/cmyk-suggested-values) and can be represented in the physical world well. Variation C above …

---

### Post by @brent (2019-09-27)
*Post #10*

Here’s a logo that uses the Japanese character that the community has been using to symbolize grin: ツ

[ grin.png684×676 17.7 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/c/c38673170ef3c2a4dddcbb3fdfa48fee95ea5163.png "grin.png")

---

### Post by @0xb100d (2019-09-27)
*Post #14*

the current grin logo is fantastic and everyone loves it. it attracts exactly the right type of crowd, and is unassuming and a funny mask to hide the serious project behind. It is a perfect bluff.

you don’t want your super private anonymous currency to stand out any more than necessary, it’s just for the people who have a reason to know about it. not for billboards and mcdonalds restaurants. it is specifically for the underground, at least until all the kinks have been worked out.

It is a minimal implementation, essentially just a proof of concept, not meant for wide consumption, and the logo reflects that playful, experimental attitude. It is not a visa or a paypal or an amazon, it is more like a crayola crayon rough draft and only people who are interested in getting their hands dirty drawing would even be interested.

grin doesn’t even need a logo. having even the website we do was a bit of a concession for the people who wanted a shiny homepage, honestly even that is not really appropriate for the type of work that is currently being done on grin. grin needs many more years of being completely unknown and almost entirely unused just like bitcoin had in order to be successful, try to see how that could make sense. actively trying to make grin more popular sooner is extremely counterproductive. We do not want grin to be popular or mainstream. We do not want grin to be popular or mainstream or used very much. We do not want grin to be popular or mainstream or used very much until it is more mature.

bitcoin is not ready for the mainstream, maybe in ten more years. very foolish to think that grin needs to polish up and look professional so it can go mainstream when it’s older brother bitcoin is still decades away from even doing it. trying to push grin to be more than it is is silly and will damage grin and hurt the chances the world will someday have a quality digital cash. If you believe in digital cash you need to be patient. If you want to get rich quick, you need to get out. You missed the bitcoin boat and you will never, ever find an opportunity like it again in a million years. Give up, you are being selfish and trying to bring others down with you. Others who might be extremely sensitive and need digital cash to live. Don’t be selfish.

disclosure ironically blurred: I designed the logo and I could not be more proud to have it used on a such a cool project. grin is underground until it organically is not, lets not try to make it grow up faster than it needs to.

---

### Post by @tromp ⭐ (2019-09-28)
*Post #23*

I’m thinking the MW look of the eyes could be reproduced in an animated version of this one if we show an alternating V and ^ between the eye bars, perhaps in a fainter color or thickness. Just a silly idea…

---

### Post by @antioch ⭐ (2019-10-04)
*Post #45*

We should definitely steal the `BUSINESS NAME - YOUR TAGLINE IS HERE` text.

---



## Grin 💕 and Encouragement
*Date: 2019-08-20 | [Forum Link](https://forum.grin.mw/t/grin-and-encouragement/5900)*
*Importance Score: 257.1 | Core Participants: lehnberg*

### Post by @LovelyGrin (2019-08-20)
*Post #1*

**In this thread we find beautiful creative ways to send love and encourage the charming and diverse community we share.**

---

### Post by @LovelyGrin (2019-08-21)
*Post #5*

The artwork is available on my git for anyone to use .

<https://github.com/lovelygrin/artwork>

---

### Post by @lehnberg ⭐ (2019-08-21)
*Post #6*

Loving this! Would you be up for creating artwork as covers for the [weekly grin newsletters](https://grinnews.substack.com)? Have three here already that I would be happy to use, others (cough cough [@Grumpy](/u/grumpy) cough [@0xb100d](/u/0xb100d)) might want to add to this as well?

---

### Post by @lehnberg ⭐ (2019-09-09)
*Post #34*

Telegram sticker pack created by user @yakamitu: <https://t.me/addstickers/MimbleWimbleGrin>

---

### Post by @lehnberg ⭐ (2020-01-27)
*Post #82*

hello [@LovelyGrin](/u/lovelygrin), you’ve been missed!

---

### Post by @lehnberg ⭐ (2020-07-23)
*Post #90*

Great to see you back again, [@LovelyGrin](/u/lovelygrin)

---



## Below 1$ condition
*Date: 2019-08-22 | [Forum Link](https://forum.grin.mw/t/below-1-condition/5919)*
*Importance Score: 95.6 | Core Participants: tromp, davidtavarez, lehnberg*

### Post by @Alrom (2019-08-22)
*Post #1*

Hi. If the price of the coin falls below $1, I propose to discuss the correctness of the basic hypothesis of the project.
The basic hypothesis is that there will be coin holders, as inflation will be low in the long run.
The risk of confusion: everyone understands that the life of any technology is limited(ICQ is dead, Skype is dying), so no one wants to wait 20 years, taking the risks of high inflation. Just for the reason that when inflation becomes acceptable, the technology will simply become obsolete.

If long-term sellers will be more than buyers, the price will tend to 1 cent. Who will use a coin that has lost 99.99% of its value and continues to lose it?

My hypothesis is that without holders, no coin can survive. The holders compensate the cost of electricity. If no one covers the losses, the project dies.
It is probably impossible to create an analogue of cash in the current environment, as the cost of electricity is too high. I would suggest making the project not cash, but an improved version of bitcoin with limited emission, making a hard fork. In my understanding, a coin with unlimited emission and high inflation is even more experimental than a coin with limited emission, as a coin with limited emission is better consistent with the short life cycle of technology and the psychology of people.

Sorry for terrible English

---

### Post by @Alrom (2019-09-16)
*Post #14*

I would like to know how well the project founders researched cryptocurrency users and their needs? According to my feelings, 90% of users buy cryptocurrency for two reasons: to invest(rich countries) and to save small savings from inflation(poor countries). All these people are betting that the popularity of the project will grow with a limited issue and this will lead to an increase in capitalization. 5% use it on the black market. I think only 5% of users dream of buying coffee for cryptocurrency. 90% of users will not buy GRIN due to high and unlimited inflation.
The success of bitcoin is related to the model: popularity - > more services - > more popularity. This is simple. GRIN’s mistake is that they build a model in a theoretical world without competition and where technology doesn’t evolve. No cryptocurrency will dominate for 30 years, all will become obsolete-the problem is in the architecture of the projects, they are not as flexible. For the same reason, GRIN appeared, which could not be implemented in bitcoin. Creating a project for 500 years ahead with unlimited emissions and high inflation, the creators destroy the most important thing - popularity. There is no problem in the limited issue, there is a problem in technology - when investors begin to consider the project unpromising it leads to sales and a drop in value. I’m not talking about short-term volatility, which will be in any project, I mean the long-term trend. Everyone wants value growth - miners, users, investors. But if the project can not become popular and effectively develop, meet the requirements of the time, it must die. It is foolish to fight against the laws of Economics - BEAM with an ugly financing model already has a larger capitalization than GRIN. I encourage developers to make mass adoption and popularity the main goal of the project. All the best projects will repeat the fate of NOKIA 3310: quality- > popularity - >obsolescence. Don’t kill popularity.

---

### Post by @tromp ⭐ (2019-09-24)
*Post #31*

Plenty examples on [Coin - Wikipedia](https://en.wikipedia.org/wiki/Coin)

---

### Post by @tromp ⭐ (2019-10-19)
*Post #60*

Alrom:

> I am sure that the development team does not invest their savings in this coin

Dead wrong. I put some of my savings into Grin and will continue to do so.
Anybody who wants to directly sell me Grin for Euros please DM me.

---

### Post by @davidtavarez ⭐ (2019-10-19)
*Post #62*

Alrom:

> popularity

You’re wrong, the most important thing is TRUST. Coins loses TRUST while the POPULARITY increase. The most important thing to survive is to be CONSISTENT. For sure it could be (or will be) inflation, but it doesn’t matter while people keep trusting. Grin should focus on gaining TRUST and keeping that trust higher as possible. Grin doesn’t need MASS ADOPTION, Grin does need a SOLID foundation.

---

### Post by @lehnberg ⭐ (2019-10-21)
*Post #72*

[@Alrom](/u/alrom) & [@MerlinsBeard](/u/merlinsbeard) feel free to take the name calling elsewhere. Perhaps get a room / hug it out in the DMs?

I’d like to avoid moderating, but I’m not shy of modding if need be.

---

### Post by @tromp ⭐ (2019-10-22)
*Post #81*

Alrom:

> while getting paid regularly.

I got paid nothing. Neither did many other unpaid developers.

Alrom:

> it takes courage to admit your mistake

It takes courage to try a novel emission, among a sea of thousands of others that blindly subscribe to bitcoin’s “rewards must fall” mantra.
I firmly believe that eventually relying on fees only is the mistake.
I believe that a constant reward makes for a much fairer distribution in the long run, by making it much harder to obtain a large fraction of all coins.

Alrom:

> paying a couple of bucks a day

One day of Grin is worth over 80000 bucks.
Besides, security depends on the ratio between marketcap and daily issuance in dollars, not the latter only. It is bitcoin that becomes more insecure with every halving, as the cost of an attack becomes a smaller and smaller fraction of the total value it is securing.

---

### Post by @tromp ⭐ (2019-10-22)
*Post #87*

The plan is to add a 2nd layer for off-chain transactions, similar to Bitcoin’s lightning network. We don’t have plans for a billion users yet.

---



## Request For Funding, @JRandomCryptographer
*Date: 2019-09-12 | [Forum Link](https://forum.grin.mw/t/request-for-funding-jrandomcryptographer/6056)*
*Importance Score: 104.9 | Core Participants: david, tromp, jaspervdm*

### Post by @david ⭐ (2019-09-12)
*Post #1*

Nearly every other serious cryptocurrency has at least 1, and often several cryptographers working to improve the protocol. With all of the new ZK-systems coming out (Halo, SNARKs, Lelantus, etc), it’s difficult for amateur cryptographers to determine the usefulness and advantages of each system. While Tromp and Jasper both have the math abilities needed, neither are cryptographers, and thus lack some of the context needed to understand and evaluate the increasing number of crypto solutions being developed (not to mention being already busy improving Grin in other ways).

I hereby propose we use some Grin council funds to hire a full-time cryptographer to start working on ways to implement one-sided payments, reduce transaction linkability, and increase scalability. Improving in these areas would help increase the privacy, usability, and long-term viability of Grin.

I understand that this is unlikely to be as simple as just posting a job opening, but I’m willing to do the legwork to seek out willing and capable candidates for the job.

---

### Post by @tromp ⭐ (2019-09-12)
*Post #2*

david:

> Nearly every other serious cryptocurrency

The ones I know are Bitcoin, Ethereum, Monero, Zcash, and Zcoin. I’m guessing there’s very few others you would consider serious.

david:

> one-sided payments

The consensus is that such a thing is impossible. The sender would not be able to produce a rangeproof for the receiver’s output as that requires knowledge of its blinding factor. So I fear you’d be paying someone to stretch the definition of “one-sided”…

david:

> reduce transaction linkability

This is a most worthwhile goal. Beam is pursuing a Lelantus based approach that looks promising but prevents pruning of spent outputs.
The big challenge is how do it without any downsides like harming scalability and/or decentralization. That would be one of the holy grails of MW.
But it will probably require lots of creativity. I don’t consider this a well-defined task that someone can be hired to carry out.

david:

> increase scalability

MW is already leading the pack in scalability. IBD remains a bottleneck with the requirement to validate all kernels in history. This could benefit from any of the proving systems that the crypto community at large is already working on.
If you pick one, then its implementation for Grin is a pretty well defined task. But picking one is the tricky part, as new systems seem to come out almost every other month. In principle that is not a problem as long as we keep our current protocol untouched, and offer the the new proofs as an optional shortcut. We may end up with multiple different proving systems, and different proof acceleration services running on top of the base layer.

I see no urgency to do this any time soon though, as IBD time is currently far from a bottleneck, and we can just wait longer to see better proving systems developed and mature.

In summary: I think hiring a cryptographer makes sense once you identify a relatively well defined task that will bring clear benefits.

---

### Post by @david ⭐ (2019-09-12)
*Post #4*

> I’m guessing there’s very few others you would consider serious.

That is correct. Missing 2 or 3, but you covered _most_ of them.

> The sender would not be able to produce a rangeproof for the receiver’s output as that requires knowledge of its blinding factor.

There was the “hanging outputs” idea that GandalfThePink proposed [Investigate BLS Signatures · Issue #2504 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/issues/2504#issuecomment-467446197). It doesn’t seem like the perfect solution, but it seems like it could make a good starting point.

> But it will probably require lots of creativity. I don’t consider this a well-defined task that someone can be hired to carry out.

Lelantus wasn’t the result of a well-defined task that Aram was hired to perform. Zcoin took a risk, found a good cryptographer, and let him do his thing. Sometimes, impressive systems are designed (like Lelantus). Other times, not so much. Every breakthrough starts with R&D. I certainly don’t agree with the premise that cryptographers must be given a clear set of requirements, or that they’re only capable of implementing well-defined cryptosystems.

> I see no urgency to do this any time soon though, as IBD time is currently far from a bottleneck, and we can just wait longer to see better proving systems developed and mature.

Maybe you’re right, or maybe we’re just making it harder on ourselves later (like bitcoin is). It seems like being able to aggregate bulletproofs and/or kernels now would be better than starting years later, but perhaps that’s not true.

---

### Post by @david ⭐ (2019-09-12)
*Post #5*

After asking Rueben to review, I want to add some clarification.

> Lelantus wasn’t the result of a well-defined task that Aram was hired to perform.

While technically correct, this is easy to misinterpret. Aram may not have been hired to perform a specific _task_ , but he _was_ hired to achieve a specific _goal_ : “Get comparable anonymity or feature sets then zcash without fancy crypto or trusted setup”

And while I don’t yet know how or even if it’s possible, I still see value in Grin hiring a cryptographer with a specific _goal_ : “Reduce transaction linkability without harming scalability and/or decentralization”

Zcash similarly has several cryptographers working on several goals, and state-of-the-art cryptography has been developed as a result (whether it’s safe to trust any of their moon math is a different question). Same with Monero. I see no reason why Grin shouldn’t follow in the footsteps of the others if we plan to be a privacy coin, because as of right now, most of the privacy Grin provides is illusionary.

---

### Post by @jaspervdm ⭐ (2019-09-12)
*Post #6*

While I do think “illusionary” is a bit too strongly worded, I do agree that it could be worthwhile to have a cryptographer researching Grin related topics.
Out of the things you mentioned, i think that finding a way to reduce the input and output linkability is the most pressing.

Since we obviously don’t have the budget to spin up a whole team of cryptographers, maybe we could find a way to structure it as a (post-doctora)l research grant in collaboration with a cryptography department at a university? This would allow for some senior supervision and give the person an environment to bounce ideas off of and keep up to date with related research. Just a thought, not sure if it’s a good one. It would make matters a bit more complicated for us and would maybe also be a too long of a commitment, since postdocs are usually at least a year long. And we might exclude some potential candidates who aren’t interested in doing it in this way. I also don’t know if any university would be interested in that kind of thing in the first place.

---

### Post by @david ⭐ (2019-09-13)
*Post #13*

Yep, I agree, starting with the student route seems like a thrifty approach that should be considered. I do believe we have enough budget for a cryptographer though. Monero pays Sarang approximately 1 standard yeast unit per month, and we’ve already earmarked an extra full-time dev or two in the budget at that salary.

---

### Post by @david ⭐ (2019-09-13)
*Post #16*

I’ll get it added to the governance agenda and we can all discuss our options there. Let me know if you can’t make it.

---

### Post by @david ⭐ (2019-09-17)
*Post #30*

> I agree with this sentiment. Grin should attract the talent it needs by itself.

How? It hasn’t attract a cryptographer yet.

---



## 3 Reasons Why BEAM is Winning
*Date: 2019-09-22 | [Forum Link](https://forum.grin.mw/t/3-reasons-why-beam-is-winning/6119)*
*Importance Score: 121.5 | Core Participants: david, davidtavarez*

### Post by @IndridCold (2019-09-22)
*Post #1*

There are a few reasons BEAM is taking market attention and winning the MW race, IMHO.

To preface this, I do believe the principles of GRIN are still stronger and longer term it will be a more antifragile project given the true open-source roots and developer talent. However, BEAM has done a better job on the so-called “business” and also user front – this is not surprising given their governance but it still an area of concern moving forward.

1. The biggest reason is the BEAM Wallet, bar none. Users want to feel like they have a homegrown, GUI-based, tested desktop client to transfer funds to from exchanges. I believe you can also mine BEAM from the wallet. Right now, yes, GRIN has Ironbelly, Grin++, etc but I’m sorry to say, these aren’t appealing to the average user. The sending of transactions is still abysmal and clunky for the average buyer/user. This is far and away the reason GRIN is losing attention.

The GRIN site itself needs a Wallet section, where GRIN devs sign off on the top 3 wallets based on security/usability/etc. Users/buyers have no idea where to go, and the current Wallet ecosystem is utterly behind BEAM. Go download the BEAM Wallet if you haven’t, it’s beautiful. If GRIN had this from the get-go, we’d be seeing 2X the amount of buyers and holders as we do today.

I just hope this focus on raw protocol development versus any semblance of usability pays off in the long run.

2. The simple fact that BEAM is more centralized allows for more direct marketing, discussions with exchanges, and having an executive team and points of contact. This isn’t a strength necessarily, it’s just a fact that gets things done more quickly. Having an executive team to hold accountable could also be an eventual pitfall for the project, so I am not too concerned with this one.

I’m not sure what the answer here is for GRIN. I know the council has had direct discussions with exchanges when needed, but I know no one wants to be that ‘point of contact’ at all times. Shuffling this duty around may help.

3. Faster development, more catalysts, more clear roadmap. They have done a better job laying out their ~6-12-18 month plans for development. Again, “faster” is not necessarily a good thing in the long term if they rush protocol development and are not laser-focused on security and scalability. Another reason they can turn development over quicker is their centralized governance. Executives can simply sign off on the roadmap, whereas GRIN has a slower, more conservative consensus.

A more visual, defined roadmap would help outside of Github.

* * *

The outcome I am hoping for is that BEAM helps raise awareness for MimbleWimble and paves the way for exchanges and the crypto community better understanding it. BEAM can be the educator for MW, but GRIN needs to eventually come in as the BEST option for MW with cypherpunk roots. From there, GRIN will continue becoming battle-tested and superior on the security and protocol layer front. By the time GRIN ‘catches up’ on usability, MW will be more well-known and integrated, but GRIN should have far better privacy, scalability, and antifragility by then.

---

### Post by @david ⭐ (2019-09-23)
*Post #12*

IndridCold:

> Right now, yes, GRIN has Ironbelly, Grin++, etc but I’m sorry to say, these aren’t appealing to the average user

My whole goal when designing the Grin++ UI was to appeal to the average user, but it sounds like I have failed to achieve that goal. Suggestions are more than welcome for how I can make this experience better. Thanks

---

### Post by @david ⭐ (2019-09-23)
*Post #16*

> Check out BEAM’s wallet as a start

I have, but I’m UX-challenged, and don’t know how to learn from another UI without just directly copying it  . If you have specifics on what you think Grin++ is lacking compared to Beam, I’m all ears.

The big UX advantage they have over us is they only support 1 transaction method (SBBS), whereas we support file, http(s), keybase, grinbox, etc. There are initiatives to simplify this[1], but I’m interested to hear ways I can improve further.

[1] [Online Transacting via TOR Hidden Services by DavidBurkett · Pull Request #24 · mimblewimble/grin-rfcs · GitHub](https://github.com/mimblewimble/grin-rfcs/pull/24)

---

### Post by @david ⭐ (2019-09-23)
*Post #22*

Excellent! I’ll PM you. I’d love to chat about ways to make Grin++ simpler and easier to use.

---

### Post by @davidtavarez ⭐ (2019-10-18)
*Post #66*

Actually, I think you’re right. People says GRIN is only oriented to tech savvy. I believe in GRIN in the long term, but I feel that it’s time to start focusing in he regular user. I met a lot of crypto enthusiasts that aren’t technical at all. The wallet and even the miner should be built for end users.

---

### Post by @david ⭐ (2019-10-22)
*Post #71*

Serious question [@0xb100d](/u/0xb100d): Why launch if we aren’t ready for everyday users? It goes against the idea that Grin’s launch was meant to be fair and accessible to everyone.

---

### Post by @david ⭐ (2019-10-22)
*Post #73*

Yea, I wondered if the Beam launch had something to do with the timeline. Thanks for the insight!

---

### Post by @davidtavarez ⭐ (2020-06-04)
*Post #97*

GonzaloTellez:

> Today with so many protests and problems in various governments, corruption and espionage by even communications companies, people will really love this technology.

Are you willing to go out and promote Grin? If I receive the gear/swag I could do it in my city

---



## Grin-tech.org domain expiration
*Date: 2019-09-29 | [Forum Link](https://forum.grin.mw/t/grin-tech-org-domain-expiration/6153)*
*Importance Score: 72.2 | Core Participants: antioch, lehnberg, quentinlesceller*

### Post by @0xb100d (2019-09-29)
*Post #1*

looks like igno forgot to pay the bill… send me IP so I can forward grin.mw [@lehnberg](/u/lehnberg) [@yeastplume](/u/yeastplume)

---

### Post by @lehnberg ⭐ (2019-09-30)
*Post #4*

Once again good job on this [@madwax](/u/madwax). Perhaps you could help [@0xb100d](/u/0xb100d) do the same so that grin.mw could point to the repo too?

I’ve contacted the domain name registrar and explained the situation, and asked whether they would consider a transfer to us now that the domain has expired. Let’s see how they respond, if at all.

---

### Post by @lehnberg ⭐ (2019-09-30)
*Post #6*

[@MerlinsBeard](/u/merlinsbeard) I don’t think much would happen if the repo would be shut down, we could migrate the code to another repo or another platform (such as GitLab), or even self host.

On the domain front, it would be a shame to lose all the valuable SEO ranking built up by forfeiting the domain completely without a redirect.

It would also open up for various scammers that could seize the domain and carry out attacks on the project, for example by cloning the `/site` repo, but editing the donation addresses to something other than what is in fact the general fund.

I’m personally keen to avoid this. So while I do encourage us as a community to both work out fall back solutions, and also to build and deploy more informational websites about Grin beyond the content of `/site`, I think we should in parallel also try to retain control of [grin-tech.org](http://grin-tech.org) if at all possible.

---

### Post by @lehnberg ⭐ (2019-10-02)
*Post #11*

Quick update: contacted both the registrar and the registration service provider, offering to pay for the extension of the account (i.e. without a transfer), but to no avail.

Will try to get the domain when it expires, but realistically, the chances for that will be quite low.

In the meanwhile we’ll look to mitigate by moving to grin.mw as was kindly offered above by [@0xb100d](/u/0xb100d).

Other ideas are welcomed.

---

### Post by @lehnberg ⭐ (2019-10-06)
*Post #17*

Yep, <https://grin.mw> now resolves correctly

---

### Post by @lehnberg ⭐ (2019-10-07)
*Post #20*

[@grundkurs](/u/grundkurs) we’re trying to get back control of the old domain, but this will likely take another month or so at least. If this fails, it probably makes sense to fully transition to the new address, but in the meanwhile, I’m personally inclined to make as few changes as possible.

We’ll discuss the matter of the domain name in tomorrow’s governance meeting, you and others are welcome to participate: <https://github.com/mimblewimble/grin-pm/issues/196>

---

### Post by @lehnberg ⭐ (2019-10-08)
*Post #23*

Yes, looks like it broke yesterday, looking into it.

---

### Post by @lehnberg ⭐ (2020-06-28)
*Post #56*

Thanks for reporting, this is now fixed.

For future reference, the wikis are directly editable by anyone (by clicking `Edit` button in the upper right hand corner). So if you see something that needs improvement, you have the ability to do so immediately.

---



## Donation to the Grin General Fund - Nov 11
*Date: 2019-11-11 | [Forum Link](https://forum.grin.mw/t/donation-to-the-grin-general-fund-nov-11/6446)*
*Importance Score: 87.2 | Core Participants: lehnberg*

### Post by @lehnberg ⭐ (2019-11-11)
*Post #1*

I’m pleased to announce receipt of another coinbase donation to Grin’s General Fund: [Bitcoin / Transaction / 0810b1644cea890aad01564de5e4518ebcddb4c84df0c93223f050d580edee45 — Blockchair](https://blockchair.com/bitcoin/transaction/0810b1644cea890aad01564de5e4518ebcddb4c84df0c93223f050d580edee45)

I had the privilege to interact briefly with this donor who wishes to remain anonymous. Some quotes I’ve personally edited and now share with you.

**Note:** “you” below refers to “the team” and no individual.

> I know how you treated the last donation, this is why I am contacting you.
>
> I don’t judge you on how to spend just want to make sure you can process it and distribute it as you need
>
> It feels like 2009/2010 again
>
> Don’t worry, you are doing great.
>
> It’s wonderful that we have GRIN now, our motives are not economical! It’s about the technology and the protocol.
>
> Please put it to good use for the development of GRIN.
>
> You keep working as you did in the past.
>
> We saw your work and your ethics towards the project and your interest free work.
>
> This is what we are honouring right now with these donations so that you can work freely on GRIN. Without economic dependencies.
>
> Thank you again for your work and please keep it this way.
>
> Hopefully we judged it right, time will tell.

---

### Post by @gary (2019-11-11)
*Post #11*

thanks a lot for your generous donation! nice 11.11

---

### Post by @babaji (2019-11-12)
*Post #20*

What are the odds that this is true?

[NewsLogical – 12 Nov 19](https://newslogical.com/charlie-lee-claims-satoshi-nakamoto-recently-donates-50-btc-to-grin/ "02:50PM - 12 November 2019")

### [Charlie Lee Claims Satoshi Nakamoto Recently Donated 50 BTC to Grin -...](https://newslogical.com/charlie-lee-claims-satoshi-nakamoto-recently-donates-50-btc-to-grin/)

The founder at Litecoin Foundation, Charlie Lee, has recently dropped a bombshell regarding the identity of the mysterious father of crypto

---

### Post by @Chronos (2019-11-13)
*Post #23*

How much of the first 50BTC donation was remaining in the dev fund at the time of the second donation?

---

### Post by @Chronos (2019-11-14)
*Post #30*

Chronos:

> How much of the first 50BTC donation was remaining in the dev fund at the time of the second donation?

* The first 50 BTC donation from this anonymous supporter was on May 6. See income_id=137 of the [income log](https://github.com/mimblewimble/grin-pm/blob/master/financials/income_log.csv).
* Since that time, about 15 BTC has been spent. See [spending log](https://github.com/mimblewimble/grin-pm/blob/master/financials/spending_log.csv).

Therefore, the second donation was given at a time when the majority of the first donation remained unspent.

---

### Post by @Orajt (2025-07-26)
*Post #38*

The CEO of Nano Labs claimed the 100 BTC (2x50 BTC) donation came from Binance.

Nano Labs not only designed the chips for Grin ASIC miners (iPollo G1 series), but also recently revealed plans to accumulate 10% of all BNB.

Binance has tightened ties with them.

A few months later, the tweet was quietly deleted,

[IMG_22821284×1082 214 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/dbac70c91c7a8b73df27a5ad67a44ddd87a0207b.jpeg "IMG_2282")

right after Nano Labs signed a $500M agreement with Binance.

---

### Post by @Cobragrin (2025-07-26)
*Post #39*

Orajt:

> The CEO of Nano Labs claimed the 100 BTC (2x50 BTC) donation came from Binance.

Binance founded at **2017**. Binance donated _ironbelly wallet_.
Ceo of Nano Labs deleted many tweets before.

Donation wallets are from **2010**.
[News Link](https://www.thecryptoupdates.com/grin-received-50-btc-via-donation/)

---



## Breaking Mimblewimble’s Privacy Model
*Date: 2019-11-18 | [Forum Link](https://forum.grin.mw/t/breaking-mimblewimble-s-privacy-model/6532)*
*Importance Score: 88.9 | Core Participants: david, tromp, antioch, quentinlesceller*

### Post by @xhipster (2019-11-18)
*Post #1*

Was not able to find any reference to [this article](https://medium.com/dragonfly-research/breaking-mimblewimble-privacy-model-84bcd67bfe52) of [Ivan Bogatyy](https://twitter.com/IvanBogatyy) on the forum so I decided to start this discussion.

The question is straightforward: Would Grin community accept the lack of privacy (linkability with amount obfuscation) or some workaround could be found?

---

### Post by @david ⭐ (2019-11-19)
*Post #8*

FirsArgentum:

> this doesn’t necessarily mean the actual originator of a transaction could ever be identified?

But often it does mean this. Grin is not private, and the response to yesterday’s article proves exactly why we need to be more vocal about this fact. We intend for it to be private sometime soon, and we have several paths we could take to get there, but as is, it’s transparent AF. The only thing hidden are amounts.

---

### Post by @david ⭐ (2019-11-19)
*Post #11*

Correct, IP address is not leaked.

Totally agree about lack of education. There were a lot of inflated expectations among casual grin users.

---

### Post by @david ⭐ (2019-11-20)
*Post #15*

Dandelion tweaks for increasing stem phase aggregation, adding decoy inputs and outputs, improving input selection, using coinjoin servers, payment channel hubs, etc. Mimblewimble is unique, and offers many possibilities. We’ve just got to figure out which combinations lead to the best outcome and tradeoffs.

---

### Post by @tromp ⭐ (2019-11-20)
*Post #17*

There was some discussion in keybase channel grincoin.teams.node_dev#research

---

### Post by @antioch ⭐ (2019-11-20)
*Post #20*

No - that channel is completely open to anyone who wants to join.

---

### Post by @quentinlesceller ⭐ (2019-11-21)
*Post #23*

Not sure why. But I can see it on my end:

[ 193038×198 26 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/862fc62959a88697d327d13b6cc6012b73620b40.png "19")

We should figure out a way to link those channels as they are buried in sub teams… One suggestion was to have some kind of shortcut on the main channel to link all of those.

---

### Post by @quentinlesceller ⭐ (2019-11-22)
*Post #25*

This channel is definitely open to everyone. On your end you have to request access? I did not receive any notification.

---



## Next PoW CuckARooM unveiled at GrinCon1
*Date: 2019-11-24 | [Forum Link](https://forum.grin.mw/t/next-pow-cuckaroom-unveiled-at-grincon1/6605)*
*Importance Score: 85.4 | Core Participants: tromp*

### Post by @tromp ⭐ (2019-11-24)
*Post #1*

Grin’s unique dual PoW system allows for a smooth transition from GPU
mining to ASIC mining, with guaranteed rewards for the secondary PoW
where GPUs need not compete with ASICs.
The main ingredient for its ASIC resistance is frequent pre-planned PoW changes.

In [0] I introduced Cuckarood as the first tweak of Cuckaroo.

Just like Cuckaroo was only active for the 6 months from Jan 15, 2019 through Jul 17, 2019, so Cuckarood will no longer be active when Grin executes its 2nd pre-planned Hard Fork around Jan 15, 2020.

Its successor, and latest member of the Cuckoo Family,
“Cuckaroom”, was unveiled last Friday at GrinCon1 as can be seen in slides [1] and video [2].
In the earlier post linked above I mentioned 3 aspects of Cuckaroo that could be tweaked:

1. the underlying hash function, currently siphash-2-4
2. the computation of endpoints of a whole block of edges
3. the type of cycle

Where Cuckarood made tweaks in 1) and 3), Cuckaroom makes tweaks in 2) and 3) instead.

Regarding siphash, Cuckaroom reverts to the standard siphash.

Regarding edge block computation, instead of xoring intermediate siphashes with the final one:

const u64 last = buf[EDGE_BLOCK_MASK];
for (u32 i=0; i < EDGE_BLOCK_MASK; i++)
buf[i] ^= last;

as in Cuckaroo/Cuckarood, in Cuckaroom we xor with all subsequent siphashes:

for (u32 i=EDGE_BLOCK_MASK; i; i--)
buf[i-1] ^= buf[i];

The biggest change is in the type of cycle. The CuckarooM graph is no longer bipartite, with the ‘M’ standing for ‘Monopartite’.
Cuckaroom29 has 2^29 directed edges on 2^29 nodes, resulting in cycles of all possible lengths, including odd ones, and even including unicycles.

Cuckaroom is implemented in the cuckoo repository at [3].
The proof verification function [4] may serve as the specification,
while Makefile targets simple19/simple29 implement a simple CPU miner and target cuda29 a reasonably performant CUDA mean miner. Due to the alternation of marking starting-points and end-points, this miner takes twice as many rounds to trim a given fraction of edges.

The expected number of 42-cycles in a Cuckaroom graph is 1/42, as it was in Cuckaroo, which is half of Cuckarood’s current value of 1/21.

So we can expect a large drop in C29 solution rate come hardfork time,
from 1) slower solvers, 2) halved solution rate, and the seemingly unavoidable 3) unprepared miners. However, difficulty should adjust within a matter of hours.

In the coming week, I will push Pull Request on grin [5] and grin-miner [6] to implement the PoW changes on the Grin side of things. Then we’ll have a chance to see Cuckaroom activate on Floonet around December 19.

Happy Cuckoo Cycling!

[0] <https://forum.grin.mw/t/mid-july-pow-hardfork-cuckaroo29-cuckarood29>
[1] <https://github.com/mimblewimble/grin-pm/blob/master/presentations/grincon1/10-cuckaroom-tromp.pdf>
[2] <https://www.youtube.com/playlist?list=PLvgCPbagiHgrQa5KVt4XixK9t_NbfpkuP>
[3] <https://github.com/tromp/cuckoo/tree/master/src/cuckaroom>
[4] <https://github.com/tromp/cuckoo/blob/master/src/cuckaroom/cuckaroom.hpp#L133-L164>
[5] <https://github.com/mimblewimble/grin/pull/3136>
[6] <https://github.com/mimblewimble/grin-miner/pull/231>

---

### Post by @tromp ⭐ (2019-11-25)
*Post #3*

ddd:

> this new release is just improving highend rigs

Where do you get that?

---

### Post by @Lolliedieb (2019-11-25)
*Post #4*

Like the changes, but will be interesting to tune the solvers - that monopartite structure makes things interesting. But wrt [@ddd](/u/ddd): As far as I can see all cards that are now physically able to mine grin-29 should also be able to do so in the future - so I do not see why this would require larger rigs. Only the hash may go down a bit due to a slower solver, but that hits slow and fast cards / small and big rigs the same way and the difficulty adjustment will handle this rather quickly.

---

### Post by @Lolliedieb (2019-11-26)
*Post #7*

By the way I did try to calculate the fraction of edges that remains now after each round.
The formulas have changed compared to cuckaroo and cuckatoo, because there now is a dependency in the 2nd round trimming.

The following formula is still unproven, but fits first experiments very well:

Let a_0 = b_0 = 1
And then a_n = 1 - exp(- b_(n-1)) and b_n = a_(n-1) for each later round.
Then the fraction of edges left after round i equals a_i * b_i

Here is a table for the first 50 rounds:

round	fraction	cumulative fraction
0       1               1
1	0,6321205588	1,6321205588
2	0,3995764009	2,0316969597
3	0,2961714876	2,3278684473
4	0,2195263531	2,5473948004
5	0,1752711746	2,722665975
6	0,1399375711	2,8626035461
7	0,1167434973	2,9793470435
8	0,0973937454	3,0767407888
9	0,0836613349	3,1604021237
10	0,0718651791	3,2322673028
11	0,0630385242	3,295305827
12	0,0552959804	3,3506018074
13	0,049275533	3,3998773404
14	0,0439105724	3,4437879128
15	0,0396150783	3,4834029911
16	0,0357397852	3,5191427764
17	0,0325646834	3,5517074598
18	0,0296716558	3,5813791156
19	0,027256743	3,6086358586
20	0,0250383749	3,6336742335
21	0,0231578796	3,6568321131
22	0,0214186181	3,6782507312
23	0,0199250419	3,6981757732
24	0,0185356167	3,7167113898
25	0,01732921	3,7340405998
26	0,0162013234	3,7502419232
27	0,0152126251	3,7654545484
28	0,014284263	3,7797388114
29	0,0134636728	3,7932024841
30	0,0126902231	3,8058927072
31	0,0120015418	3,817894249
32	0,0113502342	3,8292444832
33	0,010766533	3,8400110162
34	0,0102128493	3,8502238655
35	0,0097137542	3,8599376197
36	0,0092390496	3,8691766693
37	0,0088089122	3,8779855815
38	0,0083988006	3,8863843821
39	0,0080254388	3,8944098209
40	0,0076686745	3,9020784954
41	0,0073424885	3,9094209839
42	0,0070301767	3,9164511606
43	0,0067435175	3,923194678
44	0,0064685469	3,929663225
45	0,0062152588	3,9358784838
46	0,0059718887	3,9418503725
47	0,0057469717	3,9475973442
48	0,0055305257	3,9531278699
49	0,0053298844	3,9584577543
50	0,0051365222	3,9635942765

The series seems to converge (for over 5000 rounds) to a value at around 4.25.

Also worth a mention that after 2n-1 rounds the same number of edges is left as before after n rounds

---

### Post by @tromp ⭐ (2019-11-26)
*Post #8*

Alternatively, we could count sorting rounds instead of trimming rounds, in which case the numbers shift down like

round	fraction	cumulative fraction
0       1               1
1       1               2
2	0,6321205588	2,6321205588
3	0,3995764009	3,0316969597
4	0,2961714876	3,3278684473

giving a fraction matching between round 2n and cuckaroo(d) round n.

---

### Post by @Kurt (2019-11-27)
*Post #9*

Proving that the serie converges is a little math exercise (it does converge).

hints:

* prove that the (a_n) (or (b_n)) sequence converges to 0
* do a Taylor expansion (order 2) of the recursive relation
* use Cesàro lemma to get an equivalent of (a_n), or (b_n)
* conclude

---

### Post by @slate (2020-01-05)
*Post #11*

Kurt:

> Proving that the serie converges is a little math exercise (it does converge).
>
> hints:
>
>   * prove that the (a_n) (or (b_n)) sequence converges to 0
>   * do a Taylor expansion (order 2) of the recursive relation
>   * use Cesàro lemma to get an equivalent of (a_n), or (b_n)
>   * conclude
>

Or just denote the limit by L (showing it exists is trivial), where you have that lim_n a_n = lim_n a_{n-1} = L, and hence L=1-exp(-L), which gives L=0, without any approximations or iterative methods.

---

### Post by @Kurt (2020-01-05)
*Post #12*

You did not understand my post and what we want to show.

---



## Request for Funding, @lehnberg: Jan-Mar 2020
*Date: 2019-12-22 | [Forum Link](https://forum.grin.mw/t/request-for-funding-lehnberg-jan-mar-2020/6767)*
*Importance Score: 115.8 | Core Participants: david, antioch, yeastplume, tromp, lehnberg*

### Post by @lehnberg ⭐ (2019-12-22)
*Post #1*

## tl;dr

On Jan 5, my funding from [the previous campaign ](https://forum.grin.mw/t/request-for-funding-lehnberg-oct-jan-2019-20/6165) will expire.

This is a request for a 3 month extension `(Jan - Mar 2020)` in order for me to continue to be able to support Grin with the type of contributions I’ve been doing in 2019.

As part of this request, I’m proposing:

**To change the rate paid from USD 2,500/month to GBP 2,500/month.** This means that in USD terms, the new rate would (as of Dec 23 2019) be **$3,231.80** according to Google which **amounts to a raise**. See the FAQ below for more details.

I’m adding this request to the agenda for the [Jan 14 Governance meeting](https://github.com/mimblewimble/grin-pm/issues/233).

* * *

## Motivation

The original motivation still holds true today:

> Beyond work on the main grin (node/wallet/miner) repositories, work on the admin side of the project has evolved over the past year. The [/grin-pm ](https://github.com/mimblewimble/grin-pm) repo is now a place where we track general project management issues, meeting notes, event presentations, financial data, and more.
>
> I think this work adds value and is important for the project’s health, for it’s good governance, and for progress to be made faster.
>
> Grin would get reliable and consistent support for the non-development related tasks, that would help achieve its potential quicker.

## Evaluation of previous period

### My own assessment

* I believe the [weekly progress update thread ](https://forum.grin.mw/t/lehnberg-progress-update-thread-oct-19-to-jan-20/6230) covers my detailed contributions well.

Some of the past 12 week period’s efforts worth calling out in particular:

* grincon1:
* Worked to secure $20k in fundraising from two donors
* (Minimal) Website design
* On the ground work & speaker relations
* Video & Slide publications
* Grin [3.0.0 communications](https://forum.grin.mw/t/grin-v3-0-0-hard-fork-upgrade-jan-2020/6036) & [planning process](https://github.com/mimblewimble/grin-pm/issues/204).
* Grin Roadmap 2020 initiative
* PR work as part of the response to the “Breaking MW” article
* Work on /grin-pm, including transparency report
* Donor liaising

#### What went well?

* All the scope as outlined in the funding request was carried out as intended.
* There’s been consistency in quality and delivery, with no missed deliveries (although note that I am taking a break from the newsletter over the coming holiday period as it will be low activity in any case).
* Grincon1 turned out to be a nice event. I’m happy for the support I was able to offer personally.
* The planning feels as though it’s been greatly improved ahead of 3.0.0, and I will be thinking about how we can make it even better moving forward.
* I think I’ve become better at managing my personal grin/life balance. I’m more focused in the time I spend on the project, and “disconnect” more frequently. Aside from the full on madness days that ensued after the “Breaking Mimblewimble’s privacy model” article, it’s felt more like the part-time effort it should be.

#### What could have been improved?

* Prioritization of tasks.
* I think grincon would have benefitted from even better planning and more lead up notice. It ended up feeling a bit rushed.
* While I think we provided a decent response in the few hours of turnaround time we had to produce the reply to the “Breaking MW privacy Model” article, I feel we could have done an even better job here, and in the PR interactions that followed with journalists.
* I’m worried about the degree of centralisation in the project. We’re not seeing many contributions from a wider group of community participants. I don’t have a good response to what’s needed here, but it’s something I think about.
* I’m still too slow at turning around meeting notes.

#### What have I learned?

* Keep the long term view.
* Things will go wrong, there will be chaos and panic. Let cool heads prevail when the shit hits the fan.
* Never provide a written quote to a journalist that can be taken out of context and completely misconstrued.
* There will always be more work. Continue to work on time management and focus on the contributions that will have the most impact.

### Community feedback

Feel free to raise feedback and/or suggestions in the thread below, or in private, my DMs are open.

## Specific tasks in-scope

Same as last:

* Meeting related admin
* Maintain [agendas](https://github.com/mimblewimble/grin-pm/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3Ameetings+)
* Write [meeting notes](https://github.com/mimblewimble/grin-pm/tree/master/notes)
* Update the [decision log ](https://github.com/mimblewimble/grin-pm/blob/master/decision_log.md)
* Financials / book keeping
* Keep [grin-pm/financials/ ](https://github.com/mimblewimble/grin-pm/tree/master/financials) up do date.
* Publish quarterly transparency reports
* News reporting
* Publish the [weekly grin newsletter ](https://grinnews.substack.com)
* Submit [updates to the weekly Proof of Work newsletter](https://github.com/mimblewimble/docs/wiki/Proof-of-Work-Newsletter-updates)
* Media relations
* Focal point for media enquiries
* Weekly status report to keep track of progress.
* Manage [/grin-rfcs](https://github.com/mimblewimble/grin-rfcs) and [/grin-security](https://github.com/mimblewimble/grin-security) repos and the related processes.
* Focal point for corporate donors and ecosystem requests.

## Funding request

* **GBP £2,500/month**
* 3 months, Q1 2020, jan-mar.

### Role

* Part-time
* Ring-fenced around admin tasks

## Next steps

The intention is to raise this as a discussion point in the next Governance meeting and ask for the request to be approved.

## FAQ

### Why are you changing from USD to GBP?

As I primarily live and spend in London (United Kingdom), GBP is my main spending currency. By being paid in USD, I’m exposing myself to exchange rate fluctuations. This is the same (but on a much smaller level) as being paid in BTC: As the exchange rate moves, you end up being paid different amounts when you convert it back to your home currency. By being paid in GBP equivalent directly, this disappears. I also just now discovered that this is apparently in line with the project policy, so should have been done for the previous two campaigns: [Grin](https://grin.mw/funding.html#developer-funding-campaigns)

### Why are you keeping the rate at 2,500 and not converting 2500 USD to GBP, which would be something more like GBP 1,932.64 according to Google?

In my last funding request, I proposed 1/4th of a yeastunit, i.e. 10,000/4 = 2,500. I’d like to keep that measure as I think it makes sense. The yeastunit is not necessarily denominated in USD, yeastplume for example is paid in EUR equivalent.

### At today’s rates, this equates to ($3,231.80-2500)/2500= 0.29272 = 29.3% more in USD measures. Why are you not asking for a 29.3% raise instead?

The whole point of this is that I shouldn’t be paid in USD in the first place, as a gallon of milk for me is priced in GBP. A change in the USD exchange rate does not affect my day to day expenses, and I think £2,500 makes sense whilst being based in London, United Kingdom.

### Will you always ask in GBP from now on?

No, not necessarily. If I move country, I would change to a different home currency.

### Will you always ask for the same amount from now on?

No, not necessarily. At the moment, this is the amount I feel comfortable asking for, based on the work I’m doing for the project. This could change in either directions.

### What happens if the price of Bitcoin changes?

Nothing. The price of Bitcoin is completely orthogonal to this funding request.

### I don’t think this is right, I think you should receive some different amount. What should I do?

You can DM me with suggestions, or you can write here in the forum or on keybase. Or, you can attend the governance meeting when this will be discussed and make your own proposal.

## Changelog

Dec 22:
First version

Dec 23 #1:
* Added changelog section
* Changed 12 weeks into 3 months
* Clarified that the GBP x-rate switch will lead to a pay bump

Dec 23 #2:
* Clarifying the tl;dr section
* Adding FAQ section based on the questions and feedback received

---

### Post by @david ⭐ (2019-12-23)
*Post #3*

I obviously want to see you get funded again, but I tend to agree with [@johndavies24](/u/johndavies24). This proposal feels deceitful, first by not pointing out the 30% difference due to current GBP/USD exchange rate. But also, the previous requests have all been for 3 _months_ , not this cleverly re-defined 4-week “month”. This means your previous funding actually shouldn’t expire until the following week (12th or 13th).

Between the 30% increase from GBP/USD exchange rate, and the change from month to 4-weeks, you’re actually asking for a ~41% raise. It’s always difficult and uncomfortable to ask for a raise, so I understand the desire to mask intentions, but I don’t think that’s the kind of standard we would want to be setting for community funding proposals. I strongly recommend rewording to better highlight the changes vs last proposal.

---

### Post by @lehnberg ⭐ (2019-12-23)
*Post #4*

[@johndavies24](/u/johndavies24) Thanks for including that chart, I think it illustrates my motivation quite well! It’s a lot of fluctuation in the USD/GBP chart (just look at the past three months for example). I’d rather get paid in GBP as I live in the UK.

But yes, you’re right: `£2500 != $2500`. I don’t think I was suggesting that it was, but I also didn’t mean to be disingenuous. It’s good that you’re raising it, I take your feedback onboard, and will clarify the request.

---

### Post by @Yeastplume ⭐ (2019-12-23)
*Post #10*

He did get ask for and was gratefully granted a raise since his previous ‘part-time’ role project managing Grin quickly became an all-consuming uncompensated full time job when Igno suddenly left. He also left a comfortable full-time role (with a newborn on the way) to focus both on Grin and other ideas intended to promote Grin.

We’d be nowhere near where we are today without Daniel’s tireless contributions, both in keeping us organised and in willingly making himself a target for tons of mean-spirited, undeserved and unnecessary flack from the wider community to allow the development team to remain focused. If he says he made an error earlier, he made an error. And I hope I’m not alone in saying he can have whatever the hell he wants if it means he can keep contributing in the way has thus far.

---

### Post by @lehnberg ⭐ (2019-12-27)
*Post #35*

Thanks all. This turned out to be quite a thread. I’m disheartened by the request ending up being so contentious, but I’ve got mainly myself to blame for this. I wrote the initial funding request in a rush to get it out before the holiday break, wanting it to be short and high level. I did not imagine a scenario where readers would think I was being malicious, so I didn’t take that into account at all. In hindsight, I should have been clearer in my communication. Lesson learned. Still I hope most of you don’t think I was trying to deliberately sneak something past you: I wouldn’t have raised the request 3 weeks+ ahead of the meeting in that case.

If you want to, it’s probably quite easy to misconstrue most things I write. For example, there was exception taken to the phrase “according to Google”. I wrote it as I wanted to make clear which source I used. Google does mid-market exchange rates, which means that you wouldn’t necessarily get the same rate if you went to a proper currency exchange, and I didn’t want to get accused of deliberately providing misleading exchange rates. Such is the irony of it all, that a phrase I added in an attempt to prevent accusations, ended up being taken as a provocation. It all feels like a humbling experience to be honest, I’m learning to make fewer assumptions about how a reader interprets what I write. I’m hopeful this will lead to my writing improving over time.

[@chronos](/u/chronos), I wouldn’t want to amend the request down to GBP 2,000, I asked for GBP 2,500 explicitly, and I don’t think I’m over-reaching by doing so. It’s true that I’ve been gradually asking for more with each request, but I don’t see that as an issue. It’s a way of iterating, and (hopefully) improving confidence levels of the work I do and the value it carries. If Grin devs/community/council/whoever thinks I should get paid less than what I ask for, then it’s up to them to say so and take actions accordingly. I think my request is a good deal for Grin given the time and effort I’m putting in. After taxes, national insurance contributions, and factoring in living costs in London, it’s still not a great deal of money.

[@colincr33vey](/u/colincr33vey) I think there’s definitely an opportunity for more non-dev contributors to be supported for their work. Just as with development, there’s always a tonne of more work we could be doing. Anyone who’s making frequent and meaningful contributions on a regular basis should consider submitting a funding request. And anyone who wants to help but doesn’t know how / what’s needed, feel free to ask in the forums or on keybase.

[@johndavies24](/u/johndavies24) I agree with others that you’re being off-topic. But since you bring all these past events up, I want to make clear that I think you are way off in your summaries of what happened and the conclusions you draw from them. I don’t speak for others, but if you want me to listen more to your suggestions and ideas, try to be friendly, constructive, and don’t assume I’m being malicious. I’ll have an easier time understanding where you are coming from then.

[@paouky](/u/paouky) the fund definitely ended up being a mixed blessing, it feels like we’re stuck with it for better or worse until someone comes up with a better solution.

---

### Post by @lehnberg ⭐ (2019-12-30)
*Post #39*

Hi [@johndavies24](/u/johndavies24)

I don’t know whether it makes sense, neither for myself, or for Grin, for me to work full time on the project right now. What I do know, is that I feel comfortable with making this request for the horizon of Q1 2020. Beyond that, circumstances might change, both for the project and for myself.

> Just ask for what you deserve in a straight forward manner.

Definitely take this feedback onboard, and will try to be clearer moving forward.

> Maybe we could propose to break up the funds into known future expenses (audits, servers, domains, etc, not sure what the guaranteed future costs are), bounty funds, rainy day funds (and applied requests) and dev/core salaries. The first and fourth groups would be priority and the 2nd and 3rd would promote non-core involvement. Obviously, the first and fourth groups may need to pull from the 2nd and 3rd if new funds dont come in.

While I don’t want to derail the topic of this thread, if you feel like it, please write up a full circled proposal with as much details as you can think of about what exactly this would achieve, how it would work in practice, and why you think it is necessary. And then we can discuss the idea in a governance meeting. You may even want to consider submitting an RFC about it.

---

### Post by @antioch ⭐ (2020-01-01)
*Post #54*

A funding request is simply “fund person X with amount Y for period Z”. Previous funding amounts are basically irrelevant for the purpose of deciding if this specific request should be funded.

Everything else being discussed here is orthogonal to this request. People are free to have concerns and reservations around the way this was asked for or phrased, but these should not and do not affect the underlying request being made. People are free to debate the relative worth of different people but its not really a useful way of thinking about this. People are also free to think of this as some huge unreasonable raise but again its not a useful way of framing this.

This is not a “salary” and it is a mistake to think of this request in terms of a “raise”. Individual needs change, situations change and requirements change over time. This is not a salary but a funds to allow a person to continue working on the project.

Contributors are not working to get paid on this project, but receiving funds to allow them to continue to work. This is a nuanced position but an important one.

So to restate this request in the simplest possible terms -

[@lehnberg](/u/lehnberg) is requesting GBP 2500 monthly for the three month period Jan, Mar 2020.

Given that Grin would not be where it is today without the _incredibly_ valuable contribution that [@lehnberg](/u/lehnberg) has tirelessly given to date this is an _entirely_ reasonably request and a strong  from me.

Happy New Year everyone. Lets push forward into 2020 in a positive way here.

---

### Post by @Yeastplume ⭐ (2020-01-01)
*Post #59*

I waded into this thead early on to defend a valuable and trusted colleague against a series of rabid and vitriolic attacks, with any truth they may or may not have contained completely overshadowed by the spiteful, arrogant and disrespectful nature in which they were presented.

I knew nothing about this funding request until Daniel posted it and the furore here kicked off, and there is nothing in my post earlier that I believe can be construed as anything other that an evaluation of his character and an appreciation for his ongoing contributions to this project in the face of haranguing such as that demonstrated in this thread. This is then twisted by the same poster to accuse me of somehow being in league with an imagined conspiracy, so I then find myself the subject of a personal attack also accusing me of having a deceitful character and other such nonsense. This was then followed by an arrogant and utterly condescending post informing me of what I may and may not refer to with respect to someone’s personal conditions in the course of this discussion.

I unfortunately lost it at this point, and posted a curt message (now concealed): ‘Who the fuck do you think you are?’ This was ill-advised and done in a flash of anger and frustration, and I apologise to the community for this lapse. Other members of the core team moderated that message and its reply, and I stand duly corrected and humbled in this regard. This of course gives the poster more ammunition that we’re somehow acting ‘deceitfully’, which in reality was the correct moderation action of removing two inflammatory messages that violate community standards and don’t belong in this discussion.

However, I maintain that the personal attacks contained in this thread violated community standards well before this exchange occurred, and I agree completely with [@Elephantul](/u/elephantul) that this thread embodies a moderation failure. Rectifying this (hopefully via a completely independent moderation team) is something we’ll be looking to address this year.

---


