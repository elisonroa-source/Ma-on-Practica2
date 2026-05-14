"""
Bob Meijer - Google Ads Specialist Landing Page
Recreated in Reflex (Python)
Run with: reflex run
"""

import reflex as rx

# =============================================
# COLORES Y ESTILOS GLOBALES
# =============================================
COLORS = {
    "bg_cream": "#FAF7F2",
    "bg_light": "#F5F0E8",
    "bg_teal": "#E8F0EF",
    "dark": "#1A1A1A",
    "dark_gray": "#333333",
    "medium_gray": "#666666",
    "light_gray": "#999999",
    "border": "#E5E0D8",
    "btn_dark": "#1A1A1A",
    "btn_text": "#FFFFFF",
    "white": "#FFFFFF",
    "card_bg": "#FDFAF6",
    "accent": "#2D5A5A",
}

FONT_FAMILY = "Georgia, 'Times New Roman', serif"
FONT_SANS = "'Helvetica Neue', Arial, sans-serif"

HEADING_STYLE = {
    "font_family": FONT_FAMILY,
    "color": COLORS["dark"],
    "font_weight": "700",
}

BODY_STYLE = {
    "font_family": FONT_SANS,
    "color": COLORS["medium_gray"],
    "font_size": "0.95rem",
    "line_height": "1.7",
}

BTN_PRIMARY = {
    "background": COLORS["btn_dark"],
    "color": COLORS["btn_text"],
    "border_radius": "4px",
    "padding": "12px 28px",
    "font_family": FONT_SANS,
    "font_size": "0.85rem",
    "font_weight": "600",
    "cursor": "pointer",
    "border": "none",
    "letter_spacing": "0.03em",
    "white_space": "nowrap",
    "text_align": "center",
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "width": "auto",
    "min_width": "fit-content",
    "text_decoration": "none",
    "_hover": {"background": "#333333"},
}

BTN_OUTLINE = {
    "background": "transparent",
    "color": COLORS["dark"],
    "border_radius": "4px",
    "padding": "10px 24px",
    "font_family": FONT_SANS,
    "font_size": "0.82rem",
    "font_weight": "600",
    "cursor": "pointer",
    "border": f"1.5px solid {COLORS['dark']}",
    "letter_spacing": "0.03em",
    "white_space": "nowrap",
    "text_align": "center",
    "display": "inline-flex",
    "align_items": "center",
    "justify_content": "center",
    "width": "auto",
    "min_width": "fit-content",
    "text_decoration": "none",
    "_hover": {"background": COLORS["dark"], "color": COLORS["white"]},
}


# =============================================
# NAVBAR
# =============================================
def navbar() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                # Logo
                rx.flex(
                    rx.box(
                        rx.text(
                            "⬡",
                            font_size="1.3rem",
                            color=COLORS["dark"],
                            margin_right="8px",
                        ),
                        display="flex",
                        align_items="center",
                    ),
                    rx.text(
                        "Bob Meijer",
                        font_family=FONT_SANS,
                        font_weight="700",
                        font_size="1.05rem",
                        color=COLORS["dark"],
                        letter_spacing="0.02em",
                    ),
                    align="center",
                    gap="4px",
                ),
                # Nav links
                rx.flex(
                    rx.link(
                        "Home",
                        href="#",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        color=COLORS["dark_gray"],
                        text_decoration="none",
                        _hover={"color": COLORS["dark"]},
                    ),
                    rx.link(
                        "Google Ads Services ▾",
                        href="#",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        color=COLORS["dark_gray"],
                        text_decoration="none",
                        _hover={"color": COLORS["dark"]},
                    ),
                    rx.link(
                        "Google Ads resources",
                        href="#",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        color=COLORS["dark_gray"],
                        text_decoration="none",
                        _hover={"color": COLORS["dark"]},
                    ),
                    rx.link(
                        "About me",
                        href="#",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        color=COLORS["dark_gray"],
                        text_decoration="none",
                        _hover={"color": COLORS["dark"]},
                    ),
                    rx.link(
                        "Contact",
                        href="#",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        color=COLORS["dark_gray"],
                        text_decoration="none",
                        _hover={"color": COLORS["dark"]},
                    ),
                    rx.link(
                        "🇳🇱 NL",
                        href="#",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        color=COLORS["dark_gray"],
                        text_decoration="none",
                        _hover={"color": COLORS["dark"]},
                    ),
                    gap="32px",
                    align="center",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
        ),
        background=COLORS["white"],
        border_bottom=f"1px solid {COLORS['border']}",
        padding_y="18px",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
    )


