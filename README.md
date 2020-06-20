# PetroAlchemy
[![Documentation Status](https://readthedocs.org/projects/petroalchemy/badge/?version=latest)](https://petroalchemy.readthedocs.io/en/latest/?badge=latest)
[![Latest Version](https://img.shields.io/github/v/release/mwentzWW/PetroAlchemy?include_prereleases)](https://github.com/mwentzWW/PetroAlchemy/releases)

The PetroAlchemy project is a child of my first attempt to create an open source project for petroleum engineering called petrolpy. The vision is to create an open source desktop application with useful tools for anyone interested in petroleum evaluation. As a reservoir engineer, I wanted to build tools I would actually use. Therefore, the project is beginning with decline curve analysis and estimating cash flows for wells or groups of wells.

The project is in the Alpha phase. I wanted to share it now before developing too much further so I can get feedback from fellow engineers on what features and design decisions they would like included. Please try it out and share your thoughts.

[Alpha Release Tutorial](https://petroalchemy.readthedocs.io/en/latest/alpha_tutorial.html)

This desktop application was created using Python and Tkinter. Performing decline curve analysis and running cash flows is not computationally intensive unless you are running thousands of decline curves, which at that point the code would need to be optimized for speed. As this tool is starting with focus on analyzing a few wells at a time, Python is ideal for feature development and prototyping.

## Current Features

    1. Import Excel/CSV production file
    2. Fit Arps hyperbolic decline curves for oil and gas
    3. Run financial cash flow on decline curves
    4. Preview monthly cash flow in application
    5. Output cash flow to excel

I have a list of features to add to the project. I want to add the ability for engineers to select several different kinds of decline curves, not just Arps hyperbolic/exponential. This application utilized the Society of Petroleum Evaluation Engineer's website and best practices for equations and discounting methodologies.

![Alpha Example](./docs/img/alpha_introduction.gif)

## References

- [Petroleum Engineering Handbook (SPE) Valuation of Oil and Gas Reserves](https://petrowiki.org/PEH:Valuation_of_Oil_and_Gas_Reserves)
- [Financials - SPEE Website](https://spee.org/resources/recommended-evaluation-practices-reps)
- [Fekete Decline Theory](http://www.fekete.com/san/webhelp/feketeharmony/harmony_webhelp/content/html_files/reference_material/Analysis_Method_Theory/Traditional_Decline_Theory.htm)
