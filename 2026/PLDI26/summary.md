# PLDI 2026 论文分析报告

会议名称：第47届 ACM SIGPLAN 编程语言设计与实现会议 (PLDI 2026)
会议链接：https://pldi26.sigplan.org/track/pldi-2026-papers#event-overview
会议地点：美国科罗拉多州博尔德市 Limelight Boulder
会议时间：2026年6月17–19日（主会），6月15–16日（workshops/tutorials）
论文总数：116篇

报告覆盖了 15 大主题类别：             

1. 程序验证与分离逻辑 — 18篇，涵盖 Iris 扩展、Hyper Separation Logic、差分隐私验证等
2. 类型系统与 PL 理论 — 10篇，可达性类型、概率精化会话类型、线性 Haskell 等
3. 编译器优化与验证 — 10篇，SSA without Dominance、等式饱和、LLVM undef 值移除等
4. 程序综合 — 8篇，Presynthesis、LLM 引导循环不变式综合等
5. 程序分析与抽象解释 — 10篇，SAIL (LLM+抽象解释)、WCET 估计等
6. 量子编程语言与验证 — 7篇
7. 并发与内存模型 — 8篇，DPOR、线性化监控、分布式共识验证
8. 概率编程 — 4篇
9. 测试、符号执行与模糊测试 — 8篇
10. GPU 编程与验证 — 8篇
11. 高性能计算与编译器 — 9篇
12. 语言互操作与迁移 — 6篇（C++→Rust 为主）
14. 机器学习与代码生成 — 4篇
15. 其他 — 2篇

---

## 1. 程序验证与分离逻辑 (Program Verification & Separation Logic)

### 1.1 分离逻辑与程序逻辑
- **[TOPLAS] VyZX: Formal Verification of a Graphical Quantum Language** — 图形化量子语言的正式验证
- **Iris-WasmFX: Modular Reasoning for Wasm Stack Switching** — Iris 中 Wasm 栈切换的模块化推理
- **Cerisier: A Program Logic for Attestation in a Capability Machine** — 能力机器的 attestation 程序逻辑
- **A Deductive System for Contract Satisfaction Proofs** — 合约满足性证明的演绎系统
- **Hyper Separation Logic** — 超属性分离逻辑
- **Causality and Semantic Separation** — 因果性与语义分离
- **Code-Specify-Test-Debug-Prove: Flexibly Integrating Separation Logic Specification into Conventional Workflows** — 将分离逻辑规约灵活集成到常规工作流

### 1.2 程序验证技术
- **Counterexample-Guided Inference of Modular Specifications** — 反例引导的模块化规约推断 [SIGPLAN]
- **Verification Modulo Tested Library Contracts** — 验证模测试库合约
- **Expecto: Extracting Formal Specifications from Natural Language Description for Trustworthy Oracles** — 从自然语言提取形式规约
- **Simplifying Safety Proofs with Forward-Backward Reasoning and Prophecy** — 前向-后向推理与预言的 safety 证明
- **Solvable Tuple Patterns and Their Applications to Program Verification** — 可解元组模式及其在程序验证中的应用
- **CRIS: The Power of Imagination in Hybrid Verification** — 混合验证中的想象力
- **[TOPLAS] Denotation-based Compositional Compiler Verification** — 基于指称的组合编译器验证
- **Heterogeneous Dynamic Logic: Provability Modulo Program Theories** — 异质动态逻辑：模程序理论的可证性
- **A Categorical Basis for Robust Program Analysis** — 鲁棒程序分析的范畴论基础

### 1.3 安全与信息流
- **Pantomime: Constructive Leakage Proofs via Simulation** — 通过模拟的构造性泄漏证明
- **The Downgrading Semantics of Memory Safety** — 内存安全的降级语义
- **The Rise & Collapse of a Quantum State** — 量子态的兴起与坍缩
- **VerusBelt: A Semantic Foundation for Verus's Proof-Oriented Extensions to the Rust Type System** — Verus 的 Rust 类型系统证明扩展的语义基础
- **Project Everest: Perspectives from Developing Industrial-Grade High-Assurance Software** — 工业级高可信软件开发的 Everest 项目经验 [TOPLAS]

