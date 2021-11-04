from manim import *
from manim_pptx import *

class TitleSlide(PPTXScene):
  def construct(self):
      title = Tex(r"Safe Control Synthesis via \\ Input Constrained \\ Control Barrier Functions")#, font_size=144)
      title.shift(0.5*UP)
      authors = Tex(r"Devansh Agrawal \& Dimitra Panagou \\ University of Michigan", font_size=36)
      authors.shift(1.5*DOWN)

      title_short = Title(r"Input Constrained Control Barrier Functions")

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

      self.play(
        Transform(title, title_short),
        FadeOut(authors),
      )
      

      self.play(FadeIn(blist))
      self.endSlide()

class OutlineSlide_Background(PPTXScene):
  def construct(self):

    title_short = Title(r"Input Constrained Control Barrier Functions")
    title_new = Title(r"Background and Problem Statement")

    blist = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea",
          "Formal Construction",
           "Simulation Results")

    self.add(title_short, blist)

    def highlight(outline):
      outline.fade_all_but("Background and Problem Statement")
      outline.set_color_by_tex("Background and Problem Statement", BLUE)
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

class BackgroundSlide_Genenral(PPTXScene):
  def construct(self):
    title = Title(r"Background and Problem Statement")
    self.add(title)

    scc = Tex(r"Safety Critical Controls")
    scc.shift(2* UP)


    xdot = MathTex(r"{{\dot x = }}{{f(x, u)}}")


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
    
    self.play(FadeIn(xdot), FadeIn(doms), FadeIn(safeSet))
    self.endSlide()

    self.play(TransformMatchingTex(xdot, affine))
    self.endSlide()

    self.play(Write(qn))
    self.endSlide()

