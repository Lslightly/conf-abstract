会议名称：ASPLOS 2026 (31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems)
会议链接: https://www.asplos-conference.org/asplos2026/
会议时间：2026年3月22-26日
会议地点：Pittsburgh, PA, USA

## 研究主题类别

### 1. LLM Serving优化 (约30篇论文)

ASPLOS 2026是LLM Serving研究的重要会议，涉及多个关键方向：

| 论文标题 | 核心贡献 |
|---------|---------|
| Towards High-Goodput LLM Serving with Prefill-decode Multiplexing | 提出MuxWise框架，采用GPU内prefill-decode时分复用范式 |
| Bullet: Boosting GPU Utilization for LLM Serving | 动态时空协调提升GPU利用率 |
| QoServe: Breaking the Silos of LLM Inference Serving | QoS感知的LLM推理服务框架(Niyama) |
| Shift Parallelism: Low-Latency, High-Throughput LLM Inference | 动态工作负载的低延迟、高吞吐量推理 |
| XY-Serve: End-to-End Versatile Production Serving | 动态LLM工作负载的端到端生产服务 |
| PAT: Accelerating LLM Decoding via Prefix-Aware Attention | 前缀感知注意力加速LLM解码 |
| ZipServ: Hardware-Aware Lossless Compression | 硬件感知的无损压缩减少内存占用 |
| BlendServe: Resource-Aware Batching | 离线推理的资源感知批处理优化 |
| BAT: Efficient Generative Recommender Serving | 双分注意力的高效生成式推荐服务 |
| MoE-APEX: Adaptive Precision Expert Offloading | 混合专家模型的自适应精度专家卸载 |
| SwiftSpec: Disaggregated Speculative Decoding | 分解式投机解码和融合内核 |
| SpeContext: Speculative Context Sparsity | 长上下文推理的投机上下文稀疏性 |
| SpecProto: Speculative Decoding for Protocol Buffers | 协议缓冲区的投机解码编译器 |
| EARTH: Entropy-Aware Speculative Prefetch | 熵感知的投机预取和结果重用 |
| Taming the Long-Tail: Adaptive Drafter | 长尾推理的高效RL训练 |
| FastTTS: Test-Time Scaling for Edge | 边缘LLM推理的测试时扩展 |

**关键趋势**：
- PagedAttention和KV Cache优化是核心
- Prefill-Decode分离架构成为主流
- 投机解码(Speculative Decoding)广泛应用
- MoE (Mixture-of-Experts) 推理优化兴起

### 2. CXL内存与分解内存系统 (约20篇论文)

| 论文标题 | 核心贡献 |
|---------|---------|
| HybridTier: Adaptive CXL-Memory Tiering | 自适应CXL内存分层系统 |
| vCXLGen: Automated Synthesis of CXL Bridges | CXL桥的自动合成与验证 |
| CXLMC: Model Checking CXL Shared Memory | CXL共享内存的模型检测 |
| A Programming Model for Disaggregated Memory | 分解内存编程模型 |
| Cxlalloc: Safe Memory Allocation | CXL Pod的安全高效内存分配 |
| PIPM: Partial and Incremental Page Migration | 多主机CXL分解共享内存的页迁移 |
| CREST: Contention Resolution for Disaggregated Transactions | 分解事务的争用解决 |
| PACT: Criticality-First Design for Tiered Memory | 分层内存的关键性优先设计 |

**背景知识**：
- CXL (Compute Express Link) 提供低延迟内存语义和硬件级缓存一致性
- CXL 3.0支持多达4096个节点的fabric结构
- 主要挑战：内存延迟、缓存一致性、页迁移开销

### 3. 量子计算 (约15篇论文)

