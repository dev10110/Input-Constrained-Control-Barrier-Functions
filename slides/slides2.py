from manim import *
from manim_pptx import *
import numpy as np

titleKwargs = {'font_size': 36, 'include_underline':True, 'underline_buff': 0.125}

class TitleSlide(PPTXScene):
    def construct(self):
        title = Tex(r"Safe Control Synthesis via \\ Input Constrained \\ Control Barrier Functions")#, font_size=144)
        title.shift(0.5*UP)
        authors = Tex(r"Devansh Agrawal \& Dimitra Panagou \\ University of Michigan", font_size=36)
        authors.shift(1.5*DOWN)

        title_short = Title(r"Input Constrained Control Barrier Functions", **titleKwargs)

        self.play(
            Write(title),
            FadeIn(authors)
        )

        self.endSlide()

        blist = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea",
          "Formal Construction",
           "Simulation Results")

        
        blist2 = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea (ex. Adapative Cruise Control)",
          "Formal Construction",
           "Simulation Results (ex. Autonomous Rendezvous)")
        
        blist.align_to(blist2, LEFT).align_to(blist2, UP)
        
        self.play(
        Transform(title, title_short),
        FadeOut(authors),
        )


        self.play(FadeIn(blist))
        self.endSlide()

        self.play(FadeOut(blist), FadeIn(blist2))
        self.endSlide()
        
class BackgroundSlide_Genenral(PPTXScene):
  def construct(self):
    title = Title(r"Background and Problem Statement", **titleKwargs)
    self.add(title)

    scc = Tex(r"Safety Critical Controls")
    scc.shift(2* UP)

    doms = MathTex(r"(x &\in \mathcal{X} \subset \mathbb{R}^n) \\ (u &\in \mathcal{U} \subset \mathbb{R}^m)")
    doms.shift(4*RIGHT)

    affine = MathTex(r"{{\dot x = }}{{f(x) + g(x) u}}")

    safeSet = MathTex(r"\mathcal{S} = \{ x : h(x) \geq 0\} \subset \mathcal{X}")
    safeSet.shift(2*DOWN)

    qn = Tex(r"Which set of control inputs $u$ ensures system stays safe?")
    qn.shift(3*DOWN)
    qn.set_color(BLUE)

    self.play(Write(scc))
    self.endSlide()
    
    self.play(FadeIn(affine), FadeIn(doms), FadeIn(safeSet))
    self.play(Write(qn))
    self.endSlide()

class BackgroundSlide_CBFs(PPTXScene):
  def construct(self):
    title = Title(r"Background and Problem Statement", **titleKwargs)
    title2 = Title(r"Background: Control Barrier Functions", **titleKwargs)
    self.add(title)

    cite = Tex(r"[Ames, 2019]", font_size=26)
    cite.to_corner(DL)
    cite.shift(0.35*DOWN)
    self.add(cite)

    self.play(ReplacementTransform(title, title2))

    self.endSlide()

    ax = Axes(
            x_range=[0, 10, 2], y_range=[-1, 10, 2], axis_config={"include_tip": False},
            x_length=5,
            y_length=4,
        )
    ax.to_edge(LEFT)
    labels = ax.get_axis_labels(x_label="t", y_label="h")
    

    alpha = ValueTracker(0)
    offset = ValueTracker(0)

    def get_a(a):
      return np.cos(a)**2


    func = always_redraw(
        lambda: ax.plot(
          lambda t: 8.0 * np.exp(-get_a(alpha.get_value()) * t) - offset.get_value()*t, 
          x_range=[0,10],
          color=MAROON
        )
    )

    func_label = always_redraw(
      lambda: Tex(fr"$\alpha(r) = {get_a(alpha.get_value()):.2f}r$").next_to(ax, DOWN)
    )

    motivation = Tex(r"Let $\alpha \in \mathcal{K}$.\\",
    r"If $\forall x \in \mathcal{S}$, $\exists u \in \mathcal{U}$", r" such that \\",
    r"$\dot h(x, u) \geq - \alpha(h(x))$ \\", 
    r"then $h$ is a CBF for $\mathcal{S}$")
    
    
    # motivation.set_color_by_tex("\dot h", BLUE)
    # motivation.set_color_by_tex("If", MAROON)
    # motivation.set_color_by_tex("then", MAROON)

    motivation.shift(3*RIGHT + UP)

    conc = Tex(r"If $h$ is a CBF ", r"for $\mathcal{S}$,\\"
               r"any Lips. controller $\pi : \mathcal{S} \to \mathcal{U}$\\", 
               r" where $\dot h(x, \pi(x)) \geq -\alpha(h(x))$\\",
               r"ensures $\mathcal{S}$ is forward invariant")
    # conc.set_color_by_tex("\dot h", BLUE)
    # conc.set_color_by_tex("If", MAROON)
    # conc.set_color_by_tex("ensures", MAROON)
    conc.next_to(motivation, DOWN).shift(0.5*DOWN)


    self.play(FadeIn(motivation), Create(ax), FadeIn(func, func_label, labels))
    self.endSlide()

    self.play(FadeIn(conc))
    self.play(alpha.animate.set_value(3*np.pi), run_time = 5, rate_func=linear)

    self.endSlide()

    # self.play(motivation.animate.set_color(WHITE), conc.animate.set_color(WHITE))
    

    cons = MathTex(r"u \in \mathcal{U}")
    cons.next_to(func_label, DOWN)
    
    self.play(motivation.animate.set_color_by_tex("If", MAROON), FadeIn(cons))
    self.endSlide()

    self.play(offset.animate.set_value(0.2))
    self.endSlide()

