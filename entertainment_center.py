import media
import fresh_tomatoes


Inception = media.MovieTrailer("Inception",
                               "Enter people's dreams and steal their secrets from their subconscious.",
                               "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                               "https://www.youtube.com/watch?v=8hP9D6kZseM")

Interstellar = media.MovieTrailer("Interstellar",
                                  "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable.",
                                  "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                                  "https://www.youtube.com/watch?v=zSWdZVtXT7E")

Lightsout = media.MovieTrailer("Lightsout",
                               "Holding a mysterious attachment to their mother a supernatural entity has returned with a vengeance to torment the entire family.",
                               "http://t1.gstatic.com/images?q=tbn:ANd9GcSuBvXaTtnOIDgv0x3AzmL9MRS4x40-w-4UHV8o5k_nqCu48d72",
                               "https://www.youtube.com/watch?v=6LiKKFZyhRU")

D16 = media.MovieTrailer("D16",
                         "Three college friends run over someone with their car, while returning from a late night party. They manage to get away with the crime; however, five years later, the cop is forced to relive the incident again.",
                         "https://upload.wikimedia.org/wikipedia/en/3/35/Dhuruvangal_Pathinaaru_Poster.jpg",
                         "https://www.youtube.com/watch?v=xpt2jfiL5GY")

Ennu_ninte_moideen = media.MovieTrailer("Ennu_ninte_moideen",
                                        "Moideen, a Muslim, and Kanchanamala, a Hindu, are in love. They unite after a lot of struggles, but both become victims of a hapless fate.",
                                        "http://static.sify.com/cms/image/pjhiOXceahfcf.jpg",
                                        "https://www.youtube.com/watch?v=b_iPKIpiAm0")

Aruvi = media.MovieTrailer("Aruvi",
                           "Aruvi is a gentle yet spirited girl who decides to break bad and rebel against the oppressive forces that has treated her unfairly.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQW6ooTz_ei6uHDFdThWiHThFd6IhoXhZmq5KcxUGadgqwOJtEQ",
                           "https://www.youtube.com/watch?v=jgYYxs_d_bo")



movies = [Inception, Interstellar, Lightsout, D16, Ennu_ninte_moideen, Aruvi]
fresh_tomatoes.open_movies_page(movies)



