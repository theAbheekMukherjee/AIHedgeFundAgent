# AIHedgeFundAgent

Multi-agent AI systems using LangChain and Perplexity AI enable real-time market data retrieval, sentiment and macro analysis, and risk-aware strategy design in hedge funds. Sequential orchestration, transformer models, and reinforcement learning drive adaptive, high-performance trading pipelines.

## Overview

AIHedgeFundAgent is an experimental prototype that composes several LangChain LLMChains and Perplexity's ChatPerplexity model into a sequential orchestration. The pipeline is designed to:

- Retrieve market data
- Analyze sentiment from news and social media
- Assess macro-economic indicators
- Synthesize a quantitative trading strategy
- Produce a concise risk assessment

The project focuses on modularity: each stage is an independent chain so you can replace or extend data sources, models, and downstream logic.

## Quickstart

1. Open the workspace or clone the repo and change directory:

```bash
cd /workspaces/AIHedgeFundAgent
```

2. Install dependencies (recommended in a virtual environment):

```bash
pip install -r requirements.txt || \
pip install langchain==0.3.19 langchain-community==0.3.18 openai==1.65.2 ipykernel==6.29.5
```

3. Export your Perplexity API key into the environment (do not commit keys):

```bash
export PPLX_API_KEY="your_real_key_here"
```

4. Open and run the notebook `AIHedgeFundAgent.ipynb` in VS Code (Jupyter extension) or Jupyter Lab.

## Security note

Never commit API keys or other secrets to source control. Use environment variables, a secrets manager, or the platform's secret store. If a secret was committed by mistake: rotate the secret immediately and scrub it from your git history.

## Next steps and suggestions

- Add robust data connectors (e.g., Alpha Vantage, Yahoo Finance, Bloomberg) and caching.
- Add a backtesting harness and unit tests for strategy validation.
- Integrate a secrets manager and CI checks to block secrets before push.
- Add monitoring and logging for live deployments.

## License

Add a LICENSE file if you intend to open-source this project.
