println("Yay for Julia")

using LinearAlgebra
using ForwardDiff

using OSQP
using Compat.SparseArrays

using Plots
gr()

include("spacecraft.jl")

sc = Spacecraft
f = Spacecraft.f
g = Spacecraft.g
h = Spacecraft.h
V = Spacecraft.V

umax = Spacecraft.umax

# testing things:
x0 = [0.1, -0.01, 0,0, 0];
@show x0

@show f(x0);

@show g(x0);

@show V(x0);

@show h(x0);

function Lie(h, f)
    # returns a function that computes the Lie Derivative of h along f
    function Lfh(x)
        return ForwardDiff.gradient(h, x)' * f(x)
    end
    return Lfh
end

LfV = Lie(V, f);
LgV = Lie(V, g);

Lfh = Lie(h, f);
Lgh = Lie(h, g);

# testing
@show LfV(x0)

@show LgV(x0)

@show Lfh(x0)

@show Lgh(x0)

# define ICCBF

b0(x) = h(x)
Lfb0 = Lie(b0, f)
Lgb0 = Lie(b0, g)

α0(h) = 0.25*h
b1(x) = Lfb0(x) - norm(Lgb0(x), Inf) * umax + α0(b0(x))
Lfb1 = Lie(b1, f)
Lgb1 = Lie(b1, g);

α1(h) = 0.85*h
b2(x) = Lfb1(x) - norm(Lgb1(x), Inf) * umax + α1(b1(x))
Lfb2 = Lie(b2, f)
Lgb2 = Lie(b2, g);

α2(h) = 0.05 * h

# define the controller 
struct Controller
    prob
    A_con
    l_con
    u_con
end

function setup_controller(x0)
    
    #x0 is a dummy, just to get the correct matrices set up
    
    # Define problem data
    P = sparse(diagm([1.,1, 0, 0]))
    q = [0, 0, 10.0, 50.0]

    # generate constraints
    A_con, l_con, u_con = genConstraints(x0)
    
    # Create OSQP object
    prob = OSQP.Model()

    # Setup workspace and change alpha parameter
    OSQP.setup!(prob; P=P, q=q, A=A_con, l=l_con, u=u_con, verbose=0)
    
    return Controller(prob, A_con, l_con, u_con)
end

function genConstraints(x)
    
    # this is called once, and allocates memory
    # all the constraints are specified 
    
    kv = 0.1 * V(x)
    lfv = LfV(x)
    lgv = LgV(x)

    h = b2(x)
    lfh = Lfb2(x)
    lgh = Lgb2(x)

    αh  = α2(h)
    
    A = sparse(zeros(6, 4))

    # CLF:
    A[1,1] = lgv[1]
    A[1,2] = lgv[2]
    A[1,3] = -1
    
    # CBF:
    A[2,1] = -lgh[1]
    A[2,2] = -lgh[2]
    A[2, 4] = -h
    
    # ||u|| < umax
    A[3,1] = 1.0
    A[3,2] = 1.0
    A[4,1] = 1.0
    A[4,2] = -1.0

    # δ>0
    A[5,3] = 1.0
    
    # k>0
    A[6, 4] = 1.0
    
    
    l = [-Inf; -Inf; -umax; -umax; 0; 0]
    u = [- kv - lfv; αh + lfh; umax; umax; Inf; Inf]
    
    
    return A, l, u
end

function updateConstrains!(x, A, l, u)
    
    kv = 0.1 * V(x)
    lfv = LfV(x)
    lgv = LgV(x)
    
    h = b2(x)
    lfh = Lfb2(x)
    lgh = Lgb2(x)
    αh  = α2(h)
    
    A[1,1] = lgv[1]
    A[1,2] = lgv[2]
    
    A[2,1] = -lgh[1]
    A[2,2] = -lgh[2]
    A[2, 4] = -h
    
    u[1] = -kv - lfv
    u[2] = αh + lfh
    
end

