[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Doankt">
    <img src="https://avatars.githubusercontent.com/u/36061217?s=460&u=bd3f2f6eba3bba3356afea59827c6b1bbb4d49ee&v=4" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Rabbit & Wolf Evolution Simulation</h3>

  <p align="center">
    Closed box evolution simulation
    <br />
    <a href="https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a> -->
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
 <li><a href="#design">Design</li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Welcome to my simulation. I wrote this as a test to myself proving that I can develop and design my own system.

This program simulates Grass, Rabbits, and Wolves in a closed box envinroment. Rabbits eat Grass, while Wolves hunt Rabbits. Evolution comes into play when Rabbits and Wolves Reproduce. A child's properties will change on random to simulate genetic variance in offspring.

I challenged myself to follow concepts that I have learned at my time in university and also design that is not _spaghetti code_.

Much of the Animal logic in this project relies on a [Finite State Machine](https://en.wikipedia.org/wiki/Finite-state_machine) where Animal's decision making was based on it's state.

I was also able to demonstrate my knowlege on [Python Threading](https://docs.python.org/3/library/threading.html) by creating statistic tracker threads while the main simulation was running.

### Built With

* [pygame](https://www.pygame.org/news)
* [matplotlib](https://matplotlib.org/stable/index.html)

## Design

WORK IN PROGRESS

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow the steps below.

### Prerequisites

A Python installation is necessary for running the simulation

* [Python 3.9.0 or above](https://www.python.org/downloads/)

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation
   ```

2. [Create venv (OPTIONAL)](https://docs.python.org/3/library/venv.html)

   ```sh
   python3 -m venv /path/to/new/virtual/environment
   ```

3. Install dependencies from project root

    ```sh
    python3 -m pip install -r requirements.txt
    ```

    Alternatively if you are using a venv

    ```sh
    pip install -r requirements.txt
    ```

<!-- USAGE EXAMPLES -->
## Usage

Run the program with the following command

```sh
python evosim.py
```

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- CONTRIBUTING -->
## Contributing

Please follow common contribution timeline.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Kenneth Doan - kennethdoanor@gmail.com

Project Link: [https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation](https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew's README TEMPLATE](https://github.com/othneildrew/Best-README-Template)

<!-- * []()
* []() -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Doankt/Rabbit-Wolf-Evolution-Simulation.svg?style=for-the-badge
[contributors-url]: https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Doankt/Rabbit-Wolf-Evolution-Simulation.svg?style=for-the-badge
[forks-url]: https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation/network/members
[stars-shield]: https://img.shields.io/github/stars/Doankt/Rabbit-Wolf-Evolution-Simulation.svg?style=for-the-badge
[stars-url]: https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation/stargazers
[issues-shield]: https://img.shields.io/github/issues/Doankt/Rabbit-Wolf-Evolution-Simulation.svg?style=for-the-badge
[issues-url]: https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation/issues
[license-shield]: https://img.shields.io/github/license/Doankt/Rabbit-Wolf-Evolution-Simulation.svg?style=for-the-badge
[license-url]: https://github.com/Doankt/Rabbit-Wolf-Evolution-Simulation/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/doankt/
