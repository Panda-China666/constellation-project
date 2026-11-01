Course T1：Advanced Mathematical Foundations of Machine Learning
14 周，研究生高级数学与学习理论。
周次	研究内容
1–2	测度论概率、条件期望、集中不等式、随机过程
3–4	高维概率、随机矩阵理论、谱分析、自由概率基础
5–6	凸分析、非凸优化、变分分析、随机优化与隐式正则化
7–8	信息论、PAC-Bayes、算法稳定性、泛化界、信息瓶颈
9–10	贝叶斯推断、变分推断、统计物理、自由能与 Gibbs 分布
11–12	最优传输、Wasserstein 几何、连续性方程、梯度流
13–14	随机微分方程、Fokker–Planck 方程、随机控制与扩散过程

数学教学不能停留在介绍定义。学生需要能够证明关键结论，识别定理假设，在简化模型上构造反例，并通过数值实验检验渐近理论的适用范围。
Course T2：Frontiers in Deep Learning Theory
这门课是你所指出的理论缺口，我认为必须重点建设。
周次	核心研究专题	主要深度要求
1–2	Singular Learning Theory	代数几何、奇异模型、RLCT、Bayesian Free Energy、局部学习系数
3–4	Neural Tangent Kernel	NNGP、无限宽极限、NTK 动力学、Lazy Training
5–6	Mean-Field & Feature Learning	Mean-field PDE、Wasserstein Gradient Flow、Tensor Programs、μP、Rich Regime
7–8	Geometric Deep Learning	Lie 群与表示、等变性、流形、纤维丛、Gauge Equivariance、GNN 表达能力
9–10	Representation Geometry	表征流形、对齐与各向异性、谱结构、拓扑、特征塌缩和表征可辨识性
11–12	Deep Learning Dynamics	SGD 的随机动力系统、Hessian 谱、平坦性、隐式偏置、Grokking、Scaling Laws
13–14	Open Problems in Learning Theory	模型复杂度、特征涌现、机制可解释性、泛化与模型规模之间尚未解决的问题

这一门课需要进入具体数学对象，而不是泛泛讨论“神经网络为什么有效”。

例如：

1. Singular Learning Theory

在适当的解析性等假设下，研究贝叶斯自由能的渐近展开：
\[
F_n=nS+\lambda\log n-(m-1)\log\log n+O_p(1)
\]

其中 \(\lambda\) 是 Real Log Canonical Threshold（RLCT），体现奇异模型与经典正则统计模型的区别。

进一步研究 LLC 的估计、神经网络退化结构，以及这些复杂度概念能否解释训练中的相变与表征变化。2025 年 AISTATS 已有针对 LLC 的可扩展估计研究，可以成为理论与实验结合的优秀切入点。
Monash University+1


2. NTK 与真正的 Feature Learning