| 论文标题 | 核心贡献 |
|---------|---------|
| PowerMove: Optimizing Compilation for Neutral Atom Quantum | 中性原子量子计算机的Zoned架构编译优化 |
| Reconfigurable Quantum Instruction Set Computers | 可重构量子指令集计算机 |
| QTurbo: Compiler for Analog Quantum Simulation | 模拟量子模拟的鲁棒高效编译器 |
| Reducing T Gates with Unitary Synthesis | 幺正合成减少T门 |
| Borrowing Dirty Qubits in Quantum Programs | 量子程序中的"脏" qubit借用 |
| AlphaSyndrome: QEC Circuit Scheduling | QEC码的 Syndrome测量电路调度 |
| PropHunt: Quantum Syndrome Measurement Optimization | 量子 syndrome测量电路自动优化 |
| iSwitch: In-Situ Encoding for Ion Trap | 离子阱的按需QEC |
| Architecting Scalable Trapped Ion Quantum Computers | 表面码的可扩展离子阱量子计算机 |
| Accelerating Computation in Quantum LDPC Code | 量子LDPC码计算加速 |

### 4. Processing-In-Memory (PIM) (约15篇论文)

| 论文标题 | 核心贡献 |
|---------|---------|
| REPA: Reconfigurable PIM for KV Cache | KV Cache卸载和处理的PIM加速 |
| STARC: Selective Token Access for PIM | PIM系统的选择性token访问 |
| Mugi: Value Level Parallelism | 高效LLM的值级并行性 |
| TPLA: Tensor Parallel Latent Attention | 分解Prefill&Decode推理的张量并行潜在注意力 |
| DARTH-PUM: Hybrid Processing-Using-Memory | 混合PUM架构 |
| PUSHtap: PIM-based In-Memory HTAP | 统一数据存储格式的PIM内存HTAP |
| CoGraf: Fine-Grained PIM for Graph Applications | 细粒度PIM加速图应用 |
| Ouroboros: Wafer-Scale SRAM CIM | 晶圆级SRAM CIM的token粒度流水线 |
| A Cost-Effective Near-Storage Processing Solution | 长上下文LLM离线推理的近存储处理 |

**背景知识**：
- PIM通过在内存内部执行计算减少数据移动
- 主要技术：SRAM CIM、DRAM PIM、近存储处理
- 挑战：带宽限制、精度损失、编程模型

### 5. 3D Gaussian Splatting (约6篇论文)

| 论文标题 | 核心贡献 |
|---------|---------|
| GS-Scale: Large-Scale 3D Gaussian Training | 主机卸载的大规模3DGS训练 |
| Neo: Real-Time On-Device 3DGS | 设备上实时3DGS的复用更新排序加速 |
| CLM: Removing the GPU Memory Barrier | 消除3DGS的GPU内存障碍 |
| Nebula: Infinite-Scale 3DGS in VR | 协作渲染和加速立体光栅化的无限规模3DGS |
| AGS: 3DGS SLAM via CODEC | CODEC辅助帧共视性检测的3DGS SLAM |

**背景知识**：
- 3D Gaussian Splatting (3DGS) 由SIGGRAPH 2023提出，实现实时辐射场渲染
- 核心：使用3D高斯作为原语表示场景
- 关键组件：SfM初始化、优化高斯属性、实时splatting渲染

### 6. 全同态加密 (FHE) (约6篇论文)

| 论文标题 | 核心贡献 |
|---------|---------|
| A Framework for Developing FHE Programs on GPUs | GPU上开发和优化FHE程序的框架 |
| HEPIC: Private Inference with Client Intervention | 客户端干预的私有推理 |
| Falcon: Algorithm-Hardware Co-Design for FHE | FHE的高效算法硬件协同设计 |
| Maverick: Rethinking TFHE Bootstrapping on GPUs | GPU上TFHE bootstrapping的协同设计 |
| Cheddar: FHE Library for GPU | GPU架构的Swift FHE库 |
| CHEHAB RL: Learning to Optimize FHE | 强化学习优化FHE计算 |

**背景知识**：
- FHE允许在加密数据上直接计算，保护隐私
- 主要方案：BFV、BFV、CKKS
- 瓶颈： bootstrapping计算开销大
- Microsoft SEAL是最流行的FHE库