class BackgroundSlide_CBFs(PPTXScene):
  def construct(self):
    title = Title(r"Background and Problem Statement")
    title2 = Title(r"Background: Control Barrier Functions")
    self.add(title)

    
    cite = Tex(r"[Ames, 2019]", font_size=26)
    cite.to_corner(DL)
    cite.shift(0.35*DOWN)
    self.add(cite)

    self.play(ReplacementTransform(title, title2))
    self.endSlide()    

    suppose = Tex(r"Suppose we have some function \\$h : [t_0, \infty) \to \mathbb{R}$", r" and $\alpha > 0$ such that")
    suppose.shift(1.2*UP)

    newSuppose = Tex(r"If $\exists$ a Lipscthiz continuous feedback controller\\$\pi : \mathcal{X} \to \mathcal{U}$", r" and $\alpha > 0$ such that")
    newSuppose.shift(1.2*UP)

    newSuppose2 = Tex(r"If $\exists$ a Lipscthiz continuous feedback controller\\$\pi : \mathcal{X} \to \mathcal{U}$", r" and class-$\mathcal{K}$ function $\alpha$ such that")
    newSuppose2.shift(1.2*UP)
    
    let  = MathTex(r"{{\frac{dh}{dt}}} {{\geq}} {{-\alpha h}} {{\quad \forall t \geq t_0}}")
    newLet2 = MathTex(r"{{\frac{dh}{dx}}} {{\dot x}} {{\geq}}{{-\alpha h(x)}} {{\quad \forall x \in \mathcal{S}}}")
    newLet3 = MathTex(r"{{\frac{dh}{dx}}} {{(f(x) + g(x) \pi(x))}} {{\geq}}{{-\alpha h(x)}} {{\quad \forall x \in \mathcal{S}}}")
    newLet4 = MathTex(r"{{L_fh(x) + L_gh(x)\pi(x)}} {{\geq}}{{-\alpha h(x)}} {{\quad \forall x \in \mathcal{S}}}")
    newLet5 = MathTex(r"{{L_fh(x) + L_gh(x)\pi(x)}} {{\geq}}{{-\alpha (h(x))}} {{\quad \forall x \in \mathcal{S}}}")

    then = Tex(r"Then $h(t) \geq h(t_0) e^{-\alpha (t-t_0)}$")
    then.shift(DOWN)

    newthen = Tex(r"Then $h(x(t)) \geq h(x(t_0)) e^{-\alpha (t-t_0)}$")
    newthen.shift(DOWN)
    
    ie = Tex(r"{{$\therefore$}} {{if $h(t_0) \geq 0$,}} {{then}}  {{$h(t) \geq 0 \quad \forall t \geq t_0$}}")
    ie.shift(2*DOWN)

    newie = Tex(r"{{$\therefore$}} {{if $x(t_0) \in \mathcal{S}$,}} {{then}} {{$x(t) \in \mathcal{S}$ for all $t \geq t_0$}}")
    newie.shift(2*DOWN)
    newie.set_color(BLUE)

    newie2 = Tex(r"{{$\therefore$}} {{if $x(t_0) \in \mathcal{S}$,}} {{then}} {{$x(t) \in \mathcal{S}$ for all $t \geq t_0$}}")
    newie2.shift(DOWN)
    newie2.set_color(BLUE)


    self.play(FadeIn(suppose))
    self.play(FadeIn(let))
    self.endSlide()

    self.play(FadeIn(then))
    self.play(FadeIn(ie))
    self.endSlide()


    self.play(FadeOut(suppose, shit=UP), FadeIn(newSuppose, shift=UP),
      let.animate.fade(), then.animate.fade(), ie.animate.fade())
    
    self.endSlide()

    self.play(FadeOut(let, shit=UP), FadeIn(newLet2, shift=UP))
    self.remove(let)
    self.add(newLet2)
    self.endSlide()

    self.play(TransformMatchingTex(newLet2, newLet3))
    self.remove(newLet2)
    self.add(newLet3)
    self.endSlide()
    
    self.play(TransformMatchingTex(newLet3, newLet4))
    self.remove(newLet3)
    self.add(newLet4)
    self.endSlide()

    self.play(ReplacementTransform(then, newthen))
    self.endSlide()

    self.play(TransformMatchingTex(ie, newie))
    self.remove(ie)
    self.add(newie)
    self.endSlide()

    
    self.play(TransformMatchingTex(newSuppose, newSuppose2), 
      newLet4.animate.fade(), newthen.animate.fade(), newie.animate.fade()
    )
    self.remove(newSuppose)
    self.add(newSuppose2)
    self.endSlide()

    self.play(TransformMatchingTex(newLet4, newLet5))
    
    self.play(FadeOut(newthen))
    self.play(TransformMatchingTex(newie, newie2))
    self.remove(newie)
    self.add(newie2)
    self.endSlide()

    settext = Tex(r"The set of safe control inputs at some state $x \in \mathcal{S}$ is")
    settext.shift(2*DOWN)
    set = MathTex(r"K_{CBF}(x) = \{ u \in \mathcal{U} : L_fh(x) + L_gh(x)u + \alpha(h(x)) \geq 0 \}")
    set.shift(3*DOWN)
    set.set_color(BLUE)

    self.play(FadeIn(settext), FadeIn(set))
    self.endSlide()

class FormalProblemStatement(PPTXScene):
  def construct(self):
    title =  Title(r"Background", r"and ", r"Problem Statement")
    title2 = Title(r"Background", r": ",   r"Problem Statement")
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


    ignores = Tex(r"Noise\\State Estimation", font_size=36)
    ignores.align_to(given, UP)
    ignores.shift(5*RIGHT + 0.5*DOWN)
    cross = Cross(ignores, stroke_color=RED, stroke_width=3)

    self.play(FadeIn(ignores))
    self.play(Create(cross))
    self.endSlide()
   
class OutlineSlide_Idea(PPTXScene):
  def construct(self):

    title_short = Title(r"Input Constrained Control Barrier Functions")
    title_new = Title(r"Motivating Idea")

    blist = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea",
          "Formal Construction",
           "Simulation Results")

    self.add(title_short, blist)

    def highlight(outline):
      outline.fade_all_but("Motivating Idea")
      outline.set_color_by_tex("Motivating Idea", BLUE)
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

