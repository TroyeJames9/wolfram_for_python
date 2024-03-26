# -*- coding: utf-8 -*-

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr


# Replace 'your_kernel_path' with the actual path to the Wolfram Kernel executable.
# exp: session = WolframLanguageSession(r'your_kernel_path')
# you should have download mathematica or wolfram engine
# how to find Wolfram Kernel executable: "mathematica/MathKernel.exe" or "Wolfram Engine\*\MathKernel.exe"
# like this↓
session = WolframLanguageSession(r'D:\mathematica\MathKernel.exe')

# Evaluate any Wolfram Language code from Python
print(session.evaluate(wlexpr('Range[5]')))
print(session.evaluate(wl.MinMax([1, -3, 0, 9, 5])))

session.terminate()
