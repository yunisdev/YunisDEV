from readme_py import (
    Section,
    Readme,
    Image,
    Header,
    P,
    bold,
    generate,
    ULi,
    Link
)


class Head(Section):
    have_header = False
    inner = [
        Image(
            alt="Hello World Banner",
            src="https://github.com/YunisDEV/YunisDEV/blob/master/assets/coding.gif?raw=true"
        ),
        Header(
            size=1,
            text="""Hi there, I'm <a href="https://yunisdev.github.io" target="_blank">Yunis Huseynzade</a> <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="25px">"""
        ),
    ]


class AboutMe(Section):
    title = "About me"
    inner = [
        P("I am 17 y.o Web Developer from Azerbaijan🇦🇿"),
        P(bold("Personal Stuffs:")),
        ULi([
            P("👨🏻‍💻 I’m currently working on something cool;"),
            P("💬 Ask me about anything, I am happy to help;"),
            P("📝 I write articles on [medium](https://yunisdev.medium.com/);"),
            P("📫 How to reach me: yunisdev.04@gmail.com;")
        ])
    ]


socialLinks = [
    {
        "logo": {
            "text": "linkedin",
            "style": "for-the-badge",
            "logo": "linkedin",
            "logoColor": "white",
            "backColor": "%230077B5"
        },
        "href": "https://www.linkedin.com/in/yunisdev",
        "alt": "linked-in"
    },
    {
        "logo": {
            "text": "medium",
            "style": "for-the-badge",
            "logo": "medium",
            "logoColor": "white",
            "backColor": "%2312100E"
        },
        "href": "https://yunisdev.medium.com/",
        "alt": "medium"
    },
    {
        "logo": {
            "text": "facebook",
            "style": "for-the-badge",
            "logo": "facebook",
            "logoColor": "white",
            "backColor": "%231877F2"
        },
        "href": "https://www.facebook.com/yunisdev/",
        "alt": "facebook"
    }
]


class ConnectWithMe(Section):
    title = "Connect with me"
    inner = [
        *[Link(f"""<img align="left" alt="{i["alt"]}" src="https://img.shields.io/badge/{i["logo"]["text"]}-{i["logo"]["backColor"]}.svg?&style={i["logo"]["style"]}&logo={i["logo"]["logo"]}&logoColor={i["logo"]["logoColor"]}" />""", i["href"]) for i in socialLinks],
        P("<br/><br/>")
    ]


expertiseBadges = [
    {
        "name": "react",
        "text": "react",
        "style": "for-the-badge",
        "logoColor": "%2361DAFB",
        "backColor": "%2320232a",
    }
]


class Expertise(Section):
    title = "Expertise"
    inner = [
        *[P(f"""<img align="left" alt="{i["name"]}" src="https://img.shields.io/badge/{i["name"]}-{i["backColor"]}.svg?&style={i["style"]}&logo={i["name"]}&logoColor={i["logoColor"]}" />""") for i in expertiseBadges]
    ]


readme = Readme(
    sections=[
        Head(),
        AboutMe(),
        ConnectWithMe(),
        Expertise()
    ],
    have_header=False
)

generate(readme)