class MotivatingIdea_1(PPTXScene):
  def construct(self):

    title =Title("Motivating Idea")
    self.add(title)
    title2= Title(r"Motivating Idea: Example")
    self.play(ReplacementTransform(title, title2))

    dynamics = MathTex(r"\dot x &= x + u\\ |u| &\leq 1")
    dynamics.shift(1.5*UP + 4*LEFT)
    safety = MathTex(r"\mathcal{S} &= \{ x : x \geq 2 \} \\ h(x) &= 2 - x \geq 0")
    safety.next_to(dynamics, DOWN)
    self.play(FadeIn(dynamics, safety))


    l = NumberLine(
            x_range=[-1, 3, 1],
            include_tip=True,
            include_numbers=True,
            length=8
        )
    l.shift(1.75*DOWN)

    barr= Line(l.n2p(2) + 0.25*DOWN, l.n2p(2) + 0.25*UP, color=BLUE)
    barr2= Line(l.n2p(1) + 0.25*DOWN, l.n2p(1) + 0.25*UP, color=BLUE)

    self.play(Create(l), Create(barr))
    


    l_safe1 = Line(l.n2p(-1), l.n2p(2), color=BLUE, stroke_width=6)
    l_unsafe1 = Line(l.n2p(2), l.n2p(3), color=RED, stroke_width=6)
    l_safe2 = Line(l.n2p(-1), l.n2p(1), color=BLUE, stroke_width=6)
    l_unsafe2 = Line(l.n2p(1), l.n2p(3), color=RED, stroke_width=6)

    self.play(FadeIn(l_safe1), FadeIn(l_unsafe1))
    self.endSlide()


    butwait = MathTex(r"{{\frac{dh}{dt} &= \frac{dh}{dx} \dot x\\}} {{&= -x - u \\}} {{\therefore \dot h &\leq -x +1 \\}} {{\therefore \text{ if } x > 1&, \quad \dot h < 0}}")
    butwait.shift(0.8*UP + 3*RIGHT)
    self.play(FadeIn(butwait))
    self.endSlide()

    self.play(ReplacementTransform(l_safe1, l_safe2), ReplacementTransform(l_unsafe1,l_unsafe2), ReplacementTransform(barr, barr2) )
    

    conc = Tex(r"The inner safe set is smaller than the safe set,\\ due to input constraints").set_color(BLUE)
    conc.shift(3*DOWN)
    self.play(FadeIn(conc))
    self.endSlide()

class MotivatingIdea_2(PPTXScene):
  def construct(self):

    title = Title("Motivating Idea")
    self.add(title)

    propose = Tex(r"Consider $b(x)$:", color=BLUE) 
    propose.shift(2.2*UP + 4*LEFT)
    b = MathTex(r"b(x) &\triangleq \inf_{u \in \mathcal{U}} \left [ L_fh(x) + L_gh(x) u + \alpha(h(x)) \right]\\ \mathcal{C} &= \{ x : b(x) \geq 0 \}")
    b.shift(UP)

    self.add(propose)
    self.play(FadeIn(b))
    

    useful = Tex(r"Useful property: ", color=BLUE)
    useful.shift(4*LEFT + 0.2*DOWN)

    self.add(useful)

    self.endSlide()

    propertyA = MathTex(r"x \in \partial S \cap \mathcal{C}", 
      r"&\implies h(x) = 0 \text{ and } b(x) \geq 0\\")

    propertyB = MathTex(r"x \in \partial S \cap \mathcal{C}", 
      r"&\implies h(x) = 0 \text{ and } b(x) \geq 0\\",
      r"&\implies \inf_{u \in \mathcal{U}} \left [ L_fh(x) + L_gh(x) u + \alpha(h(x)) \right] \geq 0\\")

    propertyC = MathTex(r"x \in \partial S \cap \mathcal{C}", 
      r"&\implies h(x) = 0 \text{ and } b(x) \geq 0\\",
      r"&\implies \inf_{u \in \mathcal{U}} \left [ L_fh(x) + L_gh(x) u + \alpha(h(x)) \right] \geq 0\\",
      r"&\implies \inf_{u \in \mathcal{U}} \left [ L_fh(x) + L_gh(x) u \right] \geq 0\\")

    property = MathTex(r"x \in \partial S \cap \mathcal{C}", 
      r"&\implies h(x) = 0 \text{ and } b(x) \geq 0\\",
      r"&\implies \inf_{u \in \mathcal{U}} \left [ L_fh(x) + L_gh(x) u + \alpha(h(x)) \right] \geq 0\\",
      r"&\implies \inf_{u \in \mathcal{U}} \left [ L_fh(x) + L_gh(x) u \right] \geq 0\\",
      r"&\implies L_fh(x) + L_gh(x) u \geq 0, \quad \forall u \in \mathcal{U}")
    property.shift(2*DOWN)

    for p in [propertyA, propertyB, propertyC]:
      p.align_to(property, UP)
    
    property2 = MathTex(r"x \in \partial S \cap \mathcal{C}", r"&\implies L_fh(x) + L_gh(x) u \geq 0, \quad \forall u \in \mathcal{U}")
    property2.shift(DOWN)


    # self.play(FadeIn(property))
    # animations = [FadeIn(p) for p in property]
    # self.play(AnimationGroup(*animations, lag_ratio=0.5))
    # self.endSlide()
    self.play(FadeIn(propertyA))
    self.endSlide()
    self.play(ReplacementTransform(propertyA, propertyB))
    self.endSlide()
    self.play(ReplacementTransform(propertyB, propertyC))
    self.endSlide()
    self.play(ReplacementTransform(propertyC, property))
    self.endSlide()

    self.play(TransformMatchingTex(property, property2))
    self.endSlide()

    conc = Tex(r"If $x \in \mathcal{S}$ and $ x \in \mathcal{C}$,\\",r"any $u$ that keeps $x \in \mathcal{C}$\\", r"will also keep $x \in \mathcal{S}$", color=BLUE)

    conc.shift(2.5*DOWN)
    self.play(FadeIn(conc))
    self.endSlide()

    qn = Tex(r"Now we need to find \\$u$ to keep $x \in \mathcal{C}$", color=RED)
    qn.align_to(conc, UP)
    qn.shift(3*RIGHT)
    self.play(conc.animate.shift(3*LEFT), FadeIn(qn))
    self.endSlide()

    sol = Tex(r"Repeat same steps as above!")
    sol.next_to(qn, DOWN)
    self.play(FadeIn(sol))
    self.endSlide()