从
\[
K_\theta(x,x')
=
\nabla_\theta f_\theta(x)^\top
\nabla_\theta f_\theta(x')
\]

出发，研究固定核极限、有限宽修正、训练轨迹与特征学习之间的关系。

这里最值得研究的不是单纯证明 NTK 收敛，而是解释：为什么很多实际深度学习的成功恰恰发生在固定核近似不足以描述的区域？

Greg Yang 和 Edward Hu 的 Tensor Programs IV 是这一部分的重要文献。
NeurIPS Papers+1


3. 深度几何学习

不仅要教 GNN、SE(3) 等变网络，更要从群作用、表示论和流形上的局部坐标系统出发，研究网络如何编码对称性及物理归纳偏置。

Bronstein 等人的 Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges 适合作为理论主干。
DOI

理论课程的博士级考核
我建议设置三类正式研究作业，而不是通常的计算题：
- Proof Problem Set：证明一个关键命题，或构造能够推翻过强假设的反例。
- Theory-to-Empirics Study：例如比较 NTK、μP 与不同宽度网络的特征演化，或者在可控模型上估计 LLC。
- Open Problem Proposal：选择一项前沿理论工作，指出其定理适用边界，提出一个可证明或可证伪的新问题。
推荐核心阅读：
Neural Tangent Kernel — NeurIPS 2018

Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks — ICML 2021

The Local Learning Coefficient — AISTATS 2025

Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges

Stochastic Interpolants: A Unifying Framework for Flows and Diffusions — JMLR 2025

我希望理论部分最终达到的程度是：学生不仅能阅读新的架构论文，还能够提出一个关于该架构训练动力学、表达能力或泛化性质的数学问题，并有能力尝试证明它。
三、第二主轴：生成模型、LLM、多模态与世界模型
Track II — Advanced Generative Modeling & World Models

这是整个项目中研究跨度最大的部分，我建议拆成三门完整课程，而不是将 LLM 和世界模型压缩成几周选讲。









G1. Foundations of Deep Generative Models

以 MIT 6.S978 为基础，研究概率生成建模的各类范式及其统一数学结构。











G2. Large Language Models: Architectures & Generative Learning

从概率序列建模、架构、训练目标到 Scaling Laws，深入模型的设计与训练。











G3. Multimodal Representation & World Models

将视频、空间、动作、物理动力学与预测式表征统一起来。



Course G1：Foundations of Deep Generative Models
这一门保留你提供的 MIT 课程的学术传统，同时进一步加强概率论、微分方程及模型之间的理论联系。
周次	内容
1	Image Priors、Patch-based Modeling、Deep Image Prior
2	VAE、ELBO、Variational Inference、Posterior Collapse
3	Normalizing Flows、Change of Variables、Continuous Normalizing Flows
4	Autoregressive Models、PixelCNN、Latent Tokenization
5	GAN、Minimax Optimization、Integral Probability Metrics
6	Energy-Based Models、Score Matching、Langevin Dynamics
7	Diffusion Models：DDPM、Score SDE、Probability Flow ODE
8	Noise Schedule、Guidance、Diffusion Sampling 与蒸馏
9	Discrete Diffusion、Continuous-Time Markov Chains
10	Flow Matching、Rectified Flow、Stochastic Interpolants
11	Consistency Models、Few-step Generation、Generative Distillation
12	统一视角：Optimal Transport、Schrödinger Bridge 与随机控制
13	Generative Modeling for Geometry、Physics、Biology
14	研究论文答辩：生成建模的理论或算法创新

关键提升： 第 10–12 周必须进入向量场、连续性方程、SDE/ODE、路径测度以及随机最优控制。不能只训练一个 Diffusion Model 就结束。

可以利用 2025 年 JMLR 的 Stochastic Interpolants，将 Flow 与 Diffusion 统一到同一数学框架讨论。
Journal of Machine Learning Research


课程的最终研究任务可以是：在统一计算预算下，对不同生成轨迹、向量场参数化及数值积分器进行比较，提出一种改进，并通过理论分析或充分实验说明改进机制。
Course G2：Large Language Models — Generative Learning and Architecture
这是一门与 Stanford CS336 同级起点、但更强调模型研究与架构创新的课程。
周次	研究内容
1–2	Sequence Modeling、熵率、Tokenization、离散与连续表征
3–4	Transformer、Attention 变体、位置表示、长上下文机制
5–6	MoE、稀疏计算、State Space Models、Hybrid Architectures
7–8	预训练目标、数据分布、Scaling Laws、Compute-optimal Training
9–10	训练稳定性、优化器、参数化、梯度尺度、跨规模超参数迁移
11–12	Beyond Next-token Prediction：多 Token 预测、离散扩散语言模型、并行生成
13	Multimodal Language Modeling：离散与连续 Token 的统一生成
14	Architecture Research Defense：新模型架构的研究答辩

这里必须教会学生质疑架构的基本假设：
- Transformer 的哪些性能来自 Attention，哪些来自深度、残差和训练规模？
- 为什么 MoE 的稀疏激活可以改善部分计算效率，却增加训练与通信复杂性？
- 是否必须使用自回归逐 Token 生成？并行生成与非自回归方法的限制是什么？
- 训练计算与推理计算之间，是否存在更好的预算分配方式？
研究材料不止 Transformer 原论文。例如 DeepSeek-V3 关于 MoE、MLA、多 Token Prediction 和 FP8 训练的技术报告，就适合作为架构、优化和系统联合讨论的案例。
GitHub


毕业级项目： 在可控规模下独立提出和实现架构变体，必须包含固定 FLOPs/Token 预算、参数规模、数据预算下的比较，以及质量—吞吐—显存的 Pareto 分析。
Course G3：Multimodal Representation Learning & World Models
我建议把它视为独立的前沿核心课程，而不只是生成模型的应用专题。
周次	研究内容
1–2	多模态表征学习：Contrastive、Masked Modeling、Joint Embedding、JEPA
3–4	视觉与空间表示：3D/4D Geometry、NeRF、3D Gaussian Splatting、场景表征
5–6	Video Generative Models：时空 Attention、Video Diffusion、Flow-based Video Generation
7–8	Latent Dynamics、State Space World Models、Action-conditioned Prediction
9–10	Physical World Models：物理一致性、对象持久性、因果干预与反事实推演
11–12	World Models for Planning：Latent Planning、MPC、Uncertainty-aware Prediction
13	World-Action Models、Vision-Language-Action、世界模型与机器人策略的联合学习
14	World Model Research Proposal 与实验答辩

重要的是，我们需要明确区分：
\[
\text{Video Generation}
\neq
\text{Predictive World Representation}
\neq
\text{Action-Conditioned World Model}
\]

能够生成视觉上合理的视频，并不意味着模型理解了动作干预、物理规律或因果结构。

因此我们不能只看生成画质，也要研究状态一致性、可控性、长期预测误差及对下游决策的实际价值。

研究基础可以从 Genie、Diffusion Policy、V-JEPA 2 发展到 2026 年的 World-Action Models。例如 Stanford 在 2026 年 10 月公开的 OpenWAM，尝试在可组合框架中联合研究视频预测与机器人控制。
Research - AI at Meta+2


推荐阅读：
MIT 6.S978 — Deep Generative Models 完整课表

Stanford CS336 — Language Modeling from Scratch (2026)

Flow Matching for Generative Modeling

V-JEPA 2 — Video Understanding, Prediction and Planning

OpenWAM — Composable World-Action Models (2026)


四、第三主轴：高性能人工智能计算与系统研究
Track III — High-Performance AI Computing & Systems Research

你提出要把这部分向前沿拓展，我非常赞同。

我认为它应该具有 计算机体系结构、并行算法、编译器、分布式系统与机器学习算法协同设计 的深度，而不是简单的“PyTorch 分布式训练教程”。

建议分为两门 14 周课程。
Course S1：GPU Computing, Compilers & Efficient Kernels
周次	研究专题	必须掌握的研究方法
1–2	GPU Microarchitecture、Memory Hierarchy、Roofline Model	计算 FLOPs、访存量与带宽下界
3–4	CUDA、Triton、CuTe、Tile Programming	设计和分析矩阵乘法、归约与融合 Kernel
5–6	FlashAttention 系列、Online Softmax	IO Complexity、Tiling、异步计算
7–8	GPU 编译器、MLIR、XLA、Kernel Fusion	IR 变换、自动调优与代码生成
9–10	Mixed Precision、FP8、FP4、数值稳定性	量化误差、累积误差与精度—性能分析
11–12	Sparse Computation、MoE Kernels、Irregular Workloads	负载均衡、稀疏访存与调度
13–14	Hardware–Algorithm Co-design	提出新的 Kernel 或调度优化并答辩

在这里，FlashAttention 是一个非常优秀的研究案例。

它不只是一种更快的 Attention 实现，而体现了如何根据硬件的不同瓶颈重新设计算法。到 2026 年，FlashAttention-4 已开始围绕 Blackwell GPU 的非对称硬件性能与异步流水线重新进行算法—Kernel 协同设计。
arXiv


研究生必须能够说明：某一种优化为什么在特定硬件、序列长度和数据精度下有效，又为什么在其他配置下失效。
Course S2：Distributed Foundation Model Training & Inference Systems
周次	研究专题
1–2	Distributed Training：FSDP、ZeRO、Tensor/Pipeline/Context Parallelism
3–4	Expert Parallelism、MoE All-to-All、Communication-Computation Overlap
5–6	分布式优化器、Activation Checkpointing、异步训练与数值一致性
7–8	Scaling Infrastructure：训练拓扑、Checkpoint、故障恢复、数据流水线
9–10	Inference Architecture：PagedAttention、KV Cache、Continuous Batching、Speculative Decoding
11–12	Disaggregated Prefill/Decode、异构部署、服务调度、尾延迟优化
13	Training–Inference Co-design：联合考虑训练目标、模型架构和推理成本
14	Systems Research Defense：完整系统研究实验与答辩

这门课不仅研究如何训练大模型，还要研究：
\[
\min_{\text{architecture, schedule, precision}}
\text{Cost}
\]

在模型质量、延迟、吞吐、内存、能耗及计算预算约束下寻找最优系统设计。

尤其值得深入的方向有三个。

A. 分布式训练与通信下界

要求学生分析并行策略的通信量、计算量、内存占用、流水线气泡以及网络拓扑限制，而不是只跑通多机训练。PyTorch 的 TorchTitan 已提供组合 FSDP、TP、PP、CP 和 EP 的研究实现参考。
GitHub


B. 推理系统设计

以 PagedAttention、SGLang 和 DistServe 为基础，研究 KV Cache 管理、前缀复用、解码调度和 Prefill/Decode 分离。
DOI+2


C. Training–Inference–Algorithm Co-design

这是我认为更有研究空间的方向。不是先设计完模型再去做性能优化，而是在模型研究阶段，就把训练效率、推理复杂度、显存以及通信代价纳入架构设计。
系统方向的毕业级研究任务
学生选择一种训练或推理瓶颈，提出改进方法，并提供：
1. 理论性能模型与明确的优化假设。
2. 可复现的系统实现与正确性测试。
3. 多模型规模、多 Batch Size、多序列长度下的实验。
4. 与强基线的同硬件、同精度比较。
5. 性能异常的解释，以及改进方法的适用边界。
最重要的是，这应当是一篇具有 MLSys、OSDI、SOSP 或相关系统会议研究标准意识的工作，而不是一个跑通分布式训练的演示项目。 不要求一定胜过所有已有系统，但必须有经过验证的新技术贡献。

推荐阅读：
FlashAttention-4 — Algorithm and Kernel Pipelining Co-Design (2026)

DistServe — OSDI 2024

FlashInfer — Efficient Attention Engine

TorchTitan — 大规模 AI 训练研究参考实现

五、第四主轴：强化学习、最优决策与自我改进
Track IV — Reinforcement Learning, Decision Making & Self-Improvement

强化学习不应该只从 DQN、PPO 讲到 GRPO。

它实际上连接了 随机控制、动态规划、优化理论、博弈论、概率推断、生成式建模和自主学习。

如果我们的目标是博士研究能力，学生必须掌握这些联系，并能够对现有强化学习算法提出新的理论或方法。
Course R1：Advanced Reinforcement Learning & Stochastic Control
周次	研究内容
1–2	MDP、POMDP、Bellman Operator、Occupancy Measures、动态规划的对偶形式
3–4	Stochastic Optimal Control、HJB Equation、Pontryagin Principle、Control as Inference
5–6	Policy Gradient、Natural Policy Gradient、Mirror Descent、Trust Region 方法与收敛分析
7–8	Offline RL、Off-policy Evaluation、Distributional RL、Conservative Learning
9–10	Model-based RL、Latent Dynamics、Dreamer、TD-MPC、模型误差传播
11–12	Exploration、Intrinsic Motivation、Skill Discovery、Hierarchical RL、Meta-RL
13	Robust & Risk-sensitive RL、Multi-agent RL、Mean-field Games
14	强化学习理论或算法创新研究答辩

其中需要重点研究几个问题：

强化学习与随机最优控制是否可以统一？

许多强化学习方法可以从熵正则化决策、概率推断或随机控制的角度重新理解。进一步可以讨论 Flow Matching、扩散生成与最优控制之间的联系。

世界模型什么时候真正改善决策？

模型预测精度更高，并不自动意味着策略回报更高。需要研究模型误差的累积、规划视野、价值偏差和模型不确定性。

探索和经验积累如何形成可以迁移的能力？

重点不是只学更复杂的奖励设计，而是理解探索、技能复用和环境结构之间的关系。
Course R2：Reinforcement Learning for Reasoning & Adaptive Intelligence
这门课程负责与第二主轴的 LLM、世界模型形成联系。
周次	研究内容
1–2	Preference Learning、RLHF、DPO、KL-Regularized Policy Optimization
3–4	Reasoning RL：PPO、GRPO、DAPO、优势估计、序列级奖励
5–6	RL with Verifiable Rewards、Outcome/Process Reward Models、Verifier Learning
7–8	Test-time Scaling、Search、Best-of-N、Tree Search、Adaptive Compute Allocation
9–10	Long-horizon Credit Assignment、稀疏奖励、探索、Agentic RL
11	Self-play、Self-improvement、Synthetic Experience 与数据分布演化
12	Diffusion/Flow Policy Optimization、Reward-conditioned Generation
13	Test-time Training、Online Adaptation、Reward Hacking 与策略退化
14	Independent Research Defense

例如，DeepSeek-R1 的研究表明，可验证结果奖励能够推动模型形成更复杂的推理行为；DAPO 则进一步研究了大规模语言模型强化学习的优化与训练稳定性。
Nature+1


但高级课程不能停留在复现这些算法。

我们需要让学生直接研究：
- 为什么可验证奖励能够改善推理？它能够改善到什么程度？
- 最终答案正确性奖励是否足以训练长链条推理？
- 为什么某些模型的 RL 训练会出现长度膨胀、熵下降或奖励利用问题？
- 如何在训练时计算、推理时计算与验证计算之间实现最优资源分配？
- 自我生成的数据在什么条件下能够形成真实的能力提升，而非简单的分布强化？
在理论方面，2025 年 ICML 的 Scaling Test-Time Compute Without Verification or RL is Suboptimal，以及 ICLR 的推理时计算扩展研究，都适合作为严肃的研讨材料。
Proceedings of Machine Learning Research+1


R2 最终考核应该要求学生提出一个新的训练机制、奖励方法、验证策略或计算分配算法，在同一训练及推理预算下进行严格比较。需要报告 Pass@1、Pass@k、Token/FLOPs 成本、泛化误差、奖励与验证器失效情况，而不只是给出一个 Benchmark 分数。

六、第五主轴：推理与自主智能的计算基础
Track V — Computational Foundations of Reasoning & Autonomous Intelligence

这是我认为最需要从原方案中重建的部分。

原来的 Tool Use、Memory、Multi-Agent、Agent Framework 并非没有价值，但把它们当作前沿研究生课程的主干，确实容易沦为软件工程练习。

我们应该研究的是：

智能系统如何表示问题、积累知识、分配计算资源、进行可验证推理，以及在不确定环境中自主发现有效行动？
Course I1：Foundations of Machine Reasoning and Autonomous Intelligence
周次	研究内容
1–2	Computational Complexity、程序归纳、算法学习、组合泛化
3–4	Neural-Symbolic Reasoning、Program Synthesis、Formal Verification、Proof Search
5–6	Reasoning as Search、Inference-time Computation、Metareasoning
7–8	Learning to Plan：层次规划、Belief-State Planning、长时序依赖
9–10	Memory as Learning：可学习记忆、状态压缩、持续学习、知识更新
11	Active Information Acquisition、Bayesian Experimental Design、主动感知
12	Multi-agent Intelligence：博弈、协调、通信与分散式决策
13	Mechanistic Interpretability、Causal Interventions、Reasoning Faithfulness
14	Fundamental Research Proposal：提出智能推理基础问题并答辩

这里至少有三个真正有研究深度的核心命题。
命题 A：Reasoning 是否等同于计算搜索？

研究语言模型的推理、树搜索、程序执行、形式验证和推理时资源分配之间的关系。

一个重要问题是：什么条件下增加推理计算能够带来可靠的能力提升？什么条件下只会增加计算成本甚至放大错误？


命题 B：Memory 能否成为真正可学习的状态表示？

不只是将历史文本写入向量数据库。

研究模型如何从经验中形成压缩的、可迁移的内部状态；如何在长期交互中保留决策所需信息，并控制旧知识与新知识之间的干扰。


命题 C：我们能否验证模型确实进行了预期推理？

这涉及机械可解释性、因果干预、形式化验证、内部表征与输出推理过程的一致性。

例如 Anthropic 在 2025 年发布的 Circuit Tracing 研究，可以引入为分析模型内部计算过程的一种方法，但也必须研究其解释能力与局限性。
Anthropic



这一主轴的研究标准应该是：发现和解释智能系统的规律，而不只是让某一个 Agent 在某个平台上完成任务。

七、AI for Science、机器人、生物与安全不再单独占一个核心模块
关于你说的第六部分，我的判断是正确的：它更适合成为横向渗透的科研领域。

但我会保留专门的 Frontier Research Seminars（前沿研究研讨），让每个领域成为理论、模型、系统、决策的共同实验场。
研究领域	理论研究连接	模型与系统研究连接
AI for Biology	几何、对称性、概率模型、结构统计	蛋白质生成、分子设计、科学基础模型
Robotics & Embodied AI	控制、POMDP、等变性、因果动力学	VLA、World-Action Models、机器人策略
AI for Mathematics	形式系统、证明搜索、计算复杂性	Theorem Proving、Verifier、推理强化学习
AI for Physics	对称性、守恒律、微分方程、逆问题	Neural Operators、物理世界模型、模拟
AI Safety & Interpretability	鲁棒优化、因果识别、模型复杂度	机制可解释性、可靠推理、模型行为验证

每名学生应当至少选定一个垂直研究领域，但不要求所有人都系统修完全部领域。