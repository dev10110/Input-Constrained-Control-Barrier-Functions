module Spacecraft

# everything in this module is simply to define the 
# system.

# states:
    # x[1] - x position of chaser [m]
    # x[2] - y position of chaser [m]
    # x[3] - x velocity of chaser [m/s]
    # x[4] - y velocity of chaser [m/s]
    # x[5] - angle of port

# control inputs:
    # u[1] - x force [N]
    # u[2] - y force [N]

# safety constraint:
    # line of sight constraint

using LinearAlgebra

const μ = 398600.0 # gravitational parameter of Earth [km^3/s^2]
const r = (6371 + 400)  # oribtal radius [km]
const n = sqrt(μ/(r^3)) # angular velocity of target around Earth [rad/s]

const mc = 1000.0 # mass of chaser [kg]
const mcinv = 1.0/mc # 1/mass of chaser [1/kg]

const umax = 0.25

const rp = 2.4e-3 # port radius [km]
const rf = 3.0e-3 # finish sims when you get this far [km]

# control matrix
const B = zeros(5, 2) 
B[3,1] = mcinv
B[4,2] = mcinv


const γ = 10 * π/180 # LOS constraint angle
const cosγ = cos(γ) # cosine of LOS angle

const ω = 0.6 * π/180 # rotation rate of ISS


function f!(xd, x)
    # non-allocating version of open-loop dynamics
    
    px = x[1]
    py = x[2]
    vx = x[3]
    vy = x[4]
#     θ  = x[5]
    
    rc = sqrt((r+px)^2 + py^2)
    
    xd[1] = vx
    xd[2] = vy
    xd[3] = n^2 * px + 2 * n * vy + μ/r^2 - μ*(r+px)/rc^3
    xd[4] = n^2 * py - 2 * n * vx - μ * py / rc^3
    xd[5] = ω
    
    return xd
    
end

function f(x)
    # allocating version, provided for convenience

    xd = similar(x)
    
    f!(xd, x)
    
    return xd
end
    

function g(x)
    
    # since it is a constant,
    # its initialized once, and just returned
    
    return B
    
end

function h(x)
    # line of sight constraint
    
    # the constraint is that 
    # θ ≤ γ
    # ∴ cos(θ) ≥ cos(γ)
    # ∴ h(x) = cos(θ) - cos(γ) ≥ 0
    # where θ is the angle between the port axis and the spacecraft's position relative to the port
   
    # this code can be optimized to avoid allocations
    
    # direction vector of port
    vhat = [cos(x[5]), sin(x[5])]
    
    # direction vector of chaser relative to port
    dr = [x[1], x[2]] - rp*vhat
    drhat = dr/norm(dr)
    
    # cos(θ) - cos(γ)
    h = dot(drhat, vhat) - cosγ
    
    # rescaled
    return 100 * h
    
end


function V(x)
    
    px = x[1]
    py = x[2]
    vx = x[3]
    vy = x[4]
    θ  = x[5]
    
    # The desired vx and vy are:
        # vx = - 0.1 ex
        # vy = - 0.1 ey
    
    # relatve to the port.
    
    # where ex, ey are the position of the spacecraft relative to the port
    
    # compute the errors
    ex = px-rp*cos(θ)
    ey = py - rp*sin(θ)
    
    v = (vx + 0.1ex)^2 + (vy + 0.1ey)^2
    
    # rescale
    return 1e4*v

end
    
end    