class FormalProblemStatement(PPTXScene):
  def construct(self):
    title =  Title(r"Background", r"and ", r"Problem Statement", **titleKwargs)
    title2 = Title(r"Background", r": ",   r"Problem Statement", **titleKwargs)
    self.add(title)
    self.play(ReplacementTransform(title, title2))
    self.endSlide()    


    given = Tex(r"Given:")
    given.shift(2*UP + 5*LEFT)
    given.set_color(BLUE)
    givens = MathTex(r"\dot x &= f(x) + g(x) u\\  u &\in \mathcal{U} \\ \mathcal{S} &= \{ x : h(x) \geq 0\}")
    givens.align_to(given, UP)
    self.play(FadeIn(given), FadeIn(givens))


    find = Tex(r"Construct:", color=BLUE)
    find.shift(0.5*DOWN + 5*LEFT)
    finds = MathTex(r"\text{Inner Safe Set: } & \mathcal{C}^* \subset \mathcal{S} \\ \text{Safe Control Inputs: } & K_{ICCBF}(x)")
    finds.align_to(find, UP)

    self.play(FadeIn(find), FadeIn(finds))
    

    suchthat = Tex(r"Such that,", color=BLUE)
    suchthat.shift(2.25*DOWN + 5*LEFT)
    suchthats = Tex(r"Forward invariance of $\mathcal{C}^*$ \\ is guaranteed for any \\Lips. cont. controller $\pi(x) \in K_{ICCBF}(x)$")
    # suchthats.set_color_by_tex("Such that,", BLUE)
    suchthats.align_to(suchthat, UP)
    self.play(FadeIn(suchthat), FadeIn(suchthats))
    self.endSlide()

    otherRefs = VGroup(Tex(r"[Cortez 2020]", font_size=36), Tex(r"[Wu 2015]", font_size=36), Tex(r"[Breeden 2021]", font_size=36))
    otherRefs.arrange(DOWN, center=False, aligned_edge=LEFT)
    otherRefs.align_to(given, UP).to_edge(RIGHT)
    self.play(FadeIn(otherRefs))
    self.endSlide()


