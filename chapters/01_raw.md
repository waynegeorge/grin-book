# Chapter 1: MimbleWimble Origins

*8 topics selected for this chapter*

---

## Welcome to Discourse
*Date: 2018-01-16 | [Forum Link](https://forum.grin.mw/t/welcome-to-discourse/8)*
*Importance Score: 77.4 | Core Participants: igno.peverell, lehnberg*

### Post by @system (2018-01-16)
*Post #1*

Grin is a blockchain and a cryptocurrency focused on privacy and scalability. Grin is also an implementation of the MimbleWimble transaction format with the extensions required for a complete blockchain.
The first paragraph of this pinned topic will be visible as a welcome message to all new visitors on your homepage. It’s important!

**Edit this** into a brief description of your community:

* Who is it for?
* What can they find here?
* Why should they come here?
* Where can they read more (links, resources, etc)?

You may want to close this topic via the admin  (at the upper right and bottom), so that replies don’t pile up on an announcement.

---

### Post by @markljenkins (2018-01-24)
*Post #2*

Hello, I’m wondering if another top level category may be created for General Discussion and Community Building. It may be that such a category was intentionally left out since MW seems to be at such an early stage where the chaos of non-technical discourse is more of a distraction, if so please ignore this request.

I am a non-technical person reading the resources available and very interested in this project. I will be fumbling through a Testnet2 install and trying my hand at mining. I think it would be great to start a general discussion area where noobs like me can ask questions and support each other, even dare I say tolerate the inevitable “when lambo?”

As far as I can see, MW GRIN is an evolved crypto that has the potential to eclipse/replace many others. I could be way off base, but I sense that the MW team is actively downplaying publicity during what is still early development stages, nonetheless I know there is already an incredible “buzz” growing for GRIN. I think it would be most excellent to have a small outlet for that enthusiasm in this forum.

---

### Post by @igno.peverell ⭐ (2018-01-24)
*Post #3*

There’s a Lounge category right now but it’s not available when you just sign in. The original intent was to avoid too much noise by allowing only people who have been around for a bit longer. But maybe at this stage it’s a premature protection.

As far as the “when lambo” topics, I was hoping to keep those isolated in the Market category…

---

### Post by @alexrickard86 (2018-02-20)
*Post #6*

Very interested in this project, although the technical knowledge is way beyond me, I’ll try to keep up

---

### Post by @noobvie (2019-05-28)
*Post #11*

Just moved from Zcash community to here for many reasons. Hope GRIN have better visions and future

---

### Post by @ear2ear (2019-07-23)
*Post #13*

Hello, Is this the thread where I introduce myself?

Anyways, I am a long time bitcoiner looking for a new community to interact with. Bitcoin has become a ‘number go up’ meme factory, and frankly its not what I got into crypto for. People here seem pretty knowledgeable, so I am here to absorb all the information I can, and hopefully make a valuable contribution to the community. Thanks for having me

---

### Post by @lehnberg ⭐ (2020-08-13)
*Post #17*

[@cipher](/u/cipher) try again, I bumped your trust level

---

### Post by @rowenta01 (2021-11-05)
*Post #18*

I am a French blogger and I really wish I could post an interview of the Grin project on my blog. Would I have to speak to someone in particular for a request like this?

---



## Grin Mining FAQ - All of the answers to your mining questions
*Date: 2018-01-22 | [Forum Link](https://forum.grin.mw/t/grin-mining-faq-all-of-the-answers-to-your-mining-questions/71)*
*Importance Score: 84.1 | Core Participants: igno.peverell, yeastplume, tromp*

### Post by @Yeastplume ⭐ (2018-01-22)
*Post #1*

I’m going to keep this post updated with answers to the most commonly heard questions about mining in Grin. Please feel free to (politely!) link this FAQ to anyone asking basic mining questions on Gitter or anywhere else. If an answer isn’t on here, I’ll modify the FAQ to include it.

These answers are meant to be very high level and aimed at users rather than developers.

## What Proof-of-Work does GRIN use

Grin uses a proof-of-work system called [Cuckoo Cycle](https://github.com/tromp/cuckoo).

## What is Cuckoo Cycle?

Cuckoo Cycle is a Proof-of-Work algorithm that searches very large graphs for cycles, i.e. a cyclic path (a path that loops back on itself). For most people’s purposes, it’s an algorithm that we hope turns out to be ASIC resistant. An introduction to how it works can be found [here](https://github.com/mimblewimble/grin/blob/master/doc/pow/pow.md).

## What is ‘Graphs per Second’ (GPS)?

Cuckoo Cycle doesn’t work via hashing as most people understand it, it works by searching through large graphs. It makes more sense to think of solver speed in terms of Graph searches per second, or just Graphs per Second.

## What card/rig/setup will best for mining Grin?

The short answer is, ‘nobody knows’. And even if we did, the same answer might not hold true next week.

At the moment, the fastest GPU implementation is John Tromp’s Mean CUDA Miner, which (as of this writing) maxes out at about 1.2 seconds per graph on a 1080ti. A 1080 comes in slightly slower, and a 980ti seems to take about 4 seconds. However, all of these numbers should be taken with a pinch of salt as they represent a very early and unoptimised version of the miner. It’s expected that the community will ultimately step up to create more optimised solvers for various platforms. We have no way of predicting what hardware setup will be the fastest as it will depend on what target platforms the community ends up optimising for.

This being said, I’d like to start collecting real stats on particular GPUs, graph times, and energy efficiency, and make sure they’re all listed in this post. This will likely become more feasible after the launch of Testnet2.

## I want to build a mining system. How does [BUS Speed/RAM Timing/CPU Architecture/LED Colour] affect solve times?

See above. If you’d like to perform tests on your particular hardware to find out, I’ll be happy to share your results with the community here.

## Why are only NVIDIA cards supported?

At present, the only useful GPU solver we have is John Tromp’s CUDA miner. OpenCL/ATI solvers will likely appear in the community very soon after launch, if not before. (If you’re considering writing one, please see the note at the bottom of this post).

## Will I be able to run Multiple GPUs?

Parallel GPU support should work for NVIDIA GPUs on Testnet2 and beyond. You should also be able to run multiple GPUs and CPU mining in parallel.

## Will CPUs be competitive?

Hopefully, but it’s not guaranteed. At the moment, a mid-quality i7 comes is able to search 1 Graph in about 3-4 seconds, which is well within range of the current GPU solver. Presently, it looks as it if running a CPU miner will be worthwhile. We’d hope the ratio of CPU GPS to GPU GPS stays within about 1:5, i.e. a CPU searches 1 graphs in the time it takes a GPU to search 5. However, we don’t know what solvers will exist in the future.

## Does GPU mining work on Testnet1?

No, Testnet1 is using Cuckoo 16, which uses a reduced graph size that works very quickly (as in thousands of graphs per seconds) and uses next to no memory. Mining wasn’t really a focus for Testnet1. Testnet2 and beyond will be running Cuckoo 30, which will take an average of 4GB memory and multiple seconds per graph.

## My CPU isn’t running at 100% on testnet 1

Again, Testnet1 is not performing ‘real’ mining. Cuckoo 30 on Testnet2 and beyond is very much capable of maxxing out your GPU/CPU.

## Can Cuckoo Cycle support pooled mining?

Yes. Pool clients can easily prove they were working on a solution by providing solutions of different cycle lengths valid for the given block. Providing pooling software isn’t a primary goal of Grin, but the intention is to ensure it’s supported in the [Cuckoo Miner Library](https://github.com/mimblewimble/cuckoo-miner)

## Will Grin be mineable on mobile devices?

Possibly, but it probably won’t be practical for a while. Fast Cuckoo 30 mining requires at least 2.5GB of RAM available for use (regardless of whether you’re CPU or GPU mining), which well exceeds the usual amount of RAM on most mobile devices found today (including top-end ones). There is also another solver (the lean miner) that can perform a search using under 200MB of RAM, but with graph search time measured in minutes even on a fast CPU.

That being said, there are a few mobile devices starting to appear that have 4GB of RAM or more, so creating an efficient Cuckoo Cycle solver for one of these devices is technically feasible (and I should add that we have no idea how well it would perform).

## Will Testnet1 or Testnet2 coins be worth anything?

Each coin mined is a point of karma for your assistance in helping us develop and test Grin. Other than that, do not attempt to buy, sell, or trade Testnet coins… they are worth nothing and should never be worth anything due to the beta status of the network from which they originate.

## Why not Proof-of-Stake?

Short answer, because nobody has demonstrated, theoretically or otherwise, that PoS works or even can work as fairly or securely as PoW does.

* * *

Just one other note, if you’re considering writing a Cuckoo-Miner solver, please consider writing it as a plugin for [Cuckoo Miner](https://github.com/mimblewimble/cuckoo-miner). This is the library that interfaces Grin with C/C++ solvers, and creating a plugin that works with it should just be a matter of writing to a specific interface. This way, your solver can be included right out of the box in future versions of Grin in a way that’s (hopefully) easy to use and ‘officially’ supported. Please feel free to contact me for details about how this can work, even if you’re intending to solicit donations via your solver.

---

### Post by @igno.peverell ⭐ (2018-09-04)
*Post #17*

I think we might want to have it at least partially implemented to know all the impacts

---



## How to Mine Cuckoo 30 in Grin: Help us test and collect stats!
*Date: 2018-02-02 | [Forum Link](https://forum.grin.mw/t/how-to-mine-cuckoo-30-in-grin-help-us-test-and-collect-stats/152)*
*Importance Score: 84.3 | Core Participants: yeastplume, tromp, quentinlesceller, lehnberg*

### Post by @Yeastplume ⭐ (2018-02-02)
*Post #1*

# How to mine Cuckoo 30 using Grin

This is a brief guide on how to configure mining at production-level Cuckoo 30 in the current master version of Grin, (i.e.) Testnet2. If you have the hardware and you’d like to help with mining testing efforts, want to get a sense for what mining will be like on Grin’s mainnet, or just want to learn more about mining in Grin, then this guide is for you.

### Building Grin

The first thing you’ll need to do is [build and run grin.](https://github.com/mimblewimble/grin/blob/master/doc/build.md) Follow the instructions for installing prerequisites and building Grin down to the [Build Grin](https://github.com/mimblewimble/grin/blob/master/doc/build.md#build_grin) section of the main build doc, but note that since we’re focused on mining testnet2 at Cuckoo 30, we’ll be using the master branch for now. Ensure you’re building on the correct branch with:

git checkout master
git pull
cargo build

Make sure grin compiles and runs as usual, using the default settings. By default, Grin runs a stratum server on port 13416, which is a server that communicates with remote mining workers. One or many remote ‘miners’ can mine into a single Grin wallet hosted by the grin node.

### Modifications to grin.toml

The default settings in grin.toml should work for running a mining server for testnet2. Ensure you have a copy of grin.toml in your target directory for if you want to make modifications.

If everything is in order, the grin.toml file is in your current directory and the grin executable is in your path, you should just be able to run grin without arguments, e.g:

grin

### Building grin-miner

[grin-miner](https://github.com/mimblewimble/grin-miner) is a standalone mining client that actually runs Cuckoo Cycle solvers and communicates results back to listening stratum mining server on a Grin node. This architecture enables multiple machines mining into the same wallet, and ensures the grin node can’t be taken down by a mining plugin crashing (which happens quite frequently due to the bleeding-edge nature of solvers).

To build grin miner (in a separate directory from Grin or on a separate machine altogether:)

git clone https://github.com/mimblewimble/grin-miner
cd grin-miner
cargo build

More detailed instructions can be found on the [grin-miner build page](https://github.com/mimblewimble/grin-miner/blob/master/doc/build.md)

### Modifications to grin-miner.toml

As with grin, grin-miner should be run in a directory where it can find a grin-miner.toml file. To get a basic miner up and running, ensure that a grin node is running and that grin-miner is configured to point to it in grin-miner.toml in the line:

stratum_server_addr = "127.0.0.1:13416"

If your grin node and grin-miner are on the same machine, the defaults should work. Otherwise, modify this line accordingly.

## Basic CPU Mining

If everything is working correctly, you should see grin-miner connecting, accepting solutions, and mining in the TUI. You should also see the output similar to the following in the logs, which you can view while the application is running with `tail -f grin-miner.log`:

Feb 02 09:46:08.115 INFO Cuckoo plugin 0 - /home/yeastplume/projects/rust/grin/target/debug/plugins/mean_compat_cpu_30.cuckooplugin
Feb 02 09:46:08.115 DEBG Cuckoo Plugin 0: Setting mining parameter NUM_THREADS to 1 on Device 0
.
.
. Followed by:
Feb 02 09:47:03.872 DEBG Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 16.715218787; Graphs per second: 0.060
Feb 02 09:47:03.872 INFO Mining at 0.05982572006641841 graphs per second
Feb 02 09:47:20.754 DEBG Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 16.875651791; Graphs per second: 0.059
Feb 02 09:47:20.754 INFO Mining at 0.0592569704794047 graphs per second

If you see this, then your device is mining away (very, very slowly with the default CPU miner single-threaded). Now we’ve confirmed that mining is working, we can move on to trying to speed it up.

### Plugin Configuration

Different mining implementations can be swapped in and out of the grin-miner client via a plugin system, and you can see the default plugins built by grin-miner by examining the contents of `target/debug/plugins`. By default, grin-miner builds “Lean” and “Mean” versions of cuckoo mining CPU plugins for mining at 2^16 and 2^30 cuckoo sizes. The ‘Lean’ plugin is very slow, but designed to use minimal memory, while ‘Mean’ plugins are designed to go as fast as possible but use as much RAM as is necessary (up to 4Gb in most cases). Generally, you’ll want to be using the mean version of the CPU plugin. You’ll also want to ensure you actually have at least 4Gb RAM free, which probably means having at least 8Gb system RAM total.

By default, `grin-miner.toml` is configured to run the slowest and most widely compatible plugin, which you can see in the uncommented portion of the mining plugin configuration section:

[[mining.miner_plugin_config]]
type_filter = "mean_compat_cpu"
[mining.miner_plugin_config.device_parameters.0]
NUM_THREADS = 4

`type_filter` here denotes that grin will pick up the plugin from grin-miner’s plugin directory called `mean_compat_cpu` at Cuckoo size 30. Each plugin can optionally support multiple devices (which we’ll explore more later), but this particular plugin only has a single device at index 0, indicating the main CPU. To configure this device, parameters are set in the appropriate section, in this case under `[mining.cuckoo_miner_plugin_config.device_parameters.0]`. This particular plugin only has a single parameter which denotes the number of CPU threads the solver will run on.

The `mean_compat_cpu` plugin is intended to be widely compatible, however if your CPU is relatively up-to-date (as in the past few years) you should be able to use the ‘mean_cpu’ miner instead, which contains instructions that only work on newer processors. Chances are your processor will support it, but in any case it’s worth testing this by stopping grin, changing the following setting, and running again:

type_filter = "mean_cpu"

Which in the case of my development machine, (a middle-of-the-road i7-4790k at 4GHz), results in somewhat better performance; roughly 12 seconds instead of 17:

Feb 02 10:05:59.409 DEBG Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 11.978399334; Graphs per second: 0.083
Feb 02 10:05:59.409 INFO Mining at 0.08348360846190503 graphs per second

But we can do better… This particular device has 4 CPU cores, (which you can see if you run `cat /proc/cpuinfo`,) so I’ll try setting the number of threads to the number of physical cores in my CPU:

[mining.cuckoo_miner_plugin_config.device_parameters.0]
NUM_THREADS = 4

And try again. This time, I get output along the lines of:

Feb 02 10:08:40.870 DEBG Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 3.79394227; Graphs per second: 0.264
Feb 02 10:08:40.871 INFO Mining at 0.26357807495051844 graphs per second

Just under 4 seconds, which is starting to look much more promising. Let’s try 8 threads (as I actually have 8 virtual cores):

Feb 02 10:11:00.097 DEBG Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 3.359463397; Graphs per second: 0.298
Feb 02 10:11:00.097 INFO Mining at 0.29766658594732714 graphs per second

Which gets me under 3.5 seconds. For fun, let’s try 16:

Feb 02 10:12:17.759 INFO Mining at 0.30098994282890174 graphs per second
Feb 02 10:12:21.080 DEBG Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 3.31403283; Graphs per second: 0.302

Which seems to shave 4 hundreths of a second off of graph times. I can tweak and test as much as I like, but for the purposes of this example, I’ll stop here.

Also, note that if I inspect CPU usage using the `top` command, I can see my entire CPU is happily engaged during one of these runs.

%Cpu0  :  94.7/1.3    96[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    ]
%Cpu1  :  96.7/0.7    97[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  ]
%Cpu2  :  96.7/0.0    97[|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||   ]
%Cpu3  :  94.7/0.7    95[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    ]
%Cpu4  :  97.4/0.7    98[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  ]
%Cpu5  :  96.7/1.3    98[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  ]
%Cpu6  :  96.0/0.0    96[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    ]
%Cpu7  :  96.0/0.0    96[||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    ]

Your individual results will vary depending on many factors, but the take-away here is that tuning mining for your individual system is going to be an iterative process of tweaking parameters and observing the results. From my own experience, I know that the mean_cpu miner is unlikely to get much faster than this on my system, so I’ll leave these settings for now and move on to how we can configure a GPU miner:

## GPU (CUDA) Mining

### CUDA and nvidia-smi

Next, I’m going to try configuring my system to run a GPU miner within Grin. As noted in the [Mining FAQ](https://forum.grin.mw/t/grin-mining-faq-all-of-the-answers-to-your-mining-questions/71), only nVidia cards are supported… ATI solvers will very probably be coming later from the community.

Assuming you have an appropriate CUDA-compatible card (anything from the 9xx or 10xx series should work,) and the appropriate drivers installed (usually a package called `nvidia`) you first need to enable the building of the CUDA plugins on your system. For this, you’ll first need the nVidia `cuda` package which contains the cuda libraries and special versions of gcc used to compile cuda GPU code:

#whatever package manager your distro uses.. (don't just type the below)
[apt-get install][pacman -Sy][etc] cuda

The `cuda` package is generally quite large, so allow it to install and then check it’s working with (you may have to log out and into your shell again):

nvcc
nvcc fatal   : No input files specified; use option --help for more information

Also, it’s handy to look at the output of `nvidia-smi` to get stats on your installed cards. On my system, ‘nvidia-smi’ shows a single 980Ti:

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 387.34                 Driver Version: 387.34                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 980 Ti  Off  | 00000000:01:00.0  On |                  N/A |
| 29%   47C    P0    71W / 250W |    923MiB /  6077MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

This utility is useful for measuring workload and power usage. You can also get continually updating output via:

nvidia-smi dmon

Which scrolls output like the following until interrupted:

# gpu   pwr  temp    sm   mem   enc   dec  mclk  pclk
# Idx     W     C     %     %     %     %   MHz   MHz
0    18    46     0     7     0     0   405   135
0    18    46     1     7     0     0   405   135
0    18    46     1     7     0     0   405   135
0    18    46     0     7     0     0   405   135
0    18    46     0     7     0     0   405   135

### Building grin-miner’s CUDA plugin

Assuming the cuda package is installed as described above, next we need to configure grin-miner to build the CUDA enabled plugins. We do this by editing the file `util/Cargo.toml` in grin-miner’s source directory as follows:

#uncomment this feature to enable cuda builds (cuda toolkit must be installed)
features=["build-cuda-plugins"]

Remove the `#` from the beginning of the `#features=["build-cuda-plugins"]` line and save the file. Then rebuild grin-miner from the top-level grin-miner directory as usual:

cargo build

Then cross your fingers and hope the build works. You may come across a situation whereby the build attempts to use a version of GCC that’s incompatible with the cuda library you’re using, in which case you can override the GCC compiler used during the build via:

CUDA_HOST_COMPILER=[PATH_TO_GCC] cargo build

Many things could go wrong at this point with the build, and many conditions and cases aren’t yet handled in the underlying cmake files controlling the build. This portion of the build should get more robust over time, but for now if you have an issue you can’t fix, seek help on gitter or the forums.

If everything goes successfully with the build, you should see the cuda plugin appear in the `target/debug/plugins` directory of the grin build as in the following listing:

cuda_30.cuckooplugin      lean_cpu_30.cuckooplugin         mean_compat_cpu_30.cuckooplugin  mean_cpu_30.cuckooplugin
lean_cpu_16.cuckooplugin  mean_compat_cpu_16.cuckooplugin  mean_cpu_16.cuckooplugin

If you see `cuda_30.cuckooplugin` as listed above, you should be good to go.

### Configuring grin.toml for CUDA

Next, we’re going to try mining on a single CUDA device instead of the CPU, which just means enabling the CUDA plugin in grin.toml. For now, comment out the `mean_cpu` configuration from earlier:

#[[mining.miner_plugin_config]]
#type_filter = "mean_cpu"
#[mining.cuckoo_miner_plugin_config.device_parameters.0]
#NUM_THREADS = 16·

And comment in the following a bit further down in the file:

[[mining.miner_plugin_config]]
type_filter = "cuda"
[mining.miner_plugin_config.device_parameters.0]
USE_DEVICE = 1

Now restart Grin. This will start mining on whatever CUDA device shows up on your system as device 0, in my case, a still useful but slightly ageing 980Ti:

Feb 02 11:46:06.290 DEBG Plugin 0 - Device 0 (GeForce GTX 980 Ti) Status: OK - Last Graph time: 3.60286413; Graphs per second: 0.278
Feb 02 11:46:06.291 INFO Mining at 0.27755695577673645 graphs per second

Which is this case, is even slower than the mean CPU miner at 8 threads! However, we’re confirmed as GPU mining at this stage.

### Running Multiple Plugins

Grin-miner can run multiple plugins, or multiple devices configured within a particular plugin. To try this, without removing our GPU configuration, let’s comment back in the earlier CPU configuration:

[[mining.miner_plugin_config]]
type_filter = "mean_cpu"
[mining.cuckoo_miner_plugin_config.device_parameters.0]
NUM_THREADS = 8

And run grin-miner again. This time, we can see both plugins working away in the output, and our combined graphs per second has roughly doubled:

Feb 02 11:59:39.068 DEBG Mining: Plugin 0 - Device 0 (CPU) Status: OK : Last Graph time: 3.562477409s; Graphs per second: 0.281 - Total Attempts: 3
Feb 02 11:59:39.070 DEBG Mining: Plugin 1 - Device 0 (GeForce GTX 980 Ti) Status: OK : Last Graph time: 3.890610665s; Graphs per second: 0.257 - Total Attempts: 2
Feb 02 11:59:39.070 INFO Mining at 0.5377325938934971 graphs per second

### Running Multiple GPUs

You may have multiple GPUs in your machine (like in a dedicated mining rig, for instance). In this case, you can configure the cuda plugin to run as many on them at a time as you desire.

To do this, modify the cuda plugin configuration section of grin.toml to look roughly similar to the following, (depending on how many devices you want to use):

#Parameters can be set per device, as below. In sync mode
#device 0 is currently the only device used. In async mode
#device 0 is used by default, and all other devices are
#disabled unless explicitly enabled by setting the 'USE_DEVICE'
#param to 1 on each device, as demonstrated below.

[[mining.miner_plugin_config]]
type_filter = "cuda"
[mining.miner_plugin_config.device_parameters.0]
USE_DEVICE = 1

# Below are advanced optional per-device tweakable params

#GENU_BLOCKS = 256
#GENU_TPB = 8
#GENV_STAGE1_TPB = 32
#GENV_STAGE2_TPB = 128
#TRIM_STAGE1_TPB = 32
#TRIM_STAGE2_TPB = 96
#RENAME_0_STAGE1_TPB = 32
#RENAME_0_STAGE2_TPB = 64
#RENAME_1_STAGE1_TPB = 32
#RENAME_1_STAGE2_TPB = 128
#TRIM_3_TPB = 64
#RENAME_3_TPB = 2

[mining.miner_plugin_config.device_parameters.1]
USE_DEVICE = 1

#[mining.miner_plugin_config.device_parameters.2]
#USE_DEVICE = 1

Note we’re leaving the advanced tweakable parameters commented out for now, and will just use the defaults. In my case, I’ve switched to another machine with 2 GPUs installed, and I’ve enabled another section to include the second device. If I had a third installed, I’d add another sections such as
`[mining.cuckoo_miner_plugin_config.device_parameters.3]` and configure parameters for it as desired.

At a minimum, each device other than 0 has to have `USE_DEVICE = 1` in order to run. Whatever your system sees as device 0 will run by default, and the `USE_DEVICE = 1` is optional in that case (you can set it to 0 to exclude it from mining).

Now, running grin-miner again (note again I’ve switched machines for this example,) on a system with an i5 CPU, a 1080 and a 1080Ti, I get output like the following:

Feb 02 12:16:25.027 DEBG Mining: Plugin 0 - Device 0 (CPU) Status: OK : Last Graph time: 4.019902621s; Graphs per second: 0.249 - Total Attempts: 2
Feb 02 12:16:25.028 DEBG Mining: Plugin 1 - Device 0 (GeForce GTX 1080 Ti) Status: OK : Last Graph time: 1.135864421s; Graphs per second: 0.880 - Total Attempts: 6
Feb 02 12:16:25.028 DEBG Mining: Plugin 1 - Device 1 (GeForce GTX 1080) Status: OK : Last Graph time: 1.789290858s; Graphs per second: 0.559 - Total Attempts: 4
Feb 02 12:16:25.029 INFO Mining at 1.6880296360141922 graphs per second

For a blazing 1.7 graphs per seconds average! As grin-miner is currently configured, I should hopefully solve a block in about 30 seconds mining solo at difficulty 1.

### Advanced Parameters

In the case of this particular GPU plugin, each device can be configured with a set of tweakable parameters. The exact meaning of these parameters are difficult to explain without getting into very low level details about how the current GPU miner works, but it’s still possible to try modifying these values and see what effects they have on graph times. For instance, I’m going to attempt to change `#GENV_STAGE1_TPB` to 128 on the 1080ti and see what happens:

#GENU_BLOCKS = 256
#GENU_TPB = 8
GENV_STAGE1_TPB = 128
#GENV_STAGE2_TPB = 128
#TRIM_STAGE1_TPB = 32
#TRIM_STAGE2_TPB = 96
#RENAME_0_STAGE1_TPB = 32
#RENAME_0_STAGE2_TPB = 64
#RENAME_1_STAGE1_TPB = 32
#RENAME_1_STAGE2_TPB = 128
#TRIM_3_TPB = 64
#RENAME_3_TPB = 2

After uncommenting the appropriate line and changing the value, I get:

Feb 02 12:23:55.072 DEBG Mining: Plugin 0 - Device 0 (CPU) Status: OK : Last Graph time: 4.125390899s; Graphs per second: 0.242 - Total Attempts: 4
Feb 02 12:23:55.072 DEBG Mining: Plugin 1 - Device 0 (GeForce GTX 1080 Ti) Status: OK : Last Graph time: 1.250153236s; Graphs per second: 0.800 - Total Attempts: 13
Feb 02 12:23:55.072 DEBG Mining: Plugin 1 - Device 1 (GeForce GTX 1080) Status: OK : Last Graph time: 1.868723816s; Graphs per second: 0.535 - Total Attempts: 8
Feb 02 12:23:55.073 INFO Mining at 1.5774277673945534 graphs per second

Looks like it made things a 10th of a second slower. Now I’ll try tweaking something else:

TRIM_STAGE_2_TPB = 256

And I get:

Feb 02 12:27:51.839 DEBG (Server ID: Port 13414) Mining at Cuckoo30 for at most 90 secs at height 3 and difficulty 1.
Device 0 GPUassert: unspecified launch failure /home/mcordner/.cargo/git/checkouts/cuckoo-miner-4752934f0f1f2bfe/7608c1a/src/cuckoo_sys/plugins/cuckoo/src/mean_miner.cu 948
Device 1 GPUassert: unspecified launch failure /home/mcordner/.cargo/git/checkouts/cuckoo-miner-4752934f0f1f2bfe/7608c1a/src/cuckoo_sys/plugins/cuckoo/src/mean_miner.cu 928
Feb 02 12:27:54.054 DEBG Mining: Plugin 0 - Device 0 (CPU) Status: OK : Last Graph time: 0s; Graphs per second: inf - Total Attempts: 0
Feb 02 12:27:54.055 DEBG Mining: Plugin 1 - Device 0 (GeForce GTX 1080 Ti) Status: ERRORED : Last Graph time: 1.377844771s; Graphs per second: 0.726 - Total Attempts: 1
Feb 02 12:27:54.055 DEBG Mining: Plugin 1 - Device 1 (GeForce GTX 1080) Status: ERRORED : Last Graph time: 1.444037082s; Graphs per second: 0.693 - Total Attempts: 1
Feb 02 12:27:54.056 INFO Mining at 1.4182741537420638 graphs per second

Oops… I’ve likely exceeded a memory limit and caused everything to fail. (Note that the status of the GPU devices is ERRORED, which is a bad thing) In this case, I set values back and try something else.

Parameters and their meanings will change depending on the plugin implementation, and when new implementations come out they will most likely have completely different sets of tuning parameters.

### Cuckoo cuda_30 Parameters

A full tuning guide for the current cuda_30 plugin, with explanations for each parameter that can be used in grin.toml can be found here. Note that the names of the parameters in the guide are slightly different from the names in grin.toml; mappings are:

N_TRIMS -> -m trims
N_BLOCKS -> -b blocks
GENU_BLOCKS -> -U blocks
GENU_TPB -> -u threads
GENV_STAGE_1_TPB -> -V threads
GENV_STAGE_2_TPB -> -v threads
TRIM_STAGE_1_TPB -> -T threads
TRIM_STAGE_2_TPB -> -t threads
RENAME_0_STAGE_1_TPB -> -X threads
RENAME_0_STAGE_2_TPB -> -x threads
RENAME_1_STAGE_1_TPB -> -Y threads
RENAME_1_STAGE_2_TPB -> -y threads
TRIM_3_TPB -> -Z threads
RENAME_3_TPB -> -z threads

[github.com](https://github.com/tromp/cuckoo/blob/master/GPU_tuning.md)

#### [tromp/cuckoo/blob/master/GPU_tuning.md](https://github.com/tromp/cuckoo/blob/master/GPU_tuning.md)

Tuning the GPU solver
============

Recall the solver options:

SYNOPSIS
cuda30 [-b blocks] [-d device] [-h hexheader] [-k rounds [-c count]] [-m trims] [-n nonce] [-r range] [-U blocks] [-u threads] [-V threads] [-v threads] [-T threads] [-t threads] [-X threads] [-x threads] [-Y threads] [-y threads] [-Z threads] [-z threads]
DEFAULTS
cuda30 -b 128 -d 0 -h "" -k 0 -c 1 -m 256 -n 0 -r 1 -U 128 -u 8 -V 32 -v 128 -T 32 -t 128 -X 32 -x 64 -Y 32 -y 128 -Z 32 -z 8

Let's look at each of these in turn.

-b blocks
------------
The number of threadblocks to use, which should be a 2-power between 1 and 128. Default is 64.
Each block requires its own 21MB memory buffer. Here's how memory (in MB) and graph times in (ms)
vary with different blocks on an NVIDIA 1080 Ti

_      |     1 |     2 |    4 |    8 |   16 |   32 |   64 |  128
-----  | ----- | ----- | ---- | ---- | ---- | ---- | ---- | ----

This file has been truncated. [show original](https://github.com/tromp/cuckoo/blob/master/GPU_tuning.md)

### Collecting stats

So, if you’ve got this far, hopefully you’ve been able to mine on at least your CPU and hopefully one or more CUDA devices. Now that you’ve gone this far, please help us out by posting your findings below! Collecting metrics for all of the varying hardware specs will be invaluable feedback for development and for the entire Grin community!

When posting your findings, please be sure to note as much relevant information as you can about details of your setup, for instance (not exhaustive):

* Number of GPU/CPUs you’re running
* CPU: vendor, make, clock speed (e.g intel i7 4790k @ 4.2 Ghz)
* GPU: vendor, reference spec, RAM, overclock status (ASUS 1080Ti at stock speeds)
* GPS (graphs per second) you’re getting for each device (can be found via debug logging)
* Power usage (important!) collected from `nvidia-smi dmon` output (see the mining guide above for details)
* Whether you’re running a single device in sync more or async mode
* Parameters you’re setting for each device within grin.toml
* How long you’ve been able to mine without seeing errors
* If errors occur, and details from the logs/backtraces you can find.

And more bits of info which aren’t coming to mind right this moment but I’m sure will become evident. Once we have a decent number of stats, we’ll figure out the best way to collate them (possibly a google spreadsheet or the like). Also, if anyone from the community wants to take over stat compilation it would be much appreciated and I’ll do whatever’s needed to support them!

Looking very forward to seeing some findings below!

Happy mining!

---

### Post by @Yeastplume ⭐ (2018-02-03)
*Post #7*

Thanks for all the stats so far! Just to make them a bit more useful, be sure you’re letting us know what settings you’re using in grin.toml… we definitely need to know how many threads you’re using if you’re testing with the mean cpu miner.

---

### Post by @quentinlesceller ⭐ (2018-02-06)
*Post #9*

Intel® Core™ i7-6567U CPU @ 3.30GHz
2 Core 4 threads
16 Go 2133 MHz LPDDR3

Cuckoo Plugin 0: Setting mining parameter NUM_THREADS to 1 on Device 0
Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 13.331727716; Graphs per second: 0.075

Cuckoo Plugin 0: Setting mining parameter NUM_THREADS to 2 on Device 0
Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 7.766053389; Graphs per second: 0.129

Cuckoo Plugin 0: Setting mining parameter NUM_THREADS to 4 on Device 0
Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 6.928913164; Graphs per second: 0.144

Cuckoo Plugin 0: Setting mining parameter NUM_THREADS to 8 on Device 0
Plugin 0 - Device 0 (CPU) Status: OK - Last Graph time: 7.383482248; Graphs per second: 0.135

---

### Post by @tromp ⭐ (2018-03-01)
*Post #19*

No; it never goes over 5.5GB on my GPU solver.

---

### Post by @quentinlesceller ⭐ (2018-07-06)
*Post #25*

Join us in the [Gitter](https://gitter.im/grin_community/Lobby) so we can help you.

---

### Post by @lehnberg ⭐ (2018-11-30)
*Post #31*

Wiki page for collection of GPU mining stats on Testnet 4 and beyond: <https://github.com/mimblewimble/docs/wiki/GPU-Mining-Stats>

---

### Post by @tromp ⭐ (2019-01-17)
*Post #40*

grin.toml only existed on the earlier testnets.
it’s now called grin-server.toml

---



## Grin Logos for Community Consideration
*Date: 2018-02-02 | [Forum Link](https://forum.grin.mw/t/grin-logos-for-community-consideration/155)*
*Importance Score: 227.7 | Core Participants: igno.peverell, jaspervdm, yeastplume, hashmap, tromp, lehnberg*

### Post by @ColinCreevey (2018-02-02)
*Post #1*

There have been a few previous submissions for a logo – if you have made one, please post here so the community has the greatest variety of submissions to choose from.

---

### Post by @lehnberg ⭐ (2018-05-10)
*Post #39*

Personally, my vote from everything I’ve seen so far would go on [@0xb100d](/u/0xb100d)’s avatar image (assuming we would have permission to use it, and it’s not being used elsewhere? Not seen it used anywhere else.)

Simple, circular, has that cheeky feel to it, _stands out_ from all other coins logos (and would stand out as an icon anywhere, on a phone home screen, on a t-shirt, on a website, and so on), and works well in a simpler two-color format as well. Very flexible. Very simple. I love it.

---

### Post by @lehnberg ⭐ (2018-08-03)
*Post #58*

Thanks for sharing these variations [@Jason](/u/jason)! For what it’s worth, I still prefer [@0xb100d](/u/0xb100d)’s original, quite a lot.

It feels more warm, playful, and anarchic. The font (if it is a font and not just shapes?) in the original have some subtleties (not so rigid, not perfectly straight edges etc) that makes it feel more alive. As it is a play on the eyes of the original [“smiley-face”](https://www.google.com/search?tbm=isch&source=hp&biw=1302&bih=803&ei=sBZkW_m5F8eckwW3javQAw&q=original+smiley+face&oq=original+smiley+face&gs_l=img.3..0l4j0i30k1j0i8i30k1j0i24k1l2.2235.5351.0.5480.27.21.3.3.3.0.127.1849.13j7.20.0....0...1ac.1.64.img..1.26.1878.0..0i10k1j0i5i30k1.0.uOXXcw8t2cU) I think it makes a lot of sense. Additionally, the smile is not going up all the way to 180º, but stops a bit short of that in order to resemble a smile a bit better. These are just my personal thoughts that stood out immediately when looking at these.

* * *

Now as a side-note, something that was discussed in Gitter, was the idea of being anarchic-by-design, and not have _any_ “official” logo for the project. It’s a currency, we’re not trying to sell anything. The USD or the GBP has a currency symbol, yes, but there’s no logo. Smaller currencies throughout the world that do not have a symbol, still do not have a logo. The Swedish krona I think has something like 100:- to symbolise SEK or they just abbreviate to 100 kr. Still no logo. That does not mean that there should not be a logo, just that anyone can make a logo and there is no “official” one. Anyone is free to use whatever they like! “Let a thousand flowers bloom”, to misquote Chairman Mao.

I’m warming to this idea. The only real place I think might cause issues are in coinmarketcap-esque sites that expect a logo, need a logo, and then what if different sites use different logos? In any case, figuring out how to best handle these issues seems like a nice problem to have once mainnet is released.

---

### Post by @lehnberg ⭐ (2018-08-13)
*Post #64*

bigkev:

> I agree that no logo is a good idea in spirit, but the exchanges will be looking for something to use. If we don’t have an “official” logo, they’ll go with whatever’s on “the website.” If the main [grin.mw](http://grin.mw) website doesn’t have a logo, they’ll go to the next best thing, which may or may not be a shitty logo.

For what it’s worth, I saw this happening here: [An Overview of Privacy in Cryptocurrencies | by Richard Chen | The Control](https://thecontrol.co/an-overview-of-privacy-in-cryptocurrencies-893dc078d0d7?gi=98bad8a0570)
Article uses a fairly random Grin logo (_I think_). Haha not sure it’s that big of a deal tbh.

---

### Post by @igno.peverell ⭐ (2018-09-07)
*Post #82*

I’d love a vector format of the first.

---

### Post by @lehnberg ⭐ (2018-09-08)
*Post #91*

[@Askepios](/u/askepios) [@0xb100d](/u/0xb100d) I made some logo comparisons, see below:

[logoVariations595×525 41.2 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/d3e43f10fe6606ad2764b33ddb68e02c7ba4b01d.png "logoVariations")

In general, I think this logo works really well, across board and in many different sizes and variations. Gives us a lot of flexibility. Since we’re talking about merchandise (I’ve been thinking about it as well btw, would both be cool and a nice little source of income for the dev fund!), it might make sense to ensure the yellow is [print friendly](https://www.printninja.com/printing-resource-center/file-setup/offset-printing-guidelines/offset-color-requirements/cmyk-suggested-values) and can be represented in the physical world well. Variation C above might possibly work better in that regards, but not sure I like it that much. I personally prefer a bit more “neon” in it (as A and B have). Or we could just say we’re ok that the logo will look different in web/digital and in print/physical, but I think that would be a missed opportunity to be consistent across board. Any thoughts?

> if we’re talking a ‘Grin’ or ‘GRIN’ to go with the smiley face, I’d go for an extension of its curves and shapes—probably derived from the eyes.

I took a **quick & dirty** stab at a _prototype_ of this, as below. Even if I absolutely suck at using the vector tool properly, and the letters I made **stink** , I think we could be on to something here. The `G` was derived from the mouth, the `I` from the M-eye and the `N` from the W-eye. With `R` being drawn up from the I.

Is there’s anyone who’s a bit better at free-form drawing, who would like to take a stab at making a version that actually looks good?

Also, for good measure, here are some variations with traditional fonts:

[fontVariations595×842 32.5 KB](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/4600a022794c993ddcdc219230f0688c2b0bccd8.png "fontVariations")

---

### Post by @lehnberg ⭐ (2018-09-20)
*Post #110*

[@tromp](/u/tromp) [@drvn](/u/drvn) here’s a 5 minute quick n dirty prototype:

[ Test574×583 7.62 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/4c2fb73ace79d145db4c7b8f268dc0da96624074.png "Test")

#### My personal 2 cents (about the original version)

Pros: Really nice and creative concept, in particular chained blocks, and cut through, very much in the spirit of Grin!

Cons: Not super legible, not sure how it looks big and small, does not feel particularly iconic/memorable, and… it feels to me as though the ICOs of past have already taken the “hey let’s make a minimalist logo out of some geometric shapes”-idea and iterated on it in absurdum. I therefore fear that this style would have Grin blend in very neatly with the general population of alt-coins. This is not the fault of the logo itself, it’s rather a victim of unfortunate circumstances.

---

### Post by @lehnberg ⭐ (2018-09-21)
*Post #115*

[ Screen Shot 2018-09-21 at 09.31.36.png2040×978 93.8 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/9b4218b86437825dc338a590fc18ce74039a77c0.png "Screen Shot 2018-09-21 at 09.31.36.png")

Beam uses the current logo in their comparison table, and I personally think it makes Grin look _great_ , in particular compared to the other logos. It truly stands out from the crowd.

---



## Grin Wallet URL Format
*Date: 2018-02-16 | [Forum Link](https://forum.grin.mw/t/grin-wallet-url-format/188)*
*Importance Score: 79.0 | Core Participants: igno.peverell, tromp, antioch, lehnberg*

### Post by @rodarmor (2018-02-16)
*Post #1*

Greetings all!

Grin payees currently provide IP addresses to payers so that their wallets can rendezvous and complete the payment. We’ll need to switch to a more robust address scheme eventually, and I wanted to create this thread to get the discussion going.

The current scheme has a number of drawbacks:

* Vulnerable to man-in-the-middle attacks
* Requires the payee to be publicly reachable, which in practice will require the payee to configure their firewall or NAT
* Reveals the network location of the participants to one another, and to others who might observe the address, for example if a request for payment is posted in a public forum or on a mailing list
* May expire unpredictably, since not all IP addresses are static

I’ve written a [wiki page outlining a number of possible alternatives](https://github.com/casey/grin/wiki/Addresses). I intend for it to be comprehensive, so do let me know if I’ve left something out!

My personal suggestion, although this shouldn’t carry much weight as I won’t be able to help implement it, is as follows:

I think that first switching to `pubkeyhash@ip` / `pubkeyhash@domain` and using the key to authenticate and encrypt the connection is probably prudent. This would fix the current vulnerability to man-in-the-middle attacks. Also, the code to implement this scheme will not be obviated by later improvements, so it won’t be wasted effort, even if we switch to another scheme.

After that, I think that using Tor hidden services is the best longterm solution. This would eliminate firewall and NAT issues, as hidden service clients and servers use outbound connections only, obscure network addresses, and allow a new address to be generated per payment.

However, Tor is a somewhat painful dependency, as it is written in C, and we would need to include a separate Tor binary in standalone Grin distributions, or require that the end user install it with a package manager.

What do y’all think?

---

### Post by @igno.peverell ⭐ (2018-02-16)
*Post #2*

Superficial level first: I wouldn’t talk about addresses or address format, that’s going to confuse people. Whatever we come up with will have totally different characteristics and will live at a different stack level compared to say bitcoin addresses. So how about wallet URL?

Otherwise I share your conclusions. Thanks for doing this!

---

### Post by @igno.peverell ⭐ (2018-03-11)
*Post #11*

I wouldn’t call them Vaults, as it usually means this (that’s what I thought you were going to talk about first):

[Hacking Distributed](https://hackingdistributed.com/2016/02/26/how-to-implement-secure-bitcoin-vaults/)

### [How to Implement Secure Bitcoin Vaults](https://hackingdistributed.com/2016/02/26/how-to-implement-secure-bitcoin-vaults/)

We have come up with a simple and elegant technique for implementing hack-proof Bitcoin vaults, to deter Bitcoin thefts.

If you directly share peer IPs, how do you allow any privacy layer?

---

### Post by @antioch ⭐ (2018-05-22)
*Post #14*

Just got Wireguard (<https://www.wireguard.com/>) installed on a couple of machines, primarily to test out running a personal VPN. Their “Cryptokey Routing” ([WireGuard: fast, modern, secure VPN tunnel](https://www.wireguard.com/#cryptokey-routing)) concept got me thinking back to this topic. Specifically the concept of public keys verifying point to point communication (and distributing them out of band somehow).

> At the heart of WireGuard is a concept called Cryptokey Routing, which works by associating public keys with a list of tunnel IP addresses that are allowed inside the tunnel. Each network interface has a private key and a list of peers. Each peer has a public key. Public keys are short and simple, and are used by peers to authenticate each other. They can be passed around for use in configuration files by any out-of-band method, similar to how one might send their SSH public key to a friend for access to a shell server.

> In other words, when sending packets, the list of allowed IPs behaves as a sort of routing table, and when receiving packets, the list of allowed IPs behaves as a sort of access control list.

Makes me wonder if this might be worth a deeper look - I could imagine a possible world where each Grin wallet endpoint is running an embedded WireGuard and communicates with other endpoints based on an “internal” (to the VPN) IP and a known public key.

Edit: adding some info on the Wireguard protocol and encryption used (mainly a wishlist of modern “best practice”) -

[wireguard.com](https://www.wireguard.com/protocol/)

### [Protocol & Cryptography - WireGuard](https://www.wireguard.com/protocol/)

* ChaCha20 for symmetric encryption, authenticated with Poly1305, using RFC7539’s AEAD construction
* Curve25519 for ECDH
* BLAKE2s for hashing and keyed hashing, described in RFC7693
* SipHash24 for hashtable keys
* HKDF for key derivation, as described in RFC5869

Wireguard is an implementation of the Noise Protocol <http://noiseprotocol.org/>

---

### Post by @lehnberg ⭐ (2018-07-09)
*Post #18*

[@tianshi](/u/tianshi) I’ve been looking at Matrix as well in the context of transaction building. Do you have hands on experience using it? It appeared a bit… unstable and full of friction… last time I checked it out.

---

### Post by @tromp ⭐ (2018-07-14)
*Post #20*

Because there are no addresses in Mimblewimble and transacting requires interaction between sender and receiver.

---

### Post by @tromp ⭐ (2018-07-14)
*Post #22*

No; the wallet doesn’t care what IP address you use. It scans all new outputs and rangeproofs to see which ones could have been produced from your private keys.

---

### Post by @lehnberg ⭐ (2019-01-04)
*Post #28*

[github.com/mimblewimble/grin](https://github.com/mimblewimble/grin/issues/1798) [ ](https://github.com/hashmap)

#### [Issue: P2P transaction building](https://github.com/mimblewimble/grin/issues/1798)

opened by [hashmap](https://github.com/hashmap) on [2018-10-19](https://github.com/mimblewimble/grin/issues/1798)

It would be beneficial for user experience to implement p2p transaction buiding, secure and nat/firewall friendly. The current methods have the...

research

---



## Genesis block message
*Date: 2018-03-07 | [Forum Link](https://forum.grin.mw/t/genesis-block-message/250)*
*Importance Score: 69.2 | Core Participants: igno.peverell, yeastplume, tromp*

### Post by @harry.potter (2018-03-07)
*Post #1*

We all know what the bitcoin genesis block says about wallstreet / bank bailout. What will be the timeless message of gringots, have you any idea? we need a solid quote or something.

The best quote is quite long, maybe an exception as to the length of the message in the genesis block can be secured.

“Enter, stranger, but take heed
Of what awaits the sin of greed,
For those who take, but do not earn,
Must pay most dearly in their turn.
So if you seek beneath our floors
A treasure that was never yours,
Thief, you have been warned, beware
Of finding more than treasure there.”
― J.K. Rowling, Harry Potter and the Sorcerer’s Stone

“remember to wake devs from cryostatis in the year 2500 so that they can add big numbers to the source code”
― Harry Potter

---

### Post by @igno.peverell ⭐ (2018-03-07)
*Post #2*

It makes me a little sad but it doesn’t seem that we’ll be able to embed any text in our genesis block. Somewhat by design, all the data is obscured and there are no “open fields”.

---

### Post by @tromp ⭐ (2018-03-09)
*Post #5*

We can put in a hash of any text we like as the prevhash (which would otherwise be 0).
That’s as good as putting the text itself in…

---

### Post by @igno.peverell ⭐ (2018-03-11)
*Post #8*

I like having the previous hash be all zeroes. Makes it nice and explicit that this is the genesis block.

---

### Post by @tromp ⭐ (2018-03-13)
*Post #9*

I agree having a 0 prevhash is a very desirable feature. Which leaves only a few places to put in the hash of a freely chosen text. One such place is the blinding factor of the coinbase. Which means the message could only be revealed once that coinbase is spent. Possibly (perhaps Yeastplume can confirm) it could also be injected into the coinbase rangeproof.
Any other places anyone can think of?

---

### Post by @igno.peverell ⭐ (2018-03-14)
*Post #12*

In principle, I agree. But practically it conflicts with another requirement: the genesis block _itself_ needs to be pre-mined. And that’s somewhat required to avoid something closer to “instamine” (unless we cheat in some other way).

We need to initialize the chain with a high enough difficulty so that the first few thousand blocks don’t get mined within minutes. How high exactly is hard to tell, but as high as possible is probably the best estimate we can come up with. This means the proof of work on the genesis block needs to satisfy that difficulty. And computing that PoW is going to take us weeks, maybe a month.

There’s one possible solution: allowing the genesis block to not satisfy the initial difficulty. However we find this somewhat distasteful, especially for [@tromp](/u/tromp).

---

### Post by @igno.peverell ⭐ (2018-03-15)
*Post #14*

A GTX 1080 ti is around 32MH/s mining Ethereum. The total Ethereum hashrate is about 260,000 GH/s. That’s the equivalent of about 8.1 million such graphic cards. Let’s double this to account for other chains, and assume that 0.5% of that will want to give a shot at mining grin for a bit. That’s a conservative estimate of 80,000 GPUs that could be mining on mainnet at launch. For reference, when Zcash launched, it wiped out about 45% of Ethereum’s hashrate.

Now assume we can only get together 20 GTX 1080 ti to work on the genesis block. Those 20 will need to work for `80000/20 = 4000` minutes, or over 2.5 days, to build a single valid genesis.

---

### Post by @igno.peverell ⭐ (2018-04-03)
*Post #17*

Yes, ECC curve points addition (and subtraction) allows you to validate both that each block have the expected additional supply and that the total supply since the beginning of the chain is what’s expected as well. Every time a new node syncs, total supply is checked.

---



## Yeastplume - Progress update thread - May - Sept 2018
*Date: 2018-05-04 | [Forum Link](https://forum.grin.mw/t/yeastplume-progress-update-thread-may-sept-2018/361)*
*Importance Score: 74.5 | Core Participants: yeastplume*

### Post by @Yeastplume ⭐ (2018-05-04)
*Post #1*

Update for Friday May 4th, 2018

Going to open a new thread for this one, as technically I’m now working using proceeds from the second funding campaign, covering May to September 2018!

Going to keep it fairly short this week, as I’m currently in the middle of a large refactor. A lot of this week has spent thinking about the wallet, which I’m glad to say is starting to get it the attention it needs. We had a good gitter meeting this week about where it needs to go, [which I’ve logged here](https://github.com/mimblewimble/grin/issues/1028). If you’re at all interested in wallet design I encourage you to have a read through the conversation.

A few steps are needed to get it into a better place for a fuller redesign, with [this refactoring](https://github.com/mimblewimble/grin/pull/1035) being the first. Basically, I’m moving all of the transaction building functionality out of the keychain, in order to restore the keychain to it’s original intent… a thin wrapper for managing keys and performing a few sensitive operations. This ends up being a bit of a rabbit hole due to the project structure and tests and previous assumptions, but hopefully it should be worth it. Once this is done we should have a clearer delineation between wallet transaction building and the keychain, which will make it much easier to think about how to update the design. I hope to have all of this bit done early to mid next week.

Other bits have been a couple of bug fixes, but mostly the introduction of the updated bullet-proof lib to the consensus-breaking branch, as well as providing rust wrappers for batch validation (which we hope to be using eventually for speed improvements.

Also, I’m planning on attending [the first Grin meetup in London](https://www.meetup.com/grinlondon/events/gkhvppyxhbdc/) shortly, and given I need to fly in I can’t promise this will be a regular occurrence! So if you live nearby, I hope you’ll consider attending.

Enjoy the weekend!

---

### Post by @Yeastplume ⭐ (2018-05-11)
*Post #2*

Update Friday May 11th, 2018

It’s all about the wallet for the time being, beginning with a large refactoring

I spent quite some time this week thinking of potential designs for how the keychain, and transaction libraries should look and interact, only to throw it all out as it was most probably adding complexity without solving any particular issue. I tend to think that imposing a design on something like this up-front usually leads to unnecessary complexity as you try to impose tiers and add generic this and that or the other to anticipate future needs that you can’t quite put your finger on. I generally prefer to code to what you know now, and then refactor, refactor, refactor, letting the design take shape as more needs come to light.

So that being said, although we still don’t have a particular design for how the final keychain/transaction lib and wallet should look and interact, there are plenty of aspects in the current implementation that obviously need refactoring and cleaning up. To start bashing it into shape, I’m tacking the larger and more obvious issues, and in doing so getting a much better sense of what the final structure should be.

In the short term, I think the goals are:

* Forge a clear delineation between the keychain, transaction building, and the wallet implementation. The Keychain and transaction building can have an awareness of one another, while neither should know a thing about the details of the wallet implementation.
* Ensure all of the functionality is in the correct tier

This week’s [large refactoring PR](https://github.com/mimblewimble/grin/pull/1035) was the first step, and moved transaction building, aggsig functionality, and proof building out from the Keychain and core modules and put them into a new [libwallet](https://github.com/mimblewimble/grin/tree/master/wallet/src/libwallet) mod within the current wallet code. This leaves the keychain performing only key management functions (with one or two exceptions that can be cleaned up later), and creates a new module which should hopefully form the basis of the transaction building tier.

The next step, [which I’m currently working on here](https://github.com/mimblewimble/grin/pull/1061), is to split up the code for the aggsig transaction workflow into a separate reusable library within the libwallet module, as opposed to embedded in the middle of wallet-implementation-specific code concerned with http connections and the like. The lib functions should simply take information from the caller, use it to build and return partial transactions, and then leave it up to the caller to decide what to do with them (e.g. forward to another wallet, output for inclusion in an email, etc). I’ve managed to split the functionality out successfully, but I think the lib functions still have too much awareness of the internal wallet structure, which I think needs to be addressed next.

As the wallet is cleaned up and solidified, better approaches to handling sensitive information should become clearer. What’s more, they should be easier to implement due to everything being in a more logical place.

That’s all that’s in my head at the moment, thanks for watching and have a good weekend!

---

### Post by @Yeastplume ⭐ (2018-05-18)
*Post #3*

Update Friday, May 18th, 2018

Theme is the same as last week, plenty of work continuing on the wallet refactoring and library creation:

* <https://github.com/mimblewimble/grin/pull/1061> was integrated earlier in the week, and went a long way towards putting all of the bits of functionality that comprise a wallet into the right places. There’s a full description in the issue of what changed, so I won’t repeat it here.

* With that in place, I’ve moved on to [part 3](https://github.com/mimblewimble/grin/pull/1072), and spending time really refining what the transaction workflow should look like. This phase is about chiselling away at the API to try to get it into the most flexible and re-usable state possible, and I’m starting to like the results… the form it’s moving toward should make it far easier to support all of the transaction workflows we’ve talked about (including carrier pigeon,) as well as support future models such as multi-party, multi-sig, etc. Again, there’s a lot more detail in the issue, so I invite you to look there if you want to know further details.

Once thing I’ve done is started using the term transaction ‘Slate’ to describe something that holds all of the semi-public data needed to complete a transaction. The idea here is the slate is passed around between all parties involved, each one filling in their information until there’s enough info to finalise the transaction. How it’s passed around doesn’t matter (http or avian carrier), just that everyone adds their inputs, outputs and information correctly during the appropriate round. Once all parties have completed their rounds, anyone can finalise the transaction and post it. The slate doesn’t care who the sender or receiver is, or indeed how many parties are involved. In any case, I think using a term other than ‘Transaction’ or ‘PartialTransaction’ to describe this chunk of data makes for less ambiguity and will hopefully make future discussions clearer.

Still a lot of work to go, but it’s starting to go faster and easier as the pieces move into place and the remaining tasks become more obvious. Once I’m happy with how the aggsig workflow looks, I’ll move on to tightening up the other pieces and hopefully we’ll have a decent wallet library foundation to build on.

One last thing, if you’re in the London area and haven’t signed up for this yet, what’s wrong with you?

[Meetup](https://www.meetup.com/grinlondon/events/gkhvppyxhbdc/)

### [Grin & MimbleWimble Meetup in London with Yeastplume](https://www.meetup.com/grinlondon/events/gkhvppyxhbdc/)

Tue, May 22, 2018, 6:30 PM: The first get together to discuss MimbleWimble & Grin in London that we're aware of.We're happy to announce that Michael Cordner, a.k.a. Yeastplume, one of the lead develop

Look forward to seeing everyone there next week!

---

### Post by @Yeastplume ⭐ (2018-05-25)
*Post #4*

Update for Friday May 25th, 2018

More screw-tightening on the wallet for most of this week, and with the [lastest PR](https://github.com/mimblewimble/grin/pull/1087) I think I can say that the wallet refactoring is mostly done for now, or at least to the point where I think other bits of work can now start. The transaction workflow I think is is as optimised as it can get for the time being, and any changes or refinements will most likely be smaller changes coming out of the next phases of wallet work.

There’s a been a bit of chat on Gitter at what to do next, which will probably include moving the wallet storage from a flat file into lmdb, possibly some related work on the keychain, and creation of all the other bits up to and including a much more usable wallet. I still don’t think we have quite a complete picture of what should eventually be released with Grin, so I’ve started to put some thought into it and got down at least one UML diagram to start the discussion. I’ve just pasted what I have so far into the Gitter dev channel for the time being for discussion, and I’ll put it somewhere more permanent once we have some agreement on what we’re doing. In the meantime, just take a look on the [dev channel](https://gitter.im/grin_community/dev) for the ongoing discussions.

And while you’re there, I’d also encourage you to look though the recent discussions on dandelion and aggregation… I’m not directly involved it at the moment but [@antioch](/u/antioch) and [@quentinlesceller](/u/quentinlesceller) are, and it’s interesting stuff… I have no doubt they’ll arrive at the best solution.

The meet in London was a success, I think… I enjoyed myself anyhow and it was great meeting so many people interested in Grin! I look forward to getting out to a few more meetups and conferences eventually, (as and when it makes sense, of course, given the amount of work there’s still left to do!) Thanks to everyone who came out!

---

### Post by @Yeastplume ⭐ (2018-06-01)
*Post #5*

Update for Friday, June 1st 2018

At the risk of getting boring here, it was mostly _even more_ wallet refactoring this week, via <https://github.com/mimblewimble/grin/pull/1113> and <https://github.com/mimblewimble/grin/pull/1096>… In short:

* the wallet storage was abstracted away, meaning that it should be very easy now to drop in another backend (as opposed to a simple file as exists now). [@igno.peverell](/u/igno.peverell) is working away now on LMDB storage for consensus breaking branch, and the plan is to add an LMDB based wallet, which should hopefully operate more quickly and allow for more flexibility.
* There are 2 wallet libraries now, `libtx` which handles transaction building, and `libwallet`, which calls into `libtx` and adds functionality like selecting, querying and updating wallet outputs and keys (with no pre-knowledge of the underyling storage format).
* Most of the common/reusable functionality has been factored into `libwallet`, leaving the main wallet implementation (called `FileWallet` now) with manageable amount of code.
* The other periphery bits around the wallet, running a server, invocation etc have been reduced to a near trivial amount of code.
* Error handling reworked a bit to ensure we’re capturing errors from all the right places

Now, the current state of things isn’t perfect… we may still want to fiddle around with the expected ownership of trait objects and at some point factor our traits from the Keychain, but I think it’s in a state now where we can start attempting to build a few more things on top of it, and continue to refine and refactor based on progress there.

As I mentioned, Igno is planning on LMDBifying the backend storage. I think for my next trick, I’m going to try to start building out the skeleton of the structure planned here, and get some wallet API calls working end-to-end for both the HTTP and command line cases:

It’s been a lot of internal refactoring and foundation work on the wallet thus far, but hopefully soon we’ll start getting to the user-visible enhancements and improvements.

Have a good weekend all!

---

### Post by @Yeastplume ⭐ (2018-06-10)
*Post #6*

Update Sunday, June 10th, 2018

Bit late on this one as I was too deep into nasty web UI-type code on Friday, but here’s a quick update on last week and plans for this week.

As mentioned last week, I’ve [factored out communication](https://github.com/mimblewimble/grin/pull/1133) from the wallet code as well as created separate listeners for what I’m calling the “owner” and “foreign” api interfaces, which are intended to provide rest apis for the wallet owner and external senders respectively. [@igno.peverell](/u/igno.peverell) has jumped into the wallet fray by [factoring out the Keychain into a trait](https://github.com/mimblewimble/grin/pull/1146) and is now working on an [LMDB version of the wallet backend](https://github.com/mimblewimble/grin/pull/1151), which should hopefully be faster and more flexible than the current file-based implementation.

Up this week, first I’m going to spend a bit of time integrating Tromp’s latest ‘meaner’ miner into grin-miner, to try and get the core Grin mining experience up to the speed of the GrinGoldMiner. Then, continuing work on a bare-bones web wallet that uses the wallet owner interface. There’s a bit of work already done but it’s nowhere near ready to show. I’ll be creating a new repository soon to keep it all in, but shan’t be providing instructions to build and run it until it’s in a ready-ish state. So there.

And just as an aside, if there are any web frontend experts looking to get involved in Grin’s development (I’m using Angular for the time being), now would be a great time to jump in!

Will provide a lengthier update and hopefully a thing or two to demonstrate at the end of the week!

---

### Post by @Yeastplume ⭐ (2018-06-15)
*Post #9*

Update Friday June 5th, 2018

So without further ado, some more tangible and user-friendly results from all of this wallet work:

[ wallet-1.png1385×562 42.5 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/53c8dbb0bbf17c75bf6b16747e536682367d2003.png "wallet-1.png")

That’s a rough fist pass at Grin’s web-wallet, which can be viewed, cloned, downloaded, played with and PRed here: <https://github.com/mimblewimble/grin-web-wallet>. It’s done using Angular 6 and Bootstrap, and I’m intentionally trying to keep the number of dependencies to just that. I’m a fan of using Angular for any client side browser development, and the really nice thing about recent versions is that it contains decent tools to compile a massive project full of typescript files to a few minimised and uglified .js files that can easily be embedded and served from within Grin itself, if so desired.

For now, no secret information is passed to the client. All secrets remain on the ‘server’ (which is your local machine running your wallet,) and processing happens there. The architecture should stay this way for the forseeable future, but I may make a case for finding a solution for sending passwords back and forth as this will give us the ability to manage multiple wallets through the single application, which I think would be a nice usability feature and make it feel like other wallets.

Server side, I’ve had quite a few PRs this week to support web-wallet functions, the most major being [the addition of a wallet detail file](https://github.com/mimblewimble/grin/pull/1167) which contains information such as the last assigned key and the height at which the wallet was updated. Previously this was being inferred by the wallet output contents, however that turned out to be very irksome for a client interface where you’d like to keep a consistent view of the data, and want to be able to retrieve your wallet without necessarily wanting to update all of your outputs against a server every time.

[ wallet-2.png1363×669 116 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/aa978a2b84aca0c0eddcf43264a9487c6074c099.png "wallet-2.png")

As it stands, the web wallet does more or less exactly what the command line wallet does, and a few recent fixes and improvements I’ve done automatically apply to both, as they’re both using the exact same interface and sharing most of their code (one of the many reasons behind the past few weeks of wallet library refactoring and creation). It’s still very rough and doesn’t necessarily do all of the error checking and user-friendly hand-holding that it should eventually do, but it works and can even be used to send at the moment:

[ wallet-3.png1384×792 62.3 KB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/6424230599347ae94b72f6af77b8a2e530e24a49.png "wallet-3.png")

So, now this is in place, all I can think of is the massive amount of work still remaining to make the wallet as robust and usable as possible… Off the top of my head, the order of events should be:

In the immediate future:

* Finishing the LMDB backend for the wallet, which should make operations faster and more robust than the current simple file version. [@igno.peverell](/u/igno.peverell) is [working away on that](https://github.com/mimblewimble/grin/pull/1151)
* Replacing the web-server code… Grin is currently using Iron to serve files for both the wallet and the API, which is basically abandonware at this point. [@hashmap](/u/hashmap) is looking at replacing this with Hyper+an http routing solution… I hope to be serving up the wallet as well when grin is run with defaults. (localhost only for now)
* Adding a transaction log, which will be completely supplemental to the wallet data but give the user the option to record what has been sent and received (like a traditional wallet). I think this is really necessary to make the wallet feel familiar and more usable.
* Figure out how the compiled application is going to be served.
* Continued development on and improvements to the web wallet app based on all of the above.
* Wallet restoration based on the [committed elements version of bulletproofs](https://github.com/ElementsProject/secp256k1-zkp/pull/23)

And importantly:

* Defining the wallet security model and implementing it. A very large topic in and of itself. We’ve had some thoughts on this and will most likely be addressing this after T3 is launched and underway.

And longer term adding features that have been talked about but not really addressed, multi-party, multi-sig, vaults and all of those good things we think we can build on top of MW/Grin.

And all of this is on top of a load of other consensus-breaking work planned before T3, so a lovely fire-hose of work for the foreseeable future.

By the way, to try the web-wallet (recommended for technical-types only ATM):

* Run grin node as usual
* Run `grin wallet owner_api` in whatever directory you want the web wallet to be acting upon.
* [Follow the build and run instructions for the web application here](https://github.com/mimblewimble/grin-web-wallet). You’ll need npm installed, but other than that the build process should get all of the dependencies.
* After running `ng serve` you should be able to get to the app in a browser at `http://127.0.0.1:13420`

I’ll put more detailed instructions up when it’s further along and we’ve figured out how it’ll be packaged with Grin.

Have a good weekend all!

---

### Post by @Yeastplume ⭐ (2018-06-29)
*Post #11*

Update Friday 29th June, 2018

Testnet3 is looking closer than expected, with only a few consensus-breaking items outstanding (and of course plenty of developer testing before we release it into the wild). Most of the work this week was on various pre-T3 items, in no particular order:

* <https://github.com/mimblewimble/grin/pull/1208> Update to error handling, particularly in the chain module… we’re using a particular error strategy within the wallet crate which should work well for error handling needs, however it needs to be implemented throughout the rest of the code. This is a start anyhow.

* Testing the t3 wallet and transaction code, and a few fixes based on that: <https://github.com/mimblewimble/grin/pull/1204>

* Latest (reviewed and hopefully near final) bulletproof code implemented within T3: <https://github.com/mimblewimble/grin/pull/1194>

* Some direct commits to the T3 branch to get it stable and compiling earlier in the week (Merging some earlier messy PRs

As well as some maintenance on our [issues list](https://github.com/mimblewimble/grin/issues) which I think had gotten a bit flabby. There were quite a few out-of-date or otherwise resolved issues in there, but as of now, all of the issues in there are relevant and current (as far as I can tell)

I’d say at some point mid-next week or so we’ll be able to start developer testing on T3 to ensure it’s stable enough for general consumption. More to come on that, probably in our Dev meeting on Tuesday evening.

Have a good weekend, and remember to use sunscreen, kids!

---



## Currency Symbol [ ɠ / ꞡ / ǥ / other ] #BS
*Date: 2018-06-20 | [Forum Link](https://forum.grin.mw/t/currency-symbol-other-bs/484)*
*Importance Score: 79.6 | Core Participants: tromp, jaspervdm, lehnberg*

### Post by @0xb100d (2018-06-20)
*Post #1*

₲ang des gobelins,

At some point it will probably be useful to have a standard symbol to represent grin, for wallets and such to have some consistency. The symbol for the Paraguayan currency, the guaraní, came up early on, ₲, but being already another currency, and also upper-case when so far people have been fond of calling it grin with a minuscule G, it did not seem ideal to me. Maybe neither of those things matter, as the guarani symbol is quite handsome. Alas, the sun rains down upon naked bicycles.

I [spent some time looking](https://en.wikipedia.org/wiki/G) to see if there were some stylized lower-case G symbols out there that might do the duty and, lo, there were a few. I encourage anyone who cares about this at all to peruse wikipedia and/or other sources to find interesting alternative symbols we might use. My eyes were drawn to three in particular.

1. ɠ aka [g-wth-hook](https://en.wikipedia.org/wiki/%C6%93)
2. ꞡ aka [g-barre](https://fr.wikipedia.org/wiki/%EA%9E%A0)
3. ǥ aka [g-with-stroke](https://en.wikipedia.org/wiki/G_with_stroke)

Not all of these are created equal however.

1. ɠ - common character and shows up in many/most font sets. Renders on most devices. That hook is a little bit harry-potter-esque.

2. ꞡ - uncommon, does not appear in most font sets, and does not render on many devices. Interestingly however, it does not have an English wikipedia page… only a French one… Elvis strikes again?

3. ǥ - common character, shows up in many/most font sets. Renders on most devices. As Igno said, however, the symbol on many devices looks like a lower-case g with a bit of dust on your screen… not ideal, but also not a unique lssue, as the other symbols (even the guarani currency symbol) look hideous on many devices as well.

I think that aesthetic quality is not so much as important as universality… as long as it is not unintelligible it can be ugly as hell so long as it can be consistently used and rendered clearly across the world. Heck having it be a G in any form at all is not really important… but convenient for human relatability. Heck we could get funky with alchemical/astrological symbols… ︎ aquasius… looks like a mw to me… 🜓 cinebar… those look like cross througgh g’s to me… the shed is now two stories tall.

What’s nice about 2&3 (and the guarani as well) is the line across the letter can represent the cut-through process that happens in mimblewimble txs. A stroke of luck for us in the bikeshed biz.

4. Alternatively we could just call it XGR or XGN (or XD since it looks like a laughing grinning emoticon), but that isn’t nearly as fun.

I created [a poll on twitter](https://twitter.com/grinMW/status/1008621448573923333) to test the water, but it only contains these three options.

[twitter.com](https://twitter.com/grinMW/status/1008621448573923333)

#### [ ()](https://twitter.com/grinMW/status/1008621448573923333)

[](https://twitter.com/grinMW/status/1008621448573923333)

Looking forward to running future polls with more options if anyone discovers something very good. Hopefully not too many polls.

With the 3rd option winning out so far with 44% of 50 votes (I have no idea who is voting and whether their opinion is valuable, so I encourage forum users to partake) I also did some rough up of a design that takes the form of the G-strike symbol. These you can see on the logo discussion post here: [Grin Logos for Community Consideration - #52 by 0xb100d](https://forum.grin.mw/t/grin-logos-for-community-consideration/155/52)

A sample from that post, which shows our third option from the poll, in the courier font, with a few stylistic freedoms:

[ grin%20symbol%202%20hooked%20serif%2031080×1080 1.14 MB ](https://canada1.discourse-cdn.com/flex036/uploads/grin/original/1X/c17614b0c765b59cb9c3716f69d8217aa574ffa6.jpg "grin%20symbol%202%20hooked%20serif%203")

These are just ideas and inspirations, I’m sure there are many other diverse options to choose from I have not considered and look forward to hearing about. I am not particularly biased toward any of the symbols, but I hope at least in some part my legwork can make the decision happen more easily and with minimal additional BS (bike shedding).

Yours
0xb100d

---

### Post by @lehnberg ⭐ (2018-11-12)
*Post #23*

Not sure if I’ve written it here already, but my vote for sure goes on this Japanese character: ツ

45.642 ツ

---

### Post by @lehnberg ⭐ (2018-11-13)
*Post #25*

[@monkyyy](/u/monkyyy)

1. This is the same character used in the [ascii emoji shrug](https://emojipedia.org/shrug/): `¯\_(ツ)_/¯`
Could you point to any previous cases where the use of this emoji has caused outrage?

2. it _might_ cause _confusion_ amongst Japanese users. It’s a very real possibility. I struggle to see how it would mock them or be offensive in any way. It’s a [hiragana](https://en.wikipedia.org/wiki/Hiragana) character. Can you explain what you mean?

3. Because it’s hiragana, this has nothing to do with the Chinese [hanzi characters](https://en.wikipedia.org/wiki/Chinese_characters). How would the use of a Japanese character as a currency symbol mock the Chinese people?

---

### Post by @lehnberg ⭐ (2019-01-04)
*Post #37*

# [VOTE on Grin's currency symbol](https://forum.grin.mw/t/vote-on-grins-currency-symbol/1726)

---

### Post by @lehnberg ⭐ (2019-01-20)
*Post #38*

[last meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190117-meeting-governance.md#102-currency-symbol):

> #### 10.2 Currency symbol
>
> Meeting adopted `ツ` , aka “Tsu” as the official currency symbol of the project.

---

### Post by @lehnberg ⭐ (2019-01-20)
*Post #40*

Hi [@0xb100d](/u/0xb100d), the [poll](https://forum.grin.mw/t/vote-on-grins-currency-symbol/1726) was non-binding. As per the poll instructions:

> The vote results will guide a discussion as part of the Jan 17 governance meeting, where a decision will hopefully also be made.

As per the [meeting notes](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190117-meeting-governance.md#102-currency-symbol), `ツ` was the symbol that was adopted. You are welcome to independently verify this, the full chat transcript begins [here](https://gitter.im/grin_community/Lobby?at=5c4098cc7a0f4d5b19c3c1b4).

As for your question:

> Why pick the second from the poll if most everyone was ambivalent between the two?

It’s hard to say why exactly, but this was what happened at the meeting. I guess one symbol had to be picked in the end, and since the vote was non-binding, and several proposals were neck in neck, it was not obvious that the first from the poll would be the final decision.

If you feel this is wrong, you can petition for this decision to be reconsidered. A first step might be to make an argument for your case, and then ask for a point to be added to the agenda of the next governance meeting and see if you gather support for your proposal. Or you can refuse to use the symbol in protest. Or choose your own symbol that you think is the most appropriate and see if it gets adopted. This, and more, is all within your right as a member of the community.

---

### Post by @tromp ⭐ (2019-10-18)
*Post #76*

Kurt:

> Nobody knows how to pronounce ツ

It’s pronounced “grin”

---

### Post by @lehnberg ⭐ (2019-10-18)
*Post #84*

shush:

> I reviewed the chat logs and couldn’t find the part where Tsu was the selected choice. Could you point out where that discussion took place and ended more specifically?

<https://gitter.im/grin_community/Lobby?at=5c40ae5595e17b4525683895>

---


