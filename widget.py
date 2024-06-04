def mask_account_card(info_account_card: str) -> str:
    name_card = ""
    nun_card = ""
    for i in info_account_card:
        if i.isalpha() is True or i == " ":
            name_card = name_card + i
        elif i.isdigit():
            nun_card = nun_card + i
    if name_card == "Счет ":
        return f"{name_card + "**" + nun_card[-4:]}"
    else:
        return f"{name_card}{nun_card[0:4] + " " + nun_card[4:6] + " ** **** " + nun_card[-4:]}"


result2 = mask_account_card("Visa Gold 5999414228426353")
result1 = mask_account_card("Счет 64686473678894779589")
result = mask_account_card("Visa Platinum 8990922113665229")
print(result)
print(result1)
print(result2)