# =============================================
# HERO SECTION
# =============================================
def hero() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                # Left: Text content
                rx.vstack(
                    rx.heading(
                        "Your Google Ads campaigns perform better with me behind the wheel.",
                        font_size="2.8rem",
                        line_height="1.2",
                        font_family=FONT_FAMILY,
                        font_weight="700",
                        color=COLORS["dark"],
                        max_width="520px",
                    ),
                    rx.text(
                        "I'll get the most out of your Google Ads campaigns or teach you the intricacies so you can do it yourself!",
                        font_family=FONT_SANS,
                        font_size="1rem",
                        color=COLORS["medium_gray"],
                        line_height="1.7",
                        max_width="460px",
                        margin_top="16px",
                    ),
                    rx.flex(
                        rx.link(
                            rx.button(
                                "I want to outsource Google Ads",
                                **BTN_PRIMARY,
                            ),
                            href="#",
                            display="inline-flex",
                            width="fit-content",
                        ),
                        rx.link(
                            rx.button(
                                "Ver casos de éxito →",
                                background="transparent",
                                color=COLORS["dark"],
                                border="1.5px solid " + COLORS["dark"],
                                border_radius="4px",
                                padding="12px 24px",
                                font_family=FONT_SANS,
                                font_size="0.85rem",
                                font_weight="600",
                                cursor="pointer",
                                white_space="nowrap",
                                display="inline-flex",
                                align_items="center",
                                justify_content="center",
                                width="fit-content",
                                _hover={"background": COLORS["dark"], "color": COLORS["white"]},
                            ),
                            href="/casos",
                            display="inline-flex",
                            width="fit-content",
                        ),
                        gap="12px",
                        flex_wrap="wrap",
                        margin_top="28px",
                    ),
                    align_items="start",
                    gap="0",
                    flex="1",
                    padding_right="4rem",
                    padding_top="3rem",
                    padding_bottom="3rem",
                ),
                # Right: Hero image (decorative circle + photo)
                rx.box(
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=450&fit=crop&crop=face",
                            width="320px",
                            height="360px",
                            object_fit="cover",
                            border_radius="50% 50% 50% 50% / 60% 60% 40% 40%",
                            box_shadow="0 20px 60px rgba(0,0,0,0.12)",
                        ),
                        position="relative",
                        z_index="2",
                    ),
                    # Decorative square outline
                    rx.box(
                        position="absolute",
                        top="10px",
                        left="-20px",
                        width="80px",
                        height="80px",
                        border=f"2px solid {COLORS['border']}",
                        z_index="1",
                    ),
                    position="relative",
                    flex="0 0 auto",
                    display="flex",
                    align_items="end",
                    padding_bottom="0",
                ),
                justify="between",
                align="end",
                width="100%",
                gap="2rem",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
        ),
        background=COLORS["bg_cream"],
        width="100%",
        overflow="hidden",
    )


# =============================================
# LOGOS / COMPANIES SECTION
# =============================================
def companies() -> rx.Component:
    logos = [
        "Enercal", "Vanastamps", "Deelnemersplatform",
        "Jobseller", "UTES", "Wolt", "WightWatchers",
        "Tyhoo", "Louwman", "Demo"
    ]

    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "I work with the best companies",
                    font_size="1.8rem",
                    font_family=FONT_FAMILY,
                    font_weight="700",
                    color=COLORS["dark"],
                    text_align="center",
                ),
                rx.text(
                    "May I add you to the list?",
                    font_family=FONT_SANS,
                    font_size="0.9rem",
                    color=COLORS["light_gray"],
                    text_align="center",
                    margin_top="4px",
                ),
                # Logo grid - row 1
                rx.flex(
                    *[
                        rx.box(
                            rx.text(
                                logo,
                                font_family=FONT_SANS,
                                font_size="0.8rem",
                                font_weight="600",
                                color=COLORS["light_gray"],
                                letter_spacing="0.05em",
                            ),
                            padding_x="20px",
                            padding_y="8px",
                        )
                        for logo in logos[:5]
                    ],
                    justify="center",
                    align="center",
                    gap="32px",
                    flex_wrap="wrap",
                    margin_top="32px",
                ),
                # Logo grid - row 2
                rx.flex(
                    *[
                        rx.box(
                            rx.text(
                                logo,
                                font_family=FONT_SANS,
                                font_size="0.8rem",
                                font_weight="600",
                                color=COLORS["light_gray"],
                                letter_spacing="0.05em",
                            ),
                            padding_x="20px",
                            padding_y="8px",
                        )
                        for logo in logos[5:]
                    ],
                    justify="center",
                    align="center",
                    gap="32px",
                    flex_wrap="wrap",
                    margin_top="8px",
                ),
                gap="0",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="4rem",
        ),
        background=COLORS["white"],
        border_bottom=f"1px solid {COLORS['border']}",
        width="100%",
    )


# =============================================
# ABOUT SECTION
# =============================================
def about() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                # Left: Image with circle decoration
                rx.box(
                    rx.box(
                        rx.image(
                            src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=450&h=500&fit=crop&crop=face",
                            width="100%",
                            height="480px",
                            object_fit="cover",
                            border_radius="8px",
                        ),
                        width="380px",
                        position="relative",
                        z_index="2",
                    ),
                    # Teal circle decoration
                    rx.box(
                        position="absolute",
                        bottom="-30px",
                        right="-40px",
                        width="200px",
                        height="200px",
                        background=COLORS["bg_teal"],
                        border_radius="50%",
                        z_index="1",
                    ),
                    # Small dots decoration
                    rx.box(
                        position="absolute",
                        top="20px",
                        left="-20px",
                        font_size="2rem",
                        color=COLORS["border"],
                        z_index="1",
                    ),
                    position="relative",
                    flex="0 0 auto",
                    margin_right="5rem",
                ),
                # Right: Text content
                rx.vstack(
                    rx.heading(
                        "Hi, I'm Bob Meijer.",
                        font_size="2.2rem",
                        font_family=FONT_FAMILY,
                        font_weight="700",
                        color=COLORS["dark"],
                    ),
                    rx.text(
                        "As a Google Ads specialist, I help ",
                        rx.text.span("ambitious companies", font_weight="700", color=COLORS["dark"]),
                        " get the most out of Google Ads. I work for a select number of clients and am responsible for over €3,500,000 per month in ad spend.",
                        font_family=FONT_SANS,
                        font_size="0.95rem",
                        color=COLORS["medium_gray"],
                        line_height="1.8",
                        margin_top="16px",
                    ),
                    rx.text(
                        "Over the years, I have had the opportunity to work on more than 100 Google Ads accounts. Often challenging accounts from great names including ",
                        rx.text.span("Weight Watchers, Louwman, Harley Davidson, KPMG, Schaonenberg", font_weight="600", color=COLORS["dark_gray"]),
                        ", and more.",
                        font_family=FONT_SANS,
                        font_size="0.95rem",
                        color=COLORS["medium_gray"],
                        line_height="1.8",
                        margin_top="12px",
                    ),
                    rx.text(
                        "I also provide ",
                        rx.text.span("Google Ads courses", font_weight="700", color=COLORS["dark"]),
                        " and ",
                        rx.text.span("1-on-1 coaching sessions", font_weight="700", color=COLORS["dark"]),
                        ". In these, I share my knowledge with ",
                        rx.text.span("novice to very advanced", font_style="italic"),
                        " Google Ads advertisers. This way, they learn the intricacies of the business.",
                        font_family=FONT_SANS,
                        font_size="0.95rem",
                        color=COLORS["medium_gray"],
                        line_height="1.8",
                        margin_top="12px",
                    ),
                    align_items="start",
                    gap="0",
                    flex="1",
                ),
                align="center",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="5rem",
        ),
        background=COLORS["bg_light"],
        width="100%",
    )


