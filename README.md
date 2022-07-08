# simple_atm_controller

simple_atm_controller

#### Environment

Python 3.10

#### Run

```bash
python main.py
```

#### Exit

```bash
ctrl + c
```

#### Mock Data

```python
# Card Register
account1 = Account("111-1111111-111", 10000)
account2 = Account("222-2222222-222")
account3 = Account("333-3333333-333", 200)
account4 = Account("444-4444444-444", 1)
account5 = Account("555-5555555-555", 500)

card1 = Card("1111-1111-1111-1111", "1234")
card2 = Card("2222-2222-2222-2222", "5678")
card3 = Card("3333-3333-3333-3333", "1111")
```

#### Implemented Action

- Insert Card
  - registered check
  - suspended check
- PIN Number Check
  - validate pin
  - if the validation pin fails 3 times, suspended the card
- Select Account
  - show account list
  - if there is not have any accounts, go back to the main screen
- See Balance
- Deposit
- Withdraw