### 1.4 不确定性验证 (概率与差分隐私)
- **Modular Verification of Differential Privacy in Probabilistic Higher-Order Separation Logic** — 概率高阶分离逻辑中的模块化差分隐私验证
- **SuperDP: Differential Privacy Refutation via Supermartingales** — 通过超鞅的差分隐私反驳
- **Supermartingales for Unique Fixed Points: A Unified Approach to Lower Bound Verification** — 唯一不动点的超鞅：下界验证的统一方法
- **A Hierarchy of Supermartingales for ω-Regular Verification** — ω-正则验证的超鞅层次结构
- **Contextual Refinement of Higher-Order Concurrent Probabilistic Programs** — 高阶并发概率程序的上下文精化

---

## 2. 类型系统与编程语言理论 (Type Systems & PL Theory)

### 2.1 类型系统设计
- **[SIGPLAN] Complete the Cycle: Reachability Types with Expressive Cyclic References** — 具有表达性循环引用的可达性类型
- **Escape with Your Self: Sound and Expressive Bidirectional Typing with Avoidance for Reachability Types** — 可达性类型的可靠表达性双向类型检查
- **Typestate via Revocable Capabilities** — 通过可撤销能力实现的类型状态
- **Backwards-Compatible Row-Based Exceptions in ML** — ML 中向后兼容的基于行的异常
- **Syntactic Implicit Parameters with Static Overloading** — 具有静态重载的语法隐式参数
- **Pure Borrow: Linear Haskell Meets Rust-Style Borrowing** — 线性 Haskell 遇见 Rust 风格借用

### 2.2 语言特性与语义
- **Contextual Embeddings: Implementing Bound Variables through Instance Resolution** — 通过实例解析实现绑定变量
- **[SIGPLAN] Probabilistic Refinement Session Types** — 概率精化会话类型 [SIGPLAN]
- **Dynamically Checked Deep Immutability in Python** — Python 中动态检查的深度不可变性
- **Virtualizing Continuations** — 虚拟化 continuation
- **Responsive Parallelism with Dynamic and First-Class Priorities** — 具有动态一等优先级的响应式并行

---

## 3. 编译器优化与验证 (Compiler Optimization & Verification)

### 3.1 编译器验证
- **Towards Removing Undef Values from LLVM IR** — 从 LLVM IR 中移除 undef 值
- **[TOPLAS] Denotation-based Compositional Compiler Verification** — 基于指称的组合编译器验证（同1.2）

### 3.2 中间表示与优化
- **SSA without Dominance for Higher-Order Programs** — 高阶程序的无支配关系 SSA
- **Flow-Analysis-Based Closure Optimization** — 基于流分析的闭包优化
- **Redundant Array Computation Elimination** — 冗余数组计算消除
- **Let It Flow: A Formally Verified Compilation Framework for Asynchronous Dataflow** — 异步数据流的形式化验证编译框架
- **Compiling to Recurrent Neurons** — 编译到循环神经元

### 3.3 等式饱和 (Equality Saturation)
- **Optimism in Equality Saturation** — 等式饱和中的乐观策略
- **Versioned E-Graphs** — 版本化 E-Graphs
- **Improving Equality Saturation for EDA via Semantic E-Graphs** — 通过语义 E-Graphs 改进 EDA 的等式饱和
- **Equality Saturation for Quantum Circuit Optimization** — 量子电路优化的等式饱和

### 3.4 编译器代码生成与重定位
- **Fungible Memories for Automated Technology Mapping and Retargeting** — 自动化技术映射与重定向的可互换内存
- **Compiling Strassen-like Matrix Multiplication Algorithms to Fast CUDA Kernels** — Strassen 风格矩阵乘法的 CUDA 内核编译
- **Parameterized Algorithms and Complexity for Function Merging with Branch Reordering** — 分支重排序的函数合并参数化算法与复杂度