function updateConstrains!(x, controller)
    updateConstrains!(x, controller.A_con, controller.l_con, controller.u_con)
end


function feedback!(x, controller)

    # this is the feedback controller
    
    updateConstrains!(x, controller)
    OSQP.update!(controller.prob, Ax = controller.A_con.nzval, u=controller.u_con, l=controller.l_con)
    results = OSQP.solve!(controller.prob)
    
    if  (results.info.status != :Solved)
        println("OSQP did not solve fully!")
        @show x
        return (false, results.x[1:2])
    end

    return (true, results.x[1:2])
end




controller = setup_controller(x0)

x0 = [0.1, -0.01, 0,0, 0]

(suc, u) = feedback!(x0, controller)


function simulate(x0, t_max, dt, controller)
    # performs a simple euler step simulation
    
    t = 0.0
    
    # lazy way to initialize vector types
    tt = [t]
    xx = [x0]
    uu = [[0.0,0.0]]
    
    pop!(tt)
    pop!(xx)
    pop!(uu)
    
    
    while (t < t_max)
        

        (suc, u) = feedback!(x0, controller)
        
        if suc == false
            println("Failed at $(t)")
            break
        end        
        
        push!(tt, t)
        push!(xx, x0)
        push!(uu,u)

        # dynamics update
        x0 = x0 + (f(x0) + g(x0) * u) * dt
        t += dt
        
        if sum(abs2.(x0[1:2])) < (sc.rf)^2
            println("Completed : Successful Rendezvous!")
            break
        end

    end
    
    if (t>t_max)
        println("Completed: Reached t_max")
    end
    
    return (tt, xx, uu)
end
    

# use a short sim to pre-compile 
tt, xx, uu = simulate(x0, 1, 0.01, controller);

@time tt, xx, uu = simulate(x0, 300, 0.001, controller)

tt[end]

px = [x[1] for x in xx]
py = [x[2] for x in xx]
vx = [x[3] for x in xx]
vy = [x[4] for x in xx];
θθ = [x[5] for x in xx];

ux = [u[1] for u in uu];
uy = [u[2] for u in uu];

plot(tt, 1000*(sqrt.(px.^2 + py.^2)))
title!("Distance to Docking Port")
xlabel!("Time [sec]")
ylabel!("Distance [m]")
hline!([1000sc.rf])

plot(tt, 1000*(sqrt.(vx.^2 + vy.^2)))
title!("Relative Velocity (to origin)")
xlabel!("Time [sec]")
ylabel!("Velocity [m/s]")

hline([-1000umax, 1000umax], linestyle=:dash, color=:black, label="u_{Max}")
plot!(tt, 1000*ux, label="u_x")
plot!(tt, 1000*uy, label="u_y")
ylims!(-1500*umax, 1500*umax)
title!("Control inputs")
xlabel!("Time [sec]")
ylabel!("Force [N]")


umag = abs.(ux) + abs.(uy)
hline([1000*umax], linestyle=:dash, color=:black, label="u_{Max}")
plot!(tt, 1000umag, label="||u||_1")
title!("||u||_1")
xlabel!("Time [sec]")
ylabel!("Force [N]")


plot(tt, h.(xx))
hline!([0], linestyle=:dash, color=:black, label="h=0")
title!("Safety Constraint h")
xlabel!("Time [sec]")
ylabel!("h")

function γ(x)
    atan(x[2], x[1]) - x[5]
end
plot(tt[1:100:end], γ.(xx[1:100:end]) * 180/π, label="γ")
hline!([sc.γ, -sc.γ].*180/π,linestyle=:dash, color=:black, label="γ_{Max}")

xlabel!("Time [sec]")
ylabel!("γ [deg]")