# =============================================
# SERVICE CARD COMPONENT
# =============================================
def service_card(icon: str, title: str, description: str, btn_text: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Icon area
            rx.box(
                rx.text(icon, font_size="2rem"),
                width="60px",
                height="60px",
                display="flex",
                align_items="center",
                justify_content="center",
                background=COLORS["bg_cream"],
                border_radius="8px",
                margin_bottom="8px",
            ),
            rx.heading(
                title,
                font_size="1.15rem",
                font_family=FONT_FAMILY,
                font_weight="700",
                color=COLORS["dark"],
                margin_top="8px",
            ),
            rx.text(
                description,
                font_family=FONT_SANS,
                font_size="0.88rem",
                color=COLORS["medium_gray"],
                line_height="1.7",
                text_align="left",
                margin_top="8px",
                flex="1",
            ),
            rx.link(
                rx.button(btn_text, **BTN_OUTLINE),
                href="#",
                margin_top="20px",
                display="inline-flex",
                width="fit-content",
            ),
            align_items="start",
            height="100%",
            gap="0",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius="8px",
        padding="2rem",
        flex="1",
        box_shadow="0 2px 12px rgba(0,0,0,0.04)",
        _hover={"box_shadow": "0 8px 30px rgba(0,0,0,0.08)", "transform": "translateY(-2px)"},
        transition="all 0.2s ease",
        min_height="320px",
        display="flex",
        flex_direction="column",
    )


# =============================================
# SERVICES SECTION
# =============================================
def services() -> rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Google Ads services",
                    font_size="2rem",
                    font_family=FONT_FAMILY,
                    font_weight="700",
                    color=COLORS["dark"],
                    text_align="center",
                ),
                rx.flex(
                    service_card(
                        "📊",
                        "Outsource Google Ads",
                        "I get the most out of your Google Ads campaigns. Let me setup, manage and optimize your account.",
                        "I want to know more",
                    ),
                    service_card(
                        "🎓",
                        "Google Ads courses",
                        "Learn proven Google Ads strategies, techniques, and clever hacks I use daily to grow my client's accounts!",
                        "I want to learn Google Ads",
                    ),
                    service_card(
                        "💬",
                        "Google Ads coaching",
                        "Do you have the basics of Google Ads under control and are ready to go deeper? I am here for you!",
                        "I want to see",
                    ),
                    gap="24px",
                    align="stretch",
                    margin_top="3rem",
                    width="100%",
                ),
                gap="0",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="5rem",
        ),
        background=COLORS["white"],
        width="100%",
    )


# =============================================
# WORK WITH ME / CTA BANNER SECTION
# =============================================
def work_with_me() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                # Left: text content
                rx.vstack(
                    rx.text(
                        "Work with me.",
                        font_family=FONT_SANS,
                        font_size="0.85rem",
                        color=COLORS["medium_gray"],
                        letter_spacing="0.08em",
                        text_transform="uppercase",
                    ),
                    rx.heading(
                        "I get the most out of it.",
                        font_size="2.5rem",
                        font_family=FONT_FAMILY,
                        font_weight="700",
                        color=COLORS["dark"],
                        line_height="1.2",
                        margin_top="8px",
                    ),
                    rx.text(
                        "Let's talk about the results I can get for your business, free of jargon and without bullshit lingo.",
                        font_family=FONT_SANS,
                        font_size="0.95rem",
                        color=COLORS["medium_gray"],
                        line_height="1.7",
                        max_width="420px",
                        margin_top="12px",
                    ),
                    rx.link(
                        rx.button("Get in touch", **BTN_PRIMARY),
                        href="#",
                        margin_top="24px",
                        display="inline-flex",
                        width="fit-content",
                    ),
                    align_items="start",
                    gap="0",
                    flex="1",
                    padding_right="3rem",
                ),
                # Right: person image on beach
                rx.box(
                    rx.image(
                        src="https://images.unsplash.com/photo-1530789253388-582c481c54b0?w=500&h=400&fit=crop",
                        width="420px",
                        height="380px",
                        object_fit="cover",
                        border_radius="8px 8px 8px 8px",
                        box_shadow="0 20px 60px rgba(0,0,0,0.15)",
                    ),
                    # Teal circle behind image
                    rx.box(
                        position="absolute",
                        bottom="-20px",
                        right="-20px",
                        width="160px",
                        height="160px",
                        background=COLORS["bg_teal"],
                        border_radius="50%",
                        z_index="0",
                    ),
                    position="relative",
                    flex="0 0 auto",
                ),
                align="center",
                width="100%",
                gap="2rem",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="5rem",
        ),
        background=COLORS["bg_cream"],
        width="100%",
    )