---

## 4. 程序综合 (Program Synthesis)

### 4.1 综合方法
- **Presynthesis: Towards Scaling Up Program Synthesis with Finer-Grained Abstract Semantics** — 通过细粒度抽象语义扩展程序综合
- **Choose, Don't Label: Multiple-Choice Query Synthesis for Program Disambiguation** — 多选查询综合用于程序消歧
- **CEGIS with LLMs: Active Learning for Neurosymbolic Program Synthesis** — 神经符号程序综合的主动学习 [SIGPLAN]
- **[TOPLAS] Guiding LLM-based Loop Invariant Synthesis via Feedback on Local Reasoning Errors** — 通过局部推理错误反馈引导基于 LLM 的循环不变式综合
- **Optimal Predicate Pushdown Synthesis** — 最优谓词下推综合

### 4.2 综合应用
- **Synthesizing Backward Error Bounds, Backward** — 向后综合后向误差界
- **Trace-Guided Synthesis of Effectful Test Generators** — 迹引导的 effectful 测试生成器综合
- **TreeCoder: Systematic Exploration and Optimisation of Decoding and Constraints for LLM Code Generation** — LLM 代码生成的系统解码与约束优化

---

## 5. 程序分析与抽象解释 (Program Analysis & Abstract Interpretation)

### 5.1 抽象解释
- **Path-Sensitive Abstract Interpretation for WCET Estimation** — WCET 估计的路径敏感抽象解释
- **SAIL: Sound Abstract Interpreters with LLMs** — 基于 LLM 的可靠抽象解释器
- **Evolving Abstract Transformers for Gradient-Guided, Adaptable Abstract Interpretation** — 梯度引导的自适应抽象解释的抽象变换器进化
- **Abstract Interpretation with Confidence** — 带置信度的抽象解释

### 5.2 静态分析
- **Analyzing Bytes: Pre-Disassembly Static Binary Analysis** — 预反汇编的静态二进制分析
- **Exploiting Sophisticated Static Analysis for Verilog** — Verilog 的高级静态分析
- **Bridging Coverage and Confidence: Reliable Static False Alarm Elimination via Input-Agnosticity** — 通过输入无关性消除静态误报
- **Restart and Refine: Scalable IFDS Taint Analysis across Memory Budgets** — 跨内存预算的可扩展 IFDS 污点分析
- **A Formally Verified Foundation for Compositional Heterogeneous Coherence** — 组合式异质一致性的形式化验证基础

### 5.3 字符串分析与正则
- **Towards Efficient Matching of Regexes with Backreferences using Register Set Automata** — 基于寄存器集自动机的反向引用正则表达式匹配
- **EREQ: Regular Expressions with Quantifiers and Incremental Quantifier Elimination** — 带量词的正则表达式与增量量词消除

---

## 6. 量子程序语言与验证 (Quantum Programming Languages & Verification)

- **Verification of Recursively Defined Quantum Circuits** — 递归定义量子电路的验证
- **SAQR-QC: A Logic for Scalable but Approximate Quantitative Reasoning about Quantum Circuits** — 可扩展近似定量推理量子电路逻辑
- **Hybrid Path-Sums for Hybrid Quantum Programs** — 混合量子程序的混合路径和
- **[TOPLAS] VyZX: Formal Verification of a Graphical Quantum Language** — 图形化量子语言的形式化验证
- **Cobble: Compiling Block Encodings for Quantum Computational Linear Algebra** — 量子计算线性代数的块编码编译
- **Equality Saturation for Quantum Circuit Optimization** — 量子电路优化的等式饱和（同3.3）
- **The Rise & Collapse of a Quantum State** — 量子态的兴起与坍缩

---

