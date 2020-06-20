test_tag_parser_output = {
    "description": "An extended version of the documentary from the series finale of Silicon Valley. #HBO #SiliconValleyHBO Subscribe to HBO on YouTube: https://goo.gl/wtFYd7 Fr...",
    "form": "video",
    "image": "https://i.ytimg.com/vi/ab1H602yc_Y/maxresdefault.jpg",
    "medium": "video_link",
    "title": "Silicon Valley | Ten Years Later: The Extended Pied Piper Documentary | HBO",
    "url": "https://www.youtube.com/watch?v=ab1H602yc_Y",
}

test_get_without_og_twitter_output = {
    "description": "This site is supported by donations to The OEIS Foundation.\n",
    "form": "text",
    "image": "https://i.ibb.co/",
    "medium": "link",
    "title": "List of LaTeX mathematical symbols - OeisWiki",
    "url": "https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols",
}

test_get_params_url_output = {
    "title": "Flash Sale",
    "url": "https://www.creativelive.com/flash-sale",
    "medium": "link",
    "form": "text",
    "image": "https://downloads.creativelive.com/social/Facebook_1600x1227.jpg",
    "description": "photo & video ",
}


test_get_imdb_movie_output = {
    "title": "The Shawshank Redemption (1994) - IMDb",
    "url": "http://www.imdb.com/title/tt0111161/",
    "medium": "film",
    "form": "video",
    "image": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY1200_CR89,0,630,1200_AL_.jpg",
    "description": "Directed by Frank Darabont.  With Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler. Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
}
test_enrich_imdb_movie_output = "The Shawshank Redemption"


test_get_imdb_tv_output = {
    "title": "Game of Thrones (TV Series 2011–2019) - IMDb",
    "url": "http://www.imdb.com/title/tt0944947/",
    "medium": "tv",
    "form": "video",
    "image": "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_UY1200_CR126,0,630,1200_AL_.jpg",
    "description": "Created by David Benioff, D.B. Weiss.  With Emilia Clarke, Peter Dinklage, Kit Harington, Lena Headey. Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
}
test_enrich_imdb_tv_output = "Game of Thrones"


test_get_imdb_person_output = {
    "title": "Christopher Nolan - IMDb",
    "url": "http://www.imdb.com/name/nm0634240/",
    "medium": "link",
    "form": "text",
    "image": "https://m.media-amazon.com/images/M/MV5BNjE3NDQyOTYyMV5BMl5BanBnXkFtZTcwODcyODU2Mw@@._V1_UY1200_CR118,0,630,1200_AL_.jpg",
    "description": "Christopher Nolan, Writer: Interstellar. Best known for his cerebral, often nonlinear, storytelling, acclaimed writer-director Christopher Nolan was born on July 30, 1970, in London, England. Over the course of 15 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made. At 7 years old, Nolan began making short movies ...",
}
test_enrich_imdb_person_output = "Christopher Nolan"


test_get_goodreads_output = {
    "title": "The Bad Beginning (A Series of Unfortunate Events, #1)",
    "url": "https://www.goodreads.com/work/best_book/1069597-the-bad-beginning",
    "medium": "book",
    "form": "text",
    "image": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436737029i/78411._SR1200,630_.jpg",
    "description": "Dear Reader,  I'm sorry to say that the book you are holding in your hands is extremely unpleasant. It tells an unhappy tale about three ...",
}
test_enrich_goodreads_output = "Lemony Snicket"


