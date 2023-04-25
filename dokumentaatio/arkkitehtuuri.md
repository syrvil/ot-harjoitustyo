# Arkkitehtuurikuvaus

## Alustava luokka-/pakkauskaavio

![Pakkausrakenne](pakkauskaavio.png)

## Sekvenssikaavio: kuvien etsiminen tagilla

```mermaid
sequenceDiagram
  actor User
  participant ImageApp
  participant ImageManager
  User->>ImageApp: click "Search"
  ImageApp->>ImageManager: search_for_tag(tag)
  ImageManager-->>ImageApp: image_list
  ImageApp->>ImageApp: images_clear()
  ImageApp->>ImageApp: update_view()
  ImageApp->>ImageApp: update_image_tagas()
```