class MotivatingIdea_ACC(PPTXScene):
    def construct(self):
        title = Title("Example: Adaptive Cruise Control", **titleKwargs)
        self.add(title)
        
        car = ImageMobject("drawings/cars.png")
        # self.play(FadeIn(car))
        # self.endSlide()

        # car.generate_target()
        car.scale(0.6)
        car.shift(4*LEFT + UP)
        self.play(FadeIn(car))
        self.endSlide()


        dyn = MathTex(r"\frac{d}{dt}\begin{bmatrix}d\\ v\end{bmatrix} &= \begin{bmatrix}v_0 - v\\ -F(v)/m\end{bmatrix} + \begin{bmatrix}0\\g_0\end{bmatrix}u, \\", 
          r"|u| &\leq 0.25\\",
          r"\text{safe if } d &\geq 1.8 v\\",
          r"\therefore ", r"h(x) &= d - 1.8 v"
          )
        dyn.set_color_by_tex("0.25", BLUE)
        dyn.set_color_by_tex("h", RED)
        dyn.shift(3*RIGHT)

        cite = Tex(r"[Ames, 2019]", font_size=26)
        cite.to_corner(DL)
        cite.shift(0.35*DOWN)


        self.play(FadeIn(dyn, cite))
        self.endSlide()
        
        dyn2 =  MathTex(r"\dot x &= f(x) + g(x) u\\", 
          r"|u| &\leq 0.25\\",
          r"h(x) &= d - 1.8 v", font_size=48
          )
        
        dyn2.next_to(car, DOWN)
        
        self.play(TransformMatchingTex(dyn, dyn2))
        self.remove(dyn, cite)
        self.add(dyn2)
        
        s0 = ImageMobject("drawings/acc_sets_0.png")
        sopt = ImageMobject("drawings/acc_sets_opt.png")
        sfin = ImageMobject("drawings/acc_sets_opt_final.png")
        sgap = ImageMobject("drawings/acc_sets_opt_final_gap.png")
        for s in [s0, sopt, sfin, sgap]:
            s.width = 6
            s.shift(0.5*DOWN + 2*RIGHT)
            
        self.play(FadeIn(s0))
        self.endSlide()
        
        self.play(ReplacementTransform(s0, sopt))
        self.endSlide()
        
        self.play(ReplacementTransform(sopt, sfin))
        self.play(ReplacementTransform(sfin, sgap))
        
        self.endSlide()
        
        self.play(FadeOut(car, dyn2), ReplacementTransform(sgap, s0.to_edge(LEFT)))
        self.wait()
        self.endSlide()

