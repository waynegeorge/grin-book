# Chapter 9: Decentralized Development

*25 topics selected for this chapter*

---

## Grin product wishlist
*Date: 2022-04-14 | [Forum Link](https://forum.grin.mw/t/grin-product-wishlist/9704)*
*Importance Score: 80.2 | Core Participants: yeastplume, tromp*

### Post by @trab (2022-04-14)
*Post #1*

What are some products that incorporate grin that you would like to see?

My goal is for us to think from a product perspective so that maybe it will become more obvious what is _missing_ from a _framework/foundation_ perspective.

Mine would be:

* Venmo / Cash app style wallet. Yes, privacy focused ppl won’t like this, but i think it is a must if we want to at least use Grin amongst our friends.

* some Point of Sale system for small businesses. i’m not sure what is needed here because i’ve never run a commerce business. i’d imagine best practices around transaction generation, auditability, etc

* web wallet that enables web apps to plug into Grin value transfer with a simple library include. sending tips back and forth. charging grin for usage of the website, etc.

what products would you like to see?

---

### Post by @Anynomous (2022-04-17)
*Post #5*

trab:

> a fundraising app. bare minimum is we need a way to give an app (1) a “view key” to a wallets contents and (2) an address for people to send grin to. that base level of accountability will let people see how close the wallet is to meeting its goal and if the person has withdrawn funds (ended the campaign)

View keys are there in the code of grin-wallet. Only there is no code or tool to export them or import them at the moment:
<https://github.com/mimblewimble/grin-wallet/search?q=viewkey>

Support for Viewkeys is on the wishlist but not very high priority. See here the wishlist

[github.com](https://github.com/grincc/hub/blob/main/wishlist.md)

#### [grincc/hub/blob/main/wishlist.md](https://github.com/grincc/hub/blob/main/wishlist.md)

## Criticals / Must Have

1. [PIBD - (faster and more robust syncing strategy)](https://github.com/stakervali/grin-wishlist/issues/6)
*-In beta, being tested on mainnet*
2. [multi-sig*](https://github.com/stakervali/grin-wishlist/issues/2)
*-Not happening any time soon if I understand correctly, since there is no solution yet to generate threshold range proofs:*
3. Wallet backend improvements
*- Grin-wallet had many bug fixes and stability improvements*
4. libsecp fork update
*-not updated, last commit to libsecp was 5 years ago*
5. safe cancel*
*WIP, not merged https://github.com/mimblewimble/grin-rfcs/pull/71, part of Grin GUI?*

## Important

1. Tor support for nodes*
2. [light node*](https://github.com/stakervali/grin-wishlist/issues/7)
3. [testnet exchange/ making it easier for exchange integrations](https://github.com/stakervali/grin-wishlist/issues/4)
*-Implemented - [Link]([url](https://github.com/stakervali/grin-wishlist/issues/4))*
4. payjoins*

This file has been truncated. [show original](https://github.com/grincc/hub/blob/main/wishlist.md)

trab:

> some Point of Sale system for small businesses. i’m not sure what is needed here because i’ve never run a commerce business. i’d imagine best practices around transaction generation, auditability, etc

For this we need a good payment proof system, preferably invoice payment proofs.
It is also on the wishlist, this one is high priority.
For now the focus is on PIBD (faster initial syncing of nodes/wallets) and probably on a GUI for grin-wallet. But it all depends. If another Developer joins who wants to work on these functionalities, work can suddenly go twice as fast and these other features can be there before you know it. For now we are happy to have Yaestplume/Michael around who is working on PIBD.

---

### Post by @trab (2022-04-26)
*Post #12*

trab:

>   * a fundraising app. bare minimum is we need a way to give an app (1) a “view key” to a wallets contents and (2) an address for people to send grin to. that base level of accountability will let people see how close the wallet is to meeting its goal and if the person has withdrawn funds (ended the campaign)
>

Some are having difficulty getting donations or funds for things they want to work on. To me, what seems to be lacking in fundraising for Grin projects is a lack of transparency.

This product would be something that the Grin community could “dogfood” _immediately_ with their own [GrinCC projects.](https://www.grincc.mw/projects)

If someone wanted to donate to a project right now, they don’t really know if it is already fully funded, or what the status is without asking. And if you simply ask, you’re just going off of someone’s word (unless it comes from the full community council where people keep each other accountable).

A fundraising app (or plugin or toolkit etc) would also enable people to work on projects outside of the purview of the CC and still be transparent with their donators.

---

### Post by @tromp ⭐ (2024-03-17)
*Post #36*

trab:

> need wallet view keys etc

There is [grin/keychain/src/view_key.rs at master · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/blob/master/keychain/src/view_key.rs) but I don’t know how well the wallet supports them…

---

### Post by @Yeastplume ⭐ (2025-03-08)
*Post #61*

Early payment proofs working and enabled by default in the contracts branch of the wallet, see related PR here:

[github.com/mimblewimble/grin-wallet](https://github.com/mimblewimble/grin-wallet/pull/681)

####  [[WIP] [Contracts] Early payment proofs](https://github.com/mimblewimble/grin-wallet/pull/681)

`contracts` ← `yeastplume:early_proofs`

opened 12:14PM - 18 Apr 23 UTC

[ yeastplume ](https://github.com/yeastplume)

[ +1319 -343 ](https://github.com/mimblewimble/grin-wallet/pull/681/files)

Following on from experimental slate V5, changes, this aims to implement an expe[…](https://github.com/mimblewimble/grin-wallet/pull/681)rimental version of [early proofs](https://github.com/tromp/grin-rfcs/blob/early-payment-proofs/text/0000-early-payment-proofs.md) into the `contracts` branch. Note that `legacy' transaction workflows are not affected. * Add required arguments structures and definitions * Add initial test for development purposes * (TBD) Other notes * signature for proof type `Invoice` is automatically generated by default. Generating another proof type or omitting proof requires `opting out` at present (subject to discussion)

Really, the best way to get payment proofs live would be to get the experimental contracts branch working within Grim and test,test,test to the point where we’d be comfortable merging all of the work in the contracts branch to master.

---

### Post by @ardocrat (2025-03-08)
*Post #62*

Hello, one community member tried to test proofs with grin-wallet and got an issue:

[github.com/mimblewimble/grin-wallet](https://github.com/mimblewimble/grin-wallet/issues/729)

####  [CONTRACTS: can't make a transaction](https://github.com/mimblewimble/grin-wallet/issues/729)

opened 08:24AM - 04 Dec 24 UTC

[ aglkm ](https://github.com/aglkm)

Wallet 1: ``` ./target/release/grin-wallet --testnet contract new --send=1 --e[…]()ncrypt-for=tgrin1pj5wlv3nhvua5lgr72dq9ufu8aw2m05ke5z47j5463zvrgej54qsstc3rg Password: \--------------- SLATEPACK METADATA -------------- Slate encrypted: true Slate finalized: false Slate saved to file: /slatepack/3198ee9b-f033-4e6e-8699-19c9cb58f82d.S1.slatepack \-------------- CUT BELOW THIS LINE -------------- BEGINSLATEPACK. 3pDmAZBPAaFKxhX Hhi1beNF3pCpmpY ugZNstfhxHzQtrZ zA9HUtMTgbXmUa6 FHQAqRSa3U1fwbu D3iaiYSPLT1hjTE qGMm2rdsVyBofM6 cp6ZDe7Lm3bEm2b 7jmdrzGyfPSTNrL fWrceZbM7rKFo59 bST38KxMXginKca Y7JcQbrJoETKc2W WY6vNTWzfg9QJBt PyDUZhzmMP9KYWT ECjhaagFWtxxfKw pTPMUxgQX6kdbGx NnfuJavCv658VAR ka9upRnBD3ti5MP 27iXnvFYZEpgHJc 4UQF4PutVPdBt2r pXTQ3dRx4bAmDAk j4RG9Y4wMv2h5sc XTKHJP8pHVZGk9n vqeYQWNEK5reqUX rtK4oyA63wCmq9D r75BTjwPn9vdqma eeb9oazDpALNDCn XtguxrSwoPn7coM iCUdCvGKeigZ3rw SokXdb7x8L6x7Ej 3QimTEkg9DoJFe6 FJsEGG5dFQMfzBK 9nEHGvaLt5c2MT3 MBd1FMi9p1fMGmm r7B7bNCMMqpZm6c 7Vfc4F7T4AFRyvF WFbgzGJsafYvfNq oLfZ4vfBquVBaW3 DFsKRBMXnvaA1xy n2L1MqziRyEzGSU BRtmt4xeU3jFtZY HnhsdryC5TdiTV3 i1G6pN6mhJdCXvW nbc51S4HV4gspJJ 3Tw7k2GTt8B4hHC 4Ms93g93PkA2SDZ P19zYouaeerg6iT ScxPXuiZXbC2pZ. ENDSLATEPACK. \-------------- CUT ABOVE THIS LINE -------------- Command 'contract' completed successfully ``` Wallet 2: ``` ./grin-wallet --testnet contract sign --receive=1 Password: Paste slatepack: BEGINSLATEPACK. 3pDmAZBPAaFKxhX Hhi1beNF3pCpmpY ugZNstfhxHzQtrZ zA9HUtMTgbXmUa6 FHQAqRSa3U1fwbu D3iaiYSPLT1hjTE qGMm2rdsVyBofM6 cp6ZDe7Lm3bEm2b 7jmdrzGyfPSTNrL fWrceZbM7rKFo59 bST38KxMXginKca Y7JcQbrJoETKc2W WY6vNTWzfg9QJBt PyDUZhzmMP9KYWT ECjhaagFWtxxfKw pTPMUxgQX6kdbGx NnfuJavCv658VAR ka9upRnBD3ti5MP 27iXnvFYZEpgHJc 4UQF4PutVPdBt2r pXTQ3dRx4bAmDAk j4RG9Y4wMv2h5sc XTKHJP8pHVZGk9n vqeYQWNEK5reqUX rtK4oyA63wCmq9D r75BTjwPn9vdqma eeb9oazDpALNDCn XtguxrSwoPn7coM iCUdCvGKeigZ3rw SokXdb7x8L6x7Ej 3QimTEkg9DoJFe6 FJsEGG5dFQMfzBK 9nEHGvaLt5c2MT3 MBd1FMi9p1fMGmm r7B7bNCMMqpZm6c 7Vfc4F7T4AFRyvF WFbgzGJsafYvfNq oLfZ4vfBquVBaW3 DFsKRBMXnvaA1xy n2L1MqziRyEzGSU BRtmt4xeU3jFtZY HnhsdryC5TdiTV3 i1G6pN6mhJdCXvW nbc51S4HV4gspJJ 3Tw7k2GTt8B4hHC 4Ms93g93PkA2SDZ P19zYouaeerg6iT ScxPXuiZXbC2pZ. ENDSLATEPACK. Wallet command failed: LibWallet Error: Sender address has not been provided ``` Same if you use `--encrypt-for=`: ``` ./grin-wallet --testnet contract sign --receive=1 --encrypt-for=tgrin1wvcfnnsf63qj27yfumukrte7nyyszndcnl4d36crg0yk0dftct3qur8d4t Password: Paste slatepack: BEGINSLATEPACK. 3pDmAZBPAaFKxhX Hhi1beNF3pCpmpY ugZNstfhxHzQtrZ zA9HUtMTgbXmUa6 FHQAqRSa3U1fwbu D3iaiYSPLT1hjTE qGMm2rdsVyBofM6 cp6ZDe7Lm3bEm2b 7jmdrzGyfPSTNrL fWrceZbM7rKFo59 bST38KxMXginKca Y7JcQbrJoETKc2W WY6vNTWzfg9QJBt PyDUZhzmMP9KYWT ECjhaagFWtxxfKw pTPMUxgQX6kdbGx NnfuJavCv658VAR ka9upRnBD3ti5MP 27iXnvFYZEpgHJc 4UQF4PutVPdBt2r pXTQ3dRx4bAmDAk j4RG9Y4wMv2h5sc XTKHJP8pHVZGk9n vqeYQWNEK5reqUX rtK4oyA63wCmq9D r75BTjwPn9vdqma eeb9oazDpALNDCn XtguxrSwoPn7coM iCUdCvGKeigZ3rw SokXdb7x8L6x7Ej 3QimTEkg9DoJFe6 FJsEGG5dFQMfzBK 9nEHGvaLt5c2MT3 MBd1FMi9p1fMGmm r7B7bNCMMqpZm6c 7Vfc4F7T4AFRyvF WFbgzGJsafYvfNq oLfZ4vfBquVBaW3 DFsKRBMXnvaA1xy n2L1MqziRyEzGSU BRtmt4xeU3jFtZY HnhsdryC5TdiTV3 i1G6pN6mhJdCXvW nbc51S4HV4gspJJ 3Tw7k2GTt8B4hHC 4Ms93g93PkA2SDZ P19zYouaeerg6iT ScxPXuiZXbC2pZ. ENDSLATEPACK. Wallet command failed: LibWallet Error: Sender address has not been provided ```

[image1190×1246 165 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/f48d0cbc411b1c1c98092ae5b0fd76cc2650314f.jpeg "image")

---

### Post by @Yeastplume ⭐ (2025-03-08)
*Post #65*

Thanks for pointing this out, happy to look this in the near future.

---

### Post by @Yeastplume ⭐ (2025-03-08)
*Post #67*

Contracts flow is still experimental, in the gui-wallet you have to select it manually to enable it, but using contract flow should enable early proof generation by default in every transaction.

---



## Venmo/Cashapp product planning
*Date: 2022-04-18 | [Forum Link](https://forum.grin.mw/t/venmo-cashapp-product-planning/9714)*
*Importance Score: 93.8 | Core Participants: tromp*

### Post by @trab (2022-04-18)
*Post #1*

I initially wrote out some ideas about using Matrix for this, in the product wishlist thread here: [Grin product wishlist - #10 by trab](https://forum.grin.mw/t/grin-product-wishlist/9704/10)

the problem with matrix is that the rooms, and room participants are known to the server admins. This makes Matrix a non-starter for this use case. At least until p2p matrix comes out (i honestly think it could be 10 years before we see p2p matrix though lol).

So this new thread is about figuring out the best stack to build this product with.

The first question is which network do we use for the message sending and username lookup. Some ideas from the top of my head are:

* A fork of Signal
* manyverse (SSB protocol)
* Session (session protocol on oxen blockchain)

Protocol | Example App | SDK(s) | Forward Secrecy?
---|---|---|---
[Reticulum](https://unsigned.io/projects/reticulum/) | [Sideband](https://unsigned.io/sideband/) | [Python](https://github.com/markqvist/lxmf) | Yes
[Waku](https://waku.org/) | [Status](https://status.im/) | Javascript, Nim, Go | Yes
[Gun](https://github.com/amark/gun) | [Iris](https://github.com/irislib/iris-messenger) | Javascript, Rust | [No](https://github.com/irislib/iris-messenger#privacy)
[Nostr](https://github.com/fiatjaf/nostr) | [Nostr.chat](https://github.com/melvincarvalho/nostr.chat) | Javascript, Go, Rust, C# | No
[XMPP](https://github.com/fiatjaf/nostr) | [many](https://github.com/bluszcz/awesome-xmpp#clients) | [java, python, c++, lua, javascript, Objective-C](https://github.com/bluszcz/awesome-xmpp#libraries) | No
[Matrix](https://github.com/matrix-org) | [many](https://matrix.org/clients/) | [almost all](https://matrix.org/sdks/) | No
[Hypercore](https://hypercore-protocol.org/) |  [hyper-web-chat](https://github.com/lanmower/hyper-web-chat) / [p2p multiwriter with autobase](https://github.com/hypercore-protocol/p2p-multiwriter-with-autobase) | javascript | No
[libp2p](https://libp2p.io/) | [Berty](https://github.com/berty/berty) | [javascript, go, rust](https://libp2p.io/implementations/) | Yes
[yggdrasil](https://yggdrasil-network.github.io/) | [sprig (arborchat)](https://man.sr.ht/~whereswaldon/arborchat/) | [go](https://github.com/yggdrasil-network/yggdrasil-go) | ?

i will do a closer comparison of all these options in the near future. If someone else wants to join in, please feel free! i am probably forgetting some messaging options too. but i think we have to go with something more p2p ish where the server admins don’t have total control of accounts. so that excludes xmpp and matrix afaik.

Edit: adding a table

---

### Post by @tromp ⭐ (2022-04-18)
*Post #3*

There’s also The Mesh:

[mathmesh.com](https://mathmesh.com/Documents/draft-hallambaker-mesh-architecture.html)

### [Mathematical Mesh 3.0 Part I: Architecture Guide](https://mathmesh.com/Documents/draft-hallambaker-mesh-architecture.html)

The Mathematical Mesh 'The Mesh' is an end-to-end secure infrastructure that makes computers easier to use by making them more secure. The Mesh provides a set of protocol and cryptographic building blocks that enable encrypted data stored in the...

---

### Post by @tromp ⭐ (2022-04-19)
*Post #6*

My experience of The Mesh is limited to seeing it discussed on the cryptography mailing list [1], e.g. recently in [2].

[1] [cryptography](https://www.mail-archive.com/cryptography@metzdowd.com/info.html)

[2] [[Cryptography] A payment scheme for the Mesh](https://www.metzdowd.com/pipermail/cryptography/2022-April/037787.html)

---

### Post by @JasperKai (2023-02-28)
*Post #23*

Using Nostr addresses for Grin transactions seems to be a good choice, Ironbelly is doing a great job, looking forward to experience it soon.

[twitter.com](https://twitter.com/ironbellywallet/status/1630009566560747520?t=pmTbGUfxJ8rfRPri61OeKA&s=19)

#### [Ironbelly - Grin mobile wallet](https://twitter.com/ironbellywallet/status/1630009566560747520?t=pmTbGUfxJ8rfRPri61OeKA&s=19)

[@ironbellywallet](https://twitter.com/ironbellywallet/status/1630009566560747520?t=pmTbGUfxJ8rfRPri61OeKA&s=19)

Just some tinkering with [#Nostr](https://twitter.com/search?q=%23Nostr) 🙃 [#grin](https://twitter.com/search?q=%23grin) [#ironbelly](https://twitter.com/search?q=%23ironbelly) <https://t.co/bBbVYtxBs6>

[12:58 AM - 27 Feb 2023](https://twitter.com/ironbellywallet/status/1630009566560747520?t=pmTbGUfxJ8rfRPri61OeKA&s=19) 50  15

---

### Post by @trab (2023-03-21)
*Post #32*

Since [Python Mimblewimble](https://github.com/grinventions/mimblewimble-py#srs-transaction-building) has been released, someone can combine it with [Python Nostr](https://github.com/jeffthibault/python-nostr)

Maybe even use [Pyncone](https://github.com/pynecone-io/pynecone) for a front end!

---

### Post by @Anynomous (2024-07-12)
*Post #43*

Reopening this discussion and answering [my own question from this thread](https://forum.grin.mw/t/suggestion-make-dex-gate-io-is-over/10713/66).

**As I understand it: What makes Venmo and others like CashApp successful?:**

1. A **contact book and user IDs**. When joining Venmo you can import your contacts and get your own Venmo ID. Not something I would recommend for Grin to do, but instead we could use integration with Nostr, you can import people their Nostr IDs. Also, nothing is stopping users from sharing QR codes with a payment request or offering to pay a contract via other media such as Signal. That is basically what I do with a local payment APP in my country for easy bill splitting. This is done via sharing a link/IRI that goes to a central server which triggers opening of the Venmo APP. Perhaps we can use the **[deeplink-system](https://www.yeeply.com/en/blog/mobile-app-development/deep-linking-android-ios-apps/)** that allows opening of a wallet APP from a Grin QR payment request qr code. Using depplinks should trigger opening of the wallet APP independent from which media channel is used since the URI/IRI as link or as QR-code triggers the opening of the wallet AP via the browser.
2. _**Payment requests**_ & _**Payment offers**_ and **bill splitting**. I see this matches quite nicely with terminology from contract flow payments. Splitting of a bill to keep track of who paid a ticket and who did not might require a bit of extra wrapper metadata which touches on many discussion we had on putting slatepacks in an optional wrappers that can contain extra metadata. By including some extra metadata like payment request ID and user ID, it should be very easy to keep track of transactions that belong to a single split bill. As long as the content is encrypted for the receiver, their should be no information leakage when including extra metadata.
3. **Exchange integration**? Topping up and easy on an off ramping of Grin might be what makes Venmo easy. Not sure if this is possible, it is not something we can direct but who knows, maybe TO is interested or Gate if we have a good wallet to support it.
4. **International payments**. Venmo is from PayPal and such allows easy micropayments internationally although they take 0-3% fee on those payments via Venmo 0-5% for PayPall international payments. Grin does not have that problem at al, so potentially would be better as long as you keep your Grin as Grin.
5. **Mass adoption** and acceptance… and that is something not so easy achieve. Even with the best designed APP and with exchange integration, the main bottleneck of any crypto currency is that not many people are willing to accept it. But then again, perhaps a great wallet APP might speed up adoption considerably.

[@trab](/u/trab) Anything I missed or got wrong? I based the information on what I could find out about Venmo online, I never used the APP.

Can anyone check how split bills work? I scanned a few online Venmo example QR codes, they only contain user ID’s, but I want to know what else they might include, such as amount in a split bill request, perhaps a request ID etc.

The biggest question remains if any developer is interested in implementing some or all of such features in their wallet. We can envision, plan, support as CC and as community, but only developers have the power to make visions a reality  [@i1skn](/u/i1skn) [@davidtavarez](/u/davidtavarez) [@ardocrat](/u/ardocrat), does this anyway align with what you vision is for the wallets you work on for now or in the future?

---

### Post by @trab (2025-06-20)
*Post #82*

Lightning compared to Venmo. <https://x.com/layertwolabs/status/1936072045210542146>

How does Grin compare?

Grin is:

* slower
* more prone to catastrophic loss of funds
* infinitely more cumbersome unless used custodially
* less private
* in practice, as custodial
* introduces meta complexity to users via taxable events
* in many cases, not even using Bitcoin❌

Ok so Grin is slower than venmo and has the same potential with loss of funds as Lightning I guess (both interactive though).

Other than that, Grin is on-chain and the main chain has privacy. So there’s those benefits.

What’s the real data on speed of interactive transactions?

---



## Gri̇n i̇s di̇sappeari̇ng
*Date: 2022-06-06 | [Forum Link](https://forum.grin.mw/t/gri-n-i-s-di-sappeari-ng/9820)*
*Importance Score: 119.7 | Core Participants: tromp, davidtavarez*

### Post by @GrinTurkey (2022-06-06)
*Post #1*

Dear community, I have been following the forum and developments closely for a long time. Is there a problem in the community? David burket left, Jihad (Minexpert) left. There are limited developments. and this is what caught our attention, both the investor and us. The feeling that good things will not happen for the future in the community is overwhelming.Yes, no one lives with the dream of getting rich all of a sudden. But I know people who bought Grin for a very high price. These people may not matter to you, but it is an important issue for me and people who think like me.You are happy when you receive a few BTC donations, but you do nothing for the investor. You don’t make statements that give them hope. All the developers do is argue here.
I’m sorry to say this, but now listen to people. End the discussion in the community. This project did not appear for a few, but for all humanity.

---

### Post by @davidtavarez ⭐ (2022-06-07)
*Post #10*

Ignoring why people left the project is doing more harm than good, and unfortunately it won’t change because their pride has blinded them. Sad but true.

---

### Post by @davidtavarez ⭐ (2022-06-07)
*Post #13*

Some people left because for whatever reason, the OC hijacked Grin, at one point it was something like: “do what we want or fork Grin.” There was no incentive to write any RFC because the proposal was going to be ignored no matter what. Yes, the environment was very hostile, yes, I can now recognize a lot of injustice, and today I could understand the OC’s attitude or reaction, but the truth has to be said, that in addition to the hostile environment plus the lack of interest in actually creating a good product, it was destroying Grin and if we keep ignoring it, Grin will disappear, and sadly some people won’t care at all.

---

### Post by @davidtavarez ⭐ (2022-06-07)
*Post #18*

[@Anynomous](/u/anynomous) [@vegycslol](/u/vegycslol) [@oryhp](/u/oryhp) you are actually proving my point right now. I also believe that **good calls were made** in regards of NITX specially, **I am more and more in favor of interactive transactions**. The fact that I am in favor of the interactive transactions and a minimalist approach, it does not mean that I will forget that Kurt, Burkett, gary, Guy and others, were treated badly and/or just ignored.

oryhp:

> The OC was _protecting_ Grin, but very few community members had a deep protocol knowledge needed to be able to tell this.

Like I said, I am not judging, and again, I agree that good calls were made.

oryhp:

> The OC and the community actually reacted very poorly. The situation back then was relatively transparent/obvious along with the consequences, but everyone was focused on picking a side and playing a vigilante against OC rather than trying to understand why there were different opinions

The OC stopped interacting with everyone, what do you think was going to happen? what had to happen happened: they lost the Community’s trust, and it is unfortunate because we had very capable contributors, but **no one will put a penny or a second behind a team that no one trusts**.

Who among you has spent at least an hour supporting users? Who among you interacts with users? Yes, with those users who don’t understand the protocol.

How do you then prioritize the problems to solve if you don’t even know what the users are dealing with? Is that how you make a good product?

I have shared many times on Keybase direct feedback from the few exchanges that list Grin, what did we do with that?

How are you going to build a product for people you don’t even listen to, because you’re smarter than them?

**That attitude is nothing more but pride** , and no, just because you think you’re the smartest kid on the block doesn’t mean you’re building a good product. You have to get involved, you have to observe and understand how people are using your product, you have to understand what problems they are facing, including Exchanges, and make the correct trade-offs. But you don’t, sorry, but you don’t.

We need the Community support, we need the support of those who put their real world money mining Grin, for example. We need the support of those who are interacting with Exchanges. I am not saying that we should let moonboys change the protocol, but people losing money trading Grin are the one who push the few Exchanges to support Grin.

oryhp:

> You should know best that making Grin easy to use is a very hard task and thus creating a good product is as well.

Yes, I am well aware of that. The Slatepack RFC is just beautiful. One of the last suggestions Burkett made on Keybase was to deprecate the RSR flow, which nobody, I’ll say it again: nobody is using. But it is ignore, why? because it’s always a fight of opinions instead of asking what’s best for Grin.

What do you think will happen when you only engage in conversations about things you already agree on? If you don’t know, let me tell you that you will lose support. So, in the future, when you share a proposal, those you ignored then will simply ignore you. How does this help Grin’s development?

I get a notification on my phone every time someone asks something about Grin++ in the Telegram support channel since 2019, I try to share what we have learned from that and from Exchanges as well, and I don’t see this influencing Grin one way or another.

Don’t get me wrong, the more I get involved, the more respect I have for all the current and past contributors and developers. What I’m saying is, yes, let’s ignore the moonboys, keep building our uniqueness and keep trying to unleash the full potential of the minimalist approach and interactive transactions. But we must also grow and learn from the mistakes of the past.

---

### Post by @davidtavarez ⭐ (2022-06-07)
*Post #27*

Anynomous:

> I hope we do so. Indeed many past discussion were to much about ‘who is right’ opposed to just agreeing to disagree

It is hard for me to believe we are learning something other than the less toxic is the environment the easier is to contribute. I will give you an example. Let’s take a look into the [Coinswap Implementation](https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149) request.

I warned:

> How can we mitigate the consequences of you disappearing in the middle to the process? simple: we need to make sure anyone could finish your work if you disappear.

Also me:

> Look at the PIBD work, we ended up without neither an implementation nor a RFC nor even a work-in-progress Pull Request. In advance or not, for me that is irrelevant if we can’t find a way to get this thing, or anything else, done. It is not hard to understand. Do we want to be in the same position again where we are left with nothing? I think we don’t.

And what we have today? neither the implementation nor a documentation to [complete the work](https://github.com/mimblewimble/mwixnet/pull/3). We are in the same weaken position that I warned about and wanted to prevent. It happened on the first attempt of the Atomic Swap (from Jasper), it happened with the PIBD work, it happens on the second attempt of the Atomic Swap, and now it looks like it already happened again in regards of the Coinswap Implementation.

It is fair to say that we should re-think how we approach these things. The main reason we need clear and well explained documentation is for security, to make sure that no exploits are introduced into Grin source code, but the second reason, and especially important to us, is because we need to make sure that anyone can complete any pending work.

vegycslol:

> It’s easy to spot problems but hard to find good solutions for them and it takes time to implement them (especially with our currently limited dev resources).

Protocol related topics are the core so to say, but Grin as a project is broader than that.

I swear I don’t want to be the pessimist here, but if you put yourself in the shoes of joe normie you can understand why an outsider might come to the conclusion that Grin is a dead project, and throwing out the popular cards - “it’s fomo”, “you’re a bot”, “you don’t understand the protocol”, etc., etc. won’t help… what joe normie sees is years without any significant improvement. Is joe normie unaware of the Grin protocol? Yes, but joe normie is not so dump as to ignore what’s in front of this face.

vegycslol:

> What would you have done differently?

I’m glad you asked. I would have prioritized the reported problem that prevented one of the Exchange from updating its nodes. I would prioritize fixing the problem of the wallet stopping communicating with the node, and the problem of the nodes being out of sync. Both problems also reported by one of the Exchange. I would have also prioritized the issue with the node not removing the files from the `tmp` folder. Those are 4 examples of things that I would have differently that affect the experience of people, Exchanges, solo miners, and voluntaries running public nodes.

oryhp:

> You’re talking as if they did nothing bad and were treated badly.

So let me be clear: I think past conversations became too toxic, and some comments made went outside the bounds of the civic exchange of ideas. Things were said that could easily lead to a fist fight in the offline world.

oryhp:

> Since I’m not good at that task, my approach to help on the front of making it easier to use (which is a passive support I guess?)

I do get you approach and honestly I have nothing bad to say about it, and nothing bad to say about you. I am not asking you or [@vegycslol](/u/vegycslol) to start offering support on Telegram or something, what I am trying to say is that it does no good to reject everything other than what you see from your perspective. Want an example? I’ll give you one.

I personally prefer the TradeOgre implementation using the SRS flow by manually sharing the slatepack messages. Now, TradeOgre is the only Exchange so far willing to enable an unique UX only for Grin (thanks God). The rest prefer Tor because is easier for them and easier for their users to see the grin1 address as a Bitcoin like one, for example. What do we do then? Enable non interactive transaction because of that? Hell no! I agree, but then what?

vegycslol:

> Shops/services are cases where RSR makes the most sense but why would they implement RSR in their shop if the most popular grin wallet doesn’t support them? Sadly it makes no sense to do so.

This is just you saying. You are completely ignoring everything. I will say it again, I prefer to manually share slatepack messages. That said, why do you think TradeOgre has not implemented that flow, and only TradeOgre has enabled sharing slatepack message manually?

One would think that eventually more Exchanges will list Grin when there are more economic incentives to do it, God only knows when, but let’s take it as a valid statement. **What we then should do is to make the current experience as pleasant as possible**.

JasperKai:

> grin++ is a great wallet,

Thank you.

JasperKai:

> but there is no way to use it in many places, for example in China it doesn’t work, you have to use a VPN at the same time, and only few VPNs can support it, users are torn when using it, green address or brown address? It brings an uncertainty to the user

I am working on adding a tool to help users bypass this using Tor bridges. Hang there.

Look I have nothing against you [@oryhp](/u/oryhp) (or anyone really) I actually appreciate your constant contribution. I am not trying to divide. I want Grin to succeed.

---

### Post by @davidtavarez ⭐ (2022-06-07)
*Post #29*

vegycslol:

> Yes it makes sense, i kind of understand the protocol and still think grin will remain “dead” for the next few years. It just needs to fix existing issues and implement the right features for when inflation becomes low enough for people to speculate and hodl.

Yes! That’s what I’m trying to say

vegycslol:

> What am i ignoring? That’s what I’m saying yes and if you disagree with my examples i would appreciate if you would point out the mistakes in them (mistake in SRS flow that I’ve given? maybe a mistake in RSR flow?)

I personally do not even see any mistake in your example in general. I am saying is that the exchanges are not buying the idea. That’s all and that should tell us something.

---

### Post by @davidtavarez ⭐ (2022-06-09)
*Post #36*

trab:

> My area of interest is more on UX and products. I don’t know much about the core code. But I do want to learn. Sometimes I wonder if it could be beneficial for an expert in the core code to simply record a Zoom call with others where they walk through the codebase and explain very clearly how it all fits together and where things are located.

Bitcoin whitepaper: <https://bitcoin.org/bitcoin.pdf>
Grin for Bitcoiners: [Grin for Bitcoiners - Grin Documentation](https://docs.grin.mw/wiki/introduction/grin-for-bitcoiners/)
MimbleWimble Origin: [MimbleWimble Origin · mimblewimble/docs Wiki · GitHub](https://github.com/mimblewimble/docs/wiki/MimbleWimble-Origin)
Andrew Poelstra’s Version: <https://download.wpsoftware.net/bitcoin/wizardry/mimblewimble.pdf>
Introduction to Mimblewimble and Grin: <https://github.com/mimblewimble/grin/blob/master/doc/intro.md>

MimbleWimble with Andrew Poelstra (video)

[ ](https://www.youtube.com/watch?v=aHTRlbCaUyM)

Then you could take a look to the tests written on each implementation:

[GitHub](https://github.com/mimblewimble/grin)

### [GitHub - mimblewimble/grin: Minimal implementation of the Mimblewimble protocol.](https://github.com/mimblewimble/grin)

Minimal implementation of the Mimblewimble protocol. - GitHub - mimblewimble/grin: Minimal implementation of the Mimblewimble protocol.

[GitHub](https://github.com/mimblewimble/grin-wallet)

### [GitHub - mimblewimble/grin-wallet: Grin Wallet](https://github.com/mimblewimble/grin-wallet)

Grin Wallet. Contribute to mimblewimble/grin-wallet development by creating an account on GitHub.

[GitHub](https://github.com/GrinPlusPlus/GrinPlusPlus)

### [GitHub - GrinPlusPlus/GrinPlusPlus: A C++ Grin Node & Wallet For Windows,...](https://github.com/GrinPlusPlus/GrinPlusPlus)

A C++ Grin Node & Wallet For Windows, Mac OS X, & Linux - GitHub - GrinPlusPlus/GrinPlusPlus: A C++ Grin Node & Wallet For Windows, Mac OS X, & Linux

I think Grin++ code is easier to understand.

I also suggest to start practicing everything you learn using a simple programming language like Python or C#. If you are completely new try to take several online courses on Blockchain, there are few good ones which are also free.

You could also start contributing with something. Fork the repo of preference and start fixing small things, or pick reported issues and fix them. If you are interested on UX you could design an UI and ask for feedback here. If you like to code, Grin++ UI is written in TypeScript using React and Electron.

It is clear that there is enough resources available, you just need to invest your own time.

---

### Post by @davidtavarez ⭐ (2022-06-09)
*Post #49*

trab:

> To me, what is needed is not backend Rust experts. What is needed is actually React developers. Flutter developers. Front-end _Designers_.

You know Grin++ UI is written in ReactJs right? What is stopping you to contribute? Also IronBerry is written in React Native, what is stopping you to contribute?

trab:

> If the person with the design sensibilities also needs to dive into core Grin rust code, well that certainly limits the potential contributors to a huge degree.

You are not understanding anything, mate, or just ignoring it to keep asking for a SDK, why don’t you write one with Javascript? What is stopping you?

I’m done with people **asking** , no one is stopping anyone to do anything. Grin have only 2 people writing code and here you are “asking for a SDK”, this is simply insulting. No one is stopping you of using Figma or whatever to start designing a UI, why are you not doing that?

By the way UX is not equal than UI.

---



## Grin Bulletin Board: Discussing four options and select one for bounty
*Date: 2022-06-07 | [Forum Link](https://forum.grin.mw/t/grin-bulletin-board-discussing-four-options-and-select-one-for-bounty/9822)*
*Importance Score: 75.5 | Core Participants: tromp*

### Post by @Anynomous (2022-06-07)
*Post #1*

In the Community Council meeting of today we discussed the possibility of introducing a Bulletin Board system for Grin as sugested by [@satoshocrat](/u/satoshocrat). The purpose of a Bulleting board is for users to be able to share information while they are offline. These are not non interactive transactions, but are a solution that allows those users who do not like having their wallet online, or those who do not like to share their slatepacks via email or other known channels, to share that information.

The object is to a) all read up, compare these three solutions and possibly suggest others, and b) to create a bounty for implementing a well documented bare bone implementation for such a system.
This can initially be a centralized solution, but should in design allow decentralization, e.g. users should be able to deploy their own bulletin board server.

The three solutions at hand are:

1. SBBS system, similar to what BEAM has implemented.
[Secure bulletin board system (SBBS) · BeamMW/beam Wiki · GitHub](https://github.com/BeammW/beam/wiki/Secure-bulletin-board-system-\(SBBS\))
2. GrinBox. A system Grin had in the past to relay transaction slates
[GitHub - vault713/grinbox: Relay service for interactive transaction building for Grin / Mimblewimble](https://github.com/vault713/grinbox)
3. Contract wall, a spam free way for users to share data
[contract_wall.md · GitHub](https://gist.github.com/phyro/1046022377fcb1886a1b4f6500f23773)
4. [Proposal: A decentralized transaction BBS using a merge-mined sidechain](https://forum.grin.mw/t/proposal-a-decentralized-transaction-bbs-using-a-merge-mined-sidechain/9870)
5. [Slate store](https://github.com/grinventions/ideas/blob/main/SlateStore.md), an interactive transaction relay system.
6. [Buddy System](https://anynomouss.github.io/grin-for-muggles/transaction_buddy_system.html): A relay buddy system with send and forget functionality for the sender.

---

### Post by @satoshocrat (2022-06-07)
*Post #2*

Love it! I want to thank all involved for taking up this matter swiftly. I believe it will help forge both optimism within the active user-base, and long-needed progress on the usability front.

One question I did have, as to the DDOS/Spam attack vector: why couldn’t the hosted nodes or box or relay, extract a fee as well? Perhaps from both parties as a storage / processing fee to mitigate the bloat and spam?

NVM - I like [@oryhp](/u/oryhp)’s - this is precisely what I was thinking as well.

[ image1492×579 114 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6dd935b23d3365b6c59a905ea83bc8c234fde6cb.png "image")

---

### Post by @coolwhip (2022-06-08)
*Post #5*

Has anyone considered a DHT solution, like how Tari shares its MimbleWimble TX messages?

[tari.com](https://www.tari.com/lessons/02_how_tari_works.html)

### [Tari](https://www.tari.com/lessons/02_how_tari_works.html)

The protocol for digital assets

DHT seems to check the following boxes:

* decentralized
* spam resistant
* scalable

Without compromising on privacy & security. They even packaged this aa a stand alone Rust library, so it may be an “easy” integration:

[Lib.rs – 3 Feb 21](https://lib.rs/crates/tari_comms_dht "12:00AM - 03 February 2021")

### [tari_comms_dht](https://lib.rs/crates/tari_comms_dht)

Tari comms DHT module

---

### Post by @trab (2022-06-09)
*Post #13*

My concern is that bundling a solution _with_ Grin will discourage others from developing truly awesome messaging systems with Grin.

For example, why would anyone build a Signal type messenger with Slatepack sending functionality when the SBBS “is good enough”. And wouldn’t the Signal type app then kinda be overlapping in functionality?

We should keep in mind two things:

1. as with Python, the standard library is where projects go to die

2. the pain of not having something can be a stronger motivator than having a “good enough” solution that could be a bit cooler

---

### Post by @Anynomous (2024-05-07)
*Post #34*

Having 4 systems to chose from is hard,… so lets add another to make things even more confusing:upside_down_face: .

I want to share a very loosely designed transaction **“Buddy System”** . The idea is that you can have a buddy who handles the transaction for you, functioning as a **Relay/Intermediary**. This relay requires your signature to finish the transaction and get his reward, which is a modest relay fee. The proposed solution has some advantages, such as being an Aggregation of a regular **RSR** and **SRS** transactions, not requiring side chains, merged mining or much code. The system also has some downsides, such as the Relay knowing who sends to who, although an extra tor address could provide extra anonymity there. Also this idea requires some transaction information wrapper around a slatepack address to define this alternative transaction method.
To be very clear:
**1) I am not a cryptographer**
**2) I am not advocating this solution should ever see the light of day**

I designed/explored this solution for fun since I believe there is a wide range of use cases and possibilities using interactive crypto that are worth it to be further explored. Grin is amazing in that transactions can be aggregated at so many levels, this is just one example of an application where aggregation can be interesting.,

Grin is working as it is and I am not convinced any formal transaction relay system or Bulletin Board System is needed. Perhaps integration with Nostr or Signal on the individual wallet level would be more important as proposed by [@trab](/u/trab). This does not however mean we should not continue exploring solutions like the **Buddy System** presented here. I think there are uses cases for using _cut-through_ for aggregating transaction before they hit the chain. Sharing ideas like this one might helps keep everyone open-minded and creative and lead to new cool crypto solutions one day… that is why I share this concept idea.
If you are interested, give the transaction “Buddy System” a read  .
[Grin for muggles and aspiring wizards](https://anynomouss.github.io/grin-for-muggles/transaction_buddy_system.html) [[github](https://github.com/Anynomouss/grin-for-muggles/blob/main/transaction_buddy_system.md)]

---

### Post by @tromp ⭐ (2024-05-07)
*Post #35*

Anynomous:

>   0. Alice contacts Charlie over tor, but Charlie is offline 1) Alice send a **request** to Bob, the intermediary/_relay-buddy_ .
>

In what situation would Alice want to make a payment to Bob without having any means of communication with Bob?
I.e. no email/keybase/telegram/github/facebook/whatsapp/reddit/grin forum that could be used to send slatepacks back and forth?

How is Alice communicating with Bob, and how is Bob communicating with Charlie?

---

### Post by @tromp ⭐ (2024-05-07)
*Post #37*

Another question: if Alice can communicate with Bob, and Bob with Charlie, why does Bob have to do any transacting? Can’t he just relay Alice’s slatepack to Bob once Bob comes online, and similarly relay Charlie’s response slatepack back to Alice once Alice comes back online?

---

### Post by @tromp ⭐ (2024-05-08)
*Post #39*

Anynomous:

> The main advantage is that Alice does not need to stay online

She doesn’t have to stay online when using
email/keybase/messenger/telegram/github/facebook/whatsapp/reddit/grin forum either. All these services are already available to relay messages between users that are only occasionally online. And they don’t charge a fee.

And in many cases they are the medium in which Alice and Bob agreed on a need for payment in the first place?!

---



## Grin is dead? Or not?
*Date: 2022-06-30 | [Forum Link](https://forum.grin.mw/t/grin-is-dead-or-not/9896)*
*Importance Score: 72.7 | Core Participants: tromp, davidtavarez*

### Post by @Unclefek (2022-06-30)
*Post #1*

Hi all. Please tell me, does it make sense to buy today, in 2022, asic, ipollo G1 for Green mining or is the project already dead?

---

### Post by @Anynomous (2022-06-30)
*Post #3*

Unclefek:

> does it make sense to buy today, in 2022, asic, ipollo G1 for Green mining

G1 Mini prices are low, but indeed with current price its a gamble on the price. 2023 it is likeley new Asics will hit the market, early buying one of those is a safer bet byt probably more expensive gamble.

Regarding dead or alive projects, indeed make of it what you want. Plenty of things going on in Grin on forum and keybase and plenty going on in development.

---

### Post by @renzokuken (2022-07-26)
*Post #11*

It is dead until I get my 100K ツ, after that I don’t mind if people notice its true value.

---

### Post by @Unclefek (2022-08-04)
*Post #16*

Hi everyone! please tell me what is the reason for the increase in complexity right now, during the bear market? looking at the annual complexity of the network, it was quite high from September last year to May this year. hence income was half what it is today. for example: having one G1 ASIC today, it brings $21 at the moment, it turns out that with a complexity of 400M it will be $10? right? then it turns out there are no guarantees that tomorrow the complexity of the network will not skyrocket and mining will only bring disappointment? or am I wrong? strange why the difficulty goes up in a bear market?

---

### Post by @tromp ⭐ (2022-08-05)
*Post #18*

There is no complexity in Grin PoW. Only difficulty…

---

### Post by @Mattczt (2022-08-21)
*Post #20*

[Is C32 Grin's final PoW update?](https://forum.grin.mw/t/is-c32-grins-final-pow-update/9530/2)

> [Is C32 Grin's final PoW update?](https://forum.grin.mw/t/is-c32-grins-final-pow-update/9530/1)
>
>> C32 is only PoW for now and near future.
>
> Not quite correct. Grin’s Pow since the last hardfork is Cuckatoo32+.
>
> That means that it accepts all of C32, C33, C34, … up to C63.
>  But of course C32 is the preferred choice since C33+ puts much higher demands on mining hardware and software, and we may never see ASICs supporting C33…

C32 asics are not going to get bricked.

---

### Post by @tromp ⭐ (2022-08-27)
*Post #24*

Unclefek:

> there will always be only C32

Not quite correct; Grin’s PoW is C32+, which includes C32, C33, C34, … C63. But I expect ASICs will only ever target C32.

---



## "Contract" terminology - a dissenting opinion
*Date: 2022-07-06 | [Forum Link](https://forum.grin.mw/t/contract-terminology-a-dissenting-opinion/9915)*
*Importance Score: 73.6 | Core Participants: tromp, davidtavarez*

### Post by @Trinitron (2022-07-06)
*Post #1*

I am writing this post to disagree with the proposed use of the term “contract” for transactions or anything else in Grin.

I don’t think it is so important that it will affect the success of grin, and I am confident that even if this “contract” terminology is adopted and then Grin does become popular it will eventually be ripped out in any case because of how inapplicable it is.

The OED definition of contract is:

> a written or spoken agreement, especially one concerning employment, sales, or tenancy, that is intended to be enforceable by law.

The Wikipedia article for contract begins with:

> A contract is a legally enforceable agreement that creates, defines, and governs mutual rights and obligations among its parties. A contract typically involves the transfer of goods, services, money, or a promise to transfer any of those at a future date.

My disagreement with contract being an applicable term is a gut reaction first, the term simply isn’t applicable to Grin’s functionality. I have to pick apart my gut reaction to try to turn it into a logical argument.

1. Mutuality. A contract is basically always used to define a two way agreement. Goods for money, money for services, money for money. On at least one side of a contract is always an _obligation_ , it is an agreement to fulfill something. Grin specifically only contains transactions of money, it does not contain goods, services, or any obligation beyond the transaction of money. No one ever signs a contract in real life that simply says “I will pay you X” without defining an obligation in return.

2. Nonexistent complexity. Say that I am buying a donut and I would like to pay in Grin. There is no practical basis, _especially to a layman,_ to imply that a contract is involved in any way. It is a direct exchange of payment for donut without any outstanding obligations created. Even if you were to complicate it by paying for the donut with a check (or cheque) that involved two party signatures, nobody would ever bring the word “contract” into this exchange. It is called a transaction.

[Bike_shed_15d06_cropped1796×715 328 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e1e1f8e16c35876d4101517081839b40fc6fcb48.jpeg "Bike_shed_15d06_cropped")

---

### Post by @tromp ⭐ (2022-07-06)
*Post #4*

Trinitron:

> No one ever signs a contract in real life that simply says “I will pay you X” without defining an obligation in return.

And Grin payments are no different. They will nearly always be payments for something (donations excepted). Which is exactly what payment proofs are for. They state the purpose of payment so that the payer has some recourse when the payment recipient fails to hold up their end of the bargain. Which, by signing the contract, the receiver has committed to.

Most people would agree that increased use of payment proofs is a good thing for Grin. And if use of the term contract helps incentivize that, then I’m all for it.

---

### Post by @davidtavarez ⭐ (2022-07-08)
*Post #48*

vegycslol:

> i think sign is more appropriate than accept/complete

I also think “sign” might be more technically appropriate… but hear me out, please… think of it this way… the initial slate is actually a **draft** , which is a **preliminary version of a transaction** proposal; this proposal is sent to the recipient, the recipient then can decline or accept the proposal by adding their signature; the sender receives the signed transaction, adds their signature completing the transaction.

vegycslol:

> easier to explain safe-cancel

I am not sure… my focus is on **what it means** to add the signature… from the recipient perspective adding their signature means **accepting** the proposal, but from the sender perspective means **completing** the transaction, what do you think?

The ability to accept or reject a transaction is why I am in favor of [Manual Confirmation](https://github.com/davidtavarez/grin-rfcs/blob/manual-confirmation/text/0000-manual-confirmation.md), but that’s another topic.

---

### Post by @davidtavarez ⭐ (2022-07-08)
*Post #55*

vegycslol:

> i’m not a native speaker so my understanding of draft was limited. I’ve come across draft in emails etc, so as an unfinished thing only. Maybe my english is not good enough but i doubt non-native speakers will understand draft the way you want it

Me neither, I am not a native english speaker. But let me add more context so that you guys can understand what I am basing this on.

I do not know if you are familiar with heuristic evaluation; a heuristic evaluation helps to identify usability issues. **Jakob Nielsen** is considered the “king of usability”, and there is a list of **10 Usability heuristics** by Nielsen. These are used by UI/UX teams all around the world, and they are the next:

1. **Visibility of system status**.
The system should always keep users informed about what is going on, through appropriate feedback within reasonable time.

I think a “**draft** ” command is self explanatory of what is happening. When the status code of the slate is `S1` the slate is actually a draft that includes the sender’s inputs and change output; you are intentionally producing something (_a transaction proposal_) that will incorporate a result (_a transaction_).

I like “**accept** ” because it means literally that: the recipient can either **accept** or **just ignore** (_a sub action_) the draft. If the recipient accepts, their signature is added to the the draft and the status code of the slate is now `S2`, where the recipient has created their outputs(s) and supplied their excess, nonce and partial signature, ready to return to recipient for completion.

When the transaction is “finalized”, the status code is `S3` which means that the slate is now complete, contains all inputs, outputs and final signatures, and is ready for posting. That’s why I think “**complete** ” fits better here.

If you are not convinced yet you might be saying now: “sign - sign could be also use here”… keep reading please.

2. **Match between system and the real world**.
The system should speak the users’ language, with words, phrases and concepts familiar to the user, rather than system-oriented terms. Follow real-world conventions, making information appear in a natural and logical manner.

My first contra against “Signing” or “Sign” is that when the recipient accepts the transaction draft it is doing more than just adding their signature therefore “Sign” is not completely true. Also “Sign” is used in different contexts in the real world, making the word too subjective.

3. **User control and freedom**.
Users often choose system functions by mistake and will need a clearly marked “emergency exit” to leave the unwanted state without having to go through an extended dialogue. Support undo and redo.

This is something that I think is indirectly related but still important. I think transaction drafts should be accepted manually by default, I think it’s more natural. But in the context of slatepack, the command can be named as “accept” and when the command is called users paste the slatepack message and the wallet should display the transaction information. After reviewing the information, the recipient then confirms that they accept the proposed draft.

The sender call “complete” and also review now the almost finished draft and if everything is OK then the sender “finalizes” or completes the transaction.

I do not see how “Sign - Sign” fits here.

4. **Consistency and standards**.
Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow conventions.

This is my last argument against “Sign - Sign”. Besides not being self-explanatory of what is going on (please read more about [status codes](https://docs.grin.mw/wiki/transactions/slates/#status-codes)), also from the receiver’s point of view, “sign” means one thing, but from the sender’s point of view it is something else. “Sign” becomes **inconsistent**.

5. **Error prevention**.
Even better than good error messages is a careful design which prevents a problem from occurring in the first place. Either eliminate error-prone conditions or check for them and present users with a confirmation option before they commit to the action.

6. **Recognition rather than recall**.
Minimize the user’s memory load by making objects, actions, and options visible.

7. **Flexibility and efficiency of use**.
Allow users to tailor frequent actions.

8. **Aesthetic and minimalist design**.
Every extra unit of information in a dialogue competes with the relevant units of information and diminishes their relative visibility.

9. **Help users recognize, diagnose, and recover from errors**.
Error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution.

This is applicable because by using more generic words we could be more explicit in explaining to users if something goes wrong in any of the steps of the transaction building process. It cannot be “Sign” because in both cases there is something else going on besides “signing”.

10. **Help and documentation**.
Information should be easy to search, focused on the user’s task, list concrete steps to be carried out, and not be too large.

Explaining the interactivity process like this feels more natural:

First, the sender creates a draft of the transaction. Next, this draft is reviewed by the recipient, when the recipient accepts the draft, the draft with the required information from the recipient is sent back to the sender and the sender completes the transaction and publishes the transaction on the network.

---

### Post by @davidtavarez ⭐ (2022-07-08)
*Post #61*

tromp:

> For consistency then, a separate broadcast button/action can be added.

True, but I don’t think we want to separate those steps in practice. We currently call the last step “finalize,” but I think “complete” or “completar” (in Spanish) is more in line with what the last step really means. It should be a trade-off, I don’t believe those 10 principles are the 10 Commandments, but I have seen these principles put into practice and the results are surprisingly positive.

Trinitron:

> Oh but I see your idea doesn’t include the repeated command. It’s not draft new, draft accept, draft complete, etc.

Let me be more specific.

Sender creates the transaction:

$ grin-wallet transaction draft

(the output is an incomplete slate or draft)

Recipient accepts the transaction:

$ grin-wallet transaction accept

(the input here is an incomplete slate or draft)
(the output is a partially signed transaction, is not a draft because it is “reviewed” and then “accepted”)

Sender completes the transaction:

$ grin-wallet transaction complete

(the input is a partially signed transaction)

In the last step the transaction is finalized or “completed”, which means “signed by sender **and** broadcasted”.

This could be also well translated into a GUI based on a more intuitive API. If [SRS and RSR is unified](https://forum.grin.mw/t/grin-wallet-contract-prototype/9745) this also applies. Then we could have one single consistent flow: Draft - Accept - Complete or DAC.

---

### Post by @tromp ⭐ (2022-07-09)
*Post #64*

We could also let naming be guided be more general n party transactions. In that case, the simplest slate flow is a forward pass followed by a backward pass

party1 → party2 → … → partyN → partyN-1 → … → party 1

and the steps could be called

new → addkey1 → addkey2 → … → addkeyN → signkeyN → … → signkey1 → broadcast

(one could also designate the relay of a slate to the next party as a separate step).
new and addkey1 are both done by party1 and would thus be joined, as are addkeyN and signkeyN, and signkey1 and broadcast.
Thus we end up with 2*N-1 steps:

new_addkey1 → … → addkeyN-1 → … → addsignkeyN → signkeyN-1 → … → signkey2 → signkey1broadcast

In the simple case of 2 parties, this becomes the 3 steps

new_addkey1 → addsignkey2 → signkey1broadcast

Now, if you name these Draft, Accept and Complete, does that mean the general case is named

Draft → Accept2 → … → AcceptN-1 → CompleteN → … → Complete1 ?

That would violate the principle of the same name denoting the same steps.

---

### Post by @davidtavarez ⭐ (2022-07-09)
*Post #67*

Anynomous:

> But hold on, why is no else using the word “Sign” than if it is so universal? Well, they are. If you ever signed a transaction in Electrum, the steps are as follows. You import a .psbt file or psbt text (sounds familiar right, very similar to transaction slates) and you click the…wait for it… …**“Sign button”**

Why you guys think bringing Electrum is making you any favors? In fact, it’s the opposite. Electrum’s popularity is based on longevity, its first commit was in November 2011 and then Bitcoin forks continued reusing the same code base; from the pool of wallets out there the worst option to pick is Electrum in terms of UX/UI. if you want to look into the future of usability look at DEXes, like SundaeSwap, ShushiSwap, 1inch, MetaMask, etc., the way these guys hid all the complexity behind a nice looking and easy to use interface is a total win. By bringing the CLI or Electrum is actually proving my point: **you guys are too much focused on technicalities** , and that focus is not doing you any favor in terms of usability.

Anynomous:

> So keep in mind that Bitcoin uses a “Sign” button for any transaction that involves more than 1 signature.

What **Bitcoin** decided to use **is irrelevant** , no importante, mi amigo. I mentioned this many times. In general, people are not understanding what is the slatepack address used for. I don’t remember how many times I have had to explain to users how transactions works over and over again during the past years, and this is because users have Bitcoin in mind. We must embrace the uniqueness of Grin especially Interactivity. Grin is not Bitcoin 2.0 or anything like that, the further we move away from Bitcoin the better.

**If we try to fit Grin on any of the Bitcoin UI/UX what we will end-up doing is limiting Grin.**

Anynomous:

> This is an argument for “Sign”, a simple word expresses all that really matters, the action of signing a transaction | contract.

I said this and I will say it again: “adding signatures” is not the only thing happening. Maybe you want to “simplify” things only using “Sign” but this means nothing but only adding a signature. This means nothing to the state of the entity in question, which is **Transaction** not a Contract. **Nobody in the real world takes contracts out of their wallets**. Thinking transaction as a contract is the problem, and if we are talking about contracts rather than transactions, one could be inclined to use Sign, because of course, in that context Sign makes total sense.

My starting point is that we are talking about a **transaction**. Initially the Transaction is drafted, so the action on the noun is **draft**. Then the transaction is reviewed and accepted, the transaction is not just signed, and this is important, when a transaction is accepted more happens than just adding a signature. So the action on the noun is **accept** , not just sign. So, for the Transaction to be completed, the Transaction must be broadcasted. You cannot use “Sign” in the last step because “Sign” in addition to what is already being hidden will also hide the fact that the Transaction is also broadcasted. For the last step, the action on the noun then becomes **complete** , not sign, because the Transaction is not completed until is broadcasted.

This applies to SRS:

A Transaction is drafted.
A Transaction is accepted.
A Transaction is completed.

This also applies to RSR.

A Transaction is drafted.
A Transaction is accepted.
A Transaction is completed.

Just a single unified self-explanatory flow: **Draft** \- **Accept** \- **Complete** or **DAC**.

Also, Signatures could be use in many other context in Grin, example: [Authentication](https://github.com/mimblewimble/grin-rfcs/blob/4b86f55d85904ec478a843847532391e1a8faa49/text/xxxx-auth-slates.md). You do not want to limit the Signature concept only to the Transaction, what you want is to make sure users understand that we use Signatures and these Signatures are not limited to the transaction building process.

Anynomous:

> Alternatively, we can also use the generalized **“Sign”** button everywhere

This is bad UX practice, very bad. The effect of that is **pure confusion**.

Anynomous:

> This is an argument for “Sign”, a simple word expresses all that really matters,

It is not. You don’t want the same word to have several meanings, that is also a bad UX practice. The effect of that is **pure confusion**.

vegycslol:

> To me slatepack1 is not a draft when the only thing missing is signatures, otherwise every contract would also be a draft which sounds very confusing to me

When `S1`, to draft (a transaction) is literally what you are doing in many languages, specially on those language derived from Latin, Greek and the Indo-European languages. If you are confused is because you are applying the verb to the wrong noun. “Drafting” means producing something (der Entwurf in German which is Draft) that will incorporate a result.

On `S1` the something produced is a draft, but a draft of what? a draft of a transaction. Ask yourself, what is the **intention** of using a wallet? receive and send transactions, transactions not contracts, right? but what a wallet actually do? store and manage keys for transactions, and communicate with nodes and other wallets (in case of Grin). No one in the real-world is naming wallets as “keys handlers” which could be more technically accurate, people call these tools: “wallets”. These tools are being called wallets because of the nature of the problem they solve.

Using “Contract” instead of “Transaction” is counterproductive because it changes the whole meaning and says nothing about the purpose of the wallet, why is this important? Because a cryptocurrency wallet is not built to “setup contracts” or “sign contracts” or anything like that, why? because wallets are built to send and receive transactions, not contracts, transactions.

“ _**Electronic transactions for all**_ ” is written in grin.mw because that’s what Grin wants to achieve. Again, transactions, not contracts. Transactions. The fact that we are using signatures to create transactions is not a strong enough argument to alter the meaning of what a wallet or Grin does.

Anynomous:

> this would becomes very complex for more complex transactions involving many steps that could be performed in many different orders, such as MultiSig transactions

Yeah, this might be the only argument against using DAC, but let’s see if that is true…

tromp:

> Now, if you name these Draft, Accept and Complete, does that mean the general case is named
>
> Draft → Accept2 → … → AcceptN-1 → CompleteN → … → Complete1 ?
>
> That would violate the principle of the same name denoting the same steps.

I will respond to this separately, thanks for bringing up this.

oryhp:

> Broadcasting it to the network is a separate thing and the process should not assume who broadcasts it as it could be sent to a mixer or whatever.

I do not entirely disagree with this logic, but in practice we do not want to separate the final step from the broadcasting of the transaction because a transaction is not completed until the transaction is broadcasted. Broadcasting the transaction is what closes the transaction circle from the wallet perspective.

---

### Post by @tromp ⭐ (2022-07-17)
*Post #77*

tromp:

> We could also let naming be guided be more general n party transactions. In that case, the simplest slate flow is a forward pass followed by a backward pass
>
> party1 → party2 → … → partyN → partyN-1 → … → party 1
>
> and the steps could be called
>
> new → addkey1 → addkey2 → … → addkeyN → signkeyN → … → signkey1 → broadcast

As [@oryhp](/u/oryhp) noted, this is not just the simplest slate flow. It is the only one that is safe against key cancellation attacks. Any party that picks their key after party i, could pick theirs with PK_i subtracted from it. Since they cannot know the corresponding private key, they cannot sign with it. But if party i has to sign with PK_i before that happens, then the payment proof of party i is compromised. The other parties can collude to do a transaction with the kernel satisfying the payment proof, while leaving party i out of the payment.
The only way to prevent is, is to have all parties that pick their key after party i, also sign their key before party i needs to. When party i verifies all these partial signatures, it can be sure its key was not cancelled.

In summary, if the kernel key is simply the sum of the partial keys of the parties, then keys must be signed in the reverse order of the key additions.

To support any other order, we would need to define the kernel key in a more complicated way, e.g. as a weighted sum of partial keys with weights depending on all keys.

---



## Request for Funding - Node & Wallet Core Development | Deev | July-September
*Date: 2022-07-08 | [Forum Link](https://forum.grin.mw/t/request-for-funding-node-wallet-core-development-deev-july-september/9919)*
*Importance Score: 72.1 | Core Participants: yeastplume, davidtavarez*

### Post by @deev (2022-07-08)
*Post #1*

Funding Request to work mainly on node & wallet core code for the next 2 months once accepted.

Rate: €6,000/month
Working time: +30-35 hours/week
Funding Request: €12,000

What do I want to achieve in these next 2 months?

(My priorities but not limited, if there’s something that you would like to see and the community agreed on this that’s a necessity, just submit it on the thread. Possibly missing quite some more important features or bugs. Just let me now!)

* PRs to fix outstanding issues:

* [Node will freeze sporadically after a few days to a week of running · Issue #3725 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/issues/3725)
* [Archive node not transferable between Linux and Windows · Issue #3701 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/issues/3701)
* [inconsistent wallet transactions state · Issue #607 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/issues/607)
* …
* PRs to add features:

* Slatepack address create/verify signature ( asked by [@renzokuken](/u/renzokuken) )
* [Add mining endpoint to Node API · Issue #3201 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/issues/3201)
* Slatepack Memo
* …
* Reviews/Test PRs

* Documents new feature directly on docs.grin.mw and possibly videos as well (if the community want it)

* Start working on the Grin Core GUI. (at the end)

Who am I?
I’m a software developer and been following Grin since mi-2019 and started submitting PRs at the end 2020 mostly during my holidays or free time:

* [reorg cache fix by deevope · Pull Request #3495 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/pull/3495)
* [better naming of APIs file and variables by deevope · Pull Request #3525 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/pull/3525)
* [`verify-chain` node client arg by deevope · Pull Request #3678 · mimblewimble/grin · GitHub](https://github.com/mimblewimble/grin/pull/3678)
* [better naming of APIs files and variables by deevope · Pull Request #544 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/pull/544)
* [[5.0.x] replace .api_secret to .foreign_api_secret by deevope · Pull Request #546 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/pull/546)
* [Add the parameter confirmed_height to retrieve_tx owner_api method by deevope · Pull Request #606 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/pull/606)
* [View Wallet - fn rewind_hash & scan_rewind_hash by deevope · Pull Request #632 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/pull/632)
* [TOR bridge + TOR Proxy + migration config_file_version by deevope · Pull Request #617 · mimblewimble/grin-wallet · GitHub](https://github.com/mimblewimble/grin-wallet/pull/617)

The time spent on those PRs and following community discussions gave me good experience and knowledge of the core code and the tech globally. Always liked to help community members through their problems endured until it’s resolved.

Note, this funding request does not mean that it will become a mandatory funding on my side to work on grin code in the future. So far, it always been voluntary and motivated by the pleasure to interact with the community and play with the tech behind it.

---

### Post by @vegycslol (2022-07-08)
*Post #3*

Give him the money!  I’m not sure if memo has been defined in a rfc yet (i know tromp mentioned it in the early payment proofs rfc), so maybe we should first decide how we want memo to actually work (for example I’m still unsure whether it’s good to limit it to 32 bytes or not)

---

### Post by @Anynomous (2022-07-08)
*Post #4*

Im am all for highering @deev👍. These are issues that when solved make grin much more reliable to build on by exchanges and ecosystem developers. Unifying the memo/payment proof system, would be a great step forward. Should we think also if we can use these as memos for proving signing in MultiSig or for creating a multisig, or is it to early for that.
Not sure if we need memos for that but better to think ahaed.

---

### Post by @Yeastplume ⭐ (2022-07-10)
*Post #5*

Was happy to see this based on deeev’s earlier PRs. We’ve worked out an arrangement and deev will be joining us on the core team over the next couple of months.

We all look forward to working with him!

---

### Post by @Anynomous (2022-07-10)
*Post #6*

We can discuss and hopefully approve this funding request in the next CC meeting of 19th November, unless the OC prefers using their funds. Either way we can discuss it in the next CC meeting.

---

### Post by @davidtavarez ⭐ (2022-07-10)
*Post #7*

Yeastplume:

> We’ve worked out an arrangement and deev will be joining us on the core team over the next couple of months.

[@Anynomous](/u/anynomous) read that

---



## How to send and receive Grin with Ledger Live Desktop
*Date: 2022-09-09 | [Forum Link](https://forum.grin.mw/t/how-to-send-and-receive-grin-with-ledger-live-desktop/10021)*
*Importance Score: 69.9 | Core Participants: tromp, davidtavarez*

### Post by @NicolasFlamel (2022-09-09)
*Post #1*

I uploaded [this video](https://www.youtube.com/watch?v=M6nk1lsS8Sw) a few days ago that goes over how to send and receive MimbleWimble Coin with Ledger Live Desktop. The second half of the video focuses on doing the same with Grin. Enjoy!

[ ](https://www.youtube.com/watch?v=M6nk1lsS8Sw)

You can download the version of Ledger Live Desktop shown in the video [here](https://github.com/NicolasFlamel1/ledger-live/releases).

You can install the hardware wallet apps shown in the video onto a Ledger Nano S or Ledger Nano S Plus hardware wallet [here](https://htmlpreview.github.io/?https://github.com/NicolasFlamel1/Ledger-MimbleWimble-Coin/blob/master/tools/installer/index.html).

---

### Post by @NicolasFlamel (2022-09-10)
*Post #6*

Doogevol:

> I hoped active User confirmation would be required to receive grin with a hardware wallet. It seems to be not the case.

Correct, user confirmation is only required on the hardware wallet when sending Grin and not when receiving Grin.

Doogevol:

> t 09:21 i see verification of slatepack address on hardware wallet. (button pushed on Hardware wallet.)
>  But the Address seems to be irrelevant since it is not used on sender side or for transportation of slatepack message.

TradeOgre doesn’t support sending to a Slatepack address which is why I don’t use the Slatepack address in the video. Ledger Live Desktop only supports receiving Grin from manually entering non-encrypted and encrypted Slatepacks. The Slatepack address should be used by the sender if they want to encrypt the Slatepack and/or if they want the Slatepack to contain a payment proof.

Doogevol:

> At 09:52 first slatepack message is copied from sender wallet to Ledger Live Desktop window. Continue button is clicked on Desktop window.

Correct, Ledger Live Desktop uses the SRS workflow for sending and receiving Grin. This is the first step in that workflow.

Doogevol:

> At 10:44 Desktop window suggests “you received 9.970156” and also shows slatepack reply without any need to push a button on hardware-wallet. If your consider the desktop as as (partly) untrusted the information passed from the trusted device to the untrusted device automatically. And user does not know if the wallet automatically tries to transport the slatepack reply back to sender.
>
> I wished for a required action on hardware wallet button, before signed information goes from (trusted) hardware wallet to (partly untrusted) desktop application. But showing the User necessary information to decide, whether to sign or decline on the trusted screen.

It seems unnecessary to require user confirmation on a hardware wallet when receiving Grin since doing so doesn’t guarantee anything. Even after a Slatepack is “signed” by a recipient, malicious software could always send its own valid response back to the sender (if the Slatepack doesn’t contain a payment proof).

Currently, the only way that I know of to guarantee that a Slatepack was “signed” by the intended recipient is to have the Slatepack contain a payment proof. The payment proof allows the sender to verify the recipient’s Slatepack address after they receive the Slatepack response from the recipient. The recipient’s Slatepack address is verified by the recipient on their hardware wallet, and the sender is shown the recipient’s Slatepack address on their hardware wallet when approving the transaction if there’s a payment proof. The recipient’s hardware wallet creates the payment proof signature when receiving Grin, and the sender’s hardware wallet verifies the payment proof signature when sending Grin.

---

### Post by @NicolasFlamel (2022-09-11)
*Post #9*

The Slatepacks generated by TradeOgre when withdrawing Grin can be receive by anyone since they don’t have a specific Slatepack address set as the Slatepack’s destination.

You can set a Slatepack’s destination when sending Grin with the CLI wallet by using the the optional `--dest` argument. When a Slatepack address is set as the destination, the Slatepack will be encrypted and contain a payment proof so that only the intended recipient can receive the Slatepack.

[ send arguments1079×541 75.3 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a755964f99bb113861362eed38b8ac7ef4665059.png "send arguments")

TradeOgre doesn’t give you the option to set a destination Slatepack address when withdrawing Grin from it.

---

### Post by @NicolasFlamel (2022-11-13)
*Post #15*

I finished adding MimbleWimble Coin and Grin support to Ledger Live Mobile! Anyone who wants to try it can download the Android APK [here](https://github.com/NicolasFlamel1/ledger-live/releases).

[ Ledger Live Mobile Grin720×1520 37.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a2f13e4addb68367820554bfd5969ccd55bad39c.png "Ledger Live Mobile Grin")

Also, here’s all the changes that I’ve made to the hardware wallet apps and Ledger software since my last post. Huge thanks to the MimbleWimble Coin and Grin communities for suggesting several of these changes!

* Requires user confirmation on the hardware wallet when receiving.
* Hardware wallets shows a progress bar when creating Bulletproofs.
* Sped up creating Bulletproofs on hardware wallets by about 10%.
* Ledger Live Desktop/Mobile give the option to change a transaction’s base fee.
* Ledger Live Desktop/Mobile show a syncing percent when adding a new account.
* Fixes sending to and receiving from Grin++.
* Fixes transactions being removed when clearing the cache in Leger Live Desktop/Mobile.
* Implemented several optimizations to reduce syncing times.

And with that, everything required by Ledger to add MimbleWimble Coin and Grin support to their official Ledger Live Desktop and Ledger Live Mobile releases is now complete  Now we just have to wait for Ledger to finish auditing the code and merging in the changes. However, based on how slowly Ledger seems to operate, I’m not expecting this to happen anytime soon.

---

### Post by @davidtavarez ⭐ (2022-11-19)
*Post #16*

NicolasFlamel:

> Fixes sending to and receiving from Grin++.

When the app gets approved, I’ll add a button to install the app from Grin++

---

### Post by @airattack (2023-01-28)
*Post #17*

Should I ignore the MWC update available in Ledger Live desktop? I’m using the custom Grin integration with the installed MWC/Grin apps via the tutorial. I’m not sure if updating Ledger Live’s version of MWC will break the integration. Thanks!

[ mwc2211×537 49.6 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/61cc3f286be277d0c5b0263a42e921804c8cd0c0.jpeg "mwc")

---

### Post by @noobvie (2023-05-19)
*Post #19*

Just found a news related to Ledger’s statement: “Technically speaking it is and always has been possible to write firmware that facilitates key extraction. You have always trusted Ledger not to deploy such firmware whether you knew it or not,”
So is it true according to you? And is grin impacted same?
Source: [Crypto Wallet Maker Ledger Continues to Defend Recovery System, Vexes Crypto Twitter](https://www.coindesk.com/business/2023/05/18/ledger-continues-to-defend-recovery-system-says-its-always-technically-possible-to-extract-users-keys/?utm_source=twitter&utm_content=editorial&utm_term=organic&utm_medium=social&utm_campaign=coindesk_main)

---

### Post by @tromp ⭐ (2023-05-20)
*Post #22*

It baffles me that a company like Ledger rolls out such a feature without even answering basic questions such as:

1. are the decryption keys unique to your ledger device? (I’ve seen reports elsewhere that the seed could be restored to _another_ Ledger device, which has completely different security implications).
2. are the decryption keys in my device known to Ledger?
3. can any firmware update leak those decryption keys (some reports suggest that the decryption keys are in the firmware update itself, which is the worst of all possible worlds) ?

I want to trust them, but they make it so hard…

---



## Request for funding, @mattczt, October 2022 ~
*Date: 2022-09-21 | [Forum Link](https://forum.grin.mw/t/request-for-funding-mattczt-october-2022/10034)*
*Importance Score: 69.0 | Core Participants: tromp, davidtavarez*

### Post by @Mattczt (2022-09-21)
*Post #1*

Hello,
As some of you may be aware, our testnet miner (g1 mini) ran by [@hendi](/u/hendi) has gone down with a broken psu.
I have been running a testnet miner in the meantime. It is a single 1080ti, it is not ideal because the graph rate is too low to produce blocks consistently.
I am proposing that we need a backup miner to run along side hendi’s to keep the testnet running smoothly 24/7
I am willing to take this on if it is deemed worthwhile for the community.

I will buy a g1 mini for the purpose of running it on the testnet, on the condition of future reimbursement of cost. Usdt or grin.
Also i need the cost for electricity reimbursing at a cost of £0.92 a day or £1.15 a day if im running a stratum server. Grin preferred.
For transparency my electricity cost is 32.07p/kwh.

I am also happy if someone trustworthy can do this for a cheaper rate, they are welcome to take over this funding request from me.

I feel that we are at an important phase in testing with pibd and soon coinswap, just throwing this out there.

[@mattczt](/u/mattczt)

---

### Post by @mcm-mike (2022-09-22)
*Post #7*

[@hendi](/u/hendi) could help our here as he did run a testnet miner on how he did it?

[Could we also promote this in our GRIN newsletter:](https://twitter.com/NHASH_Official/status/1565258601849303041?s=20&t=9p65y3OWKHasJoHnntBeLA)

[twitter.com](https://twitter.com/NHASH_Official/status/1565258601849303041?s=20&t=9p65y3OWKHasJoHnntBeLA)

#### [NHASH](https://twitter.com/NHASH_Official/status/1565258601849303041?s=20&t=9p65y3OWKHasJoHnntBeLA)

[@NHASH_Official](https://twitter.com/NHASH_Official/status/1565258601849303041?s=20&t=9p65y3OWKHasJoHnntBeLA)

🎉𝑮𝒊𝒗𝒆𝒂𝒘𝒂𝒚 𝑬𝒗𝒆𝒏𝒕🎉 🎁iPollo G1 mini*1 For the Winner \- Follow [@NHASH_Official](https://twitter.com/NHASH_Official) \- RT this tweet & Tag your friends 🫧The winner will be chosen at 7⃣️7⃣️7⃣️ followers via TwitterPicker 🫧Stay tuned for more giveaway events 🫶🏼Thanks for the all-time support <https://t.co/jAqctIR7Jc>

[8:41 AM - 1 Sep 2022](https://twitter.com/NHASH_Official/status/1565258601849303041?s=20&t=9p65y3OWKHasJoHnntBeLA) 45  36

This would help us to get some sponsorship from nHash in regards to a free G1-Mini for our GRIN testnet.

---

### Post by @tromp ⭐ (2022-09-22)
*Post #9*

> Also i need the cost for electricity reimbursing at a cost of £0.92 a day or £1.15 a day if im running a stratum server. Grin preferred.

You don’t need to spend all graphing power on testnet. We have 2 minis available to mine testnet, so they could each divide graphpower 50-50 between testnet and mainnet, making back some of their electricity use in Grin. If one mini is out of commision, it’s ok to have testnet blocks be a little slower until it can be brought back.

---

### Post by @Anynomous (2022-09-27)
*Post #12*

This topic was discussed in the CC meeting of today (27-09-2022).
In general everyone is fine with the idea of having another miner on testnet, but we will wait and see if Ipollo will push through with donating one. We can write about the donation and link to their current price in Grin Post as compensation.

[@Mattczt](/u/mattczt) Do you mind getting energy cost compensated 100% in Grin? It is much easier for the CC to send Grin, which needs one signature, compared to BTC which requires 4 signatures.

---

### Post by @Cobragrin (2022-09-28)
*Post #15*

Anynomous:

> we will wait and see if Ipollo will push through with donating one. We can write about the donation and link to their current price in Grin Post as compensation.

i contacted with @nhash Hiro and he said ‘ _YES_ ’  , he accepts [@mcm-mike](/u/mcm-mike) offer. We gonna mention it on twitter and GrinPost channels.

---

### Post by @Anynomous (2022-10-12)
*Post #21*

[@Mattczt](/u/mattczt) No problem, we will ship one G1 Mini to you and reimburse electricity costs as requested . I will send you [@mcm-mike](/u/mcm-mike) Telegram handle in a private message, you can share your shipping information with him in a private message by clicking his name above.
We can send the second G1 Mini to [@hendi](/u/hendi) since he lost his miner for testnet due to a power supply breaking.
If the third G1 mini by Powpower pushes through, do you want to receive it [@navie](/u/navie)? I am not sure how hard it is to mine on tesnet since I have not tried myself. Maybe [@Mattczt](/u/mattczt) can share the details.

---

### Post by @navie (2022-10-12)
*Post #26*

Anynomous:

> If the third G1 mini by Powpower pushes through, do you want to receive it [@navie](/u/navie)?

Sounds good! Provided that I can get some initial assistance configuring the mini, hosting it is no problem.

Current electricity rate is ~ 0.094 kw/h USD

---

### Post by @davidtavarez ⭐ (2022-11-28)
*Post #40*

Could this calculation remain the same for the next 12 months

---



## 2023 Meme contest, anything goes, just have fun Meming!
*Date: 2023-01-03 | [Forum Link](https://forum.grin.mw/t/2023-meme-contest-anything-goes-just-have-fun-meming/10254)*
*Importance Score: 124.9 | Core Participants: tromp*

### Post by @Anynomous (2023-01-03)
*Post #1*

Lets kick of 2023 with a good old fashioned meme contest!
I will donate the first 42 Grin, who knows, maybe the Grin Community Council will donate as well.

**The rules:**

1. You can share any kind of meme you made that involves Grin.
2. Prices are distributed based on total accumulative likes for memes
3. The meme contest ends at February 28th, when all votes/likes are counted

Feel free to donate your Grin to the price fund, donate your time as an artists/mememancer , or simply enjoy up-voting memes.
Fee free to share any of these memes or the link on Social Media, only votes on the forum count for prize money.
I will kick of this meme contest with one of my creations!

Edit Bounty is now
42 Anynomous
50 Grinnode.live
100 Community Council
1000 David T.
= 1192 Grin

1st price 40%, 2end 30% 3rd 20%, 4th 10% of the price money. 5th or higher place is no price money but eternal fame as grin mememancer .

Your donations to the price-pot can be made via the Grin CC wallet, all transactions will be added to the price money unless specifically mentioned before sending the transaction:
`grin1jezf3lkcexvj3ydjwanan6khs42fr4036guh0c4vkc04fyxarl6svjzuuh`

---

### Post by @tromp ⭐ (2023-01-04)
*Post #7*

Technically, “when the mining stops” should read “when the emission ends”. Even more accurate would be “when the block subsidy becomes insignificant” but that wouldn’t fit:-(

---

### Post by @tromp ⭐ (2023-01-11)
*Post #28*

Constant reward is disinflationary (inflation rate going down toward 0).

---

### Post by @tromp ⭐ (2023-01-11)
*Post #29*

Someone could extend <https://i.redd.it/cwjes2b8cbba1.jpg> with another copy of the top frame for sending a Grin tx …

---

### Post by @tromp ⭐ (2023-01-12)
*Post #39*

I don’t like to see Grin advertised as a get rich quick scheme.
As I said before, there is no expectation of profit in grin…

---

### Post by @tromp ⭐ (2023-01-21)
*Post #60*

The velomobile pictured there is a Quest [1]. Perhaps they’re on a quest for simplicity ?!

[1] <https://en.velomobiel.nl/quest/>

---

### Post by @tromp ⭐ (2023-01-27)
*Post #66*

You mean loss rate will approach emission rate

But it’s disinflationary irrespective of losses.

Actually, since the term disinflationary refers to a slowing inflation, it might not even be appropriate for a system that reaches equilibrium between inflation and losses.

---

### Post by @tromp ⭐ (2023-02-16)
*Post #93*

Anynomous:

> I think on the wiki it us ab example of a single transaction

Not sure what you mean to say. Can you provide a quote from the linked docs that suggests a signature can be part of balancing values?

Anynomous:

> should I delete the part of the fee? I think the fee is part of the kernels?

You should keep the fee, which is required to balance the values. The signature just commits to the fee (it’s part of the signed message).

---



## Opposition to default coinswap
*Date: 2023-01-17 | [Forum Link](https://forum.grin.mw/t/opposition-to-default-coinswap/10280)*
*Importance Score: 67.0 | Core Participants: tromp*

### Post by @Trinitron (2023-01-17)
*Post #1*

Coinswap may get closer to a reality this year so I’ll start this discussion now.

I oppose it being built into the core gui wallet as a default or preselected transaction mode.

My most essential argument for this is that I believe optional functionalities should remain explicitly optional, and that naive users should not be passively guided into engaging with them. It is counter to the principal of minimalism to actively promote or suggest this complexity.

---

### Post by @Neo (2023-01-17)
*Post #3*

Trinitron:

> My most essential argument for this is that I believe optional functionalities should remain explicitly optional, and that naive users should not be passively guided into engaging with them. It is counter to the principal of minimalism to actively promote or suggest this complexity.

My argument against this would be what is the purpose of using Grin vs XYZ coin if you’re not interested in making a private transaction? I’d also consider where Grin’s user adoption is going to come from. IMO it’s going to come from users of other privacy focused coins.

If it was the default, then my biggest concern about making it op-out would be the impact it has on UX.

---

### Post by @tromp ⭐ (2023-01-18)
*Post #9*

trab:

> I assumed that the coinswap implementation _maintained_ the beauty of grin’s simplicity

Yes; it’s one of the bullet points I raise at

[Simple Money](https://forum.grin.mw/t/simple-money/10215/1)

> Simple mixing
>
>> CoinSwap can non-interactively mix thousands of self spends each day or hour.

Of course different wallets can have different defaults. For the reference Rust wallet, I expect the configuration file will have a mwixnet section where lists of mwixnet servers can be defined similar to how seed lists and peer lists are currently defined. But I would expect any hardcoded lists to be commented out, waiting for the user to choose one to uncomment before enabling mwixing. That way, the default behaviour is the simplest one and the user is not surprised by the change in behaviour if a set of selected mwixnet nodes interrupts or ceases operation for whatever reason.
If a particular mwixnet service proves to be both popular and reliable for a long period, and we expect the majority of Rust reference wallet users to make a particular configuration change, then it makes more sense to discuss change of this default.

Other wallet implementations may choose to enable mwixing by default.

---

### Post by @tromp ⭐ (2023-01-20)
*Post #15*

We would recommend that users learn about coinswap and its behaviours and limitations before they enable it. Having it enabled without understanding what it does or even being unaware of it may lead to unnecessary confusion. It will have to work reliably for those willing to experiment with it before we can ever consider making it a default.

---

### Post by @tromp ⭐ (2023-10-03)
*Post #40*

Grin is not a privacy-first-scalability-be-damned coin like Monero [1].
Grin’s focus is on simplicity and fairness instead.

[1] [Reddit - Dive into anything](https://www.reddit.com/r/grincoin/comments/mu88ow/is_monero_better_than_grin/)

---

### Post by @tromp ⭐ (2023-10-03)
*Post #42*

Coinswap doesn’t affect scalability. BP++ somewhat improves it, reducing rangeproof size by 38%, but has no effect on privacy.

---

### Post by @tromp ⭐ (2023-10-04)
*Post #44*

The coinswap implementation is being worked on as we speak.

For BP++ there is no great need to hurry.

Once it gets hardforked in,
the UTXO set will slowly migrate from having BP rangeproofs to having BP++ rangeproofs, as the former keep getting spent. In non-MW chains, you have to carry around the baggage of spent txos and their rangeproofs forever, so full nodes can verify the entire tx history.

In MW chains, only the utxos that never get spent, due to lost keys for instance, will remain stuck with the larger rangeproofs.

---

### Post by @tromp ⭐ (2023-10-04)
*Post #46*

trab:

> I think [@i2pZ7812HTZV69](/u/i2pz7812htzv69) is asking if it is going to be hardcoded into the base layer as a mandatory default setting.

What does it mean to “hardcode it into the base layer” ? This is completely invisible to the consensus layer.

We’re talking about wallet behaviour, which is entirely up to the wallet author. Some wallets will support coinswap, and some won’t. Those that do still need to have the user select an mwixnet to use and approve payment of mixing fees.

---



## Report of funding
*Date: 2023-03-23 | [Forum Link](https://forum.grin.mw/t/report-of-funding/10420)*
*Importance Score: 70.6 | Core Participants: yeastplume, davidtavarez*

### Post by @Danila (2023-03-23)
*Post #1*

In tg group Leedan was ask where money was spend from btc wallet, can we show some report for this pls?
Coz trust less trust is a key as I’m think

---

### Post by @davidtavarez ⭐ (2023-03-24)
*Post #3*

as long as development continues I am not concerned, and development has not stopped; furthermore, the OC has expressed the intention to support the CC when necessary.

---

### Post by @Trinitron (2023-03-24)
*Post #5*

Both councils should do a far better job at accounting. It is the most basic form of accountability and it couldn’t be simpler yet they are failing to do so. Create a text document on github or whatever, when you make a transaction add a line with a note about what the transaction is. Don’t overcomplicate it so that it doesn’t get done.

Sloppy accounting looks worse in hindsight than it does in the moment. The OC’s wallet is almost completely decipherable because it’s mostly just payments to yeastplume but CC risks losing track of stuff completely.

---

### Post by @Cobragrin (2023-03-24)
*Post #7*

You are parroting over and over same thing. The case is [OC funds](https://grin.mw/fund) update since 2021, you find an angle again to attack GRINCC and my work…
There is every detail on [GRINCC finance hub](https://github.com/cekickafa/finance). IF you want one single explanation, go and click block explorer.

---

### Post by @Cobragrin (2023-03-25)
*Post #11*

coolwhip:

> Also, why are the spending reports only on your fork of the repo, and not merged to the official grincc repo? I never would’ve thought to check your personal fork

Some members didnt yet [review the pull request](https://github.com/grincc/finance/pull/12).

Danila:

> It’s not clear by this links about all tx especially latest.

oryhp:

> I agree it’d be good to have some reporting. The development pretty much continues as it has in the past hence why the BTC wallet movements. [@Yeastplume](/u/yeastplume) can write a bit more on that.

* That was about [discussion at](https://t.me/grinprivacy/93719) TG Channel [latest Btc flow from](https://bitinfocharts.com/bitcoin/address/bc1q2x8gu8n85ylur5j83yflhpg5hf80nhnyem98k2pld46lf4czhmgsxq8wlu) OC funds.
* OC funds report missing since [2020](https://github.com/mimblewimble/grin-pm/blob/master/financials/reports/funding_transparency_2020Q4.md)

**GRINCC FUND Situation**

* GRINCC reports are up to date, funding requests are made public and decisions were publicly made. You can rewind back and see in reports, decision logs and [meeting reports](https://grincc.mw/meetings).

* GRINCC is **full clear** _when paid, to whom paid, for what job_ and all spendings matches to 1:1 to last [GRINCC FUND Bitcoin balance](https://github.com/cekickafa/finance/blob/main/payment-tracking.md).

* GRINCC Funds are multisig and they double check and sign separetly before payment.

* Any GRINCC BTC payments, if you wonder any question,cant figure out, can DM or ask here. There is no doubt, it is all public and transparent, booked.

The topic is Report  of funding or  Development Progress Report or overview.

That is for ex asked [@scilio](/u/scilio) about ‘’ [Coinswap implementation progress](https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149/75) ‘’

---

### Post by @Yeastplume ⭐ (2023-03-26)
*Post #15*

In agreement with this. In our case the accounting has been so simple that we’ve put off updating the spending reports (we haven’t had a dedicated PM for a while :D), but I’m going to bring them all up to date over the next week and keep them updated as we go from now on, even if they are simple.

I’ll also start doing more regular posts about the actual work I’ve done, what I’m doing now and my future plans. I’ve been quietly busy for the most part on various things, but perhaps a bit too quiet, will address that going forward.

---

### Post by @oryhp (2023-03-31)
*Post #29*

ardocrat:

> We need more detailed reports from OC to increase quality.

Increase quality of work or reports?

ardocrat:

> My suggestion is to describe every working hour/rate for transparency and possible correctness of efficiency at minimum bi-weekly timeline.

I strongly disagree with this. The nature of contributing to Grin is already pretty invasive because the reports are public. It’s already hard enough to find competent people that are ok with broadcasting their salary to the world while risking people judging their work by commits. I generally feel that if I have to report every hour of my work, it’s better to just switch jobs because nobody trusts you and I’d definitely never work if every hour of my work was broadcast to the whole world. I find the urge of controlling spent hours off putting and many of my colleagues feel the same. Besides, more often than not, adding bureaucracy hurts productivity and motivation and it’s really a trap many companies fall into because they want to feel they’re in control.

ardocrat:

> What was done, what will be done should be mirrored at Kanban board of the project.

I agree it’s good to have an overview on what people are working on and believe the post Yeast’s made captures the important information around that. I’m not against kanban boards, but I’m also not convinced we absolutely need one at this stage (we have a single core dev atm). Anyone interested in what’s going is probably going to find the important parts in the update post. If something is missing, I suggest we ask a question on the thread or on keybase. I’d love more involvement there and make things more active

---

### Post by @Yeastplume ⭐ (2023-03-31)
*Post #33*

Thanks Phyro. I’m not going to get drawn into a long discussion about all of this, but the project has been around for a good while now. It’s unique in a lot of ways and resourcing has always been _extremely_ challenging for many reasons, (only a handful of which are alluded to here). I think a lot of the community understands this. Things have been tried with the best of intentions that ended up being total disasters, and trying to put a load of premature structure and constraints into what’s already a challenging environment isn’t something I’m going to be supporting any time soon.

---



## Non-interactive transactions for the MW blockchain
*Date: 2023-04-29 | [Forum Link](https://forum.grin.mw/t/non-interactive-transactions-for-the-mw-blockchain/10472)*
*Importance Score: 76.9 | Core Participants: david, tromp*

### Post by @Andi (2023-04-29)
*Post #1*

Non-interactive transactions for the MW blockchain.
Below is the concept of the proposed transactions. It is assumed that the reader is familiar with the principles of building transactions in the MW blockchain. This concept describes only the general principles of building a non-interactive transaction.

1. The main advantages of the proposed transactions.
1.1. Transactions do not degrade the privacy of the MW blockchain.
1.2. After the input data is used up, most of the data can be removed from the blockchain.
1.3. The recipient performs a quick search for transactions belonging to him. The number of transactions per wallet can be quite large, but is limited by the size of the array in memory. This implementation completely removes the association of the public address from any visible transaction data.
1.4. The sender can enter a hidden identifier into the transaction so that the recipient knows exactly who made the payment.
1.5. You can implement a payment cancellation feature provided that the recipient has not accepted the payment within a given number of blocks. This can be useful if the sender wants to insure that the payment is not sent to the wrong address.

2. The main disadvantages of the proposed transactions compared to standard MW transactions.
2.1. Non-interactive transactions are always explicitly linked to the kernel, so they cannot be masked by false inputs and outputs. Thus, to obfuscate the transaction graph, you need to use these transactions as an intermediate state, which in some scenarios will lead to a double commission (see point 4 for more details).
2.2. The input size of unspent transactions has been increased compared to the standard MW input. Added coordinates of 3 elliptic curve points and 256-bit scalar. If you implement the payment cancellation function, then 1 more point of the elliptic curve is added.
2.3. Increased the size of the core stored in the blockchain by at least a 256-bit scalar. If you implement the payment cancellation function, then the coordinates of 1 point and a scalar indicating the number of blocks before cancellation are added to the blockchain.

3. Main idea.
3.1. Basic designations:

* C - Pedersen’s obligations;
* G-point blinding factor generator;
* H- point of the generator of the number of coins;
* a1, a2, bi – scalar values, acquired in some way from the initial phrase of the purse;
-A1i, A2i – recipient’s public keys - address;
-Kc - output non-interactive transaction;
-D - additional data;
-S - shared secret;
-P1i, P2i – recipient hints that use encrypted quick access to the shared secret;
* n - hint, in which the payee, payment identifier (clause 1.4.) and part of the public key A1i are encrypted;
* Bi - public key for withdrawal of funds by the recipient

3.2. Create an address.
The recipient generates the 2 public keys in a special way so that the shared secret can be determined independently of the public keys themselves.
A1i = bi*(1/a1)_G
A2i = (bi+1)_(1/a2)_G
Key moment:
a2_A2i-a1*A1i=G
a1, a2 are unique for each wallet.

3.3. Forming the output of a non-interactive transaction - Kc by the sender. The output of the transaction consists of 3 parts: Pedersen’s commitment -C, verification of the range of transferred funds BP(C) and additional data -D that the recipient needs to calculate the shared secret, as well as to determine the amount transferred and the hidden identifier (clause 1.4.)

3.3.1. To begin, the sender generates a shared secret
S=s _G
s is a random scalar number.
The shared secret is the public key S.
3.3.2. The sender generates hints for the recipient
P1i=s_A1i
P2i=s _A2i
3.3.3. The sender generates a hint - n, in which the transmitted amount, the payment identifier (clause 1.4.) and part of the public key A1i are encrypted.
n= HASH256(y(S))+v(0-64 bits)+id1_2^64(64-128 bits) + id2*2^128(128-192 bits)
y(S) – y coordinate of the shared secret S
v is the number of transferred coins;
id1 – payment identifier;
id2 - the first 64 bits of the x coordinate of the public key A1i.

3.3.4. The sender generates the public key of the recipient (also at this stage, a public key can be generated for the return of funds).
Bi=x(S)_A1i
x(S) – x coordinate of the shared secret S
3.3.5. The sender computes a common hidden factor from the shared secret.
r= HASH256(x(S))
3.3.6. The sender forms a local Pedersen commitment
Сl=r_G-Bi+v*H

3.3.7. The sender commits all elements of the transaction (it is necessary so that when included in a block, it is impossible to change the constituent elements of the output). To do this, it calculates a hash from the sum of the hashes of each element of the transaction and adds to the total hidden factor.

HASH1= HASH256(HASH256(n)+ HASH256(P1i)+ HASH256(P2i)+ HASH256(Bi)+ HASH256(Cl))
3.3.8. The sender generates the final commitment of Pedersen and writes it into the transaction element by element, with the exception of HASH1 _G, which can be calculated.
C= HASH1_G+Bi+Cl
The sender must attach a check of the range of transferred coins, for this we represent C in the following form:
С= (HASH1+r)_G+v_ H
The check of the range of transferred coins performed using “Bulletproofs” will be denoted by BP(C).
3.3.9. The final output of the confidential transaction will look like this:
Kc=C;BP(C);D = HASH1 _G+Bi+Cl; BP(C); (n,P1i,P2i).
Remember that HASH1_G does not have to be written down, it can be calculated.

3.4. Fixing a non-interactive transaction in the blockchain.
Since the sender knows the common hidden factor, it is necessary to ensure the transfer of ownership to the recipient. To do this, the following data is recorded in the blockchain:
Bi- public key of the recipient (in the process of spending the output of a non-interactive transaction, it will be signed and will be taken into account as an offset on a par with other MW cores);
HASH1 – clause 3.3.7 (prevents the sender from changing the transaction in the future, otherwise the sender will be able to rebuild the transaction with the same core, but zero cost v);
When implementing the payment cancellation function, the sender’s public key and the number of blocks through which the payment can be returned must be included.

3.5. Identification of a non-interactive transaction by the receiver.
3.5.1. The recipient calculates the shared secret
S=a2 _P2i-a1_ P1i
3.5.2. Calculates
n- HASH256(y(S))=v(0-64 bits)+id1 _2^64(64-128 bits)+ id2_ 2^128(128-192 bits)
if the received number is less than 192 bits, then the transaction belongs to the recipient.
Now the recipient knows the values v, id1, id2.
3.5.3. Knowing id2, the recipient can search the array and determine from which public keys the transaction was generated. The number of elements in the array is equal to the maximum number of possible transactions for one wallet.
3.5.4. The recipient calculates the private key for Bi.
x(S)_bi_(1/a1)

3.6. Spending.
To spend the funds, the recipient signs Bi with Schnor’s signature and a fee is paid. At the same time, the unspent output, which has now become the input of a new transaction, changes the value of the blinding factor by the value of Bi.
The Pedersen Commitment for Transaction Entry will now have the following value:
C’= HASH1*G+Cl
There is no need to sign the modified commitment range, as the Schnor signing of the kernel ensures that there is no hidden amount of coins in Bi.

3.7. Removal from the blockchain.
After spending a transaction, the following data can be removed from the blockchain:
HASH1*G+Cl; BP(C); (n,P1i,P2i).

4. The problem of obfuscating the transaction graph.
To obfuscate the transaction graph in the MW blockchain, it is possible to add false inputs and outputs during the propagation of a transaction at the stage of the Dandelion stem. False inputs and outputs are indistinguishable from regular inputs and outputs of interactive MW transactions. The outputs of non-interactive transactions are different from the outputs of interactive MW transactions, so you won’t get lost in false outputs.
In order to solve this problem, it is necessary to avoid constructing a transaction in which the input and output will be part of non-interactive transactions. The recipient must first send funds to the MW stdout among other false outputs, and then a non-interactive transaction can be created using the MW stdout mixed with the false inputs as input. Thus, a non-interactive transaction will be an intermediate state between standard inputs and outputs of MW.

---

### Post by @tromp ⭐ (2023-05-01)
*Post #12*

Back in 2012, the quantum factorization record [1], using Shor’s algorithm for numbers not of a special form, was 21, factored as 3x7.

Now, over a decade of supposed quantum progress later, the record is … still 21. I don’t see them getting much further in the next decade.

[1] [Integer factorization records - Wikipedia](https://en.wikipedia.org/wiki/Integer_factorization_records)

---

### Post by @tromp ⭐ (2023-05-01)
*Post #16*

oryhp:

> It might be good to compare your scheme to theirs

This looks rather different from those, assuming I understood it correctly.

This proposal is more like the sender just giving the blinding factor and amount to the receiver, i.e. creating of 1-of-2 output. The difference is that it uses the chain itself as a communication medium from sender to receiver, making it way more complicated then just sharing the info on a private communication medium.

---

### Post by @tromp ⭐ (2023-05-01)
*Post #19*

Yes, the idea of payment through a temporary 1-of-2 has been proposed several times in different forms, including by myself. And none of them can support payment proofs, because you cannot prove which of the 2 parties spends a 1-of-2.

---

### Post by @tromp ⭐ (2023-05-01)
*Post #21*

How can a 3rd party tell whether the sender or the receiver spent it, when both claim the other did?

---

### Post by @tromp ⭐ (2023-05-02)
*Post #23*

If there is no 1-of-2 involved then I didn’t understand your proposal. Maybe you can explain what consensus rule changes are required in your proposal.

---

### Post by @tromp ⭐ (2023-05-02)
*Post #26*

You haven’t explained what consensus rule changes are required to support your scheme…

Andi:

> I haven’t been able to find 1 of 2 yet, can you provide a link?

Here for instance <https://forum.grin.mw/t/simple-idea-for-2-step-grin-transfer/>

---

### Post by @david ⭐ (2023-05-31)
*Post #34*

tromp:

> This looks rather different from those, assuming I understood it correctly.

I’ve looked at the 2 PDFs in the most recent reply, and it looks like they are actually quite similar to the existing schemes ([1] [Minglejingle](https://forum.grin.mw/t/minglejingle-scalable-blockchain-with-non-interactive-transactions/8288), [2][ LIP-0004](https://github.com/litecoin-project/lips/blob/master/lip-0004.mediawiki), and [3] [Non-interactive Mimblewimble transactions, revisited](https://eprint.iacr.org/2022/265.pdf)).

[@Andi](/u/andi), how does your idea differ from those 3? Are there any notable improvements over these schemes? AFAICT, your writeups each seem to be just minor variations of [2] and [3], but if there is something more novel about your approach that I may have overlooked on my first read, please let me know, and I’d be happy to take another look.

---



## CC Fund: expenses, responsibilities, spending guidelines and follow-up processes
*Date: 2023-05-16 | [Forum Link](https://forum.grin.mw/t/cc-fund-expenses-responsibilities-spending-guidelines-and-follow-up-processes/10522)*
*Importance Score: 98.1 | Core Participants: davidtavarez*

### Post by @l33d4n (2023-05-16)
*Post #1*

**This post is a proposal to freeze any future expenses from the CC fund** until clear decisions are made regarding the responsibilities and roles, enforcement of the spending guidelines and clear and transparent decision making about the follow-up processes.

The proposal does not include the **role of one GK** which is necessary for transparency and the accessibility of information for the community as specified in the spending guidelines.

* * *

**Just to clarify** , this is not a personal attack against the members of the CC, 5/6 are volunteers and I believe that most of them want the best for the community, but without clear rules and responsibilities the road is easily opened and **there is no way back once the funds run out**.

* * *

## Table of Contents

1. **Basic facts to make things clear**

2. **Spending guidelines**

3. **CC role definition**

4. **Enforcing the spending guidelines and follow-up**

5. **Solution**

6. **Final note**

* * *

## **Basic facts to make things clear:**

All the information in this post is collected from the available public records of the [CC repo](https://github.com/grincc) and this forum. If you find any mistakes, outdated or missing information, please let me know and I will update it.

[Total funding since 2021-10-21 (BTC)909×564 22.4 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/3689ea6ae7bd61d01d27a7f066d28f9303df1316.png "Total funding since 2021-10-21 \(BTC\)")

The CC Fund received **33 BTC** from the original Grin Development Fund. In almost 19 months, the CC fund has spent **9.13858939 BTC** which is **27.7%** of the total CC funds.

Also, the CC [committed to paying £25,000 for CoinSwap](https://forum.grin.mw/t/request-for-funding-scilio-coinswap-implementation/9149) Milestone 3 once it’s done.

During this time the CC approved and funded **25 requests for 9 applicants**.

[Funding by applicants (BTC)909×565 41 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/132a57666e8be3049b70c6b0619d3820516d06b4.png "Funding by applicants \(BTC\)")

[Funding by categories (BTC)910×565 27.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/0c40709d77dc6963ad79bae83cf6586b90643278.png "Funding by categories \(BTC\)")

The charts show the distribution in BTC as paid by the spending log although **some payments were made in GRIN coins so the total funding should be higher.**

| Category | requests  | BTC        | USD         | % of total |
|----------|-----------|------------|-------------|------------|
| GRIN++   | 5         | 4.42621146 | $108,430.37 | 48.4%      |
| GK       | 12        | 1.54663826 | $37,927.10  | 16.9%      |
| Mining   | 2         | 1.10501997 | $52,531.99  | 12.1%      |
| CoinSwap | 2         | 1.01527389 | $30,755.22  | 11.1%      |
| BTC-GRIN | 2         | 0.54550658 | $27,539.69  | 6.0%       |
| Bounties | 2         | 0.49991923 | $11,418.00  | 5.5%       |

There was never an official tracking process for the funded tasks so I manually checked for updates for each one and marked it, **“Is this request fully completed and the benefits are transparent and clear? Yes or No.”**

**Total of 25 funding requests approved but only 18 can be easily defined as completed according to the spending guidelines** (as far as I know with my limited technical knowledge so the number may even be lower)

These are 7 funded requests that cannot be defined as completed right now because is not possible to understand what exactly was funded or why and how it serves the community:

* 2 were abandoned **(0.30840909 BTC / $6,092.14)**

* 1 is currently unclear **(1.86553872 BTC / $31,430.00)**

* 4 missing transparency reports or public records for follow-up how they used and how they serve the community today **(1.65052655 BTC / $80,071.95)**

[Follow-up tasks since 2021-10-21 (BTC)908×563 26.2 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/183a0024d6721d75e8b7e4e889569223e6141984.png "Follow-up tasks since 2021-10-21 \(BTC\)")

[Follow-up tasks since 2021-10-21 (25 tasks)907×563 26.3 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/93b46533fc3fa64b21e337f92771c1a2d1b1b6d4.png "Follow-up tasks since 2021-10-21 \(25 tasks\)")

**Abandoned:**

| Date       | spend description                | BTC        | USD       |
|------------|----------------------------------|------------|-----------|
| 2022-05-14 | @jankie Mar-May 2022 funding     | 0.07206201 | $2,112.14 |
| 2022-12-25 | @satoshcrat Jan-Apr 2023 funding | 0.23634708 | $3,980.00 |
| Total      |                                  | 0.30840909 | $6,092.14 |

**Unclear:**

| Date       | spend description                | BTC        | USD        |
|------------|----------------------------------|------------|------------|
| 2022-12-22 | @dtavares Jan-April 2023 funding | 1.86553872 | $31,430.00 |
| Total      |                                  | 1.86553872 | $31,430.00 |

The status is still unclear. The funding request specifies 3 tasks: CLI, API and documentation, but from the [discussion](https://forum.grin.mw/t/request-for-funding-davidtavarez-january-april-2023/10205) and the new “[Progress Tracking of Funded Requests](https://github.com/cekickafa/docs-1/blob/main/funded_requests_progress.md#dtavarez---grin-development-jan-apr-2023)” it is not clear what the status is right now before [a new funding request was submitted](https://forum.grin.mw/t/request-for-funding-davidtavarez-may-august-2023/10485).

**Missing reports for transparency:**

| Date       | spend description         | BTC        | USD        |
|------------|---------------------------|------------|------------|
| 2021-12-22 | BTC-GRIN conversion       | 0.50000000 | $25,756.42 |
| 2022-02-27 | BTC-GRIN conversion       | 0.04550658 | $1,783.54  |
| 2022-11-23 | community farm expenses   | 0.13977543 | $2,265.00  |
| 2021-10-21 | Community miners purchase | 0.96524454 | $50,266.99 |
| Total      |                           | 1.65052655 | $80,071.95 |

The “BTC-GRIN conversion” missing records how and why the GRIN coins were used, the [GRIN wallet report](https://github.com/grincc/finance/blob/main/grincc-wallet.md) is messy, outdated and contains errors ([revenues marked as expenses](https://github.com/grincc/finance/blob/cf8fab887513b5fbc6d54e6d991fdebb78ce02d6/grincc-wallet.md?plain=1#LL38C4-L38C4) so when calculating the balance I got a negative number -240K GRIN)

The Community farm has been discussed many times but the Miners purchase and expenses were not documented clearly so **I was unable to verify this due to a lack of transparency** (“Mining report” or something organized and accessible to the community), how many miners were purchased? How many of them are active right now? testnet or mainnet? the g1 has been inactive for a while, what is the plan and who is responsible? What are the monthly expenses/maintenance costs? What is the revenue?

* * *

## **Spending guidelines:**

Even if we can’t agree on all the expenses above we can all agree that some of the previous funding goes against the [official spending guidelines](https://github.com/grincc/docs/blob/main/spending-guidelines.md), the quotes parts in bold:

> **Decision Process:** … The Community Council will never make a decision without having clear:
>
> How the expense will be helpful for Grin, How much funds will be spent. If the expense will be a one time or require multiple rounds of financing?
>
> Some rules will be established during the discussions to clarify **how the accountability process will be.**

**We need clear decisions to be made regarding the responsibilities** and roles, enforcement of the spending guidelines and clear transparent decision making about the follow-up processes.

> **Reporting:** The result of **all funding decisions will be published in the meeting notes** found in the Grin Community Fund repository. It is mandatory to **publish a detailed spending log** of all transactions made in and out of the funds.

Some of the funding reports were published over a year after the funding made, the [GRIN wallet report](https://github.com/grincc/finance/blob/main/grincc-wallet.md) are still outdated and since the [meeting notes](https://github.com/grincc/agenda/tree/main/notes) duty removed from [@cobragrin](/u/cobragrin) duties **the meetings notes have not been published again for months until now** , I explained the [timeline here](https://forum.grin.mw/t/request-for-funding-groundskeeper-satoshocrat-jan-apr-2023/10211/9).

* * *

## **CC role definition:**

When the CC fund started we were all full of excitement and felt that finally the community will be able to fund what we want and need but the CC role definition and the responsibilities are still unclear and over time things have changed, **most of the CC members got busy with life and that’s fine, but we’ve reached a point where things need to be clear** , what exactly are the CC duties? just keyholders or active duties to enforce the guidelines?

**The CC members explained some of these challenges several time**

(Full long discussions [here](https://forum.grin.mw/t/minimalism-in-spending-of-the-community-council/10228), [here](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185) and [here](https://github.com/grincc/agenda/issues/72)):

[Pause GRIN Community Council - we need your opinion!](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185/5)

> We are all volunteers who have a variable amount of time and no consistent time available, that leads to problems now and then. Especially since most of us are business owners and have families, free time is simply limited and variable with us sometimes having not enough time to actively keep track of everything going on in Grin.

davidtavarez:

> Since the role of the CC has been reduced to mere key holders, which was not supposed to be the case, the CC has been failing with no sign of improvement in that regard

[Pause GRIN Community Council - we need your opinion!](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185/16)

> My opinion is that the community should hope CC members are more than just key holders, however, there shouldn’t be any expectation for them to be more than this, unless they’re fulfilling a funding request. However, if members can only just be a keyholder for a prolonged period, they should offer to step down. The most important thing from my perspective is that development moves forward outside of just maintaining the core codebase and the community has as many funding routes as possible. Grin needs to be keep building, everything else is noise.

[Pause GRIN Community Council - we need your opinion!](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185/5)

> We need to own our mistakes and admit that going on as we did in the last half year is not a good way forward since we were inefficient, not very effective and some members and contributors got demotivated.

[Pause GRIN Community Council - we need your opinion!](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185/10)

> The situation is very simple: if no one assumes any responsibility of any kind, then there is no reason to exist. No one has explained why a transaction takes weeks or months to be made. Or why there are still pending commitments to fulfill. My guess is that I won’t get the answer. It’s not just about payment delays, that’s just one of the symptoms.

Don’t get me wrong, a lot of the approved requests had a positive impact on the community, for example: the mobile wallet by [@davidtavarez](/u/davidtavarez) , the CC website by [@stakerv](/u/stakerv), the bounty by [@nicolasflamel](/u/nicolasflamel) and [@Cobragrin](/u/cobragrin) as a GK who is always ready to take on more responsibility.

**But what about the wasted funds?**

**GK roles:** **2 funded GK abandoned and none of the CC members even noticed or asked**. I had to [push again and again](https://forum.grin.mw/t/request-for-funding-groundskeeper-satoshocrat-jan-apr-2023/10211/9) to get an “[official refund request](https://forum.grin.mw/t/request-for-funding-groundskeeper-satoshocrat-jan-apr-2023/10211/10)” for something so obvious, and actually looking back I have to ask, **why did we even need 2 GK in the same period of time?** It doesn’t make sense after reading [the meeting notes](https://github.com/cekickafa/agenda/blob/main/notes/2022-12-20-community-meeting-notes.md#2-request-for-funding-cobragrin-dec-march-2023).

**Community miners:** **the miners purchased at the highest price ever over a year before even being placed in the facility** , The G1 has not been inactive for a while, and there will always be new issues that require some kinds of skills, ongoing expenses and responsibility.

We talked about this topic on 2023-04-29, [@davidtavarez](/u/davidtavarez) confirmed that:

> “Maybe spending on ASICs wasn’t the smartest idea, ASICs were bought in the worst moment”

Have we really considered the long term responsibility of running a mining community farm **before spending over 12% (1.10501997 BTC / $52,531.99) of our approved funding** (not including GRIN payments and ongoing maintenance costs)?

* * *

## **Enforcing the spending guidelines and follow-up:**

The **follow-ups for each new funding request is almost impossible right now** , the follow-ups and the review process requires time, tech skills, clear responsibility and equal enforcement.

For example: I brought the follow-up progress issue to the [CC meeting (2023-4-25)](https://github.com/cekickafa/agenda/blob/main/notes/2023-04-25-community-meeting-notes.md), the original idea was to follow-up the GK tasks, but in the end **I suggested adding to the GK duties follow-up for each funded task**.

[@davidtavarez](/u/davidtavarez) and [@Anynomous](/u/anynomous) **as CC members supported it** , and [@Cobragrin](/u/cobragrin) created the [progress tracking file](https://github.com/cekickafa/docs-1/blob/main/funded_requests_progress.md#dtavarez---grin-development-jan-apr-2023) as agreed but when he asked [@davidtavarez](/u/davidtavarez) one week later (2023-5-2) to update the status of his ongoing funded tasks he resisted:

**CC meeting (2023-4-25):**

**l33d4n** : We skipped the first item on the agenda list. I would like to suggest adding to the GK tasks follow-up for every funded task. Once the CC approves funding, it will be the GK responsibility to follow up and update (on a monthly basis?) what the status is.

**dtavarez** : I’ll a PR with that suggestion to add it to the repo officially.

**l33d4n** : This way we will avoid such situations in the future.

**dtavarez** : I support it

**cekickafa** : yes, i support also👍

**anynomous** : I am fine with it. Just a few bullet points will do, but it will avoid that nothing happens without no one knowing about it.

**dtavarez** : Or @cekickafa will you add it to the documents?

**cekickafa** : yes i can.

👍 anonymous, dtavarez

**dtavarez** : Thank you. That was easy. Something else?

**One week later (2023-5-2):**

[@davidtavarez contributions summary & logs](https://forum.grin.mw/t/davidtavarez-contributions-summary-logs/10474/5) [Development and Technical Discussion](/c/techtalk/9)

> No, and I never agreed on participating on any “Progress Tracking Scheme”. I post regularly, I’m reachable, I share updates, links, post, code, etc., I release things when they’re ready. When things are released you can link whatever you want. In order to follow a “Progress Tracking Scheme”, it should be properly defined, and a “Project Manager” role should be created. Keep me out of that. Thank you.

* * *

## **Solution:**

**Freeze any future expenses from the CC fund until clear decisions** are made regarding the responsibilities and roles, enforcement of the spending guidelines and clear and transparent decision making about the follow-up processes.

**For necessary or urgent developments** that is not part of the OC responsibility, it can be discussed specifically and **we can offer a bounty with a clear definition and responsibility** for the end result.

At the same time we can try to understand together how to:

[Minimalism in spending of the Community Council?](https://forum.grin.mw/t/minimalism-in-spending-of-the-community-council/10228/1)

> … work in **subteams** and have **more contribution on a voluntary basis**. This is happening to some extend, people make great contributions to discussions, marketing material, their own websites on Grin and many people use their free time and energy to contribute…

**As long as the wallets are working and the nodes are running, everything will be fine** and I can assure you that the end users won’t even notice it.

The proposal does not include the **role of one GK** which is necessary for transparency and the accessibility of information for the community as specified in the spending guidelines **to close the transparency gap in all the missing reports and meetings notes**.

It would be great if community members who have taken part in previous/ongoing bounties could share their thoughts about the model and their experience in the discussion. [@Nicolasflamel](/u/nicolasflamel) [@renzokuken](/u/renzokuken) [@Scilio](/u/scilio)

* * *

## **Final note:**

**My motivation behind this post is to make sure that the funds are used in the best way that benefits the community and are not wasted or abused without transparent follow-up process and clear responsibilities.**

I know this is a sensitive topic but let’s try to have a **productive and objective discussion based on the facts above**.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #10*

phraudsta:

> This lack of transparency is a huge problem and should be addressed as a matter of urgency. It could be nothing more than a communication issue, or it could be something much more sinister. Consequentially therefor I agree it would be most prudent to freeze the funds pending a deeper revelation or investigation providing that or close to that level of transparency required to be assured of the best outcome for grin.

More fake accounts?

[Screenshot 2023-05-16 1544531160×773 23.9 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/ed639694152d7b590f2a1feb5bbb3b040886e47b.png "Screenshot 2023-05-16 154453")

Anyways…

Of all the issues that could be addressed such as: Auditing the [Atomic Swap PR](https://github.com/mimblewimble/grin-wallet/pull/618) in such a way that it can be released, or continuing with the development of [mwixnet](https://github.com/mimblewimble/mwixnet)… or spreading [MW/Grin everywhere](https://forum.grin.mw/t/mw-grin-workshop-hackaton-in-istanbul/10166)… well… here we going again: [Pause GRIN Community Council - we need your opinion!](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185)

Good luck, this time I’m out of this conversation.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #17*

Trinitron:

> David say’s he’s out of this one, Mike and Neo are mostly gone (not to denigrate their good intentions), Anynomous is receptive to criticism and/or pausing. Who’s the fifth member again?

The last conversation about this lasted 3 months or so, opinions/feedback were asked about whether CC should be paused, you can [read the post yourself](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185), or read the logs in Keybase, I doubt you will, but I hope you do. In summary, after 2 months (and counting) a “Pause” did not get any support…

One could get a “new group” again, and again, and again, and this conversation will never go away and unfortunately the same people who brings this topic again and again will not going to take any kind of responsibility or role because what they are really saying is: “**you should do this or that, not me** ”.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #30*

johndavies24:

> Pretty sure in the time it takes you all to build a tx that you could write down a single line to keep track of it, this was always the expectation and it’s a trivial addition to the task of signing txs

I do not disagree with that… and I am not referring to you at all, you have never stopped pushing Grin forward… and for example, I would have liked to pay more attention when you brought up the subject of Nostr tbh.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #34*

Trinitron:

> I am never asking anyone to do anything. I am saying if no one is particularly doing anything, the spending should stop.

Look how long this post is, for a topic that was discusses already, and after 4 months… again… imagine this type of effort but for what I mentioned above:

davidtavarez:

> Of all the issues that could be addressed such as: Auditing the [Atomic Swap PR ](https://github.com/mimblewimble/grin-wallet/pull/618) in such a way that it can be released, or continuing with the development of [mwixnet](https://github.com/mimblewimble/mwixnet)… or spreading [MW/Grin everywhere ](https://forum.grin.mw/t/mw-grin-workshop-hackaton-in-istanbul/10166)… well… here we going again: [Pause GRIN Community Council - we need your opinion! ](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185)

Imagine a detailed process on how to bring AtomicSwaps to life. That was already paid for, and I don’t see anyone here trying to come up with solutions to deploy it, and no one is complaining about the BTC spent on that… inexplicable… but Ok… or imagine this effort in completing the CoinSwap… again, more BTC were also spent… but no… all this effort to talk about something that was already discussed 4 months ago for months.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #36*

Trinitron:

> Always asking why no one else is doing something else is just the same old redirection tactic.

Interesting take…

Trinitron:

> there will be a special expectation of you.

Is this a topic about me now? again?! what is the obsession with me? seriously, get a life, guys.

Was AtomicSwap voluntary? it was not. Was CoinSwap code written voluntarily? it was not… so, what " volunteer community" you are talking about? “CC work”?.. well, the “solution” is easy, you just need to answer the question: who is responsible of what? you can start by writing those proposals and how to do “follow-up”, and how to “enforce them”… anyone could just do it here: [GitHub - grincc/docs: Documentation relevant for the Grin Community Fund](https://github.com/grincc/docs) but **I know you won’t** , because you (and those creating fake accounts) just want others to do everything for you.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #38*

Trinitron:

> So of course it is about you.

Thanks for the clarification. My advice: get a life, you need one, and remember that envy corrodes the soul.

---

### Post by @davidtavarez ⭐ (2023-05-16)
*Post #42*

Trinitron:

> You ask for $30k funding, complete none of the stated goals, fuck around with nostr a bit, and then come back for another $30k and tell us to get a life if we ask questions.

My guy! I’m not dating you! I’m not gay, do you, but I’m not dating you.

---



## Use Grin Coin as a reserve for more Advanced Fair Tokens
*Date: 2023-06-10 | [Forum Link](https://forum.grin.mw/t/use-grin-coin-as-a-reserve-for-more-advanced-fair-tokens/10579)*
*Importance Score: 85.7 | Core Participants: tromp*

### Post by @minexpert (2023-06-10)
*Post #1*

I created 2 topic but 90% of people didn’t understand what I said. Unfortunately the old quality is no longer here. I missed reading a lot of information here in the past.

I want to collect all the things I said and give advice.

I don’t know exactly what Ignotus thinks for Grin’s future, but I feel like something is going the way he never imagined. Of course he predicted that the Grin price would drop, but I don’t think he ever expected it to drop so dramatically. Currently, Grin daily block rewards have dropped below $3000 but still no buyers. It’s very, very sad.

First of all, I think the experiment of fixed block rewards idea is not very fair. It does not protect the first miner or the first investor at all. Then there is no reason to invest in the first place and protect the network. If you do not protect the network, that network will not work. Therefore, as I mentioned on [this topic](https://forum.grin.mw/t/bitcoin-grin-hybrid-monetary-policy-model/10498), it is a fairer solution to reduce inflation in the first year without making the first investors/miners rich. Everyone should do this self-critism. We can’t blame Ignotus because this was an untested experiment and he warned us all.

**“It’s very young and experimental. Use at your own risk!”**

Secondly, I would like to clarify the issue of POS, POW.

The POS side is growing and developing quite a lot. There is a strong side that processes hundreds of thousands of transactions per second, uses very low fees, and has connections to hundreds of dapps. Every day the POW side is dying and the POS side is getting stronger. There is no POW left in the TOP100 that can hold its value expect Bitcoin.
Grin was born in the dead side. Also, actually it hasn’t been born yet. Therefore, after 4-5 years, if a fully decentralized and confidential network with 1 billion transactions per second on the POS side emerges, maybe Grin will never be born.

However, there is a point that 99% cannot see. Only this situation can pave the way for Grin to become the world currency of the future. Let’s explain this. POW generates money in exchange for a certain amount of energy and effort. You don’t need goverment money directly to produce POW. You need a core, internet and electricity.

However the main source of POS is state money. Since you don’t produce the POS with any labor, you buy the POS using government money. This creates a system that automatically derives its value from government money. The value of government money is also a piece of paper, as it is not tied to anything. The connection between the gold produced by hard work and the state money was cut off years ago.
Thus, because POW is produced by labor, it is not directly tied to government money but indirectly. So what do we will do with all this information?

We will go back and copy system monetary policy of goverment money equal to gold. Grin coin can be a reserve, and new tokens can be created from Grin. This tokens can be on POS with more faster more privacy more scability. The only source for creating this tokens are fair and producing real labor Grin.

XEN made simillar system but XEN is tied to other POS tokens as a resource, and POS tokens are directly tied to government money. Also, XEN can burn and can be converted into other tokens. I don’t think the value of something that disappears from the world and burns can be permanent. In my opinion, reserve money should not be burned, but locked up like gold.

As a result, either Ignotus has to come back, or someone who can activate this idea. Grin can’t be used as Ignotus wants with the 60 second block reward and TPS he has. This is not possible. No matter how much you improve it, its privacy, scalability, fairness and speed will lag behind POS. **So it makes sense for the labor-produced Grin to be a POS reserve.**

---

### Post by @tromp ⭐ (2023-07-12)
*Post #40*

minexpert:

> If Ignotus had known that Grin would drop this much, he never tell only %33 difference between Grin and Bitcoin in the 8 years. He spoke as don’t exaggerate too much. We’re down to $5 million. We won’t still exaggerate? Maybe we should wait $500k marketcap?

Unlike you, Igno was not preoccupied with price and marketcap. Igno was more occupied with making the simplest possible money.

Unlike all other coins, Grin is made for future generations, not to benefit the current generation and least of all to “protect early investors”. It was Igno who proposed the pure linear emission as the epitome of simplicity and fairness.

minexpert:

> Now there are dozens of more scalable, faster, cheaper networks.

More scalable as in allowing such fast chain growth that simple hardware on low bandwidth can’t keep up and takes forever to sync?

Faster as in almost as fast as payment channels that Grin can support?

Cheaper as in setting fees so low that the chain is overrun with spam (see nano/zcash)?

---

### Post by @minexpert (2023-07-12)
*Post #41*

tromp:

> Unlike you, Igno was not preoccupied with price and marketcap.

Do you really believe this? I m asking serious.
When Igno was thinking about inflation modeling, is it possible not to have guess of price and marketcap.

Tromp, I guess you should remember you that we live in the age of technology. The speed of development of technology is exponentially. The pace of development is faster each year than the previous one. If he knew it would drop to $5 million, if he knew 4.5 years of development would bottom out, if he knew that Core developers would leave one by one, do you think he would have chosen this policy? Still not enough for understanding?

While other projects developed over this 4.5-year period, Grin’s development rate decreased exponentially. This is what Ignotus want?

You know what you miss, Ignotus thought that this unique structure would exceed a significant value even with high inflation and he tried to create simple money. However, he was wrong. Anymore, there is no modeling in front of you that you can defend.

Is Igno the culprit? No because no one would know until they tried it. However after trying it, it’s an insult to Ignotus to say oh perfect. If he would be here now he would accept these points and try to develop this more.

There was only one way for Ignotus to prevent all this. Protecting the market cap of the project with a small protection mechanism without making the first investor rich. Then the power wouldn’t have decreased that much. Is it not true? Also If he did, no one would call Grin unfair, no one would say Grin make early investors rich. Then why don’t you still accept that?

You guys still don’t accept and i m sure never accept. There is no development. There is no different idea.

---

### Post by @tromp ⭐ (2023-07-12)
*Post #44*

minexpert:

> There is no different idea.

Grin is the unique coin with a different idea for emission. Tens of thousands of coins decided that the current generation should be able to hoard most if not all of the supply.

Only one coin decided to do things differently, with an eye toward future generations.

But you’re still stuck in the old mindset, wondering how the current generation that you’re part of could have made profits, happily sacrificing the one thing that makes Grin stand out in an ocean of greed.

I’d rather see Grin go to $0.01 than see it abandon its principles of simplicity and fairness.

---

### Post by @tromp ⭐ (2023-07-12)
*Post #56*

minexpert:

> The factor affecting the price is not the amount of increase in supply, but the amount of increase in supply relative to total supply. This is the most basic rule of economics.

Did you pass economics 101?

The most basic rule is about supply versus demand.
If demand grows faster than supply, then price goes up.

After the world population peaks, I don’t see how demand could grow exponentially.

---

### Post by @tromp ⭐ (2023-07-12)
*Post #58*

vegycslol:

> That’s why I’ve asked you how does the genesis block look like.

If you target 1% yearly inflation and want to end up with about 2.7 billion grin after an entire century, then you’d have to set the genesis reward at 1 billion grin; a huge premine.

---

### Post by @tromp ⭐ (2023-07-17)
*Post #70*

minexpert:

> What Tromp said is mathematically completely wrong. Constant block reward does not do fairness. He advocates it. He can’t give any mathematical equations to prove it anyway.

You fail to understand the obvious. Little can be proven until fairness is mathematically defined. Which so far it hasn’t.

But instead of defining fairness exactly, let’s try to define some properties it should have. We can agree that a fair emission should not induce a large wealth inequality. That rules out large premines.
We can also agree that it should not induce large generational wealth gaps either. Let’s formalize the latter property.

DEFINITION:
An emission is _generationally_ fair if-and-only-if no generation obtains more than twice as much of the supply as the next generation.

Note that the factor of 2 easily exceeds one generation of a yearly 2% inflation, making the issue of inflation moot.

Then out of ALL tens of thousands of existing cryptocurrencies, I know of only two which are generationally fair: Grin and Dogecoin. The latter just barely qualifying with its 1.95x gap (see my other post on wealth inequality).

minexpert:

> My proposition is absolutely correct. Only constant inflation can do Full fairness.

You demand mathematical proof of the fairness of linear emission yet you claim fairness of an emission that requires a huge premine.

minexpert:

> Is this easy to do? Not, however, it can be done if an equation is set up that is constantly burning and increasing with respect to the amount held. It’s not impossible.

How about you come back to the discussion when you can _actually_ define an emission that you can argue is more fair than Grin’s trivally defined one.

---

### Post by @tromp ⭐ (2023-07-18)
*Post #87*

minexpert:

> Start the block reward at 300. Reduce by 20 for the first 6 months and by 10 for the next 6 months block rewards. In the second year, reduce block rewards by 5. After 2 years, you continue to give fixed at 60 block rewards because inflation will come to ideal point. After 20 years, when inflation reaches 4%, you can increase the block rewards and keep the inflation at 4%.

That looks rather arbitrary. One way I interpret “fair” is as non-arbitrary. Yours is rather unfair in that way.

Anyway, I found this project that may be more to your liking: <https://bitflate.org/bitflate.pdf>

---



## Funding proposal 1: Parallel Initial Block Download
*Date: 2023-06-13 | [Forum Link](https://forum.grin.mw/t/funding-proposal-1-parallel-initial-block-download/10584)*
*Importance Score: 79.1 | Core Participants: tromp, davidtavarez*

### Post by @Anynomous (2023-06-13)
*Post #1*

This is a new format for governing funding, which I call funding proposals. The purpose is to first get sufficient community support, discussing deliverables and the value for the community and only move to a funding request or bounties if there is sufficient support. This incorporates some of the [feedback on Grin Governance from this discussion](https://forum.grin.mw/t/cc-fund-expenses-responsibilities-spending-guidelines-and-follow-up-processes/10522/75). This new format also takes away some of the work for developers to ‘sell themselves’ via Funding requests, which can be a frustrating experience, right [@davidtavarez](/u/davidtavarez). Note that even if a funding proposal gets sufficient support, the question is if a developer wants to take on the implementation, whether as funding request or a bounty.

## Funding proposal: PIBD implementation in Grin++

### What: Parallel Initial Block Download (PIBD)

PIBD is a new messaging system that allows you to download blocks simultaneously from many peers, check them, verify them, and rebuild your history. **PIBD is truly decentralized, secure and robust!** There is some additional overhead in data transferred, so currently PIBD is **not a faster** way to download the blockchain. However, as anyone knows who ever used Torrents or other decentralized downloading systems, potentially downloading from many peers in parallel can be used to make downloading faster, even with added overhead, since most users have a lower upload speed than download speed. So PIBD might in the future lead to lower initial syncing time.

### Why: Currently both grin-wallet and Grin++ download the blockchain up to the horizon as a .zip file.

This is problematic for various reasons. The biggest issue is that the process is unstable and error prone. Your node asks a single peer to download the .zip file. If that peer goes offline or is malicious, he or she can interrupt your download, corrupt your download, or keep you waiting for very long!
Anyone who synced his node or wallet multiple times knows from experience that the experience is highly varying, sometimes the blockchain syncs fast, sometimes incredibly slow, and sometimes it requires manual restarting the wallet or sync process. In other words, the initial sync as .zip file makes a horrible user experience. Secondly, it is not really decentralized to download from a single peer.
PIBD will solve the above problems and is already on test-net and soon on main-net in grin rust . However, the minority of nodes out there run Grin++, meaning grin rust nodes would only be able to use PIBD to download from rust nodes which hampers its effectiveness and hampers decentralization. Even worse, Grin++ would still be stuck with the old and poor way of syncing using a .zip file. Therefore implementing PIBD in Grin++ is essential for the whole network to take full advantage of PIBD.

### What we need from you:

We need your opinion, (dis-)likes, questions (also dumb ones) as community members. The purpose is for these requests is to be shared on social media, start a discussion on the value of funding the implementation of features for the community, and hopefully collect sufficient community support before initiating any funding requests. There is no fixed threshold since that would give spammers ultimate power over Grin governance. Your opinion and arguments are counted, and weight based on their validity, sound argumentation and your historical contribution to Grin.

Find [here](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0020-pibd-messages.md) a better explanation of PIBD by [@Yeastplume](/u/yeastplume)

Or [here](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0022-pibd-deployment.md) a more detailed technical explanation by [@Yeastplume](/u/yeastplume)

---

### Post by @Anynomous (2023-06-13)
*Post #2*

The above is a funding proposal. Anyone can make one, feel free to do so !
Here I want to express **my opinion and support for this proposal**. In my personal opinion, implementing PIDB in Grin++ is the single most important thing for the project and the community , for a) keeping the node network unified, b) for making the network more decentralized and c) for improving the user experience for users who first run their node and wallets. Like slate-packs, PIDB is one of those changes that might appear too technical for some users to truly understand or appreciate, but one that is very important for the project. I hope my explanation might help in clarifying the value of PIDB, feel free to ask questions or add explanation of your own to make it more clear.

---

### Post by @Anynomous (2023-06-14)
*Post #8*

ardocrat:

> I think it will be better to make PIBD sync optionally at beginning, can be option at **grin-server.toml** config.

I think it would be best to make PIBD default if it is stable on mainnent but keep the .zip a an option in the config files and in the code as backup sync method. Perhaps for some low computing power devices, the PIDB sync method is slower due to the calculations it involves. I can image the .zip files can in the future be modified (breaking up the chain into a few.zip files) to sync new archive nodes with existing archive nodes.

Regarding funding as bounty or as funding request, **I propose a hybrid solution** , see below the explanation. I think this address all the concerns and covers most risk to the community funds.
[@Cobragrin](/u/cobragrin), [@ardocrat](/u/ardocrat), [@l33d4n](/u/l33d4n)

### Bounties with milestones and conditional upfront payment

This solutions is similar to how [@Yeastplume](/u/yeastplume) is paid and to what we did with CoinSwap bounties (milestones 1,2 and 3)

1. We break down a funding proposal into deliverables with a bounty for each milestones/deliverable
2. We can pay milestone bounties upfront so developers do not get into problems with paying their bills
3. To have access to upfront payment there are two conditions a) all the deliverables for the previous funding requests must be finished, b) upfront payment for a milestone/deliverable is only accessible to developers and community members with a proven track-record such as [@davidtavarez](/u/davidtavarez) and [@Yeastplume](/u/yeastplume) .

Each time a milestone is reached and finished, we can pay the next milestone bounty upfront if these conditions are met. I think this would be the best compromise between being practical and considerate to our long term developers while strictly managing and covering risks for community funds. Let me know what you think, would this be a good solution?

---

### Post by @ardocrat (2023-06-14)
*Post #9*

Anynomous:

> We break down a funding proposal into deliverables with a bounty for each milestones/deliverable

This is good idea.

Anynomous:

> We can pay milestone bounties upfront so developers do not get into problems with paying their bills

I think motivation is lowering at this case. Full time devs are usually getting their salaries in the middle/end of month, cause they know if they will not work they will not receive salary. I think it can be no problem here if tasks will be divided in small parts.

Anynomous:

> only accessible to developers and community members with a proven track-record

It creates group of _favourite_ persons with special privileges. I think it will be more fair for all people who is going to be paid by CC Fund to follow same rules and be equal. We already had problems with track-record of last 3 months, so we learned from this.

I still think we need to form bounties as it was initially at CC, so everybody can apply to help, take free tasks and so on, I just don’t support idea for only 1 dev per project, collaboration is a key. For example, [@david](/u/david) can help [@davidtavarez](/u/davidtavarez) and get paid too or any other interested C++ dev.

---

### Post by @Anynomous (2023-06-15)
*Post #23*

All the above mentioned issues raised are all covered for by:

Anynomoud topic:10584:

>   3. To have access to upfront payment there are two conditions a) all the deliverables for the previous funding requests must be finished, b) upfront payment for a milestone/deliverable is only accessible to developers and community members with a proven track-record such as [@davidtavarez](/u/davidtavarez) and [@Yeastplume](/u/yeastplume)
>

But your opinion is noted, you basically want pure pay after bounties.

It is fair since everyone can build a reputation and track record to get access to upfront payment. Since it is on deliverables level, the risk to funds is much smaller than in the current 4 month upfront paid Funding Requests and the inconvenience is much less for developers who already have to wait since going from approval to payments can take up to two weeks.
Besides, we also pay [@Cobragrin](/u/cobragrin) upfront, otherwise that would be to unfair compared to long term devs.

Regarding funding PIBD. Implementation will take months, so we can wait but do not have to since it will take time to implement and test in Grin++ before getting activated.

---

### Post by @davidtavarez ⭐ (2023-06-15)
*Post #27*

l33d4n:

> Now just to make it clear, **the previous tasks are in progress and not abandoned** but the status is still unclear because of lack of communication, ego games and drama all around.

You are correct, nothing has been abandoned. Here you can follow the progress of each task individually: [Grin++ v1.2.9 · GitHub](https://github.com/orgs/GrinPlusPlus/projects/1) more details on each repo ([PR#221](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/221/files) & [PR#7](https://github.com/GrinPlusPlus/GrinPlusPlus/pull/221/files)). Anyone can try it for themselves and feel free to contact me with any questions.

I have lost interest in participating in conversations that never end. There are better things to spend time on, for example: The recent NBA postseason was epic. I would have wanted the Heat to win, but maybe it was finally Denver’s time. I wonder what Boston will do for next season, any ideas?

---

### Post by @Anynomous (2023-06-16)
*Post #29*

AceKaplin:

> Bounties bounties bounties.

We have bounties, we have had Funding Requests. So far bounties did not work out so well, only coin Swap and the Python cffi secp256k1-zkp wrapper worked out with bounties.
Switching to bounties only would be more limiting than our current system. I see no logical reason why having only bounties instead of bounties + RFC or conditional pay upfront bounties would be better. Dirrent funding types attract different types of developers and we need all devs we can find.

---

### Post by @tromp ⭐ (2023-06-17)
*Post #37*

AceKaplin:

>   * deliver: a miner that can achieve 1GPS on fancy Mac proprietary software machine
>

My bounty offer [1] required only 0.5 GpS on an M1 Ultra.

[1] [Bounty - 1 BTC + 100 Grin for a MacOS M1 C32 Open Source Miner with ≥0.5 Gps - #2 by tromp](https://forum.grin.mw/t/bounty-1-btc-100-grin-for-a-macos-m1-c32-open-source-miner-with-0-5-gps/9652/2)

---



## Suggestion: Return CC funds to OC
*Date: 2023-07-05 | [Forum Link](https://forum.grin.mw/t/suggestion-return-cc-funds-to-oc/10619)*
*Importance Score: 73.7 | Core Participants: tromp, davidtavarez*

### Post by @Trinitron (2023-07-05)
*Post #1*

I think I’ll keep the first post here brief, I may add more detailed thoughts later but the point of this post is simple and i don’t want to cloud that.

Given the recent changes CC is undergoing, I suggest that the safest course of action might be to return the CC funds to OC at this time.

Maybe CC should be reformed and refunded again, maybe CC’s bounties need to be honored, maybe certain CC funded projects should continue however they are funded. But given the turmoil, I think it would be safest to get the funds back under the control of trusted long term active key holders in the interim.

---

### Post by @davidtavarez ⭐ (2023-07-06)
*Post #9*

Trinitron:

> Given the recent changes CC is undergoing, I suggest that the safest course of action might be to return the CC funds to OC at this time.

We finally agree on something

AceKaplin:

> CC was a valiant effort, but I don’t think its working. The mission of CC is unclear, but it is clear that CC is not executing well on any mission. No offense to any of the people who have committed their personal efforts to CC. We can try again another way.

I second that.

Neo:

> How is giving the funds back to OC going to help the project? It seems more like a step backwards.

Sometimes a step backwards opens a new path forward.

Trinitron:

> If users had just been redirected to the forums instead of Telegram there is plenty of volunteer support here.

Not true at all, hundreds of times people are invited to the forum, but people still choose Telegram. Anyway, it is not the topic here.

noobvie:

> Maybe, in the OC, we need someone has ‘leadership’ characteristic like an service delivery manager for managing projects to move forward better.

Last time the guy doing that kind of task was unfairly destroyed. I doubt anyone will do it again.

Trinitron:

> Who is even going to run a coinswap server? I can hear the funding request for that coming around the bend already

Funding request? publicly running a CoinSwap server would be suicide, funded or not. Please do not do such a stupid thing.

Trinitron:

> But my question would be did the more liberal CC actually end up producing anything of value?

Not so much as to compensate the weaknesses.

The main problem was not the conservative attitude of the OC. There was general support for the conservative position on changes to the protocol. The main problem was the OC’s total disconnect with the rest of the Community. Users, miners, Exchanges, and enthusiasts in general faced challenges while the OC didn’t have time for it. Years ago it was more evident because the community was much larger and active. The CC came, but failed, to compensate for the vacuum left by the OC, while the latter continued to take care of its own things.

The issue is that one could create the perfect process and structure and still fail because there is no one to fill those positions. The “anyone can do it” is a failed statement, combined with “we are only key holders” is a recipe for disaster. With the OC it was clear who did what, and what their duties were. I still maintain the opinion that the OC could have paid more attention to the rest of the world outside of Rust, but the “few things” they did they did well.

The experts in saying a lot and doing nothing can continue designing in their head the perfect process and the ideal structure, if they want, I doubt it, but I don’t care either. Anyway, the CC experiment is already dead, so logically speaking the next step is to support what’s [@Trinitron](/u/trinitron) is suggesting here.

---

### Post by @davidtavarez ⭐ (2023-07-06)
*Post #13*

ardocrat:

> My opinion is to not destroy CC but to involve more active members

Go ahead and get involved, I heard that 2 CC guys stepped down.

ardocrat:

> it could be just one bad period at his life

First, I’m in the best period of my life, but that’s the point, I have a life. Second, I’ve said it too many times, I’m more than tired of recycling the same topics over and over again, and I’m not going to waste my time on that stuff. When I discovered Grin it was fun, now Grin is far from fun.

ardocrat:

> we are not even speaking about privacy

I wonder why…

ardocrat:

> It should be necessarily for them to work with community like write topics and create discussions about different parts of protocol and **privacy** itself.

This is what I do not understand. Most people think they have the right to demand to others what to do and how to do it. It won’t work that way, ever, no matter how much it is repeated. People should do whatever they want with their time. There was never a “Grin Academy” where one went to learn about Grin. There is enough information published for people to download, print it out and sit down and study on their own.

ardocrat:

> As it was said: “don’t hate the player hate the game”.

Well, [@Anynomous](/u/anynomous) has been very consistent in his thinking all along.

[@vegycslol](/u/vegycslol) is not wrong about that, I don’t know the context of the screenshot, but that statement is not wrong, you don’t want people who don’t know how Grin works making decisions that might affect Grin. No one will take their car to a medical doctor for mechanical work. To put it simple: the opinion of people who do not know how to do anything should not weigh one iota when it comes to making a decision. I know it’s an awkward conversation.

---

### Post by @davidtavarez ⭐ (2023-07-06)
*Post #15*

[Pause GRIN Community Council - we need your opinion!](https://forum.grin.mw/t/pause-grin-community-council-we-need-your-opinion/10185/10)

> **if no one assumes any responsibility of any kind, then there is no reason to exist**.

Real. I was damn right.

The passive attitude could only work in a large and vibrant Community, full of motivated people. One can build that large and vibrant Community, or one can simply withdraw, but to build it you have to work for it, and then the conversation is much different.

CC’s position is not wrong per se, but the conditions necessary for it to work do not exist, have not existed, and I doubt that they will exist for a long time. So the healthy thing to do is to accept reality, and return to a safer position until better conditions exist.

---

### Post by @davidtavarez ⭐ (2023-07-06)
*Post #18*

ardocrat:

> If only it could be so easy as we still have problems with peers and initially sync on Android (issue created year ago), Tor is just part of pain for better privacy.

And before that there was no Android app, and before that there were other problems, and before that bridges were not supported, and limited to advanced users, and before that many other things were not included, and before that there was not that friendly user interface,… but wow, you just found out that development is a continuous process. Congratulations, you won a cake

The issues with peers will not longer exists btw, I invite you to follow the next release [Grin++ v1.2.9 · GitHub](https://github.com/orgs/GrinPlusPlus/projects/1) binaries can be tested too already. But that’s another conversation.

---

### Post by @Neo (2023-07-06)
*Post #34*

davidtavarez:

> Sometimes a step backwards opens a new path forward.

davidtavarez:

> The main problem was the OC’s total disconnect with the rest of the Community. Users, miners, Exchanges, and enthusiasts in general faced challenges while the OC didn’t have time for it. Years ago it was more evident because the community was much larger and active.

If this is all true, then how would taking a step backwards ever open a new path forward?

CC gave you a mechanism to obtain funding and continue working on Grin++, why would you want to close this door on other future developers who could also work on Grin++ or on other projects outside of the core codebase.

OC have only funded 1x dev over the past 2 years to continue maintaining the core codebase. It’s hard to see this changing anytime soon.

Trinitron:

> But looking at prospectively at the future I just don’t see a lot of upside. We either have trustworthy members who are barely able to be present enough to sign transactions, or we potentially hand the keys over to a new group of replacements. I do not personally see an adequate pool of applicants who meet both the trust and activity requirements to even live up to the old CC

What upside do you see to the OC controlling all the funds? And how can you judge whether we have an adequate pool of new CC applicants, when we haven’t even asked for submissions yet?

Trinitron:

> I’m still uncertain about the idea of anonymous or semi anonymous users holding keys, which would make it somewhat hypocritical of me to join in my current capacity. One of the reasons I trust OC is the majority of them are publicly known under their real name.

You should know that fully doxed people rug projects all the time. It never offers the protection some people assume. Also, there’s no true Anon on the CC, it would be easy to dox any of us. I’d be open to doxing myself anyway.

Trinitron:

> If the majority opinion is to retain a community funding mechanism/group. I would like to get more opinions on this idea. From current CC members, community, and eventually from OC about whether they’d accept a plan like this.
>
> This would give the original CC members who are departing a safe exit from their keys, free from concern that they could be involved in the beginning of any sort of transfer or succesor mishap.
>
> It would also give OC an inherent veto over CC spending, if the CC fund remains under their keys. To me this would be an explicit intention. I do want OC to have veto power.
>
> I think I would consider this a prerequisite to my own potential participation in or support of any new council formation/election.

If we’re going to maintain a community funding mech, then I don’t see the point in dissolving the CC. OC don’t have the resources to be signing txs for community funding requests- It would never be as simple as just signing a tx, they would then need to do their own due diligence on everything aswell, because, ultimately it would all fall back on them.

The better option imo would be for the OC to encourage more people to put their name forward for the CC.

It’s disappointing you’ve been active is the project this long, seen all the pitfalls, stress and issues that unfolded when OC had full control of everything and now want to re-centralize the project and return funds to a more depleted/ less motivated OC

^And this is not a stab at OC, but the reality is life happens, time is limited and people move on/ focus on other things and then sometimes go full circle.

It’s also disappointing that you’re now setting conditions just for your “participation”.

Who actually controls all the OC keys atm? It must be documented somewhere in the repo, but I had a quick look and can’t find it. I’m not sure if all key holders are active on the forum anymore? So you might be better posting this on Keybase or sending them DMs with reference to this post.

---

### Post by @davidtavarez ⭐ (2023-07-07)
*Post #39*

Neo:

> CC gave you a mechanism to obtain funding and continue working on Grin++

Yes, and I said before many times that **I am very grateful for that**.

Neo:

> why would you want to close this door on other future developers who could also work on Grin++ or on other projects outside of the core codebase

Where/When did I say that I want to close this door? I never did instead I have been an advocate of funding others. **I think FRs are a excellent mechanism to speed things up and push Grin’s development in general**. I said in this very thread that I still maintain that one mistake of the OC was to just focus on Rust while ignoring the “pains” of the Community. How can someone come to the conclusion that “I want to close this door”? It’s nonsense, if that’s true, I would also be “closing the door” on myself, why would I want to “close the door” of being funded to myself? I don’t understand.

This is one of the things I am very tired of. It is impossible to have a productive conversation because everything becomes about expressing oneself in a way that is contrary to the other for the simple fact of being contrary. It is so childish, unproductive, a total waste of time and leads to nothing. Look, I don’t think [@Trinitron](/u/trinitron) likes me and he is not my favorite person either. The guy had expressed before that he is against of funding me and critics my work all the time! it’s no secret, but I’m not going to crash my keyword with my head because I see myself agreeing with him. I honestly think [@Trinitron](/u/trinitron) is mostly right this time, and I choose to focus on that rather than the disagreements, have the conversation and move on with my life. Simple.

Neo:

> OC have only funded 1x dev over the past 2 years to continue maintaining the core codebase. It’s hard to see this changing anytime soon.

Yes, I agree and I think that is not good for Grin.

oryhp:

> If we can find trustworthy members, I think this would be good

I don’t think the main problem is to find trustworthy members to “hold the keys”, although I think it is a problem, the main problem is this

davidtavarez:

> The passive attitude could only work in a large and vibrant Community, full of motivated people

And I stated:

davidtavarez:

> CC’s position is not wrong per se, but the conditions necessary for it to work do not exist, have not existed, and I doubt that they will exist for a long time

And even if one does not want to or not, **the “Community” expects an active role** from at least the majority of the members of the Community Council. I myself believe that, under the current conditions, the members of a Community Council should have an active role, otherwise we are in a worse position than before, which is what is currently happening. **The community is so small and so unproactive that maintaining an apathetic attitude is in fact a misstep**. I will never “tell” or “force” anyone to do something they are not willing or want to do. I respect their decisions as much as I expect people to respect mine, I have no beef, and that’s why I preferred to step down.

Trinitron:

> Grin is not a democracy

Correct. This is something that people overlook time and time again… It should be clear in everybody’s mind that: **Grin should never be a democracy**. This is another reason why, _under current conditions_ , the OC is the most appropriate entity to have the final say on the allocation of the curse, I mean funds.

A Community Council should always listen to the Users, Miners, Exchanges and Enthusiasts. A Community Council should drive the solutions to the Community’s challenges, and based on those challenges a Community Council could use the mechanisms of Funding Requests and Bounties. So far so good, but **these activities require an active role**. The “anyone could do it” is not working and will never work, unless the AI takes over or you create a DAO and write some smart contracts, and good luck with that in a Community of no more than probably 2 fully active developers. But I digress. My point is that the conditions are not in place for a passive Community Council to function, this is becoming increasingly clear.

As for the Funding Requests is even worse. I understand why one might want to disassociate oneself from the responsibility of approving or rejecting a request. That being said… not all opinions should carry the same weight when making a decision. A Community Council must, of course, listen to all opinions to have a overall understanding of the Community’s sentiment, but the final word must not be spoken by people who have little or no knowledge of the subject.

Once the Lenberg asked me something like this: “ _would you fund a person who is not able of defending his work?_ ” and the clear answer is: no. But now the conditions are completely different. Before one had to defend oneself in front of a group of technicians, today, as we are talking about a “Community Council” a developer has to argue with people who can’t even read your code, have no experience building anything, have no knowledge of how things work, don’t understand the development process, can’t review your code, and/or don’t even use your software. Now, add the tribalists to that equation as well, people that are against you or against what you do just because. Why do these people have to say at the time of making a decision? But more importantly, why would a developer open a Funding Request or take a Bounty? Let me answer: no one will. The market is flooded with coins/tokens that can be made without having to go through that circus. The few people writing code right now for Grin are people who really believe in Grin, and what is the payback? The most unpleasant experience in the crypto scene. Good luck attracting new collaborators or retaining the little few of them, you’re going to need a lot of it.

If the Community Council is only a “key holder” there would be no difference in returning the funds to the OC, is that simple.

---

### Post by @tromp ⭐ (2023-07-08)
*Post #44*

In the interest of decentralization, the OC would rather not see funds returned. That would only be a measure of last resort if the CC sees no way to safeguard the funds.

---



## Meme contest: Anything goes, bonus theme - the bottom is in...or is it? :scream:
*Date: 2023-08-08 | [Forum Link](https://forum.grin.mw/t/meme-contest-anything-goes-bonus-theme-the-bottom-is-in-or-is-it/10669)*
*Importance Score: 97.5 | Core Participants: *

### Post by @Anynomous (2023-08-08)
*Post #1*

# Meme contest: theme - the bottom is in…or is it?

A good time for some memes. I will donate the first 42 Grin, who knows, maybe the Grin Community Council will donate as well.

**The rules:**

1. You can share any kind of meme you made that involves Grin.
2. Prices are distributed based on total accumulative likes for memes
3. The meme contest ends at September 30, when all votes/likes are counted

Feel free to donate your Grin to the price fund, donate your time as an artists/mememancer , or simply enjoy up-voting memes.
Fee free to share any of these memes or the link on Social Media, only votes on the forum count for prize money.
I will kick of this meme contest with one of my creations!

Edit Bounty is now
42 Anynomous
88 noobvie
…
**Total 130 ツ**

1st price 40%, 2end 30% 3rd 20%, 4th 10% of the price money. 5th or higher place is no price money but eternal fame as grin mememancer .

Your donations to the price-pot can be made via the Grin CC wallet, all transactions will be added to the price money unless specifically mentioned before sending the transaction:
`grin1jezf3lkcexvj3ydjwanan6khs42fr4036guh0c4vkc04fyxarl6svjzuuh`

_**Disclaimer: By the time we are done with this meme contest, it might that the total price is worth 0 USD! Invest time at your own risk! **_

---

### Post by @l33d4n (2023-08-08)
*Post #7*

My TOP10

Anynomous:

> the bottom is in…or is it?

[image500×709 44.8 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2d463658490ce5bba9f268bcbb028e5d7fa782a3.jpeg "image")

Anynomous:

> You can share any kind of meme you made that involves Grin.

[image685×512 64.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/20dbca936a8d80f455e282bd72f8e8d1cbfa5660.jpeg "image")

[image809×500 38.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/2/2b550bd05f6bfc12c5ee9868126e082ab361af39.jpeg "image")

[image589×588 47.6 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/e3d318695060c8fe5dbc94306a4aef43f12def71.jpeg "image")

[image1280×1047 81.9 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/985935f7514f4788f82e8b811ce7ac88e04f186a.jpeg "image")

[image1080×1219 40.4 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b41e3e4a1745fc8dd723c99c3a61953d39f48683.jpeg "image")

---

### Post by @noobvie (2023-08-08)
*Post #11*

[Red - Meme 24500×5400 321 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b4c7538730ecb73988fc3391cb23a5eb914e837f.jpeg "Red - Meme 2")

---

### Post by @noobvie (2023-08-12)
*Post #29*

[Come-on-do-something-Grin-coin-meme1000×1200 47.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/d/d42df924c98e08350dee7a3fa474389ca5cf6c70.jpeg "Come-on-do-something-Grin-coin-meme")

---

### Post by @Doogevol (2023-08-16)
*Post #35*

[Ipollo G1? Should I buy it or not?](https://forum.grin.mw/t/ipollo-g1-should-i-buy-it-or-not/10520/14) [Mining](/c/mining/5)

> Probably it is not worth it to buy G1 for more than $4000. But the data to calculate it correctly is not available. The Network difficulty is declining. (I have no good grin explorer source visualization.) From my memory the Hashrate was long time around 10k Graph/s and now the Hashrate is about 7k Graph/s. So what happens to the Miners? On the other public chain where G1 could mine (MWC) the difficulty is also declining. Probably some miners are broken. Hopefully some mine only part of the d…

---

### Post by @transatoshi (2023-08-18)
*Post #44*

[grin_meme1941×750 131 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a37bd44276e50703b94b7786a071cabac899e9ba.jpeg "grin_meme1")

---

### Post by @God (2023-08-25)
*Post #66*

The emission schedule was always the problem. If grin had the same emission schedule as bitcoin it could have done better against the dollar

---

### Post by @Anynomous (2023-10-02)
*Post #86*

And the winners are:
[@Anynomous](/u/anynomous) 53  52 ツ
[@Doogevol](/u/doogevol) 37  39 ツ
[@acidmax](/u/acidmax) 32  26ツ
4rd place to @feedmeastraysa 22  13 ツ

You will be contacted to receive your price.

---



## Suggestion: Make DEX - Gate.io is Over
*Date: 2023-09-03 | [Forum Link](https://forum.grin.mw/t/suggestion-make-dex-gate-io-is-over/10713)*
*Importance Score: 138.4 | Core Participants: tromp*

### Post by @minexpert (2023-09-03)
*Post #1*

[Gate.io](http://Gate.io) has restricted trading of all privacy coins in some countries. Nor do they say which countries are open to use. It is within the countries banned in my country.

I’m a little sad about that because Gate was a good exchange with real Grin liquidity, always allowing wallet transfer. It has always supported Grin. Although it used a method “memo” in the transfer, it was fine.

However, this is not a very important issue. Centralized exchanges are now cornered by states. The Liquidity Center is moving more and more from exchanges to DEXs. Therefore, Grin’s biggest need right now is new DEXs. Now, there is only a semi-decentralized Tradeogre and it works fine. But with Gate gone, sticking to one exchange is risky. If one day Tradeogre’s server goes into trouble or the exchange decides to shut down, Grin trading will be disrupted. Therefore, the whole community from A to Z needs to work for DEX. This is the best contribution you can give to Grin.

**Here are some of my suggestions.**

* For Grin, announce the bounty for developers who can create a decentralized exchange and say you will always support it.
* Contact DEXs that support privacy coins and encourage them to list by saying they can draw liquidity as Gate is shutting down.
* Contact Old Core Devs. Maybe one of them will make a final contribution and lead the way for a DEX.

It was an inevitable end. In my opinion, all privacy coins will be delisted from centralized exchanges over time. Therefore, today is the day, moving to DEXs.

---

### Post by @minexpert (2023-09-05)
*Post #11*

I’m not sure listed in Bisq but I see that the board is empty.

[bisq.markets](https://bisq.markets/en/market/grin_btc)

### [mempool - Bisq Markets](https://bisq.markets/en/market/grin_btc)

Explore the full Bitcoin ecosystem with mempool.space™

My call is not about Tradeogre is bad or good. What will happen if the tradeogre suddenly shuts down or if they get hack attack or if the server crashes? Since it remains our only source, a second source is required. That’s why I advice to work on this issue rather than waiting like a believer. If it is listed on bisq, a call can be made to the community for using it. It can be said that existing DEXs can list Grin. If they lists, we can say, we will make announcements on twitter, forum and telegram for community to use it.

Also, just being listed in one place is incompatible with decentralization. Igno, i hope you are seeing this situations.

---

### Post by @Cobragrin (2023-10-17)
*Post #40*

We can open a _private telegram channel_ for technical assistance and help if they like. Here Exchange-FAQ for integration, you can forward them.

[github.com](https://github.com/cekickafa/hub/blob/main/exchange-faq.md#info-table)

#### [cekickafa/hub/blob/main/exchange-faq.md#info-table](https://github.com/cekickafa/hub/blob/main/exchange-faq.md#info-table)

## Info Table

| Item | Link/Answer |
| ---- | ----------- |
| Blockchain explorer | [GrinExplorer](https://grinexplorer.net) |
| Technical documentation | [Grin documentation](https://docs.grin.mw), [Grin node API](https://docs.rs/grin_api/latest/grin_api), and [Grin wallet API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api) |
| Average block time | 60 seconds |
| UTXO or account model | UTXO |
| Consensus mechanism | Proof of work |
| Proposed number of on-chain confirmations for deposit | 30 |

## Grin SDK Location

The official [Grin node](https://github.com/mimblewimble/grin) and [Grin wallet](https://github.com/mimblewimble/grin-wallet) implementations provide APIs for address generating, offline transaction building, signing, decoding, etc. These API endpoints are separated into owner and foreign accessible methods which are documented here.

- [Grin node owner API](https://docs.rs/grin_api/latest/grin_api/trait.OwnerRpc.html)
- [Grin node foreign API](https://docs.rs/grin_api/latest/grin_api/trait.ForeignRpc.html)
- [Grin wallet owner API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.OwnerRpc.html)
- [Grin wallet foreign API](https://docs.rs/grin_wallet_api/latest/grin_wallet_api/trait.ForeignRpc.html)

This file has been truncated. [show original](https://github.com/cekickafa/hub/blob/main/exchange-faq.md#info-table)

---

### Post by @tromp ⭐ (2024-07-10)
*Post #63*

TO = Trade Ogre <https://tradeogre.com/exchange/GRIN-BTC>

---

### Post by @trab (2024-08-17)
*Post #75*

mister.monster:

> adapt it to work with basicswapdex.

Here is the page that shows what to do to integrate a new coin on basicswap

[academy.particl.io](https://academy.particl.io/en/latest/basicswap-guides/basicswapguides_apply.html)

### [BasicSwap DEX Coin Usage Guide — Particl Academy latest documentation](https://academy.particl.io/en/latest/basicswap-guides/basicswapguides_apply.html)

Add your coin to the BasicSwap DEX.

> Because BasicSwap is an entirely cross-chain DEX, there are basic requirements that a coin must possess to be readily integrated.

> **The blockchain…**
>
>   * Uses UTXO scripts
>   * Has CLTV or CSV
>   * Has Segwit enabled
>   * Works with watch-only addresses
>

---

### Post by @natsu (2024-08-20)
*Post #80*

It’s worth noting Particl has no liquidity for many years because the dev team controls virtually the entire supply. It was 50% mined in its first two weeks, and then went proof-of-stake with 50% going to a devtax. Also there was an emission glitch a couple years ago, which its devs responded to by freezing the entire RingCT pool and requiring everyone to send outputs through a turnstile for verification, which is generally not a thing you want to do with a privacy coin.

Per salvaging reputation, BasicSwap doesn’t charge trading fees but it is designed for providing swap liquidity to the Particl Marketplace. All trades on the marketplace have to transition through the PART token due to how its escrow smartcontract works, even if the source and destination currencies don’t include PART. So calling BSX pro-bono is not exactly accurate, it’s intended to source your liquidity to be used to drive up the value of the PART token.

---

### Post by @mister.monster (2024-08-29)
*Post #85*

I’ll just put it out there that I am not a fan of particl, I do not own any particl, I will not use particl.

Their plans to roll it into their particl client are of no consequence, the only thing that you could consider integration between the two is they both use the SMSG protocol (a fork of bitmessage which, from my topical exploration appears to be better) and so using either strengthens the SMSG network that they both rely on. That basicswap was designed with integration into a particl client in mind doesn’t affect it at all, there’s nothing dishonest about wanting to do that. My only concern with the Dex is if it were to rely on the particl network. It does not. If they were to ever try that, well, it’s free software and the Monero community is very vigilant.

My only concern with engaging in this discussion is that I’d like to see Grin succeed. Atomic swaps are the only way that some developers can ensure liquidity for a coin and not have to rely on the approval of some product manager or marketing director. And you go where the liquidity is, as of right now the largest aggregation of atomic swap implementations is basicswap, working an existing protocol to fit into it is the lowest effort, highest potential reward endeavor in this regard. It’s basically a no brainer, all the noise is a distraction, either you want to see Grin succeed or you don’t, and no offense to you but basically every thread I’ve read on this forum, conversations about anything and everything get derailed with minutae and wind up petering out and nothing of consequence winds up happening.

It doesn’t take a committee to build this stuff, only a motivated hacker with the right skill set. I’m not here to convince everybody, only hopefully to convince the person that will decide to do it, I wish that were me because I’d do it in a heartbeat if I had the expertise to do so. Imagine a Grin without any reliance on centralized exchanges, being one of the first coins to be available trustlessly, in the package that is carrying the lions share of the work and users of such technology. Not to be a prick but I don’t understand why we are even still sitting here talking about it.

---

### Post by @trab (2025-05-28)
*Post #119*

gig:

> And yet all I hear is interest in CEX listings. Are we mad? Are we impregnated with bad actors? Or am I missing something?

Can the community show more support for this?

[github.com/haveno-dex/listing](https://github.com/haveno-dex/listing/issues/82)

####  [[Crypto] Add Grin](https://github.com/haveno-dex/listing/issues/82)

opened 08:21PM - 22 Nov 24 UTC

[ trosel ](https://github.com/trosel)

crypto: coin

\- [X] I confirm there are no other open issues about this asset \- [X] I underst[…]()and that to actually add the asset to Haveno, a PR from the developers/community of the proposed asset might be necessary \- [X] I understand that adding the asset is at discretion of the Haveno Core Team and applying doesn't necessarily imply acceptance ### What's the ticker symbol of the project? GRIN ### Why should it be added to Haveno? How would it benefit the project and the community? Grin has a lot in common with Monero. It is one of the few non-scam coins out there. It has a good community all around the world. Excellent proof of work mining economy. Just needs more liquidity (on and off ramps) and Haveno could benefit from that influx. ### Is it an Ethereum token (ERC-20)? \- [ ] Yes \- [X] No ### Was the coin pre-mined before public launch? \- [ ] Yes \- [X] No ### Is there a dev fee for the project maintainers? \- [ ] Yes \- [X] No ### Please provide resources about the project (Website, Twitter, etc) Social media is decentralized across a number of accounts. The main website is https://grin.mw/ ### Additional notes The Grin No List explains the ethos very well: ``` no on-chain addresses no visible amounts no transaction history no bloat no reward halvings no supply cap no trusted setup no checkpoints no ring signatures no moon math no symmetric PoW no ASIC resistance no ICO no premine no instamine no airdrops no mining tax no masternodes no middlemen no partnerships no room for spam no ordinals no NFTs no staking no coin burning no bs ``` https://github.com/mimblewimble/docs/wiki/No-this%2C-no-that And here is an excellent list of blog posts that go into more depth on Grin https://phyro.github.io/what-is-grin/

---



## A new grin explorer
*Date: 2023-10-25 | [Forum Link](https://forum.grin.mw/t/a-new-grin-explorer/10798)*
*Importance Score: 93.4 | Core Participants: tromp*

### Post by @vegycslol (2023-10-25)
*Post #1*

I’ve created a simple explorer which is currently available at <http://107.175.127.117>. Since i’m not a devops guy I hope someone else can host it somewhere. I’m hosting it now so that people who are testing stuff can use it.

Functionality:

* block-list + block-detail
* search (click on `?` icon to find out how to use it)
* it should display reorgs of length more than 1 and allow following the reorged blocks to see what happened
* price → for testnet it shows 0, for mainnet it shows the current tradeogre price
* graphs → currently there’s only one graph showing relation between inputs/outputs/kernels per day
* `testnet` explorer is synced on non-archive node and thus lacks early blocks while `mainnet` explorer is synced on archive node

Disclaimer: I’m not a designer so the page design is not top notch. I’ve made some assumption on what the node sends me when a reorg happens and if this assumption is wrong, then explorer might not report them correctly. The explorer is currently importing older blocks from the mainnet. At the time of writing, it imported around 20% of latest blocks and is expected to reach the genesis block in around 35 hours. I’m also sure that there are bugs

I’ll release the code for it in the following weeks so that anyone can set one up locally and explain a bit more how one can run it.
In the end I would like to thank [@hendi](/u/hendi) from whom I’ve copied a lot of the models, [@xiaojay](/u/xiaojay) for his python api work which I’ve used, [@yeastplume](/u/yeastplume) for adding new api that I needed and [@davidtavarez](/u/davidtavarez) for making grin++ api the same as grin-rust (still in progress).

---

### Post by @tromp ⭐ (2023-12-01)
*Post #30*

trab:

> The biggest critique of monero is that the supply is uncertain.

They prefer to live under the delusion that their supply is as fully auditable as Bitcoin:

<https://www.reddit.com/r/Monero/comments/1875cu9/comment/kbk613b/?context=3>

---

### Post by @tromp ⭐ (2023-12-02)
*Post #36*

Within each block, sum of coinbase outputs must have value exactly 60 grins + all fees.

---

### Post by @tromp ⭐ (2023-12-02)
*Post #40*

I mention the assumption that both Monero and Grin (and Zcash) use in the highlighted comment

<https://www.reddit.com/r/Monero/comments/1875cu9/comment/kbo8ah1/>

which the good Monero folk downvoted because it conflicts with their fantasy of being as fully auditable as bitcoin.

---

### Post by @tromp ⭐ (2023-12-03)
*Post #42*

There are no “fee outputs”. Every tx transparently lists the fees it pays in its kernels. So every node can see all the fees paid in a block. Each output encodes its output type, which is either plain or coinbase [1].

[1] [What’s inside a Grin Transaction File? | by Brandon Arvanaghi | Medium](https://medium.com/@brandonarvanaghi/whats-inside-a-grin-transaction-file-f062a0dcbf99)

---

### Post by @tromp ⭐ (2023-12-03)
*Post #46*

> In grin you need to trust EC

More specifically, you need to trust that no amount of money and effort can solve just one specific discrete log, namely that of point H.

---

### Post by @tromp ⭐ (2023-12-03)
*Post #48*

trab:

> They could then basically have their own money printer and no one would know?

Yes; they could subvert all cryptosystems relying on Pedersen commitments over secp256k1 with points G and H. Which includes Monero, Zcash, and Grin.
They just have to exercise a little care in how they spend their inflated outputs. If they take some outputs originating from under 10000 coinbases and then deposit it at an exchange as 1 million Grin, then that would expose their powers.

---

### Post by @tromp ⭐ (2023-12-03)
*Post #50*

Since the discrete log is defined relative to the base G, we have dlog G = 1, and H = (dlog H) * G.

---



## Should the CC donate to Grinvention - mimblewimble.py?
*Date: 2024-02-13 | [Forum Link](https://forum.grin.mw/t/should-the-cc-donate-to-grinvention-mimblewimble-py/10942)*
*Importance Score: 77.7 | Core Participants: tromp*

### Post by @Anynomous (2024-02-13)
*Post #1*

In the last two CC meetings we had a lot of discussion on funding [@renzokuken](/u/renzokuken) for his development of Grinvention | mimblewimble.py
I know not everyone is aware of Grinvention, so let me provide a short explanation, or read about it yourself [GitHub - grinventions/mimblewimble-py: Pure Python implementation of Mimblewimble protocol for Grin cryptocurrency](https://github.com/grinventions/mimblewimble-py/).

> “We are building the first Python-based implementation of the Mimblewimble protocol for the [grin cryptocurrency](https://grin.mw/). At the moment it is at the most early stage of development. Heavily based on the [grin++ wallet](https://github.com/GrinPlusPlus/GrinPlusPlus).”

The way I would describe Grinvention, is as _“a collection of Python scripts to easily play around with various components of Grin”_. For example, a script to easily generate a grin wallet.

## Why would a donation to Grinvention be useful for Grin as a project you might ask?

1. On the long run, Grinvention could become a full Python implementation of Mimblewimble.
2. On the short run, Grinvention provides useful code that can be easily modified for various purposes, or simply can be used to understand the various technical aspects of Grin. For example, the code can relatively easily be modified to generate a wallet using BIP39 passphrase protected seeds, or custom word lists (two requests made by community members to me in the past). In that sense mimblewimble.py is like what **bitcoinlib** and **bip_utils** Python libraries are for Bitcoin. These packages provides a Swiss army knife to play around with Bitcoin, greatly reducing the barrier for anyone to start using or learning Bitcoin. The reason why is simple. Python is a) the most popular programming language in the worl, and b) the most easy to learn and read programming language in the world.
Hence, having a similar Swiss army knife of scripts in Python to learn and program various Grin/mimblewimble components, is beneficial.

## How to fund Grinvention?

After a lot of discussion we came to the conclusion that [@renzokuken](/u/renzokuken) does not want to apply for any official Funding Request for various reasons, such as his believe that being-independent from the project and fully donation based is better for the project and for Grinvention even though it earns him much less. This donation based model does however create an obstacle since donations have been few, meaning there has been little financing for [the work put in by](https://github.com/grinventions/timesheets/tree/main/timesheets/2022) [@renzokuken](/u/renzokuken).
What I want to discuss here is if the CC should make a donation to Grinvention, and if so how much.
Since this is a donation and not a funding request, the amount will most likely be modest and much less than he could get via an official funding request. Although we can attach a message such as “we would like to see functionalities XYZ”, these are not obligatory requirements or objectives since it would be a donation and not a funding request.
Taking in consideration the past work of [@renzokuken](/u/renzokuken), I think making a donation based on the merits of his work makes sense and is relatively low risk. Worst case scenario, we pay him for the work that he has already put in
My question to you as community members would be to ask your opinion about making such a donation. Do you think we should make a donation? How much should a donation be. What features would you like to see for Grinvention development?

---

### Post by @Cobragrin (2024-02-13)
*Post #2*

Anynomous:

> In that sence mimblewimble.py is like what **bitcoinlib** and b**ip_utils** Python libraries are for Bitcoin. These packages provides a Swiss army knife to play around with Bitcoin, greatly reduce the barrier for anyone to start using or learning B Bitcoin. The reason why is simple. Python is the most popular, and the most easy to understand programming language in the world.
>  Hence, having a similar “toolbox” of scripts in Python for Grin is beneficial.

Python Implementation will enhance Grin developer pool and ecosystem which we are lack of since years.
Practically ‘’ we will have more man power’', more wallet and node implementations are welcome.
**Grinventions** already reached many milestones, let it be completed for the benefit of GRIN.
I support it.

---

### Post by @mcm-mike (2024-02-13)
*Post #3*

Anynomous:

> Although we can attach a message such as “we would like to see functionalities XYZ”, these are not obligatory requirements or objectives since it would be a donation and not a funding request.

I am in favor of this approach.
About the amount I would ask the others CC members including GRIN community to share their idea of a BTC amount.

As a minimum I would suggest: `0.05267 BTC [¹]`

At the same time I would encourage everyone to go over to [grinventions · GitHub](https://github.com/grinventions) and open up **enhancement issues** or **feature requests**.

–
[1]

Description | Value
---|---
Total Hours | 73.23 hours
Desired Hourly Rate (USD) | $35
Total Amount for Desired Rate (USD) | $2,563.08
BTC price at $48,660.80 (13.02.2024) |

---

### Post by @trab (2024-02-16)
*Post #10*

Anynomous:

> What features would you like to see for Grinvention development?

You mention that people can then combine and use these scripts to create larger projects.

I would like to see an example of how you can combine the scripts to make a full product.

I definitely think this should be funded, but maybe we can include an example product as a goal?

Edit: if this funding is just as a “thank you”, I would accept that too. The Python implementation is extremely valuable.

---

### Post by @renzokuken (2024-02-16)
*Post #11*

trab:

> You mention that people can then combine and use these scripts to create larger projects.
>
> I would like to see an example of how you can combine the scripts to make a full product.

I think one possible example is the betting app idea that was recently proposed. [Grin Betting Platform Idea - #8 by Anynomous](https://forum.grin.mw/t/grin-betting-platform-idea/10928/8)

Imagine you write your backend in Python Flask or FastAPI and just import `mimblewimble` to process transactions and store them in your PostgreSQL database (`mimblewimble-py` is meant to be shipped with SQLAlchemy models for storing slates and all other required data).

---

### Post by @Trinitron (2024-02-18)
*Post #16*

I’m torn because I think this is another project everyone will root for and no one will use. I hope I’m wrong about that.

---

### Post by @tromp ⭐ (2024-02-24)
*Post #23*

Certainly.

Supporting development of useful Grin tools is money well spent…

---

### Post by @Anynomous (2024-03-01)
*Post #27*

This funding request has been approved  .

As we move forward with this donation of 10k euro to Grinvention, I think it would be good to list features we would like to see in Mimblewimble-py. Note that these are just requests and not an requirement for funding. When you as community member would like to see a certain function being added to mimblewimble-py, please list your request here in this thread.
Below is a list of feature’s based on my own and [@renzokuken](/u/renzokuken) input that I think would be highly beneficial to have:

* Although everything in mimblewimble-py is important, I think adding all wallet related functionalities now would be most important
* Slatepacks
* Some example code for interaction between grin-wallet/grin++ and mimblewimle.py wallets
* Support for BIP39 password protected seeds
* Support for custom word lists (only as an opt-in since this is risky for beginners).
* Persistence of state (database models to build wallets) and RSR tx building flow.
* Not sure if it is there, but if not, support for testnet wallets
* Transaction, generating QR-code for airgapped mimblewimble-, possibly on micropython, see bounty proposal HW.
* Whatever else [@renzokuken](/u/renzokuken) thinks is important to prioritize, I trust his judgement

[@Neo](/u/neo) What are your thoughts, anything you would like to see for grin pixels?

---



## Grincoin.org - blockchain explorer
*Date: 2024-05-06 | [Forum Link](https://forum.grin.mw/t/grincoin-org-blockchain-explorer/11045)*
*Importance Score: 79.7 | Core Participants: tromp*

### Post by @bruges (2024-05-06)
*Post #1*

Here’s my contribution to Grin:

[Grincoin.org (GRIN) Blockchain Explorer](https://grincoin.org)

### [Grin Blockchain Explorer](https://grincoin.org)

Grincoin.org website allows you to explore Grin blockchain.

[GitHub](https://github.com/aglkm/grin-explorer)

### [GitHub - aglkm/grin-explorer: Grincoin.org (GRIN) Blockchain Explorer](https://github.com/aglkm/grin-explorer)

Grincoin.org (GRIN) Blockchain Explorer. Contribute to aglkm/grin-explorer development by creating an account on GitHub.

---

### Post by @tromp ⭐ (2024-05-06)
*Post #3*

Looking mighty fine! I love how you provide all the raw data of each block. Also, showing issuance relative to soft total supply is a nice touch.

How is size computed? Is that simply the sum of block sizes?
Is it possible to also compute Sync Size, i.e. the amount of data needed to sync by PIBD?

For mining cost, one could also show the break-even electricity cost. E.g. you need an electricity cost below $0.20 per kW/h to mine profitably.

I see a link to the rust grin repo, but not to the explorer repo.

---

### Post by @tromp ⭐ (2024-05-30)
*Post #16*

No; Grin is not sponsored/made by CoinGecko.
Grin was made by Ignotus Peverell with help from others like Antioch, Yeastplume and myself.

---

### Post by @bruges (2024-05-30)
*Post #18*

Coingecko has the following requirement if you use their free API.

[Screenshot_20240530_121711_org.mozilla.firefox_edit_27730926633789361200×278 98.9 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b7c4b22105f0fbb48a209abb667c17ce2941dbf3.jpeg "Screenshot_20240530_121711_org.mozilla.firefox_edit_2773092663378936")

---

### Post by @CircusDad (2024-09-20)
*Post #25*

[@bruges](/u/bruges), This is A.M.A.Z.I.N.G. Nice work.

Regarding:

bruges:

> Coingecko has the following requirement if you use their free API.

By changing from “Powered by CoinGecko” to “Price data powered by CoinGecko” it might honor their requirement without creating confusion about who is providing the awesome explorer. I only bring this up because when I initially saw their name I hit ‘view source’ to see if they had trackers in the site. They don’t (as you obviously know), but the current text led me to question it for a moment. Up to you of course.

One other comment. It might be interesting for viewers if you listed two blockchain sizes,

* Blockchain ~3.9G
* Archive Node ~18.71G.

Obviously this is not critical, but it kind of shows off the fact that Grin enables a full node/Blockchain audit with much less data. It might be too hard to implement since the explorer obviously wants an archive node and thus likely doesn’t know the size of a non-archive node. Maybe an easier path for your consideration would be to add one of your info bubbles next to node size with a short text explaining something like, “The grin blockchain is only ~20% of this size and grows in proportion to the quantity of unspent UTXO…”.

Anyway. The site is amazing even if you don’t make either of these changes. Thank you so much for your contribution. It is GREAT WORK!

---

### Post by @tromp ⭐ (2024-12-01)
*Post #44*

> equivalent to performing a hash

Not quite. Searching graphs is very memory intensive. Cuckatoo is essentially a proof of SRAM rather than a proof of hash circuits.

---

### Post by @transatoshi (2025-03-15)
*Post #48*

I’m having issues with the testnet explorer, I have to reboot the thing daily or else it starts spitting out 500 errors.

Any thoughts? I had modified the HTML/CSS of the explorer, but otherwise made no code changes.

Here’s the errors it spits out:

[Screenshot from 2025-03-15 12-22-401192×517 138 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/f/fb6d8000ef60944c4de606d760b72331e404f3c9.png "Screenshot from 2025-03-15 12-22-40")

---

### Post by @bruges (2025-07-02)
*Post #59*

Added tor onion link:
<http://wieo55w5a56itvs73sqbvr5er6rxfukqjgf2rjbrlzxb3pax66rlodid.onion>

[Screenshot_20250702_155914_org.mozilla.firefox_edit_32716258433054721200×848 82.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/068c1c29df4115d15e5125f02e9f218cbc18ad6e.jpeg "Screenshot_20250702_155914_org.mozilla.firefox_edit_3271625843305472")

---



## Grim - cross-platform GUI for Grin
*Date: 2024-08-02 | [Forum Link](https://forum.grin.mw/t/grim-cross-platform-gui-for-grin/11128)*
*Importance Score: 78.0 | Core Participants: *

### Post by @ardocrat (2024-08-02)
*Post #1*

Good Morning, have a Grin day ツ

[image1288×1080 103 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/7ff6974a6d7855599a5ee8aa3a18c05186a25271.jpeg "image")

I am happy to announce result of my near half-year contribution - public release of **Grim** \- cross-platform GUI for **Grin ツ** in pure Rust. It was named by the character [Grim](http://harrypotter.wikia.com/wiki/Grim) \- the shape of a large, black, menacing, spectral giant dog.

Initially supported platforms are Android, Linux, Windows, and MacOS **(iOS is coming)** with help of [egui](https://github.com/emilk/egui) \- immediate mode GUI library.

It will be FAQ how to use it, key features are:

* [SeedQR](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/README.md) format support to safely store seed-phrase.
* [Uniform Resources](https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md) to transfer data with camera by scanning animated QR codes to share Slatepack Messages and future hardware/offline wallet functionality.
* Multiple connections, wallets and accounts.

Plans:

* iOS
* Offline wallet functionality
* Mwixnet integration
* Plugins/SDKs for integration
* dApps

Download:

[getgrin.github.io](https://getgrin.github.io/)

### [Grim - Cross-platform GUI for Grin](https://getgrin.github.io/)

Cross-platform GUI for Grin ツ in Rust for maximum compatibility with original Mimblewimble implementation with focus on usability and availability to be used by anyone, anywhere.

Contribute:

[GitHub](https://github.com/GetGrin)

### [Grim](https://github.com/GetGrin)

More use-cases for Grin ツ create demand, to be used by anyone, anywhere, without censorship and restrictions. - Grim

Support:

[Telegram](https://t.me/grim_app)

### [GRIM](https://t.me/grim_app)

Cross-platform GUI for Grin @grinprivacy on Rust with focus on usability and availability to be used by anyone, anywhere.

---

### Post by @trab (2024-08-05)
*Post #7*

ardocrat:

> For wallet there is integrated Tor client with arti lib [The Tor Project / Core / Arti · GitLab](https://gitlab.torproject.org/tpo/core/arti)

Have you integrated this yet or no? I didn’t see anything in the UI about Tor being on or turning it on/off.

---

### Post by @Anynomous (2024-08-07)
*Post #23*

The easiest example would be an exchange that manages funds for multiple people. For each customer you have a separate account, derived from the same master seed.
In theory it could even be semi non custodial, meaning each person can backup their own account master key and derive its sub addresses. Similarly one could create a PubKey to show funds for a single account/customer.
The example from [@natsu](/u/natsu) is also common, you only want a single node and wallet, but have separate accounts for private and business.

Regarding what this protects against, not really adding protection, just compartmentalizing funds in a way that resembles the real world, so on account/user/use-case level.
Running separate wallets does add a lot more privacy but has the downside that you only can have one wallet/tor address listening at the same time.

---

### Post by @noobvie (2024-08-24)
*Post #41*

Just a dumb question, any ways to run Grim on Pentium 4, windows xp?

---

### Post by @CircusDad (2024-08-29)
*Post #45*

Per the site, Grim aims for “maximum compatibility with original [Mimblewimble](https://github.com/mimblewimble/grin) implementation”.

Are Grim coders maintaining an additional revision of the rust node and rust wallet vs. installing and using the reference implementations that exists and then interacting with them via API?

I ask because I just installed Grim on a kubuntu VM and it offered to start a node (I already have a rust grin node running on that VM). I do see how to point Grim to the existing node but does the Grim install include an entire additional instance of a Grim node code vs. installing the standard grin node? Likewise, I already have the rust CLI wallet installed and running on that VM. I kinda expected that Grim was a front-end for the reference Rust wallet and would interact with it via the API. Did installing Grim actually install another Rust node and wallet all together? Assuming yes, what is meant by “maximum compatibility with original grin implementation”.

Thanks to ardocrat for this awesome contribution. It’s awesome either way, my question is just aimed at getting a better understanding what I just installed.

* Thanks.

---

### Post by @ardocrat (2024-09-04)
*Post #52*

CircusDad:

> Per the site, Grim aims for “maximum compatibility with original [Mimblewimble](https://github.com/mimblewimble/grin) implementation”.

yes, it uses grin crates:

[image909×512 57 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/baf12d09950954118ba84638cca0a5026c061e84.png "image")

---

### Post by @ardocrat (2025-04-19)
*Post #59*

hellogrin:

> I wish we could have a ‘simple’ message/chatroom function in this app.

I am thinking how implement it the best, simple p2p tor/nym connection can be enough. Current problem is Tor is not working on Android, cause no bridges support, I am looking at NYM mixnet now: [nym/sdk/rust/nym-sdk/src/tcp_proxy/bin at develop · nymtech/nym · GitHub](https://github.com/nymtech/nym/tree/develop/sdk/rust/nym-sdk/src/tcp_proxy/bin)

---

### Post by @hellogrin (2025-07-19)
*Post #72*

The site is no longer available? is it possible to share it in the public github in case someone needs?

---



## I love all grinners❤️. Meme theme
*Date: 2024-10-22 | [Forum Link](https://forum.grin.mw/t/i-love-all-grinners-meme-theme/11227)*
*Importance Score: 120.5 | Core Participants: tromp*

### Post by @Alice (2024-10-22)
*Post #1*

[1000001492696×542 66.2 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/8b7c341b791cf76c12f2730c8fa77531db7cf0e2.jpeg "1000001492")

---

### Post by @Anynomous (2024-10-24)
*Post #9*

In case anyone wondered, the origin of that pill (that inspired the Wachowski brothers who directed the Matrix), SeedSigner logo design and current and past cypher and cyber punks:
**Akira** , a famous manga and anime from the 80’ies. Based on that I designed some quick and dirty wallpapers, unfortunately not very high resolution. The kanji are the Chinese characters for Grin.

[Akira21600×1200 158 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/1250fe05b8861efda84ddc57c4257811f59fdee7.jpeg "Akira2")

[Akira11600×1200 164 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/5/556d5ac6090cd1bbfd7689cb6ff5ed3b1f917b22.jpeg "Akira1")

---

### Post by @Anynomous (2024-10-24)
*Post #11*

Having fun with a Grin [Haiku generator](https://poemanalysis.com/poem-generator/haiku/), all except my first try are quite nice:
**Try 2**

**Grin of the Digital Age**

_Whispers through the wires,_
_A grin of silent consent,_
_Cash flows, unseen hands._

_Minimal pathways,_
_Each node a promise to share,_
_Fair in the design._

_Privacy wrapped tight,_
_In shadows where secrets thrive,_
_Freedom stems from trust._

_Scalable visions,_
_A world where wealth finds a way,_
_Digits dance like dreams._

################################
**Try 3**

**The Digital Grin**

_Whispers in the code,_
_Scalable trust takes root here,_
_Fairness in each byte._

_Privacy guards dreams,_
_Digital cash flows like streams,_
_A grin, bright and wide._

_In the vast unknown,_
_A minimal path unfolds,_
_Connections that glow._

##################################
**Try 4**

**The Whisper of Trust**

_In shadows we grin,_
_Mimblewimble whispers soft,_
_Privacy’s embrace._

_Digital dreams flow,_
_Cash in code, flowing like streams,_
_Fairness comes alive._

_Scalable futures,_
_Trust blooms in the unseen space,_
_Minimalist hearts._

##########
**Try N**

**Whispers of a Grin**

_In shadows, they smile,_
_Mimblewimble whispers soft,_
_Trust intertwined deep._

_Digital echoes,_
_Cash flows like a gentle stream,_
_Fairness in each byte._

_Hidden in the light,_
_Privacy holds the key close,_
_Scalable dreams soar._

---

### Post by @Alice (2025-05-31)
*Post #47*

[ 10000067871024×1536 99.3 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/6b6b530b100f3ac58d9d5b121ad1161a1a15954d.jpeg "1000006787")

---

### Post by @Alice (2025-06-10)
*Post #51*

[10000069551024×1024 78.4 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/b/b4dc6c8b4d05a07c4786cfcde5dfa9b6b9e4f260.jpeg "1000006955")

[10000069511024×1024 78.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/67f1cf4d0fd3edee8e84b63af19fafd69c294d23.jpeg "1000006951")

We don’t have a mascot.

---

### Post by @Alice (2025-06-11)
*Post #61*

[10000069961024×1536 189 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/ab274e22c5138a4a2b99342009ab648da45b13e1.jpeg "1000006996")

---

### Post by @Alice (2025-06-29)
*Post #89*

[10000072891024×1536 64.1 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/a368a3485f7ea9a4fc148b94b22617b6b4cab964.jpeg "1000007289")

[10000072901024×1536 76.8 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4eb7eeb4ae2bfaca916a7068e23bc5120c6e7bf5.jpeg "1000007290")

---

### Post by @tromp ⭐ (2025-11-21)
*Post #115*

[IMG_20251114_1920201824×1368 516 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/9/94e62472f76ad24053e6f1585c03bb71109e264a.jpeg "IMG_20251114_192020")

Grin ツ spotted in Amsterdam.
Not sure what the rest of that Japanese is saying…

---



## [LISTING] MEXC x GRIN
*Date: 2024-11-13 | [Forum Link](https://forum.grin.mw/t/listing-mexc-x-grin/11376)*
*Importance Score: 73.8 | Core Participants: *

### Post by @Arka (2024-11-13)
*Post #1*

Hello everyone,

MEXC contacted me about potentially listing GRIN.

We will likely need technical support to assist them in listing GRIN.

I have, of course, made it clear that **GRIN will not be paying anything to be listed**.

[@Ardocrat](/u/ardocrat) has volunteered to help, and if any other volunteers (I’m mainly talking about GRIN developers and contributors) would like to get involved, feel free to make yourselves known, and I will share the Telegram group link with you.

I won’t hide that I was almost 99% certain it was a scam, but after verification with an administrator from the official MEXC group and confirmation on [Verify MEXC Official Channels, News and Publications](https://www.mexc.com/en-US/official-verify), it turns out that the person is indeed legitimate.

[Capture d’écran 2024-11-13 à 15.59.30972×968 96.6 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/43d7f3f01894ec608d6bc064bc28ea43bf30403a.jpeg "Capture d’écran 2024-11-13 à 15.59.30")

---

### Post by @Anynomous (2024-11-26)
*Post #16*

Personally I am _against any form of paid listing_.
Grin is however a free project. Anyone can start a fundraising where people can pledge an amounts in USD or BTC, I would just not endorse it or participate in it. I very much doubt we could raise 30k in funding for any listing since many community members like myself are per definition against paid listings.

Also good to mention there might be more idealistic alternatives out there that do not require any listing fees at all. Personally I would favor exploring those options.
See this thread:

[Secure Trade - Suitable exchange for listing Grin?](https://forum.grin.mw/t/secure-trade-suitable-exchange-for-listing-grin/11397/2)

> I’ve used safetrade a time or two, and it’s definitely a step up from the usual small exchanges like xeggex, vitex, etc. I like that they have 2FA and lot’s of privacy coins.

---

### Post by @Cobragrin (2025-01-17)
*Post #23*

i also emailed and talked with Mexc and they demand 20k listing fee and 50k usd worth of Grin coin liqudity. No replied back via email after all.

[2548×214 50.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/7/77a885eaf699c24148927916c7df241f70b0f746.jpeg "2")

[3ız548×278 55.6 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/e/ec5a9bbd4596a7a914db65bc54b9dd0a02965959.jpeg "3ız")

---

### Post by @syntaxjak (2025-02-14)
*Post #33*

I don’t know if another exchange is going to help with the liquidity issue.

Tradeogre is in desperate need of grin liquidity. Like for acouple thousand bucks people can make the price do very drastic swings.

Technically, the responsibility for liquidity providing would fall into the hands of those who have access to the community funds for grin - instead they just hodl btc and do nothing for grin liquidity.

I should note that this is probably because none of the cc or core really know anything about market making.

---

### Post by @Rust (2025-02-14)
*Post #34*

syntaxjak:

> desperate need of grin liquidity

Dead coin walking… The only thing keeping this project alive is its remaining funding, which is slowly being drained by useless requests that have zero impact on its trajectory.

---

### Post by @happypigeon (2025-02-14)
*Post #38*

Interesting observation related to this market making on the kraken website:

[Kraken Blog – 19 Sep 24](https://blog.kraken.com/product/asset-listings/4-simple-steps-how-to-get-listed-on-kraken "01:00PM - 19 September 2024")

### [4 simple steps: How to get listed on Kraken](https://blog.kraken.com/product/asset-listings/4-simple-steps-how-to-get-listed-on-kraken)

You've worked hard, built your community and planned your roadmap. So how do you get listed on Kraken?

Est. reading time: 7 minutes

Having market makers could boost the credibility of this project.

> ## **Step 4: Listing Day!**
>
> Now we’re ready to launch your token on Kraken! In the run-up to your listing date, we’ll coordinate with your market makers (MMs) and post on social media and across our various marketing channels, to make sure as many people as possible are aware of your listing on Kraken.
>
> Using MMs helps with market liquidity, driving volume and better price discovery. It is one of the first steps toward creating a healthy trading market for a specific token.
>
> Going forward, we’ll monitor your asset pairs on Kraken. We’ll be looking at volume, liquidity and spread to gauge how the market is performing.
>
> **Remember: We recommend projects use Market Makers at launch; many projects bring their own.**
>
> The listing process is important to us, because we believe that the builders are the lifeforce of crypto. Our mission at Kraken is to accelerate the adoption of cryptocurrency around the world in order to promote financial freedom and inclusion. We couldn’t do that without the support of the projects and teams pushing the industry forward. So, builders, click below and take the first step toward getting your cryptoasset listed on Kraken!

---

### Post by @Cobragrin (2025-02-15)
*Post #40*

i applied to Kraken last week. Hope they consider listing.

[krakenlisting1050×556 22.5 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/1/15139a58ef20611310d2e6ebf9f8e288ff461103.png "krakenlisting")

[KRAKENz725×676 41.4 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/3/36e9f653b9996d6d783a74b3a52500f0562db7ea.jpeg "KRAKENz")

---

### Post by @Anynomous (2025-03-05)
*Post #55*

The first question would be, which governance meetings? Only the CC has public governance meetings and at the moment only 3 of us are active, which is not enough for quorum. Unless the OC would become active or merge with the CC, any transfer of funds would be meaningless since it would be from one inactive council to another inactive council

[@natsu](/u/natsu) Which spending decisions of the CC would you categorize as “squandered”, apart from the mining investment which turned out really bad but which was pushed for by the community. Most of the funds were spend on continued development of Grin++, was that all a waste in your opinion? Or was it paying for a ground-keeper, who provided all the administration and a newsletter for outreach, which again, was very strongly fought for by the community. To be clear, I have no strong feelings about this, but I would appreciate getting some more input and outsider perspective. [@Arka](/u/arka) and [@natsu](/u/natsu) if you have strong feelings about governance and the direction of Grin, just drop by in these CC meetings, it makes them more useful if there are more community members present. See here a link to the next meetings agenda:

[github.com/grincc/agenda](https://github.com/grincc/agenda/issues/162)

####  [Agenda: Community Council (CC), 11 March 2025](https://github.com/grincc/agenda/issues/162)

opened 09:53AM - 27 Feb 25 UTC

[ cekickafa ](https://github.com/cekickafa)

Solicit suggestions for agenda items for the Governance meeting to be held on Tu[…]()esday **March 11** @ _19:30 UTC_ in grincoin#general channel on [Keybase](https://keybase.io/team/grincoin#general). Please comment to provide topics or suggestions. (Meeting can be followed on @keybase-ro channel - GRIN community [discord server](https://discord.gg/5p4vCQY9km) via GRIN discord bridge). ## To Do List. \- Donation payment to [Grincoin.org](https://grincoin.org/) \- Groundkeeper [ voting for funding request](https://forum.grin.mw/t/cekic-progress-and-request-for-2025-groundskeeper/11615). ## Proposed Agenda \- _Fixing peers_, [grin++ node bans Rust nodes](https://forum.grin.mw/t/funding-proposal-pibd-implementation-in-grin/11583/2). \- [Payment proofs ](https://github.com/tromp/grin-rfcs/blob/early-payment-proofs/text/0000-early-payment-proofs.md)implementation.

---


