# We'll piece together different parts of a link to give users a 50% discount
# when signing up with the link.

base = "www.homeflix.com"
coupon = "signup/coupon"
discount = 50
amount = 4

for num in range(amount):
    print(f"{base}/{coupon}/{discount}/{num}")
    print(f"{amount} coupons created")