class MotivatingIdea_Sets(PPTXScene):
    def construct(self):
        title = Title("Example: Adaptive Cruise Control", **titleKwargs)
        title_new = Title("Motivating Idea", **titleKwargs)
        self.add(title)

        s0 = ImageMobject("drawings/acc_sets_opt.png")
        s0.width = 6
        s0.shift(0.5*DOWN + 2*RIGHT)
        s0.to_edge(LEFT)
        self.add(s0)
        
        self.play(ReplacementTransform(title, title_new))
        self.endSlide()
        
        s1 = ImageMobject("drawings/sets_abstract.png")
        s1.width = 6
        s1.shift(0.5*DOWN + 2*RIGHT)
        s1.to_edge(LEFT)

        s2 = ImageMobject("drawings/sets_abstract_opt.png")
        s2.width = 6
        s2.shift(0.5*DOWN + 2 * RIGHT)
        s2.to_edge(LEFT)
        
        
        self.play(FadeOut(s0), FadeIn(s2))
        self.endSlide()
        self.play(FadeOut(s2), FadeIn(s1))
        self.play(s1.animate.shift(LEFT))
        self.endSlide()
        
        # choose a font size
        fs = 36
        
        b = MathTex(r"\text{Consider }b(x) &\triangleq \inf_{u \in \mathcal{U}} \dot h(x, u) + \alpha(h(x))\\",
                    r"\mathcal{C} &= \{ x : b(x) \geq 0 \}",
                   font_size=fs)
        b.shift(1.5*UP + 2*RIGHT)

        sC = ImageMobject("drawings/sets_abstract_C.png")
        sC.width = 6
        sC.shift(0.5*DOWN + 2*RIGHT)
        sC.to_edge(LEFT).shift(LEFT)
        
        
        self.play(FadeOut(s1), FadeIn(sC, b))
        self.endSlide()
        
        sC1 = ImageMobject("drawings/sets_abstract_C_p1.png")
        sC1.width = 6
        sC1.shift(0.5*DOWN + 2*RIGHT)
        sC1.to_edge(LEFT).shift(LEFT)
        
        usefulA1 = MathTex(r"\text{Useful Property 1: }", r"\text{If } x \in \partial S, \text{ and } \nexists \text{ safe } u\\", font_size=fs)
        usefulA2 = MathTex(r"h(x) = 0 \text{ and }  \dot h(x, u) < 0 \ \forall u \in \mathcal{U}", font_size=fs)
        usefulA3 = MathTex(r"h(x) = 0 \text{ and } \inf_{u \in \mathcal{U}} \dot h(x, u) < 0", font_size=fs)
        usefulA4 = MathTex(r"h(x) = 0 \text{ and } \inf_{u \in \mathcal{U}} \dot h(x, u) + \alpha(h(x))< 0", font_size=fs)
        usefulA5 = MathTex(r"h(x) = 0 \text{ and } b(x) < 0 ", font_size=fs)
        usefulA6 = MathTex(r"\therefore x \notin \mathcal{C}", font_size=fs)
        usefulA1.set_color_by_tex("Useful", BLUE)

        usefulA1.next_to(b, DOWN)
        usefulA2.next_to(usefulA1, DOWN)
        usefulA3.next_to(usefulA2, DOWN).align_to(usefulA2, LEFT)
        usefulA4.next_to(usefulA3, DOWN).align_to(usefulA2, LEFT)
        usefulA5.next_to(usefulA4, DOWN).align_to(usefulA2, LEFT)
        usefulA6.next_to(usefulA5, DOWN).align_to(usefulA2, LEFT)
        
        self.play(FadeOut(sC), FadeIn(sC1, usefulA1))
        self.endSlide()
        
        self.play(FadeIn(usefulA2))
        self.endSlide()
        
        self.play(FadeIn(usefulA3))
        self.endSlide()
        
        self.play(FadeIn(usefulA4))
        self.endSlide()

        self.play(FadeIn(usefulA5))
        self.endSlide()
        
        
        concA = Tex(r"$\therefore$ unsafe $\partial \mathcal{S}$ not in  $\mathcal{C}$", color=BLUE, font_size=fs)
        concA.next_to(usefulA6).shift(RIGHT)
        
        self.play(FadeIn(usefulA6, concA))
        self.endSlide()
        
        self.play(FadeOut(usefulA1, usefulA2, usefulA3, usefulA4, usefulA5, usefulA6, concA))
        
        
        sC2 = ImageMobject("drawings/sets_abstract_C_p2.png")
        sC2.width = 6
        sC2.shift(0.5*DOWN + 2*RIGHT)
        sC2.to_edge(LEFT).shift(LEFT)
        
        usefulB1 = MathTex(r"\text{Useful Property 2: }", r"\text{If }x \in \mathcal{C} \text{ and } x \in \partial S,\\", font_size=fs)
        usefulB2 = MathTex(r"b(x) \geq 0, \text{ and } h(x) = 0.\\", font_size=fs)
        usefulB3 = MathTex(r"b(x) = \inf_{u \in \mathcal{U}} \dot h(x, u)", 
                          r" + \alpha(h(x)) ", r"\geq 0\\", font_size=fs)
        usefulB4 = MathTex(r"\therefore & \forall u \in \mathcal{U}: \dot h(x, u) \geq 0", font_size=fs)
        usefulB1.set_color_by_tex("Useful", BLUE)

        usefulB1.next_to(b, DOWN)
        usefulB2.next_to(usefulB1, DOWN)
        usefulB3.next_to(usefulB2, DOWN).align_to(usefulB2, LEFT)
        usefulB4.next_to(usefulB3, DOWN)

        
        self.play(FadeOut(sC1), FadeIn(sC2, usefulB1))
        # self.endSlide()
        self.play(FadeIn(usefulB2))
        self.endSlide()
        self.play(FadeIn(usefulB3))
        self.endSlide()
        
        cross = Cross(usefulB3[1], stroke_color=RED, stroke_width=3)
        self.play(Create(cross))
        self.endSlide()
        
        self.play(FadeIn(usefulB4))
        self.endSlide()
        
        concB = Tex(r"If $u = \pi(x)$ keeps $x \in \mathcal{C}$,\\", r"then $\mathcal{S} \cap \mathcal{C}$ is forward invariant", color=BLUE, font_size=48)
        concB.next_to(usefulB4, DOWN).shift(0.25*DOWN)

        sSC = ImageMobject("drawings/sets_abstract_SC.png")
        sSC.width = 6
        sSC.shift(0.5*DOWN + 2*RIGHT)
        sSC.to_edge(LEFT).shift(LEFT)


        self.play(FadeIn(concB, sSC), FadeOut(sC2))
        self.endSlide()

