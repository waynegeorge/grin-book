# Chapter 1: MimbleWimble Origins

In July 2016, someone using the pseudonym "Tom Elvis Jedusor"—an anagram of Voldemort's French name—dropped a whitepaper onto a Bitcoin research IRC channel and vanished. The paper described MimbleWimble, a protocol that promised to dramatically improve blockchain privacy and scalability. The cryptography community was intrigued, but the author was gone.

Within months, another pseudonymous figure emerged. Calling themselves "Igno Peverell"—after the Harry Potter character who created the Invisibility Cloak—they began building the first implementation of MimbleWimble. They called it Grin.

## The Forum Awakens

On January 16, 2018, the Grin forum came to life with a simple welcome message: "Grin is a blockchain and a cryptocurrency focused on privacy and scalability. Grin is also an implementation of the MimbleWimble transaction format with the extensions required for a complete blockchain."

The early days attracted a particular kind of person—technically curious, drawn to the project's combination of cryptographic innovation and Harry Potter references. Within a week, community members were already asking for spaces to discuss the project beyond pure technical matters.

"I am a non-technical person reading the resources available and very interested in this project," wrote one early member. "As far as I can see, MW GRIN is an evolved crypto that has the potential to eclipse/replace many others... I sense that the MW team is actively downplaying publicity during what is still early development stages."

Igno Peverell responded with characteristic pragmatism, explaining that a "Lounge" category existed but was hidden from new users—"the original intent was to avoid too much noise." As for market speculation and "when lambo" discussions, Igno hoped to keep those isolated in a dedicated Market category.

## Cuckoo Cycle: A New Kind of Mining

One of Grin's most distinctive features was its proof-of-work algorithm: Cuckoo Cycle, created by John Tromp. Unlike the hash-based mining that powered Bitcoin and most other cryptocurrencies, Cuckoo Cycle worked by searching through massive graphs for cycles—paths that loop back on themselves.

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