# =============================================
# TESTIMONIAL CARD COMPONENT
# =============================================
def testimonial_card(quote: str, name: str, role: str, company: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Quote marks
            rx.text(
                "❝❝",
                font_size="1.5rem",
                color=COLORS["accent"],
                letter_spacing="-0.1em",
                opacity="0.6",
            ),
            rx.text(
                quote,
                font_family=FONT_SANS,
                font_size="0.88rem",
                color=COLORS["dark_gray"],
                line_height="1.7",
                margin_top="8px",
                flex="1",
            ),
            rx.flex(
                rx.box(
                    rx.image(
                        src=f"https://i.pravatar.cc/50?u={name}",
                        width="42px",
                        height="42px",
                        border_radius="50%",
                        object_fit="cover",
                    ),
                ),
                rx.vstack(
                    rx.text(
                        name,
                        font_family=FONT_SANS,
                        font_size="0.85rem",
                        font_weight="700",
                        color=COLORS["dark"],
                    ),
                    rx.text(
                        f"{role} at {company}",
                        font_family=FONT_SANS,
                        font_size="0.78rem",
                        color=COLORS["light_gray"],
                    ),
                    gap="2px",
                    align_items="start",
                ),
                gap="12px",
                align="center",
                margin_top="16px",
            ),
            align_items="start",
            height="100%",
            gap="0",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius="8px",
        padding="1.75rem",
        box_shadow="0 2px 12px rgba(0,0,0,0.04)",
        flex="1",
        display="flex",
        flex_direction="column",
        min_height="220px",
    )


# =============================================
# TESTIMONIALS SECTION
# =============================================
def testimonials() -> rx.Component:
    testimonials_data = [
        {
            "quote": "Bob convinced WeightWatchers of his knowledge and expertise from the 1st moment of contact. The results exceeded expectations!",
            "name": "Jens Rijs",
            "role": "Head of Digital",
            "company": "WeightWatchers",
        },
        {
            "quote": "Bob has provided results quickly with a structured approach. He also offered a more professional basis for further optimizing our campaigns.",
            "name": "Tim Nelis",
            "role": "Director",
            "company": "Wolfton",
        },
        {
            "quote": "We have been working with Bob for quite some time, and his expertise in Google Ads has become indispensable. We are extremely satisfied.",
            "name": "Fanar Al-Obaidy",
            "role": "Founder",
            "company": "NOX Sleep Drive",
        },
        {
            "quote": "We have experienced your service as very nice and enlightening. You work fast, are flexible and always advise us well. Our target group now knows how to find us much better.",
            "name": "Laura Meijer",
            "role": "Online Marketeer",
            "company": "Bronnen",
        },
        {
            "quote": "The number of conversions has more than tripled compared to the previous year. I think it needs no further explanation that I am very satisfied with that.",
            "name": "Ellen Das",
            "role": "Owner",
            "company": "Love, Peace & Joy",
        },
        {
            "quote": "We felt we could get more out of Google Ads. Since switching to Bob, things have been going much better. We are getting more bookings for less budget, great!",
            "name": "René Speetman",
            "role": "Marketing Manager",
            "company": "Dannnacity",
        },
    ]

    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "What people say about me",
                    font_size="2rem",
                    font_family=FONT_FAMILY,
                    font_weight="700",
                    color=COLORS["dark"],
                    text_align="center",
                ),
                # Row 1 - 3 testimonials
                rx.flex(
                    *[
                        testimonial_card(
                            t["quote"], t["name"], t["role"], t["company"]
                        )
                        for t in testimonials_data[:3]
                    ],
                    gap="20px",
                    align="stretch",
                    margin_top="3rem",
                    width="100%",
                ),
                # Row 2 - 3 testimonials
                rx.flex(
                    *[
                        testimonial_card(
                            t["quote"], t["name"], t["role"], t["company"]
                        )
                        for t in testimonials_data[3:]
                    ],
                    gap="20px",
                    align="stretch",
                    margin_top="20px",
                    width="100%",
                ),
                gap="0",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="5rem",
        ),
        background=COLORS["bg_cream"],
        width="100%",
    )


# =============================================
# READY TO GROW CTA SECTION
# =============================================
def ready_cta() -> rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                rx.heading(
                    "Ready to grow?",
                    font_size="2.2rem",
                    font_family=FONT_FAMILY,
                    font_weight="700",
                    color=COLORS["dark"],
                    text_align="center",
                ),
                rx.text(
                    "Let's talk about the results I can get for your business. Free of jargon and without bullshit lingo.",
                    font_family=FONT_SANS,
                    font_size="0.95rem",
                    color=COLORS["medium_gray"],
                    text_align="center",
                    max_width="500px",
                    line_height="1.7",
                    margin_top="12px",
                ),
                rx.link(
                    rx.button("Get in touch", **BTN_PRIMARY),
                    href="#",
                    margin_top="28px",
                    display="inline-flex",
                    width="fit-content",
                ),
                gap="0",
                align="center",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="5rem",
        ),
        background=COLORS["bg_light"],
        width="100%",
    )


