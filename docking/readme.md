# Rendezvous

This folder contains the simulations for the rendezvous scenario

# Usage

This code was written using Julia 1.5.1

From inside this folder, run julia:

```
julia
```

Activate the env
```

] activate .

```

and now we should be able to run IJulia 
```
using IJulia; notebook()
```

Navigate to `./docking.ipnb` and run the file. All the simulations and plots should just work. 

# Notes

The `spacecraft.jl` file defines the system

The `docking.ipynb` file is the jupyter file in which i did all my sims

The `docking.jl` file is just an export of the above jupyter file, in case Jupyter doesnt work for you. 