### 7. 硬件设计语言与形式化验证 (约15篇论文)

| 论文标题 | 核心贡献 |
|---------|---------|
| Anvil: Timing-Safe Hardware Description Language | 计时安全的硬件描述语言 |
| Graphiti: Formally Verified Out-of-Order Execution | 数据流电路的序外执行形式化验证 |
| Highly Automated Verification of Security Properties | 未修改系统软件的安全属性验证 |
| SylQ-SV: Scaling Symbolic Execution | 硬件设计的符号执行扩展 |
| LPO: Discovering Missed Peephole Optimizations | LLM发现遗漏的peephole优化 |
| LOOPRAG: Loop Transformation with RAG | 循环变换优化的检索增强LLM |

### 8. 其他重要主题

- **Graph Computing**: TempGraph、Graphiti、CoGraf、Voyager
- **Database Systems**: CREST、Understanding Database Pushdown
- **Serverless**: Lambda-trim、Skyler、WorksetEnclave
- **Network**: Toasty、Hitchhike、Enabling fast networking
- **Security**: DejaVuzz、Signal Breaker、SEVI

## 主题基础和经典论文

### Mixture of Experts (MoE)

**核心Survey论文**：
1. **A Survey on Inference Optimization Techniques for Mixture of Experts Models** (arXiv 2024)
   - 论文：https://arxiv.org/abs/2412.14219
   - 论文：https://huggingface.co/papers/2412.14219
   - 全面综述MoE模型的系统级、架构级和硬件级优化

2. **A Survey on Accelerated Technologies for Mixture-of-Experts Model Training** (Tsinghua Science and Technology 2025)
   - 论文：https://www.sciopen.com/article/10.26599/TST.2025.9010169
   - 重点：MoE训练系统加速技术

3. **Toward Efficient Inference for Mixture of Experts** (NeurIPS 2024)
   - 论文：https://neurips.cc/virtual/2024/poster/93368
   - 技术：动态门控、专家缓冲、专家负载均衡

**关键优化技术**：
- Dynamic Gating：动态门控提升吞吐量6-11倍
- Expert Buffering：缓存热门专家到GPU内存
- Expert Load Balancing：专家负载均衡

### LLM Serving

**核心经典论文**：
1. **vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention** (SOSP 2023)
   - 论文：https://arxiv.org/abs/2309.06140
   - 核心：PagedAttention管理KV Cache
   - 影响：已成为LLM serving的标准基础

2. **Orca: A Distributed Serving System for Transformer-Based Generative AI** (OSDI 2022)
   - 论文：https://arxiv.org/abs/2208.08476
   - 核心：Continuous batching、iteration-level scheduling

3. **FastServe: GPU-aware Scheduling and Prefetching for LLM Serving** (ASPLOS 2024)
   - 论文：https://arxiv.org/abs/2309.17443
   - 核心：GPU感知的调度和预取

4. **SpecInfer: Accelerating Generative LLM Serving with Tree-based Speculative Inference** (SOSP 2023)
   - 论文：https://arxiv.org/abs/2305.09718
   - 核心：基于树的投机推理

5. **SGLang: Efficient Execution of Structured Language Model Programs** (SOSP 2024)
   - 论文：https://arxiv.org/abs/2312.07148
   - GitHub：https://github.com/sgl-project/sglang

**最新Survey/Tutorial**：
1. **LLM Inference Serving: Survey of Recent Advances and Opportunities** (arXiv 2024)
   - 论文：https://arxiv.org/html/2407.12391v1

2. **A Survey of LLM Inference Systems** (arXiv 2025)
   - 论文：https://arxiv.org/html/2506.21901v1

3. **Efficient Inference for Edge Large Language Models: A Survey** (Tsinghua Science and Technology 2025)
   - 论文：https://www.sciopen.com/article/10.26599/TST.2025.9010166
   - 重点：投机解码和模型卸载

