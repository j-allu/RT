*** Settings ***
Library          DynamicLibrary.py
Library          HybridLibrary.py


*** Test Cases ***
Dynamic library
    Dynamic keyword
    Keyword with arguments    argument
    Keyword with arguments    foo    bar

Hybrid library
    Hybrid keyword
    External hybrid keyword
