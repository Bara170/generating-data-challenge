import os
from faker import Faker

fake = Faker("en_GB")
Faker.seed(17)

output = "data/originals"

used_surnames = []
count = 0

while count < 4:
    first_name = fake.first_name()
    last_name = fake.last_name()

    if last_name in used_surnames:
        continue

    used_surnames.append(last_name)
    full_name = f"{fake.prefix()} {first_name} {last_name}"
    filename = os.path.join(output, f"{last_name}")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(full_name + "\n")
        address_lines = fake.address().split("\n")
        for line in address_lines:
            file.write(line + "\n")

    count += 1
