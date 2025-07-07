# project-bodhi-tree
A next-generation AI ecosystem for generating and composing Synthetic Expertise, powered by a novel (Spinor Processing Unit) SPU hardware concept and a Geometric-Causal Language Model (GCLM) software architecture.
# Project Bodhi Tree - Software Development Kit (SDK)
**Version: 0.1.0-alpha**

Welcome to the Project Bodhi Tree SDK. This repository contains the reference implementation and simulation of the **Geometric-Causal Language Model (GCLM v3.0)**, a novel AI architecture designed for creative, goal-oriented problem-solving.

Our system is built on the philosophy of **Synthetic Expertise**, where an AI can not only execute tasks but can autonomously learn, create, and share new skills within a decentralized ecosystem.

## Core Concepts

*   **Spinor Processing Unit (SPU):** A custom hardware concept (simulated in this SDK as the `VirtualSPU`) that efficiently performs geometric transformations, which are the mathematical equivalent of conceptual blending.
*   **Assembly of Experts (AoE):** A methodology for creating new AI capabilities by merging the parameters of existing "expert" models. Our `AssemblyModule` implements this.
*   **Goal-Oriented Creative Synthesis:** The highest function of the GCLM. It uses its creative engine to invent novel solutions to user-defined problems.

## Quick Start

This SDK allows you to run a full simulation of the GCLM's creative process on your local machine.

**1. Installation:**
Clone the repository and install the required dependencies.
```bash
git clone [https://github.com/rvjwhite/project-bodhi-tree.git
cd project-bodhi-tree
pip install -r requirements.txt

#File Structure

/project-bodhi-tree
|
|-- bodhi_sdk/
| |-- init.py
| |-- gclm.py # Contains the GCLMv3 class
| |-- goal.py # Contains the Goal data class
| |-- assembly_module.py # The AoE merging logic
| |-- causal_engine.py # The CIE and Curiosity/Planner modules
| |-- spu/
| | |-- init.py
| | |-- virtual_spu.py # The V-SPU simulation
| | |-- dashboard.py # The text-based visualizer
| | |-- driver.py # The software driver
|
|-- examples/
| |-- creative_demo.py # Our main, impressive demo
|
|-- tests/
| |-- test_assembly_module.py
| |-- test_virtual_spu.py
|
|-- .gitignore
|-- LICENSE
|-- README.md
|-- setup.py
|-- requirements.txt

#Python
pycache/
*.py[cod]
*$py.class
#Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
#Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/