class FormalConstruction(PPTXScene):
    def construct(self):
        title=Title("Formal Construction (Main Result)", **titleKwargs)
        self.play(FadeIn(title))
        self.endSlide()
        
        #### IMPORT SVG DRAWING and SET COLORS
        sets = SVGMobject("drawings/SandC_v6.svg", color=BLUE, fill_opacity=0.25, height=3.5)
        sets.to_edge(LEFT).shift(0.8*UP)
        fills = [BLUE, GREEN_E, GREEN_A, YELLOW]
        for i, s in enumerate(sets):    
            s.set_fill(fills[i], 0.25)
            s.set_stroke(fills[i])
        
        #### CREATE CAPTIONS FOR SVG
        Cs = MathTex(r"\mathcal{S} &= \{ x : h(x) \geq 0 \}\\",
                     r"\mathcal{C}_1 &= \{ x : b_1(x) \geq 0 \}\\",
                     r"& \ \ \cdots\\", 
                     r" \mathcal{C}_N &= \{ x : b_N(x) \geq 0 \}\\",
                     r"\mathcal{C}^* &= \mathcal{S} \cap \mathcal{C}_1 \cdots \cap \mathcal{C}_N",
                     font_size=36)
        Cs[0].set_color(fills[0])
        Cs[1].set_color(fills[1])
        Cs[3].set_color(fills[2])
        Cs[4].set_color(fills[3])
        Cs.next_to(sets, DOWN)
        boxC = SurroundingRectangle(Cs[4], color=ORANGE)
        
        #### DEFINE Bs
        bs = MathTex(r"b_0(x) &= h(x)\\",
        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot b_0(x, u) + \alpha_0 (b_0(x))\\",
        r"&\ \ \cdots\\",
        r"b_N(x) &= \inf_{u \in \mathcal{U}} \dot b_{N-1}(x, u) + \alpha_{N-1} (b_{N-1}(x))"
        , font_size=36)
        bs.to_edge(RIGHT).shift(0.5*LEFT)
        bs.align_to(sets, UP)
        
        bsexplain = MathTex(r"b_1(x)", r"&= \inf_{u \in \mathcal{U}} L_fb_0(x) + L_gb_0(x) u + \alpha_0 (b_0(x))\\",
                            r"&(b_i(x)\text{ does not depend on } u)", font_size=36)
        bsexplain.next_to(bs[1], DOWN).align_to(bs[1], LEFT)
        bsexplain[0].set_color(BLACK)
        
        
        #### START ANIMATIONS
        self.play(FadeIn(bs[0], Cs[0]),DrawBorderThenFill(sets[0]))
        self.endSlide()
        
        self.play(FadeIn(bs[1], Cs[1]),DrawBorderThenFill(sets[1]))
        self.endSlide()
        
        self.play(FadeIn(bsexplain))
        self.endSlide()
        
        self.play(FadeOut(bsexplain))
        
        self.play(FadeIn(bs[2], Cs[2]))
        
        self.play(FadeIn(bs[3], Cs[3]), DrawBorderThenFill(sets[2]))
        self.endSlide()
        
        self.play(FadeIn(Cs[4], boxC), DrawBorderThenFill(sets[3]))
        self.endSlide()
        
        #### BRING IN DEFINITION
        cond = MathTex(r"&\text{If } \exists \alpha_N \in \mathcal{K} \text{ s.t. }\forall x \in \mathcal{C}^*,\\", 
                       r"&\ \sup_{u \in \mathcal{U}} \dot b_N(x, u) + \alpha_N(b_N(x)) \geq 0\\",
                       r"&\text{then } b_N \text{ is an ICCBF.}", font_size=48)
        cond.next_to(bs, DOWN).shift(0.7*DOWN)
        boxCond = SurroundingRectangle(cond, color=ORANGE, buff=MED_LARGE_BUFF*0.5)
        condLab = Tex(r"Def:", font_size=36, color=ORANGE)
        condLab.next_to(boxCond, UP).align_to(boxCond, LEFT).shift(0.15*DOWN)
        
        condGroup = VGroup(cond, boxCond, condLab)
        
        self.play(FadeIn(condGroup))
        self.endSlide()
        
        self.play(FadeOut(bs, Cs, boxC), condGroup.animate.align_to(sets, UP).shift(0.0*DOWN))

        #### BRING IN THEOREM
        thm = Tex(r"If $b_N$ is an ICCBF, any Lips. controller $\pi$ s.t.\\", 
                 r"$\pi(x) \in \{ u \in \mathcal{U} : \dot b_N(x, u) + \alpha_N(b_N(x)) \geq 0 \}$\\",
                 r"renders $\mathcal{C}^* \subset \mathcal{S}$ forward invariant.")
        thm.to_edge(DOWN).shift(0.1*UP)
        thmBox = SurroundingRectangle(thm, color=BLUE, buff=MED_LARGE_BUFF*0.5)
        thmLab = Tex(r"Theorem:", font_size=36, color=BLUE)
        thmLab.next_to(thmBox, UP).align_to(thmBox, LEFT).shift(0.15*DOWN)

        thmGroup = VGroup(thm, thmBox, thmLab)
        self.play(FadeIn(thmGroup))
        self.endSlide()