4. **A Survey of Speculative Decoding Techniques in LLM Inference** (arXiv 2024)
   - 论文：https://arxiv.org/abs/2411.13157
   - 博客：https://blog.codingconfessions.com/p/a-selective-survey-of-speculative-decoding

5. **Awesome-LLM-Inference** (持续更新的资源列表)
   - GitHub：https://github.com/xlite-dev/Awesome-LLM-Inference

6. **LLM Serving from Scratch: The Systems Behind Fast Inference**
   - 博客：https://briansu.co/articles/optimization/llm-serving

**技术解析**：
- PagedAttention详解：https://insujang.github.io/2024-01-07/llm-inference-continuous-batching-and-pagedattention/
- vAttention (替代PagedAttention)：https://arxiv.org/html/2405.04437v3

### CXL内存与分解内存系统

**核心经典论文**：
1. **Revisiting Distributed Memory in the CXL Era** (SIGOPS 2024)
   - 论文：https://www.sigops.org/2024/revisiting-distributed-memory-in-the-cxl-era/
   - 全面回顾CXL时代的分布式内存

2. **CXL-SHM: Efficient Remote Memory Sharing**
   - 核心：引用计数优化远程内存回收

3. **DirectCXL: Memory Pooling with CXL**
   - 论文：https://panmnesia.com/technology/pub/memory-pooling-with-cxl/
   - 性能：比RDMA快7倍

4. **Pond: CXL-based Memory Pooling for Cloud Platforms**
   - 核心：云平台的内存池化系统

**最新Survey**：
1. **Innovation in Computational Architecture: CXL Memory Disaggregation** (Tsinghua Science and Technology 2025)
   - 论文：https://www.sciopen.com/article/10.26599/TST.2025.9010010
   - 全面综述CXL内存分解技术三代发展

2. **Survey of Disaggregated Memory: Cross-layer Technique Insights** (arXiv 2025)
   - 论文：https://arxiv.org/abs/2503.20275
   - 论文：https://arxiv.org/html/2503.20275v1

3. **Survey of Disaggregated Memory: Cross-Layer Technique Insights for Next-Generation Datacenters**
   - 论文：https://www.researchgate.net/publication/403591187

**CXL资源**：
- CXL Consortium：https://computeexpresslink.org/
- CXL 3.0规范：支持多达4096节点的fabric结构

### 量子计算编译

**核心经典论文**：
1. **Quantum Compilation Process: A Survey** (Euro-Par 2024)
   - 论文：https://dl.acm.org/doi/10.1007/978-3-031-90200-0_9
   - PDF：https://citius.gal/static/bcd68a21f39959133ea914bf142bfe11/978_3-031-90200-0_9_20250619104125176_ae9e8e6c7a.pdf
   - 全面综述量子比特映射和电路优化

2. **Quantum Circuit Synthesis and Compilation Optimization: Overview and Prospects** (arXiv 2024)
   - 论文：https://arxiv.org/html/2407.00736v2
   - 涵盖：量子逻辑电路合成、优化、比特映射

3. **Quantum Compiler Design for Qubit Mapping and Routing** (arXiv 2025)
   - 论文：https://arxiv.org/html/2505.16891v2

4. **Dynamic Quantum Circuit Compilation** (IEEE 2024)
   - 论文：https://www.computer.org/csdl/journal/tc/5555/01/11299583

5. **Quantum circuit compilation with quantum computers** (arXiv 2024)
   - 论文：https://arxiv.org/abs/2408.00077

**QEC (量子纠错) 基础**：
- Surface Code：离子阱量子计算的基础
- Quantum LDPC Code：高效量子纠错码

**相关工作**：
- GEYSER: 量子计算编译框架（中性原子）
  - 论文：https://arxiv.org/abs/2205.06308

### Processing-In-Memory (PIM)

**核心经典论文**：
1. **Survey of Deep Learning Accelerators for Edge and Emerging Computing** (Electronics 2024)
   - 论文：https://www.mdpi.com/2079-9293/electronics-13-04731
   - 综述：边缘处理器的数据流、神经形态和PIM架构