## 7. 并发与内存模型 (Concurrency & Memory Models)

### 7.1 并发验证
- **State Space Estimation for DPOR-Based Model Checkers** — 基于 DPOR 的模型检查器的状态空间估计
- **Fixed Parameter Tractable Linearizability Monitoring** — 固定参数可处理的线性化监控
- **Fast Atomicity Monitoring** — 快速原子性监控
- **SuperCollider: Scalable and Effective Data Race Detection for CUDA** — CUDA 的可扩展有效数据竞争检测
- **Hyper Separation Logic** — 超属性分离逻辑（同1.1）

### 7.2 分布式系统验证
- **SureDistrib: Verifying Almost-Sure Termination of Composite Asynchronous Byzantine Protocols** — 组合异步拜占庭协议的几乎必然终止验证
- **Implementability of Global Distributed Protocols Modulo Network Architectures** — 模网络架构的全局分布式协议可实现性
- **Weighted NetKAT: A Programming Language For Quantitative Network Verification** — 定量网络验证的编程语言
- **MatchBox: A Semantic Foundation for Data Plane Portability** — 数据平面可移植性的语义基础
- **Revisiting Partial Tracing for Safe, Efficient, and Concurrent Garbage Collection** — 部分追踪的并发垃圾回收

---

## 8. 概率编程 (Probabilistic Programming)

- **Incremental Computation for Efficient Programmable Inference in Probabilistic Programs** — 概率程序的高效可编程推理的增量计算
- **GradInf: Gradient Estimation as Probabilistic Inference** — 作为概率推理的梯度估计
- **[SIGPLAN] Probabilistic Inference for Datalog with Correlated Inputs** — 相关输入的 Datalog 概率推理
- **Categorical Semantics of Probabilistic Symbolic Execution** — 概率符号执行的范畴语义

---

## 9. 测试、符号执行与模糊测试 (Testing, Symbolic Execution & Fuzzing)

### 9.1 符号执行与测试
- **Soteria: Efficient Symbolic Execution as a Functional Library** — 作为函数库的高效符号执行
- **Categorical Semantics of Probabilistic Symbolic Execution** — 概率符号执行的范畴语义（同8）
- **[SIGPLAN] Scalable and Accurate Application-Level Crash-Consistency Testing via Representative Testing** — 基于代表性测试的应用级崩溃一致性测试

### 9.2 测试生成与模糊测试
- **Hardening the Foundation: Testing Data and Compute-Intensive AI-Enabling Stacks** — AI 支撑栈的测试
- **Semantic Reification: A New Paradigm for Random Program Generation** — 随机程序生成的新范式：语义具体化
- **The Search for Constrained Random Generators** — 约束随机生成器的搜索
- **Trace-Guided Synthesis of Effectful Test Generators** — 迹引导的效果测试生成器综合（同4.2）
- **Navigating AND–OR Graph Modifications to Debug Failing Proof Search** — 导航 AND-OR 图修改以调试失败的证明搜索

### 9.3 程序可视化与调试
- **Diagramming Program Values by Spatial Refinement** — 通过空间精化的程序值图示
- **Persistent Iterators with Value Semantics** — 具有值语义的持久迭代器

---

## 10. GPU 编程与验证 (GPU Programming & Verification)

### 10.1 GPU 验证
- **Kuiper: Correct and Efficient GPU Programming with Dependent Types and Separation Logic** — 依赖类型和分离逻辑的正确高效 GPU 编程
- **SuperCollider: Scalable and Effective Data Race Detection for CUDA** — CUDA 的可扩展数据竞争检测（同7.1）