@gif for i=1:100:length(tt)
    
    l = @layout [:a, :b]
    
    p1 = plot(px[1:i], py[1:i], aspect_ratio=:equal, legend=false)
    xlims!(0, 0.1)
    ylims!(-0.05, 0.05)
    plot!(x-> sc.rp*sin(θθ[i]) + (x-sc.rp*cos(θθ[i]))*tan(sc.γ + θθ[i]), 0, 0.1, linestyle=:dash, color=:red)
    plot!(x-> sc.rp*sin(θθ[i]) + (x-sc.rp*cos(θθ[i]))*tan(-sc.γ + θθ[i]), 0, 0.1, linestyle=:dash, color=:red)
    plot!(x-> sc.rp*sin(x), x-> sc.rp*cos(x), 0, 2π, linestyle=:dash, color=:green)
    xlabel!("x [km]")
    ylabel!("y [km]")
    
    p2 = plot(tt[1:i], sqrt.(ux.^2 + uy.^2)[1:i], ylim=(0,1.2umax), xlim=(0, tt[end]), legend=false)
    hline!([umax])
    
    
    xlabel!("time [sec]")
    ylabel!("||u||")
    
    plot(p1, p2)
    
end

using MeshCat
using GeometryBasics
using CoordinateTransformations
using Rotations

function initialize_vis(x0)

    vis = Visualizer()

    scale=100

    d0 = scale * sc.rp
    d1 = scale * sc.rf
    l = scale * 0.1


    cyl = Cylinder(Point(-d1,0,0), Point(d1,0,0), d0)
    los_material = MeshPhongMaterial(color=RGBA(1, 0, 1, 0.15))
    los = Cone(Point(d0 + l, 0 , 0), Point(d0,0,0), l * atan(sc.γ))


    sph = Cone(Point(-0.25,0.,0.), Point(0,0.,0.), 0.05)
    sph_material = MeshPhongMaterial(color=RGBA(0, 1, 0, 1.0))

    setobject!(vis["group1"]["cyl"], cyl)
    setobject!(vis["group1"]["los"], los, los_material)
    
    setobject!(vis["group2"]["sph"], sph, sph_material)

    
    settransform!(vis["group2"],Translation(Point(scale*x0[1], scale*x0[2], 0))∘LinearMap(AngleAxis(π, 0, 0, 1)))
    
    θ = x0[5]
    settransform!(vis["group1"], LinearMap(AngleAxis(θ, 0, 0,1)))
    
    settransform!(vis["/Cameras/default"], LinearMap(AngleAxis(0.8π + x0[5], 0, 0, 1)))
    setprop!(vis["/Cameras/default/rotated/<object>"], "zoom", 2)
    return vis
end 

function animate_vis(vis, tt, xx)
    
    N = 300 # number of frames wanted
    Nextend = 330
    scale = 100
    
    anim=MeshCat.Animation(4800)
    
    atframe(anim, 1) do
        setprop!(vis["/Cameras/default/rotated/<object>"], "zoom", 0.2)
    end
    
    for i=1:Nextend
        

        ii = min(1, i/N)
        # closest frame
        fr = Integer(floor(length(tt) * ii))
        
        x0 = xx[fr]
        
        px = scale*x0[1]
        py = scale*x0[2]
        
        θ = x0[5]
        
        atframe(anim, fr) do
            
            cam  = 1/(1+exp(-10*(ii-0.8)))
            
            γ = atan(x0[4], x0[3])
            
            settransform!(vis["group1"], LinearMap(AngleAxis(θ, 0, 0, 1)))
            settransform!(vis["group2"], Translation(Point(px, py, 0))∘LinearMap(AngleAxis(γ, 0, 0, 1)))
            settransform!(vis["/Cameras/default"], LinearMap(AngleAxis(0.8π + θ + π * cam, 0, 0, 1)))
            setprop!(vis["/Cameras/default/rotated/<object>"], "zoom", 2 + 2*(ii)^2)
        end
    end
    

    setanimation!(vis, anim)
end

vis2 = initialize_vis(x0)

render(vis2)
animate_vis(vis2, tt, xx)
render(vis2)




