def remove_highest_cards(cards):
    if not cards:
        return []

    max_card = max(cards)
    filtered_cards = [card for card in cards if card < max_card]
    return filtered_cards

video_cards = [3070, 2060, 3090, 3070, 3090]

print("Старый список видеокарт:", video_cards)
new_video_cards = remove_highest_cards(video_cards)
print("Новый список видеокарт:", new_video_cards)