class OutlineSlide_FormalConstruction(PPTXScene):
  def construct(self):

    title_short = Title(r"Input Constrained Control Barrier Functions")
    title_new = Title(r"Formal Construction")

    blist = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea",
          "Formal Construction",
           "Simulation Results")#, height=2, width=2)

    self.add(title_short, blist)

    def highlight(outline):
      outline.fade_all_but("Formal Construction")
      outline.set_color_by_tex("Formal Construction", BLUE)
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

class FormalConstruction(PPTXScene):
  def construct(self):
    title=Title("Formal Construction")
    title2=Title("Formal Construction: ICCBFs")
    self.add(title)
    self.play(ReplacementTransform(title, title2))
    

    bs = MathTex(r"b_0(x) &= h(x)\\",
    r"b_1(x) &= \inf_{u \in \mathcal{U}} {{L_fb_0}}{{(x)}} + {{L_gb_0}}{{(x)}}{{u + }}{{\alpha_0(b_0}}{{(x)}}{{)}}\\", 
    r"&\vdots\\",
    r"b_N(x) &= \inf_{u \in \mathcal{U}} {{L_fb_{N-1}}}{{(x)}}{{ + }}{{L_gb_{N-1}}}{{(x)}}{{ u + }}{{\alpha_{N-1}(b_{N-1}}}{{(x)}}{{)}}"
    , font_size=36)
    bs.shift(2*LEFT)

    bsNoX = MathTex(r"b_0(x) &= h(x)\\",
    r"b_1(x) &= \inf_{u \in \mathcal{U}} {{L_fb_0}} + {{L_gb_0}}{{u + }}{{\alpha_0(b_0}}{{)}}\\", 
    r"&\vdots\\",
    r"b_N(x) &= \inf_{u \in \mathcal{U}} {{L_fb_{N-1}}}{{ + }}{{L_gb_{N-1}}}{{ u + }}{{\alpha_{N-1}(b_{N-1}}}{{)}}"
    , font_size=36)
    # bsNoX.shift(2*LEFT)
    bsNoX.align_to(bs, LEFT)


    cs = MathTex(r"\mathcal{S} = \mathcal{C}_0 &= \{x : b_0(x) \geq 0\}\\",
    r"\mathcal{C}_1 &= \{x : b_1(x) \geq 0\}\\",
    r"&\vdots\\",
    r"\mathcal{C}_N &= \{x : b_N(x) \geq 0\}\\",
    r"\mathcal{C}^* &= \mathcal{C}_0 \cap \mathcal{C}_1 \cap \cdots \cap \mathcal{C}_N"
    , font_size=36
    )
    cs.set_color_by_tex("\mathcal{C}^*", BLUE)
    cs.next_to(bsNoX, 0.5*RIGHT)
    cs.align_to(bs, UP)

    self.play(FadeIn(bs))
    self.endSlide()

    self.play(TransformMatchingTex(bs, bsNoX))
    self.remove(bs)
    self.add(bsNoX)
    self.endSlide()

    self.play(FadeIn(cs))
    self.endSlide()

    self.play(bsNoX.animate.shift(1.1*UP), cs.animate.shift(1.1*UP))
    self.endSlide()

    defLabel = Tex(r"\textbf{Defn:}", font_size=36)
    defLabel.shift(0.9*DOWN)
    definition =VGroup()
    d1 = Tex(r"If ",r"$\exists \alpha_N \in \mathcal{K}$ s.t. ", r"$\sup_{u\in \mathcal{U}} L_fb_N + L_gb_N u + \alpha_N(b_N) \geq 0 \ \forall x \in \mathcal{C}^*$, \\", font_size=36)
    # d1.set_color_by_tex("If", BLUE)
    definition += d1

    d2 = Tex(r"then $b_N$ is an \textbf{Input Constrained CBF}", font_size=36)
    # d2.set_color_by_tex("b_N", BLUE)
    definition += d2
    
    definition.arrange(DOWN, center=False, aligned_edge=LEFT)

    defLabel.to_edge(LEFT)

    definition.next_to(defLabel, RIGHT)
    definition.align_to(defLabel, UP)
    

    theoremLabel = Tex(r"\textbf{Thm:}", font_size=36)
    
    theorem = VGroup()
    t1 = Tex(r"If $b_N$ is an ICCBF, then", r" any Lips. cont. controller where", font_size=36)
    t1.set_color_by_tex("If", ORANGE)
    theorem += t1

    theorem += Tex(r"$\pi(x) \in K_{ICCBF}(x) = \{ u \in \mathcal{U} : L_fb_N + L_gb_N u + \alpha_N(b_N) \geq 0 \}$,", font_size=36, color=BLUE)
    t2 = Tex(r"will render $\mathcal{C}^*$ forward invariant.", font_size=36)
    t2.set_color_by_tex("forward", ORANGE)
    theorem += t2
    theorem.arrange(DOWN, center=False, aligned_edge=LEFT)
    
    theorem.next_to(definition, DOWN)
    theoremLabel.to_edge(LEFT)
    
    theorem.align_to(definition,LEFT)
    theoremLabel.align_to(theorem, UP)
 
    self.play(FadeIn(defLabel), FadeIn(definition))
    self.endSlide()

    
    self.play(FadeIn(theoremLabel), FadeIn(theorem))
    self.endSlide()

