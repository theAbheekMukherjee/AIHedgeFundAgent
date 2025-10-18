#!/usr/bin/env python3
"""
Run the AIHedgeFundAgent notebook programmatically for quick validation.
Usage:
    python run_notebook.py

This script will:
- Check that the PPLX_API_KEY environment variable is set (warn if placeholder).
- Execute `AIHedgeFundAgent.ipynb` and write an executed copy to `AIHedgeFundAgent-executed.ipynb`.

Note: Running the notebook will make live API calls if the chains are invoked.
"""
import os
import sys
from nbformat import read, write, NO_CONVERT
from nbconvert.preprocessors import ExecutePreprocessor

NOTEBOOK = "AIHedgeFundAgent.ipynb"
OUT_NOTEBOOK = "AIHedgeFundAgent-executed.ipynb"


def main():
    key = os.getenv("PPLX_API_KEY")
    if not key or key == "<REPLACE_WITH_YOUR_KEY>" or key.startswith("<"):
        print("Warning: PPLX_API_KEY is not set to a real value. Set environment variable before running the notebook.")
        print("You can set it with: export PPLX_API_KEY=\"your_real_key\"")

    if not os.path.exists(NOTEBOOK):
        print(f"Notebook {NOTEBOOK} not found in current directory: {os.getcwd()}")
        sys.exit(2)

    with open(NOTEBOOK, "r", encoding="utf-8") as fh:
        nb = read(fh, as_version=NO_CONVERT)

    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    try:
        ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})
    except Exception as e:
        print("Notebook execution failed:", e)
        # still write partial output for debugging
        with open(OUT_NOTEBOOK, "w", encoding="utf-8") as fh:
            write(nb, fh)
        sys.exit(1)

    with open(OUT_NOTEBOOK, "w", encoding="utf-8") as fh:
        write(nb, fh)

    print(f"Executed notebook written to {OUT_NOTEBOOK}")


if __name__ == "__main__":
    main()
