# EDM Sample Remixing

A Python/PyQt5 interface for analysing, extracting and re-synthesising loops from audio samples, powered by solver-aided code generation with Rosette, generating the resulting programs in Sonic Pi.
Project for Part II of Computer Science Degree

---

## Features

- **Real-time Waveform and Envelope Rendering**
- **Loop Extraction and Pattern Detection** (bar-based activations, RQA, VMM)
- **Solver-Aided Program Synthesis** into Sonic Pi scripts via Rosette and custom DSL
- **MongoDB/GridFS & hash database** for fast audio I/) and recognition
- **Modular Design** following SOLID and Layered Architecture principles
- **Unit Tests** powered by pytest

---

## Repository Layout

```plaintext
EDM_Sample_Remixing/
├── loopextractor/             # External loop-extraction module (git submodule or vendor copy)
├── sample-pi-main/            # Sonic Pi sample `.wav` assets
├── uploaded_projects/         # Example user remix sessions
├── interface/ 
│    ├── interface.py          # MainWindow, signal/slot wiring, UI logic
|    ├── custom.css            # Qt styles
│    ├── load_window.py        # loader dialog
│    ├── worker_thread.py      # Background Worker wrapper
│    ├── draggable_item.py     # envelope plotting helper
│    ├── audio_graph.py        # optimised waveform plotting
├── audio_processing/
│    ├── audiofile_manager.py  # Sample loading & manipulation
│    ├── envelope_processor.py,# Envelope computation
│    ├── repeat_processor.py   # Generate track to play repeated sample occurrences
│    ├── correlator.py         # similairty measures (bar activations, NCC, etc.)
├── storage/
│    ├── audio_database.py     # MongoDB/GridFS persistence
│    ├── audio_recogniser.py   # Content-based matching with abracadabra (Shazam-based algorithm)
├── synthesis/
│    ├── rqa_detector.py       # Recurrence quantification analysis
│    ├── variable_markov_model.py
│    ├── program_generator.py  # DSL AST builders
│    ├── sonic_pi_dsl.py       # Sonic Pi code DSL
│    ├── rosette_integrator.py # Rosette solver glue
│    ├── rosette_translator.py # AST → Sonic Pi code
├── tests_interface.py         # pytest suites (GUI tests)
├── loop_extractor.py          # loop extractor wrapper with optimisations over loopextractor
├── main.py                    # App bootstrap & Qt event loop
└── README.md                  # (this file)
```

## Acknowledgments

- Loop extraction algorithms adapted from the [jblsmith/loopextractor](https://github.com/jblsmith/loopextractor) repository.  
- Inspired by techniques described on the [Unmixer website](https://unmixer.com) for source‐separation and loop detection.  