2. **PIM-GPT: Hybrid Process in Memory Accelerator** (Nature 2024)
   - 论文：https://www.nature.com/articles/s44335-024-00004-2
   - 核心：PIM加速自回归transformer

3. **Survey on Processing-in-Memory Techniques** (ResearchGate)
   - 论文：https://www.researchgate.net/publication/366694377

4. **A Fast Overlap-Driven Mapping Framework for Processing In-Memory** (IEEE 2025)
   - 论文：https://ui.adsabs.harvard.edu/abs/2025ITCAD..44..130W/abstract

5. **A Processing In-Memory Architecture for Neural Network Acceleration**
   - 论文：https://acsweb.ucsd.edu/~sag076/papers/tc19_nnpim.pdf

**Survey资源**：
- Survey of Energy Efficient PIM Processors: https://semiengineering.com/survey-of-energy-efficient-pim-processors/

**相关工作**：
- GNNear: 近存储PIM加速GNN训练
- HGL: 异构GNN训练加速

### 3D Gaussian Splatting

**核心经典论文**：
1. **3D Gaussian Splatting for Real-Time Radiance Field Rendering** (SIGGRAPH 2023)
   - 论文：https://www.graphics.cornell.edu/~tzhang/research/3d_gs/
   - PDF：https://arxiv.org/pdf/2308.04079
   - 原始3DGS论文

2. **3D Gaussian Splatting: Survey, Technologies, Challenges** (arXiv 2024)
   - 论文：https://arxiv.org/pdf/2402.07181
   - 全面综述

3. **3D Gaussian Splatting as a New Era: A Survey** (arXiv 2024)
   - 论文：https://arxiv.org/abs/2402.07181

**Tutorial和资源**：
1. **3D Gaussian Splatting Tutorial (3DV 2024)**
   - 网站：https://3dgstutorial.github.io/
   - 视频：International Conference on 3D Vision (3DV) 2024

2. **Introduction to 3D Gaussian Splatting (SGI 2024)**
   - 论文：https://summergeometry.org/sgi2024/introduction-to-3d-gaussian-splatting/

3. **LearnOpenCV: 3D Gaussian Splatting**
   - 教程：https://learnopencv.com/3d-gaussian-splatting/

**核心概念**：
- SfM (Structure-from-Motion)：从图像恢复相机姿态
- 3D高斯属性：位置、协方差、颜色、不透明度、球谐函数
- Splatting：将3D高斯投影到2D图像平面

### 全同态加密 (FHE)

**核心经典论文**：
1. **Microsoft SEAL: Homomorphic Encryption Library**
   - 官网：https://www.microsoft.com/en-us/research/project/microsoft-seal/
   - 视频：https://www.microsoft.com/en-us/research/video/homomorphic-encryption-with-microsoft-seal/

2. **Homomorphic Encryption on GPU** (Cryptology ePrint 2022)
   - 论文：https://eprint.iacr.org/2022/1222.pdf
   - 性能：比CPU快63.4倍

3. **Empirical Study of FHE Using Microsoft SEAL** (Applied Sciences 2024)
   - 论文：https://www.mdpi.com/2076-3417/14/10/4047

**FHE方案**：
- BFV (Brakerski-Fan-Vercauteren)
- CKKS (Cheon-Kim-Kim-Song)
- TFHE (Torus FHE)

**最新研究**：
1. **Efficient LLM Inference with Fully Homomorphic Encryption** (arXiv 2024)
2. **FHE-based Private Inference** (IEEE 2024)

**Tutorial资源**：
- YouTube: Implement GPU Acceleration in FHE Using Concrete
  - 视频：https://www.youtube.com/watch?v=dgLf2nUlpSY
- Concrete ML: https://github.com/zama-ai/concrete-ml

### 图神经网络加速

**Survey**：
1. **A Survey on Graph Neural Network Acceleration: Algorithms, Systems, and Customized Hardware** (ACM Computing Surveys 2026)
   - 论文：https://arxiv.org/html/2306.14052v2
   - 论文：https://www.researchgate.net/publication/403230972

