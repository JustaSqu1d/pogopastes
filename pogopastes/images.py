def get_pokemon_image(pokemon_species: str) -> str:
    new_pokemon_string = (pokemon_species
                          .lower()
                          .replace(" ", "-")
                          .replace("(", "")
                          .replace(")", "")
                          .replace("alolan", "alola")
                          .replace("hisuian", "hisui")
                          .replace("galarian", "galar")
                          .replace("--", "-")
                          .replace("mega-x", "megax")
                          .replace("mega-y", "megay")
                          )

    match new_pokemon_string:
        case "pikachu-doctor":
            new_pokemon_string = "pikachu"
        case "pikachu-flying-01":
            new_pokemon_string = "pikachu"
        case "pikachu-flying-okinawa":
            new_pokemon_string = "pikachu"
        case "pikachu-gofest-2024-mtiara":
            new_pokemon_string = "pikachu"
        case "pikachu-horizons":
            new_pokemon_string = "pikachu"
        case "pikachu-pop-star":
            new_pokemon_string = "pikachu"
        case "pikachu-rock-star":
            new_pokemon_string = "pikachu"
        case "nidoran-male":
            new_pokemon_string = "nidoranm"
        case "nidoran-female":
            new_pokemon_string = "nidoranf"
        case "mr-mime":
            new_pokemon_string = "mrmime"
        case "mr-mime-galar":
            new_pokemon_string = "mrmime-galar"
        case "mewtwo-a":
            new_pokemon_string = "mewtwo"
        case "ho-oh":
            new_pokemon_string = "hooh"
        case "cherrim-sunny":
            new_pokemon_string = "cherrim-sunshine"
        case "mime-jr":
            new_pokemon_string = "mimejr"
        case "porygon-z":
            new_pokemon_string = "porygonz"
        case "darmanitan-galar-standard":
            new_pokemon_string = "darmanitan-galar"
        case "darmanitan-galar-zen":
            new_pokemon_string = "darmanitan-galarzen"
        case "meowstic-female":
            new_pokemon_string = "meowstic-f"
        case "pumpkaboo-average":
            new_pokemon_string = "pumpkaboo"
        case "gourgeist-average":
            new_pokemon_string = "gourgeist"
        case "zygarde-complete-ten-percent":
            new_pokemon_string = "zygarde-10"
        case "type-null":
            new_pokemon_string = "typenull"
        case "jangmo-o-jangmo-o":
            new_pokemon_string = "jangmoo"
        case "hakamo-o-hakamo-o":
            new_pokemon_string = "hakamoo"
        case "kommo-o-kommo-o":
            new_pokemon_string = "kommoo"
        case "tapu-koko":
            new_pokemon_string = "tapukoko"
        case "tapu-lele":
            new_pokemon_string = "tapulele"
        case "tapu-bulu":
            new_pokemon_string = "tapubulu"
        case "tapu-fini":
            new_pokemon_string = "tapufini"
        case "necrozma-dawn-wings":
            new_pokemon_string = "necrozma-dawnwings"
        case "necrozma-dusk-mane":
            new_pokemon_string = "necrozma-duskmane"
        case "mr-rime":
            new_pokemon_string = "mrrime"
        case "indeedee-male":
            new_pokemon_string = "indeedee"
        case "indeedee-female":
            new_pokemon_string = "indeedee-f"
        case "zacian-crowned-sword":
            new_pokemon_string = "zacian-crowned"
        case "zacian-hero":
            new_pokemon_string = "zacian"
        case "zamazenta-crowned-shield":
            new_pokemon_string = "zamazenta-crowned"
        case "zamazenta-hero":
            new_pokemon_string = "zamazenta"
        case "urshifu-single-strike":
            new_pokemon_string = "urshifu"
        case "urshifu-rapid-strike":
            new_pokemon_string = "urshifu-rapidstrike"
        case "calyrex-ice-rider":
            new_pokemon_string = "calyrex-ice"
        case "calyrex-shadow-rider":
            new_pokemon_string = "calyrex-shadow"
        case "oinkologne-male":
            new_pokemon_string = "oinkologne"
        case "oinkologne-female":
            new_pokemon_string = "oinkologne-f"
        case "greattusk-great-tusk":
            new_pokemon_string = "greattusk"
        case "screamtail-scream-tail":
            new_pokemon_string = "screamtail"
        case "brutebonnet-brute-bonnet":
            new_pokemon_string = "brutebonnet"
        case "fluttermane-flutter-mane":
            new_pokemon_string = "fluttermane"
        case "slitherwing-slither-wing":
            new_pokemon_string = "slitherwing"
        case "sandyshocks-sandy-shocks":
            new_pokemon_string = "sandyshocks"
        case "irontreads-iron-treads":
            new_pokemon_string = "irontreads"
        case "ironbundle-iron-bundle":
            new_pokemon_string = "ironbundle"
        case "ironhands-iron-hands":
            new_pokemon_string = "ironhands"
        case "ironjugulis-iron-jugulis":
            new_pokemon_string = "ironjugulis"
        case "ironmoth-iron-moth":
            new_pokemon_string = "ironmoth"
        case "ironthorns-iron-thorns":
            new_pokemon_string = "ironthorns"
        case "wochien-wo-chien":
            new_pokemon_string = "wochien"
        case "chienpao-chien-pao":
            new_pokemon_string = "chienpao"
        case "tinglu-ting-lu":
            new_pokemon_string = "tinglu"
        case "chiyu-chi-yu":
            new_pokemon_string = "chiyu"
        case "roaringmoon-roaring-moon":
            new_pokemon_string = "roaringmoon"
        case "ironvaliant-iron-valiant":
            new_pokemon_string = "ironvaliant"

    return f"https://play.pokemonshowdown.com/sprites/gen5/{new_pokemon_string}.png"


def get_image_asset(key: str) -> str:
    return f"pogopastes/assets/{key}.png"