class FormalConstructionRemarks(PPTXScene):
  def construct(self):
    title=Title("Formal Construction: Remarks")
    self.add(title)

    defLabel = Tex(r"\textbf{Defn:}", font_size=36)
    defLabel.to_edge(UP)
    defLabel.shift(DOWN)
    definition =VGroup()
    d1 = Tex(r"If ",r"$\exists \alpha_N \in \mathcal{K}$ s.t. ", r"$\sup_{u\in \mathcal{U}} L_fb_N + L_gb_N u + \alpha_N(b_N) \geq 0 \ \forall x \in \mathcal{C}^*$, \\", font_size=36)
    definition += d1
    d2 = Tex(r"then $b_N$ is an \textbf{Input Constrained CBF}", font_size=36)
    definition += d2
    
    definition.arrange(DOWN, center=False, aligned_edge=LEFT)
    defLabel.to_edge(LEFT)
    definition.next_to(defLabel, RIGHT)
    definition.align_to(defLabel, UP)

    theoremLabel = Tex(r"\textbf{Thm:}", font_size=36)
    
    theorem = VGroup()
    t1 = Tex(r"If $b_N$ is an ICCBF, then", r" any Lips. cont. controller where", font_size=36)
    # t1.set_color_by_tex("If", ORANGE)
    theorem += t1

    theorem += Tex(r"$\pi(x) \in K_{ICCBF}(x) = \{ u \in \mathcal{U} : L_fb_N + L_gb_N u + \alpha_N(b_N) \geq 0 \}$,", font_size=36)
    t2 = Tex(r"will render $\mathcal{C}^*$ forward invariant.", font_size=36)
    # t2.set_color_by_tex("forward", ORANGE)
    theorem += t2
    theorem.arrange(DOWN, center=False, aligned_edge=LEFT)
    
    theorem.next_to(definition, DOWN)
    theoremLabel.to_edge(LEFT)
    
    theorem.align_to(definition,LEFT)
    theoremLabel.align_to(theorem, UP)
 
    self.add(defLabel, definition)
    self.add(theoremLabel, theorem)
    self.endSlide()

    qn = Tex(r"1: How to verify if $b_N$ is an ICCBF?\\", font_size=36)
    sol =Tex(r"Either analytically or (approx.) numerically, eg:", font_size=36)
    qn.set_color_by_tex("verify", BLUE)
    qn.shift(1.1*DOWN + 3*LEFT)
    sol.next_to(qn, DOWN)
    sol.align_to(qn,LEFT)
    sol.shift(RIGHT)
    
    numSol = MathTex(r"&\gamma = \underset{x \in \mathcal{C}^*}{\text{minimize}}  \ \sup_{u\in\mathcal{U}} [L_fb_N + L_gb_N u + \alpha_N(b_N)]\\", r"&\gamma \geq 0 \implies b_N \text{ is ICCBF}", font_size=36)
    numSol.next_to(sol, DOWN)
    numSol.align_to(sol,LEFT)
    
    self.play(FadeIn(qn))
    self.play(FadeIn(sol), FadeIn(numSol))
    
    self.endSlide()

    self.remove(sol, numSol)

    hocbf = Tex(r"2: ICCBFs are a generalisation of Higher Order CBFs", font_size=36, color=BLUE)
    simple = Tex(r"3: Simple ICCBFs implies $K_{ICCBF}(x) = \mathcal{U}$", font_size=36, color=BLUE)
    hocbf.next_to(qn, DOWN)
    hocbf.align_to(qn,LEFT)
    simple.next_to(hocbf, DOWN)
    simple.align_to(hocbf,LEFT)

    self.play(FadeIn(hocbf))
    self.endSlide()

    bs = MathTex(r"b_0(x) &= h(x)\\",
    r"{{b_1(x) &=}} \inf_{u \in \mathcal{U}} {{L_fb_0}}{{(x)}} + {{L_gb_0}}{{(x)}}{{u + }}{{\alpha_0(b_0}}{{(x)}}{{)}}\\", font_size=36)
    bs2 = MathTex(r"b_0(x) &= h(x)\\",
    r"{{b_1(x) &=}} \inf_{u \in \mathcal{U}} {{L_fb_0}}{{(x)}} + {{\alpha_0(b_0}}{{(x)}}{{)}}\\", font_size=36)
    bs3 = MathTex(r"b_0(x) &= h(x)\\",
    r"{{b_1(x) &=}} {{L_fb_0}}{{(x)}} + {{\alpha_0(b_0}}{{(x)}}{{)}}\\", font_size=36)
    bs.next_to(hocbf, DOWN)
    bs.align_to(hocbf,LEFT)
    bs.shift(RIGHT)
    bs2.align_to(bs, UP)
    bs2.align_to(bs, LEFT)
    bs3.align_to(bs2, UP)
    bs3.align_to(bs2, LEFT)

    self.play(FadeIn(bs))
    self.endSlide()
    
    self.play(TransformMatchingTex(bs, bs2))
    self.endSlide()

    self.remove(bs)
    self.add(bs2)
    self.play(ReplacementTransform(bs2, bs3))
    self.endSlide()

    self.remove(bs2)
    self.add(bs3)
    self.endSlide()

    self.remove(bs3)
    self.play(FadeIn(simple))
    self.endSlide()

