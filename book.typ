
#import "@preview/shiroa:0.2.0": *

#show: book

#book-meta(
  title: "Zixi Chen",
  description: "Experimental Particle Physics",
  repository: "https://github.com/Serein-Xi/Serein-Xi.github.io",
  authors: ("Zixi Chen",),
  language: "en",

  summary: [
    #prefix-chapter("intro.typ")[Home]

    = Profile

    - #chapter("news.typ")[News]
    - #chapter("research.typ")[Research]
    - #chapter("projects.typ")[Projects]
      - #chapter("projects/solar-pp.typ")[Solar pp Analysis]
      - #chapter("projects/xenonnt-calibration.typ")[XENONnT Calibration]
      - #chapter("projects/discrete-diffusion.typ")[Discrete Diffusion & Metastability]
      - #chapter("projects/potts-phase-transitions.typ")[Potts Phase Transitions]
      - #chapter("projects/airy-wkb.typ")[Airy Equation & WKB]
    - #chapter("about.typ")[About Me]

    = Research Notes

    - #chapter("notes/xenonnt.typ")[XENONnT Notes]
    - #chapter("notes/qft.typ")[Quantum Field Theory]
    - #chapter("notes/statphys.typ")[Statistical Physics]
  ],
)



// re-export page template
#import "/templates/page.typ": project
#let book-page = project
