from tkinter import Tk, Label, Entry, Button, PhotoImage, IntVar, Canvas, StringVar, ttk
import random
import os


def main():
    def restart(end_canva):
        end_canva.destroy()
        main()

    let_num = IntVar()
    errors = IntVar()
    errors.set(1)
    if errors.get() > 11:
        errors.set(0)
    canva = Canvas(root, width=500, height=500, bg="#edf5e1")
    file = open("words.txt", "r")
    words = file.readlines()
    file.close()
    firs_img = PhotoImage(file="1.png")
    first_img_label = Label(root, image=firs_img, bg="#edf5e1")
    first_img_label.image = firs_img
    canva.create_window(250, 100, window=first_img_label)
    while True:
        right_word = random.choice(words).replace("\n", "").lower()
        if len(right_word) > 4:
            break

    word = []
    right_list = []
    ind = 0
    for char in right_word:
        word.append("_")
        right_list.append(char)
        ind += 1
    word_label = Label(
        root, text="   ".join(word), font=("Mistral", 14), width=500, bg="#edf5e1"
    )
    canva.create_window((250, 250), window=word_label)

    def game_ended(text):
        canva.destroy()
        end_canva = Canvas(root, width=500, height=500, bg="#edf5e1")
        play_again = PhotoImage(
            file="play_again.png"
        )
        if text == f"YOU LOST!\nTHE RIGHT WORD WAS {right_word.upper()}":
            hanged = PhotoImage(file="11.png")
            hanged_label = Label(root, image=hanged)
            hanged_label.image = hanged
            end_canva.create_window(250, 100, window=hanged_label)
        quit_game = PhotoImage(
            file="quit_game.png"
        )
        button = Button(
            root,
            image=play_again,
            command=lambda: restart(end_canva),
            border=0,
            activebackground="#edf5e1",
            bg="#edf5e1",
        )
        button.image = play_again
        close_button = Button(
            root,
            image=quit_game,
            command=root.destroy,
            activebackground="#edf5e1",
            bg="#edf5e1",
            border=0,
        )
        close_button.image = quit_game

        end_canva.create_window(180, 300, window=button)
        end_canva.create_window(330, 300, window=close_button)
        end_label = Label(root, bg="#edf5e1", text=text, font=("Mistral", 14),)
        end_canva.create_window(250, 200, window=end_label)
        end_canva.grid()

    def check(letter, button):
        is_in = False
        button.destroy()

        for index in range(len(right_list)):
            if letter == right_list[index]:
                word[index] = letter.upper()
                is_in = True
                let_num.set(let_num.get() + 1)
        word_label = Label(
            root, text="   ".join(word), font=("Mistral", 14), bg="#edf5e1", width=500
        )
        canva.create_window((250, 250), window=word_label)

        if not is_in:

            errors_value = StringVar()
            errors_value.set(errors.get() + 1)
            path = errors_value + ".png"
            
            errors.set(errors.get() + 1)
            img = PhotoImage(file=path)
            img_label = Label(root, image=img, bg="#edf5e1")
            img_label.image = img
            canva.create_window(250, 100, window=img_label)

        if errors.get() == 11:
            game_ended(f"YOU LOST!\nTHE RIGHT WORD WAS {right_word.upper()}")

        if let_num.get() == len(right_list):
            game_ended("YOU WON!")

    a = PhotoImage(file="a.png")
    b = PhotoImage(file="b.png")
    c = PhotoImage(file="c.png")
    d = PhotoImage(file="d.png")
    e = PhotoImage(file="e.png")
    f = PhotoImage(file="f.png")
    g = PhotoImage(file="g.png")
    h = PhotoImage(file="h.png")
    i = PhotoImage(file="i.png")
    j = PhotoImage(file="j.png")
    k = PhotoImage(file="k.png")
    l = PhotoImage(file="l.png")
    m = PhotoImage(file="m.png")
    n = PhotoImage(file="n.png")
    o = PhotoImage(file="o.png")
    p = PhotoImage(file="p.png")
    q = PhotoImage(file="q.png")
    r = PhotoImage(file="r.png")
    s = PhotoImage(file="s.png")
    t = PhotoImage(file="t.png")
    u = PhotoImage(file="u.png")
    v = PhotoImage(file="v.png")
    w = PhotoImage(file="w.png")
    x = PhotoImage(file="x.png")
    y = PhotoImage(file="y.png")
    z = PhotoImage(file="z.png")

    a_button = Button(
        root, command=lambda: check("a", a_button), image=a, border=0, bg="#edf5e1"
    )
    a_button.image = a

    b_button = Button(
        root,
        command=lambda: check("b", b_button),
        image=b,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    b_button.image = b
    c_button = Button(
        root,
        command=lambda: check("c", c_button),
        image=c,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    c_button.image = c
    d_button = Button(
        root,
        command=lambda: check("d", d_button),
        image=d,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    d_button.image = d
    e_button = Button(
        root,
        command=lambda: check("e", e_button),
        image=e,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    e_button.image = e
    f_button = Button(
        root,
        command=lambda: check("f", f_button),
        image=f,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    f_button.image = f
    g_button = Button(
        root,
        command=lambda: check("g", g_button),
        image=g,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    g_button.image = g
    h_button = Button(
        root,
        command=lambda: check("h", h_button),
        image=h,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    h_button.image = h
    i_button = Button(
        root,
        command=lambda: check("i", i_button),
        image=i,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    i_button.image = i
    j_button = Button(
        root,
        command=lambda: check("j", j_button),
        image=j,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    j_button.image = j
    k_button = Button(
        root,
        command=lambda: check("k", k_button),
        image=k,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    k_button.image = k
    l_button = Button(
        root,
        command=lambda: check("l", l_button),
        image=l,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    l_button.image = l
    m_button = Button(
        root,
        command=lambda: check("m", m_button),
        image=m,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    m_button.image = m
    n_button = Button(
        root,
        command=lambda: check("n", n_button),
        image=n,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    n_button.image = n
    o_button = Button(
        root,
        command=lambda: check("o", o_button),
        image=o,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    o_button.image = o
    p_button = Button(
        root,
        command=lambda: check("p", p_button),
        image=p,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    p_button.image = p
    q_button = Button(
        root,
        command=lambda: check("q", q_button),
        image=q,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    q_button.image = q
    r_button = Button(
        root,
        command=lambda: check("r", r_button),
        image=r,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    r_button.image = r
    s_button = Button(
        root,
        command=lambda: check("s", s_button),
        image=s,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    s_button.image = s
    t_button = Button(
        root,
        command=lambda: check("t", t_button),
        image=t,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    t_button.image = t
    u_button = Button(
        root,
        command=lambda: check("u", u_button),
        image=u,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    u_button.image = u
    v_button = Button(
        root,
        command=lambda: check("v", v_button),
        image=v,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    v_button.image = v
    w_button = Button(
        root,
        command=lambda: check("w", w_button),
        image=w,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    w_button.image = w
    x_button = Button(
        root,
        command=lambda: check("x", x_button),
        image=x,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    x_button.image = x
    y_button = Button(
        root,
        command=lambda: check("y", y_button),
        image=y,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    y_button.image = y
    z_button = Button(
        root,
        command=lambda: check("z", z_button),
        image=z,
        border=0,
        bg="#edf5e1",
        activebackground="#edf5e1",
    )
    z_button.image = z

    canva.create_window(115, 300, window=a_button)
    canva.create_window(145, 300, window=b_button)
    canva.create_window(175, 300, window=c_button)
    canva.create_window(205, 300, window=d_button)
    canva.create_window(235, 300, window=e_button)
    canva.create_window(265, 300, window=f_button)
    canva.create_window(295, 300, window=g_button)
    canva.create_window(325, 300, window=h_button)
    canva.create_window(355, 300, window=i_button)
    canva.create_window(385, 300, window=j_button)
    canva.create_window(115, 330, window=k_button)
    canva.create_window(145, 330, window=l_button)
    canva.create_window(175, 330, window=m_button)
    canva.create_window(205, 330, window=n_button)
    canva.create_window(235, 330, window=o_button)
    canva.create_window(265, 330, window=p_button)
    canva.create_window(295, 330, window=q_button)
    canva.create_window(325, 330, window=r_button)
    canva.create_window(355, 330, window=s_button)
    canva.create_window(385, 330, window=t_button)
    canva.create_window(185, 360, window=u_button)
    canva.create_window(215, 360, window=v_button)
    canva.create_window(245, 360, window=w_button)
    canva.create_window(275, 360, window=x_button)
    canva.create_window(305, 360, window=y_button)
    canva.create_window(335, 360, window=z_button)

    def bindings(letter, button):
        if button.winfo_exists():
            check(letter, button)

    root.bind("<a>", lambda event: bindings("a", a_button))
    root.bind("<b>", lambda event: bindings("b", b_button))
    root.bind("<c>", lambda event: bindings("c", c_button))
    root.bind("<d>", lambda event: bindings("d", d_button))
    root.bind("<e>", lambda event: bindings("e", e_button))
    root.bind("<f>", lambda event: bindings("f", f_button))
    root.bind("<g>", lambda event: bindings("g", g_button))
    root.bind("<h>", lambda event: bindings("h", h_button))
    root.bind("<i>", lambda event: bindings("i", i_button))
    root.bind("<j>", lambda event: bindings("j", j_button))
    root.bind("<k>", lambda event: bindings("k", k_button))
    root.bind("<l>", lambda event: bindings("l", l_button))
    root.bind("<m>", lambda event: bindings("m", m_button))
    root.bind("<n>", lambda event: bindings("n", n_button))
    root.bind("<o>", lambda event: bindings("o", o_button))
    root.bind("<p>", lambda event: bindings("p", p_button))
    root.bind("<q>", lambda event: bindings("q", q_button))
    root.bind("<r>", lambda event: bindings("r", r_button))
    root.bind("<s>", lambda event: bindings("s", s_button))
    root.bind("<t>", lambda event: bindings("t", t_button))
    root.bind("<u>", lambda event: bindings("u", u_button))
    root.bind("<v>", lambda event: bindings("v", v_button))
    root.bind("<w>", lambda event: bindings("w", w_button))
    root.bind("<x>", lambda event: bindings("x", x_button))
    root.bind("<y>", lambda event: bindings("y", y_button))
    root.bind("<z>", lambda event: bindings("z", z_button))
    canva.grid()


root = Tk()

root.iconbitmap("icon.ico")
root.title("Hanged Man")
root.resizable(False, False)
main()
root.mainloop()