class OutlineSlide_Sims(PPTXScene):
  def construct(self):

    title_short = Title(r"Input Constrained Control Barrier Functions")
    title_new = Title(r"Simulation Results")

    blist = BulletedList(
        "Background and Problem Statement",
         "Motivating Idea",
          "Formal Construction",
           "Simulation Results")#, height=2, width=2)

    self.add(title_short, blist)

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
    title = Title("Simulation Results")
    self.add(title)

    title2 = Title("Simulation Results: Adaptive Cruise Control")
    self.play(ReplacementTransform(title, title2)  )



    car = ImageMobject("drawings/cars.png")
    self.play(FadeIn(car))
    self.endSlide()

    car.generate_target()
    car.target.scale(0.6)
    car.target.shift(4*LEFT +0.75* UP)
    

    dyn = MathTex(r"\frac{d}{dt}\begin{bmatrix}d\\ v\end{bmatrix} &= \begin{bmatrix}v_0 - v\\ -F(v)/m\end{bmatrix} + \begin{bmatrix}0\\g_0\end{bmatrix}u, \\", 
      r"|u| &\leq 0.25\\"
      )
    dyn.set_color_by_tex("0.25", BLUE)
    dyn.shift(3*RIGHT + UP)
    
    safety = MathTex(r"d &\geq 1.8 v\\ h(x) &= x_1 - 1.8 x_2 \geq 0", color=RED)
    safety.next_to(dyn, DOWN)
    safety.shift(0.5*DOWN)

    annotations = VGroup(
      Tex(r"$d$: distance between cars", font_size=36),
      Tex(r"$v_0$: velocity of red car", font_size=36),
      Tex(r"$v$: velocity of blue car", font_size=36),
      Tex(r"$u$: acceleration of blue car (control input)", font_size=36),
      Tex(r"$F(v) = f_0 + f_1 v + f_2 v^2$: resistive forces on blue car", font_size=36),
    )

    cite = Tex(r"[Ames, 2019]", font_size=26)
    cite.to_corner(DR)
    cite.shift(0.35*DOWN)

    annotations.arrange(DOWN, center=False, aligned_edge=LEFT)  
    annotations.next_to(car.target, DOWN)
    annotations.align_to(car.target,LEFT)

    self.play(MoveToTarget(car), FadeIn(dyn, annotations, safety, cite))
    self.endSlide()