class OutlineSlide_Sims(PPTXScene):
  def construct(self):

    title_short = Title(r"Input Constrained Control Barrier Functions", **titleKwargs)
    title_new = Title(r"Simulation Results", **titleKwargs)

    blist = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea",
          "Formal Construction",
           "Simulation Results")#, height=2, width=2)

    self.play(FadeIn(title_short, blist))

    def highlight(outline):
      outline.fade_all_but("Simulation Results")
      outline.set_color_by_tex("Simulation Results", BLUE)
      return outline
    
    self.play(
        ApplyFunction(highlight, blist)
      )

    self.endSlide()

    self.play(
      FadeOut(blist),
      Transform(title_short, title_new)
    ) 
    
    self.endSlide()

class SimulationResultsACCSetUp(PPTXScene):
  def construct(self):
    title = Title("Simulation Results", **titleKwargs)
    self.add(title)

    title2 = Title("Simulation Results: Adaptive Cruise Control", **titleKwargs)
    self.play(ReplacementTransform(title, title2)  )

    car = ImageMobject("drawings/cars.png")
    self.play(FadeIn(car))
    self.endSlide()

    # car.generate_target()
    # car.target.scale(0.6)
    # car.target.shift(4*LEFT +0.75* UP)
    

    # dyn = MathTex(r"\frac{d}{dt}\begin{bmatrix}d\\ v\end{bmatrix} &= \begin{bmatrix}v_0 - v\\ -F(v)/m\end{bmatrix} + \begin{bmatrix}0\\g_0\end{bmatrix}u, \\", 
    #   r"|u| &\leq 0.25\\"
    #   )
    # dyn.set_color_by_tex("0.25", BLUE)
    # dyn.shift(3*RIGHT + UP)
    
    # safety = MathTex(r"d &\geq 1.8 v\\ h(x) &= x_1 - 1.8 x_2 \geq 0", color=RED)
    # safety.next_to(dyn, DOWN)
    # safety.shift(0.5*DOWN)

    # annotations = VGroup(
    #   Tex(r"$d$: distance between cars", font_size=36),
    #   Tex(r"$v_0$: velocity of red car", font_size=36),
    #   Tex(r"$v$: velocity of blue car", font_size=36),
    #   Tex(r"$u$: acceleration of blue car (control input)", font_size=36),
    #   Tex(r"$F(v) = f_0 + f_1 v + f_2 v^2$: resistive forces on blue car", font_size=36),
    # )

    # cite = Tex(r"[Ames, 2019]", font_size=26)
    # cite.to_corner(DR)
    # cite.shift(0.35*DOWN)

    # annotations.arrange(DOWN, center=False, aligned_edge=LEFT)  
    # annotations.next_to(car.target, DOWN)
    # annotations.align_to(car.target,LEFT)

    # self.play(MoveToTarget(car), FadeIn(dyn, annotations, safety, cite))
    # self.endSlide()

