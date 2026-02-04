from nicegui import ui


# ---------- FOOTER ----------
def footer():
    with ui.footer().classes(
        'w-full bg-[#111111] text-[#BB6B00] py-2 px-4 flex flex-col items-center'
    ):
        # DJCUT LINK TO MAIN
        ui.link('DjCut Studio © 2026', '/').classes(
            'font-semibold text-center text-sm no-underline cursor-pointer'
        ).style('color: #BB6B00;')

        # EMAIL
        ui.label('contact@djcutstudio.com').classes(
            'text-xs opacity-80 text-center'
        )

# ---------- DJCUT STUDIO PAGE ----------
@ui.page('/')
def index():
    with ui.column().style('background-color: black;').classes(
        'w-full items-center gap-8 px-4 py-12'
    ):
        # TITLE
        ui.label('DjCut Studio').classes(
            'text-4xl md:text-6xl font-bold text-[#BB6B00] text-center'
        )

        # LOGO
        with ui.card().classes(
            'max-w-xs w-full p-3 bg-white shadow-xl'
        ):
            ui.image('./static/djcut_s.png') \
                .classes('w-full rounded')

            # DESCRIPTION
            ui.label("""    DjCut Studio is an indie game studio passionate about creating memorable board game experiences.
Our debut game, Legendary Dragon, challenges players to cooperate, plan, and fight various creatures together."""
            ).style('white-space: pre-wrap').classes(
                'text-lg text-center mt-6 text-[#3b2f2f]'
            )

        # LINK TO GAME
        with ui.card().classes(
            'p-2 bg-white text-[#3b2f2f] hover:scale-105 transition cursor-pointer w-full max-w-xs'
        ).on('click', lambda: ui.navigate.to('/legendarydragon')):
            ui.image('./static/ld_logo_black_m.png') \
                .classes('w-full rounded pointer-events-none')
            ui.label('Discover the game').classes(
                'text-center text-xl mt-4 font-semibold pointer-events-none'
            )

    footer()

# ---------- LEGENDARY DRAGON PAGE ----------
@ui.page('/legendarydragon')
def legendarydragon_page():
    with ui.column().style('background-color: black;').classes(
        'w-full items-center gap-8 px-4 py-12'
    ):
        # TITLE
        ui.label('Legendary Dragon').classes(
            'text-4xl md:text-6xl font-bold text-[#BB6B00] text-center'
        )

        # LOGO
        with ui.card().classes(
            'max-w-md w-full p-6 bg-white shadow-xl'
        ):
            ui.image('./static/ld_logo_black_m.png') \
                .classes('w-full rounded')

            # DESCRIPTION
            ui.label("""    A cooperative game full of strategy and teamwork. Each turn, players debate, plan, and position the Bard, the Magician and the Shaman in front of the right monsters to maximize gains and try to win the round.
    Roll the dice, activate your abilities at the right moment, team up to win the battle, and face creatures like Strong Goblins, Weak Skeleton or ... a Legendary Dragon!"""
            ).style('text-align: justify;white-space: pre-wrap').classes(
                'text-lg text-center mt-6 text-[#3b2f2f]'
            )

        # YOUTUBE
        ui.html('''
        <div style="
            width: 50vw;
            min-width: 320px;
            max-width: 1400px;
            margin: 0 auto;
            aspect-ratio: 16/9;
        ">
            <iframe
                src="https://www.youtube.com/embed/DOoi-Gt-0rE"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen
                style="width:100%; height:100%; border:0;">
            </iframe>
        </div>
        ''')

        # RULES
        with ui.card().classes(
            'p-1 bg-[#000000] text-[#F9DBBD] hover:scale-105 transition w-26 h-26' 
        ).style('border: 2px solid #BB6B00; border-radius: 0.5rem;'):
            ui.image('./static/dl_icon.png') \
                .classes('w-10 rounded block mx-auto')
            ui.label('Download English Rules').classes(
                'text-center mt-1 font-semibold'
            )

    footer()

ui.run(host="0.0.0.0", port=8080, forwarded_allow_ips="*", favicon="./static/favicon.ico", title='DjCut Studio')