class SimulationResultsACC_res1(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Adaptive Cruise Control")
        self.add(title)

        cbf_standard = ImageMobject("drawings/acc_results_1.png")
        cbf_standard.width = 15
        cbf_standard.shift(DOWN)
        
        desc = Tex(r"Applying clipped CLF-CBF-QP controller is not safe\\since $h(x)$ is not a valid CBF, with input constraints", color=BLUE)
        desc.shift(2.5*DOWN)
        
        self.play(FadeIn(cbf_standard))
        self.play(FadeIn(desc))
        self.endSlide()

class SimulationResultsACC_res2(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Adaptive Cruise Control")
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
        self.add(cond1)
        self.endSlide()
                
        cond2 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\", 
                        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot h + ",r"\alpha_0(h(x))\\",
                        r"&{}\quad\quad \quad (\alpha_0(r) = 4 r)")
        cond2.set_color_by_tex(r"4", BLUE)
        cond2.next_to(s2, RIGHT)
        self.play(TransformMatchingTex(cond1, cond2))
        self.remove(cond1)
        self.add(cond2)
        self.endSlide()
        
        self.play(FadeOut(s1), FadeIn(s2))
        self.endSlide()
        
        
        cond3 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\", 
                        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot h + ", r"4h(x)\\",
                        r"b_2(x) &= \inf_{u \in \mathcal{U}} \dot b_1 + ", r"\alpha_1(b_1(x))\\",
                        r"&{}\quad\quad \quad (\alpha_1(r) = 7 \sqrt{r})")
        cond3.set_color_by_tex(r"7", BLUE)
        cond3.next_to(s3, RIGHT)
        self.play(TransformMatchingTex(cond2, cond3))
        self.remove(cond2)
        self.add(cond3)
        self.endSlide()
        
        self.play(FadeOut(s2), FadeIn(s3))
        self.endSlide()
        
        
        cond4 = MathTex(r"h(x) &= x_1 - 1.8 x_2\\", 
                        r"b_1(x) &= \inf_{u \in \mathcal{U}} \dot h + ", r"4h(x)\\",
                        r"b_2(x) &= \inf_{u \in \mathcal{U}} \dot b_1 + ", r"7\sqrt{b_1(x)}\\",
                        r"\mathcal{C}^* &= \mathcal{S} \cap \mathcal{C}_1 \cap \mathcal{C}_2")
        cond4.set_color_by_tex(r"\mathcal{C}", BLUE)
        cond4.next_to(s4, RIGHT).shift(0.5*UP)
        self.play(TransformMatchingTex(cond3, cond4))
        self.remove(cond3)
        self.add(cond4)
        self.endSlide()
        
        self.play(FadeOut(s3), FadeIn(s4))
        self.endSlide()
        
        controller = MathTex(r"\text{Safe } u &: \dot b_2 + \alpha_2(b_2(x)) \geq 0\\&\quad \quad (\alpha_2(r) = 2 r)")
        controller.next_to(cond4, DOWN)

        self.play(FadeIn(controller))
        self.endSlide()
        
