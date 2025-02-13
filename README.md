# Langchain 教程 Notebooks

本仓库包含一系列 Jupyter Notebook，旨在引导您学习和掌握 Langchain 的各项功能。Langchain 是一个强大的框架，用于构建由语言模型驱动的应用程序。

本教程通过一系列 Notebook，由浅入深地介绍 Langchain 的各种特性。每个 Notebook 都专注于 Langchain 的一个特定方面，并在之前 Notebook 的基础上逐步构建知识体系。这种结构化的学习方式能够帮助您循序渐进地学习和掌握 Langchain 的强大功能，从基本用法到更高级的技术应用。

## Notebook 目录结构

所有的 Notebook 都组织在 `langchain` 目录下，并且按照序号排列，以反映一个循序渐进的学习路径：
*   **`01.base.ipynb`**:  介绍 Langchain 的基本概念，搭建基础环境并演示核心功能。
*   **`02.role_player.ipynb`**:  探索如何使用 Langchain 创建角色扮演场景或代理，使其能够扮演不同的角色和行为模式。
*   **`03.length_selector.ipynb`**:  重点介绍控制和管理 Langchain 中语言模型生成响应长度的技术。
*   **`04.output_parser_json.ipynb`**:  演示如何将语言模型的输出解析为结构化的 JSON 格式，方便数据提取和处理。
*   **`05.output_parser_xml.ipynb`**:  类似于 JSON 解析器，本 Notebook 展示如何将语言模型输出解析为 XML 格式，以处理结构化数据。
*   **`06.runnable_bind_tools.ipynb`**:  探索外部工具与 Langchain Runnable 的集成，使语言模型能够与外部资源交互和利用。
*   **`07.document_loader.ipynb`**:  涵盖将不同类型文档加载到 Langchain 中进行处理和分析的各种方法。
*   **`08.extract_information_from_arxiv.ipynb`**:  提供一个实际示例，展示如何使用 Langchain 从 arXiv 上的研究论文中提取相关信息。
*   **`09.runnable_lambda.ipynb`**:  介绍 `RunnableLambda` 在 Langchain 中的应用，使自定义 Python 函数能够集成到 Langchain 链中。
*   **`10.runnable_parallel.ipynb`**:  演示如何并行执行 Langchain Runnable，从而加速复杂任务的处理。
*   **`11.split_document.ipynb`**:  重点介绍将大型文档分割成更小块的技术，这对于语言模型高效处理长文档通常是必要的。
*   **`12.simple_conversation.ipynb`**:  指导您使用 Langchain 构建基本的对话应用程序，展示记忆和对话流程管理。
*   **`13.retriever_fusion.ipynb`**:  探索合并多个检索器以提高检索信息相关性和全面性的方法。
*   **`14.context_compression.ipynb`**:  介绍压缩提供给语言模型的上下文的技术，从而提高性能并减少 Token 使用量。
*   **`15.selfquery.ipynb` & `15-1.selfquery_process_coding.ipynb`**:  深入研究自查询技术，使语言模型能够生成自己的查询来检索与用户输入相关的的信息。Notebook `15-1` 可能侧重于自查询的编码过程。
*   **`16.time_weight.ipynb`**:  探索时间加权检索的概念，文档的最新程度或时间会影响其相关性。
*   **`17.document_parent.ipynb`**:  可能与文档层级结构和父子关系相关，用于更复杂的文档检索策略。
*   **`18.multi_vector.ipynb`**:  介绍多向量检索的使用，可能涉及不同的嵌入类型或向量表示，以增强检索效果。
*   **`19.indexing.ipynb`**:  涵盖 Langchain 中文档索引技术，以实现高效的搜索和检索。
*   **`20.memory.ipynb`**:  扩展 Langchain 中记忆的概念，展示更高级的记忆管理和在对话应用程序中的应用。
*   **`21.runnable_passthrough.ipynb`**:  演示 `RunnablePassthrough` 在 Langchain 中的应用，允许数据在链中流动，并在特定步骤保持不变。
*   **`22.runnable_sequence.ipynb`**:  重点介绍创建 Langchain Runnable 的顺序链，通过组合更简单的组件构建复杂的工作流程。
*   **`23.agent.ipynb`**:  介绍使用 Langchain 开发 Agent，展示自主实体如何与环境交互并根据语言模型推理执行任务。

## 代码克隆

克隆代码，并进入项目目录。

```bash
git clone git@github.com:geekmaxi/langchain_guide.git
cd langchain_guide
```

## 环境配置

本教程推荐使用 conda 管理 Python 环境。请确保您已安装 conda。如果尚未安装，请访问 [conda 官网](https://docs.conda.io/en/latest/miniconda.html) 下载并安装。

1.  **创建 conda 虚拟环境:**

    打开终端或 Anaconda Prompt，导航到本仓库根目录，并运行以下命令创建名为 `langchain-tutorial` 的虚拟环境 (您可以根据需要自定义环境名称):

    ```bash
    conda create -n langchain-tutorial python=3.10  # 推荐使用 Python 3.10 或更高版本
    ```

2.  **激活虚拟环境:**

    创建完成后，激活该虚拟环境：

    ```bash
    conda activate langchain-tutorial
    ```

## 依赖安装

本项目的依赖包信息已记录在 `pyproject.toml` 文件中。推荐使用 `pip` 安装项目依赖。请确保您已激活上面创建的 conda 虚拟环境，然后在仓库根目录下运行以下命令安装依赖：

```bash
pip install -e . # 基于 pyproject.toml 文件进行安装依赖命令
```

## 快速开始
按照以下步骤开始学习这些 Notebook：

1. 克隆本仓库到本地。
1. 确保您已安装 Python 和 Jupyter Notebook，并配置好 conda 虚拟环境。
1. 根据 "环境配置" 和 "依赖安装" 章节的说明，创建并激活 conda 虚拟环境，并安装项目依赖。
1. 导航到 langchain 目录，并在 Jupyter Notebook 中打开 Notebook 文件。
1. 按照 Notebook 的序号顺序，逐个学习 Langchain 的各项功能。

本教程系列旨在为您提供 Langchain 的全面入门指导。通过学习这些 Notebook，您将能够扎实地掌握如何利用 Langchain 构建强大的语言模型应用程序。祝您 Langchain 学习之旅愉快！