# =============================================
# FOOTER
# =============================================
def footer() -> rx.Component:
    return rx.box(
        rx.container(
            rx.flex(
                # Column 1: Brand
                rx.vstack(
                    rx.flex(
                        rx.text("⬡", font_size="1.1rem", color=COLORS["white"], margin_right="6px"),
                        rx.text(
                            "Bob Meijer",
                            font_family=FONT_SANS,
                            font_weight="700",
                            font_size="0.95rem",
                            color=COLORS["white"],
                        ),
                        align="center",
                    ),
                    rx.text(
                        "Nijntjestraat 2\n7478EJ Diepenheim\nNetherlands",
                        font_family=FONT_SANS,
                        font_size="0.8rem",
                        color="#888888",
                        line_height="1.8",
                        margin_top="12px",
                        white_space="pre-line",
                    ),
                    rx.text(
                        "KvK-number: 78443027\nBtw-identificatienumber:\nNL861402720B01",
                        font_family=FONT_SANS,
                        font_size="0.78rem",
                        color="#666666",
                        line_height="1.8",
                        margin_top="8px",
                        white_space="pre-line",
                    ),
                    align_items="start",
                    gap="0",
                    min_width="180px",
                ),
                # Column 2: Google Ads Services
                rx.vstack(
                    rx.text(
                        "Google Ads services",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        font_weight="700",
                        color=COLORS["white"],
                        margin_bottom="16px",
                    ),
                    *[
                        rx.link(
                            label,
                            href="#",
                            font_family=FONT_SANS,
                            font_size="0.82rem",
                            color="#888888",
                            text_decoration="none",
                            _hover={"color": COLORS["white"]},
                        )
                        for label in [
                            "Outsource Google Ads",
                            "Google Ads audit",
                            "Google Ads coaching",
                        ]
                    ],
                    align_items="start",
                    gap="10px",
                    min_width="160px",
                ),
                # Column 3: Resources
                rx.vstack(
                    rx.text(
                        "Resources",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        font_weight="700",
                        color=COLORS["white"],
                        margin_bottom="16px",
                    ),
                    *[
                        rx.link(
                            label,
                            href="#",
                            font_family=FONT_SANS,
                            font_size="0.82rem",
                            color="#888888",
                            text_decoration="none",
                            _hover={"color": COLORS["white"]},
                        )
                        for label in [
                            "Visit my LinkedIn",
                            "Google Ads community",
                            "Google Ads newsletter",
                            "Google Ads podcast",
                        ]
                    ],
                    align_items="start",
                    gap="10px",
                    min_width="160px",
                ),
                # Column 4: General
                rx.vstack(
                    rx.text(
                        "General",
                        font_family=FONT_SANS,
                        font_size="0.88rem",
                        font_weight="700",
                        color=COLORS["white"],
                        margin_bottom="16px",
                    ),
                    *[
                        rx.link(
                            label,
                            href="#",
                            font_family=FONT_SANS,
                            font_size="0.82rem",
                            color="#888888",
                            text_decoration="none",
                            _hover={"color": COLORS["white"]},
                        )
                        for label in [
                            "About me",
                            "Contact",
                            "Terms and conditions",
                            "Privacy statement",
                            "Cookie policy",
                        ]
                    ],
                    align_items="start",
                    gap="10px",
                    min_width="160px",
                ),
                gap="4rem",
                align="start",
                width="100%",
                flex_wrap="wrap",
            ),
            # Divider + Badges (clickable)
            rx.box(
                rx.divider(border_color="#333333", margin_y="2rem"),
                rx.flex(
                    # Google Partner badge
                    rx.link(
                        rx.box(
                            rx.text(
                                "Google",
                                font_family=FONT_SANS,
                                font_size="0.72rem",
                                font_weight="700",
                                color=COLORS["white"],
                                text_align="center",
                                line_height="1.3",
                            ),
                            rx.text(
                                "Partner",
                                font_family=FONT_SANS,
                                font_size="0.72rem",
                                font_weight="700",
                                color=COLORS["white"],
                                text_align="center",
                                line_height="1.3",
                            ),
                            background="#1a73e8",
                            padding="10px 20px",
                            border_radius="6px",
                            display="flex",
                            flex_direction="column",
                            align_items="center",
                            cursor="pointer",
                            _hover={"background": "#1557b0", "transform": "translateY(-1px)"},
                            transition="all 0.2s ease",
                        ),
                        href="https://www.google.com/partners/",
                        is_external=True,
                        text_decoration="none",
                    ),
                    # Microsoft Advertising Partner badge
                    rx.link(
                        rx.box(
                            rx.text(
                                "Microsoft",
                                font_family=FONT_SANS,
                                font_size="0.72rem",
                                font_weight="700",
                                color=COLORS["white"],
                                text_align="center",
                                line_height="1.3",
                            ),
                            rx.text(
                                "Partner",
                                font_family=FONT_SANS,
                                font_size="0.72rem",
                                font_weight="700",
                                color=COLORS["white"],
                                text_align="center",
                                line_height="1.3",
                            ),
                            background="#00a1f1",
                            padding="10px 20px",
                            border_radius="6px",
                            display="flex",
                            flex_direction="column",
                            align_items="center",
                            cursor="pointer",
                            _hover={"background": "#0078d4", "transform": "translateY(-1px)"},
                            transition="all 0.2s ease",
                        ),
                        href="https://about.ads.microsoft.com/en/resources/partner-badges",
                        is_external=True,
                        text_decoration="none",
                    ),
                    gap="12px",
                    justify="center",
                ),
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="4rem",
        ),
        background="#111111",
        width="100%",
    )


# =============================================
# MAIN INDEX PAGE
# =============================================
def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        companies(),
        about(),
        services(),
        work_with_me(),
        testimonials(),
        ready_cta(),
        footer(),
        width="100%",
        max_width="100%",
        margin="0 auto",
        padding="0",
        min_height="100vh",
        background=COLORS["white"],
        font_family=FONT_SANS,
        overflow_x="hidden",
    )


