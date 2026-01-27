# Chapter 4: Launch Day

*8 topics selected for this chapter*

---

## Bminer 15.7.6 Fix Cuckaroo29d on RTX-series cards
*Date: 2019-01-15 | [Forum Link](https://forum.grin.mw/t/bminer-15-7-6-fix-cuckaroo29d-on-rtx-series-cards/2177)*
*Importance Score: 108.8 | Core Participants: tromp*

### Post by @realbminer (2019-01-15)
*Post #1*

Bminer is a highly optimized cryptocurrency miner that runs on modern AMD / NVIDIA GPUs. Bminer is one of the _fastest_ publicly available miners today – we use various techniques including tiling and pipelining to realize the full potentials of the hardware.

Releases[¶](https://www.bminer.me/releases/#releases)

15.7.6

* Fix the regression that the Cuckaroo29d miner fails to start on RTX-series cards.

15.7.5

* Improve the performance of the miner of Cuckatoo31.
* Increase the dynamic ranges of -intensity for older machines to fully utilize the GPUs (at the cost of a slight performance loss). please setting -intensity from 0 and increase the number if it’s stable.

15.7.4

* Improve the performance of Cuckaroo29d / Aeternity.
* Support 4GB cards for Cuckaroo29d.
* Fix the regression that the Cuckaroo29d miner fails to start on Windows.
15.7.3
* Improve the performance of the Cuckaroo29d miner.

15.7.2

* Improve the stability of the Cuckaroo29d miner.
* Reduce the CPU usage of Cuckaroo29d miner.
* Support 5GB cards for Cuckaroo29d.

15.7.1

* Improve the performance of the Cuckaroo29d algorithm.
* Fix the issue that the Cuckaroo29d failed to start for Turing-based cards.

15.7.0

* Support the cuckaroo29d algorithm.

15.5.3

* Fix invalid shares ETH + VBK when using multiple cards.

15.5.1

* Fix the regression that Cuckaroo29 fails to work on Turing cards
* Significantly improve the performance of ETH / VBK dual mine.

15.5.0

* Improve the performance of the Cuckatoo algorithm.
* Support dual-mining ETH and VBK.
* Add the parameter `-version` to output the version and exit.

15.4.0

* Improve performance of Cuckaroo29 / Aeternity.
* Improve compatibility on Windows.
* Add an experimental flag --fast to improve the performance for Cuckaroo29 / Aeternity, but it might lead to unstability on some systems.

15.3.1

* Slightly improve performance of Cuckaroo29 / Cuckatoo31.
* Reduce CPU usages of Cuckatoo31.
* Fix the regressions of Cuckaroo29 on RTX cards.
* Fix the incorrect reportings of Ethash speed to the mining pools.

15.3.0

* Improve the performance of Cuckaroo29 by 5%.
* Slightly improve the performance of Cuckatoo31.
* Improve compatibility on Windows.

15.2.0

* Improve performance and stability of Cuckatoo31.
* Slightly improved performance of Ccukaroo29
* Reduced the chance of reject and stale shares of CC29/CC31
* Support RTX 2080/2070 for Cuckatoo31. RTX 2080 expected speed 1.45G/s

15.1.0

* Improve performance of Cuckaroo29 / Cuckatoo31.
* Experimental support Cuckaroo29 on AMD cards (ROCM only)
* Improve compatibility on Windows.
* Fix the regression on UI dashboard.
* Reduce reject rate of Cuckaroo29 / Cuckatoo31.

15.0.2

* Improve the fidelity of Cuckaroo29 on 1060 / P106 / 1070.

15.0.1

* Fix compatibility issues on Windows.

15.0.0

* Support 8G cards for Cuckatoo31 (except for Windows 10).
* Improve stability of the Cuckatoo31 solver.

14.3.1

* Improve the performance of Cuckaroo29.
* Reduce the likelihood of rejected shares of Cuckatoo31.
* Support Nicehash for both Cuckaroo29 / Cuckatoo31.

14.3.0

* Improve the performance for Cuckatoo31.
* Support 2080Ti for Cuckatoo31.
* Reduce the CPU usages for Grin / Aeternity by default.
* Reduce the likelihood of rejected shares for Cuckatoo31.

14.2.0

* Experimental support for Cuckatoo31 on 1080Ti.
* Fix the regression where ETH dual mine fails to start on Windows.
* Improve performance on mining Aeternity.
* Support tweaking the CPU usage for mining AE / Grin with the `-intensity` flag.

14.1.0

* Improve performance of AE / Grin on Turing cards.
* Improve performance of AE / Grin on lower-end CPUs and Windows platforms.
* Support mining beam on leafpool and nicehash.
* Fix the regression where /api/v1/devices is occasionally unresponsive.

14.0.0

* Improved Grin/AE mining speed.
* Print fidelity information. It is a measure of the luck/miner correctness. Overtime, the number should be close to one. For miners running over two hours, the fidelity should be at least greater than 0.95.
* Improved multi-card performance on Windows
* Improved the miner fidelity by 8%-10%. You will not see big local difference but you will see roughly 10% higher speed on the pool side.
* Reduced reject chance.
* Fixed equihash issue.
* Fix the regression that the equihash miner fails to start on Windows.

13.2.0

* Improve the performance of Turing GPUs when mining Grin.
* Reduced rejected share chance for all cards.

13.1.0

* Support mining Grin / AE with 4G or 5G of video memory. (P104 only on Linux)

13.0.0

* 30% performance improvement on Grin and AE on NVIDIA GPUs only
* Reduce the likelihood of rejected shares.

12.2.0

* Optimize CPU usage.
* Fix compatibility issues with [grin-pool.org](http://grin-pool.org) and [grinmint.com](http://grinmint.com).
* Experimental support for Turing GPUs.
* Allow bminer to run with older NVIDIA drivers.

12.1.0

* 50% performance improvement on Aeternity.
* 10% performance improvement on Grin.
* Support 8GB cards on Windows 10.
* Support SSL connections for Grin.

12.0.1

* Experimental support mining Grin
* 100% performance improvement on the beam miner compared to 11.4.1.
* Bug fixes

**Grin(**Cuckaroo29**) mining on stock settings:**

* **10.8 G/s on GTX 2080Ti**
* **7.90 G/s on GTX 2080**
* 7.10 G/s on GTX 1080Ti
* 4.60 G/s on GTX 1070
* 3.20 G/s on GTX 1060 6G
* 6.76 G/s on GTX P102
* 4.00 G/s on GTX P104

**Grin(**Cuckaroo31**) mining on stock settings:**

* 2.2 G/s on GTX 2080ti
* 1.3 G/s on GTX 1080 Ti

**AE mining on stock settings:**

* **11.80 Sol/s on RTX 2080ti**
* **8.9 Sol/s on RTX 2080**
* **7.40 Sol/s on GTX 1080Ti**
* 4.37 Sol/s on GTX 1070
* 3.15 Sol/s on GTX 1060 6G
* 6.60 Sol/s on P102
* 4.10 Sol/s on P104

Please see <https://www.bminer.me/performances/> for more performance information.

**Mining Grin (Grin)**

Currently bminer only supports the Cuckaroo29 algorithm. There are a few things that need to be customized for your own usages:

* Substitute `bminergrin` with your own GRIN address.
* Substitute `worker` to your worker name.
* Substitute `foo` to your password.

**Currently bminer only supports the Cuckaroo29 algorithm.** For example:
bminer -uri cuckaroo29://bminergrin.worker:foo@grin.f2pool.com:8898

**Downloads Bminer**
<https://www.bminer.me/releases/>

**Grin Mining Tutorial**
[Bminer Grin mining on F2pool](https://medium.com/@realbminer/bminer-grin-mining-on-f2pool-10ecbb519417)
[Bminer Grin mining on Sparkpool](https://medium.com/@realbminer/bminer-grin-mining-on-sparkpool-2b18151dd530)
Note: you are able to set the worker name on spark pool if you follow the tutorial.
[Bminer Grin mining on Grinmint pool](https://medium.com/@realbminer/bminer-grin-mining-on-grinmint-pool-f0e3d160e260)
Note: you are able to set the worker name on Grinmint pool if you follow the tutorial.

**How to tweaking the CPU usage for mining AE / Grin with the** `-intensity` **flag?**

Both Aeternity / Grin requires significant CPU power to aid the mining. You might have sub-optimal performance if the machine is running on a low-end CPU (e.g. Intel Celeron) with multiple GPUs. Optionally, you can experiment the CPU usage with the `-intensity` flag:

_bminer -uri cuckaroo29://bminergrin.worker:foo@grin29.f2pool.com:13654 -intensity 6_

The intensity is between 0 and 12. Lower intensity has lower CPU usage but potentially slower on mining.

Sample Usage of mining grin over nicehash:

* bminer -uri cuckaroo29://1DQ4bZpFTDiSNk2CWLEFWK9K96rBFP2Hv@grincuckaroo29.usa.nicehash.com:3371

* bminer -uri cuckatoo31://1DQ4bZpFTDiSNk2CWLEFWK9K96rBFP2Hv@grincuckatoo31.usa.nicehash.com:3372

## Specifying AMD devices[¶](https://www.bminer.me/examples/#specifying-devices)

You can specify which cards that Bminer should mine on using the `-devices` options. While Bminer runs on the NVIDIA cards by default, you can prefix the device IDs with `amd:` to run on AMD cards. For example:
bminer -devices amd:0 -uri beam+ssl://3a13205ec464807c9400f0fde8d56ac49da03bb3812055f08844fe2eaf0b9166.worker@beam.sparkpool.com:2222

Bminer will run on the first AMD card on the system.

---

### Post by @tromp ⭐ (2019-01-15)
*Post #6*

May I ask how you are complying with <https://github.com/tromp/cuckoo/blob/master/LICENSE.txt> ?

---

### Post by @tromp ⭐ (2019-01-18)
*Post #29*

realbminer:

> Will DM you for more details.

Nothing received. Please respond timely to compliance requests…

---

### Post by @18fcv (2019-01-24)
*Post #79*

Hey. When you run bminer 13.1 on P104-100 cards, it gives an error

[
image.png962×134 3.88 KB
](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/8/85bc3eb0fd6687930d0750018108d20d074cbe8e.png)

If you run with the -devices option without a GPU 0, then the operation

[
image.png1130×51 1.79 KB
](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4feaafb6d0e22f6d3f4022f238b91288322680a8.png)

[
image.png892×461 9.26 KB
](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/a/acc05a24103a3a258f47a739a5e804387d7777e3.png)

Windows 10, driver nvidia 417 and 391. No difference

Help me)

---

### Post by @realbminer (2019-01-30)
*Post #113*

We’re pleased to release Bminer 14.1.0.

Improve performance of AE / Grin on Turing cards.
Improve performance of AE / Grin on lower-end CPUs and Windows platforms.
Support mining beam on leafpool and nicehash.
Fix the regression where /api/v1/devices is occasionally unresponsive.

**AE mining on stock settings:**

* 11.00 Sol/s on RTX 2080ti
* 8.3 Sol/s on RTX 2080

**Grin mining on stock settings:**

* 10.8 G/s on GTX 2080Ti
* 7.90 G/s on GTX 2080

Please see [https://www.bminer.me](https://www.bminer.me/) for more details.

Happy mining!

---

### Post by @keepwalking1234 (2019-02-07)
*Post #122*

<https://www.bminer.me/releases/>

### 14.2.0 (Current)[¶](https://www.bminer.me/releases/#1420-current)

* Experimental support for Cuckatoo31 on 1080Ti.
* Fix the regression where ETH dual mine fails to start on Windows.
* Improve performance on mining Aeternity.
* Support tweaking the CPU usage for mining AE / Grin with the `-intensity` flag.

---

### Post by @realbminer (2019-02-10)
*Post #128*

We’re pleased to release Bminer 14.3.0.

Improve the performance for Cuckatoo31.
Support 2080Ti for Cuckatoo31.
Reduce the CPU usages for Grin / Aeternity by default.
Reduce the likelihood of rejected shares for Cuckatoo31.

Please see [https://www.bminer.me](https://www.bminer.me/) for more details.
Please see <https://www.bminer.me/performances/> for performances of Bminer on mining different coins.

Happy mining!

---

### Post by @realbminer (2019-03-01)
*Post #183*

We’re pleased to release Bminer 15.1.0. The release provides:

* Improve performance of Cuckaroo29 / Cuckatoo31.
* Experimental support Cuckaroo29 on AMD cards (ROCM only)
* Improve compatibility on Windows.
* Fix the regression on UI dashboard.

[How to specifying AMD devices](https://www.bminer.me/examples/#specifying-devices)
[Download Bminer15.1.0](https://www.bminer.me/releases/#releases)

---



## Miner for AMD/NVIDIA 4G 6G 8G 10G GPU from Minerbabe
*Date: 2019-01-15 | [Forum Link](https://forum.grin.mw/t/miner-for-amd-nvidia-4g-6g-8g-10g-gpu-from-minerbabe/2184)*
*Importance Score: 94.3 | Core Participants: tromp*

### Post by @jie (2019-01-15)
*Post #1*

# A Grin GPU miner from Minerbabe

Minerbabe is a GPU mining OS base on Linux. Minerbabe supports many digital coins.

Today, Minerbabe releases a new miner to support Grin.

You can use AMD/NVIDIA GPUs with 4G/6G/8G/10G memory to mining Grin now!

The miner is optimized for GPUs with different memory.

The test results on some typical GPU are below:

* Cuckaroo 29

GPU | GPS
---|---
AMD 380 4G/8G | 1.17
AMD 560 4G/8G | 0.81
AMD 390 4G/8G | 1.52
AMD 570 4G/8G | 1.7
AMD Vega 64 8G | 3.53
NVIDIA 1050Ti 4G | 1.4
NVIDIA 1060 6G | 3.3
NVIDIA 1070 8G | 4.8
NVIDIA 1080 8G | 5.2
NVIDIA 1080Ti 11G | 7.35

* Cuckatoo 31

GPU | GPS
---|---
AMD 390 8G | 0.150
AMD 570 8G | 0.161
AMD 570 8G on ROCm | 0.174
AMD 480 8G | 0.210
AMD 580 8G | 0.178
AMD 580 8G on ROCm | 0.197
AMD Vega64 8G | 0.410
NVIDIA 1070 8G | 0.316
NVIDIA 1080 8G | 0.339
NVIDIA 1070TI 8G | 0.380
NVIDIA 1080Ti 11G | 0.551
NVIDIA 2080 8G | 0.69
NVIDIA 2080Ti 8G | 1.7

ROCm is a new computing driver from AMD. Unfortunately not all of the mining rigs support ROCm.

The miner is being continuously optimized. Install Minerbabe to automatically keep the miner being updated.

Minerbabe dev fee: 2% for Grin; 1% for the other coins.

The minerbabe’s kbminer for Grin is released under FAIR MINING license. As a result, half of the dev fee is for the coin developers.

Download minerbabe image: <https://cdn3.minerbabe.com/disk/minerbabe_v4.14en.img.zip>

Manage your rigs at: <https://en.dashboard.minerbabe.com>

Get tutorial and more information at: [www.minerbabe.com](http://www.minerbabe.com)

Telegram: <https://t.me/joinchat/HkFS5xXBWHhA5QE-WfcxDg>

Tech Support: minerbabe (#AT#) [mcarlo.com](http://mcarlo.com)

Enjoy!

### Kbminer Release Notes

#### v1.0.1 2019-02-22

1. Add support for AMD Hawaii Arch GPU: RX290 RX390
2. The performance of Cuckaroo 29 is optimized.
3. Reduce dev fee to 2%, half of the dev fee is for Grin Team.

#### pre release v0.0.7 2019-01-30

1. Based on v0.7.0
2. Add support for AMD Hawaii Arch GPU: RX290 RX390

#### v0.7.0 2019-01-28

1. Add “nocpu” feature for Nvidia gpu.
2. Add option: verify share’s difficulty before submit.

#### v0.6.4 2019-01-18

1. Add support for AMD 380 550 560;
2. Reduce the delay rate of shares;

### Minerbabe Screenshot

[ 51162923-e541bc00-18d2-11e9-9076-2c9bb0305a99.jpg1920×1121 312 KB ](/uploads/grin/original/1X/80ca66958b11327323ddf0eef23d9546be8a77d6.jpeg "51162923-e541bc00-18d2-11e9-9076-2c9bb0305a99.jpg")

---

### Post by @tromp ⭐ (2019-01-15)
*Post #3*

jie:

> Minerbabe dev fee: 3% for Grin

May I ask how you are complying with <https://github.com/tromp/cuckoo/blob/master/LICENSE.txt> ?

---

### Post by @dewminer76 (2019-01-15)
*Post #6*

i already know that, thanks.
are you sure then miner can handle 4gb amd cards ?

## root@miner:/opt/kbminer# ./kbminer --verbose --agent=false --algorithm=grin-cuckaroo29 --pool=[eu.stratum.grin-pool.org:3416](http://eu.stratum.grin-pool.org:3416) \--user=test --pass=test --enableapi=false --disablewatchdog

* * *

| | __ | |__ _ __ ___ (_) _ __ ___ _ __
| |/ / | ’_ \ | '_ ` _ \ | | | '_ \ / _ \ | '**|
| < | |_) | | | | | | | | | | | | | | __/ | |
|_|_\ |_.**/ |_| |_ | |_| |_ | |_| |_ | ___| |_|

v0.5.1                www.minerbabe.com

* * *

collecting gpu infomation …
available devices:
__ 0. Radeon RX 570 Series(Ellesmere) vram: 4084.5M avail: 3833.9M

INFO[2019-01-15T13:35:29+01:00] algorithm: grin-cuckaroo29
INFO[2019-01-15T13:35:29+01:00] auto detect cpuload flag: true
ERRO[2019-01-15T13:36:19+01:00] out of memory

---

### Post by @Neo (2019-01-15)
*Post #11*

[ photo_2019-01-16_00-53-56.jpg1280×960 243 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/e87cedca8d4767cb3fca0341f2e2e96daf061c58.jpeg "photo_2019-01-16_00-53-56.jpg")

I tested out your OS/ miner.

It’s connecting to Sparkpool, but then it auto switches and tries to connect to stratum.mwgrinpool.com:3333- and the connection gets refused. [stratum.mwgrinpool.com:3333](http://stratum.mwgrinpool.com:3333) is not listed anywhere in my config file( I assume this must your Dev wallet).

---

### Post by @Rabinovitch (2019-01-19)
*Post #35*

How can I do driver update and fan speed settings under minerbabe OS?
The rig is working OK through the night on us-east server.

p.s. I have 2 rigs under minerbabe now. 5x1070s and 6x1070. First shows 0.27 GPS per card, second shows 0.33 GPS per card. What should I do to equalize those numbers? I have already added 100 MHz to GPU clock for first rig with no result.

p.p.s. v4.12 is available: <https://cdn2.minerbabe.com/disk/minerbabe_v4.12en.img.zip> Use DownloadMaster to download it much faster.

---

### Post by @hsynynrdg (2019-01-19)
*Post #43*

[@jie](/u/jie) Trying to install ROCm driver from that guide you give above. But having not enough space error. How to pass it or how to increase /dev/sda2 partition size?

[ Screenshot from 2019-01-19 22-29-54.png1196×628 139 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4192a99c25dd2ee8f6987e483ca4ceb6359230a7.png "Screenshot from 2019-01-19 22-29-54.png")

---

### Post by @Frango (2019-01-22)
*Post #70*

estas:

> ngs but sam

thanks on info…wanna try that…I am trying to put image on another USB and using 4.12 version…tried with 4.11. On h81 have network but there is some errors on dashboard.

---

### Post by @Vitaly77 (2019-02-01)
*Post #295*

Not working and 4.15 on the motherboard boards Z270-Gaming k3, unsubscribe pliz in lichku who managed in this Board to run

[ IMG_0399-01-02-19-04-00.jpeg2851×2138 3.71 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/6/64ee874b5db080740ea64389504ea80f6b933318.jpeg "IMG_0399-01-02-19-04-00.jpeg")

when you enable do not burn indicators LAN port. the Internet is connected through a cable
the ’ net. nearby there are Riga on other motherboards are working fine))

My mail [vitaly11091977@mail.ru](mailto:vitaly11091977@mail.ru)

---



## Cuckatoo31+ (im)mutability
*Date: 2019-01-16 | [Forum Link](https://forum.grin.mw/t/cuckatoo31-im-mutability/2442)*
*Importance Score: 64.6 | Core Participants: igno.peverell, tromp*

### Post by @tromp ⭐ (2019-01-16)
*Post #1*

Our primary PoW of Cuckatoo31+ is intended to be mined by ASICs.

As such, it is important to have all rules regarding validity of cycles, validity and weighing of graph sizes, and allocation of block rewards, clearly set out, implemented, and immutable for the foreseeable future, so that ASIC manufacturers can feel confident to invest in ASIC development.

[20190625 UPDATE]: We concretize “foreseeable future” as 18 months. So we do NOT allow any primary PoW consensus changes that take effect in under 18 months.

The rules for cuckatoo validity are codified in C at

[github.com](https://github.com/tromp/cuckoo/blob/master/doc/spec)

#### [tromp/cuckoo/blob/master/doc/spec](https://github.com/tromp/cuckoo/blob/master/doc/spec)

#define ROTL(x,b) (u64)( ((x) << (b)) | ( (x) >> (64 - (b))) )
#define SIPROUND \
do { \
v0 += v1; v2 += v3; v1 = ROTL(v1,13); \
v3 = ROTL(v3,16); v1 ^= v0; v3 ^= v2; \         _\(        == __\
v0 = ROTL(v0,32); v2 += v1; v0 += v3; \         / '>    __.-"\---|__
v1 = ROTL(v1,17);   v3 = ROTL(v3,21); \        (  (\   /  \\_@\-'/  \
v1 ^= v2; v3 ^= v0; v2 = ROTL(v2,32); \        ""-'\   \__/      \__/
} while(0)

u64 siphash24(const siphash_keys *keys, const u64 nonce) {
u64 v0 = keys->k0, v1 = keys->k1, v2 = keys->k2, v3 = keys->k3 ^ nonce;
SIPROUND; SIPROUND;
v0 ^= nonce; v2 ^= 0xff;
SIPROUND; SIPROUND; SIPROUND; SIPROUND;
return (v0 ^ v1) ^ (v2  ^ v3);
}

int verify(edge_t edges[PROOFSIZE], siphash_keys *keys) {
node_t uvs[2*PROOFSIZE];

This file has been truncated. [show original](https://github.com/tromp/cuckoo/blob/master/doc/spec)

and in Rust at

[github.com](https://github.com/mimblewimble/grin/blob/master/core/src/pow/cuckatoo.rs#L280-L340)

#### [mimblewimble/grin/blob/master/core/src/pow/cuckatoo.rs#L280-L340](https://github.com/mimblewimble/grin/blob/master/core/src/pow/cuckatoo.rs#L280-L340)

280. 	/// Verify that given edges are ascending and form a cycle in a header-generated

281. 	/// graph

282. 	pub fn verify_impl(&self, proof: &Proof) -> Result<(), Error> {

283. 		if proof.proof_size() != global::proofsize() {

284. 			return Err(ErrorKind::Verification("wrong cycle length".to_owned()))?;

285. 		}

286. 		let nonces = &proof.nonces;

287. 		let mut uvs = vec![0u64; 2 * proof.proof_size()];

288. 		let mut xor0: u64 = (self.params.proof_size as u64 / 2) & 1;

289. 		let mut xor1: u64 = xor0;

290.

291. 		for n in 0..proof.proof_size() {

292. 			if nonces[n] > to_u64!(self.params.edge_mask) {

293. 				return Err(ErrorKind::Verification("edge too big".to_owned()))?;

294. 			}

295. 			if n > 0 && nonces[n] <= nonces[n - 1] {

296. 				return Err(ErrorKind::Verification("edges not ascending".to_owned()))?;

297. 			}

298. 			uvs[2 * n] = to_u64!(self.sipnode(to_edge!(T, nonces[n]), 0)?);

299. 			uvs[2 * n + 1] = to_u64!(self.sipnode(to_edge!(T, nonces[n]), 1)?);

This file has been truncated. [show original](https://github.com/mimblewimble/grin/blob/master/core/src/pow/cuckatoo.rs#L280-L340)

The rules for phasing out smaller sizes are codified in ([20190625 UPDATE] NOTE that phase outs of C32 and beyond have been put on hold)

[github.com](https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs#L167-L177)

#### [mimblewimble/grin/blob/master/core/src/consensus.rs#L167-L177](https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs#L167-L177)

167. /// This can wait until end of 2019 at latest

168. pub fn graph_weight(height: u64, edge_bits: u8) -> u64 {

169. 	let mut xpr_edge_bits = edge_bits as u64;

170.

171. 	let bits_over_min = edge_bits.saturating_sub(global::min_edge_bits());

172. 	let expiry_height = (1 << bits_over_min) * YEAR_HEIGHT;

173. 	if height >= expiry_height {

174. 		xpr_edge_bits = xpr_edge_bits.saturating_sub(1 + (height - expiry_height) / WEEK_HEIGHT);

175. 	}

176.

177. 	(2 << (edge_bits - global::base_edge_bits()) as u64) * xpr_edge_bits

The rules for balancing block rewards, are codified in

[github.com](https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs#L61-L66)

#### [mimblewimble/grin/blob/master/core/src/consensus.rs#L61-L66](https://github.com/mimblewimble/grin/blob/master/core/src/consensus.rs#L61-L66)

61.

62. /// Ratio the secondary proof of work should take over the primary, as a

63. /// function of block height (time). Starts at 90% losing a percent

64. /// approximately every week. Represented as an integer between 0 and 100.

65. pub fn secondary_pow_ratio(height: u64) -> u64 {

66. 	90u64.saturating_sub(height / (2 * YEAR_HEIGHT / 90))

And of course the supply is fixed at 1 Grin per second.

The Grin developers currently have no intention of changing these rules in the foreseeable future, unless Cuckatoo is shown to be broken (e.g. by exhibiting a sublinear time-memory tradeoff), or unless the phasing out of smaller sizes should be delayed in order to ensure public availability of >= 1 GPS miners.

---

### Post by @rodarmor (2019-01-17)
*Post #2*

This is awesome!

Definitely a silly question, but would time/memory tradeoffs in either direction merit a change to the rules? I.E. if an ASIC could employ double the memory to achieve a greater than 2x speedup.

---

### Post by @tromp ⭐ (2019-01-17)
*Post #3*

I think you cannot get speedup from using k times more memory, since you’d presumably want to access most of it, and the current solvers already work in linear time.

---

### Post by @tromp ⭐ (2019-01-19)
*Post #6*

rodarmor:

> computes multiple solutions in parallel.

You can work on multiple graphs in parallel. But each graph need’s its own memory, and its own energy expenditure…

---

### Post by @monkyyy (2019-01-19)
*Post #7*

Wait wait hear me out on this, what if you generated a large number of graphs, you store it on cheap media like tape drives. Sort them using a metric that somehow put “similar” graphs next to each other, somehow you reuse a tiny amount of work if graphs look alike( and given the birthday pardox, you would only need the square root of the total possiblity space and as we know O() really likes sub linear inputs like that)

If you managed to reuse graph logic in such a way, you would only need to sort thru square root of 2^31 on tape drives which we all know a sort function is n log n, and therefore negligible.

You may need to slow down the network speed to enable this asic design for the start up time this system would need; but 1 minute was kinda fast anyway.

---

### Post by @tromp ⭐ (2019-01-19)
*Post #10*

It would be nice if a hard disk filled with cuckatoo solutions, sorted by cyclehash, could be used as a Proof of Capacity. But I see no way to avoid grinding attacks:

[reddit](https://www.reddit.com/r/burstcoin/comments/a98tj4/grinding_attacks/)

### [r/burstcoin - grinding attacks](https://www.reddit.com/r/burstcoin/comments/a98tj4/grinding_attacks/)

9 votes and 11 comments so far on Reddit

---

### Post by @tromp ⭐ (2019-06-25)
*Post #12*

Phaseouts of C32 and beyond have been put on hold, as per the proposal <https://forum.grin.mw/t/grin-improvement-proposal-1-put-later-phase-outs-on-hold-and-rephrase-primary-pow-commitment> that was accepted today.

---



## Introducing the GRN1 - A Cuckatoo31 ASIC from Obelisk
*Date: 2019-01-17 | [Forum Link](https://forum.grin.mw/t/introducing-the-grn1-a-cuckatoo31-asic-from-obelisk/2519)*
*Importance Score: 56.2 | Core Participants: antioch*

### Post by @Taek (2019-01-17)
*Post #1*

Obelisk is excited to announce the GRN1, a cuckatoo31 miner. We are looking forward to work with the community and targeting it’s ASIC friendly family of algorithms.

Full details can be found at our blog post, I’ll be around for Q&A: <https://medium.com/obelisk-blog/the-obelisk-grn1-an-asic-for-grin-1d1ff580a19d>

---

### Post by @timolson (2019-01-17)
*Post #8*

Anyone considering this is cautioned to look at Obelisk’s history of shipping ASICs way late and way below spec.

I don’t understand how they’re still in business… oh right it’s because they take your money first, deliver crap later, and leave normal people to suffer the consequences of having useless mining hardware. I never even plugged in my Decred miner. It lost money on electricity before it even shipped (many months late and way below promised specs)

How’s the lawsuit from SIA and Decred miner customers going? Did you spend all your customers’ money on lawyers?

---

### Post by @Taek (2019-01-17)
*Post #9*

0xb100d:

> what is the estimate on how long the grin1 asic will be viable for? october until april? so if they arrive first thing in october they will be competitive for 6 months?

That’s about what we expect. Beyond April the weight of CC31 becomes low enough that CC32 miners will likely out compete them. If no CC32 ASICs appear, the miners will be viable for a few months longer than April.

timolson:

> Anyone considering this is cautioned to look at Obelisk’s history of shipping ASICs way late and way below spec.

There are some key differences things that we have for the GRN1 sale that we did not have for the SC1 sale:

* A completed frontend design for a chip
* Trusted and proven relationships with a full suite of suppliers (PSU, Fans, Bare boards, Contract Manufacturing, and all other sourcing)
* A direct relationship with our Foundry
* A working previous-generation hashing board as well as the team that made it
* A working previous-generation control board as well as a complete set of firmware to go with the control board
* An executive team that has shipped hardware before
* An executive team that has shipped mining hardware before

We have much better control over the manufacturing process this time around. We’re a much more experienced company and we’re working with teams and suppliers that have proven themselves to be reliable previously. Many of the issues for the SC1 came from working with unreliable / incompetent contractors, and these have been replaced and re-tested accordingly.

timolson:

> How’s the lawsuit from SIA and Decred miner customers going? Did you spend all your customers’ money on lawyers?

Most of the lawsuits have either been resolved or dismissed from court. Obelisk has gone above and beyond to handle its missed shipping dates, including providing full compensation for all customers who missed out on block rewards from not having units shipped to them by the due date. We compensated the cash value equivalent for all tokens that would have been mined by the machine, assuming that the customer had free access to electricity.

We take care of our customers.

---

### Post by @spartadata (2019-01-18)
*Post #11*

This is exciting, A new coin and an ASIC to mine it! As a miner of SIA and prior to the fork I am seeing all the careful design and product polishing that is going into all the current and future products. ROI has been met and net profits for those early customers and miners on the SC1 has been a pleasure to deal with. So much so that no wonder why the resell market and aftermarket is so small - miners are quiet and making net profits, both mining and reselling gear.

Fact is if the other larger manufacturers took their time to really look after the needs of miners they would have done a much better job at modulating the hardware design. For example I was an early adopter of DCR mining via first batch D9’s and they were not cheap! At $6k each I spent a small fortune ordering my rack full. Sure I was netting $200 per day but that was short lived. What was happening behind the scene was that there was a massive hoard of these being used to mine the DCR network dry at such a high rate that the roi via mining DCR was impossible to reach. Luckily I was able to flip my gear - the second, third and fourth batch owners were kind of screwed… This is what lead me to really consider the exclusivity roadmap where Sia + Obelisk meant they would ensure a much more stable roi opportunity for early miners whom got in. Fast forward to now, SC1 remains on the top of the ASIC profitability charts - 4 months post fork! Take a look: <https://apanel.com> check it out full screen on your cpu browser so you can see the full data set - on mobile it is condensed.

Now Intro GRIN Coin and the newly announced GRN1 ASIC. This is super exciting as a miner because the coin is so fresh off the lab and so Obelisk is leading the charge to serve that coin and allow us miners to join the mining opportunity - outside of the GPU realm. I am not a gpu miner so I can’t wait for this one!

Instead of insulting and complaining lets validate some of the real facts and milestones Obelisk has achieved for its customers and miners. For a US based company I sure am proud of how far they have come in such a short time. At the end of the day if you don’t jump in early as in securing your GRN1 via the vouchers which is a significant discount initially at just $100 per then once things start looking great on GRIN value and realize you want to get into the cool club it will most likely cost you double as one can clearly see what happens once demand outpaces availability.

Keep up the great work!

As a miner I manage a large group on telegram called Blockchain Association of Miners and we welcome all miners to join the discussion and connect with fellow miners all over the world.
[Telegram](https://t.me/Blockchainminersgroup)

### [Blockchain Miners](https://t.me/Blockchainminersgroup)

Blockchain Miners is a community of crypto miners. Share, learn, discuss and meet! Instant access to the group and deep group knowledge from all aspects of running a mining business.

---

### Post by @amamam (2019-01-18)
*Post #12*

spartadata:

> Instead of insulting and complaining lets validate some of the real facts and milestones Obelisk has achieved for its customers and miners.

Their sia asic is profitable because they forked the sia coin along to accomodate it. Profits for miners doesn’t mean security of a blockchain. There are some points to be made about the low quality of their asics and how they handled the issues along the way to building them (mostly thinking about communication problem).

Yet they gave coupons and credits to early buyers and in retrospect the initial buying price at today’s btc value is fair. We need more players in the field so I hope they succeed, that being said I expect them to learn from their mistakes and do better this time around.

---

### Post by @Taek (2019-01-19)
*Post #19*

timolson:

> Obelisk doesn’t design ASIC’s, and they don’t build them.

Obelisk full time employees were directly involved with the design and architecture of the GRN1 chip and memory architecture, including being responsible for several innovations and solutions that pushed performance and efficiency beyond where they would have been without Obelisk involvement. Obelisk full time employees were also directly responsible for several choices related to chip comms that contributed to the overall market viability of our machine.

Obelisk full time employees were also directly involved in the PCB design, both hashing board and control board, of the SC1 slim and will be directly involved in the design and architecture of the PCBs for the GRN1.

Obeliks full time employees were also directly involved with the design and architecture of the mechanical enclosures.

timolson:

> They are a front company, a general contractor, who takes your money and hands it out to subcontractors in China who do the work for them.

Huh? None of the core IP was developed in China. The chip design, PCB design, and mechanical design was all done in North America for the SC1 and SC1 slim, and will also all be done in North America for the GRN1. I’m not sure that it’s a big deal either way, but your statement is just factually incorrect.

---

### Post by @timolson (2019-01-19)
*Post #20*

Sorry, that was an ad hominem attack. Maybe the people responsible for your past projects are gone or replaced. Maybe you have a stellar team now inside Obelisk. It’s possible. But show us a working product before asking for money.

If you ask ordinary users for presales to fund your R&D, then I will shout “scam” all day long.

If Obelisk can make a better product than Bitmain, Innosilicon, Whatsminer, and the others, awesome. Do it. Show us. But don’t ask for us to pay for it before you make it.

---

### Post by @antioch ⭐ (2019-01-19)
*Post #22*

Looks like you’ve posted the same factually incorrect statement multiple times in various Grin chatrooms as well. If you’re looking for an estimate of how many people are mining currently you should look at total network graphs/second, not the difficulty. The difficulty does not directly correlate with this as you are not taking the (still adjusting) ar_scale into consideration.

Total network graphs/second has grown pretty steadily from 200k to well over 600k since genesis.

It might be worth redoing your calculations before coming to the conclusion that there is zero demand and that nobody is mining.

---



## [SOLVED] Early disappointments
*Date: 2019-02-01 | [Forum Link](https://forum.grin.mw/t/solved-early-disappointments/3682)*
*Importance Score: 118.1 | Core Participants: igno.peverell, jaspervdm*

### Post by @igno.peverell ⭐ (2019-02-01)
*Post #1*

After just over 2 weeks of grin being live, I’m disappointed by the way the industry around Grin is shaping up. Of course it’s early, but I’d rather not this be an indication of future direction.

Grin was started with as fair of a launch as possible for what’s under our control. We did this for good reason: we believe in Grin’s mission. I think I made pretty clear that to continue forward, the project would still need help. And yet [yeastplume’s campaign](https://grin.mw/yeastplume) is still very far from being even 10% funded.

The lesson for every development or research team watching looks pretty clear: more scammy ICOs for more money and a lot less work. Perhaps forcefully taking 20% of all rewards is the only way to get any contribution out of the mining industry. Are those the conclusions you want to impress on everyone in this sector? Because if greed feeding on itself is the only lesson, then this space truly deserves a really long and hard winter. A lot more creation is needed to reach escape velocity, and that won’t happen if everyone’s goal is just feeding off it.

To be clear, this isn’t addressed to the existing community that has been extremely generous and admirable at supporting us over the last 2 years, when things were a lot more uncertain. This is directly addressed to some of the new funds, miners, mining pools and exchanges that have entered this ecosystem since the launch and benefited from it.

So please, forward this to those you think this message concerns. Perhaps a Chinese translation would be a good thing. Make everyone aware of [our needs](https://grin.mw/yeastplume). We have a long way to go, this can certainly be fixed. And keep in mind that Grin will profit infinitely more from the contributions of a great developer like Yeastplume than from any single additional miner, exchange or fund.

---

### Post by @igno.peverell ⭐ (2019-02-01)
*Post #13*

sebseb7:

> Also the intentions of the team behind grin are not clear as of yet. In this uncertainty

What do you mean our intentions aren’t clear? We’ve been at this for 2.5 years and haven’t deviated, I don’t know how to make them any clearer.

---

### Post by @jaspervdm ⭐ (2019-02-01)
*Post #44*

They announced this recently:

> Grinmint will start enforcing mining fees in the next couple weeks. The fee will be 2% for the mining pool and an additional 0.5% for the Grin project.

---

### Post by @MidasTouch (2019-02-01)
*Post #46*

I almost feel bad for GrinMint because they’ve had to claw their way up to their current position at 0% fees and now people are asking for them to implement a 1% fee **before they’ve even enacted a fee to cover their own costs**. The issue is that the coin is being dominated by pools and miners from outside of the community, many who straddle multiple currencies and see GRIN as just another revenue stream.

In GRIN’s decision to launch as quickly as possible, likely out of worry that other MW currencies would steal the spotlight, they have ensured that community-driven pools had neither the time nor core infrastructure to make a dent compared to the mining pool behemoths that showed up. How can small teams of mining pool devs expect to successfully launch with the coin when the wallet wasn’t performant enough to handle payouts of that frequency / magnitude and core changes were being made up all of the way up to the launch? The only pools that were able to handle this sort of environment were ones that already had pool infrastructure written (ie from other coins), hash power on standby (again, from mining other coins), and could eat any potential losses (again, because they are well-funded).

I know so many normal individuals who were so excited about this coin for so long and literally none of them are happy with the way things went following launch. I fully understand that this space is no longer a small-man’s industry anymore, but there were so many things that could have been done differently.

If any of the mining software out there isn’t enacting the % fee that is supposed to go to the dev fund then why not out them so that we know which teams they are? As it stands it’s hard to figure out which pools are contributing to dev funds and which are not. Does the dev fund go toward YeastPlume’s fund? The core devs have also been somewhat unclear on that as well.

Ultimately if you wanted to make sure that pools were donating a fair share to the dev fund then helping to support a community-driven open-source pool codebase would have done wonders to help. Unfortunately the only open-source pool that I’m aware of didn’t receive nearly that sort of support and now is becoming defunct.

---

### Post by @igno.peverell ⭐ (2019-02-01)
*Post #51*

timolson:

> Do not expect one of the thinnest margin industries to cough up much cash, if any. Was that your plan all along?

Nope. I don’t have any “all along” plan, other than what has already been said over and over. We need everyone to pitch in within their means. And obviously right now, that should still be more than $1500 (which is what [@yeastplume](/u/yeastplume) had before I sent this).

---

### Post by @igno.peverell ⭐ (2019-02-01)
*Post #54*

Looks like you all decided to prove me wrong, I like it! Thanks a ton to [@keepwalking1234](/u/keepwalking1234) and Sparkpool, as well as everyone who pitched in after this email. This is very much appreciated and it looks like Yeastplume is fully funded for this new period, which is awesome!

We’re still going to need you, so recurring donations to the [general fund](https://grin.mw/fund) will be the most helpful at avoiding emergency situations like these. As I mentioned before, we have used all previous donations judiciously and will continue doing so, mostly to continue and facilitate development (no lambo).

Going back to work now. Thanks again for your help and support. Still so much to do to keep Grin awesome!

---



## Grin transaction fees
*Date: 2019-02-18 | [Forum Link](https://forum.grin.mw/t/grin-transaction-fees/4114)*
*Importance Score: 53.2 | Core Participants: tromp*

### Post by @MerlinsBeard (2019-02-18)
*Post #1*

[This infographic](https://raw.githubusercontent.com/mimblewimble/grin/master/doc/wallet/transaction/basic-transaction-wf.png) seems to say that transaction fees are 4 milligrin per output with a discount of 1 milligrin per input, but at a minimum 1 milligrin of fee.

Is possible to pay less fee?
Is it possible to pay more fee?

If it is not possible to pay more fee, what happens when blocks become full, and what about miners mining empty blocks if they deem fees to be negligble?

---

### Post by @kargakis (2019-02-18)
*Post #2*

It’s not configurable now but I guess it’s going to be once the block size starts being an issue.

---

### Post by @noobvie (2023-12-18)
*Post #8*

I have a noob question: I see BTC fee now nearly cost $40, I just imagine, what a maximum fee for standard transaction if the network is busy? or people can bid the priority to any value they want?

---

### Post by @ardocrat (2023-12-18)
*Post #9*

Yeah… thx to Ordinals

[image1464×639 53.7 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/45b01ae481430b5c132110d2b4d6e36928441056.png "image")

**Miners have to be successful** as Saylor said:
<https://twitter.com/to/status/1660268453188739072>

For Grin there is a formula:

(num_inputs + num_outputs * 21 + num_kernels * 3) * fee_base

where is `fee_base` is **0.0005**

`accept_fee_base` and `max_pool_size` are also options on node to handle “mempool”:

[image930×543 70 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/4/4d356b6a532c1da744efe4eda97c0a821b6fcc7f.png "image")

Will be interesting to test how it will work on Grin network load with high payments amount for sure, I guess pools can tweak these values for better bandwidth.

Also it’s good we have no such thing as ordinals and other bloatware to spam the chain

---

### Post by @ardocrat (2023-12-18)
*Post #10*

[image829×344 42.5 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/2X/0/0d0e888a6aed7fdd10f5e9d1b340dd5948a2b731.png "image")

This future became closer than we thought.

[Gavin Andresen on Svbtle](http://gavinandresen.ninja/a-possible-btc-future)

### [A Possible BTC Future • Gavin Andresen](http://gavinandresen.ninja/a-possible-btc-future)

Take this as a little piece of science fiction; the chances the future looks like this are small, but of all the possible futures I think this has as good a chance of any of happening: Imagine: it is the year 2061. The BTC price is six million US......

---

### Post by @Anynomous (2024-02-29)
*Post #12*

You cannot. The minimum fees are there to protect the chain and mempool from spam attacks. They are calculated giving weights to inputs, outputs and kernels based on how much memory these parts of the transaction will use on-chain. So basically you pay linearly for the blockchain space you use.

See this link for how fees are calculated:

[github.com/mimblewimble/grin](https://github.com/mimblewimble/grin/issues/3369)

####  [Revisit fee structure](https://github.com/mimblewimble/grin/issues/3369)

opened 11:13AM - 27 Jun 20 UTC

closed 10:13AM - 29 Apr 21 UTC

[ tromp ](https://github.com/tromp)

P1: Critical

The current minimum relay fee rules use accept_fee_base = 1000000 as set[…]() in the default grin-server.toml. Since this is in units of nanogrin, it expresses a base cost of 1 milli-grin. This is what you pay for each unit of a transaction weight, which is defined in https://github.com/mimblewimble/grin/blob/20e5c1910bcc1afa317a7847b398488ac08b0ca7/core/src/core/transaction.rs#L847-L856 as the linear combination 4 * #outputs + 1 * #kernels + (-1) * #inputs, with a minimum of 1. This means that a typical tx with 2 outputs, 1 input and 1 kernel requires a relay fee of 8 milligrin, currently worth about 1/3 cent. We should revisit this base fee and tx weight coefficients to provide a good long term balance between spam resistance and tx affordability. It would also be nice to make the tx weight coefficients seem less arbitrary.

Not sure how Grin++came to 0.00125, especially the 0.00005 part has me puzzled. Probably [@tromp](/u/tromp) can explain it

---

### Post by @tromp ⭐ (2024-03-01)
*Post #13*

The current fee rules are described in [grin-rfcs/text/0017-fix-fees.md at master · mimblewimble/grin-rfcs · GitHub](https://github.com/mimblewimble/grin-rfcs/blob/master/text/0017-fix-fees.md)

Standard fees are multiples of accept_fee_base which equals half a milligrin, so a fee of 0.00125 is not standard. I have no idea how grin++ computes fees, but apparently it’s not following the standard formula.

---

### Post by @tromp ⭐ (2024-03-02)
*Post #15*

No; nanogrin is the smallest unit.

---



## SuperGrin - GUI Wallet [Mainnet] v1.0.2
*Date: 2019-02-18 | [Forum Link](https://forum.grin.mw/t/supergrin-gui-wallet-mainnet-v1-0-2/4125)*
*Importance Score: 53.1 | Core Participants: *

### Post by @futurerheza (2019-02-18)
*Post #1*

Hi All,

_After a few days working on it, I think I can finally release what I have been working on. This should be a GUI Wallet we have been waiting for, Simple Wallet with file based transaction allow you to send and receive Grin Coin._

_This app currently only run on Mac, will add the windows release in the coming days._

_It’s currently running on Floonet Chain for GRIN. If there is no problem in my testing, I will try release the Mainnet chain build Tomorrow or In 48 hours from now._

_and Yes, It will be open sourced the day I release the Mainnet Chain build._

===================================================
Here is the mainnet release.

Introducing SuperGrin Mac App:

[ Xvk7XYR.png864×1024 144 KB ](/uploads/grin/original/2X/f/f821f68e27b99c91fb3a1f090a12c8b3c3e29eb1.png "Xvk7XYR.png")

Source Code:

* <https://github.com/rheza/SuperGrin/>

Download link:

* <https://github.com/rheza/SuperGrin/releases/tag/1.0.2>

How to install:

1. Download the binary from the github.
2. Extract and Copy the SuperGrin App to Applications Folder.
3. Double-Click the shiny SuperGrin Logo.

How to use it should be pretty straight forward.
Every file that Finalize and Response will be generated to Your Desktop.

Feel free to check the code, to check whether its legit or not. All source code available on Github.

I greatly appreciated any amount to support my work in the future,
Please send http based transaction to,
[http://35.197.132.97:3415 ](http://35.197.132.97:3415/)

Any feedback and support, please write on this thread, I try to help as much as possible.

==================================================

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

==================================================

---

### Post by @Grin1 (2019-02-18)
*Post #2*

I have downloaded the app and all is great so far.

A few questions:

• Is it ok to rename the output files once on the desktop?
• After slate files have been finalizing should they be deleted from computer?
• Is it ok to have multiple transactions or is one at a time?

I will check back for when it’s ready and on main net. I am ready to receive now.
• Do I need to generate new keys or download again when live?

---

### Post by @futurerheza (2019-02-19)
*Post #3*

* Yes. you can rename and change the name to anything.

* Nice one, I think I can make that happen.

* You cannot create multiple transaction before it’s finalized by the network. thats why all the balance will be locked in "Awaiting Confirmation state. I think this is the basic of Grin transaction. I try to read more about this.

* Yes, you need to create the new keys, since the wallet _seed.key will be different for the mainnet

Thanks

---

### Post by @Grin1 (2019-02-19)
*Post #5*

Great I have the new release downloaded and created new wallet.

I have a recieve.input file that I have drag and dropped into the SuperGrin app but I don’t get anything happening. I see the green plus sign before letting go but nothing confirms the file yet. Any suggestions? Perhaps I didn’t fully delete the test wallet?

---

### Post by @futurerheza (2019-02-20)
*Post #6*

Sorry,
I still have some of my floonet code on the production,
This should be fixed on the next release.

**Release note:**
bug fixes release.

* Ask password when user want to send or receive the coin.
* save password to local, so it will not ask as much.
* Please use check balance button, if you think it’s not responsive.

Please replace the old version with this.

[GitHub](https://github.com/rheza/SuperGrin/releases/tag/1.0.1)

### [rheza/SuperGrin](https://github.com/rheza/SuperGrin/releases/tag/1.0.1)

SuperGrin. A GUI Wallet for Grin. Contribute to rheza/SuperGrin development by creating an account on GitHub.

---

### Post by @PoKAHANTAS (2019-02-23)
*Post #7*

futurerheza:

> This app currently only run on Mac, will add the windows release in the coming days.

Any news about the windows release?

---

### Post by @futurerheza (2019-02-25)
*Post #8*

Still working on it though, I think i need to use a workaround for the windows, Like a Automatic password generator. Have you try the Mac version ?

Thanks

---

### Post by @bucketbrigade (2019-06-28)
*Post #12*

[GitHub](https://github.com/GrinPlusPlus/GrinPlusPlus/releases)

### [GrinPlusPlus/GrinPlusPlus](https://github.com/GrinPlusPlus/GrinPlusPlus/releases)

A C++ MimbleWimble/Grin Node For Windows & Mac OS X - GrinPlusPlus/GrinPlusPlus

---



## Follow all the Grin Meetups Here
*Date: 2019-02-18 | [Forum Link](https://forum.grin.mw/t/follow-all-the-grin-meetups-here/4139)*
*Importance Score: 56.1 | Core Participants: hashmap, lehnberg*

### Post by @PoKAHANTAS (2019-02-18)
*Post #1*

Hi Grin Community

This thread is the initial try to save information about Grin Meetups.
I will update it by mentioning the announced meetups for Grin Coin.

Feb 22, Bangkok, THA:** [Grin Asia Meetup] : [Grincon Asia - Bangkok - co-hosted by bitfish and Hashtag Capital | Meetup](https://www.meetup.com/grinasia/events/258729635/)

Mar 26, Amsterdam, NL:** [Grin Amsterdam Meetup] :

[Meetup](https://www.meetup.com/Grin-Amsterdam/events/258141382/)

### [GRIN AMSTERDAM 2019](https://www.meetup.com/Grin-Amsterdam/events/258141382/)

Tue, Mar 26, 2019, 7:30 PM: Grin is coming to Amsterdam on March 26th 2019With presentations by Grin main devsWith Q&ASupporting the Grin Council by contributing 100% of the profits to the Grin Founda

Feel free to post about the meetups dates and locations you know.

---

### Post by @lehnberg ⭐ (2019-02-24)
*Post #2*

There’s also: <https://github.com/mimblewimble/docs/wiki/Events>
Which we hopefully will be able to keep up to date if we all work together!

---

### Post by @kargakis (2019-03-01)
*Post #4*

lehnberg:

> There’s also: [https://github.com/mimblewimble/docs/wiki/Events ](https://github.com/mimblewimble/docs/wiki/Events)

Seems like at least the London meetups are missing?

---

### Post by @lehnberg ⭐ (2019-03-02)
*Post #6*

[@kargakis](/u/kargakis) [@0xb100d](/u/0xb100d) good points - how about adding the events you think are missing to the wiki?

---

### Post by @lehnberg ⭐ (2019-04-21)
*Post #13*

[@PoKAHANTAS](/u/pokahantas) see here for a pretty good recap  <https://cryptonomist.ch/en/2019/03/30/news-grin-amsterdam/>

I would also recommend <https://grinnews.substack.com> as a good resource to keep yourself up to date in general (disclosure: I write it)

---

### Post by @hashmap ⭐ (2019-04-29)
*Post #15*

Moscow, May 16th <https://www.meetup.com/MimbleWimble-Grin-Moscow/events/260942761/>

---

### Post by @lehnberg ⭐ (2019-05-12)
*Post #17*

[Meetup](https://www.meetup.com/grinlondon/events/261345626)

### [Grin & Mimblewimble London: 4th Meetup](https://www.meetup.com/grinlondon/events/261345626)

Tue, Jul 16, 2019, 6:30 PM: Welcome to the first Grin Meetup in London on Mainnet!We'll be hosting a get together with an overview of what has happened since launch, where the project is going, and so

---

### Post by @hashmap ⭐ (2019-06-17)
*Post #19*

[Meetup](https://www.meetup.com/Grin-Seoul/events/262377214/)

### [Grin meetup in Seoul](https://www.meetup.com/Grin-Seoul/events/262377214/)

Tue, Jul 23, 2019, 7:00 PM: Grin meetup in Seoul will be held for the first time!Please attend and enjoy.More details will be announced soon!

---


