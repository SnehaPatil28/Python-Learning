import requests


def main():
    print("Simple Currency Coverter!!")

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rate = response.json()["rates"]
        print("Got Rates Successfully!!!")
    except:
        print("Sorry! Coundn't connect to converter API")
        return

    print("Popular: USD EUR GBP JPY AUD INR")

    while True:
        print("Enter details:")
        from_currency = input("From currency code (e.g USD): ").upper()
        if from_currency not in rate:
            print(f"Invalid code : {from_currency}")
            continue

        to_currency = input("To currency code (e.g EUR): ").upper()
        if to_currency not in rate:
            print(f"Invalid code : {to_currency}")

        try:
            amount = float(input(f"Enter amount in {from_currency}: "))
        except:
            print("Please enter valid amount")
            continue

        amount_in_USD = amount / rate[from_currency]
        result = amount_in_USD * rate[to_currency]

        print(
            f"Result : {amount} {from_currency} = {result:.2f} {to_currency}")
        print(
            f"Rate 1 {from_currency} = {rate[to_currency] / rate[from_currency]:.4f} {to_currency}")

        if not input("\n Convert again?").lower().startswith('y'):
            print("GoodBye!!!")
            break


main()