# =============================================
# CASOS DE ÉXITO PAGE
# =============================================

CASOS = [
    {
        "company": "WeightWatchers",
        "industry": "Health & Wellness",
        "icon": "⚖️",
        "color": "#2D5A5A",
        "bg": "#E8F0EF",
        "result_1": "+340%",
        "label_1": "Conversiones",
        "result_2": "-28%",
        "label_2": "Coste por lead",
        "result_3": "€2.1M",
        "label_3": "Ad spend gestionado",
        "quote": "Bob convirtió nuestras campañas en una máquina de conversiones desde el primer mes. Su expertise es innegable.",
        "person": "Jens Rijs",
        "role": "Head of Digital",
        "duration": "18 meses de colaboración",
    },
    {
        "company": "NOX Sleep Drive",
        "industry": "E-commerce / Sleep Tech",
        "icon": "🌙",
        "color": "#1A1A6E",
        "bg": "#EEEEF8",
        "result_1": "+510%",
        "label_1": "ROAS",
        "result_2": "x3.2",
        "label_2": "Facturación",
        "result_3": "#1",
        "label_3": "Posición en Google Shopping",
        "quote": "Llevamos años trabajando juntos. Google Ads se ha vuelto nuestro canal más rentable gracias a Bob.",
        "person": "Fanar Al-Obaidy",
        "role": "Founder & CEO",
        "duration": "3 años de colaboración",
    },
    {
        "company": "Love, Peace & Joy",
        "industry": "Lifestyle / Retail",
        "icon": "🌸",
        "color": "#8B3A62",
        "bg": "#F8EEF4",
        "result_1": "+280%",
        "label_1": "Transacciones",
        "result_2": "x3",
        "label_2": "Conversiones totales",
        "result_3": "+190%",
        "label_3": "Revenue online",
        "quote": "Triplicamos las conversiones. No hay más que decir — estoy más que satisfecha.",
        "person": "Ellen Das",
        "role": "Owner",
        "duration": "12 meses de colaboración",
    },
    {
        "company": "Wolfton",
        "industry": "B2B / SaaS",
        "icon": "🏢",
        "color": "#2C4A6E",
        "bg": "#EEF3F8",
        "result_1": "-42%",
        "label_1": "CPL reducido",
        "result_2": "+220%",
        "label_2": "Leads cualificados",
        "result_3": "4.8x",
        "label_3": "ROAS en Search",
        "quote": "Enfoque estructurado y resultados rápidos. La base profesional que pusimos nos sigue dando frutos.",
        "person": "Tim Nelis",
        "role": "Director",
        "duration": "9 meses de colaboración",
    },
    {
        "company": "Bronnen",
        "industry": "Local Business",
        "icon": "📍",
        "color": "#5A3A1A",
        "bg": "#F8F0E8",
        "result_1": "+180%",
        "label_1": "Visitas a tienda",
        "result_2": "x2.4",
        "label_2": "Llamadas recibidas",
        "result_3": "+95%",
        "label_3": "Leads locales",
        "quote": "Nuestro grupo objetivo ahora nos encuentra con facilidad. El impacto fue inmediato y sostenido.",
        "person": "Laura Meijer",
        "role": "Online Marketeer",
        "duration": "6 meses de colaboración",
    },
    {
        "company": "Damnacity",
        "industry": "Travel & Hospitality",
        "icon": "✈️",
        "color": "#1A4A3A",
        "bg": "#E8F4F0",
        "result_1": "+310%",
        "label_1": "Reservas online",
        "result_2": "-35%",
        "label_2": "Coste por reserva",
        "result_3": "+250%",
        "label_3": "Revenue directo",
        "quote": "Más reservas, menos presupuesto. Eso es exactamente lo que necesitábamos. Bob lo consiguió.",
        "person": "René Speetman",
        "role": "Marketing Manager",
        "duration": "14 meses de colaboración",
    },
]


def stat_pill(value: str, label: str, color: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            value,
            font_family=FONT_FAMILY,
            font_size="2rem",
            font_weight="700",
            color=color,
            line_height="1",
        ),
        rx.text(
            label,
            font_family=FONT_SANS,
            font_size="0.75rem",
            color=COLORS["medium_gray"],
            letter_spacing="0.04em",
            text_transform="uppercase",
            margin_top="4px",
        ),
        align="center",
        gap="0",
    )