class SimulationResultsACC_res3(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Adaptive Cruise Control")
        self.add(title)
        
        cbf1 = ImageMobject("drawings/acc_results_1.png")
        cbf1.width = 15
        cbf1.shift(DOWN)
        self.add(cbf1)
        
        cbf2 = ImageMobject("drawings/acc_results_2.png")
        cbf2.width = 15
        cbf2.shift(DOWN)
        
        self.play(ReplacementTransform(cbf1, cbf2))
        self.endSlide()
        
        
        desc = Tex(r"Using the ICCBF, the controller starts\\ braking earlier to maintain safety", color=BLUE)
        desc.shift(2.5*DOWN)
        
        self.play(FadeIn(desc))
        self.endSlide()

class SimulationResultsISS_1(PPTXScene):
    def construct(self):
        title = Title("Simulation Results: Docking")
        self.add(title)
        
        setup = ImageMobject("drawings/iss_setup.png")
        setup.width = 15
        self.play(FadeIn(setup))
        self.endSlide()
        
        setup.generate_target()
        setup.target.scale(0.7).to_edge(DOWN).to_edge(LEFT).shift(DOWN + LEFT)
        
        self.play(MoveToTarget(setup))
        self.endSlide()
        
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

class OutlineSlide_Conclusion(PPTXScene):
    def construct(self):

        title_short = Title(r"Input Constrained Control Barrier Functions")

        blist = BulletedList(
            "Background and Problem Statement",
             "Motivating Idea",
              "Formal Construction",
               "Simulation Results")

        self.play(FadeIn(title_short, blist))
        self.endSlide()
        
        bsNoX = MathTex(r"b_0(x) &= h(x)\\",
            r"b_1(x) &= \inf_{u \in \mathcal{U}} {{L_fb_0}} + {{L_gb_0}}{{u + }}{{\alpha_0(b_0}}{{)}}\\", 
            r"&\vdots\\",
            r"b_N(x) &= \inf_{u \in \mathcal{U}} {{L_fb_{N-1}}}{{ + }}{{L_gb_{N-1}}}{{ u + }}{{\alpha_{N-1}(b_{N-1}}}{{)}}"
            , font_size=36)
        bsNoX.shift(1*UP + 2.5*LEFT)    
        self.play(FadeOut(blist), FadeIn(bsNoX))
        self.endSlide()
        
        
        diagram = ImageMobject("drawings/conclusion.png")
        diagram.width = 8
        diagram.to_edge(DOWN).shift(2*RIGHT)
        self.play(FadeIn(diagram))
        self.endSlide()
        
        
        

slides = [
    TitleSlide,
    OutlineSlide_Background,
    BackgroundSlide_Genenral,
    BackgroundSlide_CBFs,
    FormalProblemStatement,
    OutlineSlide_Idea,
    MotivatingIdea_1,
    MotivatingIdea_2,
    # OutlineSlide_FormalConstruction,
    # FormalConstruction,
    # FormalConstructionRemarks,
    # OutlineSlide_Sims,
    # SimulationResultsACCSetUp,
    # SimulationResultsACC_res1,
    # SimulationResultsACC_res2,
    # SimulationResultsACC_res3,
    # SimulationResultsISS_1,
    # OutlineSlide_Conclusion,
]


class Together(*slides):
    
    def setup(self):
        for s in slides:
            s.setup(self)

    def construct(self):
        for s in slides:
            s.construct(self)
            
            if len(self.mobjects) >= 1:
                self.remove(*self.mobjects)
            