test_get_wikiart_artwork_output = {
    "title": "The Chess Player, 1876 - Thomas Eakins - WikiArt.org",
    "url": "https://www.wikiart.org/en/thomas-eakins/the-chess-player-1876",
    "medium": "link",
    "form": "text",
    "image": "https://uploads6.wikiart.org/images/thomas-eakins/the-chess-player-1876.jpg!Large.jpg",
    "description": "‘The Chess Player’ was created in 1876 by Thomas Eakins in Realism style. Find more prominent pieces of genre painting at Wikiart.org – best visual art database.",
}
test_enrich_wikiart_artwork_output = {
    "data": [
        {
            "id": "57726f82edc2cb3880bb105d",
            "title": "Chess-Players",
            "url": None,
            "artistUrl": "honore-daumier",
            "artistName": "Honore Daumier",
            "artistId": "57726d7fedc2cb3880b481f6",
            "completitionYear": 1867,
            "width": 750,
            "image": "https://uploads8.wikiart.org/images/honore-daumier/chess-players.jpg!Large.jpg",
            "height": 585,
        },
        {
            "id": "577272a0edc2cb3880c5ebd3",
            "title": "Egyptian Chess Players",
            "url": None,
            "artistUrl": "sir-lawrence-alma-tadema",
            "artistName": "Sir Lawrence Alma-Tadema",
            "artistId": "57726d84edc2cb3880b48a2b",
            "completitionYear": 1865,
            "width": 750,
            "image": "https://uploads1.wikiart.org/images/alma-tadema-lawrence/egyptian-chess-players-1865.jpg!Large.jpg",
            "height": 511,
        },
        {
            "id": "57727661edc2cb3880d14ee1",
            "title": "Portrait of Chess Players",
            "url": None,
            "artistUrl": "marcel-duchamp",
            "artistName": "Marcel Duchamp",
            "artistId": "57726d87edc2cb3880b49292",
            "completitionYear": 1911,
            "width": 573,
            "image": "https://uploads7.wikiart.org/images/marcel-duchamp/portrait-of-chess-players-1911.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "57727663edc2cb3880d150c9",
            "title": "The Chess Players",
            "url": None,
            "artistUrl": "marcel-duchamp",
            "artistName": "Marcel Duchamp",
            "artistId": "57726d87edc2cb3880b49292",
            "completitionYear": 1911,
            "width": 706,
            "image": "https://uploads8.wikiart.org/images/marcel-duchamp/the-chess-players-1911.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "57727903edc2cb3880d9e170",
            "title": "Portrait of chess player A. D.  Petrova",
            "url": None,
            "artistUrl": "grigoriy-myasoyedov",
            "artistName": "Grigoriy Myasoyedov",
            "artistId": "57726d8bedc2cb3880b49aea",
            "completitionYear": None,
            "width": 384,
            "image": "https://uploads8.wikiart.org/images/grigoriy-myasoyedov/portrait-of-chess-player-a-d-petrova.jpg",
            "height": 550,
        },
        {
            "id": "57727e43edc2cb3880ea56d9",
            "title": "Sketch for The Chess Players",
            "url": None,
            "artistUrl": "thomas-eakins",
            "artistName": "Thomas Eakins",
            "artistId": "57726d9aedc2cb3880b4b6e8",
            "completitionYear": None,
            "width": 493,
            "image": "https://uploads4.wikiart.org/images/thomas-eakins/sketch-for-the-chess-players.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "57727e45edc2cb3880ea599c",
            "title": "The Chess Player",
            "url": None,
            "artistUrl": "thomas-eakins",
            "artistName": "Thomas Eakins",
            "artistId": "57726d9aedc2cb3880b4b6e8",
            "completitionYear": 1876,
            "width": 750,
            "image": "https://uploads6.wikiart.org/images/thomas-eakins/the-chess-player-1876.jpg!Large.jpg",
            "height": 544,
        },
        {
            "id": "57728019edc2cb3880f004dd",
            "title": "The Chess Player",
            "url": None,
            "artistUrl": "corneliu-baba",
            "artistName": "Corneliu Baba",
            "artistId": "57726da3edc2cb3880b4c802",
            "completitionYear": 1948,
            "width": 348,
            "image": "https://uploads5.wikiart.org/images/corneliu-baba/the-chess-player-1948.jpg",
            "height": 400,
        },
        {
            "id": "57728380edc2cb3880fabf99",
            "title": "Chess Players",
            "url": None,
            "artistUrl": "ernest-meissonier",
            "artistName": "Ernest Meissonier",
            "artistId": "57726dbbedc2cb3880b4ed63",
            "completitionYear": 1853,
            "width": 750,
            "image": "https://uploads7.wikiart.org/images/ernest-meissonier/chess-players-1853.jpg!Large.jpg",
            "height": 588,
        },
        {
            "id": "577283a6edc2cb3880fb4eef",
            "title": "The Chess Players",
            "url": None,
            "artistUrl": "john-lavery",
            "artistName": "John Lavery",
            "artistId": "57726dbcedc2cb3880b4ef5b",
            "completitionYear": 1929,
            "width": 750,
            "image": "https://uploads5.wikiart.org/images/john-lavery/the-chess-players-1929.jpg!Large.jpg",
            "height": 480,
        },
        {
            "id": "5772842bedc2cb3880fd1a37",
            "title": "Chess Players III",
            "url": None,
            "artistUrl": "willi-baumeister",
            "artistName": "Willi Baumeister",
            "artistId": "57726dc1edc2cb3880b4f87c",
            "completitionYear": 1924,
            "width": 355,
            "image": "https://uploads0.wikiart.org/images/willi-baumeister/chess-players-iii-1924.jpg",
            "height": 451,
        },
        {
            "id": "5772893dedc2cb38800d231b",
            "title": "The Chess Players",
            "url": None,
            "artistUrl": "william-orpen",
            "artistName": "William Orpen",
            "artistId": "57726dfbedc2cb3880b552a2",
            "completitionYear": 1902,
            "width": 464,
            "image": "https://uploads7.wikiart.org/images/william-orpen/the-chess-players-1902.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "5c7f810cedc2c95a04e53552",
            "title": "Chess Player",
            "url": None,
            "artistUrl": "max-oppenheimer",
            "artistName": "Max Oppenheimer",
            "artistId": "5c7bc0f9edc2c911c8eaf361",
            "completitionYear": 1916,
            "width": 576,
            "image": "https://uploads1.wikiart.org/00226/images/max-oppenheimer/chess-player-1916.jpg",
            "height": 450,
        },
    ],
    "paginationToken": "mYYKCPvUlMCe%2bm%2bFr5oqhRUwpA2NgYOK%2fqurC%2bhv3IPFO0G5x7nxRaZ3JcZqONEG2ICeCVS8n78enlsBEi8VqA%3d%3d",
    "hasMore": False,
}


