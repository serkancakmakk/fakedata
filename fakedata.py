from faker import Faker

faker = Faker()
print(f'Name: {faker.name()}')
print(f'Address: {faker.address()}')
print(f'Country: {faker.country()}')
print(f'Text: {faker.text()}')