2. **Acceleration Algorithms in GNNs: A Survey** (IEEE 2025)
   - 论文：https://www.computer.org/csdl/journal/tk/2025/06/10882936

**经典工作**：
- G-Sparse: GPU上广义稀疏计算编译器
- GNNear: 近存储PIM加速GNN
- HGL: 异构GNN训练

### 其他相关资源

**LLM推理框架对比**：
- vLLM vs TensorRT-LLM: https://docs.rafay.co/blog/2025/04/28/choosing-your-engine-for-llm-inference-the-ultimate-vllm-vs-tensorrt-llm-guide/
- 十大LLM服务引擎：https://gautam75.medium.com/ten-ways-to-serve-large-language-models-a-comprehensive-guide-292250b02c11

**KV Cache优化**：
1. **Keep the Cost Down: A Review on Methods to Optimize LLM's KV-Cache Consumption** (OpenReview)
   - 论文：https://openreview.net/forum?id=8tKjqqMM5z
   - 综述：训练、部署、推理各阶段的KV-Cache压缩方法

2. **KVQuant: Towards 10 Million Context Length LLM Inference** (arXiv)
   - 论文：https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf
   - 核心：KV Cache量化到3-bit

3. **CacheGen: KV Cache Compression and Streaming** (SIGCOMM 2024)
   - 论文：https://cs.stanford.edu/~keithw/sigcomm2024/sigcomm24-final1571-acmpaginated.pdf

4. **ChunkKV: Semantic-Preserving KV Cache Compression** (NeurIPS 2025)
   - 论文：https://neurips.cc/virtual/2025/poster/120181

**内存层次结构**：
- Memory-Centric Computing Systems (MCCSys) @ ASPLOS 2026
  - 官网：https://events.safari.ethz.ch/asplos26-MCCSys/

**HPC/AI与量子计算集成**：
- Survey on Integrating Quantum Computers into HPC Systems (arXiv 2025)
  - 论文：https://arxiv.org/pdf/2507.03540

### 硬件设计语言与形式化验证

**核心Survey论文**：
1. **Hardware Design and Verification with Large Language Models: A Literature Survey** (Preprints 2024)
   - 论文：https://www.preprints.org/manuscript/202411.0156
   - 分析54篇论文，全面综述LLM在硬件设计验证中的应用

2. **Formal Hardware Verification Methods: A Survey** (Formal Methods in System Design 1992)
   - 论文：https://collaborate.princeton.edu/en/publications/formal-hardware-verification-methods-a-survey/
   - 经典Survey：形式化验证方法的基础文献

3. **LLMs for Hardware Verification: Frameworks, Techniques, and Applications** (IEEE 2024)
   - 论文：https://www.computer.org/csdl/proceedings-article/ats/2024/10915476/254QXedavJu/

4. **Unlocking Hardware Verification with Oracle Guided Synthesis** (FMCAD 2025)
   - 论文：https://www.research.ed.ac.uk/files/564404482/YeEtalFMCAD2025UnlockingHardwareVerification.pdf

**硬件描述语言**：
- Chisel: https://www.chisel-lang.org/
- SystemVerilog: IEEE 1800标准
- Bluespec: https://www.bluespec.com/

**形式化验证工具**：
- ACL2: http://www.cs.utexas.edu/users/moore/acl2/
- Coq: https://coq.inria.fr/
- Isabelle: https://isabelle.in.tum.de/
- Symbiyosys: https://symbiyosys.readthedocs.io/

### 数据库系统与分解存储

**核心Survey论文**：
1. **Understanding and Optimizing Database Pushdown on Disaggregated Storage**
   - ASPLOS 2026论文

2. **Survey of Disaggregated Memory** (arXiv 2025) - 见上文CXL部分
   - 包含数据库相关的内容

**相关工作**：
- **dLSM**: 分解内存的LSM-tree优化
  - 论文：https://arxiv.org/abs/2308.16775