class SimulationResultsACC_res1(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Adaptive Cruise Control", **titleKwargs)
        self.add(title)
        self.endSlide()
        cbf_standard = ImageMobject("drawings/acc_results_1.png")
        cbf_standard.width = 15
        cbf_standard.shift(DOWN)

        cite = Tex(r"[Ames, 2019]", font_size=26)
        cite.to_corner(DL)
        cite.shift(0.35*DOWN)

        qp = MathTex(r"&h(x) = x_1 - 1.8x_2\\ &\pi(x) = \operatorname{clip}[ \ \operatorname{argmin} ||u|| \text{ s.t. } L_fh(x) + L_gh(x) u + \alpha h(x) \geq 0 \ ]", font_size=32)
        qp.shift(2.25*UP).to_edge(LEFT).shift(RIGHT)


        desc = Tex(r"Applying clipped CLF-CBF-QP controller is not safe\\since $h(x)$ is not a valid CBF, with input constraints", color=BLUE)
        desc.shift(2.5*DOWN)
        
        self.play(FadeIn(qp, cite, cbf_standard))
        self.play(FadeIn(desc))
        self.endSlide()

class SimulationResultsACC_res2(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Adaptive Cruise Control", **titleKwargs)
        self.add(title)
        
        s1 = ImageMobject("drawings/acc_sets_1.png")
        s2 = ImageMobject("drawings/acc_sets_2.png")
        s3 = ImageMobject("drawings/acc_sets_3.png")
        s4 = ImageMobject("drawings/acc_sets_4.png")
        for s in [s1,s2,s3,s4]:
            s.width = 6
            s.shift(0.5*DOWN + 3*LEFT)
            
        self.add(s1)
        
        cond1 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\")
        
        cond1.next_to(s1, RIGHT)
        self.play(FadeIn(cond1))

        self.endSlide()
                
        cond2 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\", 
                        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot h + ",r"\alpha_0(h(x))\\",
                        r"&{}\quad\quad \quad (\alpha_0(r) = 4 r)")
        cond2.set_color_by_tex(r"4", BLUE)
        cond2.next_to(s2, RIGHT)
        self.play(TransformMatchingTex(cond1, cond2))
        self.play(FadeOut(s1), FadeIn(s2))
        self.endSlide()
        self.remove(cond1)
        self.add(cond2)
        
        
        cond3 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\", 
                        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot h + ", r"4h(x)\\",
                        r"b_2(x) &= \inf_{u \in \mathcal{U}} \dot b_1 + ", r"\alpha_1(b_1(x))\\",
                        r"&{}\quad\quad \quad (\alpha_1(r) = 7 \sqrt{r})")
        cond3.set_color_by_tex(r"7", BLUE)
        cond3.next_to(s3, RIGHT)
        self.play(TransformMatchingTex(cond2, cond3))
        self.play(FadeOut(s2), FadeIn(s3))

        self.endSlide()
        self.remove(cond2)
        self.add(cond3)
        
        
        cond4 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\", 
                        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot h + ", r"4h(x)\\",
                        r"b_2(x) &= \inf_{u \in \mathcal{U}} \dot b_1 + ", r"7\sqrt{b_1(x)}\\",
                        r"\mathcal{C}^* &= \mathcal{S} \cap \mathcal{C}_1 \cap \mathcal{C}_2")
        cond4.set_color_by_tex(r"\mathcal{C}", BLUE)
        cond4.next_to(s4, RIGHT).shift(0.5*UP)
        self.play(TransformMatchingTex(cond3, cond4))
        self.play(FadeOut(s3), FadeIn(s4))
        self.endSlide()
        self.remove(cond3)
        self.add(cond4)
        
        controller = MathTex(r"\text{Safe } u &: \dot b_2 + \alpha_2(b_2(x)) \geq 0\\&\quad \quad (\alpha_2(r) = 2 r)")
        controller.next_to(cond4, DOWN)

        self.play(FadeIn(controller))
        self.endSlide()
        