### 10.2 GPU 编程模型与优化
- **Modular GPU Programming with Typed Perspectives** — 带类型视角的模块化 GPU 编程
- **[TOPLAS] StreamAlloc: A Framework for Analyzing and Transforming CUDA Code to Enable Asynchronous Execution** — CUDA 异步执行的分析与变换框架
- **SIMT-Step Execution: A Flexible Operational Semantics For GPU Subgroup Behavior** — GPU 子组行为的灵活操作语义
- **Uniformity Analysis in the WebGPU Shading Language** — WebGPU 着色语言的 uniformity 分析
- **Neptune: Advanced ML Operator Fusion for Locality and Parallelism on GPUs** — GPU 上 ML 算子融合的高级优化
- **Compiling Strassen-like Matrix Multiplication Algorithms to Fast CUDA Kernels** — Strassen 风格矩阵乘法的 CUDA 编译（同3.4）

---

## 11. 高性能计算与编译器 (High-Performance Computing & Compilers)

- **A Mechanized Algebra of Verified Data Structures for Optimizing Sparse Tensor Programs** — 稀疏张量程序优化的验证数据结构代数
- **NEURA: A Unified and Retargetable Compilation Framework for Coarse-Grained Reconfigurable Architectures** — 粗粒度可重构架构的统一可重定向编译
- **SparseZETA: Intelligent Auto-tuner for Designing High-Performance SpMV Programs** — 高性能 SpMV 程序的智能自动调优器
- **Decoupling Data Layouts from Bounding Volume Hierarchies** — 数据布局与包围体层次结构的解耦
- **Bonsai: Compiling Queries to Pruned Tree Traversals** — 查询编译到剪枝树遍历
- **A Compiler for Fused Relational Operations on Multisets** — 多重集融合关系操作的编译器
- **[SIGPLAN] Homomorphism Calculus for User-Defined Aggregations** — 用户定义聚合的同态演算
- **CoTenN: Constrained Optimization with Tensor Networks** — 张量网络的约束优化
- **Verifying Array Properties in Pure Data-Parallel Programs** — 纯数据并行程序的数组属性验证

---

## 12. 编程语言互操作与迁移 (Language Interoperability & Migration)

### 12.1 C++ 到 Rust 翻译
- **Cpp2Rust: Automatic Translation of C++ to Safe Rust** — C++ 到安全 Rust 的自动翻译
- **&inator: Correct, Precise C-to-Rust Interface Translation** — 正确精确的 C 到 Rust 接口翻译
- **Hayroll: A Modular Wrapper for Translating C Macros and Conditional Compilation to Rust** — C 宏和条件编译到 Rust 的模块化封装翻译

### 12.2 内存管理
- **FlexHeap: Dynamic I/O-Aware Heap Resizing for Managed Applications** — 托管应用的动态 I/O 感知堆大小调整
- **Revisiting Partial Tracing for Safe, Efficient, and Concurrent Garbage Collection in Unmanaged Languages** — 非托管语言的部分追踪并发垃圾回收（同7.2）

---

## 13. 浮点与数值计算 (Floating-Point & Numerical Computation)

- **Scalable Floating-Point Satisfiability via Staged Optimization** — 通过分阶段优化的可扩展浮点可满足性
- **Synthesizing Backward Error Bounds, Backward** — 向后综合后向误差界（同4.2）

---

## 14. 机器学习与代码生成 (ML & Code Generation)

- **TreeCoder: Systematic Exploration and Optimisation of Decoding and Constraints for LLM Code Generation** — LLM 代码生成的系统解码与约束优化（同4.2）
- **[TOPLAS] Guiding LLM-based Loop Invariant Synthesis via Feedback on Local Reasoning Errors** — 通过局部推理错误反馈引导 LLM 循环不变式综合（同4.1）
- **SAIL: Sound Abstract Interpreters with LLMs** — 基于 LLM 的可靠抽象解释器（同5.1）
- **[SIGPLAN] Active Learning for Neurosymbolic Program Synthesis** — 神经符号程序综合的主动学习（同4.1）

---

## 15. 其他主题

- **An Efficient Algorithm for Streaming BPE Tokenization** — 流式 BPE 分词的高效算法
- **Intrinsically Correct Algorithms and Recursive Coalgebras** — 内在正确算法与递归余代数