test_get_handleparams_sample = {
    "url": "https://www.google.com/search?sxsrf=ALeKk008Cq1wh8s7ndSr8aRtsSUp9zw1hg:1592632411112",
    "ei": "W6TtXvurBpKuUpOxiOgP",
    "q": "flask travis continuous deployment heroku",
    "oq": "flask travis continuous deployment heroku",
    "gs_lcp": "CgZwc3ktYWIQAzoECCMQJzoGCAAQFhAeOgIIADoFCCEQoAE6BAghEBU6BwghEAoQoAE6CAghEBYQHRAeUPrSB1iVmQhggJsIaABwAHgAgAHjAYgBmSOSAQQyLTIxmAEAoAEBqgEHZ3dzLXdpeg",
    "sclient": "psy-ab",
    "ved": "0ahUKEwi7xfyI2o_qAhUSlxQKHZMYAv0Q4dUDCAw",
    "uact": "5",
}

test_get_handleparams_output = "https://www.google.com/search?sxsrf=ALeKk008Cq1wh8s7ndSr8aRtsSUp9zw1hg:1592632411112&ei=W6TtXvurBpKuUpOxiOgP&q=flask travis continuous deployment heroku&oq=flask travis continuous deployment heroku&gs_lcp=CgZwc3ktYWIQAzoECCMQJzoGCAAQFhAeOgIIADoFCCEQoAE6BAghEBU6BwghEAoQoAE6CAghEBYQHRAeUPrSB1iVmQhggJsIaABwAHgAgAHjAYgBmSOSAQQyLTIxmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwi7xfyI2o_qAhUSlxQKHZMYAv0Q4dUDCAw&uact=5"