class SimulationResultsACC_res3(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Adaptive Cruise Control", **titleKwargs)
        self.add(title)
        
        cbf1 = ImageMobject("drawings/acc_results_1.png")
        cbf1.width = 15
        cbf1.shift(DOWN)
        self.add(cbf1)
        
        cbf2 = ImageMobject("drawings/acc_results_2.png")
        cbf2.width = 15
        cbf2.shift(DOWN)
        
        self.play(ReplacementTransform(cbf1, cbf2))
        
        
        desc = Tex(r"Using the ICCBF, the controller starts\\ braking earlier to maintain safety", color=BLUE)
        desc.shift(2.5*DOWN)
        
        self.play(FadeIn(desc))
        self.endSlide()

class SimulationResultsISS_1(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Docking", **titleKwargs)
        self.add(title)
        
        setup = ImageMobject("drawings/iss_setup.png")
        setup.width = 15
        self.play(FadeIn(setup))
        self.endSlide()
        

class OutlineSlide_Conclusion(PPTXScene):
    def construct(self):

        title_short = Title(r"Conclusions: Input Constrained Control Barrier Functions", **titleKwargs)

        self.add(title_short)

        blist = MathTex(
          r"\boldsymbol{\cdot} & \text{ Method to construct ICCBFs}\\",
          r"\boldsymbol{\cdot} &\text{ Simulation Results}\\",
          r"\boldsymbol{\cdot} &\text{ Remarks}\\",
          r"&\quad \boldsymbol{\cdot} \text{ Generalisation of Higher Order CBFs [Xiao, 2019]}\\",
          r"&\quad \boldsymbol{\cdot} \text{ Simple ICCBFs}\\",
          r"\boldsymbol{\cdot} & \text{ Future Directions}\\",
          r"&\quad \boldsymbol{\cdot} \text{ Noise, Robustness}\\",
          r"&\quad \boldsymbol{\cdot} \text{ Verification}",
          font_size=42
        )

        # for b in blist:
        #   self.play(FadeIn(b))
        #   self.endSlide()
        self.play(FadeIn(blist[0],blist[1]))
        self.endSlide()
        self.play(FadeIn(blist[2],blist[3],blist[4]))
        self.endSlide()
        self.play(FadeIn(blist[5],blist[6],blist[7]))
        self.endSlide()





class AppendixSlide(PPTXScene):
    def construct(self):

      title=Tex(r"Appendix")
      self.play(FadeIn(title))

      self.endSlide()



        
############# APPENDIX

class SimulationResultsISS_DETAILS(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Docking", **titleKwargs)
        self.add(title)
        
        setup = ImageMobject("drawings/iss_setup.png")
        setup.width = 15
        self.play(FadeIn(setup))
        self.endSlide()
        
        setup.generate_target()
        setup.target.scale(0.7).to_edge(DOWN).to_edge(LEFT).shift(DOWN + LEFT)
        
        self.play(MoveToTarget(setup))
        
        
        dyn = MathTex(
            r"\frac{d}{dt} \begin{bmatrix} p_x\\ p_y \\  v_x \\ v_y \\ \psi \end{bmatrix} = \begin{bmatrix}v_x \\v_y \\n^2 p_x + 2 n v_y + \frac{\mu}{r^2} - \frac{\mu(r+p_x)}{r_c^3}\\n^2 p_y - 2 n v_x - \frac{\mu p_y} {r_c^3}\\\omega\end{bmatrix} + \frac{1}{m_c}\begin{bmatrix}0 \\ 0 \\ u_x \\ u_y \\ 0\end{bmatrix}",
            font_size=36)
        dyn.shift(1.35*UP)
        
        cons = MathTex(r"|u_x| + |u_y| \leq 0.25\text{ kN}")
        cons.next_to(setup.target, RIGHT).shift(LEFT)
        
        safety = MathTex(r"h(x) = \cos \theta - \cos 10^\circ")
        safety.next_to(cons, DOWN)
        
        self.play(FadeIn(dyn, cons, safety))
        self.endSlide()
        
        

slides = [
    TitleSlide,
    BackgroundSlide_Genenral,
    BackgroundSlide_CBFs,
    FormalProblemStatement,
    MotivatingIdea_ACC,
    MotivatingIdea_Sets,
    FormalConstruction,
    # SimulationResultsACCSetUp,
    SimulationResultsACC_res1,
    SimulationResultsACC_res2,
    SimulationResultsACC_res3,
    OutlineSlide_Sims,
    SimulationResultsISS_1,
    OutlineSlide_Conclusion,
    AppendixSlide,
    SimulationResultsISS_DETAILS
]


class _Slides(*slides):
    
    def setup(self):
        for s in slides:
            s.setup(self)

    def construct(self):
        counter = 1

        for s in slides:
            # self.endSlide()
            pageNum = Tex(counter, font_size=24, fill_opacity=0.8)
            pageNum.to_edge(DOWN).to_edge(RIGHT).shift(0.25*DOWN)
            self.add(pageNum)
            counter += 1
            s.construct(self)

            if len(self.mobjects) >= 1:
                self.remove(*self.mobjects)
            
            