---

## 主题基础与经典论文

### 程序验证与分离逻辑
- Reynolds, J.C. "Separation Logic: A Logic for Shared Mutable Data Structures" (LICS 2002)
- O'Hearn, P. "Resources, Concurrency, and Local Reasoning" (Theoretical Computer Science, 2007)
- Iris: Krebbers et al. "The Essence of Higher-Order Concurrent Separation Logic" (ESOP 2017)
- Dafny: Leino. "Dafny: An Automatic Program Verifier for Functional Correctness" (LPAR 2010)

### 类型系统
- Girard, R. "The System F of Variable Types, Fifteen Years Later" (Theoretical Computer Science, 1986)
- Milner, R. "A Theory of Type Polymorphism in Programming" (Journal of Computer and System Sciences, 1978)
- Pierce, B.C. "Types and Programming Languages" (MIT Press, 2002)

### 编译器优化与验证
- Lerner, S. et al. "Automatically Proving the Correctness of Compiler Optimizations" (PLDI 2003)
- Lopes, N.P. et al. "Alive: Low-Level Compiler Verification" (PLDI 2015)
- Muchnick, S.S. "Advanced Compiler Design and Implementation" (Morgan Kaufmann, 1997)

### 程序综合
- Gulwani, S. et al. "Program Synthesis" (Foundations and Trends in Programming Languages, 2017)
- Solar-Lezama, A. "Program Synthesis by Sketching" (PhD Thesis, UC Berkeley, 2008)

### 抽象解释
- Cousot, P. & Cousot, R. "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs" (POPL 1977)
- Nielson, F., Nielson, H.R., Hankin, C. "Principles of Program Analysis" (Springer, 1999)

### 等式饱和与 E-Graphs
- Tate, R. et al. "Equality Saturation: A New Approach to Optimization" (POPL 2009)
- Willsey, M. et al. "Egg: Fast and Extensible Equality Saturation" (POPL 2021)

### 概率编程
- Goodman, N.D. et al. "Church: A Language for Generative Models" (UAI 2008)
- Wingate, D. et al. "Lightweight Implementations of Probabilistic Programming Languages via Transformational Compilation" (AISTATS 2011)

### 量子程序语言
- Selinger, P. "Towards a Quantum Programming Language" (Mathematical Structures in Computer Science, 2004)
- Knill, E. "Conventions for Quantum Pseudocode" (LANL Report, 1996)

### 并发与内存模型
- Lamport, L. "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs" (IEEE Transactions on Computers, 1979)
- Sewell, P. et al. "x86-TSO: A Rigorous and Usable Programmer's Model for x86 Multiprocessors" (Communications of the ACM, 2010)
- Flanagan, C. & Qadeer, S. "Types for Atomicity" (TLDI 2003)

### 分布式系统验证
- Lamport, L. "The Part-Time Parliament" (ACM TOCS, 1998)
- Ongaro, D. & Ousterhout, J. "In Search of an Understandable Consensus Algorithm" (ATC 2014)

### GPU 编程
- NVIDIA. "CUDA C++ Programming Guide" (2024)
- Kessenich, J. et al. "SPIR-V Specification" (Khronos Group, 2024)

### 程序测试
- Cadar, C. et al. "EXE: Automatically Generating Inputs of Death" (CCS 2006)
- Godefroid, P. et al. "DART: Directed Automated Random Testing" (PLDI 2005)

### 差分隐私
- Dwork, C. et al. "Calibrating Noise to Sensitivity in Private Data Analysis" (TCC 2006)
- Barthe, G. et al. "Proving Differential Privacy in Hoare Logic" (CSF 2014)

### LLM for Code
- Chen, M. et al. "Evaluating Large Language Models Trained on Code" (arXiv, 2021)
- Li, R. et al. "Competition-Level Code Generation with AlphaCode" (Science, 2022)
