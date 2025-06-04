import os
from faker import Faker

fake = Faker("en_GB")
Faker.seed(28)  # Different seed for different addresses

updates_dir = "data/updates"

#loop through filenames(surnames) from the originals directory
for filename in os.listdir("data/originals"):
    surname = filename
    with open(os.path.join("data/originals", filename), "r", encoding="utf-8") as original_file:
        full_name = original_file.readline().strip()

    updates_file_path = os.path.join(updates_dir, surname)
    with open(updates_file_path, "w", encoding="utf-8") as update_file:
        update_file.write(full_name + "\n")
        updated_address = fake.address().split("\n")
        for line in updated_address:
            update_file.write(line + "\n")