def caso_card(caso: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            # Header: icon + company + industry
            rx.flex(
                rx.box(
                    rx.text(caso["icon"], font_size="1.8rem"),
                    width="56px",
                    height="56px",
                    background=caso["bg"],
                    border_radius="14px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text(
                        caso["company"],
                        font_family=FONT_FAMILY,
                        font_size="1.2rem",
                        font_weight="700",
                        color=COLORS["dark"],
                        line_height="1.2",
                    ),
                    rx.box(
                        rx.text(
                            caso["industry"],
                            font_family=FONT_SANS,
                            font_size="0.72rem",
                            font_weight="600",
                            color=caso["color"],
                            letter_spacing="0.05em",
                        ),
                        background=caso["bg"],
                        padding="3px 10px",
                        border_radius="20px",
                        display="inline-flex",
                        margin_top="4px",
                    ),
                    gap="0",
                    align_items="start",
                ),
                gap="14px",
                align="center",
            ),
            # Divider
            rx.box(height="1px", background=COLORS["border"], width="100%", margin_y="20px"),
            # Stats row
            rx.flex(
                stat_pill(caso["result_1"], caso["label_1"], caso["color"]),
                rx.box(width="1px", background=COLORS["border"], height="50px", align_self="center"),
                stat_pill(caso["result_2"], caso["label_2"], caso["color"]),
                rx.box(width="1px", background=COLORS["border"], height="50px", align_self="center"),
                stat_pill(caso["result_3"], caso["label_3"], caso["color"]),
                justify="between",
                align="center",
                width="100%",
            ),
            # Quote
            rx.box(
                rx.text(
                    "❝ " + caso["quote"],
                    font_family=FONT_FAMILY,
                    font_size="0.92rem",
                    color=COLORS["dark_gray"],
                    line_height="1.7",
                    font_style="italic",
                ),
                background=caso["bg"],
                border_radius="8px",
                padding="16px 20px",
                margin_top="20px",
                border_left=f"3px solid {caso['color']}",
            ),
            # Author
            rx.flex(
                rx.box(
                    rx.text(
                        caso["person"][0],
                        font_size="0.85rem",
                        font_weight="700",
                        color=COLORS["white"],
                    ),
                    width="36px",
                    height="36px",
                    background=caso["color"],
                    border_radius="50%",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text(
                        caso["person"],
                        font_family=FONT_SANS,
                        font_size="0.83rem",
                        font_weight="700",
                        color=COLORS["dark"],
                    ),
                    rx.text(
                        caso["role"],
                        font_family=FONT_SANS,
                        font_size="0.75rem",
                        color=COLORS["light_gray"],
                    ),
                    gap="1px",
                    align_items="start",
                ),
                rx.box(flex="1"),
                rx.text(
                    caso["duration"],
                    font_family=FONT_SANS,
                    font_size="0.72rem",
                    color=COLORS["light_gray"],
                    font_style="italic",
                ),
                gap="10px",
                align="center",
                margin_top="16px",
                width="100%",
            ),
            gap="0",
            align_items="start",
            width="100%",
        ),
        background=COLORS["white"],
        border=f"1px solid {COLORS['border']}",
        border_radius="12px",
        padding="2rem",
        box_shadow="0 2px 16px rgba(0,0,0,0.05)",
        _hover={"box_shadow": "0 12px 40px rgba(0,0,0,0.10)", "transform": "translateY(-3px)"},
        transition="all 0.25s ease",
        width="100%",
    )


def casos_hero() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.link(
                    rx.flex(
                        rx.text("←", font_size="1rem"),
                        rx.text(
                            "Volver al inicio",
                            font_family=FONT_SANS,
                            font_size="0.85rem",
                            font_weight="600",
                        ),
                        gap="6px",
                        align="center",
                    ),
                    href="/",
                    color=COLORS["medium_gray"],
                    text_decoration="none",
                    _hover={"color": COLORS["dark"]},
                    margin_bottom="2rem",
                    display="inline-flex",
                ),
                rx.box(
                    rx.text(
                        "RESULTADOS REALES",
                        font_family=FONT_SANS,
                        font_size="0.75rem",
                        font_weight="700",
                        color=COLORS["accent"],
                        letter_spacing="0.15em",
                    ),
                    background=COLORS["bg_teal"],
                    padding="6px 16px",
                    border_radius="20px",
                    display="inline-flex",
                    margin_bottom="16px",
                ),
                rx.heading(
                    "Casos de Éxito.",
                    font_family=FONT_FAMILY,
                    font_size="3.5rem",
                    font_weight="700",
                    color=COLORS["dark"],
                    line_height="1.1",
                    text_align="center",
                ),
                rx.text(
                    "Números reales. Empresas reales. Sin bullshit.",
                    font_family=FONT_SANS,
                    font_size="1.1rem",
                    color=COLORS["medium_gray"],
                    text_align="center",
                    margin_top="12px",
                ),
                # Global stats bar
                rx.flex(
                    rx.vstack(
                        rx.text("100+", font_family=FONT_FAMILY, font_size="2.2rem", font_weight="700", color=COLORS["dark"]),
                        rx.text("Cuentas gestionadas", font_family=FONT_SANS, font_size="0.78rem", color=COLORS["medium_gray"], text_transform="uppercase", letter_spacing="0.05em"),
                        align="center", gap="4px",
                    ),
                    rx.box(width="1px", height="60px", background=COLORS["border"]),
                    rx.vstack(
                        rx.text("€3.5M+", font_family=FONT_FAMILY, font_size="2.2rem", font_weight="700", color=COLORS["dark"]),
                        rx.text("Ad spend mensual", font_family=FONT_SANS, font_size="0.78rem", color=COLORS["medium_gray"], text_transform="uppercase", letter_spacing="0.05em"),
                        align="center", gap="4px",
                    ),
                    rx.box(width="1px", height="60px", background=COLORS["border"]),
                    rx.vstack(
                        rx.text("8+ años", font_family=FONT_FAMILY, font_size="2.2rem", font_weight="700", color=COLORS["dark"]),
                        rx.text("de experiencia", font_family=FONT_SANS, font_size="0.78rem", color=COLORS["medium_gray"], text_transform="uppercase", letter_spacing="0.05em"),
                        align="center", gap="4px",
                    ),
                    rx.box(width="1px", height="60px", background=COLORS["border"]),
                    rx.vstack(
                        rx.text("4.9★", font_family=FONT_FAMILY, font_size="2.2rem", font_weight="700", color=COLORS["dark"]),
                        rx.text("Valoración media", font_family=FONT_SANS, font_size="0.78rem", color=COLORS["medium_gray"], text_transform="uppercase", letter_spacing="0.05em"),
                        align="center", gap="4px",
                    ),
                    justify="between",
                    align="center",
                    width="100%",
                    margin_top="3rem",
                    padding="2rem 3rem",
                    background=COLORS["white"],
                    border_radius="12px",
                    border=f"1px solid {COLORS['border']}",
                    box_shadow="0 2px 16px rgba(0,0,0,0.04)",
                ),
                align="center",
                gap="0",
                width="100%",
            ),
            max_width="1100px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="5rem",
        ),
        background=COLORS["bg_cream"],
        width="100%",
    )