### 网络与I/O优化

**核心Survey论文**：
1. **I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention**
   - ASPLOS 2026论文

2. **Enabling fast networking in the public cloud**
   - ASPLOS 2026论文

**相关资源**：
- Toasty: Cache-warm buffers加速网络I/O
- Hitchhike: 地址连续性延迟执行的请求提交

### 安全与隐私保护

**相关经典工作**：
1. **DejaVuzz: Transient Execution Bugs with Dynamic Swappable Memory**
   - ASPLOS 2026论文

2. **Signal Breaker: Fuzzing Digital Signal Processors**
   - ASPLOS 2026论文

3. **SEVI: Silent Data Corruption of Vector Instructions**
   - ASPLOS 2026论文

**安全研究资源**：
- CHERI: Capability Hardware Enhanced RISC Instructions
  - 论文：https://www.cl.cam.ac.uk/research/security/erts/cheri/
- ARM CCA: Confidential Computing Architecture
  - 相关论文：Detecting Inconsistencies in ARM CCA's Formally Verified Specification

### 服务器与无服务器计算

**核心Survey论文**：
1. **Lambda-trim: Reducing Monetary and Performance Cost of Serverless Cold Starts**
   - ASPLOS 2026论文
   - 核心：成本驱动的应用精简

2. **Skyler: Static Analysis for Predicting API-Driven Costs in Serverless**
   - ASPLOS 2026论文

3. **WorksetEnclave: Optimizing Cold Starts in Confidential Serverless**
   - ASPLOS 2026论文

**相关资源**：
- Firecracker: AWS的轻量级虚拟化
  - 论文：https://arxiv.org/abs/2401.15112

### 神经符号计算与混合AI

**核心论文**：
1. **Lobster: A GPU-Accelerated Framework for Neurosymbolic Programming**
   - ASPLOS 2026论文

2. **Compositional AI Beyond LLMs: System Implications of Neuro-Symbolic-Probabilistic Architectures**
   - ASPLOS 2026论文

**Survey资源**：
- 神经符号AI综述：https://arxiv.org/abs/2401.01271

### 强化学习与系统优化

**核心论文**：
1. **HistoRL: Accelerating Reinforcement Learning with HistoRL**
   - ASPLOS 2026论文
   - 核心：利用历史数据的rollout加速RL

2. **Taming the Long-Tail: Efficient Reasoning RL Training**
   - ASPLOS 2026论文

**Survey资源**：
- RL for Compiler Optimization: 编译器优化的强化学习
- LLM + RL: DeepMind, OpenAI的相关工作

## 引用链分析

### 主要研究趋势

1. **LLM Serving → Prefill-Decode分离**
   - 经典：vLLM → Orca → 各类PD分离优化 → MuxWise

2. **Memory Disaggregation → CXL生态**
   - 趋势：从远程内存共享 → 内存池化 → 分层内存管理

3. **Quantum Compilation → 实用化**
   - 关注：T门优化、QEC调度、离子阱架构

4. **PIM → 神经网络的实际部署**
   - 方向：KV Cache处理、近存储推理、Wafer-scale CIM

5. **3DGS → 实时大规模渲染**
   - 挑战：GPU内存、训练效率、VR/AR应用

### 跨领域交叉

- LLM + PIM: KV Cache PIM卸载
- Quantum + Compiler: 量子电路优化
- FHE + GPU: 隐私保护推理
- CXL + Database: 分解事务处理

## 总结

ASPLOS 2026展现了系统研究的几个重要方向：

1. **LLM Serving成为核心主题**，涵盖从理论到实践的完整优化栈
2. **CXL内存技术成熟**，开始从研究走向生产系统
3. **量子计算编译**关注实用化和可扩展性
4. **PIM技术多样化**，从神经网络到图计算都有应用
5. **新兴主题**：3DGS、FHE、形式化验证持续增长

会议反映了AI驱动下系统研究的范式转变，硬件软件协同设计成为主流方法。