#!/usr/bin/env python
import media
import fresh_tomatoes


rangastalam = media.Jashu("Rangastalam", "Brother Sentiment",
                          "https://bit.ly/2KHHLei",
                          "https://www.youtube.com/embed/sueMmTm-M")
nps = media.Jashu("Naa Peru Surya", "Character",
                  "https://bit.ly/2KF6rUU",
                  "https://www.youtube.com/embed/ZnVIUr_BQSs")
ban = media.Jashu("Bharat Ane Nenu", "Politics",
                  "https://bit.ly/2ITtkXz",
                  "https://www.youtube.com/embed/KMWS5y2gZ6E")
avengers = media.Jashu("Avenegers", "Fantasy",
                       "https://bit.ly/2IztZOy",
                       "https://www.youtube.com/embed/6ZfuNTqbHE8")
ghajinikanth = media.Jashu("Ghajinikanth", "comedy",
                           "https://bit.ly/2rWQLVt",
                           "https://www.youtube.com/embed/M8mCjRbCPIo")

movies = [rangastalam, nps, ban, avengers, ghajinikanth]
fresh_tomatoes.open_movies_page(movies)