def casos_grid() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.grid(
                    *[caso_card(c) for c in CASOS],
                    columns="2",
                    gap="24px",
                    width="100%",
                ),
                # Bottom CTA
                rx.box(
                    rx.vstack(
                        rx.text(
                            "¿Listo para ser el próximo caso de éxito?",
                            font_family=FONT_FAMILY,
                            font_size="1.8rem",
                            font_weight="700",
                            color=COLORS["dark"],
                            text_align="center",
                        ),
                        rx.text(
                            "Hablemos sobre tu negocio. Sin rodeos, sin jerga, solo resultados.",
                            font_family=FONT_SANS,
                            font_size="0.95rem",
                            color=COLORS["medium_gray"],
                            text_align="center",
                            margin_top="8px",
                        ),
                        rx.link(
                            rx.button(
                                "Contactar ahora →",
                                background=COLORS["dark"],
                                color=COLORS["white"],
                                border_radius="6px",
                                padding="14px 32px",
                                font_family=FONT_SANS,
                                font_size="0.9rem",
                                font_weight="700",
                                cursor="pointer",
                                white_space="nowrap",
                                display="inline-flex",
                                align_items="center",
                                justify_content="center",
                                border="none",
                                _hover={"background": "#333333"},
                            ),
                            href="/",
                            margin_top="24px",
                            display="inline-flex",
                            width="fit-content",
                        ),
                        align="center",
                        gap="0",
                    ),
                    background=COLORS["bg_light"],
                    border_radius="16px",
                    padding="3rem 2rem",
                    margin_top="3rem",
                    width="100%",
                    border=f"1px solid {COLORS['border']}",
                ),
                gap="0",
                width="100%",
            ),
            max_width="1100px",
            margin="0 auto",
            padding_x="2rem",
            padding_y="4rem",
        ),
        background=COLORS["white"],
        width="100%",
    )


def casos_navbar() -> rx.Component:
    return rx.box(
        rx.box(
            rx.flex(
                rx.flex(
                    rx.text("⬡", font_size="1.1rem", color=COLORS["dark"], margin_right="6px"),
                    rx.text("Bob Meijer", font_family=FONT_SANS, font_weight="700", font_size="1rem", color=COLORS["dark"]),
                    align="center", gap="4px",
                ),
                rx.flex(
                    rx.link("Inicio", href="/", font_family=FONT_SANS, font_size="0.85rem", color=COLORS["medium_gray"], text_decoration="none", _hover={"color": COLORS["dark"]}),
                    rx.link("Servicios", href="/#services", font_family=FONT_SANS, font_size="0.85rem", color=COLORS["medium_gray"], text_decoration="none", _hover={"color": COLORS["dark"]}),
                    rx.box(
                        rx.text("Casos de éxito", font_family=FONT_SANS, font_size="0.85rem", color=COLORS["dark"], font_weight="700"),
                        padding_bottom="2px",
                        border_bottom=f"2px solid {COLORS['dark']}",
                    ),
                    rx.link(
                        rx.button(
                            "Contactar",
                            background=COLORS["dark"],
                            color=COLORS["white"],
                            border_radius="4px",
                            padding="8px 18px",
                            font_family=FONT_SANS,
                            font_size="0.82rem",
                            font_weight="600",
                            cursor="pointer",
                            border="none",
                            white_space="nowrap",
                            _hover={"background": "#333"},
                        ),
                        href="/",
                        display="inline-flex",
                        width="fit-content",
                    ),
                    gap="28px",
                    align="center",
                ),
                justify="between",
                align="center",
                width="100%",
            ),
            max_width="1100px",
            margin="0 auto",
            padding_x="2rem",
        ),
        background=COLORS["white"],
        border_bottom=f"1px solid {COLORS['border']}",
        padding_y="16px",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
    )


def casos_page() -> rx.Component:
    return rx.box(
        casos_navbar(),
        casos_hero(),
        casos_grid(),
        width="100%",
        min_height="100vh",
        background=COLORS["white"],
        font_family=FONT_SANS,
        overflow_x="hidden",
    )


# =============================================
# APP CONFIGURATION
# =============================================
app = rx.App(
    style={
        "font_family": FONT_SANS,
        "background": COLORS["white"],
        # Reset global box model
        "*": {"box_sizing": "border-box", "margin": "0", "padding": "0"},
        # Ensure html/body take full width with no offset
        "html": {"width": "100%", "margin": "0", "padding": "0"},
        "body": {
            "margin": "0",
            "padding": "0",
            "width": "100%",
            "overflow_x": "hidden",
        },
        # Reflex mounts into #app — make sure it's full-width too
        "#app": {"width": "100%", "margin": "0", "padding": "0"},
    }
)
app.add_page(index, route="/", title="Bob Meijer - Google Ads Specialist")
app.add_page(casos_page, route="/casos", title="Casos de Éxito | Bob Meijer")